from pathlib import Path
import re

import yaml


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "research/packets/mary-magdalene-authority-reception-v1.yaml"
PROSE = ROOT / "research/packets/mary-magdalene-authority-reception-v1.md"

HEX40 = re.compile(r"^[0-9a-f]{40}$")


def _load() -> dict:
    data = yaml.safe_load(PACKET.read_text(encoding="utf-8"))
    assert isinstance(data, dict)
    return data


def test_packet_binds_exact_parent_and_separates_work_from_witnesses() -> None:
    data = _load()
    assert data["base_subject"]["head"] == "04bf5c56927417567b23732b5e5d5e1fbc02cb24"
    assert HEX40.fullmatch(data["base_subject"]["head"])

    work_ids = {item["id"] for item in data["works"]}
    witness_ids = {item["id"] for item in data["witnesses"]}
    assert "SRC-GOSPEL-MARY" in work_ids
    assert witness_ids == {
        "WIT-GOSPEL-MARY-POXY-3525",
        "WIT-GOSPEL-MARY-PRYL-463",
        "WIT-GOSPEL-MARY-BG-8502",
    }
    assert all(item["witness_of"] == "SRC-GOSPEL-MARY" for item in data["witnesses"])


def test_gospel_of_mary_identity_and_historical_conflict_remain_contested() -> None:
    data = _load()
    claims = {item["id"]: item for item in data["claims"]}

    identity = claims["CLM-GOSPEL-MARY-MARY-IS-MAGDALENE"]
    assert identity["contested"] is True
    assert identity["opposing_sources"]

    conflict = claims["CLM-GOSPEL-MARY-PETER-CONFLICT-IS-HISTORICAL-SUCCESSION"]
    assert conflict["confidence"] == "unresolved"
    assert conflict["contested"] is True


def test_reception_does_not_promote_suppression_motive() -> None:
    data = _load()
    claims = {item["id"]: item for item in data["claims"]}

    gregory = claims["CLM-GREGORY-591-COMPOSITE-MARY"]
    assert gregory["claim_type"] == "RECEPTION_HISTORY"
    assert gregory["confidence"] == "high"

    suppression = claims["CLM-COORDINATED-SUPPRESSION-OF-MARY"]
    assert suppression["supporting_sources"] == []
    assert suppression["confidence"] == "unresolved"
    assert suppression["contested"] is True

    assert data["effect_boundary"]["establishes_coordinated_suppression_motive"] is False


def test_packet_preserves_three_layer_and_witness_date_controls() -> None:
    data = _load()
    gospel_mary = next(item for item in data["works"] if item["id"] == "SRC-GOSPEL-MARY")
    assert gospel_mary["physical_witness_date"]["precision"] == "see-witness-records"

    bg = next(item for item in data["witnesses"] if item["id"] == "WIT-GOSPEL-MARY-BG-8502")
    assert "disagreement" in bg["witness_date"]["precision"]

    text = PROSE.read_text(encoding="utf-8")
    assert "CANONICAL_TEXTUAL_ROLE" in text
    assert "LATER_NONCANONICAL_AUTHORITY_CONSTRUCTION" in text
    assert "MOTIVE_CLAIM" in text
    assert "NONE_ESTABLISHED / MOTIVE_UNRESOLVED" in text

def test_packet_uses_only_branch_evidence_classes() -> None:
    data = _load()
    allowed = {
        "PRIMARY_TEXT",
        "MATERIAL_EVIDENCE",
        "HISTORICAL_RECONSTRUCTION",
        "LATER_TRADITION",
        "SCHOLARLY_INTERPRETATION",
        "PROJECT_INFERENCE",
        "SPECULATIVE_MODEL",
        "UNKNOWN",
    }
    used = set()
    for section in ("works", "scholarly_context", "claims"):
        for item in data.get(section, []):
            used.update(item.get("evidence_class", []))
    assert used <= allowed, sorted(used - allowed)

def test_all_evidence_references_resolve_inside_packet() -> None:
    data = _load()
    declared = {item["id"] for item in data["works"]}
    declared |= {item["id"] for item in data["scholarly_context"]}
    declared |= {item["id"] for item in data["witnesses"]}

    for witness in data["witnesses"]:
        assert witness["witness_of"] in declared

    for claim in data["claims"]:
        for field in ("supporting_sources", "opposing_sources"):
            for source_id in claim.get(field, []):
                assert source_id in declared, (claim["id"], field, source_id)

    for edge in data["transmissions"]:
        for source_id in edge.get("from_sources", []):
            assert source_id in declared, (edge["id"], source_id)
        if edge.get("to_source"):
            assert edge["to_source"] in declared, (edge["id"], edge["to_source"])
