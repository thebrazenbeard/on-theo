from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "research/packets/jubilees-mastema-passage-witness-inventory-v1.yaml"
PROSE = ROOT / "research/packets/jubilees-mastema-passage-witness-inventory-v1.md"

def _load():
    data = yaml.safe_load(PACKET.read_text(encoding="utf-8"))
    assert isinstance(data, dict)
    return data

def test_exact_parent_and_named_passage_count():
    data = _load()
    assert data["base_subject"]["head"] == "8a61302fb7c6565a11a4fe10ea9523e6e9672a59"
    passages = data["named_mastema_passages"]
    assert len(passages) == 12
    ids = [p["id"] for p in passages]
    assert len(ids) == len(set(ids))
    assert {p["ref"] for p in passages} == {
        "Jubilees 10:8", "Jubilees 11:5", "Jubilees 11:11",
        "Jubilees 17:16", "Jubilees 18:9", "Jubilees 18:12",
        "Jubilees 19:28", "Jubilees 48:2", "Jubilees 48:9",
        "Jubilees 48:12", "Jubilees 48:15", "Jubilees 49:2",
    }

def test_contextual_satan_bridge_is_not_promoted_to_global_identity():
    data = _load()
    assert data["contextual_lexical_bridges"] == [{
        "id": "JUB-SATAN-10-11",
        "ref": "Jubilees 10:11",
        "relation_to_mastema": "IMMEDIATE_CONTEXTUAL_COREFERENCE_STRONG",
        "classification": "CONTEXTUAL_LEXICAL_BRIDGE",
        "caveat": "Ethiopic article/proper-name interpretation is uncertain; do not generalize all satan language to Mastema.",
    }]
    assert data["effect_boundary"]["equates_all_satan_language_with_mastema"] is False

def test_complete_geez_witness_and_latin_range_are_bounded():
    data = _load()
    witnesses = {w["id"]: w for w in data["direct_witnesses"]}
    mastema_ids = {p["id"] for p in data["named_mastema_passages"]}
    assert set(witnesses["WIT-JUB-ETH-BL-OR485"]["coverage"]["mastema_passage_ids"]) == mastema_ids
    assert witnesses["WIT-JUB-LATIN-C73INF"]["coverage"]["mastema_passage_ids"] == ["JUB-MASTEMA-48-2"]
    assert witnesses["WIT-JUB-LATIN-C73INF"]["date"]["precision"] == "fifth-century"

def test_direct_qumran_jubilees_coverage_does_not_fake_mastema_attestation():
    data = _load()
    q = data["direct_hebrew_qumran_jubilees_manuscripts"]
    assert len(q) == 15
    assert all(item["named_mastema_coverage"] == [] for item in q)
    assert any(item["siglum"] == "4Q222" and "Jubilees 48:5" in item["coverage"] for item in q)
    assert any(item["siglum"] == "2Q20" and "Jubilees 46:1-3" in item["coverage"] for item in q)
    assert data["effect_boundary"]["infers_original_absence_from_qumran_gap"] is False

def test_4q225_is_related_ancient_hebrew_not_direct_jubilees_manuscript():
    data = _load()
    w = data["related_hebrew_witnesses"][0]
    assert w["id"] == "WIT-4Q225-PSEUDOJUBILEES"
    assert w["direct_jubilees_manuscript"] is False
    assert len(w["mastema_passages"]) == 4
    assert data["effect_boundary"]["treats_4q225_as_direct_jubilees_manuscript"] is False

def test_inventory_claim_references_resolve():
    data = _load()
    passage_ids = {p["id"] for p in data["named_mastema_passages"]}
    for claim in data["claims"]:
        for ref in claim.get("support", []):
            assert ref in passage_ids, (claim["id"], ref)

def test_prose_keeps_witness_asymmetry_explicit():
    text = PROSE.read_text(encoding="utf-8")
    assert "do **not** include the twelve named Mastema loci" in text
    assert "not catalogued here as a manuscript of the Book of Jubilees" in text
    assert "fifth-century Latin palimpsest" in text
    assert "late physical manuscript date" in text
