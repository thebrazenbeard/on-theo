from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import random
from dataclasses import dataclass
from pathlib import Path
from typing import Dict

WORLD_TYPES = (
    "S0_NULL",
    "S1_PHYSICAL",
    "S2_NATAL_SEED",
    "S3_RUNTIME",
    "S4_PLASTICITY",
    "S5_COMMON_CAUSE",
    "S6_CULTURAL_ONLY",
    "S7_WEAK_SIGNAL_CULTURAL",
)


def logistic(x: float) -> float:
    if x >= 0:
        z = math.exp(-x)
        return 1 / (1 + z)
    z = math.exp(x)
    return z / (1 + z)


def wrap_deg(x: float) -> float:
    return x % 360.0


def angle_sep(a: float, b: float) -> float:
    d = abs((a - b) % 360.0)
    return min(d, 360.0 - d)


def stable_unit(text: str) -> float:
    digest = hashlib.sha256(text.encode("utf-8")).digest()
    return int.from_bytes(digest[:8], "big") / (2**64 - 1)


def celestial_state(t: int) -> Dict[str, float]:
    periods = {"p1": 37.0, "p2": 61.0, "p3": 97.0, "p4": 149.0}
    phase = {name: wrap_deg(360.0 * t / period) for name, period in periods.items()}

    d1 = 1.0 + 0.18 * math.sin(math.radians(phase["p1"]))
    d2 = 1.5 + 0.25 * math.sin(math.radians(phase["p2"] + 41.0))
    illumination = (
        1.0 + math.cos(math.radians(phase["p1"] - phase["p2"]))
    ) / 2.0

    sep = min(
        angle_sep(phase["p1"], phase["p3"]),
        angle_sep(phase["p2"], phase["p4"]),
    )
    angular_code = (
        1.0 if min(abs(sep - target) for target in (0, 60, 90, 120, 180)) <= 6 else 0.0
    )
    sign_code = (
        int(phase["p1"] // 30)
        + 2 * int(phase["p2"] // 30)
        + 3 * int(phase["p3"] // 30)
    ) % 7

    physical = (1 / d1**2) + (0.6 / d2**2) + 0.25 * illumination
    tidal = (1 / d1**3) + (0.6 / d2**3)

    # Hidden state is deliberately excluded from observable celestial_state.csv.
    controller = (
        math.sin(math.radians(phase["p4"] * 2 + phase["p2"])) * 0.65
        + (sign_code - 3) * 0.08
    )

    return {
        "p1_lon": phase["p1"],
        "p2_lon": phase["p2"],
        "p3_lon": phase["p3"],
        "p4_lon": phase["p4"],
        "d1": d1,
        "d2": d2,
        "illumination": illumination,
        "physical": physical,
        "tidal": tidal,
        "angular_code": angular_code,
        "sign_code": float(sign_code),
        "controller": controller,
    }


@dataclass
class Agent:
    agent_id: int
    birth_t: int
    base_trait: float
    trait: float
    learning_rate: float
    cultural_belief: float


def birth_signal(celestial: Dict[str, float]) -> float:
    key = (
        f'{round(celestial["p1_lon"], 1)}|'
        f'{round(celestial["p2_lon"], 1)}|'
        f'{int(celestial["sign_code"])}'
    )
    return (stable_unit(key) - 0.5) * 2.0


def run(world: str, agents_n: int, steps: int, seed: int):
    if world not in WORLD_TYPES:
        raise ValueError(f"unknown world: {world}")

    rng = random.Random(seed)
    agents = []
    births = []

    for agent_id in range(agents_n):
        birth_t = rng.randrange(max(1, steps // 4))
        base_trait = rng.gauss(0, 1)
        c_birth = celestial_state(birth_t)
        trait = base_trait

        if world == "S2_NATAL_SEED":
            trait += 0.45 * birth_signal(c_birth)
        elif world == "S7_WEAK_SIGNAL_CULTURAL":
            trait += 0.12 * birth_signal(c_birth)

        belief = max(0.0, min(1.0, rng.random() * 0.25))
        agent = Agent(agent_id, birth_t, base_trait, trait, 0.06, belief)
        agents.append(agent)
        births.append(
            {
                "agent_id": agent_id,
                "birth_t": birth_t,
                "base_trait": base_trait,
                "initial_trait": trait,
                "birth_signal": birth_signal(c_birth),
            }
        )

    states = []
    outcomes = []
    culture = []

    for t in range(steps):
        c = celestial_state(t)
        states.append(
            {
                "t": t,
                **{
                    key: round(value, 8)
                    for key, value in c.items()
                    if key != "controller"
                },
            }
        )
        hidden_state = c["controller"]

        active_agents = 0
        belief_total = 0.0

        for agent in agents:
            if t < agent.birth_t:
                continue

            active_agents += 1
            runtime = 0.0
            learning_rate = agent.learning_rate

            if world == "S1_PHYSICAL":
                runtime = 0.35 * (c["physical"] - 1.1)
            elif world == "S3_RUNTIME":
                runtime = 0.38 * math.sin(
                    math.radians(c["p1_lon"] - c["p3_lon"])
                )
            elif world == "S4_PLASTICITY":
                learning_rate *= 1 + 0.75 * max(
                    -0.8,
                    min(0.8, math.sin(math.radians(c["p2_lon"]))),
                )
            elif world == "S5_COMMON_CAUSE":
                runtime = 0.42 * hidden_state
            elif world == "S7_WEAK_SIGNAL_CULTURAL":
                runtime = 0.08 * hidden_state

            environment = 0.18 * math.sin(2 * math.pi * t / 50.0)
            experience = rng.gauss(0, 1)

            if world == "S4_PLASTICITY":
                agent.trait += learning_rate * 0.04 * experience
            else:
                agent.trait += agent.learning_rate * 0.012 * experience

            cultural = 0.0
            if world in ("S6_CULTURAL_ONLY", "S7_WEAK_SIGNAL_CULTURAL"):
                perceived_hit = int(c["angular_code"] > 0 and agent.trait + environment > 0)
                agent.cultural_belief = max(
                    0.0,
                    min(
                        1.0,
                        agent.cultural_belief + 0.015 * (perceived_hit - 0.35),
                    ),
                )
                cultural = 0.10 * agent.cultural_belief

            belief_total += agent.cultural_belief
            score = (
                agent.trait
                + runtime
                + environment
                + cultural
                + rng.gauss(0, 0.45)
            )
            probability = logistic(score)
            outcome = int(rng.random() < probability)

            outcomes.append(
                {
                    "t": t,
                    "agent_id": agent.agent_id,
                    "outcome": outcome,
                    "probability": round(probability, 8),
                    "trait": round(agent.trait, 8),
                    "environment": round(environment, 8),
                    "belief": round(agent.cultural_belief, 8),
                }
            )

        if world in ("S6_CULTURAL_ONLY", "S7_WEAK_SIGNAL_CULTURAL"):
            culture.append(
                {
                    "t": t,
                    "claim": "special_angles_are_important",
                    "mean_belief": round(
                        belief_total / max(1, active_agents),
                        8,
                    ),
                }
            )

    coupling = {
        "S0_NULL": "none",
        "S1_PHYSICAL": "physical",
        "S2_NATAL_SEED": "birth_seed",
        "S3_RUNTIME": "runtime",
        "S4_PLASTICITY": "learning_rate",
        "S5_COMMON_CAUSE": "hidden_common_cause",
        "S6_CULTURAL_ONLY": "none_with_cultural_pattern_learning",
        "S7_WEAK_SIGNAL_CULTURAL": "weak_birth_and_common_cause_plus_culture",
    }[world]

    truth = {"world": world, "seed": seed, "coupling": coupling}
    return births, states, outcomes, culture, truth


def write_csv(path, rows):
    path = Path(path)
    rows = list(rows)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--world", choices=WORLD_TYPES, default="S0_NULL")
    parser.add_argument("--agents", type=int, default=100)
    parser.add_argument("--steps", type=int, default=180)
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--out", default="simulation-output")
    args = parser.parse_args(argv)

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    births, states, outcomes, culture, truth = run(
        args.world, args.agents, args.steps, args.seed
    )

    manifest = {
        "schema": "ON_THEO_CELESTIAL_CONDITIONING_WORLD_V1",
        "world": args.world,
        "agents": args.agents,
        "steps": args.steps,
        "seed": args.seed,
        "generator": "reference_simulation.py",
        "ground_truth_file": "ground_truth_private.json",
    }

    (out / "world_manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )
    write_csv(out / "agent_births.csv", births)
    write_csv(out / "celestial_state.csv", states)
    write_csv(out / "agent_outcomes.csv", outcomes)
    write_csv(out / "cultural_claims.csv", culture)
    (out / "ground_truth_private.json").write_text(
        json.dumps(truth, indent=2), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
