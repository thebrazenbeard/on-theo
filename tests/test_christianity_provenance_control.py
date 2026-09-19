from pathlib import Path
import re

import yaml


ROOT = Path(__file__).resolve().parents[1]
LOCK = ROOT / "traditions/christianity/provenance-lock-v1.yaml"
CONTROL = ROOT / "traditions/christianity/PROVENANCE_AND_SOURCE_LAYER_CONTROL_V1.md"

HEX40 = re.compile(r"^[0-9a-f]{40}$")

EXPECTED_MODULES = {
    "earliest-layers",
    "birth-paternity-and-infancy",
    "christology-development",
    "mary-magdalene-and-authority",
    "noncanonical-and-gnostic-adjacent",
    "sources",
}

EXPECTED_RESEARCH_SUBJECTS = {
    "yeshua-hypothesis-map",
    "yeshua-hypothesis-map-hostile-review",
    "celsus-jew-source-provenance",
    "mark6-matronymic",
    "john8-41-porneia",
    "panthera-parthenos-wordplay",
    "panthera-rabbinic-parallels",
    "porneia-semantic-control",
    "early-christian-rabbinic",
    "corpus-enoch-daniel-philo",
    "corpus-second-temple-greco-roman",
}


def _load() -> dict:
    data = yaml.safe_load(LOCK.read_text(encoding="utf-8"))
    assert isinstance(data, dict)
    return data


def test_christianity_subject_is_exact_head_bound() -> None:
    data = _load()
    subject = data["audited_subject"]
    assert subject["branch"] == "tradition/christianity"
    assert subject["head"] == "38132a768c754e180a9f8a2bb50bf81b6c13719e"
    assert subject["tree"] == "869230c7e2b1e1fb6e180e42ddeb310da7a2cb75"
    assert HEX40.fullmatch(subject["head"])
    assert HEX40.fullmatch(subject["tree"])


def test_all_christianity_modules_have_maturity_state_and_existing_path() -> None:
    data = _load()
    modules = {item["id"]: item for item in data["module_inventory"]}
    assert set(modules) == EXPECTED_MODULES
    for item in modules.values():
        assert (ROOT / item["path"]).is_file()
        assert isinstance(item["state"], str) and item["state"]
        assert isinstance(item["evidence_layers"], list) and item["evidence_layers"]
        assert isinstance(item["limitation"], str) and item["limitation"]


def test_research_anchors_are_exact_and_review_independence_is_not_inflated() -> None:
    data = _load()
    subjects = {item["id"]: item for item in data["research_subjects"]}
    assert set(subjects) == EXPECTED_RESEARCH_SUBJECTS
    assert all(HEX40.fullmatch(item["head"]) for item in subjects.values())
    hostile = subjects["yeshua-hypothesis-map-hostile-review"]
    assert hostile["qualification"] == "PASS_WITH_LIMITATIONS_SAME_RUNTIME_ROLE_PASS"
    assert data["method_contract"]["rules"]["same_runtime_role_review_is_not_independent_review"] is True


def test_control_preserves_claim_ceilings_and_non_import_boundary() -> None:
    data = _load()
    assert data["effect_boundary"] == {
        "imports_research_branch_bytes": False,
        "changes_existing_historical_claims": False,
        "canonical_promotion": False,
        "merge_authority": False,
    }
    text = CONTROL.read_text(encoding="utf-8")
    assert "Textual occurrence" in "\n".join(data["claim_ceiling"])
    assert "CONCEPTUAL_AVAILABILITY != EARLIEST_COMMUNITY_SIMULTANEOUS_USE" in text
    assert "SAME_RUNTIME_ROLE_PASS" in text
    assert "provenance bridge only" in text
