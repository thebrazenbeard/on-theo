# On-Theo Promotion Candidate Construction V1

Status: `PREPARED / GATE-BLOCKED / NO CANDIDATE CREATED`

This document specifies the exact transformation to use **only after** the independent review gate in `docs/ON_THEO_PROMOTION_GATE_V1.md` is satisfied.

It does not authorize merge, canonical materialization, or candidate construction before that gate.

## Frozen source subject

The currently reviewed rehearsal subject is:

- repository: `thebrazenbeard/on-theo`
- PR: `#30`
- commit: `8e651851cdc1d1d4994784a69b961d87914a32e0`
- tree: `0679ca2c88b237840d647d1406bb34d4214f3d8d`

The current byte-bound rehearsal output is valid only for that exact subject unless an independently reviewed successor explicitly supersedes it.

## Candidate branch rule

After gate closure:

1. create one new branch from the exact reviewed rehearsal head;
2. keep PR #28, #29, and #30 frozen;
3. generate materialized registries using the reviewed rehearsal implementation;
4. write generated registry bytes exactly once;
5. archive every active extension input byte outside validator-active paths;
6. remove the active `registry/extensions/*.yaml` copies from the candidate tree only after archival byte equality is proved;
7. replace the active extension manifest with the exact reviewed materialized manifest;
8. run exact byte verification before opening the draft promotion PR.

No force-push or history rewrite.

## Required archival layout

The candidate must preserve the pre-materialization input set under a non-active provenance namespace:

```text
provenance/materialization-input-v1/
  source-subject.yaml
  registry/
    extension-manifest.yaml
    extensions/
      <all 20 original extension YAML files, byte-identical>
  digests/
    extension-sha256.yaml
    source-registry-sha256.yaml
```

The archive is evidence only. Nothing under `provenance/materialization-input-v1/` is executable registry input.

The original extension paths must not remain active under `registry/extensions/` after the materialized manifest contains an empty extension list, because the validator correctly treats those files as orphan extensions.

Historical Git objects and predecessor branches remain untouched.

## Required active materialized registry bytes

The candidate must reproduce these exact SHA-256 values:

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

Expected materialized counts:

- sources: 131
- claims: 129
- concepts: 26
- transmission edges: 23
- witnesses: 4
- active extensions: 0
- collisions: 0
- unresolved references: 0

## Required input preservation

The archive must preserve the exact 20 extension files used by the reviewed rehearsal.

The candidate receipt must bind every extension ID to:

- original active path;
- archived candidate path;
- source Git blob SHA where available;
- SHA-256;
- declared base;
- introduced-at commit;
- declared dependencies;
- review/rebase evidence.

Archive verification is byte-level, not YAML-semantic-only.

## Rebase evidence binding

Nine extensions use declared bases that are not ancestors of the frozen rehearsal subject.

A promotion candidate may be constructed only if the independent gate accepts the rebase exception using the current evidence or a reviewed successor.

Current supplemental evidence includes:

- `receipts/ON_THEO_EXTENSION_REBASE_EQUIVALENCE_V1.yaml`
- `receipts/ON_THEO_EXTENSION_DEPENDENCY_CLOSURE_V1.yaml`
- `receipts/ON_THEO_REBASE_PRECONDITION_AUDIT_V1.yaml`

The latest mechanical audit proves:

- 9 divergent extensions across 6 unique bases;
- 0 hidden cross-extension dependency violations;
- 8 divergent extensions have no pre-existing external stable-ID references;
- the ninth references only `SRC-CELSUS-TRUE-DOCTRINE`;
- that record is canonically identical at the declared base and frozen rehearsal subject;
- referential precondition mismatches: 0.

This evidence is not self-authorizing; the independent disposition controls the gate.

## Candidate receipt requirements

The draft promotion candidate must contain a machine-readable receipt with at least:

```yaml
schema_version: on-theo.promotion-candidate.v1
status: DRAFT_UNMERGED_NOT_CANONICAL
source:
  repo: thebrazenbeard/on-theo
  rehearsal_head: <exact reviewed head>
  rehearsal_tree: <exact reviewed tree>
reviews:
  consolidation: <independent receipts>
  validator: <independent receipts>
  materialization: <independent receipts>
  rebase_exception: <independent disposition>
inputs:
  manifest_sha256: <sha256>
  extensions:
    - extension_id: <id>
      source_path: <path>
      archive_path: <path>
      source_blob: <git blob>
      sha256: <sha256>
outputs:
  registries:
    <path>: <sha256>
counts:
  sources: 131
  claims: 129
  concepts: 26
  transmissions: 23
  witnesses: 4
validation:
  pytest: <exact result>
  registry_validator: <exact result>
  archive_byte_check: PASS
  source_to_candidate_digest_match: PASS
effect_boundary:
  main_modified: false
  merged: false
  canonical_materialized: false
  downstream_cutover: false
```

## Exact verification gates before the PR is reviewable

Candidate construction must stop unless all are true:

1. source rehearsal head/tree still equal the independently reviewed subject;
2. every archived extension byte equals its reviewed input byte;
3. the archived manifest byte equals the reviewed input manifest byte;
4. all eight active output registry SHA-256 values exactly match the frozen rehearsal values;
5. all active `registry/extensions/*.yaml` files are absent;
6. the active materialized manifest has no extensions and says `canonical_materialized: false`;
7. registry validator passes with zero errors/findings/warnings;
8. full tests pass;
9. generated counts equal the reviewed counts;
10. no file outside the explicitly planned materialization/provenance set changes unexpectedly.

Any mismatch stops the candidate. Do not regenerate a different byte set and silently call it equivalent.

## Draft PR boundary

The eventual promotion candidate PR must remain:

- `DRAFT`
- `UNMERGED`
- `NOT CANONICAL`

It may be reviewed as the exact byte set that would be eligible for a later protected promotion decision.

It must not:

- merge to `main`;
- set canonical state true;
- delete historical branches or review evidence;
- alter downstream consumers such as Testament;
- imply that structural consistency establishes historical truth.

Those effects remain separately protected and require Patrick's explicit authority.
