from __future__ import annotations

import shutil
from pathlib import Path

import yaml

from tools.on_theo_registry.validator import validate_repository


ROOT = Path(__file__).resolve().parents[1]


def _copy_repo(tmp_path: Path) -> Path:
    target = tmp_path / "repo"
    shutil.copytree(
        ROOT,
        target,
        ignore=shutil.ignore_patterns(".git", ".pytest_cache", "__pycache__"),
    )
    return target


def _append_yaml_item(root: Path, relative: str, key: str, item: object) -> None:
    path = root / relative
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert isinstance(data, dict)
    values = data.setdefault(key, [])
    assert isinstance(values, list)
    values.append(item)
    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")


def test_review_receipts_must_not_silently_drop_non_mapping_records(tmp_path: Path) -> None:
    root = _copy_repo(tmp_path)
    _append_yaml_item(root, "registry/reviews.yaml", "receipts", "MALFORMED_REVIEW_RECORD")

    report = validate_repository(root)

    assert not report.ok, "validator silently ignored malformed review receipt"


def test_source_access_must_not_silently_drop_non_mapping_records(tmp_path: Path) -> None:
    root = _copy_repo(tmp_path)
    _append_yaml_item(root, "registry/source-access.yaml", "records", "MALFORMED_ACCESS_RECORD")

    report = validate_repository(root)

    assert not report.ok, "validator silently ignored malformed source-access record"


def test_pending_witness_index_must_not_silently_drop_non_mapping_records(tmp_path: Path) -> None:
    root = _copy_repo(tmp_path)
    _append_yaml_item(
        root,
        "registry/witnesses.yaml",
        "pending_extension_records",
        "MALFORMED_PENDING_WITNESS_RECORD",
    )

    report = validate_repository(root)

    assert not report.ok, "validator silently ignored malformed pending-witness record"
