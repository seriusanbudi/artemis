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
---

# Agent-Discovered Social Handle Becomes H

## Context

The submitted page may not expose a social handle. Skipping social tests would
hide whether ChatGPT can natively associate the website with a social account.
Searching for and supplying an account before the agent test would remove that
native-discovery signal.

## Decision

When no social handle is published on the submitted page, Artemis will use the
seven URL-only (`U`) answers as a discovery phase. It extracts every
platform-and-username pair returned by ChatGPT and selects the most consistently
discovered candidate as `H` for the remaining identity combinations.

```text
Run U seven times
→ extract social-account candidates
→ select the most consistently returned candidate
→ record H provenance as agent_discovered
→ run H, N+H, U+H, and N+U+H tests
```

If the submitted page already publishes a handle, that handle is used and its
provenance is recorded as `page_declared`.

## Interpretation

A consistently returned account that does not match the intended business is
reported as **entity misattribution** or **identity fragmentation**, not merely
discarded as model hallucination.

The finding indicates that observable public identity signals did not lead the
agent to the intended association. Possible causes include inconsistent naming,
weak cross-profile linking, incomplete website identity signals, outdated
profiles, third-party ambiguity, or agent behavior. Artemis should identify
supporting evidence before attributing the failure to a specific cause.

## Consequences

- The `U` runs must complete before combinations containing an agent-discovered
  `H` can run.
- `H` always retains provenance: `page_declared` or `agent_discovered`.
- Later `H` tests measure how strongly the discovered association persists when
  the candidate handle is supplied.
- Feeding `H` back into later prompts is an intentional second-stage test and
  must be labeled separately from native discovery.
- A candidate must appear in at least four of the seven `U` runs before it can
  become `H`. See [[2026-09-04 Agent-Discovered H Requires Four of Seven]].

## Related notes

- [[Identity Signal Combination Matrix]]
- [[2026-09-04 Core Identity Matrix Uses Name URL and Handle|Core Identity Matrix Uses Name URL and Handle]]
- [[2026-09-04 Seven Runs Per Prompt|Seven Runs Per Prompt]]
- [[Decision Log]]
