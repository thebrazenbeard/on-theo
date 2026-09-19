from pathlib import Path
import re

import yaml


ROOT = Path(__file__).resolve().parents[1]
LOCK = ROOT / "synthesis/input-lock-v1.yaml"
GATE = ROOT / "synthesis/COMPARISON_ELIGIBILITY_GATE_V1.md"

HEX40 = re.compile(r"^[0-9a-f]{40}$")


def _load_lock() -> dict:
    data = yaml.safe_load(LOCK.read_text(encoding="utf-8"))
    assert isinstance(data, dict)
    return data


def test_synthesis_input_lock_binds_exact_heads() -> None:
    data = _load_lock()
    subject = data["synthesis_subject"]
    assert subject["branch"] == "synthesis/commonality"
    assert HEX40.fullmatch(subject["head"])
    assert HEX40.fullmatch(subject["tree"])

    existing = {item["id"]: item for item in data["existing_synthesis_inputs"]}
    assert set(existing) == {"judaism", "christianity", "islam", "chronology"}
    assert all(HEX40.fullmatch(item["head"]) for item in existing.values())


def test_new_master_lanes_are_not_auto_admitted() -> None:
    data = _load_lock()
    available = {item["id"]: item for item in data["available_additional_master_lanes"]}
    assert set(available) == {
        "sumerian",
        "buddhism",
        "hindu",
        "shinto",
        "daoism",
        "norse_asatru",
    }
    assert all(item["comparison_eligibility"] == "NOT_YET_ASSERTED" for item in available.values())
    assert all(HEX40.fullmatch(item["head"]) for item in available.values())


def test_comparison_gate_keeps_nonflattening_controls() -> None:
    data = _load_lock()
    assert all(data["rules"].values())
    text = GATE.read_text(encoding="utf-8")
    for gate in range(1, 10):
        assert f"### G{gate} " in text
    assert "STRUCTURAL_SIMILARITY" in text
    assert "HISTORICAL_LINEAGE" in text
    assert "NO_HIT_IN_CURRENT_SEARCH" in text
    assert "HISTORICAL_ABSENCE" in text
