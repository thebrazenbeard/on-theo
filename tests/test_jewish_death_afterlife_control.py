from pathlib import Path
import yaml


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "research/packets/jewish-death-afterlife-control-v1.yaml"
PROSE = ROOT / "research/packets/jewish-death-afterlife-control-v1.md"

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
    assert data["base_subject"]["head"] == "aca04ed902091149e9ebb0e8a900bc1709fb8589"
    assert data["base_subject"]["inherited_exact_anchors"] == {
        "second_temple_corpus": "7493cdd8f9fb56f388641f3006fb6c62ac81ad00",
        "enoch_daniel_philo_corpus": "f4c4b4e940a8e6c76e9603d298bab819fbcc448d",
    }


def test_core_non_equivalences_are_enforced() -> None:
    data = _load()
    assert all(data["rules"].values())
    text = PROSE.read_text(encoding="utf-8")
    for marker in (
        "SHEOL != GEHENNA",
        "RESURRECTION != IMMORTAL_SOUL",
        "VALLEY_OF_HINNOM != AUTOMATIC_LATER_HELL",
        "ONE_JEWISH_AFTERLIFE_MODEL != SECOND_TEMPLE_DIVERSITY",
    ):
        assert marker in text


def test_daniel_resurrection_is_high_confidence_but_not_universalized() -> None:
    data = _load()
    claim = next(item for item in data["claims"] if item["id"] == "CLM-DANIEL12-RESURRECTION")
    assert claim["confidence"] == "high"
    assert "not silently expanded" in claim["ceiling"]


def test_diversity_claim_has_multiple_source_types() -> None:
    data = _load()
    claims = {item["id"]: item for item in data["claims"]}
    diverse = claims["CLM-SECOND-TEMPLE-RESURRECTION-AND-SOUL-MODELS-DIVERSE"]
    assert set(diverse["supporting_sources"]) >= {
        "SRC-DANIEL-12-2-3",
        "SRC-2MACCABEES-7",
        "SRC-4MACCABEES",
    }
    linear = claims["CLM-SHEOL-GEHENNA-RESURRECTION-ONE-LINEAR-LADDER"]
    assert linear["supporting_sources"] == []
    assert linear["confidence"] == "unresolved"


def test_all_references_resolve_and_taxonomy_is_valid() -> None:
    data = _load()
    declared = {item["id"] for item in data["sources"]}
    declared |= {item["id"] for item in data["scholarly_context"]}

    used = set()
    for section in ("sources", "scholarly_context", "claims"):
        for item in data.get(section, []):
            used.update(item.get("evidence_class", []))
    assert used <= ALLOWED_EVIDENCE, sorted(used - ALLOWED_EVIDENCE)

    for source in data["sources"]:
        via = source.get("access", {}).get("via_scholarship")
        if via:
            assert via in declared, (source["id"], via)

    for claim in data["claims"]:
        for field in ("supporting_sources", "opposing_sources"):
            for source_id in claim.get(field, []):
                assert source_id in declared, (claim["id"], field, source_id)


def test_effect_boundary_rejects_systematic_overpromotion() -> None:
    data = _load()
    assert data["effect_boundary"] == {
        "changes_parent_daniel_packet": False,
        "changes_existing_judaism_claims": False,
        "canonical_promotion": False,
        "merge_authority": False,
        "establishes_one_jewish_afterlife_model": False,
        "establishes_one_fixed_gehenna_model": False,
        "equates_resurrection_with_immortal_soul": False,
    }
