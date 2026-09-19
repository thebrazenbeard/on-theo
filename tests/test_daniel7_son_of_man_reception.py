from pathlib import Path
import yaml


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "research/packets/daniel7-son-of-man-reception-v1.yaml"
PROSE = ROOT / "research/packets/daniel7-son-of-man-reception-v1.md"

ALLOWED_EVIDENCE = {
    "PRIMARY_TEXT",
    "MATERIAL_EVIDENCE",
    "HISTORICAL_RECONSTRUCTION",
    "LATER_TRADITION",
    "SCHOLARLY_INTERPRETATION",
    "PROJECT_INFERENCE",
    "SPECULATIVE_MODEL",
    "UNKNOWN",
}


def _load() -> dict:
    data = yaml.safe_load(PACKET.read_text(encoding="utf-8"))
    assert isinstance(data, dict)
    return data


def test_packet_is_exact_parent_and_corpus_bound() -> None:
    data = _load()
    assert data["base_subject"]["head"] == "2cef8b57c51e0da11653a441e3987cd657614f3e"
    assert data["base_subject"]["inherited_exact_anchors"]["enoch_daniel_philo_corpus"] == "f4c4b4e940a8e6c76e9603d298bab819fbcc448d"


def test_daniel_vision_and_interpretation_are_both_preserved() -> None:
    data = _load()
    claims = {item["id"]: item for item in data["claims"]}
    assert claims["CLM-DANIEL7-HUMANLIKE-FIGURE-TEXT"]["confidence"] == "high"
    assert claims["CLM-DANIEL7-HOLY-ONES-INTERPRETATION"]["confidence"] == "high"
    unresolved = claims["CLM-DANIEL7-FIGURE-ORIGINAL-REFERENT"]
    assert unresolved["supporting_sources"] == []
    assert unresolved["confidence"] == "unresolved"
    assert unresolved["contested"] is True


def test_fixed_title_and_universal_doctrine_are_not_promoted() -> None:
    data = _load()
    claims = {item["id"]: item for item in data["claims"]}
    fixed = claims["CLM-DANIEL7-SON-MAN-FIXED-TITLE"]
    universal = claims["CLM-UNIVERSAL-FIRST-CENTURY-SON-MAN-DOCTRINE"]
    assert fixed["supporting_sources"] == []
    assert universal["supporting_sources"] == []
    assert universal["contested"] is True
    assert data["effect_boundary"]["establishes_universal_son_man_doctrine"] is False


def test_later_individualization_does_not_backdate_itself() -> None:
    data = _load()
    claim = next(item for item in data["claims"] if item["id"] == "CLM-LATER-JEWISH-DANIELIC-INDIVIDUALIZATION")
    assert set(claim["supporting_sources"]) >= {
        "SRC-1ENOCH-SIMILITUDES",
        "SRC-4EZRA-13",
        "SCH-SLATER-1995-SON-MAN-FIRST-CENTURY",
    }
    assert "does not determine Daniel 7" in claim["ceiling"]


def test_all_references_resolve_and_taxonomy_is_valid() -> None:
    data = _load()
    declared = {item["id"] for item in data["sources"]}
    declared |= {item["id"] for item in data["scholarly_context"]}

    used = set()
    for section in ("sources", "scholarly_context", "claims"):
        for item in data.get(section, []):
            used.update(item.get("evidence_class", []))
    assert used <= ALLOWED_EVIDENCE, sorted(used - ALLOWED_EVIDENCE)

    for claim in data["claims"]:
        for field in ("supporting_sources", "opposing_sources"):
            for source_id in claim.get(field, []):
                assert source_id in declared, (claim["id"], field, source_id)


def test_gospel_analysis_is_explicitly_deferred() -> None:
    data = _load()
    claim = next(item for item in data["claims"] if item["id"] == "CLM-GOSPEL-SON-MAN-AUTOMATIC-DANIEL7")
    assert claim["supporting_sources"] == []
    assert data["effect_boundary"]["establishes_yeshua_self_designation"] is False
    text = PROSE.read_text(encoding="utf-8")
    assert "Gospel Son of Man requires its own source analysis" in text
