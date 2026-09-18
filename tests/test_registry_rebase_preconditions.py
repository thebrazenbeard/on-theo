from pathlib import Path

from tools.on_theo_registry.rebase_preconditions import audit_rebase_preconditions


SUBJECT = "d81ab5ab58f326b0827dbc0f9903befb5580947e"


def test_divergent_extension_referential_preconditions_are_equivalent() -> None:
    root = Path(__file__).resolve().parents[1]

    report = audit_rebase_preconditions(root, SUBJECT)

    assert report["extension_count"] == 20
    assert report["ancestor_extension_count"] == 11
    assert report["divergent_extension_count"] == 9
    assert report["divergent_unique_base_count"] == 6
    assert report["referential_precondition_mismatch_count"] == 0, report["mismatches"]
    assert report["referential_preconditions_equivalent"] is True

    divergent = [
        item
        for item in report["extensions"]
        if item["relation"] == "DIVERGED_REBASE_EXCEPTION_REQUIRED"
    ]
    assert len(divergent) == 9
    assert all(item["mismatch_count"] == 0 for item in divergent)
