---
type: decision
status: accepted
created: 2026-09-04
updated: 2026-09-04
tags:
  - artemis
  - decision
  - v1
  - execution
  - consistency
---

# Seven Runs Use Round-Robin Execution

## Context

Running the same prompt seven consecutive times concentrates its observations
into a short time window. A transient ChatGPT condition could then affect all
seven answers for that prompt.

## Decision

Artemis will execute known prompts in seven rounds. Every eligible prompt runs
once in each round:

```text
Round 1: every eligible prompt once
Round 2: every eligible prompt once
...
Round 7: every eligible prompt once
```

Each individual execution still receives a new Incognito Chrome session.

## Dependent prompts

Some prompts depend on values discovered in the seven URL-only runs, such as an
agent-discovered social handle or location. The cycle therefore has two stages:

1. Run all immediately available prompts in seven rounds, including `U`.
2. Promote eligible 4/7 discoveries, generate dependent prompts, and run those
   prompts in their own seven rounds.

## Consequences

- Repetitions for one prompt are spread across more of the monitoring period.
- Every run records its round number, execution order, and timestamp.
- Newly eligible second-stage prompts are clearly labeled as dependent tests.
- The runtime is longer than consecutive execution.
- A temporary platform incident is less likely to dominate all observations for
  one prompt.

## Related notes

- [[2026-09-04 Seven Runs Per Prompt|Seven Runs Per Prompt]]
- [[Prompt Test Matrix]]
- [[2026-09-04 Agent-Discovered Social Handle Becomes H|Agent-Discovered Social Handle Becomes H]]
- [[2026-09-04 Agent-Discovered Location Requires Four of Seven|Agent-Discovered Location Requires Four of Seven]]
- [[Decision Log]]

