# Chronology schema and coverage audit V1

Status: AUDIT / NON-CANONICAL / NO NEW HISTORICAL CLAIMS

Exact audited base:

- branch: `history/chronology`
- head: `71dec0ffb6602dfcdc7e3561e82fae276f720303`
- tree: `d6444ac8b84ab18dbb1e13e8429a83a7239ef5e4`

This audit checks the chronology lane's own contract against its current files. It does not supply missing historical dates and does not treat absence from this partial chronology as historical absence.

## Findings

### C01 — three-clock contract was not machine-represented

`chronology/README.md` requires three clocks where applicable:

1. claimed event date;
2. source/composition date;
3. physical witness date.

Before this audit successor, `chronology/entries.yaml` contained 18 entries. All 18 had `claimed_event_date` and `source_date`, while 18/18 omitted the `physical_witness_date` field entirely.

This is a schema-representation gap, not evidence that physical-witness dates are known. The repair in this branch adds the third field with explicit `unknown` values only; it does not invent dates.

### C02 — classification vocabulary drifted

The README declared seven entry types:

- `POLITICAL_HISTORY`
- `MATERIAL_EVIDENCE`
- `TEXT_COMPOSITION`
- `CLAIMED_EVENT`
- `TRADITION_DEVELOPMENT`
- `DOCTRINAL_FORMULATION`
- `RECEPTION_HISTORY`

The machine index currently uses eleven distinct labels. In addition to declared types, it uses:

- `HISTORICAL_RECONSTRUCTION`
- `PRIMARY_TEXT`
- `LATER_TRADITION`
- `TEXTUAL_TRANSMISSION`
- `SPECULATIVE_MODEL`
- `PROJECT_INFERENCE`

The README is updated to distinguish chronology entry types from additional project evidence classifications already used by the machine index.

### C03 — prose/machine coverage is not equivalent

`MASTER_TIMELINE.md` currently contains 42 timeline rows.

`entries.yaml` contains 18 machine entries.

Therefore the machine index is a partial index of the prose timeline, not a lossless machine rendering. No code or downstream consumer should assume row-for-entry completeness until an explicit synchronization rule exists.

### C04 — current machine chronology is tradition-skewed

Current `entries.yaml` tag counts are:

- christianity: 12
- judaism: 7
- greco-roman: 7
- jesus-movement: 5
- comparative: 3
- islam: 2

There are currently no machine entries tagged for the active Sumerian, Buddhist, Hindu, Shinto, Daoist/Taoist, or Norse/Ásatrú master lanes.

The prose master timeline likewise contains no literal Sumerian, Buddhist, Hindu, Shinto, Daoist/Taoist, Norse, or Ásatrú coverage.

This is a project-coverage gap only. It is not evidence about the antiquity, importance, or historical content of those traditions.

### C05 — evidence binding is weak

Machine chronology entries currently carry prose `notes` but do not bind their propositions to registry source IDs, witness IDs, or exact source-access records.

That makes the chronology useful as navigation but weak as an evidence-bearing integration layer.

## Applied safe repair in this branch

This audit branch makes only two contract-alignment changes:

1. every existing machine entry gains an explicit `physical_witness_date` object with `start: null`, `end: null`, and `precision: unknown`;
2. the README documents the additional classification labels already present in `entries.yaml`.

No event dates, source dates, confidence labels, contested flags, tradition tags, notes, or historical propositions are changed.

## Next implementation gates

The next chronology successor should not simply add more dates. It should first define and test:

- a machine schema for the three clocks;
- a controlled classification vocabulary;
- a prose-to-machine synchronization policy;
- evidence links to registry source/witness IDs where available;
- tradition coverage without forcing false symmetry;
- chronology entries sourced from each tradition's own internal reconstruction before comparative alignment.

Only after those controls exist should the lane be expanded with new Sumerian, Buddhist, Hindu, Shinto, Daoist, Norse/Ásatrú, and other chronology entries.
