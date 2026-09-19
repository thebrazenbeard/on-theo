# ON_THEO CHAT CONTINUATION — 2026-09-19 V1

Status: DURABLE_CONTINUATION_CHECKPOINT / NOT_CANONICAL / RESTORE_THEN_FRESH_CHECK

## 0. Restore intent

This file preserves the current ON_THEO research frontier, corrections, open-PR state, user-created branch portfolio, and exact next work so a new chat can continue without relying on chat-local memory.

Freshness rule:
- treat every SHA/state below as a checkpoint snapshot;
- fresh-check repository/branch/PR state before any new write;
- never carry PASS/FAIL/mergeability/review state across a moved head;
- do not merge, canonically promote, delete branches, modify main, deploy, or perform other protected effects without Patrick's exact authority.

Primary repository:
- thebrazenbeard/on-theo

Main at checkpoint:
- eedbcf660c2cfe6cff5636e798806b0cd3d56efc

## 1. Active research tip

Current single active successor tip:
- PR #73
- title: Research: Ilimilku/Attenu named-carrier control V1
- branch: research/ugarit-ilimilku-attenu-carrier-control-v1-20260918
- head: 6d9004a17dc04d5dd399407c4a37e48c7766bcaa
- base branch: research/ugarit-dumuzi-syllabic-corpus-search-v1-20260918
- base head: c82601e33df54f7d2d15863df68540fd7a6b25d1
- state at checkpoint: OPEN / DRAFT / MERGEABLE-CLEAN / UNMERGED / NOT CANONICAL

PR #72 was closed as superseded after #73 verified clean.

PR #33 remains:
- Candidate: byte-bound registry materialization V1
- head: 7ac78cb61ec216fe98347b33b6ff07c2a3aed81c
- DRAFT / HOLD / DO NOT MERGE
- candidate integrity previously verified
- canonical promotion remains blocked pending genuinely independent reviewer receipts plus separate merge authority.
Do not clear or reinterpret this HOLD from same-runtime review evidence.

## 2. ON_THEO method controls

Evidence classes:
- PRIMARY_TEXT
- MATERIAL_EVIDENCE
- HISTORICAL_RECONSTRUCTION
- LATER_TRADITION
- SCHOLARLY_INTERPRETATION
- PROJECT_INFERENCE
- SPECULATIVE_MODEL
- UNKNOWN

Core rules:
- reconstruct traditions internally/diachronically before comparison;
- distinguish source/work identity from physical witness and access surface;
- later theology must not be projected backward;
- motif similarity != transmission;
- chronology/contact alone != transmission;
- transmission requires chronology + contact + relevant carrier/source exposure + semantic fit + directional/source-specific evidence;
- structural parallel is the default absent lineage evidence;
- English motif labels must not replace source-language comparison;
- scholastic deity equivalence != total cultic/mythological identity;
- digital search non-hit != historical absence;
- old claim snapshots can be superseded by later exact controls and must not silently revive;
- open/green/reviewed PR != canonical state.

## 3. Dumuzid → Baal research chain: current evidence-governed state

The chain was advanced through successive clean draft tips while predecessor research PRs were closed as superseded.

Important current synthesis was persisted in:
- comparative/dumuzid-baal-transmission-evidence-ladder-v1.md
- comparative/dumuzid-baal-transmission-evidence-ladder-v1.yaml
- registry/extensions/dumuzid-baal-transmission-evidence-ladder-v1.yaml

Evidence-ladder predecessor tip:
- PR #71
- head: 89920c8e281b97a2806708a21c16e0115f884f64
- closed when #72 verified clean.

Current ladder result:
- CHRONOLOGY: PASS
- REGIONAL CONTACT: PASS
- MESOPOTAMIAN LITERARY CONTACT AT UGARIT: PASS
- DUMUZI-SPECIFIC UGARIT SCHOLASTIC EXPOSURE: PASS
- INSTITUTIONAL CARRIER CAPACITY: PASS
- NAMED CARRIER: now refined to PARTIAL NETWORK IDENTIFIED / RELEVANT SOURCE CARRIER NOT ESTABLISHED
- DUMUZI DEATH-RETURN NARRATIVE AT UGARIT: NOT ESTABLISHED
- LOCAL DUMUZI EQUIVALENT: OPEN / LOST DATUM
- PROPOSITION-LEVEL SEMANTIC MATCH: PARTIAL
- LEXICAL/FORMULA DEPENDENCE: NOT ESTABLISHED
- SOURCE-SPECIFIC BORROWING SIGNAL: NOT ESTABLISHED
- DIRECTION: UNRESOLVED
- DIRECT DUMUZID→BAAL TRANSMISSION: NONE ESTABLISHED
- INFLUENCE: PLAUSIBLE BUT UNPROVEN

