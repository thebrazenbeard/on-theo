import csv
import json
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import blind_benchmark as bench
import reference_simulation as sim
import score_benchmark as scorer


class BlindBenchmarkTests(unittest.TestCase):
    def test_public_projection_removes_leaks(self):
        with tempfile.TemporaryDirectory() as directory:
            public, private = bench.generate_benchmark(
                directory,
                repeats=1,
                agents=12,
                steps=30,
                benchmark_seed=9,
            )

            self.assertEqual(
                public["run_count"],
                8,
            )
            self.assertEqual(
                len(private["runs"]),
                8,
            )

            run_id = public["runs"][0]["run_id"]
            run_dir = (
                Path(directory)
                / "public"
                / run_id
            )

            manifest = json.loads(
                (
                    run_dir
                    / "manifest.json"
                ).read_text(
                    encoding="utf-8"
                )
            )

            self.assertNotIn(
                "world",
                manifest,
            )
            self.assertNotIn(
                "seed",
                manifest,
            )
            self.assertNotIn(
                "coupling",
                manifest,
            )

            with (
                run_dir
                / "agent_births.csv"
            ).open(newline="") as handle:
                fields = next(
                    csv.reader(handle)
                )

            self.assertEqual(
                fields,
                [
                    "agent_id",
                    "birth_t",
                ],
            )

            with (
                run_dir
                / "agent_outcomes.csv"
            ).open(newline="") as handle:
                fields = next(
                    csv.reader(handle)
                )

            self.assertEqual(
                fields,
                [
                    "t",
                    "agent_id",
                    "outcome",
                    "environment",
                ],
            )

            forbidden = {
                "probability",
                "trait",
                "belief",
                "base_trait",
                "initial_trait",
                "birth_signal",
                "controller",
            }

            self.assertTrue(
                forbidden.isdisjoint(fields)
            )

    def test_all_worlds_once_when_repeats_one(self):
        with tempfile.TemporaryDirectory() as directory:
            _, private = bench.generate_benchmark(
                directory,
                repeats=1,
                agents=5,
                steps=10,
                benchmark_seed=2,
            )

            self.assertEqual(
                {
                    row["world"]
                    for row in private["runs"]
                },
                set(sim.WORLD_TYPES),
            )

    def test_deterministic_answer_key(self):
        with tempfile.TemporaryDirectory() as first:
            with tempfile.TemporaryDirectory() as second:
                _, key_one = bench.generate_benchmark(
                    first,
                    repeats=1,
                    agents=5,
                    steps=10,
                    benchmark_seed=4,
                )
                _, key_two = bench.generate_benchmark(
                    second,
                    repeats=1,
                    agents=5,
                    steps=10,
                    benchmark_seed=4,
                )

                self.assertEqual(
                    key_one,
                    key_two,
                )

    def test_answer_key_commitment_verifies(self):
        with tempfile.TemporaryDirectory() as directory:
            public, private = bench.generate_benchmark(
                directory,
                repeats=1,
                agents=5,
                steps=10,
                benchmark_seed=4,
            )

            digest = scorer.verify_answer_key_commitment(
                public,
                private,
            )

            self.assertEqual(
                digest,
                public[
                    "answer_key_commitment_sha256"
                ],
            )

    def test_perfect_frozen_submissions_score_one(self):
        with tempfile.TemporaryDirectory() as directory:
            _, key = bench.generate_benchmark(
                directory,
                repeats=1,
                agents=5,
                steps=10,
                benchmark_seed=5,
            )

            submissions = {
                "submissions": [
                    {
                        "run_id": row["run_id"],
                        "predicted_world": row["world"],
                        "frozen_before_unblinding": True,
                    }
                    for row in key["runs"]
                ]
            }

            report = scorer.score(
                key,
                submissions,
            )

            self.assertEqual(
                report["accuracy_on_submitted"],
                1.0,
            )
            self.assertEqual(
                report["coverage"],
                1.0,
            )
            self.assertEqual(
                report["exact_correct"],
                8,
            )

    def test_unresolved_scores_as_unresolved_not_correct(self):
        with tempfile.TemporaryDirectory() as directory:
            _, key = bench.generate_benchmark(
                directory,
                repeats=1,
                agents=5,
                steps=10,
                benchmark_seed=6,
            )
            row = key["runs"][0]

            report = scorer.score(
                key,
                {
                    "submissions": [
                        {
                            "run_id": row["run_id"],
                            "predicted_world": "UNRESOLVED",
                            "frozen_before_unblinding": True,
                        }
                    ]
                },
            )

            self.assertEqual(
                report["unresolved"],
                1,
            )
            self.assertEqual(
                report["exact_correct"],
                0,
            )

    def test_unfrozen_submission_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            _, key = bench.generate_benchmark(
                directory,
                repeats=1,
                agents=5,
                steps=10,
                benchmark_seed=7,
            )
            row = key["runs"][0]

            with self.assertRaises(ValueError):
                scorer.score(
                    key,
                    {
                        "submissions": [
                            {
                                "run_id": row["run_id"],
                                "predicted_world": row["world"],
                                "frozen_before_unblinding": False,
                            }
                        ]
                    },
                )


if __name__ == "__main__":
    unittest.main()
