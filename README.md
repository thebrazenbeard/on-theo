> **License:** Source-visible, not open source. Original material is proprietary. Commercial use, redistribution, hosted-service use, and commercial derivative products require written permission. See [LICENSE](LICENSE) and [COMMERCIAL_LICENSE.md](COMMERCIAL_LICENSE.md). Separately identified third-party components retain their own licenses.

# On-Theo — comparative theology and provenance research

On-Theo is a reusable, evidence-disciplined **research corpus, claim registry, and validation toolkit** for comparing religious traditions, their historical development, and later philosophical interpretations. It currently provides curated research documents, structured YAML provenance registries, and Python validation/rehearsal tools—not a hosted research service, automatic historical fact-checker, or model-authenticated authority.

Researchers can use the methodology and registry schemas as a starting point for their own source-critical projects, subject to the repository's licensing terms. A passing validator establishes **internal consistency of recorded relationships**, not the historical truth of the entries.

## What is available today

| Component | Reusable purpose | Evidence boundary |
| --- | --- | --- |
| [Research method](docs/METHOD.md) and [claim schema](docs/CLAIM_SCHEMA.md) | Keep source attestations, dates, witnesses, academic disputes, and project inferences separate | A project classification is not an independent scholarly ruling |
| [Tradition and comparison corpus](traditions/) and [research packets](research/) | Source-oriented questions about Jewish, Christian, Islamic, and adjacent traditions | Corpus coverage is partial; branches and drafts are not automatically canonical |
| [YAML registries](registry/) and [registry validator](tools/on_theo_registry/validator.py) | Detect stable-ID collisions, unresolved references, manifest/dependency inconsistencies, and invalid review terminology | Structural validation is not source authentication or truth certification |
| [Rebase-precondition audit](scripts/audit_rebase_preconditions.py) and [materialization rehearsal](scripts/rehearse_materialization.py) | Inspect proposed registry extensions before any promotion | Audit/rehearsal outputs do not automatically merge or authorize research changes |
| [Speculative synthesis](synthesis/) | Explore analogies between ancient symbols and modern systems concepts | Explicitly a hypothesis layer, never evidence that ancient writers described computers |

## Use it for a research project

1. Start with the [method](docs/METHOD.md), [corpus scope](docs/CORPUS_SCOPE_V1.md), and [claim schema](docs/CLAIM_SCHEMA.md).
2. Identify the primary text, surviving witness, composition date, competing interpretations, and gaps for each proposed claim. Do not treat a late tradition as a contemporary witness.
3. Add or inspect registry entries as **research evidence**, keeping proposed extensions on review branches until reconciled.
4. Run the read-only consistency validator from a source checkout:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_registry.py --root .
python scripts/validate_registry.py --root . --json
```

The validator checks references and graph conventions. It does **not** fetch ancient documents, independently authenticate a manuscript, decide competing historical claims, promote a branch, or authorize actions in a host system.

### Running the tests

```bash
python -m pytest -q
```

Most tests exercise the registry schema, consistency rules, and review/materialization boundaries. The **historical rebase-precondition** test additionally invokes Git against historical commit IDs recorded in [extension-manifest.yaml](registry/extension-manifest.yaml). Some are outside current `main` ancestry; a shallow checkout or a clone without those historical objects can fail with a missing-commit error. A full test result therefore depends on obtaining the specific historical Git objects, not just installing the Python requirements. For a portable first check, use the registry-validator command above.

## Evidence discipline

Never collapse these categories:

1. **PRIMARY TEXT** — what an identified text actually says.
2. **HISTORICAL RECONSTRUCTION** — what historians reasonably infer from available evidence.
3. **LATER TRADITION** — accounts or interpretations arising after the claimed event.
4. **SCHOLARLY INTERPRETATION** — attributed academic readings and disputes.
5. **PROJECT INFERENCE** — reasoning within this repository from cited material.
6. **SPECULATIVE MODEL** — deliberate analogy, including the GOD/runtime/simulation framework.
7. **UNKNOWN** — the evidence does not justify a stronger claim.

The detailed [research method](docs/METHOD.md) also separates material evidence, event date, source-composition date, and surviving-manuscript date. Similarity alone does not establish borrowing, common authorship, supernatural origin, or historical accuracy. A compelling analogy is not a source citation.

## Research questions and scope

The initial corpus investigates:

- First-century Jewish meanings of *Kingdom of God*, Messiah, Son of Man, resurrection, Sheol, Gehenna, Torah, and Temple before later doctrinal compression.
- What source evidence permits—or does not permit—about Yeshua's birth, social setting, Nazareth, undocumented years, hometown rejection, and Panthera/Pandera traditions.
- How later Jewish, Christian, and Qur'anic traditions preserve, contest, and reinterpret earlier themes, with chronological dependence kept explicit.
- Recurring accounts of creation, delegated authority, revelation, judgment, resurrection, and transcendence.
- Experimental mappings of source concepts into modern computational metaphors without projecting contemporary technology into ancient authorship.

No tradition receives automatic deference or automatic contempt. Disagreement is research evidence, not a flaw to erase for a tidy synthesis.

## Canonical state and limits

`main` carries the reconciled infrastructure and baseline corpus. The `traditions/`, `chronology/`, `comparative/`, `research/`, `registry/`, and `synthesis/` namespaces contain durable materials. Thematic branches (for example `tradition/judaism`, `tradition/christianity`, `tradition/islam`, and `history/chronology`) may preserve unreconciled provenance, but their mere existence does not elevate their contents to canonical evidence.

On-Theo is a research resource and validation toolkit, not an identity provider, consent registry, cryptographic provenance authority, historical truth oracle, or operational AI control plane. A downstream system must independently authenticate people and providers, enforce access and publication permissions, and distinguish source records from generated interpretations.