This is not an impossibility claim.

## 4. Critical corrections and supersessions

### A. A.1146 morphology correction

Earlier state:
- A.1146 reconstructed death verb treated as secure agentive Akkadian daku "kill."

Corrected state:
- death/harm context remains strong;
- English "they kill him" retained only as scholarly reconstruction;
- daku lemma/morphology is DISPUTED;
- exact morphology remains unresolved;
- a Sasson alternative involving pressing/pushing/piercing is only a reported scholarly alternative;
- iterative taru return control is retained separately;
- no-shared-Dumuzid/Baal-lexical-formula conclusion survives in narrower form.

Durable files:
- comparative/a1146-morphology-correction-v1.md
- comparative/a1146-morphology-correction-v1.yaml
- registry/extensions/a1146-morphology-correction-v1.yaml

Do not revive the older secure-daku claim from predecessor snapshots.

### B. Dumuzi at Ugarit correction

Earlier state:
- no Dumuzi/Tammuz source identified at Ugarit.

Corrected state:
- RS 20.123+ / Ugaritica 5, 137 / CDLI P332950 directly preserves Dumuzi in a Middle Babylonian lexical/scholastic tablet excavated at Ugarit;
- reverse ii 7 preserves Mesopotamian Dumuzi and Hurrian du-mu-zi;
- the Ugaritic-equivalent field is broken/lost;
- this proves Dumuzi-specific SCHOLASTIC exposure at Ugarit;
- it does NOT prove a Dumuzi narrative, local cult, Baal equation, or Ilimilku-specific access.

Durable files:
- comparative/ugarit-dumuzi-direct-attestation-v1.md
- comparative/ugarit-dumuzi-direct-attestation-v1.yaml
- registry/extensions/ugarit-dumuzi-direct-attestation-v1.yaml

### C. Dumuzi equivalence at Ugarit

P332950:
- Dumuzi row: Dumuzi = Hurrian du-mu-zi = [Ugaritic field lost]
- Utu row: Utu = Shimigi = Shapshu
- Baal row: Imzuanna = Teshub = Baal

Targeted parallel search did not recover the lost Ugaritic Dumuzi equivalent.
Status:
- LOCAL UGARITIC DUMUZI EQUIVALENT = UNRESOLVED
- DUMUZI=BAAL = NOT ESTABLISHED

The preserved Imzuanna-Teshub-Baal row is a hostile control:
- god-list equations can reflect learned/sign-based scribal correspondence;
- they do not automatically establish full cultic or mythological identity;
- Baal's preserved row does not license restoring Baal into Dumuzi's broken field.

Durable files:
- comparative/ugarit-dumuzi-equivalence-control-v1.*
- registry/extensions/ugarit-dumuzi-equivalence-control-v1.yaml
- comparative/ugarit-baal-scholastic-equivalence-v1.*
- registry/extensions/ugarit-baal-scholastic-equivalence-v1.yaml

## 5. Mari source controls

Mari evidence is deliberately asymmetric.

A.1146:
- original publication provenance confirmed: Pierre Marello, 1992, Florilegium marianum I, pp. 115–126;
- ARCHIBAB T1011;
- crucial Dumuzi death/return passage damaged and reconstruction-dependent;
- spring restoration / cult-statue journey / exact ritual calendar are secondary reconstructions.

A.4540:
- Jacquet 2011 / FM XII;
- current lexical control supports line 4 ana temrim sha Dumuzi = "for the burial of Dumuzi";
- burial evidence does not itself prove return/resurrection.

MARI 5 p. 599 no. 14:
- resolved as Dominique Charpin 1987, MARI 5, p. 599 no. 14;
- CDLI P497204;
- publication identity secure;
- line-level transliteration remained unrecovered in the completed pass.

A.512:
- direct published wording that Dumuzi was caused to enter the temple of Annunitum of Mari;
- temple entry != bodily resurrection.

M.13167:
- reported oil-ration record for Dumuzi entering Belet-ekallim, dated 10/x/ZL2;
- transcription control attributed to Duponchel 1997 p. 222;
- direct collation pending.

M.15090:
- unpublished parallel reported by Charpin;
- lower evidence ceiling.

