# Celestial Conditioning Reference Experiment

Classification: SPECULATIVE_MODEL / EXPERIMENTAL INFRASTRUCTURE

This directory implements the synthetic-world experiment described in
`traditions/astrology/celestial-conditioning-simulation-spec-v1.md`.

It does **not** model the real Solar System and it does **not** provide evidence
that astrology or simulation theory is true.

## Purpose

The experiment asks whether an observer can distinguish worlds where celestial
state is:

- irrelevant;
- connected through an ordinary continuous physical proxy;
- used only at agent initialization;
- used as runtime conditioning;
- used to gate learning/plasticity;
- correlated through a hidden common cause;
- culturally believed despite no true coupling;
- weakly real but distorted by cultural transmission.

## World classes

- `S0_NULL`
- `S1_PHYSICAL`
- `S2_NATAL_SEED`
- `S3_RUNTIME`
- `S4_PLASTICITY`
- `S5_COMMON_CAUSE`
- `S6_CULTURAL_ONLY`
- `S7_WEAK_SIGNAL_CULTURAL`

## Development run

```bash
python experiments/astrology/reference_simulation.py \
  --world S5_COMMON_CAUSE \
  --agents 500 \
  --steps 720 \
  --seed 7 \
  --out simulation-output
```

Development outputs include:

- `world_manifest.json`
- `agent_births.csv`
- `celestial_state.csv`
- `agent_outcomes.csv`
- `cultural_claims.csv`
- `ground_truth_private.json`

### Important correction

The development output is **not a blind analyst surface**.

It intentionally exposes useful debugging fields, including the selected world
in its manifest and latent/internal variables in some tables.

Do not use development output for a causal-identification benchmark.

Use `blind_benchmark.py` instead.

## Blind benchmark

Protocol:
`experiments/astrology/BLIND_BENCHMARK.md`

Generate shuffled unlabeled runs:

```bash
python experiments/astrology/blind_benchmark.py \
  --out blind-benchmark \
  --repeats 10 \
  --agents 500 \
  --steps 720 \
  --benchmark-seed 23
```

Only `blind-benchmark/public/` is analyst-visible.

The private answer key is committed by SHA-256 in the public benchmark index so
it can be verified after predictions are frozen.

Score frozen submissions:

```bash
python experiments/astrology/score_benchmark.py \
  --public-index blind-benchmark/public/benchmark.json \
  --answer-key blind-benchmark/private/answer_key.json \
  --submissions submissions.json \
  --out score_report.json
```

The score report contains:
- coverage;
- exact classification accuracy;
- unresolved count;
- per-world recall;
- a full confusion matrix.

## Important implementation choice

The astronomy generator is intentionally synthetic. Four orbital phases are
deterministic periodic functions. “Physical” channels are constructed from
inverse-square, inverse-cube and illumination-like proxies.

That is deliberate.

The first experiment tests **causal identifiability**, not astronomical fidelity.
A real ephemeris can replace the synthetic generator only after the inference
pipeline can correctly recover known synthetic ground truth.

## Reproducibility

Run development tests:

```bash
python experiments/astrology/test_reference_simulation.py
```

Run blind-boundary/scoring tests:

```bash
python experiments/astrology/test_blind_benchmark.py
```

## Research ceiling

A successful recovery demonstrates only that the specified synthetic causal
structure is recoverable.

It does not imply that the corresponding structure exists in humans or in the
real universe.
