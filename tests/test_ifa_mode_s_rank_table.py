from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "ritual-interface-exploit"
    / "reference"
    / "ifa_mode_s_rank_table.py"
)
SPEC = spec_from_file_location("ifa_mode_s_rank_table", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_rank_table_checksum_is_frozen():
    assert (
        MODULE.rank_table_sha256()
        == MODULE.EXPECTED_RANK_TABLE_SHA256
    )


def test_rank_table_contains_every_ordered_pair_once():
    rows = MODULE.build_rank_table()
    assert len(rows) == 256
    assert len({row["state_id"] for row in rows}) == 256
    expected = {
        f"{right}__{left}"
        for right in MODULE.GENERIC_ORDER
        for left in MODULE.GENERIC_ORDER
    }
    assert {row["state_id"] for row in rows} == expected


def test_major_16_are_first_in_source_bound_order():
    rows = MODULE.build_rank_table()
    assert [
        row["state_id"] for row in rows[:16]
    ] == [
        f"{name}__{name}" for name in MODULE.GENERIC_ORDER
    ]


def test_first_30_juniors_follow_source_bound_pair_pattern():
    rows = MODULE.build_rank_table()
    observed = [row["state_id"] for row in rows[16:46]]
    expected = []
    for other in MODULE.GENERIC_ORDER[1:]:
        expected.extend([f"OGBE__{other}", f"{other}__OGBE"])
    assert observed == expected


def test_bidirectional_maps_are_exact():
    state_to_rank = MODULE.state_to_rank()
    rank_to_state = MODULE.rank_to_state()
    assert len(state_to_rank) == 256
    assert len(rank_to_state) == 256
    for state_id, rank in state_to_rank.items():
        assert rank_to_state[rank] == state_id


def test_validation_passes():
    MODULE.validate_frozen_rank_table()
