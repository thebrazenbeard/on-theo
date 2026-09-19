from pathlib import Path
import yaml


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "research/packets/jewish-messiah-expectations-v1.yaml"
PROSE = ROOT / "research/packets/jewish-messiah-expectations-v1.md"

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


def test_packet_is_exact_parent_bound() -> None:
    data = _load()
    assert data["base_subject"]["head"] == "75598bab3d62c25e7d7b05384f0a67856cd3a713"
    anchors = data["base_subject"]["inherited_exact_anchors"]
    assert anchors["second_temple_corpus"] == "7493cdd8f9fb56f388641f3006fb6c62ac81ad00"
    assert anchors["enoch_daniel_philo_corpus"] == "f4c4b4e940a8e6c76e9603d298bab819fbcc448d"


def test_lexical_control_requires_multiple_nonidentical_anointed_roles() -> None:
    data = _load()
    claims = {item["id"]: item for item in data["claims"]}
    claim = claims["CLM-MASHIACH-LEXEME-NOT-ONE-ESCHATOLOGICAL-ROLE"]
    assert claim["confidence"] == "high"
    assert set(claim["supporting_sources"]) == {
        "SRC-LEVITICUS-4-3",
        "SRC-1SAMUEL-24-11",
        "SRC-ISAIAH-45-1",
    }


def test_messianic_diversity_is_preserved() -> None:
    data = _load()
    claims = {item["id"]: item for item in data["claims"]}
    universal = claims["CLM-SECOND-TEMPLE-ONE-UNIVERSAL-MESSIAH-JOB-DESCRIPTION"]
    assert universal["supporting_sources"] == []
    assert len(universal["opposing_sources"]) >= 5
    assert universal["confidence"] == "unresolved"

    q521 = claims["CLM-4Q521-MESSIAH-ROLE"]
    assert q521["contested"] is True
    assert q521["confidence"] == "high-for-role-contestation"


def test_messiah_title_is_not_promoted_to_divine_ontology() -> None:
    data = _load()
    claims = {item["id"]: item for item in data["claims"]}
    divine = claims["CLM-MESSIAH-TITLE-ENTAILS-INCARNATE-DIVINITY"]
    assert divine["supporting_sources"] == []
    assert data["effect_boundary"]["establishes_christian_divine_ontology_from_title_alone"] is False
    text = PROSE.read_text(encoding="utf-8")
    assert "YESHUA_IS_MESSIAH" in text
    assert "YESHUA_IS_GOD_INCARNATE" in text


def test_all_references_resolve_and_evidence_taxonomy_is_valid() -> None:
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


def test_effect_boundary_is_nonpromotional() -> None:
    data = _load()
    assert data["effect_boundary"] == {
        "changes_parent_judaism_claims": False,
        "imports_registry_extension_bytes": False,
        "canonical_promotion": False,
        "merge_authority": False,
        "establishes_universal_second_temple_messiah_profile": False,
        "establishes_yeshua_self_identification": False,
        "establishes_christian_divine_ontology_from_title_alone": False,
    }
    assert all(data["rules"].values())