Result:
MARI_CONTACT_FIELD = RETAINED / STRONGER AND NARROWER
DEATH + BURIAL + TEMPLE-ENTRY + REPORTED RETURN
!= one undifferentiated resurrection rite.

## 6. Baal physical-witness and scribal controls

KTU 1.5:
- RS 2.[022] + RS 3.[565]
- Louvre AO 16641 + AO 16642
- Baal death announcement bound to this physical witness.

KTU 1.6:
- RS 2.[009] + RS 5.155
- Louvre AO 16636
- renewed-life recognition bound to this separate physical witness
- full Ilimilku colophon bound here.

Rule:
CYCLE-LEVEL DEATH/RETURN != SINGLE-TABLET DEATH/RETURN.
KTU 1.5 and 1.6 are distinct physical artifacts joined at literary/cycle level.

Ilimilku:
- directly named on KTU 1.4 and KTU 1.6;
- attribution of other Baal Cycle tablets is cycle/ductus reconstruction, not six direct colophons;
- named scribe != original author of every inherited motif;
- named scribe != proven Dumuzid transmission carrier.

## 7. Ugarit scribal-contact controls

Physical Mesopotamian literature at Ugarit:
- Akkadian Middle Babylonian Gilgamesh witnesses including P500683 / RS 94.2066, P500685 / RS 94.2082, P500686 / RS 94.2083.

Cuneiform school tradition:
- ORACC/DCCLT Ugarit lexical/school materials;
- general Mesopotamian literary/scholastic contact capacity = SUPPORTED.

Dumuzi-specific Ugarit witness:
- P332950 / RS 20.123+ / Ugaritica 5, 137
- House of Rapanu, room 5 / Residential Quarter archive context;
- Dumuzi-specific scholastic exposure = SUPPORTED.

Archive separation:
- House of Rapanu: P332950 Dumuzi lexical witness / scribal-training context.
- House of High Priest: Baal Cycle / Ilimilku literary corpus.
- House of Urtenu: KTU 1.179, Ilimilku-associated mythico-magical text / colophon pattern.

Same city / scribal culture != same archive or direct tablet transfer.

## 8. Alphabetic and syllabic Dumuzi corpus searches

Alphabetic-Ugaritic targeted search:
- no controlled independent Dumuzi/Tammuz deity, ritual, offering-list, or mythological occurrence recovered;
- variants included Dumuzi, Dumuzid, Tammuz, tmz, dmz;
- current ORACC AEMW Ugarit divine-name index gives no indexed Dumuzi/Tammuz hit.

Status:
ALPHABETIC UGARITIC DUMUZI OCCURRENCE = NOT FOUND IN TARGETED V1 SEARCH
HISTORICAL ABSENCE = NOT PROVEN.

Syllabic/cuneiform targeted search:
- P332950 remains the only controlled direct Dumuzi divine-name witness recovered in the current accessible Ugarit syllabic/lexical search;
- no second controlled witness recovered;
- historical uniqueness is NOT claimed.

Dadmis/Tadmis false-positive control:
- Dadmis/Tadmis is not a second Dumuzi occurrence;
- on P332950 Dumuzi = r ii 7;
- Suzianna/Tadmis/Dadmishu is a separate row at iii 15'.

Tammuz/Du'uzu month-name route:
- no controlled Ugarit month-name hit recovered in the completed bounded pass;
- incomplete index access blocks absence claims.

## 9. Named-carrier frontier completed in PR #73

Direct:
- Ilimilku is Attenu's student.
- Attenu bears prln, understood in current work through Hurrian professional/divinatory vocabulary.
- KTU 1.179 repeats the Ilimilku/Shubbanite/student-of-Attenu pattern and is from the House of Urtenu.

Important correction:
- older proposed KTU 1.179 restoration "scribe of Babylon" is uncertain;
- current readable treatments leave the relevant lines fragmentary;
- ATTENU SCRIBE OF BABYLON = NOT SECURE PRIMARY TEXT;
- ATTENU BABYLONIAN TRAINING = NOT ESTABLISHED.

Current G07 named-carrier state:
- named target scribe: PASS
- named teacher: PASS
- cross-archive Ilimilku presence: PASS
- general multilingual scribal network: PASS
- direct Rapanu→Urtenu transfer: NOT ESTABLISHED
- Ilimilku access to P332950: NOT ESTABLISHED
- Attenu access to P332950: NOT ESTABLISHED
- named carrier of a Dumuzi death-return source: NOT ESTABLISHED
- overall: PARTIAL NETWORK IDENTIFIED / RELEVANT SOURCE CARRIER NOT ESTABLISHED

