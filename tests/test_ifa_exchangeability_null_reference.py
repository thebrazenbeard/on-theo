from importlib.util import module_from_spec, spec_from_file_location
from math import isclose
from pathlib import Path


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "ritual-interface-exploit"
    / "reference"
    / "ifa_exchangeability_null_reference.py"
)
SPEC = spec_from_file_location("ifa_exchangeability_null_reference", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

iid_rank_comparison = MODULE.iid_rank_comparison
ordered_position_comparison = MODULE.ordered_position_comparison


def test_uniform_256_matches_idealized_benchmark():
    result = iid_rank_comparison([1 / 256] * 256)
    assert isclose(result["tie"], 1 / 256, abs_tol=1e-15)
    assert isclose(result["first_wins"], 255 / 512, abs_tol=1e-15)
    assert isclose(result["second_wins"], 255 / 512, abs_tol=1e-15)


def test_nonuniform_iid_remains_directionally_balanced():
    result = iid_rank_comparison([0.5, 0.3, 0.2])
    assert isclose(result["tie"], 0.38, abs_tol=1e-15)
    assert isclose(result["first_wins"], 0.31, abs_tol=1e-15)
    assert isclose(result["second_wins"], 0.31, abs_tol=1e-15)
    assert isclose(result["first_wins"] / result["valid"], 0.5, abs_tol=1e-15)


def test_position_specific_marginals_can_break_directional_balance():
    result = ordered_position_comparison(
        [0.7, 0.2, 0.1],
        [0.1, 0.2, 0.7],
    )
    assert isclose(result["first_wins"], 0.77, abs_tol=1e-15)
    assert isclose(result["second_wins"], 0.05, abs_tol=1e-15)
    assert not isclose(result["first_wins"], result["second_wins"])


def test_invalid_probability_vectors_fail():
    try:
        iid_rank_comparison([0.6, 0.6])
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError for probabilities not summing to 1")
