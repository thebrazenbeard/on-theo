from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "ritual-interface-exploit"
    / "reference"
    / "ifa_mode_s_placement_schedule.py"
)
SPEC = spec_from_file_location("ifa_mode_s_placement_schedule", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_schedule_checksum_is_frozen():
    schedule = MODULE.build_schedule()
    assert (
        MODULE.schedule_sha256(schedule)
        == MODULE.EXPECTED_SCHEDULE_SHA256
    )


def test_every_attempt_is_present_once():
    schedule = MODULE.build_schedule()
    assert len(schedule) == MODULE.TOTAL_ATTEMPTS
    assert [
        row["attempt_index_global"] for row in schedule
    ] == list(range(1, MODULE.TOTAL_ATTEMPTS + 1))


def test_every_session_is_exactly_balanced():
    schedule = MODULE.build_schedule()
    assert (
        MODULE.SESSION_COUNT * MODULE.SESSION_SIZE
        == MODULE.TOTAL_ATTEMPTS
    )
    for session_index in range(MODULE.SESSION_COUNT):
        block = schedule[
            session_index * MODULE.SESSION_SIZE
            : (session_index + 1) * MODULE.SESSION_SIZE
        ]
        assert (
            sum(row["token_left"] == "A" for row in block)
            == MODULE.A_LEFT_PER_SESSION
        )
        assert (
            sum(row["token_right"] == "A" for row in block)
            == MODULE.A_LEFT_PER_SESSION
        )


def test_validation_passes():
    MODULE.validate_frozen_schedule()
