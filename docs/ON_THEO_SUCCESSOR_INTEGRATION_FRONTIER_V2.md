# ON_THEO Successor Integration Frontier V2

Status: CURRENT_PORTFOLIO_AUDIT / SOURCE_INTEGRATION_REQUIRED / NO_CANONICAL_EFFECT

Recorded: 2026-09-19

## Executive correction

The previous frontier treated corpus-branch population as the next high-value task.

A fresh whole-repository comparison changes that priority.

ON_THEO's dominant bottleneck is now **state fragmentation across incompatible-but-valid source lineages**:

1. canonical `main` remains a minimal charter surface at `eedbcf660c2cfe6cff5636e798806b0cd3d56efc`;
2. the consolidation/materialization lineage culminates in PR #33 at `7ac78cb61ec216fe98347b33b6ff07c2a3aed81c`, materialized from a frozen 20-extension input;
3. the active research lineage culminates in PR #75 at `64bba017c763325e737f8fea31353f11f3396848`, with 40 active extensions;
4. user-created master/topic branches contain additional research content that is neither equivalent to #33 nor represented by #75.

Therefore neither PR #33 nor PR #75 is a complete current portfolio subject.

The next frontier is a **source-level successor integration cut**, followed by fresh validator/materialization work and exact-head review.

## Exact comparison: PR #33 versus PR #75

PR #33:
- head: `7ac78cb61ec216fe98347b33b6ff07c2a3aed81c`
- status: DRAFT / HOLD / UNMERGED / NOT CANONICAL
- active extension list after materialization: 0
- recorded applied input extensions: 20
- its exact validation and receipt evidence remain valid only for that frozen subject.

PR #75:
- head: `64bba017c763325e737f8fea31353f11f3396848`
- status at audit: OPEN / DRAFT / CLEAN / UNMERGED / NOT CANONICAL
- active source extensions: 40

Git comparison:
- relation: DIVERGED
- #75 has 117 commits not in #33
- #33 has 45 commits not in #75
- merge base: `7e354667770a6c4bed958a01c5ff843345a35b40`

This is not a stale-head problem that can be solved by fast-forwarding one lane.

## Extension-set topology

The frozen PR #33 applied set contains 20 extension IDs.

The PR #75 source manifest contains 40 extension IDs.

Intersection:
- 10 extension IDs.

Present in PR #33's applied set but absent from PR #75:
- EXT-SIMULATION-THEORY-V1
- EXT-SIMULATION-DISCRIMINABILITY-V2
- EXT-SECOND-TEMPLE-GRECO-ROMAN-V1
- EXT-ENOCH-DANIEL-PHILO-V1
- EXT-EARLY-CHRISTIAN-RABBINIC-V1
- EXT-LATE-ANTIQUE-CONTACT-ZONE-V1
- EXT-QURANIC-SYSTEM-V1
- EXT-YESHUA-HYPOTHESIS-MAP-V1
- EXT-QURAN-LATE-ANTIQUE-FEATURE-TESTS-V1
- EXT-EARLY-ISLAMIC-DEVELOPMENT-V1

Present in PR #75 but absent from PR #33's applied input:
- 30 later Sumerian, Mari, Ugaritic, Dumuzid/Baal, witness-control, and carrier-control extensions.

Union:
- **50 distinct extension IDs**.

Important:
`50` is an inventory ceiling, not authorization to concatenate manifests blindly.
Stable-ID collisions, supersessions, base ancestry, dependency closure, and semantic replacement rules must be checked on the successor subject.

## Topic/master branch portfolio

Sixteen user-created topic/master branches remain relevant inputs.

Direct descendants of current main:
- `chrisanity-master` — 2 commits ahead
- `judaism` — 2 ahead
- `sumerian` — 2 ahead
- `sim-theory` — 2 ahead
- `taoism` — 4 ahead
- `shinto` — 4 ahead
- `buddhism` — 5 ahead
- `asatru` — 4 ahead
- `hindu` — 4 ahead
- `islam` — 2 ahead
- `shinto-1` — 2 ahead

Diverged from current main:
- `history/chronology` — 3 ahead / 2 behind
- `synthesis/commonality` — 8 ahead / 2 behind
- `tradition/christianity` — 7 ahead / 2 behind
- `tradition/judaism` — 6 ahead / 2 behind
- `tradition/islam` — 7 ahead / 2 behind

