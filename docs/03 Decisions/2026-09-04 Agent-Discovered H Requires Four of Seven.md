---
type: decision
status: accepted
created: 2026-09-04
updated: 2026-09-04
tags:
  - artemis
  - decision
  - v1
  - social-identity
  - consistency
---

# Agent-Discovered H Requires Four of Seven

## Context

When the submitted page does not publish a social handle, Artemis extracts
candidate platform-and-username pairs from the seven URL-only answers. A
promotion rule is required before a candidate can become `H` in later tests.

## Decision

An agent-discovered candidate becomes `H` only when the exact normalized
platform-and-username pair appears in at least four of the seven `U` runs.

```text
candidate frequency >= 4/7 → promote to H
candidate frequency < 4/7  → do not promote
```

If no candidate reaches the threshold, Artemis reports social identity as
unstable and skips `H`, `N+H`, `U+H`, and `N+U+H` for that monitoring cycle.

## Consequences

- Promotion requires a simple majority rather than a plurality.
- Equivalent URL and username formats must be normalized before counting.
- Ties above the threshold are reported as ambiguous and are not automatically
  resolved.
- Skipped combinations are reported as not runnable, not scored as zero.
- All observed candidates and their frequencies remain visible in the report.

## Related notes

- [[2026-09-04 Agent-Discovered Social Handle Becomes H|Agent-Discovered Social Handle Becomes H]]
- [[Identity Signal Combination Matrix]]
- [[2026-09-04 Seven Runs Per Prompt|Seven Runs Per Prompt]]
- [[Decision Log]]

