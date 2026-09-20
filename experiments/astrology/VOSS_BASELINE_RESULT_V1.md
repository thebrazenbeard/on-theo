# Voss V2 Blind Baseline Result V1

Status: HELD_OUT_COMPLETE / SYNTHETIC_IDENTIFIABILITY_RESULT

## Bound sources

on-theo benchmark source:
`e608ed75fe0fe669f20a1c1d49b9c6d1a6f2c4b0`

Voss analyst frozen before held-out evaluation:
`thebrazenbeard/voss@d8660dc63e4813f37ed1722a2e867ee2c10b1a49`

Voss durable result:
`thebrazenbeard/voss@fe2f309539246d52ec24b83949f603d855657a1d`

Voss branch:
`revival/voss-forensic-analyst-v2-20260920`

## Protocol

Calibration:
- 20 labeled seeds per world;
- 160 calibration runs.

Held-out:
- 25 previously unused seeds per world;
- 200 runs total;
- 200 agents per run;
- 360 steps per run.

Model/features/confidence gates and the held-out seed schedule were frozen in the
Voss analyst commit before held-out evaluation.

## Forced-choice confusion

Columns:
S0, S1, S2, S3, S4, S5, S6, S7.

- S0: 8, 0, 3, 0, 14, 0, 0, 0
- S1: 0, 25, 0, 0, 0, 0, 0, 0
- S2: 2, 0, 15, 0, 8, 0, 0, 0
- S3: 0, 0, 0, 25, 0, 0, 0, 0
- S4: 6, 0, 8, 0, 11, 0, 0, 0
- S5: 0, 0, 0, 0, 0, 25, 0, 0
- S6: 0, 0, 0, 0, 0, 0, 24, 1
- S7: 0, 0, 0, 0, 0, 0, 2, 23

Exact:
156 / 200 = 78.0%.

## Evidence-gated Voss

Voss may return UNRESOLVED.

Resolved:
121 / 200.

Coverage:
60.5%.

Correct among resolved:
119 / 121 = 98.3471%.

Only two resolved errors occurred:
- one true S0 was called S2;
- one true S4 was called S2.

## Identifiability result

Under the current simulator and public observation surface:

### Strongly separable

- S1_PHYSICAL: 25 / 25 forced
- S3_RUNTIME: 25 / 25 forced
- S5_COMMON_CAUSE: 25 / 25 forced

### Mostly separable

- S6_CULTURAL_ONLY: 24 / 25 forced
- S7_WEAK_SIGNAL_CULTURAL: 23 / 25 forced

### Not reliably separable

- S0_NULL: 8 / 25 forced
- S2_NATAL_SEED: 15 / 25 forced
- S4_PLASTICITY: 11 / 25 forced

The S0/S2/S4 family achieved only 34 / 75 = 45.33% forced-choice accuracy.

The evidence-gated analyst therefore left almost all S0 and S4 runs unresolved
and most S2 runs unresolved.

## Interpretation

This is a negative result about the current observation design.

It shows that philosophical causal distinctions do not automatically create
observable statistical distinctions.

S4 is especially weakly exposed: the simulated plasticity mechanism changes a
latent learning-rate/random-walk process, while the public analyst receives
binary outcomes rather than the latent state. At the current horizon and sample
size it is largely indistinguishable from S0.

The experiment should be redesigned before another confirmatory held-out run.

Candidate changes must be specified before new evaluation seeds are opened:
- longer longitudinal horizons;
- larger populations;
- continuous repeated outcomes;
- predeclared plasticity-sensitive observables;
- controlled perturbation/intervention channels.

## Claim ceiling

This result concerns synthetic causal identifiability only.

It is not evidence for astrology, real celestial influence, simulation theory,
or a real hidden controller.
