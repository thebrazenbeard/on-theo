from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import pytest


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "ritual-interface-exploit"
    / "reference"
    / "ifa_null_calibration_analysis.py"
)
SPEC = spec_from_file_location("ifa_null_calibration_analysis", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

PLACEMENT_PATH = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "ritual-interface-exploit"
    / "reference"
    / "ifa_mode_s_placement_schedule.py"
)
PLACEMENT_SPEC = spec_from_file_location(
    "ifa_mode_s_placement_schedule_for_test",
    PLACEMENT_PATH,
)
assert PLACEMENT_SPEC is not None and PLACEMENT_SPEC.loader is not None
PLACEMENT = module_from_spec(PLACEMENT_SPEC)
PLACEMENT_SPEC.loader.exec_module(PLACEMENT)
PLACEMENT_SCHEDULE = PLACEMENT.build_schedule()

RANK_TABLE_PATH = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "ritual-interface-exploit"
    / "reference"
    / "ifa_mode_s_rank_table.py"
)
RANK_TABLE_SPEC = spec_from_file_location(
    "ifa_mode_s_rank_table_for_test",
    RANK_TABLE_PATH,
)
assert RANK_TABLE_SPEC is not None and RANK_TABLE_SPEC.loader is not None
RANK_TABLE = module_from_spec(RANK_TABLE_SPEC)
RANK_TABLE_SPEC.loader.exec_module(RANK_TABLE)
RANK_TO_STATE = RANK_TABLE.rank_to_state()

ENCODER_PATH = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "ritual-interface-exploit"
    / "reference"
    / "ifa_mode_s_opele_encoder.py"
)
ENCODER_SPEC = spec_from_file_location(
    "ifa_mode_s_opele_encoder_for_test",
    ENCODER_PATH,
)
assert ENCODER_SPEC is not None and ENCODER_SPEC.loader is not None
ENCODER = module_from_spec(ENCODER_SPEC)
ENCODER_SPEC.loader.exec_module(ENCODER)


def generic_to_faces(generic):
    return [
        ENCODER.INSIDE_ROUGH if digit == "1" else ENCODER.OUTSIDE_SMOOTH
        for digit in ENCODER.GENERIC_TO_PATTERN[generic]
    ]


def state_to_faces(state_id):
    right, left = state_id.split("__", 1)
    return generic_to_faces(right), generic_to_faces(left)


