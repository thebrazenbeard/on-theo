from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "research/packets/qumran-belial-passage-witness-inventory-v1.yaml"
PROSE = ROOT / "research/packets/qumran-belial-passage-witness-inventory-v1.md"

def _load():
    data = yaml.safe_load(PACKET.read_text(encoding="utf-8"))
    assert isinstance(data, dict)
    return data

def test_exact_parent_and_current_lexical_control():
    data = _load()
    assert data["base_subject"]["head"] == "80c4fc3f359e7838f6c112267c59ca38fbe46289"
    lc = data["lexical_control"]
    assert lc["version"] == "1.3.0"
    assert lc["publication_date"] == "2026-05-21"

def test_personified_loci_are_unique_and_multicorpus():
    data = _load()
    loci = data["personified_loci"]
    ids = [x["id"] for x in loci]
    assert len(ids) == len(set(ids))
    assert len(loci) >= 35
    witnesses = {x["witness"] for x in loci}
    assert {"1QS", "1QM", "CD", "4Q174", "11Q13"} <= witnesses

def test_abstract_examples_are_excluded_from_personified_inventory():
    data = _load()
    locus_pairs = {(x["witness"], x["ref"]) for x in data["personified_loci"]}
    assert ("1QS", "10:21") not in locus_pairs
    assert ("4Q398", "frg. 14-17 ii,5") not in locus_pairs
    assert data["effect_boundary"]["promotes_abstract_belial_to_person"] is False

def test_mstm_bridge_is_real_but_identity_is_blocked():
    data = _load()
    bridge = data["bridge_features"][0]
    assert bridge["locus_id"] == "BEL-1QM-13-10-11"
    assert bridge["hebrew_feature"] == "מלאך משטמה"
    assert bridge["identity_inference"] == "NOT_ESTABLISHED"
    assert bridge["direct_parallel_witness"] == "4Q495 frg. 2,3"
    assert data["effect_boundary"]["equates_belial_with_mastema"] is False

def test_all_witness_locus_references_resolve():
    data = _load()
    locus_ids = {x["id"] for x in data["personified_loci"]}
    for witness in data["physical_and_textual_witnesses"]:
        for locus_id in witness.get("direct_personified_loci", []):
            assert locus_id in locus_ids, (witness["id"], locus_id)
        for p in witness.get("qumran_parallels", []):
            if "locus_id" in p:
                assert p["locus_id"] in locus_ids

def test_cd_is_not_silently_retyped_as_qumran_physical_manuscript():
    data = _load()
    cd = next(x for x in data["physical_and_textual_witnesses"] if x["id"] == "WIT-CD")
    assert cd["kind"] == "MEDIEVAL_CAIRO_TEXTUAL_WITNESS_WITH_QUMRAN_PARALLELS"
    assert {x["siglum"] for x in cd["qumran_parallels"]} == {"4Q266", "4Q271"}

def test_no_identity_overpromotion():
    data = _load()
    boundary = data["effect_boundary"]
    assert boundary["equates_belial_with_mastema"] is False
    assert boundary["equates_belial_with_satan"] is False
    assert boundary["equates_belial_with_watchers"] is False
    text = PROSE.read_text(encoding="utf-8")
    assert "BELIAL_LEXEME_HIT != PERSONIFIED_BELIAL" in text
    assert "does not by itself prove" in text
