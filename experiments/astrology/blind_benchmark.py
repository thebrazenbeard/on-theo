from __future__ import annotations

import argparse
import csv
import hashlib
import json
import random
from pathlib import Path

import reference_simulation as sim


PUBLIC_BIRTH_FIELDS = ("agent_id", "birth_t")
PUBLIC_OUTCOME_FIELDS = ("t", "agent_id", "outcome", "environment")
PUBLIC_STATE_FIELDS = (
    "t",
    "p1_lon",
    "p2_lon",
    "p3_lon",
    "p4_lon",
    "d1",
    "d2",
    "illumination",
    "physical",
    "tidal",
    "angular_code",
    "sign_code",
)


def canonical_json_bytes(value) -> bytes:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def write_csv(path: Path, rows, fieldnames):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fieldnames,
            extrasaction="ignore",
        )
        writer.writeheader()
        for row in rows:
            writer.writerow({name: row.get(name, "") for name in fieldnames})


def _run_id(index: int, benchmark_seed: int) -> str:
    token = hashlib.sha256(
        f"{benchmark_seed}:{index}".encode("utf-8")
    ).hexdigest()[:12]
    return f"blind-{index:03d}-{token}"


def generate_benchmark(
    out_dir,
    repeats=2,
    agents=200,
    steps=360,
    benchmark_seed=23,
):
    out = Path(out_dir)
    public_root = out / "public"
    private_root = out / "private"
    public_root.mkdir(parents=True, exist_ok=True)
    private_root.mkdir(parents=True, exist_ok=True)

    assignments = [
        world
        for world in sim.WORLD_TYPES
        for _ in range(repeats)
    ]
    rng = random.Random(benchmark_seed)
    rng.shuffle(assignments)

    answer_runs = []
    public_runs = []

    for index, world in enumerate(assignments, 1):
        run_seed = rng.randrange(1, 2**31)
        run_id = _run_id(index, benchmark_seed)

        births, states, outcomes, culture, truth = sim.run(
            world,
            agents,
            steps,
            run_seed,
        )

        run_dir = public_root / run_id
        run_dir.mkdir(parents=True, exist_ok=True)

        public_births = [
            {
                "agent_id": row["agent_id"],
                "birth_t": row["birth_t"],
            }
            for row in births
        ]

        public_states = [
            {
                field: row[field]
                for field in PUBLIC_STATE_FIELDS
            }
            for row in states
        ]

        public_outcomes = [
            {
                "t": row["t"],
                "agent_id": row["agent_id"],
                "outcome": row["outcome"],
                "environment": row["environment"],
            }
            for row in outcomes
        ]

        write_csv(
            run_dir / "agent_births.csv",
            public_births,
            PUBLIC_BIRTH_FIELDS,
        )
        write_csv(
            run_dir / "celestial_state.csv",
            public_states,
            PUBLIC_STATE_FIELDS,
        )
        write_csv(
            run_dir / "agent_outcomes.csv",
            public_outcomes,
            PUBLIC_OUTCOME_FIELDS,
        )
        write_csv(
            run_dir / "cultural_claims.csv",
            culture,
            ("t", "claim", "mean_belief"),
        )

        seed_commitment = hashlib.sha256(
            str(run_seed).encode("utf-8")
        ).hexdigest()

        manifest = {
            "schema": "ON_THEO_ASTROLOGY_BLIND_RUN_V1",
            "run_id": run_id,
            "agents": agents,
            "steps": steps,
            "seed_commitment_sha256": seed_commitment,
            "observable_files": [
                "agent_births.csv",
                "celestial_state.csv",
                "agent_outcomes.csv",
                "cultural_claims.csv",
            ],
        }

        (run_dir / "manifest.json").write_text(
            json.dumps(
                manifest,
                indent=2,
                sort_keys=True,
            ),
            encoding="utf-8",
        )

        public_runs.append(manifest)
        answer_runs.append(
            {
                "run_id": run_id,
                "world": world,
                "seed": run_seed,
                "seed_commitment_sha256": seed_commitment,
                "coupling": truth["coupling"],
            }
        )

    private_key = {
        "schema": "ON_THEO_ASTROLOGY_BLIND_ANSWER_KEY_V1",
        "benchmark_seed": benchmark_seed,
        "repeats_per_world": repeats,
        "runs": answer_runs,
    }
    answer_key_commitment = hashlib.sha256(
        canonical_json_bytes(private_key)
    ).hexdigest()

    public_index = {
        "schema": "ON_THEO_ASTROLOGY_BLIND_BENCHMARK_PUBLIC_V1",
        "run_count": len(public_runs),
        "world_labels_withheld": True,
        "answer_key_commitment_sha256": answer_key_commitment,
        "runs": [
            {
                "run_id": row["run_id"],
                "agents": row["agents"],
                "steps": row["steps"],
                "path": f'{row["run_id"]}/manifest.json',
            }
            for row in public_runs
        ],
    }

    (public_root / "benchmark.json").write_text(
        json.dumps(
            public_index,
            indent=2,
            sort_keys=True,
        ),
        encoding="utf-8",
    )
    (private_root / "answer_key.json").write_text(
        json.dumps(
            private_key,
            indent=2,
            sort_keys=True,
        ),
        encoding="utf-8",
    )

    return public_index, private_key


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="blind-benchmark")
    parser.add_argument("--repeats", type=int, default=2)
    parser.add_argument("--agents", type=int, default=200)
    parser.add_argument("--steps", type=int, default=360)
    parser.add_argument("--benchmark-seed", type=int, default=23)
    args = parser.parse_args(argv)

    generate_benchmark(
        args.out,
        repeats=args.repeats,
        agents=args.agents,
        steps=args.steps,
        benchmark_seed=args.benchmark_seed,
    )


if __name__ == "__main__":
    main()
