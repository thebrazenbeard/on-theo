# Qumran Belial passage and witness inventory V1

Status: SOURCE/WITNESS CONTROL / REVIEW REQUIRED / NON-CANONICAL

Exact parent:
- branch: `research/jubilees-mastema-passage-witness-inventory-v1-20260919`
- head: `80c4fc3f359e7838f6c112267c59ca38fbe46289`

Primary lexical control:
- Qumran-Digital lexicon, `בליעל`, version 1.3.0, 2026-05-21.

Machine-readable inventory:
`research/packets/qumran-belial-passage-witness-inventory-v1.yaml`

## Scope rule

A raw concordance search for `בליעל` is **not** an entity inventory.

The lexical field includes:
- ordinary/abstract "wickedness / worthlessness" uses;
- ambiguous damaged uses;
- personified Belial.

This packet admits a locus to the personified inventory only where the current Qumran-Digital lexical analysis classifies the term under personified Belial or where the immediate text unambiguously treats Belial as an acting hostile power.

Therefore:

`BELIAL_LEXEME_HIT != PERSONIFIED_BELIAL`.

## Personified Belial inventory

### A. Entrapment, temptation, and rule

- 4Q174 frg. 1-2 i,9 — captured by Belial in guilty error.
- CD 4:14-15 — "three nets of Belial."
- 4Q171 frg. 1-2 ii,9-10 — "snares of Belial."
- 1QS 1:18 — "during the rule of Belial."
- 1QS 1:23-24 — sins/transgressions during the rule of Belial.
- 1QM 14:9 — rule of Belial, damaged/uncertain context.
- 1QS 2:19 — all days of the rule of Belial.
- 4Q390 frg. 2 i,3-4 — rule of Belial, fragmentary context.
- CD 4:12-13 — Belial "sent/let loose" in Israel.
- 4Q174 frg. 4,3 — time in which Belial is released/opened; uncertain context.

### B. Belial as instrument of divine judgment

- 1QM 13:10-11 — God made Belial for destruction, "an angel of hostility" (`מלאך משטמה`).
- CD 8:2 / CD 19:14 — destruction by the hand of Belial.
- 4Q266 frg. 3 iii,25 — Qumran manuscript parallel to the CD destruction-by-Belial tradition.

The 1QM 13:10-11 phrase is a critical lexical bridge for later transmission analysis:
`BELIAL + מלאך משטמה`
does not by itself prove
`BELIAL = JUBILEES' PRINCE MASTEMA`.

It proves that Qumran Belial can be characterized using the same Hebrew hostility/enmity word-family.

### C. Cursing, rebuking, and eschatological defeat

- 1QS 2:4-5 — Levites curse the men of Belial's lot.
- 1QM 13:4 — Belial cursed for hostile/evil planning.
- 4Q286 frg. 7 ii,1-2 — curse against Belial and his guilty lot; overlaps/parallels the curse tradition.
- 4Q463 frg. 2,3 — rebuke/threat against Belial; damaged context.
- 11Q13 3,7 — Belial destroyed by fire; reading/context uncertain.
- 1QM 1:5 — eternal destruction of Belial's lot.
- 4Q496 frg. 3,5 — manuscript parallel for the 1QM 1:5 destruction formula.
- 1QM 4:1-2 — battle-standard formula invoking God's wrath against Belial.
- 1QM 11:8 — defeat of the bands/troops of Belial.
- 1QM 18:1 — God's great hand raised against Belial; fragmentary context.
- 1QM 18:3 — Israel's God against the host/crowd of Belial.

### D. Belial's people, lot, spirits, and army

- CD 5:17-19 — Belial raises Jannes and his brother against Moses/Aaron.
- 4Q175 1,23 — an accursed man "of Belial."
- 4Q177 frg. 10-11,4 — men of Belial.
- 4Q386 frg. 1 ii,3 — "son of Belial."
- 4Q174 frg. 1-2 i,8 — "sons of Belial."
- 11Q13 2,12-13 — Belial and the spirits of his lot; Melchizedek-opposition context.
- 11Q13 2,22 — movement/turning away from Belial.
- 11Q13 2,25 — liberation from the hand/power of Belial.
- CD 12:2 — spirits of Belial.
- 4Q271 frg. 5 i,18 — Qumran manuscript parallel to CD 12:2.
- 1QM 1:1 — army of Belial.
- 1QM 1:13 — army of Belial.
- 1QM 15:2-3 — whole army of Belial.

