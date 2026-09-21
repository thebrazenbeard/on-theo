# Yorùbá / Ifá — Public Binary Null Model V1

Status: NON-CANONICAL / PROJECT-INFERENCE / CONDITIONAL MATHEMATICAL MODEL

## Purpose

Formalize the ordinary chance baseline for a public binary Ifá abstraction
without pretending that every lineage or every `ibo/adimu` implementation is
identical.

This document does NOT redefine traditional Ifá.

It asks only:

If a public binary determinant procedure can legitimately be represented as a
comparison of two independently generated uniformly distributed Ifá figures,
what null probabilities follow?

## Source inputs

William Bascom reports that the 256 Ifá figures can be analyzed etically as
equiprobable under the standard figure-generation model:

`P(each figure) = 1/256`.

Bascom also documents specific-alternative questioning in which propositions
may be framed as mutually exclusive alternatives or yes/no questions.

Public descriptions of `ibo` assign affirmative and negative values to
determinant objects and can use relative figure rank/seniority in selecting
between them.

The exact mechanics vary by description and may vary by lineage.

Therefore the mathematical model below is conditional.

## Conditional idealized model

Assumptions:

1. two generated figures are independent;
2. each is uniformly distributed over 256 ranked figures;
3. lower or higher numerical rank consistently represents "senior" under a
   frozen convention;
4. the first-versus-second seniority determines the two binary sides;
5. tied ranks are either declared invalid or repeated.

Under these assumptions:

`P(tie) = 1/256 = 0.00390625`.

By symmetry:

`P(first is senior) = 255/512 = 0.498046875`.

`P(second is senior) = 255/512 = 0.498046875`.

Conditional on a non-tie:

`P(first side | no tie) = 1/2`.

`P(second side | no tie) = 1/2`.

These values were independently checked with Wolfram Language.

## What this establishes

Only this:

If the documented experimental procedure actually satisfies the assumptions
above, then a 50/50 binary null is mathematically justified after conditioning
on non-ties.

It does NOT establish that:
- every public Ifá binary procedure satisfies those assumptions;
- every lineage treats ties the same way;
- all figures are equiprobable under every physical implementation;
- operator handling cannot bias the distribution.

## Empirical pretest requirement

Before any anomalous-information trial:

1. freeze the exact public procedure;
2. record several hundred or more null-only outputs with no hidden target;
3. estimate A/B frequency;
4. estimate tie/invalid rate;
5. test serial dependence;
6. test operator dependence;
7. compare observed distribution with the theoretical conditional model;
8. freeze the null model before target trials begin.

If the empirical procedure produces biased A/B frequencies, use the empirical
null or a validated mechanistic null rather than 0.5.

## Why this matters

A divination system can appear "accurate" against the wrong baseline.

For example, if a procedure outputs A 60% of the time and the target also has a
60% A base rate, naive 50/50 scoring manufactures apparent performance.

Therefore:

`WRONG_NULL = FALSE_ANOMALY_RISK`.

## Trial scoring under a validated 0.5 null

Only after validating the conditional fair-binary model may N independent
target trials be modeled as:

`K ~ BinomialDistribution[N, 1/2]`.

The primary analysis should still predeclare:
- N;
- one-sided or two-sided test;
- minimum effect of interest;
- stopping rule;
- exclusion rule;
- replication requirement.

## Hidden-target separation

A binary null model is useful only when:
- target generation is independent;
- target base rates are fixed;
- target is hidden from practitioner and model;
- answer is committed before reveal;
- every trial is retained.

The null-model document does not itself authorize or define a traditional Ifá
ritual.

## Evidence class

This file is:

`PROJECT_INFERENCE + MATHEMATICAL_DERIVATION`.

It is not:
- PRIMARY TEXT;
- initiatory teaching;
- ethnographic authority over lineage practice;
- empirical evidence that Ifá exceeds chance.

## Claim ceiling

Admitted:

`IDEALIZED_TWO_UNIFORM_RANK_COMPARISON_HAS_CONDITIONAL_50_50_OUTPUT`.

Not admitted:

`ALL_IFA_BINARY_PRACTICE_HAS_50_50_NULL`.

`IFA_ACCURACY_EXCEEDS_CHANCE`.

## Guards

- CONDITIONAL_MODEL_NE_TRADITIONAL_TOTALITY
- BASCOM_256_UNIFORM_MODEL_NE_EVERY_IMPLEMENTATION
- TIE_RULE_MUST_BE_FROZEN
- EMPIRICAL_NULL_PRETEST_REQUIRED
- 50_50_NE_ASSUMED_BY_DEFAULT
- BINARY_NULL_NE_DIVINATORY_ACCURACY
