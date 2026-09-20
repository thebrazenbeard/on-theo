# Hellenistic / Greco-Roman Astrology — Technical Provenance V1

Status: RESEARCHED FOUNDATION / SOURCE DIFFERENTIATION

## Purpose

“Hellenistic astrology” is not one doctrine.

This file separates major surviving witnesses and asks which techniques are actually present in which source.

## Dorotheus of Sidon

Dorotheus' Carmen Astrologicum derives from a Greek verse work of the first century CE preserved through later Persian/Arabic transmission.

Core modern edition:
David Pingree, ed./trans., Carmen Astrologicum (1976).

Accessible orientation:
https://www.skyscript.co.uk/dorotheus1.pdf
https://books.google.com/books?id=XiZhP1MiUbEC

Book structure in the surviving tradition includes:
- nativities;
- marriage and children;
- lifespan;
- transfer/timing of years;
- interrogations/elections.

Dorotheus strongly emphasizes triplicity rulers.

The surviving text explicitly divides the zodiac into four triplicities and provides different sequences of rulers by day and night.

Source witness:
https://unifiedastrology.wordpress.com/sources/hellenistic-sources/carmen-astrologicum-of-dorotheus-book-one/

This creates an important control:

SECT_DAY_NIGHT_LOGIC is not decorative. It changes technical rulership.

Other technical elements associated with the Dorothean corpus include:
- terms/bounds;
- dodecatemoria;
- lots;
- natal topic judgments;
- timing/prognostic techniques.

Because the extant text passed through translation and redaction, each unusually specific doctrine should eventually be tagged:
GREEK_CORE | PERSIAN_LAYER_POSSIBLE | ARABIC_LAYER_POSSIBLE | UNCERTAIN.

## Vettius Valens

Vettius Valens, active in the second century CE, compiled the Anthologies approximately 152–188 CE.

Digital Mark Riley translation:
https://www.skyscript.co.uk/valens_janegca.html

Source significance:
Valens is the largest surviving practical manual of Hellenistic horoscopic technique and includes worked chart material.

The source should be used to investigate:
- lots, especially Fortune;
- triplicity and planetary rulership;
- operative/inoperative places;
- chronocrator/timing techniques;
- annual and period methods;
- solar/lunar conditions;
- aspects;
- actual practitioner handling of conflicting indicators.

Guard:

VALENS != PTOLEMY.

Valens preserves a working technical tradition whose procedures cannot be safely reconstructed by reading Ptolemy alone.

## Claudius Ptolemy

Ptolemy's Tetrabiblos is a second-century CE systematization.

Public-domain Robbins translation:
https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Ptolemy/Tetrabiblos/

### Ptolemy's epistemic posture

Ptolemy distinguishes:
- mathematical astronomy: celestial movements themselves;
- prognostication: terrestrial consequences inferred from celestial configurations.

He explicitly treats the second as less certain because terrestrial matter is variable.

Book I §§1–3:
https://penelope.uchicago.edu/thayer/e/roman/texts/ptolemy/tetrabiblos/1a*.html

### Ptolemy is not simple fatalism

Ptolemy argues that:
- celestial motion is regular;
- terrestrial outcomes involve multiple interacting causes;
- some effects can be resisted or overridden by stronger causes.

That means a proposition such as:

PTOLEMAIC_ASTROLOGY = ABSOLUTE_PREDETERMINATION

is false as a description of his stated model.

### Natural-quality model

Ptolemy attempts to naturalize planetary influence with qualities such as:
- heating;
- cooling;
- drying;
- moistening.

Book I §§4 onward:
https://penelope.uchicago.edu/thayer/e/roman/texts/ptolemy/tetrabiblos/1b*.html

His account of Sun/Moon/planetary nature belongs to an Aristotelian-style physical framework, not modern gravitational physics.

Guard:

ANCIENT_NATURAL_CAUSATION != NEWTONIAN_FORCE_MODEL.

### Technical rulership

Ptolemy discusses:
- planetary houses/domiciles;
- triangles/triplicities;
- exaltations;
- terms/bounds;
- aspects;
- applications/separations.

He also preserves competing systems.

For example, in his treatment of terms he explicitly distinguishes Egyptian and Chaldaean arrangements and criticizes inconsistencies in the received Egyptian ordering.

This is direct evidence of technical plurality inside antiquity itself.

## Neugebauer and Van Hoesen — Greek horoscope corpus

O. Neugebauer and H. B. Van Hoesen, Greek Horoscopes (1959).

Digital corpus:
https://sites.dlib.nyu.edu/viewer/books/isaw_aphs000001/1

Use:
- dated horoscope evidence;
- actual combinations of chart data in documentary sources;
- comparison between handbook doctrine and real surviving charts.

Research rule:

MANUAL_PRESCRIPTION != DOCUMENTARY_PRACTICE.

## Technique provenance matrix — initial

### Twelve zodiacal signs
Status: established before major surviving Hellenistic manuals.
Earlier roots: Babylonian zodiac.

### Houses / places
Status: mature in Greco-Roman horoscopic practice.
Open research:
- earliest secure documentary witness;
- geometrical versus sign-based place division;
- transmission eastward and westward.

### Aspects
Status: explicit technical role in Hellenistic systems.
Research:
- sign-based configurations;
- later degree-based refinements;
- application/separation.

### Triplicity
Status: prominent.
Dorotheus: three-ruler day/night schemes.
Ptolemy: different rationalization/systematization.

### Exaltations
Status: inherited doctrine present in Ptolemy and other sources.
Ptolemy attempts a physical/seasonal rationalization rather than simply repeating a table.

### Terms/bounds
Status: multiple competing systems already acknowledged by Ptolemy.

### Lots
Status: major practical feature, especially in Dorothean/Valens material.
Open research:
- formula variation by sect;
- earliest surviving named lots;
- transmission into Arabic/Persian and Indian systems.

### Sect
Status: day/night distinction is structurally important in multiple Hellenistic techniques.
Open research:
- exact terminology by source;
- which doctrines change under sect.

### Timing
Status: substantial in Valens and Dorotheus.
Open research:
- annual profections;
- planetary periods;
- releasing/time-lord systems;
- transfer of years;
- later Arabic transformations.

## Comparative warning

Do not build a fake “classical astrology” by selecting:
- Ptolemy's causal theory,
- Dorotheus' triplicity rulers,
- Valens' timing techniques,
- later medieval houses,
and pretending a single ancient author taught the combined package.

The branch should instead maintain SOURCE -> TECHNIQUE edges.

## Next ingestion

1. Parse Greek Horoscopes into a dated chart registry.
2. Extract Dorotheus by book/chapter/technique.
3. Extract Valens by book/chapter/technique and worked chart.
4. Extract Tetrabiblos proposition-by-proposition.
5. Build disagreements matrix.
6. Compare each technique to Babylonian predecessors and later Arabic/Indian adoption.
