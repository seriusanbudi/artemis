#!/usr/bin/env python3
"""Create deterministic coverage summaries from accepted Agent Glasses answers."""

from __future__ import annotations

import argparse
import json
import re
import statistics
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def percentile(values: list[float], fraction: float) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    index = round((len(ordered) - 1) * fraction)
    return round(ordered[index], 2)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("plan", type=Path)
    parser.add_argument("ledger", type=Path)
    parser.add_argument("signals", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    plan = json.loads(args.plan.read_text())
    spec = json.loads(args.signals.read_text())
    ledger = load_jsonl(args.ledger)
    accepted = {row["session_id"]: row for row in ledger if row.get("accepted") is True}
    patterns = {
        name: [re.compile(pattern, re.IGNORECASE) for pattern in values]
        for name, values in spec["signals"].items()
    }

    prompt_rows: dict[str, list[dict]] = defaultdict(list)
    citation_labels: Counter[str] = Counter()
    durations: list[float] = []

    for planned in plan["sessions"]:
        row = accepted.get(planned["session_id"])
        if not row:
            continue
        answer = row["answer"]
        flags = {name: any(pattern.search(answer) for pattern in compiled) for name, compiled in patterns.items()}
        flags["correct_entity_heuristic"] = flags.get("business_name", False) and any(
            flags.get(name, False) for name in spec["entity_anchor_signals"]
        )
        flags["actionable_heuristic"] = any(
            flags.get(name, False) for name in spec["actionability_signals"]
        )
        enriched = {**row, "flags": flags, "prompt_id": planned["prompt_id"], "labels": planned["labels"]}
        prompt_rows[planned["prompt_id"]].append(enriched)
        citation_labels.update(row.get("citation_labels", []))
        try:
            start = datetime.fromisoformat(row["started_at"])
            end = datetime.fromisoformat(row["completed_at"])
            durations.append((end - start).total_seconds())
        except (TypeError, ValueError):
            pass

    prompt_summaries = []
    label_summaries: dict[str, dict] = {}
    for prompt in plan["prompts"]:
        rows = prompt_rows[prompt["prompt_id"]]
        counts = {
            signal: sum(row["flags"].get(signal, False) for row in rows)
            for signal in [*patterns, "correct_entity_heuristic", "actionable_heuristic"]
        }
        summary = {
            "prompt_id": prompt["prompt_id"],
            "labels": prompt["labels"],
            "prompt": prompt["prompt"],
            "runs": len(rows),
            "answer_chars": {
                "min": min((len(row["answer"]) for row in rows), default=0),
                "median": statistics.median((len(row["answer"]) for row in rows)) if rows else 0,
                "max": max((len(row["answer"]) for row in rows), default=0),
            },
            "autonomous_browsing": sum(row["autonomous_browsing"] == "observed" for row in rows),
            "signal_counts": counts,
        }
        prompt_summaries.append(summary)
        for label in prompt["labels"]:
            label_summaries[label] = {
                "prompt_id": prompt["prompt_id"],
                "runs": len(rows),
                "autonomous_browsing": summary["autonomous_browsing"],
                "signal_counts": counts,
            }

    failed = [row for row in ledger if row.get("accepted") is not True]
    result = {
        "audit_id": plan["audit_id"],
        "accepted_sessions": len(accepted),
        "ledger_attempts": len(ledger),
        "failed_attempts": len(failed),
        "failed_attempt_errors": dict(Counter(row.get("error") or "unknown" for row in failed)),
        "autonomous_browsing": sum(row.get("autonomous_browsing") == "observed" for row in accepted.values()),
        "latency_seconds": {
            "median": round(statistics.median(durations), 2) if durations else None,
            "p95": percentile(durations, 0.95),
            "max": round(max(durations), 2) if durations else None,
        },
        "citation_label_frequency": dict(citation_labels.most_common()),
        "prompt_summaries": prompt_summaries,
        "label_summaries": label_summaries,
        "method_note": "Signal counts are deterministic regex observations. Correct-entity and actionability fields are declared heuristics and require semantic review.",
    }
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(f'Summarized {len(accepted)} accepted sessions across {len(prompt_summaries)} unique prompts.')


if __name__ == "__main__":
    main()
