# On-Theo Repository Consolidation Audit V1

Status: DRAFT / INTEGRATION DESIGN / NO MERGE AUTHORITY  
Cut: 2026-09-18  
Canonical base inspected: `main@eedbcf660c2cfe6cff5636e798806b0cd3d56efc`

## Purpose

This audit pauses corpus expansion long enough to reconcile the repository's actual research graph with its intended provenance architecture.

The research content is not being rejected. The problem is structural: On-Theo now contains substantially more valid draft research than its branch/PR architecture can represent cleanly.

No merge, canonical promotion, branch deletion, PR closure, or protected effect is authorized by this document.

## 1. Live state at audit cut

Observed live state:

- 35 branches.
- 26 open pull requests.
- all 26 open PRs are drafts.
- `main` contains 5 files: project charter/method/schema/branch map/backlog.
- `corpus/world-traditions-expansion-v1-20260917` contains 49 files and is 52 commits ahead of `main`.
- `corpus/sumerian-religion-v1-20260917` contains 50 files and adds one commit above the world-traditions branch.
- PR #26 is based on the world-traditions branch rather than `main`.

The repository therefore has a large draft corpus but a very small canonical surface.

## 2. PR graph is a dependency graph, not 26 independent candidates

The open PR list is mostly a stacked research graph.

Examples:

- PR #1 introduces the V1 provenance integration spine.
- PRs #2-10 stack research and architecture work over that spine.
- PR #11 begins broad mythos expansion from the Panthera/wordplay chain.
- later corpus PRs stack through Second Temple, Christian/rabbinic, Late Antique, Qur'anic, Egyptian/Vedic, and Buddhist branches.
- simulation and Yeshua branches fork from intermediate corpus states.
- PR #26 adds Sumerian research on top of an intermediate branch that itself has no PR.

This means a PR number is not a self-contained unit of repository state. Review and future materialization must respect ancestry.

## 3. Unrepresented live branches

Nine live branches are not current open-PR heads:

- `main`;
- `tradition/judaism`;
- `tradition/christianity`;
- `tradition/islam`;
- `synthesis/commonality`;
- `history/chronology`;
- `corpus/global-expansion-queue-v1-20260917`;
- `corpus/world-traditions-expansion-v1-20260917`;
- `state/on-theo-chat-continuation-20260917-2025`.

Some are intentionally long-lived lanes or state branches. Two are material corpus branches that affect current research ancestry.

### World-traditions branch

`corpus/world-traditions-expansion-v1-20260917@5e6db919ab3b40615c14257e2a56751579cb72fe`

This branch adds:

- `docs/WORLD_TRADITIONS_EXPANSION_V1.md`;
- `research/source-maps/world-traditions-expansion-v1.md`.

It is the base of PR #26 but has no PR of its own.

### Global expansion queue

`corpus/global-expansion-queue-v1-20260917@cd588c7cabc210f8ae8eb43c148170872aa4b9ac`

This branch adds:

- `docs/CORPUS_EXPANSION_QUEUE_V2.md`.

It and the world-traditions branch are siblings off PR #25's head, not one lineage.

Comparison:

- world-traditions is 2 commits ahead and 1 commit behind the queue branch;
- Sumerian is 3 commits ahead and 1 commit behind the queue branch.

Therefore the current Sumerian research branch does **not** contain the queue document that defined the expansion frontier.

## 4. Validator/corpus split

The executable registry validator is isolated on:

`work/registry-validator-v1-20260917@b4cddd100007d4b2c90fdce4d519a4e1b5b7d3ed`

Relative to `main`, that branch is 40 commits ahead and includes:

- validator implementation;
- CLI;
- tests;
- CI workflow;
- `pytest.ini`;
- development requirements;
- registry contract work.

The current world-traditions branch is 52 commits ahead of `main`.

Direct comparison shows the two branches have diverged:

- world-traditions: 24 commits ahead of validator;
- world-traditions: 12 commits behind validator.

The validator therefore exists, but the newest corpus branch does not inherit the validator toolchain.

This is a structural defect because validation capability and the corpus it is intended to validate are evolving on separate lines.

## 5. Original thematic lanes remain unreconciled

The original repository architecture defined long-lived research lanes:

- `tradition/judaism`;
- `tradition/christianity`;
- `tradition/islam`;
- `synthesis/commonality`;
- `history/chronology`.

Those branches still contain unique files.

Against current `main`:

- Judaism lane: 6 unique files;
- Christianity lane: 7 unique files;
- Islam lane: 7 unique files;
- synthesis lane: 8 unique files;
- chronology lane: 3 unique files.

Each lane has also diverged from `main` and is two main commits behind.

The newer V1 registry/corpus architecture says these lanes remain useful, but their content has not been explicitly materialized into or reconciled with the new integration spine.

On-Theo therefore currently has two overlapping architectures:

1. long-lived thematic branches as research stores;
2. short-lived stacked corpus/registry branches as the newer integration model.

