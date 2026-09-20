# Celestial Conditioning Simulation Implementation Spec V1

Classification: SPECULATIVE_MODEL / EXPERIMENTAL DESIGN

Status: IMPLEMENTATION-READY SPECIFICATION, NOT IMPLEMENTED

## Goal

Create synthetic worlds in which the true causal relationship between celestial
state and agents is known, then test whether downstream observers can correctly
infer that relationship.

The purpose is not to make a visually convincing astrology simulator.

The purpose is to test identifiability.

## Core question

Can an intelligent population living inside a governed world distinguish:

- no celestial effect;
- ordinary physical influence;
- natal initialization;
- runtime conditioning;
- learning-rate/parameter-update conditioning;
- hidden common cause;
- culturally generated false astrology?

## World state

At simulation step t:

W_t = {
  astronomy_t,
  environment_t,
  controller_t,
  agents_t,
  culture_t
}

### Astronomy

Deterministic ephemeris-like state:

C_t = {
  orbital_longitudes,
  angular_relations,
  distances,
  illumination,
  rise_set_geometry,
  local_sky_coordinates
}

The first implementation does not need a physically perfect Solar System.

It needs:
- deterministic reproducibility;
- continuous variables;
- categorical features derivable from the same state;
- enough structure to distinguish physics-like and code-like coupling.

### Physical channel

G_t includes:
- inverse-square force proxies;
- inverse-cube tidal proxies;
- illumination;
- periodic environmental signals.

This creates a known ordinary-physics baseline.

### Agents

Each agent has:

theta_i:
- stable latent traits;
- policy parameters;
- learning parameters.

z_i,t:
- transient internal state.

history_i,t:
- experiences and actions.

observable outcomes:
- choices;
- performance;
- affect-like scalar states;
- social behavior;
- health-like synthetic variables.

No claim is made that these abstractions reproduce actual human psychology.

## Experimental worlds

### S0 — Null world

Celestial state has no causal effect on agents.

Culture can still invent astrology.

Purpose:
measure false-system emergence under pattern seeking alone.

### S1 — Physical-only world

Agents are affected only by G_t.

Purpose:
test whether observers infer a physics-like continuous relationship or invent
categorical astrological rules.

### S2 — Natal-seed world

theta_i,0 += f(C_birth)

Purpose:
test whether stable birth-correlated traits can be recovered.

### S3 — Runtime-conditioning world

z_i,t += f(C_t)

Purpose:
test transit-like transient effects.

### S4 — Plasticity-gate world

learning_rate_i,t = base_lr_i * g(C_t)

Purpose:
test whether celestial state changes how experiences become durable parameters.

### S5 — Hidden-common-cause world

H_t -> C_t
H_t -> agent_modulation_t

No direct C_t -> agent causal edge.

Purpose:
test whether inhabitants correctly infer “clock/proxy” rather than celestial cause.

### S6 — Cultural-only astrology world

No physical/controller coupling.

Agents:
- search for patterns;
- publish rules;
- preferentially transmit memorable hits;
- reinterpret misses;
- inherit named symbolic categories.

Purpose:
measure how convincing astrology-like systems can become with zero true signal.

### S7 — Weak-signal plus cultural distortion

A small real coupling exists, but cultural transmission modifies the discovered
rule set.

Purpose:
test the project's most interesting possibility:

REAL_CORRELATION + WRONG_MECHANISM + CULTURAL_DRIFT.

## Frozen candidate encodings

At minimum compare four f(C) families.

### F1 continuous physical

f(C) derived from mass/distance/illumination proxies.

### F2 angular categorical

Examples:
- conjunction windows;
- opposition windows;
- trine/square-like angles.

### F3 birth hash

Seed = Hash(discretized_C_birth)

The hash is deliberately nontraditional.

Purpose:
see whether observers can discover a real birth-state signal whose code has no
symbolic resemblance to historical astrology.

### F4 structured symbolic controller code

A deliberately fixed arbitrary mapping uses:
- planet identity;
- angular relationship;
- sign-like sector;
- local horizon sector.

Purpose:
create a true “astrology-like” controller and see what observers recover.

## Observer separation

Ground-truth simulator and analyst must be separate roles.

Generator knows:
- world type;
- coupling;
- random seeds.

Analyst receives only:
- observational data;
- allowed astronomical variables;
- cultural records if the experiment includes them.

Analyst must not receive hidden controller state.

## Data products

For every run persist:

world_manifest.yaml
agent_births.parquet
celestial_state.parquet
physical_channels.parquet
agent_outcomes.parquet
cultural_claims.jsonl
ground_truth_private.yaml
analysis_submission.yaml

The ground-truth file must remain hidden until scoring.

## Discovery and holdout

Split by time and agents.

Discovery set:
used to infer rules.

Holdout-A:
new time periods, same population.

Holdout-B:
new agents, same astronomical process.

Holdout-C:
new agents and new time periods.

A model that succeeds only on discovery is not considered recovered.

## Scoring

### Prediction

- log loss / likelihood;
- AUROC where appropriate;
- RMSE for continuous outcomes;
- calibration;
- effect-size recovery.

### Causal structure

Score whether analyst identifies:
- direct physical cause;
- natal initialization;
- runtime effect;
- plasticity effect;
- common cause;
- null.

### Rule recovery

Compare inferred f_hat(C) to true f(C).

### Cultural distortion

Measure:
- false rule count;
- retained true-rule information;
- exaggeration;
- mutation rate;
- confidence versus accuracy.

## Success criteria

The experiment is informative if at least one of the following happens:

1. null worlds routinely generate convincing but nonpredictive astrology;
2. true coupling is recoverable out of sample;
3. observers systematically confuse physical cause with symbolic categories;
4. hidden-common-cause worlds produce stable correlation but incorrect causal inference;
5. cultural transmission preserves weak signal while corrupting mechanism.

## Failure criteria

The experiment fails scientifically if:

- rules are chosen after observing holdout results;
- controller mappings are changed to rescue failed predictions;
- analyst sees hidden ground truth;
- null and alternative worlds cannot be distinguished even in principle;
- the only conclusion is “anything could be possible.”

## Historical bridge experiment

After technical validation, encode simplified historically inspired systems:

- Babylonian birth-state records;
- Dorothean triplicity/lots;
- Valens timing;
- Ptolemaic ambient causal model;
- selected jyotiṣa structures.

Question:

Which system, if any, extracts signal under each synthetic world?

This compares information architecture, not theological truth.

## Nonclaim

A successful simulation would show that a proposed mechanism is coherent and
discoverable under specified conditions.

It would not show that our universe uses that mechanism.
