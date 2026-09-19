from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / "research/packets/hostile-powers-transmission-map-v1.yaml"
PROSE = ROOT / "research/packets/hostile-powers-transmission-map-v1.md"
MASTEMA = ROOT / "research/packets/jubilees-mastema-passage-witness-inventory-v1.yaml"
BELIAL = ROOT / "research/packets/qumran-belial-passage-witness-inventory-v1.yaml"

def _load(path):
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert isinstance(data, dict)
    return data

def test_map_is_exact_bound_to_both_inventories():
    data = _load(MAP)
    assert data["base_subject"]["head"] == "e7ea73a00fd1fccfba715cee9a8e2a1d33712c12"
    assert data["prerequisite_subjects"]["mastema_inventory"] == "80c4fc3f359e7838f6c112267c59ca38fbe46289"
    assert data["prerequisite_subjects"]["belial_inventory"] == "e7ea73a00fd1fccfba715cee9a8e2a1d33712c12"

def test_all_edge_nodes_and_relations_resolve():
    data = _load(MAP)
    node_ids = {n["id"] for n in data["nodes"]}
    allowed = set(data["allowed_relation_types"])
    edge_ids = set()
    for edge in data["edges"]:
        assert edge["id"] not in edge_ids
        edge_ids.add(edge["id"])
        assert edge["from"] in node_ids
        assert edge["to"] in node_ids
        assert edge["relation"] in allowed
        assert edge["direct_identity"] is False
        assert edge["scope_limit"]

def test_inventory_references_resolve_to_frozen_packets():
    data = _load(MAP)
    mastema = _load(MASTEMA)
    belial = _load(BELIAL)
    mastema_ids = {p["id"] for p in mastema["named_mastema_passages"]}
    mastema_ids |= {p["id"] for p in mastema["contextual_lexical_bridges"]}
    belial_ids = {p["id"] for p in belial["personified_loci"]}
    witness_ids = {w["id"] for w in mastema["related_hebrew_witnesses"]}

    for node in data["nodes"]:
        if node["id"] in {"HP-JUB-MASTEMA", "HP-JUB-SATAN-10-11"}:
            assert set(node["inventory_ids"]) <= mastema_ids
        if node["id"] == "HP-4Q225-MASTEMA":
            assert node["witness_id"] in witness_ids

    for edge in data["edges"]:
        refs = edge.get("evidence_refs", {})
        for x in refs.get("mastema_inventory", []):
            assert x in mastema_ids, (edge["id"], x)
        if "belial_locus" in refs:
            assert refs["belial_locus"] in belial_ids, (edge["id"], refs["belial_locus"])

def test_map_contains_required_strong_and_bounded_edges():
    data = _load(MAP)
    edges = {e["id"]: e for e in data["edges"]}
    assert edges["EDGE-ENOCH-JUB-DEMON-COMPLEX"]["relation"] == "LITERARY_REWRITING_STRONGLY_SUPPORTED"
    assert edges["EDGE-JUB-AKEDAH-4Q225"]["relation"] == "RELATED_TEXTUAL_DEPENDENCE_STRONGLY_SUPPORTED"
    assert edges["EDGE-JUB-MASTEMA-SATAN-10-11"]["relation"] == "CONTEXTUAL_COREFERENCE_STRONG"
    assert edges["EDGE-JUB-MASTEMA-QUMRAN-BELIAL"]["relation"] == "LEXICAL_FUNCTIONAL_BRIDGE"
    assert edges["EDGE-JUB-BELIAL-MASTEMA"]["relation"] == "IDENTITY_CONTESTED"

def test_direct_dependence_unresolved_edges_do_not_claim_direction():
    data = _load(MAP)
    for edge in data["edges"]:
        if "DIRECT_DEPENDENCE_UNRESOLVED" in edge["relation"]:
            assert edge["direction_status"] == "DIRECT_DEPENDENCE_UNRESOLVED"
        if edge["relation"] == "SHARED_TRADITION_FIELD_DIRECTION_UNRESOLVED":
            assert edge["direction_status"] == "DIRECT_DEPENDENCE_UNRESOLVED"

def test_no_linear_genealogy_or_identity_leak():
    data = _load(MAP)
    assert all(item["status"] == "NOT_ESTABLISHED" for item in data["negative_paths"])
    boundary = data["effect_boundary"]
    assert boundary["one_continuous_satan_biography"] is False
    assert boundary["mastema_equals_belial"] is False
    assert boundary["watchers_equal_mastema"] is False
    assert boundary["watchers_equal_giant_spirits"] is False
    assert boundary["direct_enoch_mastema_belial_chain_established"] is False

def test_prose_states_network_not_family_tree():
    text = PROSE.read_text(encoding="utf-8")
    assert "networked" in text
    assert "not linear" in text
    assert "SAME_ENTITY_BECAUSE_SIMILAR" in text
    assert "ha-satan -> Watchers -> Mastema -> Belial -> later Devil" in text
