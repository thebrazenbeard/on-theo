from pathlib import Path
import yaml


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "research/packets/noncanonical-witness-control-v1.yaml"
PROSE = ROOT / "research/packets/noncanonical-witness-control-v1.md"

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


def test_noncanonical_packet_is_exact_parent_bound() -> None:
    data = _load()
    assert data["base_subject"]["head"] == "e3a1f08b1e4ffb081f583501140efaf81c650d29"
    assert data["base_subject"]["inherited_control"]["state"] == "EXACT_PARENT_CONTROL"


def test_each_witness_points_to_a_declared_work_and_has_own_date() -> None:
    data = _load()
    works = {item["id"] for item in data["works"]}
    assert len(works) == 4
    for witness in data["witnesses"]:
        assert witness["witness_of"] in works
        date = witness["witness_date"]
        assert set(date) == {"start", "end", "precision"}
        assert date["precision"]


def test_infancy_thomas_preserves_recension_and_version_distinctions() -> None:
    data = _load()
    witnesses = {item["id"]: item for item in data["witnesses"]}
    assert witnesses["WIT-IGT-GS-SABAITICUS-259"]["witness_date"]["precision"] == "eleventh-century"
    assert witnesses["WIT-IGT-LV-VINDOBONENSIS-563"]["witness_date"]["precision"] == "fifth-century"
    assert witnesses["WIT-IGT-SYRIAC-W"]["witness_date"]["precision"] == "sixth-century"
    assert witnesses["WIT-IGT-SYRIAC-G"]["witness_date"]["precision"] == "sixth-century"
    assert witnesses["WIT-IGT-GS-SABAITICUS-259"]["recension"] != witnesses["WIT-IGT-LV-VINDOBONENSIS-563"]["recension"]


def test_gospel_peter_identification_and_fragment_claim_remain_bounded() -> None:
    data = _load()
    claims = {item["id"]: item for item in data["claims"]}
    early = claims["CLM-GOSPEL-PETER-EARLY-FRAGMENTS-AUTOMATIC"]
    assert early["supporting_sources"] == []
    assert early["opposing_sources"] == ["SCH-FOSTER-2006-GOSPEL-PETER-FRAGMENTS"]
    assert early["confidence"] == "unresolved"
    assert early["contested"] is True

    akhmim = next(item for item in data["witnesses"] if item["id"] == "WIT-GOSPEL-PETER-AKHMIM")
    assert akhmim["witness_date"]["start"] == "0600"
    assert akhmim["witness_date"]["end"] == "0899"


def test_all_evidence_ids_resolve_and_use_existing_taxonomy() -> None:
    data = _load()
    declared = {item["id"] for item in data["works"]}
    declared |= {item["id"] for item in data["witnesses"]}
    declared |= {item["id"] for item in data["scholarly_context"]}

    used = set()
    for section in ("works", "scholarly_context", "claims"):
        for item in data.get(section, []):
            used.update(item.get("evidence_class", []))
    assert used <= ALLOWED_EVIDENCE, sorted(used - ALLOWED_EVIDENCE)

    for witness in data["witnesses"]:
        assert witness["witness_of"] in declared
        assert witness["source_basis"] in declared

    for claim in data["claims"]:
        for field in ("supporting_sources", "opposing_sources"):
            for source_id in claim.get(field, []):
                assert source_id in declared, (claim["id"], source_id)


def test_packet_keeps_work_witness_and_canon_status_distinct() -> None:
    data = _load()
    assert all(data["rules"].values())
    assert data["effect_boundary"]["establishes_noncanonical_historical_superiority"] is False
    text = PROSE.read_text(encoding="utf-8")
    assert "WORK_IDENTITY" in text
    assert "PHYSICAL_WITNESS_IDENTITY" in text
    assert "NONCANONICAL" in text
    assert "SUPPRESSED_TRUE" in text