Some passages above recur in more than one functional category. The machine inventory stores each physical/textual locus once and gives it multiple role tags when necessary.

## Exact manuscript/witness controls

### Community Rule

Primary witness:
- `1QS` / 1Q28 — Community Rule.

Direct Qumran parallel witnesses visible in the Qumran-Digital transcription include:
- `4Q256` for 1QS 1:18, 1:23-24, and 2:4-5;
- `4Q257` for the 1QS 2:4-5 Belial-lot curse;
- `5Q11` preserves part of the same curse context but the Belial lexeme itself is not fully preserved in the surfaced parallel lines.

Witness rule:
a parallel is counted as **direct lexical Belial attestation** only where the letters of `בליעל` themselves survive/reconstruct in that physical witness.

### War Scroll

Primary witness:
- `1QM` / 1Q33 — War Scroll.

Important physical parallels:
- `4Q495 frg. 2,3` directly parallels 1QM 13:10-11 and preserves Belial with `מלאך משטמה`.
- `4Q496 frg. 3,5` parallels 1QM 1:5 and preserves Belial.

The War Scroll supplies one of the strongest personified-Belial clusters:
rule, lot, army, curse, divine creation/subordination, and final defeat.

### Damascus Document textual tradition

The medieval Cairo Damascus Document columns are textual witnesses to the CD wording, not Qumran physical manuscripts.

Where Qumran manuscript parallels survive, V1 binds them separately:
- CD 8:2 / 19:14 ↔ `4Q266 frg. 3 iii,25`;
- CD 12:2 ↔ `4Q271 frg. 5 i,18`.

This prevents:
`CAIRO_CD_TEXTUAL_LOCUS = QUMRAN_PHYSICAL_WITNESS`
from being silently assumed.

### Florilegium / pesharim / related Cave 4 texts

Direct Qumran physical witnesses in the personified inventory include:
- `4Q174` — Florilegium;
- `4Q171` — Pesher Psalms;
- `4Q390`;
- `4Q286`;
- `4Q463`;
- `4Q175` — Testimonia;
- `4Q177`;
- `4Q386`.

Each remains a separate textual witness. Shared Belial vocabulary does not prove that every work was composed by one author or at one moment.

### 11Q13 / Melchizedek

`11Q13` is a direct Cave 11 manuscript witness.

Personified-Belial loci in the current V1 control include:
- 2:12-13 — Belial and spirits of his lot;
- 2:22 — turning away from Belial;
- 2:25 — deliverance from Belial's hand;
- 3:7 — fiery destruction of Belial, reading/context uncertain.

This gives a particularly clear eschatological opposition structure:
`MELCHIZEDEK'S LOT / JUSTICE`
versus
`BELIAL / SPIRITS OF HIS LOT`.

It does not require identifying Melchizedek with Michael unless separately demonstrated.

## Abstract / ambiguous exclusions

Examples intentionally excluded from the personified inventory include:
- 1QS 10:21 — abstract wickedness in the heart;
- multiple Hodayot (`1QHᵃ`) uses whose semantics are abstract or ambiguous;
- 4Q398 frg. 14-17 ii,5 — "counsel of wickedness";
- 4Q88 10,9-10 — uncertain/possibly abstract.

The complete concordance contains additional damaged `בליעל` forms. V1 does not upgrade them to personified Belial merely because the letters survive.

## Strongest bounded conclusions

1. Personified Belial is not a one-off label: it appears across multiple Qumran textual corpora.
2. Belial's functions include rule/temptation, hostile planning, command of a lot/spirits/army, opposition to the righteous, and eschatological defeat.
3. 1QM 13:10-11 explicitly subordinates Belial to God: God makes/appoints Belial for destruction.
4. That same line calls Belial `מלאך משטמה`, an "angel of hostility/enmity," creating a real lexical bridge to the `mśṭmh` word-family.
5. The lexical bridge does not itself prove Belial and Jubilees' named Mastema are one entity.
6. Qumran's personified Belial remains distinct from abstract `belial` vocabulary in other loci.

## Claim ceiling

This inventory does not establish:
- that every `בליעל` token is a proper name;
- that Belial is a coequal evil god;
- that Belial is identical with Mastema;
- that Belial is identical with Job's `ha-satan`;
- that Belial is identical with the Enochic Watchers or giant spirits;
- one direct literary source for every Belial passage;
- that all "spirits of Belial" traditions derive from one recension or author.
