import pytest

from research.ritual_interface_exploit.reference.ifa_target_custody_reference import (
    PAYLOAD_BYTES,
    RevealRecord,
    answer_bit,
    commitment_hex,
    score_hit,
    serialize_commitment_payload,
    verify_commitment,
)

NONCE = bytes.fromhex(
    "000102030405060708090a0b0c0d0e0f"
    "101112131415161718191a1b1c1d1e1f"
)

VECTORS = [
    (1, 0, 1, "398a4c6610d72727b0d0d3cb7b93a1899ce1d7080b6556e37fb4cdea3908cd23"),
    (42, 1, 0, "68f02771508219886126081bc13631fa588e6390a94f89feedc596fd0d4e1fe2"),
    (1551, 1, 1, "4bfbb69e8bc67de4bc845399824577c00b85682d6ad28f43eb3828f248715f9a"),
]


@pytest.mark.parametrize("trial,target,mapping,digest", VECTORS)
def test_public_vectors(trial, target, mapping, digest):
    record = RevealRecord(trial, target, mapping, NONCE)
    assert len(serialize_commitment_payload(record)) == PAYLOAD_BYTES
    assert commitment_hex(record) == digest
    assert verify_commitment(record, digest)


@pytest.mark.parametrize("bad", [b"", b"x" * 31, b"x" * 33])
def test_nonce_length_rejected(bad):
    with pytest.raises(ValueError):
        commitment_hex(RevealRecord(1, 0, 1, bad))


@pytest.mark.parametrize(
    "field,value",
    [("target_bit", 2), ("target_bit", -1), ("side_mapping_bit", 2)],
)
def test_bad_bits_rejected(field, value):
    kwargs = dict(trial_id=1, target_bit=0, side_mapping_bit=1, nonce=NONCE)
    kwargs[field] = value
    with pytest.raises(ValueError):
        commitment_hex(RevealRecord(**kwargs))


@pytest.mark.parametrize("trial", [-1, 2**64])
def test_bad_trial_id_rejected(trial):
    with pytest.raises(ValueError):
        commitment_hex(RevealRecord(trial, 0, 1, NONCE))


def test_mutation_breaks_commitment():
    original = RevealRecord(42, 1, 0, NONCE)
    digest = commitment_hex(original)
    assert not verify_commitment(RevealRecord(42, 0, 0, NONCE), digest)
    assert not verify_commitment(RevealRecord(42, 1, 1, NONCE), digest)
    changed_nonce = bytes([1]) + NONCE[1:]
    assert not verify_commitment(RevealRecord(42, 1, 0, changed_nonce), digest)


def test_mapping_truth_table():
    assert answer_bit("LEFT", 0) == 0
    assert answer_bit("RIGHT", 0) == 1
    assert answer_bit("LEFT", 1) == 1
    assert answer_bit("RIGHT", 1) == 0


def test_score_hit_is_mechanical():
    assert score_hit("LEFT", RevealRecord(1, 0, 0, NONCE)) == 1
    assert score_hit("RIGHT", RevealRecord(1, 0, 0, NONCE)) == 0
    assert score_hit("LEFT", RevealRecord(1, 1, 1, NONCE)) == 1


def test_invalid_side_rejected():
    with pytest.raises(ValueError):
        answer_bit("CENTER", 0)
