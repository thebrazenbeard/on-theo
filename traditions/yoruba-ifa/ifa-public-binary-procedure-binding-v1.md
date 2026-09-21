# Yorùbá / Ifá — Public Binary Procedure Binding V1

Status: PUBLIC-SOURCE PARTIAL PROCEDURE BINDING / NON-CANONICAL

## Purpose

Bind enough of a public Ifá specific-alternative procedure to determine whether
the current conditional binary null model is historically grounded.

This artifact deliberately stops where the public source stops.

## Public source 1 — William Bascom

William Bascom, *Ifa Divination: Communication between Gods and Men in West
Africa* (1969), chapter V, pp. 51–59, documents:

- specific questions framed as mutually exclusive alternatives;
- affirmative and negative propositions;
- yes/no questions;
- the broader etic probability model in which each of the 256 figures has
  probability 1/256 under the standard figure-generation abstraction.

Bascom therefore securely binds:

`FINITE_BINARY_OR_MUTUALLY_EXCLUSIVE_OUTPUT`.

## Public source 2 — Wande Abimbola

Wande Abimbola, *Ifá Divination Poetry* (NOK Publishers, 1977), in the
introductory description of the consultation procedure, publicly describes:

- one affirmative/negative determinant object in one client hand and the other
  determinant object in the other hand;
- the client may conceal either object in either hand;
- the diviner poses the specific question;
- the diviner generates/manipulates the divination instruments twice;
- if the second Odù is senior to the first, one hand is requested;
- if the second Odù is junior to the first, the other hand is requested;
- the revealed determinant object supplies the affirmative/negative answer.

The same passage gives the example that a bone can signify the negative answer.

This is sufficient to bind:

`TWO_SUCCESSIVE_ODU + SENIORITY_COMPARISON -> HAND_SELECTION -> BINARY_DETERMINANT`.

## Seniority ordering

Abimbola further describes:

- sixteen principal Odù;
- 240 junior Odù;
- a strict ordering of seniority among the junior Odù.

This makes relative rank a source-defined structural variable.

## What is now source-bound

### A/B proposition structure
BOUND.

### Affirmative/negative determinant objects
BOUND at public descriptive level.

### Client may randomize left/right concealment
BOUND.

### Two successive figure generations
BOUND.

### Relative seniority determines hand selection
BOUND.

### Strict rank ordering exists
BOUND.

### Base 256-figure probability model
BOUND through Bascom's etic description.

## What remains unresolved

### Exact tie rule
`HOLD`.

The current public-source pass has not found an authoritative clause stating what
to do when the two successive Odù are identical in rank.

Do not invent:
- automatic recast;
- automatic invalidation;
- first-hand default;
- second-hand default.

### Physical implementation equivalence
`PARTIAL`.

Different public descriptions may use:
- divining chain;
- palm nuts;
- other lineage-specific implementations.

The future calibration must freeze one public implementation.

### Cross-lineage universality
`NOT_ESTABLISHED`.

This procedure description must not be projected onto all Ifá lineages.

## Mathematical implication

Under a modern abstract model where:

- the two source-defined successive figures are independent;
- all 256 figures are equiprobable;
- rank order is total;
- tied ranks are excluded from the binary output;

symmetry yields:

`P(second senior | non-tie) = 1/2`.

`P(second junior | non-tie) = 1/2`.

This is a mathematical consequence of the model.

It is not a source statement about ties.

## Tie strategy for calibration design

Until an authoritative public tie rule is bound, two paths are allowed.

### Path A — practitioner-approved public rule

A voluntary competent practitioner supplies a publicly shareable tie rule before
data collection.

That rule is documented and frozen.

### Path B — modern structural abstraction

Treat identical-rank pairs as:

`INVALID_TIE`.

Record them and exclude them only from the conditional A/B proportion.

This produces a modern binary abstraction.

It must be labeled:

`MODERN_STRUCTURAL_ABSTRACTION`,
not
`LITERAL_TRADITIONAL_IFA`.

## Calibration readiness

The procedure is now:

`PARTIALLY_READY`.

The remaining blocker for a historically closer protocol is narrow:

`TIE_RULE + ONE_FROZEN_PUBLIC_IMPLEMENTATION`.

The statistical/logging framework in PR #148 is otherwise usable.

## Evidence classes

Bascom:
`SCHOLARLY_ETHNOGRAPHIC_DESCRIPTION / DOCUMENTARY_PRACTICE`.

Abimbola:
`SCHOLARLY_INDIGENOUS_AUTHORSHIP / DOCUMENTARY_DESCRIPTION / LITERARY_CORPUS_CONTEXT`.

Mathematical null:
`PROJECT_INFERENCE / MATHEMATICAL_DERIVATION`.

## Guards

- PUBLIC_DESCRIPTION_NE_ALL_IFA
- TIE_RULE_UNRESOLVED
- ABIMBOLA_DESCRIPTION_NE_LINEAGE_UNIVERSAL
- MODERN_INVALID_TIE_RULE_NE_TRADITIONAL_RULE
- SENIORITY_COMPARISON_NE_ANOMALOUS_INFORMATION
- BINARY_OUTPUT_NE_ACCURACY
- SOURCE_BINDING_NE_EMPIRICAL_EFFECT
