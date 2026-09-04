#!/usr/bin/env python3
"""Validate an Agent Glasses JSONL ledger against its execution plan."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path


REQUIRED_TRUE = (
    "logged_out_verified",
    "incognito_verified",
    "single_turn_verified",
    "generation_complete",
    "window_closed",
)


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def audit(plan: dict, ledger: list[dict]) -> dict:
    planned = {row["session_id"]: row for row in plan["sessions"]}
    attempts: dict[str, list[dict]] = defaultdict(list)
    errors: list[dict] = []

    for row_number, item in enumerate(ledger, start=1):
        session_id = item.get("session_id")
        attempts[session_id].append(item)
        if session_id not in planned:
            errors.append({"type": "unknown_session", "row": row_number, "session_id": session_id})

    accepted: dict[str, dict] = {}
    for session_id, rows in attempts.items():
        winners = [row for row in rows if row.get("accepted") is True]
        if len(winners) > 1:
            errors.append({"type": "multiple_accepted_attempts", "session_id": session_id})
        elif len(winners) == 1:
            accepted[session_id] = winners[0]

    for session_id, planned_row in planned.items():
        item = accepted.get(session_id)
        if item is None:
            errors.append({"type": "missing_accepted_session", "session_id": session_id})
            continue
        if item.get("prompt") != planned_row["prompt"]:
            errors.append({"type": "prompt_mismatch", "session_id": session_id})
        if not isinstance(item.get("answer"), str) or not item["answer"].strip():
            errors.append({"type": "missing_answer", "session_id": session_id})
        for field in REQUIRED_TRUE:
            if item.get(field) is not True:
                errors.append({"type": f"control_failed:{field}", "session_id": session_id})

    accepted_in_ledger_order = [row for row in ledger if row.get("accepted") is True]
    actual_orders = [planned.get(row.get("session_id"), {}).get("execution_order") for row in accepted_in_ledger_order]
    if actual_orders != sorted(value for value in actual_orders if value is not None):
        errors.append({"type": "accepted_sessions_out_of_order"})

    prompt_counts = Counter(planned[sid]["prompt_id"] for sid in accepted if sid in planned)
    for prompt in plan["prompts"]:
        if prompt_counts[prompt["prompt_id"]] != plan["repeats"]:
            errors.append(
                {
                    "type": "repeat_count_mismatch",
                    "prompt_id": prompt["prompt_id"],
                    "expected": plan["repeats"],
                    "actual": prompt_counts[prompt["prompt_id"]],
                }
            )

    return {
        "audit_id": plan["audit_id"],
        "status": "pass" if not errors else "fail",
        "planned_sessions": len(planned),
        "accepted_sessions": len(accepted),
        "ledger_attempts": len(ledger),
        "failed_attempts": sum(1 for row in ledger if row.get("accepted") is not True),
        "errors": errors,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("plan", type=Path)
    parser.add_argument("ledger", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    plan = json.loads(args.plan.read_text())
    result = audit(plan, load_jsonl(args.ledger))
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(f'{result["status"].upper()}: {result["accepted_sessions"]}/{result["planned_sessions"]} sessions accepted')
    if result["errors"]:
        print(f'{len(result["errors"])} validation error(s)')


if __name__ == "__main__":
    main()
