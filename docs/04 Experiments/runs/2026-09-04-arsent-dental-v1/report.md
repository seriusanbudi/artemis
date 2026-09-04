---
type: experiment-run
status: failed
created: 2026-09-04
updated: 2026-09-04
audit_id: 2026-09-04-arsent-dental-v1
---

# Arsent Dental v1 engineering run

This run is intentionally preserved as failed.

- Planned sessions: 77
- Accepted sessions: 1
- Recorded attempts: 13
- Failed attempts: 12
- Cause: the runner polled the accessibility tree without a real delay and
  exhausted three attempts for sessions S0002–S0005 while ChatGPT was still
  generating.

No failed attempt was promoted to an accepted observation. See `audit.json` and
`ledger.jsonl` in this directory. The complete production run is v3.
