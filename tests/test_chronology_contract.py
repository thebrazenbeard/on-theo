from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
ENTRIES_PATH = ROOT / "chronology/entries.yaml"

ALLOWED_CLASSIFICATIONS = {
    "POLITICAL_HISTORY",
    "MATERIAL_EVIDENCE",
    "TEXT_COMPOSITION",
    "CLAIMED_EVENT",
    "TRADITION_DEVELOPMENT",
    "DOCTRINAL_FORMULATION",
    "RECEPTION_HISTORY",
    "HISTORICAL_RECONSTRUCTION",
    "PRIMARY_TEXT",
    "LATER_TRADITION",
    "TEXTUAL_TRANSMISSION",
    "SPECULATIVE_MODEL",
    "PROJECT_INFERENCE",
}

CLOCK_FIELDS = (
    "claimed_event_date",
    "source_date",
    "physical_witness_date",
)


def _load_entries() -> list[dict]:
    document = yaml.safe_load(ENTRIES_PATH.read_text(encoding="utf-8"))
    assert isinstance(document, dict)
    entries = document.get("entries")
    assert isinstance(entries, list)
    return entries


def test_chronology_entry_ids_are_unique() -> None:
    entries = _load_entries()
    ids = [entry.get("id") for entry in entries]
    assert all(isinstance(entry_id, str) and entry_id for entry_id in ids)
    assert len(ids) == len(set(ids))


def test_chronology_entries_expose_all_three_clocks() -> None:
    for entry in _load_entries():
        for field in CLOCK_FIELDS:
            clock = entry.get(field)
            assert isinstance(clock, dict), (entry.get("id"), field)
            assert set(clock) == {"start", "end", "precision"}, (entry.get("id"), field)
            assert isinstance(clock.get("precision"), str) and clock["precision"]


def test_chronology_classifications_are_documented() -> None:
    for entry in _load_entries():
        classifications = entry.get("classification")
        assert isinstance(classifications, list) and classifications
        unknown = set(classifications) - ALLOWED_CLASSIFICATIONS
        assert not unknown, (entry.get("id"), sorted(unknown))
