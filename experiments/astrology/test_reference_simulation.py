import json
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import reference_simulation as sim


class ReferenceSimulationTests(unittest.TestCase):
    def test_all_worlds_run(self):
        for world in sim.WORLD_TYPES:
            births, states, outcomes, culture, truth = sim.run(
                world, 12, 40, 11
            )
            self.assertEqual(len(births), 12)
            self.assertEqual(len(states), 40)
            self.assertGreater(len(outcomes), 0)
            self.assertEqual(truth["world"], world)

    def test_deterministic(self):
        self.assertEqual(
            sim.run("S5_COMMON_CAUSE", 20, 50, 3),
            sim.run("S5_COMMON_CAUSE", 20, 50, 3),
        )

    def test_private_controller_not_in_observed_state(self):
        _, states, _, _, _ = sim.run("S5_COMMON_CAUSE", 5, 10, 1)
        self.assertNotIn("controller", states[0])

    def test_world_types_have_distinct_ground_truth_classes(self):
        couplings = {
            sim.run(world, 5, 10, 1)[4]["coupling"]
            for world in sim.WORLD_TYPES
        }
        self.assertGreaterEqual(len(couplings), 7)

    def test_cli_outputs(self):
        with tempfile.TemporaryDirectory() as directory:
            sim.main(
                [
                    "--world",
                    "S2_NATAL_SEED",
                    "--agents",
                    "8",
                    "--steps",
                    "20",
                    "--seed",
                    "5",
                    "--out",
                    directory,
                ]
            )
            path = Path(directory)
            for name in (
                "world_manifest.json",
                "agent_births.csv",
                "celestial_state.csv",
                "agent_outcomes.csv",
                "cultural_claims.csv",
                "ground_truth_private.json",
            ):
                self.assertTrue((path / name).exists(), name)

            manifest = json.loads(
                (path / "world_manifest.json").read_text(encoding="utf-8")
            )
            self.assertEqual(manifest["world"], "S2_NATAL_SEED")


if __name__ == "__main__":
    unittest.main()
