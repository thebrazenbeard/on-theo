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

## Run

```bash
python experiments/astrology/reference_simulation.py \
  --world S5_COMMON_CAUSE \
  --agents 500 \
  --steps 720 \
  --seed 7 \
  --out simulation-output
```

Outputs:

- `world_manifest.json`
- `agent_births.csv`
- `celestial_state.csv`
- `agent_outcomes.csv`
- `cultural_claims.csv`
- `ground_truth_private.json`

The analyst should not receive `ground_truth_private.json` until after an
analysis submission is frozen.

## Important implementation choice

The astronomy generator is intentionally synthetic. Four orbital phases are
deterministic periodic functions. “Physical” channels are constructed from
inverse-square, inverse-cube and illumination-like proxies.

That is deliberate.

The first experiment tests **causal identifiability**, not astronomical fidelity.
A real ephemeris can replace the synthetic generator only after the inference
pipeline can correctly recover known synthetic ground truth.

## Reproducibility

The same world, agent count, step count and seed must produce byte-equivalent
logical records.

Run tests:

```bash
python experiments/astrology/test_reference_simulation.py
```

## Blinding rule

Generator role:
knows world type and ground truth.

Analyst role:
receives observable tables but not `ground_truth_private.json`.

Changing a controller rule after holdout evaluation invalidates the run.

## Research ceiling

A successful recovery demonstrates only that the specified synthetic causal
structure is recoverable.

It does not imply that the corresponding structure exists in humans or in the
real universe.
