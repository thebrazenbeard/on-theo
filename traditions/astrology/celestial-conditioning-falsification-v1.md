# Celestial Conditioning — Falsification Protocol V1

Classification: SPECULATIVE_MODEL / PRE-EXPERIMENT DESIGN

## Target hypothesis family

The motivating idea is that celestial configuration could alter the equivalent of computational model parameters or runtime state in biological agents.

This file turns that idea into competing models that can lose.

## Variables

Let:

C(t, x) = astronomical state vector at time t and location x.

G(t, x) = ordinary physical celestial variables such as gravitational acceleration, tidal gradient and illumination.

A(t) = conventional astrological feature vector under one frozen system.

E(t, x) = terrestrial environmental variables such as season, temperature, photoperiod and social scheduling.

H = hidden controller state, included only in speculative simulation models.

Y = measurable human outcome.

## H0 — no celestial information beyond terrestrial covariates

Y = F(E, demographics, history, noise)

Prediction:
Adding C, G or A produces no reproducible out-of-sample improvement.

## H1 — ordinary physical mediation

Y = F(E, G, demographics, history)

Prediction:
Effects vary continuously with physical magnitude and geometry.

For gravity:
acceleration term scales approximately with M/r².

For tidal effects:
gradient scales approximately with M/r³.

Therefore a literal gravity hypothesis must track:
- mass;
- distance;
- direction;
- time;
- local competing gravitational sources.

A categorical sign boundary has no privileged role unless separately justified.

## H2 — birth-seed model

Agent parameters at birth depend partly on celestial state:

theta_0 = Init(genetics, prenatal_development, environment, f(C_birth))

Prediction:
Stable differences correlate with birth configuration even after later transits are ignored.

Strong test:
siblings/twins and geographically/time-separated births with carefully modeled prenatal/seasonal confounds.

## H3 — runtime-conditioning model

Current state depends partly on current celestial configuration:

z_t = Runtime(theta, history, environment, f(C_t))

Prediction:
Repeated within-person measurements should covary with prespecified celestial variables.

This model is better tested longitudinally than by static personality questionnaires.

## H4 — learning/plasticity-gate model

Celestial state modifies how experience updates durable parameters:

theta_(t+1) = Update(theta_t, experience_t, f(C_t))

Prediction:
The same experience produces different lasting updates under different prespecified celestial states.

This is distinct from H3.

## H5 — traditional astrological feature model

Y = F(A, covariates)

Prediction:
Frozen traditional features such as aspects, houses or dignities predict outcomes above physical variables and terrestrial baselines.

Required:
The school/system must be locked before analysis.

## H6 — hidden common-cause/controller model

H -> C
H -> Y

Celestial configuration is a visible indicator or clock, not necessarily the physical cause.

Prediction requirement:
H6 is scientifically empty unless a specific mapping f(C) is fixed before testing and produces results not expected under H0-H5.

Guard:

ABILITY_TO_EXPLAIN_ANY_RESULT = FAILURE_TO_PREDICT.

## Information-channel discriminants

A useful controller-style hypothesis should predict something physically surprising but statistically specific.

Examples of discriminants:
- categorical phase changes at a defined astronomical boundary despite smooth gravitational variables;
- equal predictive effects from bodies with radically different physical force but equivalent code roles under the frozen model;
- lag structure tied to symbolic/configuration state rather than physical propagation or season;
- reproducible interaction rules that are arbitrary from known physics but fixed before data access.

These would still not prove simulation.

They would only reject some simpler models if replicated.

## Birth-chart versus transit separation

Do not combine:
- natal initialization;
- current transit conditioning;
- cumulative exposure;
- event-election effects.

Each creates different predictions.

## Recommended first empirical design

Use a large longitudinal dataset with repeated measures.

Before accessing outcomes:

1. Freeze one astronomical ephemeris implementation.
2. Freeze one astrological representation if testing H5/H6.
3. Define primary outcomes.
4. Define physical covariates.
5. Define terrestrial/environmental covariates.
6. Define training and untouched holdout periods.
7. Register all interaction terms.
8. Set minimum effect size of interest.

Compare models:

M0 = E + demographics + history
M1 = M0 + G
M2 = M0 + raw C
M3 = M0 + frozen A
M4 = M0 + prespecified controller-code f(C)

Use out-of-sample predictive improvement rather than narrative fit.

## Simulation experiment

Within the future on-theo world model, create agents under known ground truth:

S0: no celestial coupling
S1: gravitational coupling
S2: natal seed coupling
S3: runtime coupling
S4: plasticity coupling
S5: hidden controller/common cause
S6: no coupling + cultural pattern seeking

Then give downstream analyst-agents only in-world observations.

Question:

Can they correctly infer which world they inhabit?

This is the cleanest way to test whether an astrology-like knowledge system can:
- emerge without a real effect;
- preserve a real correlation with the wrong mechanism;
- distinguish direct cause from system clock;
- degrade or improve across cultural transmission.

## Evidence ceiling

No current evidence in the branch establishes H2-H6.

This document is a falsification framework, not support for the hypothesis.
