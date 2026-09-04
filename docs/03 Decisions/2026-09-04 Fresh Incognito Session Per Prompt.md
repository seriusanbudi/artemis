---
type: decision
status: accepted
created: 2026-09-04
updated: 2026-09-04
tags:
  - artemis
  - decision
  - v1
  - browser-isolation
---

# Fresh Incognito Session Per Prompt

## Context

Starting every prompt in a new ChatGPT conversation prevents conversational
steering, but prompts can still share cookies, local storage, and other browser
state when they run inside the same Incognito session.

## Decision

Every prompt will run in a completely new Incognito Chrome session:

```text
Close prior Incognito session
→ open new Incognito session
→ navigate to logged-out ChatGPT.com
→ submit one prompt
→ capture one answer and its evidence
→ close the session
```

No Incognito session is reused across prompts, prompt categories, or repeated
runs.

## Consequences

- Prompt results do not share browser-session state.
- The run will be slower and use more browser operations.
- Session startup, consent dialogs, product onboarding, CAPTCHAs, and failures
  must be handled consistently.
- Network-level, IP-location, language, time, and product-rollout signals can
  still affect results and must be recorded where observable.
- The feasibility experiment must validate reliable session creation and
  teardown, not only prompt submission.

## Related notes

- [[2026-09-04 V1 Uses Single-Turn Prompts]]
- [[2026-09-04 V1 Observes Logged-Out ChatGPT]]
- [[Prompt Test Matrix]]
- [[Decision Log]]

