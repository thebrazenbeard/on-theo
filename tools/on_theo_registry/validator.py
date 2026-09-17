from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import yaml


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    level: str
    path: str
    message: str


@dataclass(frozen=True)
class ValidationReport:
    findings: tuple[Finding, ...]

    @property
    def errors(self) -> tuple[Finding, ...]:
        return tuple(item for item in self.findings if item.level == "error")

    @property
    def warnings(self) -> tuple[Finding, ...]:
        return tuple(item for item in self.findings if item.level == "warning")

    @property
    def ok(self) -> bool:
        return not self.errors


class _Validator:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.findings: list[Finding] = []
        self.seen_ids: dict[str, str] = {}
        self.source_ids: set[str] = set()
        self.claim_ids: set[str] = set()
        self.concept_ids: set[str] = set()
        self.witness_ids: set[str] = set()
        self.extensions: list[tuple[dict[str, Any], dict[str, Any], str]] = []

    def finding(self, code: str, path: str, message: str, level: str = "error") -> None:
        self.findings.append(Finding(code=code, level=level, path=path, message=message))

    def load(self, relative: str, *, required: bool = True) -> dict[str, Any]:
        path = self.root / relative
        if not path.exists():
            if required:
                self.finding("MISSING_FILE", relative, "required registry file is missing")
            return {}
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError) as exc:
            self.finding("YAML_LOAD_ERROR", relative, str(exc))
            return {}
        if data is None:
            return {}
        if not isinstance(data, dict):
            self.finding("INVALID_YAML_ROOT", relative, "top-level YAML value must be a mapping")
            return {}
        return data

    def register_id(self, entity_id: Any, path: str, kind: str) -> None:
        if not isinstance(entity_id, str) or not entity_id:
            self.finding("MISSING_ID", path, f"{kind} record is missing a non-empty id")
            return
        previous = self.seen_ids.get(entity_id)
        if previous is not None:
            self.finding("DUPLICATE_ID", path, f"stable id {entity_id!r} already declared at {previous}")
            return
        self.seen_ids[entity_id] = path
        if kind == "source":
            self.source_ids.add(entity_id)
        elif kind == "claim":
            self.claim_ids.add(entity_id)
        elif kind == "concept":
            self.concept_ids.add(entity_id)
        elif kind == "witness":
            self.witness_ids.add(entity_id)

    @staticmethod
    def records(data: dict[str, Any], key: str) -> list[dict[str, Any]]:
        value = data.get(key, [])
        if not isinstance(value, list):
            return []
        return [item for item in value if isinstance(item, dict)]

    def register_base_ids(
        self,
        sources: dict[str, Any],
        claims: dict[str, Any],
        concepts: dict[str, Any],
        transmissions: dict[str, Any],
        witnesses: dict[str, Any],
        reviews: dict[str, Any],
    ) -> None:
        for index, item in enumerate(self.records(sources, "sources")):
            self.register_id(item.get("id"), f"registry/sources.yaml:sources[{index}]", "source")
        for index, item in enumerate(self.records(claims, "claims")):
            self.register_id(item.get("id"), f"registry/claims.yaml:claims[{index}]", "claim")
        for index, item in enumerate(self.records(concepts, "concepts")):
            self.register_id(item.get("id"), f"registry/concepts.yaml:concepts[{index}]", "concept")
        for index, item in enumerate(self.records(transmissions, "edges")):
            self.register_id(item.get("id"), f"registry/transmissions.yaml:edges[{index}]", "transmission")
        for index, item in enumerate(self.records(witnesses, "witnesses")):
            self.register_id(item.get("id"), f"registry/witnesses.yaml:witnesses[{index}]", "witness")
        for index, item in enumerate(self.records(reviews, "receipts")):
            self.register_id(item.get("id"), f"registry/reviews.yaml:receipts[{index}]", "review")

    def load_manifest_extensions(self, manifest: dict[str, Any]) -> None:
        entries = self.records(manifest, "extensions")
        positions: dict[str, int] = {}
        for index, entry in enumerate(entries):
            extension_id = entry.get("extension_id")
            path = f"registry/extension-manifest.yaml:extensions[{index}]"
            if not isinstance(extension_id, str) or not extension_id:
                self.finding("MISSING_EXTENSION_ID", path, "manifest extension entry requires extension_id")
                continue
            if extension_id in positions:
                self.finding("DUPLICATE_EXTENSION_ID", path, f"extension {extension_id!r} is listed more than once")
            else:
                positions[extension_id] = index

        for index, entry in enumerate(entries):
            extension_id = entry.get("extension_id")
            path = f"registry/extension-manifest.yaml:extensions[{index}]"
            if not isinstance(extension_id, str) or not extension_id:
                continue
            for dependency in entry.get("depends_on", []) or []:
                if dependency not in positions:
                    self.finding("UNKNOWN_EXTENSION_DEPENDENCY", path, f"dependency {dependency!r} is not in the manifest")
                elif positions[dependency] >= index:
                    self.finding("MANIFEST_DEPENDENCY_ORDER", path, f"dependency {dependency!r} must precede {extension_id!r}")

            relative = entry.get("path")
            if not isinstance(relative, str) or not relative:
                self.finding("MISSING_EXTENSION_PATH", path, "manifest extension entry requires path")
                continue
            extension = self.load(relative)
            if not extension:
                continue
            actual_id = extension.get("extension_id")
            if actual_id != extension_id:
                self.finding(
                    "MANIFEST_EXTENSION_ID_MISMATCH",
                    relative,
                    f"manifest declares {extension_id!r} but file declares {actual_id!r}",
                )
            declared_base = entry.get("declared_base")
            actual_base = extension.get("base_registry_head")
            if declared_base != actual_base:
                self.finding(
                    "MANIFEST_EXTENSION_BASE_MISMATCH",
                    relative,
                    f"manifest base {declared_base!r} does not match file base {actual_base!r}",
                )
            self.extensions.append((entry, extension, relative))

    def register_extension_ids(self) -> None:
        key_kinds = (
            ("source_additions", "source"),
            ("scholarly_context_additions", "source"),
            ("claim_additions", "claim"),
            ("concept_additions", "concept"),
            ("witness_additions", "witness"),
            ("transmission_additions", "transmission"),
        )
        for _, extension, relative in self.extensions:
            for key, kind in key_kinds:
                for index, item in enumerate(self.records(extension, key)):
                    self.register_id(item.get("id"), f"{relative}:{key}[{index}]", kind)

    def validate_source_reference(self, source_id: Any, path: str) -> None:
        if isinstance(source_id, str) and source_id and source_id not in self.source_ids:
            self.finding("UNKNOWN_SOURCE_REFERENCE", path, f"source_id {source_id!r} does not resolve")

    def validate_witness_reference(self, witness_id: Any, path: str) -> None:
        if isinstance(witness_id, str) and witness_id and witness_id not in self.witness_ids:
            self.finding("UNKNOWN_WITNESS_REFERENCE", path, f"witness_id {witness_id!r} does not resolve")

    def validate_claims(self, claims: Iterable[tuple[dict[str, Any], str]]) -> None:
        for claim, path in claims:
            for edge_key in ("supporting_sources", "opposing_sources"):
                for index, edge in enumerate(self.records(claim, edge_key)):
                    edge_path = f"{path}:{edge_key}[{index}]"
                    self.validate_source_reference(edge.get("source_id"), edge_path)
                    self.validate_witness_reference(edge.get("witness_id"), edge_path)

    def validate_witnesses(self, witnesses: Iterable[tuple[dict[str, Any], str]]) -> None:
        for witness, path in witnesses:
            source_id = witness.get("witness_of")
            if not isinstance(source_id, str) or source_id not in self.source_ids:
                self.finding("UNKNOWN_WITNESS_SOURCE", path, f"witness_of {source_id!r} does not resolve to a source")

    def validate_transmissions(self, edges: Iterable[tuple[dict[str, Any], str]]) -> None:
        for edge, path in edges:
            self.validate_source_reference(edge.get("from_source"), f"{path}:from_source")
            self.validate_source_reference(edge.get("to_source"), f"{path}:to_source")
            for index, evidence in enumerate(self.records(edge, "evidence")):
                self.validate_source_reference(evidence.get("source_id"), f"{path}:evidence[{index}]")

    def validate_concepts(self, concepts: Iterable[tuple[dict[str, Any], str]]) -> None:
        for concept, path in concepts:
            for claim_id in concept.get("linked_claims", []) or []:
                if isinstance(claim_id, str) and claim_id not in self.claim_ids:
                    self.finding("UNKNOWN_CONCEPT_CLAIM", path, f"linked claim {claim_id!r} does not resolve")
            for index, relation in enumerate(self.records(concept, "relations")):
                target = relation.get("target_concept_id")
                if isinstance(target, str) and target not in self.concept_ids:
                    self.finding("UNKNOWN_CONCEPT_TARGET", f"{path}:relations[{index}]", f"target concept {target!r} does not resolve")

    def validate_reviews(self, reviews: dict[str, Any]) -> None:
        allowed = set(reviews.get("allowed_results", []) or [])
        provenance = set(reviews.get("execution_provenance_types", []) or [])
        for index, receipt in enumerate(self.records(reviews, "receipts")):
            path = f"registry/reviews.yaml:receipts[{index}]"
            if receipt.get("result") not in allowed:
                self.finding("INVALID_REVIEW_RESULT", path, f"result {receipt.get('result')!r} is not declared")
            if receipt.get("execution_provenance") not in provenance:
                self.finding(
                    "INVALID_EXECUTION_PROVENANCE",
                    path,
                    f"execution_provenance {receipt.get('execution_provenance')!r} is not declared",
                )

    def validate_source_access(self, source_access: dict[str, Any]) -> None:
        for index, record in enumerate(self.records(source_access, "records")):
            self.validate_source_reference(record.get("source_id"), f"registry/source-access.yaml:records[{index}]")

    def run(self) -> ValidationReport:
        sources = self.load("registry/sources.yaml")
        claims = self.load("registry/claims.yaml")
        concepts = self.load("registry/concepts.yaml")
        transmissions = self.load("registry/transmissions.yaml")
        witnesses = self.load("registry/witnesses.yaml")
        reviews = self.load("registry/reviews.yaml")
        source_access = self.load("registry/source-access.yaml")
        manifest = self.load("registry/extension-manifest.yaml")

        self.register_base_ids(sources, claims, concepts, transmissions, witnesses, reviews)
        self.load_manifest_extensions(manifest)
        self.register_extension_ids()

        claim_records: list[tuple[dict[str, Any], str]] = [
            (item, f"registry/claims.yaml:claims[{index}]")
            for index, item in enumerate(self.records(claims, "claims"))
        ]
        witness_records: list[tuple[dict[str, Any], str]] = [
            (item, f"registry/witnesses.yaml:witnesses[{index}]")
            for index, item in enumerate(self.records(witnesses, "witnesses"))
        ]
        transmission_records: list[tuple[dict[str, Any], str]] = [
            (item, f"registry/transmissions.yaml:edges[{index}]")
            for index, item in enumerate(self.records(transmissions, "edges"))
        ]
        concept_records: list[tuple[dict[str, Any], str]] = [
            (item, f"registry/concepts.yaml:concepts[{index}]")
            for index, item in enumerate(self.records(concepts, "concepts"))
        ]

        for _, extension, relative in self.extensions:
            claim_records.extend(
                (item, f"{relative}:claim_additions[{index}]")
                for index, item in enumerate(self.records(extension, "claim_additions"))
            )
            witness_records.extend(
                (item, f"{relative}:witness_additions[{index}]")
                for index, item in enumerate(self.records(extension, "witness_additions"))
            )
            transmission_records.extend(
                (item, f"{relative}:transmission_additions[{index}]")
                for index, item in enumerate(self.records(extension, "transmission_additions"))
            )
            concept_records.extend(
                (item, f"{relative}:concept_additions[{index}]")
                for index, item in enumerate(self.records(extension, "concept_additions"))
            )

        self.validate_claims(claim_records)
        self.validate_witnesses(witness_records)
        self.validate_transmissions(transmission_records)
        self.validate_concepts(concept_records)
        self.validate_reviews(reviews)
        self.validate_source_access(source_access)

        ordered = tuple(sorted(self.findings, key=lambda item: (item.level, item.code, item.path, item.message)))
        return ValidationReport(findings=ordered)


def validate_repository(root: Path) -> ValidationReport:
    return _Validator(Path(root)).run()
