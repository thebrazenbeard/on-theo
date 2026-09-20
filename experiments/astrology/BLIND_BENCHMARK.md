# Blind Celestial-Conditioning Benchmark V1

Classification: SPECULATIVE_MODEL / CAUSAL-IDENTIFIABILITY TEST

## Why this exists

The original reference simulator was useful for development but was not safe for
blind inference.

Its ordinary single-run outputs exposed:
- the world label in the manifest;
- the random seed;
- latent base and current trait values;
- the synthetic natal signal;
- model-generated outcome probability;
- cultural belief state.

Hiding only `ground_truth_private.json` was therefore insufficient.

The blind benchmark uses a strict public projection.

## Public analyst surface

For each run, the analyst may receive only:

### `manifest.json`
- opaque run id;
- number of agents;
- number of steps;
- SHA-256 commitment to the hidden seed;
- filenames.

It does **not** identify the world class.

### `agent_births.csv`
- agent id;
- birth time.

It does not expose:
- base trait;
- initialized trait;
- birth-signal hash.

### `celestial_state.csv`
- four synthetic orbital longitudes;
- two distance proxies;
- illumination;
- inverse-square-style physical proxy;
- inverse-cube-style tidal proxy;
- angular categorical code;
- sector/sign-like code.

The hidden-controller variable is excluded.

### `agent_outcomes.csv`
- time;
- agent id;
- binary outcome;
- known environmental covariate.

It does not expose:
- latent trait;
- exact model probability;
- cultural-belief state.

### `cultural_claims.csv`
Observable in-world cultural claims, when present.

This file is intentionally public because cultural transmission is itself part
of worlds S6 and S7.

## Private generator surface

`private/answer_key.json` contains:
- run-to-world mapping;
- run seed;
- coupling type.

The public benchmark index contains a SHA-256 commitment to the canonical answer
key. That permits later verification that the answer key was not changed after
analyst submissions were frozen.

## Generate

```bash
python experiments/astrology/blind_benchmark.py \
  --out blind-benchmark \
  --repeats 10 \
  --agents 500 \
  --steps 720 \
  --benchmark-seed 23
```

This yields 80 shuffled runs: ten from each S0-S7 class.

Do not give the analyst the `private/` directory.

## Analyst submission

Use the collection structure in
`benchmark-submissions.schema.json`.

Every run classification must include:
- predicted world;
- model description;
- holdout metrics;
- causal claim;
- `frozen_before_unblinding: true`.

The boolean alone does not prove chronology. For a serious run, persist the
submission or its cryptographic digest on a durable timestamped surface before
revealing the private answer key.

## Score

```bash
python experiments/astrology/score_benchmark.py \
  --public-index blind-benchmark/public/benchmark.json \
  --answer-key blind-benchmark/private/answer_key.json \
  --submissions submissions.json \
  --out score_report.json
```

The scorer verifies the answer-key commitment when `--public-index` is supplied.

Outputs include:
- coverage;
- exact classification accuracy;
- unresolved count;
- per-world recall;
- full confusion matrix.

## Scientific interpretation

A confusion matrix is the point.

If an analyst repeatedly confuses:
- S1 physical with S3 runtime;
- S3 runtime with S5 hidden common cause;
- S0 null with S6 cultural-only;
- S2 natal seed with S7 weak-signal cultural,

then those world classes are not yet observationally identifiable under the
current data-generating process.

The correct response is to redesign the experiment or lower the claim ceiling,
not to reinterpret the errors as success.

## Current ceiling

This benchmark can test whether synthetic causal structures are distinguishable
from their observable consequences.

It cannot establish that:
- real astrology works;
- celestial bodies affect human psychology;
- the universe is simulated;
- a hidden controller exists.
