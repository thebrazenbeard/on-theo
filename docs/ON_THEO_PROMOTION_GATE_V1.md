# On-Theo Promotion Gate V1

Status: `PRE_GATE / NOT AUTHORIZED / NO PROMOTION CANDIDATE YET`

Recorded: 2026-09-18T10:52-04:00

This document defines the conditions under which a byte-bound promotion **candidate** may be constructed. It does not authorize canonical materialization, merge, or any write to `main`.

## Frozen review subjects

| Layer | PR | Commit | Tree | State |
| --- | --- | --- | --- | --- |
| Consolidation | #28 | `99be7dd0e222480e0c82ed41c3d43383a759ab90` | `278c7b102c1582ae97bc75a59745c481e2cfd277` | DRAFT / UNMERGED |
| Validator hardening | #29 | `8234d3fcc2d5a0eda26e5c7d4c2211de067c600a` | `dd1d60bc93af70d5c2af8ce202bafb5884512b73` | DRAFT / UNMERGED |
| Materialization rehearsal | #30 | `8e651851cdc1d1d4994784a69b961d87914a32e0` | `0679ca2c88b237840d647d1406bb34d4214f3d8d` | DRAFT / UNMERGED |

Current canonical branch remains `main@eedbcf660c2cfe6cff5636e798806b0cd3d56efc`.

Frozen subjects are review targets. Required repairs must not rewrite these exact heads. Any required repair creates a successor subject with its own exact-head review.

## Independent review gates

For each frozen subject, require independent review from the routed review lanes:

- Masa — hostile/falsification review;
- Mune — provenance/readback review;
- Hephaestus — architecture/interoperability review.

A review counts only when:

1. it names the exact subject commit;
2. its execution provenance is independent of the authoring/runtime path being reviewed, or is an external human review;
3. it records an explicit disposition;
4. any limitation or finding is concrete enough to classify as blocking or non-blocking.

Acceptable gate dispositions:

- `PASS_EXACT`; or
- `PASS_WITH_LIMITATIONS` only when every limitation is explicitly non-blocking for promotion-candidate construction.

Blocking dispositions:

- `CHANGES_REQUIRED`;
- `FAIL`;
- unresolved critical/high-severity finding;
- exact-head mismatch;
- ambiguous or same-runtime-only review represented as independent.

A blocking finding stops the gate. The repair must occur on a successor branch/PR, pass CI/readback, and receive fresh exact-head review.

## Current mechanical evidence

PR #29 exact-head validation:

- 29/29 tests PASS;
- registry validator: zero errors/findings/warnings;
- all 34 unique manifest base/introduction SHAs resolve;
- all 20 `introduced_at` commits contain the claimed extension path and matching extension ID.

PR #30 exact-head validation:

- 37/37 tests PASS;
- source registry validator: zero errors/findings/warnings;
- rehearsal output validator: zero errors/warnings;
- 20 extensions applied;
- zero collisions;
- every extension record materializes exactly once;
- base + addition counts equal output counts;
- repeated rehearsal is deterministic;
- exact source-registry SHA-256 maps before/after are identical.

These facts are necessary engineering evidence. They do not replace independent review or establish historical truth.

## Rehearsal input binding

Source manifest SHA-256:

`bf99460c7a6b37eac0cbc266f9a330988a5a4af1083ed1dbb5ac3ea1e98b82e2`

Expected counts after rehearsal:

- sources: 131
- claims: 129
- concepts: 26
- transmission edges: 23
- witnesses: 4

Expected output registry SHA-256 values:

| Path | SHA-256 |
| --- | --- |
| `registry/claims.yaml` | `89c4422a2e7d03ecc2997fc6a0be5c24f80cbe4fa338a62afbf24ec815bb99b6` |
| `registry/concepts.yaml` | `a8a7354ccd1bbf0aae0ee0f6fdda8545098027297bbde004c57ee8a895f44b97` |
| `registry/extension-manifest.yaml` | `6f5c21bdd3c32446194ae7ca9b2d7e7b25dc130967006cba11bd6f2d6c9f3bd9` |
| `registry/reviews.yaml` | `0f7ed711f8d089a778526bf5a042e708f10cd05de39edbebfc3bb096f3cc1a72` |
| `registry/source-access.yaml` | `6c97263769c615ac5863ed879da857f58ebfda2031c799d50ef683623efc0d5a` |
| `registry/sources.yaml` | `b5e54df4eb984c0f30865be08d33dd7bc711bacba3f6596cef2e370e30cf1d56` |
| `registry/transmissions.yaml` | `423f746b65e93fb5efa54ad17490fdbbe8f3f84bec094d9dead55954a8ad770d` |
| `registry/witnesses.yaml` | `7e22b5b0c46065eeb12108ee14e3c34a818f4d45062f9a99ad4e3b7f6b42e49a` |

The future promotion candidate must reproduce these registry bytes exactly unless a reviewed successor rehearsal deliberately supersedes this digest set.

## Ordering invariant

The manifest contract says application order is topological by `depends_on`, then manifest order for independent extensions.

The current validator rejects any dependency that does not precede its dependent in manifest order. Therefore, for the frozen PR #30 subject, direct manifest iteration is equivalent to the declared topological order.

The promotion candidate gate must preserve this equivalence. If manifest ordering or dependency semantics change, the rehearsal and independent review are stale.

## Promotion-candidate construction constraints

Only after all independent review gates are satisfied may a candidate be constructed.

The candidate must:

1. be created on a new branch/PR; never write to `main`;
2. use the reviewed source/rehearsal subject or an explicitly reviewed successor;
3. reproduce all eight expected registry SHA-256 values byte-for-byte;
4. preserve every extension input byte/digest in durable provenance, even if active extension files are moved out of the validator-visible active directory;
5. contain no unresolved IDs, collisions, or validator findings;
6. emit a candidate receipt binding:
   - source repo/commit/tree;
   - all extension IDs and SHA-256 values;
   - output registry SHA-256 values;
   - record counts;
   - CI run IDs;
   - independent review receipts;
   - candidate branch/commit/tree;
7. prove that no canonical branch, protected configuration, or external consumer was changed;
8. remain DRAFT / UNMERGED / NOT CANONICAL.

If active extension files would become orphaned after the materialized manifest clears its extension list, the candidate must preserve those input bytes in a non-active archival/provenance location or use another independently reviewed mechanism. It must not weaken the validator merely to silence orphan detection.

## Protected boundary

Constructing the draft byte-bound candidate is permitted only after the above review gates.

The following remain separately protected and require Patrick's explicit authorization at the time of effect:

- merge to `main`;
- canonical materialization/promotion;
- deletion of predecessor source/provenance;
- downstream dependency cutover;
- production/runtime/provider effects.

A candidate, green CI, review PASS, or receipt is not the protected effect.
