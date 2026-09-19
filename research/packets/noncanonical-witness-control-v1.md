# Noncanonical witness-control packet V1

Status: SOURCE / MANUSCRIPT CONTROL / REVIEW REQUIRED / NON-CANONICAL

Exact parent:
- `research/mary-magdalene-authority-reception-v1-20260919`
- `e3a1f08b1e4ffb081f583501140efaf81c650d29`

Machine-readable map:
`research/packets/noncanonical-witness-control-v1.yaml`

## Purpose

The Christianity lane already warns that noncanonical does not mean secretly true and canonical does not mean historically neutral.

This packet adds the missing manuscript rule:

`WORK_IDENTITY`
!=
`COMPOSITION_DATE`
!=
`PHYSICAL_WITNESS_IDENTITY`
!=
`PHYSICAL_WITNESS_DATE`
!=
`MODERN_EDITION`.

A manuscript can be centuries later than the work it preserves. A late manuscript therefore does not date the work late by itself. Conversely, a scholarly early composition date does not make a late manuscript an early physical witness.

## Gospel of Mary

Witness control for the Gospel of Mary is inherited from the exact parent research packet.

That parent distinguishes:
- P.Oxy. L 3525;
- P.Ryl. III 463;
- Berlin Codex 8502;
- work composition from witness dates;
- the common but contested identification of the work's Mary as Mary Magdalene.

This packet does not duplicate those records.

## Gospel of Thomas

Current manuscript control:

- P.Oxy. 1;
- P.Oxy. 654;
- P.Oxy. 655;

are the three extant Greek Thomas fragments and are dated broadly to the third century in the checked textual-criticism literature.

The complete Coptic Gospel of Thomas survives in Nag Hammadi Codex II, copied in the fourth century.

Therefore:

`THIRD_CENTURY_GREEK_WITNESSES`
and
`FOURTH_CENTURY_COPTIC_WITNESS`

do not by themselves settle the date of original composition.

The composition and source-history debates around Thomas remain separate from the physical-witness facts.

## Protoevangelium / Protevangelium of James

Papyrus Bodmer V is an early physical witness to the work commonly called the Protoevangelium of James.

Checked scholarship dates the Bodmer witness to the late third / early fourth century or, in some reference works, the fourth century.

V1 preserves that range without using it as a composition timestamp.

The later title "Protevangelium" is itself reception/editorial history; the work's manuscript titles vary.

## Infancy Gospel of Thomas

The manuscript tradition makes a simple "oldest Greek manuscript = oldest recoverable text" rule unsafe.

Checked recent scholarship reports:

- the Greek S-recension represented by Codex Sabaiticus 259 is an eleventh-century manuscript;
- a fifth-century Latin witness, the palimpsest portion of Codex Vindobonensis lat. 563, supports the short recension;
- two sixth-century Syriac manuscripts also support the short recension;
- the older versions can preserve a form closer to the recoverable archetype than the surviving Greek recensions.

Therefore:

`LANGUAGE_OF_SURVIVING_MANUSCRIPT`
does not establish
`LANGUAGE_OR_DATE_OF_ARCHETYPE`.

This packet records witness chronology without pretending the textual genealogy is solved.

## Gospel of Peter

The Akhmîm codex preserves the fragment conventionally identified as the Gospel of Peter.

Its physical manuscript is much later than the commonly proposed composition of the work: scholarship places the Akhmîm witness broadly between the seventh and ninth centuries, while many scholars place the Gospel of Peter in the second half of the second century.

But the identification and early-fragment problem itself has been challenged.

Paul Foster's textual work specifically cautions against assuming that proposed early papyrus fragments automatically belong to the Akhmîm Gospel of Peter and even urges caution about the relationship between the Akhmîm text and the second-century Gospel of Peter known from patristic references.

Therefore V1 records separately:

- `AKHMIM_PHYSICAL_WITNESS = LATE_ANTIQUE/EARLY_MEDIEVAL_MANUSCRIPT`;
- `GOSPEL_PETER_SECOND_CENTURY_COMPOSITION = SCHOLARLY_RECONSTRUCTION`;
- `EARLY_FRAGMENT_IDENTIFICATIONS = CONTESTED`;
- `AKHMIM_TEXT_IDENTIFICATION_WITH_PATRISTIC_GOSPEL_OF_PETER = STRONG_TRADITIONAL_IDENTIFICATION_BUT_NOT_METHOD_FREE`.

## Cross-work controls

### N1 — manuscript date is not composition date

Never infer:
`WITNESS_DATE == WORK_DATE`.

### N2 — earliest surviving witness is a terminus, not an autograph

An early witness can establish that a text-form existed by that point. It does not establish when every saying, episode, or redactional layer originated.

### N3 — translation witness is still evidence

A Coptic, Latin, Syriac, Ethiopic, Georgian, or Irish witness may preserve older textual states.

Translation does not make it irrelevant.

It does make reconstruction of the prior-language form a separate critical problem.

### N4 — one named work can have multiple recensions

"Infancy Gospel of Thomas" is not one mechanically uniform manuscript object.

Recension identity must remain explicit.

### N5 — title identity can be retrospective

Modern conventional titles can postdate the ancient work.

Do not turn a later catalog title into proof of original authorship.

### N6 — noncanonical status is not an evidence score

`NONCANONICAL`
does not imply
`EARLY`,
`LATE`,
`SUPPRESSED_TRUE`,
or
`HISTORICALLY_FALSE`.

Those are separate propositions.

## Current claim ceiling

This packet establishes manuscript/witness controls only.

It does not establish:
- that Thomas preserves sayings independent of the Synoptics;
- that the Protoevangelium preserves historical information about Mary's childhood;
- that Infancy Thomas preserves historical childhood deeds of Jesus;
- that the Akhmîm Gospel of Peter is independent of the canonical passion narratives;
- that any noncanonical text is more authentic because it was excluded from the later canon.

## Next research frontier

With witness identity separated from work identity, the next useful move is source-specific content analysis:

1. Thomas — saying-by-saying dependence/independence controls;
2. Protoevangelium — canonical-gap expansion and Marian development;
3. Infancy Thomas — recension-aware childhood miracle development;
4. Gospel Peter — passion/resurrection dependence and anti-/philo-Jewish redaction questions.

Content comparison should occur only after the witness layer remains explicit.
