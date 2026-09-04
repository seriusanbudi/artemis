---
type: decision
status: accepted
created: 2026-09-04
updated: 2026-09-04
tags:
  - artemis
  - decision
  - v1
  - identity-resolution
---

# Core Identity Matrix Uses Name, URL, and Handle

## Context

Artemis needs a fixed set of identity signals that is broad enough to measure
signal lift but small enough to remain interpretable and runnable seven times
per prompt.

## Decision

The V1 core identity matrix uses three signals:

- `N`: official business name extracted from the submitted page
- `U`: exact URL supplied by the user
- `H`: one primary social handle exposed on the submitted page or consistently
  discovered in the seven URL-only runs

The matrix contains all seven non-empty combinations:

```text
N
U
H
N+U
N+H
U+H
N+U+H
```

Each combination runs seven times in independent Incognito sessions, producing
49 browser executions for the base identity matrix.

## Consequences

- Results remain comparable across businesses that expose all three signals.
- The matrix can calculate the marginal lift produced by each signal.
- Phone numbers, addresses, taglines, product names, and other identifiers are
  excluded from the fixed V1 identity matrix.
- If no social handle is visible on the submitted page, the seven `U` runs act
  as a native social-discovery phase. See
  [[2026-09-04 Agent-Discovered Social Handle Becomes H]].

## Related notes

- [[Identity Signal Combination Matrix]]
- [[Prompt Test Matrix]]
- [[2026-09-04 Seven Runs Per Prompt|Seven Runs Per Prompt]]
- [[Decision Log]]
