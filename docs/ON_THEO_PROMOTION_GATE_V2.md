# On-Theo Promotion Gate V2

Status: `REVIEW_GATES_RECONCILED / CANDIDATE_CONSTRUCTION_AUTHORIZED / CANONICAL_EFFECT_NOT_AUTHORIZED`

Recorded: 2026-09-18 14:45 ET

V2 supersedes the candidate-construction gate in V1 after Patrick corrected the review route: Masa, Mune, and Hephaestus are to be run from this chat using their durable repository-defined review disciplines rather than waiting for separate reviewer chats.

This changes the **required execution route**, not the factual provenance label. The three completed reviews are `SAME_RUNTIME_ROLE_PASS`; they are not represented as independent model samples.

## Accepted review chain

- consolidation subject PR #28: `99be7dd0e222480e0c82ed41c3d43383a759ab90`
- validator V2 PR #29: `8234d3fcc2d5a0eda26e5c7d4c2211de067c600a` — superseded after CHANGES_REQUIRED
- rehearsal PR #30: `8e651851cdc1d1d4994784a69b961d87914a32e0` — output bytes retained, control subject superseded after CHANGES_REQUIRED
- validator/materializer successor PR #31: `d81ab5ab58f326b0827dbc0f9903befb5580947e`, tree `e6e94b7ed35551ca675fed64ce2a0999ea441628`

Role dispositions:

| Role | PR28 | PR29 | PR30 | PR31 |
| --- | --- | --- | --- | --- |
| Masa | PASS_WITH_LIMITATIONS | CHANGES_REQUIRED | CHANGES_REQUIRED | PASS_WITH_LIMITATIONS |
| Mune | PASS_WITH_LIMITATIONS | CHANGES_REQUIRED | CHANGES_REQUIRED | PASS_WITH_LIMITATIONS |
| Hephaestus | PASS_WITH_LIMITATIONS | CHANGES_REQUIRED | CHANGES_REQUIRED | PASS_WITH_LIMITATIONS |

All PR31 limitations are nonblocking for **draft candidate construction**:
- remote subject-SHA existence must be read back before consequential admission;
- same-runtime role passes are not independent sampling;
- structural integrity does not prove historical truth;
- the candidate must explicitly bind PR31 as the control/source subject rather than pretending the fixes were present on PR30.

## PR31 exact evidence

- head: `d81ab5ab58f326b0827dbc0f9903befb5580947e`
- tree: `e6e94b7ed35551ca675fed64ce2a0999ea441628`
- push run `35381285810`: SUCCESS
- PR run `35381382184`: SUCCESS
- 53/53 tests PASS
- registry validator: zero errors/findings/warnings
- rehearsal: PASS
- unresolved-reference count: 0
- materialized output registry bytes: unchanged from reviewed PR30 rehearsal.

PR31-bound rebase/dependency reread:
- audit head `ef93955a9a902bf2d8ce4256fed9b30126c8343f`
- Actions run `35381678450`
- 55/55 tests PASS
- rebase precondition mismatches: 0
- cross-extension dependency violations: 0.

## Byte-bound output set

The draft candidate must reproduce exactly:

- `registry/claims.yaml` — `89c4422a2e7d03ecc2997fc6a0be5c24f80cbe4fa338a62afbf24ec815bb99b6`
- `registry/concepts.yaml` — `a8a7354ccd1bbf0aae0ee0f6fdda8545098027297bbde004c57ee8a895f44b97`
- `registry/extension-manifest.yaml` — `6f5c21bdd3c32446194ae7ca9b2d7e7b25dc130967006cba11bd6f2d6c9f3bd9`
- `registry/reviews.yaml` — `0f7ed711f8d089a778526bf5a042e708f10cd05de39edbebfc3bb096f3cc1a72`
- `registry/source-access.yaml` — `6c97263769c615ac5863ed879da857f58ebfda2031c799d50ef683623efc0d5a`
- `registry/sources.yaml` — `b5e54df4eb984c0f30865be08d33dd7bc711bacba3f6596cef2e370e30cf1d56`
- `registry/transmissions.yaml` — `423f746b65e93fb5efa54ad17490fdbbe8f3f84bec094d9dead55954a8ad770d`
- `registry/witnesses.yaml` — `7e22b5b0c46065eeb12108ee14e3c34a818f4d45062f9a99ad4e3b7f6b42e49a`

## Candidate construction authority

Patrick previously authorized: after review gates, construct a byte-bound promotion candidate; actual canonical merge/materialization remains separately protected.

That candidate construction gate is now satisfied under Patrick's corrected repo-grounded review route.

Candidate requirements:
1. branch from exact PR31 head;
2. archive the reviewed pre-materialization manifest and all 20 extension files byte-identically under `provenance/materialization-input-v1/`;
3. replace the eight active registry files with the exact byte set above;
4. remove active `registry/extensions/*.yaml` only after archive byte equality is proven;
5. keep `canonical_materialized: false`;
6. run full tests, registry validation, archive-byte readback, exact output digest checks, and counts;
7. emit a machine-readable candidate receipt binding PR31, review dispositions, input blobs/digests, output digests, and CI;
8. open only a DRAFT / UNMERGED / NOT CANONICAL PR.

## Protected boundary

This gate does **not** authorize:
- merge to main;
- setting canonical materialization true;
- deleting predecessor provenance/history;
- changing Testament or another downstream consumer;
- production/provider/runtime effects.

Those remain separate protected effects requiring Patrick's exact authorization.
