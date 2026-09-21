import assert from 'node:assert/strict';

import {
  PAYLOAD_BYTES,
  answerBit,
  commitmentHex,
  serializeCommitmentPayload,
  verifyCommitment,
} from '../research/ritual-interface-exploit/reference/ifa_target_custody_verifier.mjs';

const nonce = Buffer.from(
  '000102030405060708090a0b0c0d0e0f'
  + '101112131415161718191a1b1c1d1e1f',
  'hex',
);

const vectors = [
  [1n, 0, 1, '398a4c6610d72727b0d0d3cb7b93a1899ce1d7080b6556e37fb4cdea3908cd23'],
  [42n, 1, 0, '68f02771508219886126081bc13631fa588e6390a94f89feedc596fd0d4e1fe2'],
  [1551n, 1, 1, '4bfbb69e8bc67de4bc845399824577c00b85682d6ad28f43eb3828f248715f9a'],
];

for (const [trialId, targetBit, sideMappingBit, digest] of vectors) {
  const record = { trialId, targetBit, sideMappingBit, nonce };
  assert.equal(serializeCommitmentPayload(record).length, PAYLOAD_BYTES);
  assert.equal(commitmentHex(record), digest);
  assert.equal(verifyCommitment(record, digest), true);
}

assert.equal(answerBit('LEFT', 0), 0);
assert.equal(answerBit('RIGHT', 0), 1);
assert.equal(answerBit('LEFT', 1), 1);
assert.equal(answerBit('RIGHT', 1), 0);

assert.throws(() => serializeCommitmentPayload({
  trialId: -1n,
  targetBit: 0,
  sideMappingBit: 0,
  nonce,
}));
assert.throws(() => serializeCommitmentPayload({
  trialId: 1n,
  targetBit: 2,
  sideMappingBit: 0,
  nonce,
}));
assert.throws(() => serializeCommitmentPayload({
  trialId: 1n,
  targetBit: 0,
  sideMappingBit: 0,
  nonce: Buffer.alloc(31),
}));

console.log('Ifa target-custody JS cross-check: PASS');
