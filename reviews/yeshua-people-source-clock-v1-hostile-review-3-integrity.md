# Hostile Review 3 — R3 People Source Clock Integrity Revalidation

Review subject: `8ce9a4d10a0b315446d7e5c5a813083745308751`

Execution provenance: `SAME_RUNTIME_ADVERSARIAL_REVIEW`

Status: `INTERNAL_HOSTILE_PASS_WITH_GUARDS`

This is not an independent review.

## Why a third review exists

The previous exact-head review covered commit `b9f30ca6b9a70c3593ef558cf45e736d39bef789`.

Subsequent post-review edits changed the durable artifacts and introduced:
- duplicate prose;
- duplicate YAML keys for `identity_control`;
- duplicate YAML keys for `priority_rationale`.

That made the prior review receipt stale for the current branch head.

The current subject is the cleaned artifact set.

## PROPOSAL

Treat the integrity-cleaned source clock as semantically equivalent to, or narrower than, the previously reviewed R3 control and allow it to govern the Judas dossier.

> **HOSTILE REVIEWER**
>
> A cleanup commit is not automatically semantically inert. Removing duplicate YAML keys can change which value a parser would have used, and rewriting prose can quietly alter a claim. Therefore the cleaned head must be checked as a research artifact, not merely as formatting.
>
> The key questions are:
> 1. Did the cleanup promote any person-level historical claim?
> 2. Did it weaken the Judas bias guard?
> 3. Did it convert later portrayals into historical development claims?
> 4. Did it restore rankability claims about Mary/Thomas/Peter?
> 5. Did the Cephas/Peter control become stronger than the evidence allows?

## RESEARCH RESPONSE

The cleaned head does not promote any person-level historical claim.

Specific effects:
- duplicate `EARLIER_SOURCE != TRUTH_SCORE` prose was reduced to one instance;
- duplicated Pauline-silence wording was consolidated without changing the conclusion that silence is weak negative evidence;
- duplicate YAML `identity_control` entries were reduced to the structured control preserving mainstream Cephas=Peter identification plus minority dissent;
- duplicate `priority_rationale` entries were replaced by one prose rationale plus a separate `priority_mode` field;
- the Thomas cross-person claim was narrowed from "development" to "later portrayals";
- the Mary cross-person claim was narrowed from generic "important witness" to prominence in surviving Markan passion/burial/tomb memory.

No change promotes:
- Judas innocence;
- Judas invention;
- Mary/Thomas historical superiority;
- Peter hidden betrayal;
- James dynastic succession;
- collective Roman collaboration.

> **HOSTILE REJOINDER**
>
> The cleaned version is stronger methodologically than the stale reviewed version because it removes parser ambiguity and narrows two source-history formulations.
>
> One guard remains essential: the cleaned branch head is reviewed only as a **source-clock control**. It does not pre-review the conclusions of the Judas dossier merely because Judas is its next consumer.
>
> The Judas dossier must independently hostile-test:
> - existence of a historical insider-handover core;
> - the function of Judas;
> - motive;
> - payment;
> - identification/location information;
> - death traditions;
> - diachronic demonization;
> - invention/scapegoat hypotheses.

## DISPOSITION

`INTERNAL_HOSTILE_PASS_WITH_GUARDS`

The cleaned R3 source clock is valid for downstream person-level research.

The earlier review receipt is superseded for current-head use, not erased as historical provenance.

Independent exact-head review is still required before any high-bias person-level promotion.
