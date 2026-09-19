from pathlib import Path
import yaml


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "research/packets/jewish-hostile-powers-control-v1.yaml"
PROSE = ROOT / "research/packets/jewish-hostile-powers-control-v1.md"

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
    assert data["base_subject"]["head"] == "3acfe117989a78eac7ca17e8e70228d4d8a42deb"
    assert data["base_subject"]["inherited_exact_anchors"]["enoch_daniel_philo_corpus"] == "f4c4b4e940a8e6c76e9603d298bab819fbcc448d"


def test_core_nonidentities_are_explicit() -> None:
    data = _load()
    assert all(data["rules"].values())
    text = PROSE.read_text(encoding="utf-8")
    for marker in (
        "JOB_HA_SATAN != LATER_COSMIC_DEVIL",
        "WATCHERS != DEMONS != MASTEMA != BELIAL",
        "RELATED_DEVELOPMENT != ONE_CONTINUOUS_CHARACTER_IDENTITY",
        "HOSTILE_AGENT != COEQUAL_ANTI_GOD",
    ):
        assert marker in text


def test_job_and_zechariah_are_not_promoted_to_later_devil_system() -> None:
    data = _load()
    claims = {item["id"]: item for item in data["claims"]}
    job = claims["CLM-JOB-HA-SATAN-DIVINE-COURT"]
    assert job["confidence"] == "high"
    assert "fully developed later Devil" in job["ceiling"]
    assert claims["CLM-ZECHARIAH-SATAN-ACCUSER"]["confidence"] == "high"


def test_mastema_belial_and_watcher_identity_is_not_harmonized() -> None:
    data = _load()
    claims = {item["id"]: item for item in data["claims"]}
    identity = claims["CLM-MASTEMA-BELIAL-SATAN-ONE-IDENTICAL-FIGURE"]
    assert identity["supporting_sources"] == []
    assert identity["confidence"] == "unresolved"
    assert len(identity["opposing_sources"]) >= 3
    assert data["effect_boundary"]["establishes_one_continuous_satan_biography"] is False


def test_genesis_serpent_identification_is_not_added_without_source() -> None:
    data = _load()
    claim = next(item for item in data["claims"] if item["id"] == "CLM-GENESIS-SERPENT-IS-SATAN-SOURCE-TEXT")
    assert claim["supporting_sources"] == []
    assert claim["confidence"] == "unresolved"
    assert data["effect_boundary"]["establishes_genesis_serpent_as_satan"] is False


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


def test_effect_boundary_blocks_dualism_and_identity_overpromotion() -> None:
    data = _load()
    assert data["effect_boundary"] == {
        "changes_parent_afterlife_packet": False,
        "changes_existing_judaism_claims": False,
        "canonical_promotion": False,
        "merge_authority": False,
        "establishes_one_continuous_satan_biography": False,
        "establishes_coequal_dualism": False,
        "establishes_genesis_serpent_as_satan": False,
    }
