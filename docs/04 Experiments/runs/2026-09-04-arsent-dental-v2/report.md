---
type: experiment-run
status: failed
created: 2026-09-04
updated: 2026-09-04
audit_id: 2026-09-04-arsent-dental-v2
---

# Arsent Dental v2 engineering run

This run is intentionally preserved as failed.

- Planned sessions: 77
- Accepted sessions: 33
- Recorded attempts: 43
- Failed attempts: 10
- Causes: one slow generation, transient composer-load failures, two clipboard
  timeouts, one kernel reset after capture, and a read-only Computer Use proxy
  regression that exhausted session S0034's retries.

The captured response interrupted by the kernel reset was retained as a failed
attempt before a fresh retry. No session with exhausted retries was continued
outside the protocol. See `audit.json` and `ledger.jsonl` in this directory.
The complete production run is v3.
