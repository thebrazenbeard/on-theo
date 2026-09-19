from pathlib import Path
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]
LOCK = ROOT / "traditions/judaism/provenance-lock-v1.yaml"
CONTROL = ROOT / "traditions/judaism/PROVENANCE_AND_SOURCE_LAYER_CONTROL_V1.md"
HEX40 = re.compile(r"^[0-9a-f]{40}$")

EXPECTED_MODULES = {
    "second-temple-context",
    "concepts-before-christianity",
    "yeshua-in-the-mess",
    "paternity-panthera-countertraditions",
    "sources",
}

EXPECTED_SUBJECTS = {
    "corpus-second-temple-greco-roman",
    "corpus-enoch-daniel-philo",
    "early-christian-rabbinic",
    "yeshua-hypothesis-map",
    "yeshua-hypothesis-map-hostile-review",
    "celsus-jew-source-provenance",
    "panthera-parthenos-wordplay",
    "panthera-rabbinic-parallels",
    "mark6-matronymic",
    "john8-41-porneia",
    "porneia-semantic-control",
}


def _load() -> dict:
    data = yaml.safe_load(LOCK.read_text(encoding="utf-8"))
    assert isinstance(data, dict)
    return data


def test_judaism_subject_and_modules_are_exact_bound() -> None:
    data = _load()
    subject = data["audited_subject"]
    assert subject["head"] == "74492647fc76cb56574c8dda0cdaebc142399482"
    assert subject["tree"] == "c13e0724756fc25dbd82f63b0174cced2c9b5e97"
    assert HEX40.fullmatch(subject["head"])
    modules = {item["id"]: item for item in data["module_inventory"]}
    assert set(modules) == EXPECTED_MODULES
    assert all((ROOT / item["path"]).is_file() for item in modules.values())


def test_research_subjects_are_exact_and_review_is_not_inflated() -> None:
    data = _load()
    subjects = {item["id"]: item for item in data["research_subjects"]}
    assert set(subjects) == EXPECTED_SUBJECTS
    assert all(HEX40.fullmatch(item["head"]) for item in subjects.values())
    assert subjects["yeshua-hypothesis-map-hostile-review"]["qualification"] == "PASS_WITH_LIMITATIONS_SAME_RUNTIME_ROLE_PASS"
    assert data["method_contract"]["rules"]["same_runtime_role_review_is_not_independent_review"] is True


def test_judaism_control_keeps_internal_plurality_and_semantic_limits() -> None:
    data = _load()
    rules = data["method_contract"]["rules"]
    assert rules["preserve_internal_jewish_plurality"] is True
    assert rules["conceptual_availability_does_not_imply_universal_belief"] is True
    text = CONTROL.read_text(encoding="utf-8")
    for marker in (
        "ANOINTED/MESSIANIC_TITLE != GOD_INCARNATE",
        "GEHENNA != AUTOMATICALLY_MEDIEVAL_CHRISTIAN_HELL",
        "JOB_HA_SATAN != EVERY_LATER_SATAN_ONTOLOGY",
        "HISTORICAL_YESHUA != FOUNDER_OF_FULLY_DEVELOPED_LATER_CHRISTIANITY",
    ):
        assert marker in text


def test_no_import_or_claim_promotion_occurs() -> None:
    data = _load()
    assert data["effect_boundary"] == {
        "imports_research_branch_bytes": False,
        "changes_existing_historical_claims": False,
        "canonical_promotion": False,
        "merge_authority": False,
    }
    ceilings = "\n".join(data["claim_ceiling"])
    assert "Panthera/Pandera textual traditions do not establish" in ceilings
    assert "Late rabbinic texts" in ceilings
