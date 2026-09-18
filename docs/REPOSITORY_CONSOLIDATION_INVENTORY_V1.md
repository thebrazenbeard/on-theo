# On-Theo Repository Consolidation Inventory V1

Status: DRAFT / FILE-LEVEL INVENTORY / NO MERGE AUTHORITY  
Audit parent: `docs/REPOSITORY_CONSOLIDATION_AUDIT_V1.md`  
Inventory cut: 2026-09-18

## 1. Candidate source baseline

For **candidate construction only**, the most content-rich single lineage inspected is:

`corpus/sumerian-religion-v1-20260917@7e354667770a6c4bed958a01c5ff843345a35b40`

It contains 50 files and already includes the main provenance spine, Panthera research chain, broad-mythos foundation, Egyptian/Vedic work, early Buddhism, world-traditions expansion, and Sumerian overview.

Using this as a construction baseline does **not** mean it is accepted, canonical, or preferred over parallel reviewed material. It is simply the cheapest tree from which to prove lossless consolidation.

## 2. Material missing from the Sumerian lineage

Exact tree comparison found **65 distinct files** present on important open-PR heads but absent from the Sumerian lineage.

These files fall into the following groups.

### Review artifacts — 4 files

From PR #5 review branch:
- `reviews/pr1/hephaestus-architecture-role-pass.md`
- `reviews/pr1/masa-hostile-role-pass.md`
- `reviews/pr1/mune-readback-role-pass.md`

From PR #7 review branch:
- `reviews/pr6/hephaestus-architecture-role-pass.md`

These must remain review evidence with their original exact-head scope. Importing the files cannot promote their result to a different candidate head.

### Second Temple / Greco-Roman / early-Christian / rabbinic / Late Antique / Qur'anic line

The Sumerian lineage does not contain the parallel corpus line carried through PRs #12-16.

Missing examples include:
- `comparative/second-temple-internal-plurality-v1.md`
- `comparative/second-temple-greco-roman-contact-zone-v1.md`
- `comparative/early-christian-rabbinic-trajectories-v1.md`
- `comparative/late-antique-near-east-arabia-contact-zone-v1.md`
- `traditions/second-temple-judaism/overview-v1.md`
- `traditions/second-temple-judaism/enochic-watchers-v1.md`
- `traditions/second-temple-judaism/danielic-apocalypse-v1.md`
- `traditions/second-temple-judaism/philo-alexandria-v1.md`
- `traditions/greco-roman/overview-v1.md`
- `traditions/early-christianity/overview-v1.md`
- `traditions/rabbinic-judaism/overview-v1.md`
- `traditions/late-antique-christianity/overview-v1.md`
- `traditions/late-antique-arabia/overview-v1.md`
- `traditions/sasanian-iran/overview-v1.md`
- four Qur'anic internal-system packets.

Missing registry extensions include:
- `registry/extensions/second-temple-greco-roman-v1.yaml`
- `registry/extensions/enoch-daniel-philo-v1.yaml`
- `registry/extensions/early-christian-rabbinic-v1.yaml`
- `registry/extensions/late-antique-contact-zone-v1.yaml`
- `registry/extensions/quranic-system-v1.yaml`

### Qur'an / Late Antique feature tests — 2 files

PR #17 uniquely adds:
- `comparative/quran-late-antique-feature-tests-v1.md`
- `registry/extensions/quran-late-antique-feature-tests-v1.yaml`

### Early Islamic development — 6 files

PR #19 uniquely adds:
- `comparative/quran-early-islam-development-v1.md`
- `registry/extensions/early-islamic-development-v1.yaml`
- `traditions/early-islam/overview-v1.md`
- `traditions/early-islam/material-documentary-v1.md`
- `traditions/early-islam/sira-hadith-formation-v1.md`
- `traditions/early-islam/law-authority-confessions-v1.md`

### Simulation-theory lane — 15 files

The PR #18 -> PR #22 line adds simulation material absent from Sumerian, including:
- two comparative files;
- simulation research design/plan;
- two registry extensions;
- eight simulation-theory research packets;
- hostile-review/source-readback artifacts.

This lane remains `SPECULATIVE_MODEL`/model-analysis material and must retain its evidence firewall when consolidated.

### Yeshua hypothesis/review lane — 3 files beyond shared corpus dependencies

The PR #20 -> PR #23 line uniquely adds:
- `registry/extensions/yeshua-hypothesis-map-v1.yaml`
- `research/yeshua/hypothesis-map-v1.md`
- `reviews/yeshua-hypothesis-map-v1-hostile-review.md`

Its hostile review remains exact-head scoped.

### Registry validator/tooling — 10 files

PR #24 contains ten files absent from Sumerian:
- `.github/workflows/validate-registries.yml`
- `docs/superpowers/plans/2026-09-17-registry-validator-v1.md`
- `pytest.ini`
- `requirements-dev.txt`
- `scripts/validate_registry.py`
- `tests/test_registry_cli.py`
- `tests/test_registry_validator.py`
- `tests/test_registry_workflow.py`
- `tools/on_theo_registry/__init__.py`
- `tools/on_theo_registry/validator.py`

These should be present in the same tree as the corpus before structural validation can mean anything about that tree.

## 3. Original thematic-lane material missing from the Sumerian lineage

The five original long-lived research lanes contribute **31 additional unique files** that are not present in the Sumerian lineage.

Counts:
- Judaism: 6
- Christianity: 7
- Islam: 7
- synthesis/commonality: 8
- chronology: 3

These paths are mechanically non-colliding with the current corpus paths.

They still require semantic reconciliation because some prose may overlap newer packets or represent earlier research states.

Do not discard them merely because newer branch names exist.

## 4. Expansion queue sibling — 1 missing file