That ambiguity should be resolved before further expansion.

## 6. Research-state assessment

The structural finding is not that the research is invalid.

Current strengths include:

- explicit evidence classes;
- event/source/witness date separation;
- source identity separated from physical witness identity;
- typed transmission relations;
- hostile/alternative-explanation review requirements;
- exact-head review semantics;
- source-access/preservation modeling;
- disciplined separation of simulation theory from historical evidence;
- broad-corpus reconstruction before comparison.

The failure mode is repository topology: increasingly good epistemic controls are being stored in a graph that is getting harder to reason about.

## 7. Proposed successor architecture

### 7.1 Canonical content lives in directories, not permanent research branches

Long-lived branches should stop serving as the only storage location for substantive accepted material.

Target canonical directory families on `main`:

- `traditions/`
- `chronology/`
- `comparative/`
- `research/`
- `registry/`
- `synthesis/`
- `tools/`
- `tests/`
- `docs/`

Branches remain work/review surfaces, not durable epistemic namespaces.

### 7.2 One explicit consolidation candidate

After audit/review, construct one isolated integration candidate that reconciles:

1. the current corpus ancestry through the Sumerian head;
2. the missing global expansion queue;
3. the validator/tooling branch;
4. unique files from the five original thematic lanes;
5. exact registry-extension application semantics;
6. current documentation/branch map.

Do not materialize registry extensions merely by copying them into one tree. Materialization still requires the manifest invariants and validation receipts.

### 7.3 Stop arbitrary PR stacking

Until consolidation is resolved:

- do not create new tradition-expansion branches on arbitrary prior PR heads;
- do not treat later PR ancestry as implicit acceptance of earlier PRs;
- do not use an unrepresented intermediate branch as a hidden dependency.

After a consolidation candidate exists, new research should fork from one explicitly named accepted/integration base.

### 7.4 Bring validation and corpus together before promotion

The consolidation candidate must contain the validator toolchain and the corpus being validated in the same exact tree.

Required checks before any promotion claim:

- registry validator;
- direct CLI validation;
- test suite;
- unresolved-reference count;
- duplicate-ID count;
- extension dependency/order check;
- exact-head review;
- citation/readback spot checks for material corpus additions.

A green validator proves structural consistency, not historical truth.

## 8. Proposed integration sequence

This is a plan, not merge authority.

Phase A — inventory/freeze:
1. freeze new corpus expansion temporarily;
2. record every branch/PR exact head;
3. classify each unique file as architecture, registry, research, review, chronology, synthesis, tooling, or state-only;
4. identify path/content collisions.

Phase B — isolated candidate construction:
1. choose a single exact source base;
2. incorporate the global queue sibling;
3. incorporate validator/tooling work;
4. reconcile thematic-lane unique files;
5. preserve all source/witness/review provenance;
6. update branch map and architecture docs to describe the successor model.

Phase C — deterministic validation:
1. run registry validator/tests;
2. inspect extension-manifest correctness;
3. verify no unique file disappeared;
4. compare candidate against every source branch;
5. emit a consolidation receipt mapping source branch/head -> candidate artifact paths.

Phase D — hostile review:
1. architecture review;
2. provenance review;
3. corpus loss/duplication review;
4. review of any semantic conflict introduced during reconciliation.

Phase E — Patrick decision:
- only after the exact candidate is reviewed may Patrick decide whether to authorize merge/canonical promotion.
- stale review does not transfer if the candidate moves.

## 9. PR disposition after a future canonical consolidation

Do not delete history.

If a consolidation candidate is eventually merged, old PRs may be marked superseded/closed with explicit pointers to the materialization receipt rather than pretending each stacked PR independently merged.

Review records and failed/limited reviews remain historical evidence.

## 10. External dependency watch: Testament

Patrick reported that a branched chat is creating `thebrazenbeard/testament` and may use On-Theo as a dependency.

At this audit cut:

- `thebrazenbeard/testament` exists;
- its repository size is effectively empty/currently unpopulated;
- GitHub code search returned no current `testament` reference inside On-Theo, although search indexing reported incomplete results.

Boundary:

- Testament is external to On-Theo unless an explicit interface is introduced.
- Testament work does not gain write authority over On-Theo.
- On-Theo should not import Testament state merely because Testament consumes On-Theo.
- If Testament needs stable On-Theo material before canonical consolidation, it should pin exact immutable On-Theo repository/commit/path references rather than track a mutable branch by implication.
- Any future bidirectional dependency must be explicit to avoid circular provenance.

## 11. Immediate next frontier

Before adding another religious corpus packet:

1. produce the exact file/branch consolidation inventory;
2. identify collisions between validator, corpus, and thematic lanes;
3. design the isolated consolidation candidate;
4. only then resume Sumerian registry materialization or the next world-tradition expansion.

The current research remains preserved. The objective is to make the repository structure finally deserve the epistemic discipline of the research it contains.
