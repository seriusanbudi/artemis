#!/usr/bin/env python3
"""Build a deduplicated, seven-round Agent Glasses execution plan."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def render(template: str, **values: str) -> str:
    return template.format(**values)


def add_prompt(prompts: dict[str, dict], prompt: str, label: str, **metadata: object) -> None:
    record = prompts.setdefault(prompt, {"prompt": prompt, "labels": [], **metadata})
    if label not in record["labels"]:
        record["labels"].append(label)


def build(config: dict) -> dict:
    name = config["name"]
    url = config["target_url"]
    handle = config.get("social_handle")
    local = config["local_language"]
    templates = config["templates"]
    en_base = templates["en_base"]
    local_base = templates["local_base"]
    local_location = templates["local_location"]

    identities: list[tuple[str, str, list[str]]] = [("N", name, ["N"]), ("U", url, ["U"])]
    if handle:
        social = f'{handle["value"]} on {handle["platform"]}'
        identities.extend(
            [
                ("H", social, ["H"]),
                ("N+U", f"{name} ({url})", ["N", "U"]),
                ("N+H", f"{name} ({social})", ["N", "H"]),
                ("U+H", f"{url} and {social}", ["U", "H"]),
                ("N+U+H", f"{name} ({url}, {social})", ["N", "U", "H"]),
            ]
        )
    else:
        identities.append(("N+U", f"{name} ({url})", ["N", "U"]))

    prompts: dict[str, dict] = {}
    for label, identity, signals in identities:
        add_prompt(
            prompts,
            render(en_base, identity=identity),
            f"identity:{label}",
            language="en",
            identity_signals=signals,
            location_level=None,
        )

    add_prompt(
        prompts,
        render(local_base, identity=url),
        "geography:G0",
        language=local["code"],
        identity_signals=["U"],
        location_level="none",
    )
    add_prompt(
        prompts,
        render(en_base, identity=url),
        "language:en",
        language="en",
        identity_signals=["U"],
        location_level="none",
    )
    add_prompt(
        prompts,
        render(local_base, identity=url),
        f'language:{local["code"]}',
        language=local["code"],
        identity_signals=["U"],
        location_level="none",
    )

    for level in ("city", "province", "country"):
        location = config.get(level)
        if location:
            add_prompt(
                prompts,
                render(local_location, url=url, location=location),
                f"geography:{level}",
                language=local["code"],
                identity_signals=["U"],
                location_level=level,
            )

    unique = list(prompts.values())
    for number, record in enumerate(unique, start=1):
        record["prompt_id"] = f"P{number:02d}"

    sessions = []
    order = 0
    for round_number in range(1, 8):
        for record in unique:
            order += 1
            sessions.append(
                {
                    "session_id": f"S{order:04d}",
                    "round": round_number,
                    "execution_order": order,
                    **record,
                }
            )

    conceptual_labels = sum(len(item["labels"]) for item in unique)
    return {
        "audit_id": config["audit_id"],
        "protocol_version": config.get("protocol_version", "agent-glasses-v1"),
        "target_url": url,
        "repeats": 7,
        "unique_prompts": len(unique),
        "conceptual_matrix_cells": conceptual_labels,
        "planned_sessions": len(sessions),
        "prompts": unique,
        "sessions": sessions,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("config", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    config = json.loads(args.config.read_text())
    plan = build(config)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n")
    print(
        f'Built {plan["unique_prompts"]} unique prompts, '
        f'{plan["conceptual_matrix_cells"]} conceptual cells, '
        f'and {plan["planned_sessions"]} sessions.'
    )


if __name__ == "__main__":
    main()
