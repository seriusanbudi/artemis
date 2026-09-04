---
type: experiment
status: complete
created: 2026-09-04
updated: 2026-09-04
tags:
  - artemis
  - experiment
  - agent-glasses
  - production-run
target_url: https://www.arsentdental.com/
accepted_sessions: 77
---

# Arsent Dental Full Agent Glasses Audit

## Outcome

The complete v1 matrix passed its production integrity audit with 77/77
accepted unique sessions and zero validation errors.

The central finding is a split identity state:

- URL-bearing prompts resolved the target 56/56 times.
- Name-only prompts resolved it 0/7 times.
- Instagram-handle-only prompts resolved it 0/7 times.
- Name plus handle was unstable and produced one mixed identity with a
  conflicting phone number and street.

The site itself provides highly stable dentist, SIP, service, price, and
location information once the exact URL anchors the answer.

## Reports and artifacts

- [Full audit report](runs/2026-09-04-arsent-dental-v3/report.md)
- [Protocol audit](runs/2026-09-04-arsent-dental-v3/audit.json)
- [Per-prompt analysis](runs/2026-09-04-arsent-dental-v3/analysis.json)
- [Execution plan](runs/2026-09-04-arsent-dental-v3/plan.json)
- [Raw append-only ledger](runs/2026-09-04-arsent-dental-v3/ledger.jsonl)

The incomplete v1 and v2 engineering runs are preserved in sibling run folders
with their own failing audit records. See the production report's engineering
run history for details.

## Related notes

- [[2026-09-04 Arsent Dental Incognito Feasibility]]
- [[Experiment Log]]
- [[Prompt Test Matrix]]
- [[Scoring Model]]
- [[2026-09-04 Identical Prompts Execute Once]]
