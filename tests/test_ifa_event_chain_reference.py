from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import sys

import pytest

MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "ritual-interface-exploit"
    / "reference"
    / "ifa_event_chain_reference.py"
)
SPEC = spec_from_file_location("ifa_event_chain_reference", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

AuditEvent = MODULE.AuditEvent
ZERO_HASH = MODULE.ZERO_HASH
EVENT_TARGET_COMMIT = MODULE.EVENT_TARGET_COMMIT
EVENT_RESPONSE = MODULE.EVENT_RESPONSE
EVENT_REVEAL = MODULE.EVENT_REVEAL
EVENT_INVALID = MODULE.EVENT_INVALID
VALUE_LEFT = MODULE.VALUE_LEFT
VALUE_RIGHT = MODULE.VALUE_RIGHT
VALUE_TIE = MODULE.VALUE_TIE
VALUE_INVALID = MODULE.VALUE_INVALID
VALUE_NONE = MODULE.VALUE_NONE
event_hash = MODULE.event_hash
event_hash_hex = MODULE.event_hash_hex
serialize_event = MODULE.serialize_event
validate_chain = MODULE.validate_chain
observation_precedes_reveal = MODULE.observation_precedes_reveal

COMMIT = bytes.fromhex(
    "398a4c6610d72727b0d0d3cb7b93a189"
    "9ce1d7080b6556e37fb4cdea3908cd23"
)


def valid_events():
    e1 = AuditEvent(
        1, 1, EVENT_TARGET_COMMIT, VALUE_NONE, COMMIT, ZERO_HASH
    )
    h1 = event_hash(e1)
    e2 = AuditEvent(
        2, 1, EVENT_RESPONSE, VALUE_LEFT, ZERO_HASH, h1
    )
    h2 = event_hash(e2)
    e3 = AuditEvent(
        3, 1, EVENT_REVEAL, VALUE_NONE, COMMIT, h2
    )
    return e1, e2, e3


def test_public_event_vectors():
    e1, e2, e3 = valid_events()
    assert len(serialize_event(e1)) == 101
    assert event_hash_hex(e1) == (
        "078f7df0527c061bd2f6665454f02c5c"
        "4e49092345e6f698ffac0690a90f6b3c"
    )
    assert event_hash_hex(e2) == (
        "81369648c69fcf0d9afeb7832df26371"
        "4f253e646c0166a398a38ded2fcd7ff7"
    )
    assert event_hash_hex(e3) == (
        "6bb4a860af88c6dd6cece256d7e30ed2"
        "5c18b56baba272b90454f3ddcdad3066"
    )


def test_valid_chain_and_response_order():
    events = list(valid_events())
    assert validate_chain(events)
    assert observation_precedes_reveal(events, 1)


def test_rewrite_or_reorder_breaks_chain():
    e1, e2, e3 = valid_events()
    assert not validate_chain([e1, e3, e2])
    bad_e3 = AuditEvent(
        3, 1, EVENT_REVEAL, VALUE_NONE, COMMIT, event_hash(e1)
    )
    assert not validate_chain([e1, e2, bad_e3])


def test_reveal_without_observation_fails_gate():
    e1, _, _ = valid_events()
    e2 = AuditEvent(
        2, 1, EVENT_REVEAL, VALUE_NONE, COMMIT, event_hash(e1)
    )
    assert validate_chain([e1, e2])
    assert not observation_precedes_reveal([e1, e2], 1)


def test_invalid_tie_can_precede_reveal():
    e1, _, _ = valid_events()
    e2 = AuditEvent(
        2, 1, EVENT_INVALID, VALUE_TIE, ZERO_HASH, event_hash(e1)
    )
    e3 = AuditEvent(
        3, 1, EVENT_REVEAL, VALUE_NONE, COMMIT, event_hash(e2)
    )
    assert validate_chain([e1, e2, e3])
    assert observation_precedes_reveal([e1, e2, e3], 1)


@pytest.mark.parametrize(
    "event_type,value",
    [
        (EVENT_TARGET_COMMIT, VALUE_LEFT),
        (EVENT_RESPONSE, VALUE_NONE),
        (EVENT_REVEAL, VALUE_RIGHT),
        (EVENT_INVALID, VALUE_LEFT),
        (9, VALUE_NONE),
    ],
)
def test_invalid_event_value_combinations_rejected(event_type, value):
    event = AuditEvent(
        1, 1, event_type, value, ZERO_HASH, ZERO_HASH
    )
    with pytest.raises(ValueError):
        serialize_event(event)


@pytest.mark.parametrize("bad", [b"", b"x" * 31, b"x" * 33])
def test_bad_hash_lengths_rejected(bad):
    event = AuditEvent(
        1, 1, EVENT_TARGET_COMMIT, VALUE_NONE, bad, ZERO_HASH
    )
    with pytest.raises(ValueError):
        serialize_event(event)