def make_records(rank_pairs):
    records = []
    prior = MODULE.GENESIS_HASH
    split_point = max(1, len(rank_pairs) // 2)
    for index, (first_rank, second_rank) in enumerate(rank_pairs, start=1):
        relation = MODULE.expected_relation(first_rank, second_rank)
        side = MODULE.expected_side(relation)
        placement = PLACEMENT_SCHEDULE[index - 1]
        token_left = placement["token_left"]
        token_right = placement["token_right"]
        if side == "LEFT":
            output = token_left
        elif side == "RIGHT":
            output = token_right
        else:
            output = "INVALID"
        session_id = "S1" if index <= split_point else "S2"
        session_index = index if index <= split_point else index - split_point
        cast1_state = RANK_TO_STATE[first_rank]
        cast2_state = RANK_TO_STATE[second_rank]
        cast1_right_faces, cast1_left_faces = state_to_faces(cast1_state)
        cast2_right_faces, cast2_left_faces = state_to_faces(cast2_state)
        record = {
            "trial_id": f"T{index:05d}",
            "procedure_version": "MODE_S_TEST",
            "procedure_hash": "a" * 64,
            "timestamp_utc": f"2026-09-21T12:{index % 60:02d}:00Z",
            "session_id": session_id,
            "operator_id_pseudonymous": "OP1",
            "attempt_index_global": index,
            "attempt_index_session": session_index,
            "placement_block_id": placement["placement_block_id"],
            "attempt_index_block": placement["attempt_index_block"],
            "cast1_right_faces": cast1_right_faces,
            "cast1_left_faces": cast1_left_faces,
            "cast1_raw_state": cast1_state,
            "cast1_rank": first_rank,
            "cast2_right_faces": cast2_right_faces,
            "cast2_left_faces": cast2_left_faces,
            "cast2_raw_state": cast2_state,
            "cast2_rank": second_rank,
            "pair_relation": relation,
            "selected_side": side,
            "token_left": token_left,
            "token_right": token_right,
            "raw_output": output,
            "invalid_reason": (
                "EQUAL_RANK" if relation == "EQUAL" else None
            ),
            "recast_count": 0,
            "deviation_code": None,
            "prior_event_hash": prior,
        }
        record["event_hash"] = MODULE.compute_event_hash(record)
        records.append(record)
        prior = record["event_hash"]
    return records


def rehash_records(records):
    prior = MODULE.GENESIS_HASH
    for record in records:
        record["prior_event_hash"] = prior
        record["event_hash"] = MODULE.compute_event_hash(record)
        prior = record["event_hash"]
    return records


def test_balanced_orientation_is_not_rejected():
    pairs = []
    for _ in range(50):
        pairs.extend([(1, 2), (2, 1), (17, 49), (49, 17)])
    summary = MODULE.summarize_mode_s(
        make_records(pairs),
        swap_replicates=2000,
    )
    assert summary["p_right"] == 0.5
    assert summary["directional_half_rejected_alpha_0_01"] is False
    assert summary["symmetry_projection_rejected_alpha_0_01"] is False
    assert summary["cast_position_state_total_variation"] == 0.0


def test_strong_position_bias_is_rejected():
    pairs = [(1, 33)] * 180 + [(33, 1)] * 20
    summary = MODULE.summarize_mode_s(
        make_records(pairs),
        swap_replicates=5000,
    )
    assert summary["p_right"] == 0.1
    assert summary["directional_half_rejected_alpha_0_01"] is True
    assert summary["symmetry_projection_rejected_alpha_0_01"] is True


def test_equal_rank_is_invalid_and_retained():
    summary = MODULE.summarize_mode_s(
        make_records([(1, 1), (2, 1), (1, 2)]),
        swap_replicates=200,
    )
    assert summary["attempts"] == 3
    assert summary["ties"] == 1
    assert summary["valid"] == 2


def test_target_bearing_record_is_rejected():
    records = make_records([(1, 2)])
    records[0]["target"] = "A"
    records[0]["event_hash"] = MODULE.compute_event_hash(records[0])
    with pytest.raises(MODULE.CalibrationIntegrityError, match="prohibited"):
        MODULE.summarize_mode_s(records, swap_replicates=100)


def test_broken_hash_chain_is_rejected():
    records = make_records([(1, 2), (2, 1)])
    records[1]["prior_event_hash"] = "f" * 64
    records[1]["event_hash"] = MODULE.compute_event_hash(records[1])
    with pytest.raises(MODULE.CalibrationIntegrityError, match="chain"):
        MODULE.summarize_mode_s(records, swap_replicates=100)


def test_duplicate_trial_id_is_rejected():
    records = make_records([(1, 2), (2, 1)])
    records[1]["trial_id"] = records[0]["trial_id"]
    records[1]["event_hash"] = MODULE.compute_event_hash(records[1])
    with pytest.raises(MODULE.CalibrationIntegrityError, match="duplicate"):
        MODULE.summarize_mode_s(records, swap_replicates=100)


def test_wrong_frozen_placement_is_rejected():
    records = make_records([(1, 2)])
    records[0]["token_left"], records[0]["token_right"] = (
        records[0]["token_right"],
        records[0]["token_left"],
    )
    records[0]["raw_output"] = records[0]["token_left"]
    records[0]["event_hash"] = MODULE.compute_event_hash(records[0])
    with pytest.raises(
        MODULE.CalibrationIntegrityError,
        match="frozen placement schedule",
    ):
        MODULE.summarize_mode_s(records, swap_replicates=100)


def test_midstream_procedure_change_is_rejected():
    records = make_records([(1, 2), (2, 1)])
    records[1]["procedure_hash"] = "b" * 64
    records[1]["event_hash"] = MODULE.compute_event_hash(records[1])
    with pytest.raises(
        MODULE.CalibrationIntegrityError,
        match="midstream procedure",
    ):
        MODULE.summarize_mode_s(records, swap_replicates=100)


def test_noncontiguous_session_index_is_rejected():
    records = make_records([(1, 2), (2, 1), (3, 2), (2, 3)])
    records[1]["attempt_index_session"] = 3
    records[1]["event_hash"] = MODULE.compute_event_hash(records[1])
    records[2]["prior_event_hash"] = records[1]["event_hash"]
    records[2]["event_hash"] = MODULE.compute_event_hash(records[2])
    records[3]["prior_event_hash"] = records[2]["event_hash"]
    records[3]["event_hash"] = MODULE.compute_event_hash(records[3])
    with pytest.raises(
        MODULE.CalibrationIntegrityError,
        match="attempt_index_session",
    ):
        MODULE.summarize_mode_s(records, swap_replicates=100)


def test_closed_session_id_cannot_reappear():
    records = make_records([(1, 2), (2, 1), (3, 2), (2, 3)])
    records[3]["session_id"] = "S1"
    records[3]["attempt_index_session"] = 3
    records[3]["event_hash"] = MODULE.compute_event_hash(records[3])
    with pytest.raises(
        MODULE.CalibrationIntegrityError,
        match="reappears after closure",
    ):
        MODULE.summarize_mode_s(records, swap_replicates=100)


def test_raw_state_rank_mismatch_is_rejected():
    records = make_records([(1, 2)])
    records[0]["cast1_rank"] = 3
    records[0]["event_hash"] = MODULE.compute_event_hash(records[0])
    with pytest.raises(
        MODULE.CalibrationIntegrityError,
        match="cast1_rank contradicts",
    ):
        MODULE.summarize_mode_s(records, swap_replicates=100)


def test_raw_state_face_mismatch_is_rejected():
    records = make_records([(1, 2)])
    records[0]["cast2_raw_state"] = "IWORI__IWORI"
    records[0]["event_hash"] = MODULE.compute_event_hash(records[0])
    with pytest.raises(
        MODULE.CalibrationIntegrityError,
        match="cast2_raw_state contradicts recorded faces",
    ):
        MODULE.summarize_mode_s(records, swap_replicates=100)


def test_bad_face_value_is_rejected():
    records = make_records([(1, 2)])
    records[0]["cast1_right_faces"][0] = "UNREADABLE"
    records[0]["event_hash"] = MODULE.compute_event_hash(records[0])
    with pytest.raises(
        MODULE.CalibrationIntegrityError,
        match="faces violate frozen Opele encoder",
    ):
        MODULE.summarize_mode_s(records, swap_replicates=100)


def test_predeclared_partial_invalid_is_retained():
    records = make_records([(1, 2)])
    records[0]["cast2_right_faces"] = None
    records[0]["cast2_left_faces"] = None
    records[0]["cast2_raw_state"] = None
    records[0]["cast2_rank"] = None
    records[0]["pair_relation"] = "INVALID"
    records[0]["selected_side"] = None
    records[0]["raw_output"] = "INVALID"
    records[0]["invalid_reason"] = "PAIR_DISTURBED_BEFORE_COMPLETION"
    records[0]["event_hash"] = MODULE.compute_event_hash(records[0])
    summary = MODULE.summarize_mode_s(records, swap_replicates=100)
    assert summary["attempts"] == 1
    assert summary["valid"] == 0
    assert summary["ties"] == 0
    assert summary["other_invalid"] == 1


def test_unlisted_invalid_reason_is_rejected():
    records = make_records([(1, 2)])
    records[0]["cast2_raw_state"] = None
    records[0]["cast2_rank"] = None
    records[0]["pair_relation"] = "INVALID"
    records[0]["selected_side"] = None
    records[0]["raw_output"] = "INVALID"
    records[0]["invalid_reason"] = "FELT_WRONG"
    records[0]["event_hash"] = MODULE.compute_event_hash(records[0])
    with pytest.raises(
        MODULE.CalibrationIntegrityError,
        match="invalid_reason is not predeclared",
    ):
        MODULE.summarize_mode_s(records, swap_replicates=100)


def test_valid_pair_cannot_be_retroactively_invalidated():
    records = make_records([(1, 2)])
    records[0]["invalid_reason"] = "PAIR_DISTURBED_BEFORE_COMPLETION"
    records[0]["event_hash"] = MODULE.compute_event_hash(records[0])
    with pytest.raises(
        MODULE.CalibrationIntegrityError,
        match="valid pair cannot carry invalid_reason",
    ):
        MODULE.summarize_mode_s(records, swap_replicates=100)


def test_unlisted_deviation_code_is_rejected():
    records = make_records([(1, 2)])
    records[0]["deviation_code"] = "POSTHOC_EXCEPTION"
    records[0]["event_hash"] = MODULE.compute_event_hash(records[0])
    with pytest.raises(
        MODULE.CalibrationIntegrityError,
        match="deviation_code is not predeclared",
    ):
        MODULE.summarize_mode_s(records, swap_replicates=100)


def test_within_session_serial_clustering_is_rejected():
    pairs = (
        [(2, 1)] * 50
        + [(1, 2)] * 50
        + [(2, 1)] * 50
        + [(1, 2)] * 50
    )
    records = make_records(pairs)
    for index, record in enumerate(records, start=1):
        record["session_id"] = "S1"
        record["attempt_index_session"] = index
    rehash_records(records)
    p_value, observed, expected, edges = (
        MODULE.serial_order_permutation_pvalue(
            records,
            replicates=3000,
            seed=12345,
        )
    )
    assert edges == 199
    assert observed > expected
    assert p_value < 0.01


def test_session_heterogeneity_is_rejected():
    pairs = [(2, 1)] * 100 + [(1, 2)] * 100
    records = make_records(pairs)
    p_value, statistic, session_count = (
        MODULE.session_heterogeneity_permutation_pvalue(
            records,
            replicates=3000,
            seed=54321,
        )
    )
    assert session_count == 2
    assert statistic > 0
    assert p_value < 0.01


def test_chronological_quintile_drift_is_rejected():
    pairs = (
        [(2, 1)] * 500
        + [(1, 2)] * 500
        + [(2, 1), (1, 2)] * 250
        + [(2, 1)] * 500
        + [(1, 2)] * 500
    )
    records = make_records(pairs)
    p_value, statistic, table = MODULE.chronological_quintile_homogeneity(
        records
    )
    assert len(table) == 5
    assert statistic is not None and statistic > 0
    assert p_value is not None and p_value < 0.01


def test_multiple_operators_block_half_null_admission_flag():
    records = make_records([(2, 1), (1, 2)] * 100)
    records[100]["operator_id_pseudonymous"] = "OP2"
    rehash_records(records)
    summary = MODULE.summarize_mode_s(
        records,
        swap_replicates=200,
    )
    assert summary["operator_count"] == 2
    assert summary["half_null_admission_ready"] is False