`corpus/global-expansion-queue-v1-20260917@cd588c7cabc210f8ae8eb43c148170872aa4b9ac`

contributes:

- `docs/CORPUS_EXPANSION_QUEUE_V2.md`

This file is absent from the Sumerian lineage because the queue and world-traditions branches forked as siblings from PR #25.

## 5. Minimum lossless union size

Relative to the 50-file Sumerian baseline:

- 65 distinct files from parallel PR/review/tooling lines;
- 31 unique files from original thematic lanes;
- 1 expansion-queue file.

That is **97 additional distinct paths** before same-path reconciliation.

A mechanically lossless union therefore contains at least:

`50 + 97 = 147 distinct file paths`

before any new consolidation receipt, updated branch map, or integration documentation is added.

This number is an inventory floor, not a canonical target.

## 6. Same-path collision classes

The file inventory found a small number of repeated paths with different blobs.

### `README.md`

Validator branch blob:
`977f264e04c8a74c07a9b28d6dec13057bcde4d7`

Sumerian/main-family blob:
`b56d41403ca190642872accbf62f3235f2fbda58`

Disposition:
`ADDITIVE_RECONCILIATION`

The validator README is the ordinary README plus a registry-validation usage section. No contradictory project semantics were observed in that difference.

Candidate action:
preserve the validation instructions, then update the branch-architecture section separately to describe the successor architecture.

### `registry/concepts.yaml`

PR #5 review-line blob:
`b0f958f86da1e68af23790cde8794aa14f263014`

Sumerian blob:
`ce9311621561ba7b4ff228d41795dc6a8dc73857`

Disposition:
`LATER_HARDENING_SUPERSET`

The Sumerian-line version adds explicit proposed-contract status, an incomplete-coverage state, and the guard that absence of a concept record is not negative evidence.

Candidate action:
retain the hardened Sumerian version unless exact hostile review finds a semantic regression.

### `registry/extension-manifest.yaml`

This path has materially different additive tails across independent corpus branches.

Examples:
- Sumerian line includes broad mythos, Deut32 witness control, Egyptian/Vedic, and early Buddhist extensions.
- simulation/Qur'anic line includes broad mythos, Deut32, Second Temple, Enoch/Daniel/Philo, early Christian/rabbinic, Late Antique, Qur'anic, and simulation extensions.

Disposition:
`DIVERGENT_ADDITIVE_REGISTRY`

Candidate action:
**do not choose one file wholesale.**
Construct an ID-level union, preserve each extension's original `declared_base`, `introduced_at`, and `depends_on`, then run topological/dependency validation.

The resulting consolidated manifest is a new review subject.

### `registry/source-access.yaml`

This path also evolved independently.

Examples:
- Sumerian line adds ancient Near Eastern/Zoroastrian access records.
- parallel Second Temple/Qur'anic/simulation lines add Josephus, DSS, Greek/Roman, Enochic, Danielic, Philonic, and related access records.

Disposition:
`DIVERGENT_ADDITIVE_REGISTRY`

Candidate action:
perform source-ID-level union.
For duplicate IDs:
- identical records may deduplicate;
- non-identical records must stop consolidation until explicitly reconciled;
- never apply newest-wins.

## 7. Candidate construction strategy

The lowest-risk construction sequence currently appears to be:

1. create an isolated candidate from exact Sumerian head
   `7e354667770a6c4bed958a01c5ff843345a35b40`;
2. add the 97 missing unique paths with exact source-branch attribution;
3. reconcile `README.md`;
4. preserve the hardened `registry/concepts.yaml`;
5. construct deterministic union versions of:
   - `registry/extension-manifest.yaml`
   - `registry/source-access.yaml`;
6. update `docs/BRANCH_MAP.md` to make directories the durable content model and branches work/review surfaces;
7. add a machine-readable consolidation receipt mapping every imported path to source branch + exact head + source blob;
8. run validator/tests against the resulting exact tree;
9. compare candidate tree against every source head and prove no unique artifact disappeared;
10. submit the candidate to architecture/provenance/hostile review.

Candidate construction is not materialization or merge.

## 8. Required receipt shape

A future consolidation receipt should minimally record:

```yaml
schema: on-theo.consolidation-receipt.v1
candidate_head: <exact SHA>
candidate_tree: <exact tree SHA>
source_heads:
  - branch: <branch>
    sha: <exact SHA>
artifacts:
  - path: <candidate path>
    source_branch: <branch>
    source_head: <SHA>
    source_blob: <blob SHA>
    operation: IDENTICAL | ADD | RECONCILE
collisions:
  - path: <path>
    input_blobs: []
    resolution: <typed resolution>
validator:
  exact_head: <candidate SHA>
  result: PASS | FAIL
  unresolved_references: <integer>
  duplicate_ids: <integer>
review_state:
  architecture: <state>
  provenance: <state>
  hostile: <state>
```

No receipt may imply historical truth merely because file/registry consolidation succeeded.

## 9. Testament dependency boundary

`thebrazenbeard/testament` remains external.

Until On-Theo has an accepted consolidated head:
- Testament should pin immutable On-Theo commit/path references for any consumed evidence;
- it should not treat `main` as containing the draft corpus;
- it should not track `corpus/sumerian-religion-v1-20260917` or another mutable branch as an unqualified canonical dependency;
- Testament-originated interpretation must not flow back into On-Theo source claims without normal On-Theo evidence classification and review.

This prevents the branched-chat workflow from creating a provenance loop.

## 10. Exact next work

Build the isolated consolidation candidate only after a final ID-level collision check across the divergent registry files.

The immediate technical subtask is therefore:

**extract and compare all extension IDs and source-access IDs across the Sumerian, Second Temple/Qur'anic, simulation, Yeshua, and validator lines; prove which entries are identical, unique, or conflicting before any candidate write.**
