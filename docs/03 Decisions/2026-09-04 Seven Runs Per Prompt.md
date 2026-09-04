---
type: decision
status: accepted
created: 2026-09-04
updated: 2026-09-04
tags:
  - artemis
  - decision
  - v1
  - consistency
---

# Seven Runs Per Prompt

## Context

A single generative response cannot show whether an answer is stable. Artemis
needs repeated independent observations for every unique prompt.

## Decision

Every unique prompt will be executed exactly seven times. Each execution uses
the isolation policy in [[2026-09-04 Fresh Incognito Session Per Prompt|Fresh Incognito Session Per Prompt]]:

```text
Prompt 1
→ Run 1 in new Incognito session
→ Run 2 in new Incognito session
→ Run 3 in new Incognito session
→ Run 4 in new Incognito session
→ Run 5 in new Incognito session
→ Run 6 in new Incognito session
→ Run 7 in new Incognito session
```

Each run contains one prompt and one captured answer.

Known prompts execute once per round across seven rounds. Prompts that depend on
agent-discovered values begin a second round-robin stage after the discovery
threshold is evaluated. See [[2026-09-04 Seven Runs Use Round-Robin Execution]].

## Consistency measurement

Across the seven answers, Artemis should compare:

- Whether the business is recognized
- Whether the same business entity is resolved
- Facts stated about the business
- Products and services mentioned
- Contact and location details
- Source and citation selection
- Answer confidence and qualifying language
- Recommendation outcome when applicable

The report should expose the seven-run distribution, not only label the prompt
as consistent or inconsistent.

## Consequences

- Total browser executions equal the number of unique prompts multiplied by
  seven.
- Runtime and failure handling become important product constraints.
- A failed browser execution is recorded separately and does not automatically
  count as a negative visibility answer.
- Re-running a failed execution must create a new Incognito session and retain
  an audit trail of both attempts.

## Related notes

- [[Prompt Test Matrix]]
- [[Scoring Model]]
- [[2026-09-04 Fresh Incognito Session Per Prompt|Fresh Incognito Session Per Prompt]]
- [[Decision Log]]
