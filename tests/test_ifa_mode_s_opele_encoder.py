from importlib.util import module_from_spec, spec_from_file_location
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REFERENCE = ROOT / "research" / "ritual-interface-exploit" / "reference"


def load(name, filename):
    spec = spec_from_file_location(name, REFERENCE / filename)
    assert spec is not None and spec.loader is not None
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ENCODER = load("ifa_mode_s_opele_encoder", "ifa_mode_s_opele_encoder.py")
RANKS = load("ifa_mode_s_rank_table_encoder_test", "ifa_mode_s_rank_table.py")


def test_pattern_table_checksum_is_frozen():
    assert (
        ENCODER.pattern_table_sha256()
        == ENCODER.EXPECTED_PATTERN_TABLE_SHA256
    )


def test_public_physical_anchor_extremes():
    inside = [ENCODER.INSIDE_ROUGH] * 4
    outside = [ENCODER.OUTSIDE_SMOOTH] * 4
    assert ENCODER.encode_cast(inside, inside) == "OGBE__OGBE"
    assert ENCODER.encode_cast(outside, outside) == "OYEKU__OYEKU"


def test_mixed_public_sign_examples():
    to_faces = {
        "1": ENCODER.INSIDE_ROUGH,
        "2": ENCODER.OUTSIDE_SMOOTH,
    }
    right = [to_faces[digit] for digit in "2112"]
    left = [to_faces[digit] for digit in "1221"]
    assert ENCODER.encode_cast(right, left) == "IWORI__ODI"


def test_every_four_face_pattern_maps_once():
    faces = [ENCODER.INSIDE_ROUGH, ENCODER.OUTSIDE_SMOOTH]
    observed = {
        ENCODER.encode_leg(pattern)
        for pattern in product(faces, repeat=4)
    }
    assert observed == set(ENCODER.GENERIC_TO_PATTERN)


def test_all_256_casts_land_in_frozen_rank_table():
    faces = [ENCODER.INSIDE_ROUGH, ENCODER.OUTSIDE_SMOOTH]
    legs = list(product(faces, repeat=4))
    observed = {
        ENCODER.encode_cast(right, left)
        for right in legs
        for left in legs
    }
    assert observed == set(RANKS.state_to_rank())


def test_bad_face_and_bad_length_fail():
    try:
        ENCODER.encode_leg([ENCODER.INSIDE_ROUGH] * 3)
    except ValueError:
        pass
    else:
        raise AssertionError("three-face arm must fail")

    try:
        ENCODER.encode_leg(
            [
                ENCODER.INSIDE_ROUGH,
                ENCODER.INSIDE_ROUGH,
                ENCODER.INSIDE_ROUGH,
                "UNKNOWN",
            ]
        )
    except ValueError:
        pass
    else:
        raise AssertionError("unknown face must fail")


def test_validation_passes():
    ENCODER.validate_frozen_encoder()
