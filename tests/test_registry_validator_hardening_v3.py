from pathlib import Path

import yaml

from tools.on_theo_registry.validator import validate_repository


def _write_yaml(root: Path, relative: str, data: dict) -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")


def _repo(root: Path) -> None:
    _write_yaml(root, "registry/sources.yaml", {"sources": [{"id": "SRC-A"}]})
    _write_yaml(
        root,
        "registry/claims.yaml",
        {
            "allowed_evidence_classes": ["PRIMARY_TEXT"],
            "claims": [{"id": "CLM-A", "evidence_class": ["PRIMARY_TEXT"]}],
        },
    )
    _write_yaml(root, "registry/concepts.yaml", {"relation_types": [], "concepts": []})
    _write_yaml(root, "registry/transmissions.yaml", {"relation_types": [], "edges": []})
    _write_yaml(
        root,
        "registry/witnesses.yaml",
        {
            "materialization_state": "EXTENSIONS_PENDING",
            "witnesses": [],
            "pending_extension_records": [],
        },
    )
    _write_yaml(
        root,
        "registry/reviews.yaml",
        {
            "allowed_results": ["PASS_EXACT"],
            "execution_provenance_types": ["INDEPENDENT_RUNTIME"],
            "receipts": [],
        },
    )
    _write_yaml(
        root,
        "registry/source-access.yaml",
        {
            "access_states": {"DIGITAL_EDITION": "digital"},
            "records": [{"source_id": "SRC-A", "state": "DIGITAL_EDITION"}],
        },
    )
    _write_yaml(root, "registry/extension-manifest.yaml", {"extensions": []})


def _codes(root: Path) -> set[str]:
    return {finding.code for finding in validate_repository(root).errors}


def test_review_receipts_reject_non_mapping_records(tmp_path: Path) -> None:
    _repo(tmp_path)
    _write_yaml(
        tmp_path,
        "registry/reviews.yaml",
        {
            "allowed_results": ["PASS_EXACT"],
            "execution_provenance_types": ["INDEPENDENT_RUNTIME"],
            "receipts": ["MALFORMED_REVIEW_RECORD"],
        },
    )

    assert "INVALID_RECORD_TYPE" in _codes(tmp_path)


def test_source_access_rejects_non_mapping_records(tmp_path: Path) -> None:
    _repo(tmp_path)
    _write_yaml(
        tmp_path,
        "registry/source-access.yaml",
        {
            "access_states": {"DIGITAL_EDITION": "digital"},
            "records": ["MALFORMED_ACCESS_RECORD"],
        },
    )

    assert "INVALID_RECORD_TYPE" in _codes(tmp_path)


def test_pending_witness_index_rejects_non_mapping_records(tmp_path: Path) -> None:
    _repo(tmp_path)
    _write_yaml(
        tmp_path,
        "registry/witnesses.yaml",
        {
            "materialization_state": "EXTENSIONS_PENDING",
            "witnesses": [],
            "pending_extension_records": ["MALFORMED_PENDING_WITNESS_RECORD"],
        },
    )

    assert "INVALID_RECORD_TYPE" in _codes(tmp_path)


def test_record_container_must_be_list(tmp_path: Path) -> None:
    _repo(tmp_path)
    _write_yaml(
        tmp_path,
        "registry/source-access.yaml",
        {
            "access_states": {"DIGITAL_EDITION": "digital"},
            "records": {"source_id": "SRC-A", "state": "DIGITAL_EDITION"},
        },
    )

    assert "INVALID_RECORD_LIST" in _codes(tmp_path)


def test_extension_additions_reject_non_mapping_records(tmp_path: Path) -> None:
    _repo(tmp_path)
    _write_yaml(
        tmp_path,
        "registry/extensions/example.yaml",
        {
            "schema_version": "on-theo.registry-extension.v1",
            "extension_id": "EXT-A",
            "base_registry_head": "abc",
            "status": "PROPOSED",
            "claim_additions": ["MALFORMED_CLAIM_ADDITION"],
        },
    )
    _write_yaml(
        tmp_path,
        "registry/extension-manifest.yaml",
        {
            "extension_schema_version": "on-theo.registry-extension.v1",
            "extensions": [
                {
                    "extension_id": "EXT-A",
                    "path": "registry/extensions/example.yaml",
                    "declared_base": "abc",
                    "depends_on": [],
                    "status": "PROPOSED",
                    "adds_entity_types": [],
                }
            ],
        },
    )

    assert "INVALID_RECORD_TYPE" in _codes(tmp_path)