Durable files in PR #73:
- comparative/ilimilku-attenu-carrier-control-v1.md
- comparative/ilimilku-attenu-carrier-control-v1.yaml
- registry/extensions/ilimilku-attenu-carrier-control-v1.yaml
- registry/extension-manifest.yaml registration

## 10. User-created branch portfolio is now part of the task

Patrick explicitly stated that populating the new branches is part of ON_THEO work.

Do not treat these branches as foreign/noise.
Fresh-check each exact branch head before writes because several changed during this chat.

Current user-created/master branches known at checkpoint:
- asatru
- buddhism
- chrisanity-master   [preserve exact spelling]
- hindu
- islam
- judaism
- shinto
- shinto-1
- sim-theory
- sumerian
- taoism
- history/chronology
- synthesis/commonality
- tradition/christianity
- tradition/islam
- tradition/judaism

At initial inventory many master branches were one-file seed placeholders, but several were populated concurrently before checkpoint. Never assume they remain seed-only.

Open master/corpus PRs at checkpoint:
- #59 Corpus hub: Christianity master research lane V1 — head efafea1d04c4dcd8543200c022a037f36471bc5f — branch chrisanity-master — base main
- #60 Corpus hub: Judaism master research lane V1 — head cb7825ceba44ea05a2111d94ae50d91fb67ad1f9 — branch judaism — base main
- #62 Corpus hub: Sumerian religion master research lane V1 — head bd6b6572141dc2f48f2f104b8f25301662d4a06f — branch sumerian — base main
- #63 Research hub: simulation theory and discriminability V1 — head 8f8af585b8a73bcf830953b8eef4cd0c6c837603 — branch sim-theory — base main
- #64 Corpus: Daoism source-control foundation V1 — head 30de6433ab2bdce86b88fcdad1a3134084ed39ab — branch taoism — base main
- #65 Corpus: Shinto source-control foundation V1 — head a578729a2e3cec02fe533c3c1d20946347da9aa4 — branch shinto — base main
- #67 Corpus: Buddhism diachronic source foundation V1 — head b9f2e2a635cd98129b0a0122aeb8a2e7a65cfaa5 — branch buddhism — base main
- #68 Review: Shinto hostile source-control lane V1 — head 58917fbd88cdba79fc16eca27d33feb2b92a02a1 — branch shinto-1 — base main
- #69 Corpus: Asatru / Norse religion source foundation V1 — head 4af66d0bb3aa3f9bbfcd45fb52b400045b9d5339 — branch asatru — base main
- #70 Corpus: Hindu traditions source foundation V1 — head ccd5b82cf99fa9dfda238366a93447047f74b1fa — branch hindu — base main
- #74 Corpus hub: Islam master research lane V1 — head 827815e8806fa038f9ecb23abf558d608826eee8 — branch islam — base main

Additional substantial user branches seen without relying on open-PR state:
- history/chronology
  initial inventory against main: ahead 3 / behind 2; files included chronology/MASTER_TIMELINE.md, chronology/README.md, chronology/entries.yaml.
- synthesis/commonality
  initial inventory against main: ahead 8 / behind 2; files included synthesis/GOD-model.md, PROVENANCE.md, README.md, commonality-matrix.md, epistemic-tests.md, experimental-research-program.md, transmission-vs-convergence.md, yeshua-substrate-skepticism.md.
- tradition/christianity
  initial inventory: ahead 7 / behind 2; files included README, birth/paternity/infancy, christology development, earliest layers, Mary Magdalene/authority, noncanonical/gnostic-adjacent, sources.
- tradition/islam
  initial inventory: ahead 7 / behind 2; files included README, creation/humanity/test, death/resurrection/judgment, late-antique context, Mary/Jesus, sources, systems analogy.
- tradition/judaism
  initial inventory: ahead 6 / behind 2; files included README, concepts-before-Christianity, Panthera countertraditions, Second Temple context, sources, Yeshua material.

These inventories are snapshots only. Fresh-check before modifying.

## 11. Branch-population task

Patrick's latest directive:
- populating the user-created religion/topic branches is part of the ongoing ON_THEO task;
- continue ON_THEO research while also building those branch corpora.

Recommended next workflow:

A. Restore/fresh-check:
- PR #73 exact state/head;
- main;
- open PRs;
- exact heads of all master/topic branches above.

