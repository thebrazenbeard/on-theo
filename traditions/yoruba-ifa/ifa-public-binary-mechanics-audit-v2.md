# Yorùbá / Ifá Public Binary Mechanics Audit V2

Status: NON-CANONICAL / PUBLIC-SOURCE PROCEDURE AUDIT
Research frontier: PUBLIC_BINARY_PROCEDURE_CALIBRATION_DESIGN

## Scope

This audit tightens the public ìbò / specific-alternative procedure binding used
for calibration design. It does not claim to reconstruct all Ifá lineages, does
not request restricted knowledge, and does not authorize an efficacy test.

## Evidence classes

William Bascom, Ifa Divination: Communication between Gods and Men in West
Africa, chapter V, pp. 51-59:
SCHOLARLY ETHNOGRAPHIC DESCRIPTION / DOCUMENTARY PRACTICE.

Wándé Abímbọ́lá, Ifá Divination Poetry (1977), introductory procedure:
SCHOLARLY INDIGENOUS AUTHORSHIP / DOCUMENTARY DESCRIPTION.

Oludamini Ogunnaike, Sufism and Ifa: Ways of Knowing in Two West African
Intellectual Traditions (Harvard dissertation, 2015), especially the public
procedure discussion around p. 261 and later discussion of seniority variation:
SCHOLARLY INTERPRETATION / PRACTITIONER-INFORMED DESCRIPTION.

## Source-secure public mechanics

Across the admitted public descriptions, the following bounded structure is
supported:

1. A specific question can be framed as affirmative/negative or as mutually
   exclusive alternatives.
2. Public ìbò examples use determinant objects. Abímbọ́lá describes tied
   cowries as affirmative and a bone as negative.
3. The client can conceal either determinant in either hand.
4. The divination instrument is manipulated twice, producing two successive
   Odù.
5. Relative seniority of the two Odù determines which hand is selected.
6. In Abímbọ́lá's description, second Odù senior to first selects the right
   hand; second junior to first selects the left hand.
7. The determinant found in the selected hand supplies the answer.

This supports a finite mechanically scoreable stage.

It does not establish that the stage is universal across lineages or that its
religious causal interpretation is empirically correct.

## Candidate-search loop is not a single binary trial

Abímbọ́lá also describes sequential questioning in which a negative answer to
one proposed candidate can be followed by substitution of another candidate
and another question until an affirmative answer is obtained.

That is a different statistical object from one independent A/B trial.

Therefore the calibration protocol must not silently import:

CANDIDATE_SEARCH_UNTIL_YES

into:

ONE_FROZEN_BINARY_QUERY -> ONE_BINARY_OUTPUT.

If a later study examines search-until-affirmative behavior, its stopping rule
and family-wise outcome space require a separate model.

## Seniority is structured but not safely universalized

The public sources support ordered seniority among Odù.

Ogunnaike also reports variation among practitioners in ordering conventions,
and describes special priority treatment for Eji Ogbe and Ofun Meji in the
ìbò context.

Consequences:

- one ranking table must be frozen before data collection;
- a ranking table from one source must not be projected onto all lineages;
- special priority rules must be explicit if the historically closer mode uses
  them;
- ranking variation alone does not imply output bias if the same deterministic
  comparison rule is applied symmetrically to both cast positions.

## Equal-rank / tie rule

Current public-source search has not produced a sufficiently secure rule for
what happens when the two successive Odù have equal rank.

Current status:

TIE_RULE = UNKNOWN.

Do not infer automatic recast, automatic first-hand selection, automatic
second-hand selection, or any ritual interpretation.

## Two admissible research modes

### HISTORICALLY_CLOSER_PUBLIC_MODE

Requires, before data:

- one voluntary competent practitioner or one sufficiently explicit public
  lineage description;
- a publicly shareable frozen ranking rule;
- a publicly shareable tie/equal-rank rule;
- a frozen implement and handling procedure;
- explicit consent and no restricted teaching.

Until the tie rule is bound, this mode remains HOLD.

### MODERN_STRUCTURAL_ABSTRACTION_MODE

Allowed scientific abstraction:

- preserve the public two-successive-Odù / seniority / hand-selection skeleton;
- identical-rank pair = INVALID_TIE;
- no recast;
- preserve every tie in the raw log;
- use neutral A/B labels for calibration;
- make no claim that the abstraction is literal traditional Ifá.

This mode is suitable for null calibration because it removes the unresolved
tie decision instead of inventing one.

## Living-community boundary

A living tradition is not laboratory equipment.

No trial count, protocol requirement, or demand for disclosure overrides:
- practitioner consent;
- community boundaries;
- refusal to disclose restricted material;
- refusal to perform repetitive ritual for research.

A high-volume calibration may therefore use the MODERN_STRUCTURAL_ABSTRACTION
rather than pressure a practitioner to perform thousands of sacred acts.

## Claim ceiling

Strongly supported here:
PUBLIC_SOURCE_BINARY_PROCEDURE_SKELETON.

Not established:
ONE_UNIVERSAL_IFA_BINARY_PROCEDURE;
EXACT_TRADITIONAL_TIE_RULE;
EMPIRICAL_DIVINATORY_ACCURACY;
ANOMALOUS_INFORMATION;
EXTERNAL_AGENCY.

## Guards

- PUBLIC_DESCRIPTION_NE_ALL_IFA
- DOCUMENTED_PROCEDURE_NE_EMPIRICAL_EFFECT
- CANDIDATE_LOOP_NE_SINGLE_BINARY_TRIAL
- RANKING_VARIATION_NE_AUTOMATIC_BIAS
- UNKNOWN_TIE_RULE_REMAINS_UNKNOWN
- MODERN_INVALID_TIE_NE_TRADITIONAL_RULE
- RESTRICTED_KNOWLEDGE_NOT_REQUIRED
