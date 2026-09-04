---
type: decision
status: accepted
created: 2026-09-04
updated: 2026-09-04
tags:
  - artemis
  - decision
  - v1
  - reference-data
---

# Website Is the V1 Reference Profile

## Context

Artemis needs a reference profile to evaluate whether ChatGPT's facts about a
business match the business's official information. The profile could be
automatically extracted, verified by the user, or supplied manually.

## Decision

V1 will automatically extract the reference business profile from the exact
page supplied by the user. It will not deliberately crawl other website paths.
The user does not need to confirm or manually enter business facts.

## Measurement boundary

The extracted profile represents **official website claims**, not independently
verified real-world truth. Therefore, V1 measures whether the agent's answer is
aligned with the business's own published information.

If the website is incomplete or outdated, Artemis should report missing or
ambiguous reference data rather than silently treating inferred facts as
confirmed truth.

## Consequences

- Onboarding remains URL-only.
- Landing-page information and extraction quality directly affect evaluation
  quality.
- Every field must retain the supplied source URL and supporting page text.
- Facts found only on Maps, social profiles, directories, or media cannot
  override the official website reference profile.
- The report must distinguish "differs from the official website" from
  "factually incorrect."

## Related notes

- [[Product Workflow]]
- [[Scoring Model]]
- [[Source Attribution]]
- [[Decision Log]]