B. Do not overwrite concurrent work:
- compare each user branch to main and to any related tradition/corpus PR branch;
- if branch moved since checkpoint, read current files before writing;
- avoid force/stale overwrite.

C. Populate each branch as a coherent corpus hub, not a one-file dump.
Suggested standard structure where compatible:
- README / scope and diachronic boundaries
- primary sources / witness layers
- historical development
- ritual/practice/material evidence
- cosmology / anthropology / death/afterlife
- deity/concept ontology
- chronology
- internal plurality / sectarian diversity
- later reception
- comparative guards
- source bibliography/provenance
- machine-readable claims/registry extensions only when structurally appropriate.

D. Priority order:
1. fresh-check already-populated master PRs (#59/#60/#62–#70/#74) for thin spots and duplication;
2. history/chronology;
3. synthesis/commonality, with strong controls against flattening traditions into one perennialist model;
4. tradition/christianity, tradition/judaism, tradition/islam;
5. continue remaining master branches and review lanes;
6. keep the Dumuzid→Baal frontier moving from PR #73 in parallel, but do not let it monopolize ON_THEO.

E. High-value research standards for branch population:
- primary texts first;
- date/witness provenance;
- diachronic internal reconstruction;
- material evidence where available;
- distinguish normative theology from historical practice;
- distinguish modern reconstruction from primary source;
- preserve intra-tradition plurality;
- avoid treating present-day forms as timeless;
- comparative claims only after internal reconstruction;
- negative search results typed as bounded search-state evidence.

## 12. Existing older ON_THEO PR lanes still open

At checkpoint, older open draft lanes include:
- #28 consolidation candidate
- #29 validator V2
- #30 materialization rehearsal V1
- #31 validator V3 successor
- #32 pre/post materialization tests
- #33 byte-bound materialization candidate HOLD
- earlier corpus/research PRs #5, #7, #12–#24.

Do not close or merge these merely because the active Dumuzid research successor chain closed its own predecessors. Their governance/engineering roles are distinct.

## 13. Open-PR hygiene rule

For the active successor research pattern:
- open a new child draft from the exact clean active tip;
- verify OPEN + DRAFT + MERGEABLE-CLEAN + exact base/head;
- only then close the immediately superseded predecessor from that same chain;
- never close unrelated PR numbers just because GitHub consumed intervening numbers;
- PR numbers #59/#60/#62–#70/#74 are user/master corpus work and must not be mistaken for research-chain noise.

## 14. Bus / communication

Historical project rule says non-PR work communication should use the Chat Communication Bus.

However, the R10 Bus topology had a previously recorded conflict:
- exact R10 topology mapped Vera to bus/vera-v2;
- live branch topology had drifted to a different mapping.

Do not blindly write Bus until current routing/topology is fresh-checked and reconciled.
A PR body itself remains appropriate PR-local provenance.

## 15. Exact next research frontier after restore

Primary immediate frontier from PR #73:
1. fresh-check PR #73 and branch head;
2. inspect whether current Ugarit prosopography can establish any source-specific bridge from House of Rapanu / P332950 to House of Urtenu / Attenu / Ilimilku without relying on uncertain KTU 1.179 Babylon restoration;
3. if no stronger carrier edge is found, preserve G07 as PARTIAL and move to the next gate rather than over-searching one hypothesis;
4. likely next direct-transmission gate after G07: source-specific borrowing / distinctive narrative sequence versus common regional mythologem.

Parallel portfolio frontier:
- start systematic population/audit of the user-created master/topic branches listed above;
- do not wait for Dumuzid/Baal research to finish before expanding the broader religion corpus.

## 16. Protected boundaries

No authority from this checkpoint to:
- merge PRs;
- modify main;
- delete branches;
- canonically materialize registry state;
- clear PR #33 HOLD;
- deploy;
- change credentials/providers/permissions;
- force-push/stale overwrite;
- publish private material.

Branch/file/PR work may continue within the existing research pattern, with exact-head checks before writes.

## 17. Restore command

Recommended new-chat command:

ON_THEO::RESTORE_AND_RUN::ON_THEO_CHAT_CONTINUATION_20260919_V1

On receipt:
- read this checkpoint from branch state/on-theo-chat-continuation-20260919-v1;
- verify its file/blob/commit against the restore receipt if present;
- fresh-check main, PR #73, PR #33, open PRs, and all user-created master/topic branches;
- resume both the active Dumuzid→Baal research frontier and the branch-population portfolio;
- preserve all supersessions/corrections above;
- do not merge/canonically promote without Patrick's exact authority.
