from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import reference_simulation as sim


ALLOWED = set(sim.WORLD_TYPES) | {"UNRESOLVED"}


def canonical_json_bytes(value) -> bytes:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def load_json(path):
    return json.loads(
        Path(path).read_text(encoding="utf-8")
    )


def verify_answer_key_commitment(public_index, answer_key):
    expected = public_index["answer_key_commitment_sha256"]
    actual = hashlib.sha256(
        canonical_json_bytes(answer_key)
    ).hexdigest()
    if expected != actual:
        raise ValueError(
            "answer key does not match public commitment"
        )
    return actual


def score(answer_key, submissions):
    truth = {
        row["run_id"]: row["world"]
        for row in answer_key["runs"]
    }

    seen = set()
    rows = []

    for submission in submissions["submissions"]:
        run_id = submission["run_id"]

        if run_id in seen:
            raise ValueError(
                f"duplicate submission for {run_id}"
            )
        seen.add(run_id)

        if run_id not in truth:
            raise ValueError(
                f"unknown run_id: {run_id}"
            )

        predicted = submission["predicted_world"]

        if predicted not in ALLOWED:
            raise ValueError(
                f"invalid predicted_world: {predicted}"
            )

        if submission.get(
            "frozen_before_unblinding"
        ) is not True:
            raise ValueError(
                f"submission not frozen: {run_id}"
            )

        rows.append(
            (truth[run_id], predicted)
        )

    missing = sorted(
        set(truth) - seen
    )
    labels = list(sim.WORLD_TYPES) + [
        "UNRESOLVED"
    ]

    matrix = {
        actual: {
            predicted: 0
            for predicted in labels
        }
        for actual in sim.WORLD_TYPES
    }

    for actual, predicted in rows:
        matrix[actual][predicted] += 1

    exact = sum(
        actual == predicted
        for actual, predicted in rows
    )
    unresolved = sum(
        predicted == "UNRESOLVED"
        for _, predicted in rows
    )

    per_world = {}
    for world in sim.WORLD_TYPES:
        total = sum(
            matrix[world].values()
        )
        per_world[world] = {
            "submitted": total,
            "correct": matrix[world][world],
            "recall": (
                matrix[world][world] / total
                if total
                else None
            ),
        }

    return {
        "schema": "ON_THEO_ASTROLOGY_BLIND_SCORE_V1",
        "answer_key_runs": len(truth),
        "submitted_runs": len(rows),
        "missing_run_ids": missing,
        "exact_correct": exact,
        "unresolved": unresolved,
        "accuracy_on_submitted": (
            exact / len(rows)
            if rows
            else None
        ),
        "coverage": (
            len(rows) / len(truth)
            if truth
            else 1.0
        ),
        "confusion_matrix": matrix,
        "per_world": per_world,
    }


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--answer-key",
        required=True,
    )
    parser.add_argument(
        "--submissions",
        required=True,
    )
    parser.add_argument(
        "--public-index",
    )
    parser.add_argument(
        "--out",
        default="score_report.json",
    )
    args = parser.parse_args(argv)

    answer_key = load_json(
        args.answer_key
    )

    if args.public_index:
        verify_answer_key_commitment(
            load_json(args.public_index),
            answer_key,
        )

    report = score(
        answer_key,
        load_json(args.submissions),
    )

    Path(args.out).write_text(
        json.dumps(
            report,
            indent=2,
            sort_keys=True,
        ),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
