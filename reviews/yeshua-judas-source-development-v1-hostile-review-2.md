# Hostile Review 2 — Judas Source Development + Logistics/Lexical Layers

Review subject: `c8111654a7d539f8499e91d372b221cfc9a9820b`

Execution provenance: `SAME_RUNTIME_ADVERSARIAL_REVIEW`

Status: `REVISION_REQUIRED_BEFORE_INTERNAL_PASS`

This is not an independent review.

## Review question

Did the first hostile-review narrowing propagate consistently into the newly added arrest-logistics, lexical, and research-state layers?

## Findings

### 1. Dedicated dossier narrowing

PASS.

The primary dossier now correctly separates:
- historical Judas existence: PLAUSIBLE_TO_PROBABLE;
- historical Judas handover: PLAUSIBLE_NOT_YET_SECURE;
- motive: unresolved;
- money in Mark: textually present but not equal to greed;
- location/timing/access: plausible operational model, not established event;
- later reception: materially diversified without proving original innocence.

### 2. Artifact authority

PASS.

`research/yeshua/judas/JUDAS_ARTIFACT_AUTHORITY_V1.yaml` correctly designates the dedicated Judas lane as promotion authority and the `research/yeshua/people/` files as supporting controls.

This cures the duplicate-dossier drift risk at the architectural level.

### 3. Arrest-logistics packet

REVISION REQUIRED.

The packet does good work separating:
- public recognizability;
- timing;
- location;
- access;
- identification;
- legal testimony;
- Roman involvement.

But it overstates one result:

`LOCATION_TIMING_AWAY_FROM_CROWD = PLAUSIBLE / CURRENTLY STRONGEST LOGISTICAL MODEL`.

"Strongest" is too strong at the historical level because the ranking is generated largely by fitting Gospel narrative features together, including later John.

The admissible formulation is:

`LOCATION_TIMING_ACCESS = PLAUSIBLE_BOUNDED_OPERATIONAL_MODEL`.

It may be the most economical model among those currently tested, but that is PROJECT_INFERENCE, not a historically demonstrated ranking.

The external Roman/Judean policing background still needs source-specific evidence before promotion.

### 4. `paradidomi` packet

PASS WITH ONE REVISION.

The lexical conclusion is sound:

- neutral core = hand over / deliver;
- Mark's context is morally negative;
- "betray" is contextually reasonable;
- lexeme alone does not recover motive;
- lexical neutrality does not exonerate Judas.

However, the packet still says the Markan historical event is "source-bound/probable at current ceiling."

That conflicts with the first hostile review.

It must read:

`MARKAN_HANDOVER_NARRATIVE = SOURCE_BOUND`;
`HISTORICAL_JUDAS_HANDOVER = PLAUSIBLE_NOT_YET_SECURE`.

### 5. Research-state conflict

FAIL UNTIL RECONCILED.

`research-state-v2.yaml` and `research-state-v3.yaml` preserve pre-review values:
- historical Judas = PROBABLE;
- some handover = PLAUSIBLE_TO_PROBABLE;
- strongest logistical function = LOCATION_TIMING_ACCESS_CONFIRMATION.

Those values conflict with the revised authoritative dossier/state.

A repository with contradictory current research-state files cannot claim a valid exact-head review.

Required repair:
- create a new V4 state that supersedes V1/V2/V3 for current use;
- V4 must carry the narrowed confidence levels;
- update the artifact-authority manifest so V4 is the current state authority;
- preserve older states as provenance, not current truth.

### 6. Historical Judas existence

PASS WITH GUARD.

`PLAUSIBLE_TO_PROBABLE` is acceptable if its basis is stated correctly:

- Mark is the single earliest explicit named source;
- Judas is embedded specifically in a Twelve roster and passion sequence;
- later diverse traditions retain the named figure;
- no competing early named handover agent survives.

This is a synthetic historical judgment, not multiple independent early attestation.

### 7. Historical Judas handover

PASS AT NARROWED LEVEL.

Current ceiling:

`PLAUSIBLE_NOT_YET_SECURE`.

The next material discriminator belongs in R4:
- pre-Markan passion tradition;
- arrest logistics;
- literary function;
- source dependence;
- rival intentional-handover traditions.

### 8. Money

PASS.

Mark already contains money.

Therefore no valid reconstruction may claim:
"money was added only later."

What remains uncertain:
- actual historical payment;
- amount;
- greed as motive;
- whether payment was primary or secondary to another motive.

### 9. Gospel of Judas

PASS.

It remains evidence for later Christian theological reconfiguration, not a historical authorization document.

Its reversal is compatible with an already powerful negative Judas tradition.

### 10. Scapegoat / concentration hypothesis

PASS AS UNPROMOTED.

The project still lacks the positive evidence needed to promote broader intentional collaboration concentrated into Judas.

Mark's preservation of:
- collective flight;
- Peter denial

actually weakens the simplistic claim that Mark had to dump all disciple failure onto Judas.

## REQUIRED RESEARCH RESPONSE

Before internal pass:

1. narrow arrest-logistics ranking;
2. narrow the historical-handover statement in the lexical packet;
3. create reconciled `research-state-v4.yaml`;
4. update Judas artifact authority to point to V4;
5. fresh-read and exact-head hostile-review the reconciled state.

> **HOSTILE REVIEWER**
>
> The important semantic lesson is that an "operationally sensible" Judas can be just as seductive as an "innocent Judas." Historical economy is not attestation.
>
> A location/timing/access role may indeed explain why an insider was useful, but until independent policing/context evidence and the Gospel source relationships are integrated, it remains a model—not the recovered job description of Judas.

## DISPOSITION

`REVISION_REQUIRED_BEFORE_INTERNAL_PASS`

No exoneration, invention, conspiracy, or preferred logistical function is promoted.
