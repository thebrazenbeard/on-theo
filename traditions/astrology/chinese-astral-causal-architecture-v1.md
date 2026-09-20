# Chinese Astral Causal Architecture V1

Status: PROJECT SYNTHESIS FROM PRIMARY-TEXT PROPOSITIONS

## Problem

Calling the *Tianguan shu* “Chinese astrology” is accurate only at a very broad
level.

Its information architecture is substantially different from a modern Western
natal chart.

The primary unit is often:

CELESTIAL ANOMALY
-> POLITICAL / REGIONAL MAPPING
-> OMEN
-> RULER RESPONSE
-> TERRESTRIAL OUTCOME

rather than:

BIRTH CONFIGURATION
-> PERSONALITY / LIFE TRAIT.

## State representation

The *Shiji* tracks:
- the sun and moon;
- the five visible planets;
- the twenty-eight mansions;
- asterisms/celestial offices;
- conjunctions and conflicts;
- color, brightness, shape, visibility and abnormal motion;
- atmospheric phenomena.

The sky is therefore treated as a structured state surface rather than merely a
list of zodiacal labels.

## Normal versus anomalous state

One of the most important primary-text controls is that celestial changes are
prognostically interpreted when they exceed normal limits.

Project abstraction:

OBSERVED_STATE
+ EXPECTED_STATE
-> DEVIATION
-> OMEN_CLASSIFICATION.

This resembles anomaly detection more than a universal lookup table in which
every normal position is equally meaningful.

That is a structural analogy only.

## Field allocation

The twenty-eight mansions are mapped onto terrestrial states/regions.

This creates a routing layer:

CELESTIAL_EVENT
-> SKY_REGION
-> TERRESTRIAL_POLITY.

That is why the same planetary phenomenon can be interpreted in relation to a
particular state.

This is not equivalent to Western houses.

## Political feedback loop

The text does not portray rulers as helpless recipients of celestial fate.

Celestial anomalies can prompt:
- cultivation of virtue;
- review of punishments;
- restoration of political harmony;
- administrative correction;
- remedial action;
- ritual action.

The resulting model is reflexive:

CELESTIAL_OMEN
-> HUMAN_INTERPRETATION
-> POLITICAL_ACTION
-> DIFFERENT_TERRESTRIAL_TRAJECTORY.

Therefore a simple deterministic representation loses a major part of the
system.

## Moral conditioning

Five-planet convergence provides an especially useful example.

A major conjunction can signify political elevation, but the outcome is
conditioned by whether the ruler is virtuous.

Project representation:

OUTCOME = F(CELESTIAL_CONFIGURATION, POLITICAL_MORAL_STATE).

This is not a scientific equation and is not claimed by the project as true.

It is a faithful structural abstraction of the textual logic.

## Comparison with Ptolemy

Ptolemy's *Tetrabiblos* tends to naturalize celestial influence through physical
qualities and multiple terrestrial causes.

The *Tianguan shu* is more naturally represented through:
- correspondence;
- omen;
- political mapping;
- normative response.

Therefore:

PTOLEMAIC_CAUSAL_NATURALISM
!=
HAN_CORRELATIVE_OMENOLOGY.

They should not be combined into a generic ancient “astrological mechanism.”

## Comparison with the controller hypothesis

The Chinese material offers an interesting analogy for the project's
hidden-controller idea because the heavens function as an information-bearing
state surface for terrestrial affairs.

But the texts do not establish:
- computation;
- simulation;
- software-like control;
- a hidden state variable;
- literal parameter updates.

The only defensible relation is:

ANCIENT_INFORMATION_SURFACE
~ PROJECT_ANALOGY
GLOBAL_STATE_INDICATOR.

It is not evidence that the universe is implemented that way.

## Experimental consequence

The on-theo simulations should eventually include an omen architecture distinct
from natal/runtime direct coupling.

Candidate synthetic world:

S8_INDICATOR_RESPONSE

Hidden environmental/political state H affects both:
- public celestial indicator C;
- terrestrial risk R.

Agents observe C and change policy.

So final outcomes depend on:
H
+ risk
+ whether agents correctly interpret/respond to C.

That world would distinguish:
- direct celestial causation;
- common-cause celestial indicator;
- common-cause indicator plus intelligent intervention.

This is closer to the *Tianguan shu* structure than simply mapping planets onto
agent personality weights.