These branches contain unique corpus, chronology, synthesis, or review material.

They are not noise, but they are also not automatically canonical inputs merely because they are user-created.

## Why branch population is no longer first

Continuing to deepen isolated branches would increase the integration deficit faster than the repository's ability to reconcile it.

The current risk is not lack of material.

The current risk is losing track of which mutually divergent source cuts jointly represent the intended project.

That creates four failure modes:

1. **newest-wins loss** — choosing #75 would silently drop ten earlier extensions and materialization/control work;
2. **materialized-wins loss** — choosing #33 would silently drop thirty later extensions plus subsequent research;
3. **branch-name authority** — importing all master/topic branches without conflict analysis would collapse review state and duplicate content;
4. **generated-state inversion** — using PR #33's generated materialized registry as the source base for V2 would make an old generated output outrank newer source-level evidence.

## Successor integration rule

The V2 integration must be constructed from source evidence, not by merging whichever branch looks newest.

Recommended source roles:

### A. Architecture/consolidation source
Use PR #28 / the consolidation lineage as architecture and integration provenance.

Do not assume its corpus is current.

### B. Frozen materialization evidence
Treat PR #33 as:
- exact proof that its 20-extension subject could be deterministically materialized;
- archived input/output evidence;
- validator/test provenance.

Do **not** treat its generated registry bytes as the current portfolio source of truth.

### C. Current research source
Treat PR #75's 40-extension stack as the current tip of the Sumerian→Dumuzid→Baal research lineage.

Do not treat it as a portfolio superset.

### D. Missing earlier extension source
Recover and revalidate the ten #33-only extension lineages at source level.

### E. Master/topic branch source
Inventory and reconcile unique content from the sixteen topic/master branches.

Files that are alternate hub summaries must be typed as:
- UNIQUE_PAYLOAD,
- SUPERSEDED_SUMMARY,
- DUPLICATE_EQUIVALENT,
- CONFLICTING_RECONSTRUCTION, or
- REVIEW_ONLY.

Do not import root-level master files merely because they exist.

## V2 construction sequence

1. Freeze exact input heads for:
   - PR #28 lineage;
   - PR #33 receipt subject;
   - PR #75;
   - all sixteen topic/master branches.

2. Build an immutable input inventory:
   - file path;
   - Git blob;
   - source branch/head;
   - semantic role;
   - supersession relation if any.

3. Reconstruct a **source-level** extension manifest over the 50-ID union candidate.

4. Validate:
   - duplicate IDs;
   - unresolved references;
   - base ancestry / explicit rebase equivalence;
   - dependency closure;
   - replacement/supersession correctness;
   - claim/source/witness collisions.

5. Reconcile topic/master branch payloads into durable namespaces without flattening competing reconstructions.

6. Run validator on the unmaterialized integrated source.

7. Only after source integration is stable, perform a fresh deterministic materialization rehearsal.

8. Obtain fresh exact-head independent reviews.

9. Construct a new byte-bound promotion candidate only from that reviewed V2 subject.

## Promotion-state correction

PR #33 remains a valid frozen candidate for its historical 20-extension subject.

It is **not** the current portfolio promotion candidate after the subsequent project expansion.

PR #75 remains a valid source/research successor for its exact research lineage.

It is **not** the current portfolio source superset.

No existing branch currently qualifies as:

`CURRENT_COMPLETE_ON_THEO_SOURCE_SUBJECT`.

Current classification:

`CURRENT_COMPLETE_ON_THEO_SOURCE_SUBJECT = NOT_YET_CONSTRUCTED`.

## Protected effects

This audit authorizes none of:
- merge to main;
- canonical materialization;
- closing unrelated research/master PRs;
- branch deletion;
- publication;
- downstream cutover.

It changes the work frontier, not effect authority.

## Exact next executable frontier

Construct **ON_THEO SOURCE INTEGRATION V2 INPUT INVENTORY**.

The first bounded implementation unit should:
- capture exact heads/blobs for the 50-extension union sources;
- capture the sixteen topic/master branch heads and unique payload paths;
- classify path collisions before copying bytes;
- emit a machine-readable inventory and collision report.

Only then create the actual V2 integration branch.
