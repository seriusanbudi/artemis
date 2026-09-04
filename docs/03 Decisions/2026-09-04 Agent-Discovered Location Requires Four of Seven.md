---
type: decision
status: accepted
created: 2026-09-04
updated: 2026-09-04
tags:
  - artemis
  - decision
  - v1
  - geography
  - consistency
---

# Agent-Discovered Location Requires Four of Seven

## Context

The submitted page may not expose a city, province, or country. Skipping the
geography layer would hide whether ChatGPT natively associates the URL with a
location, while pre-searching for a location would remove that native-discovery
signal.

## Decision

When a geographic level is not published on the submitted page, Artemis will
extract location candidates from the seven URL-only (`U`) answers.

An exact normalized city, province, or country value becomes eligible for the
geography layer only when it appears in at least four of the seven runs. Each
geographic level is evaluated independently.

```text
location frequency >= 4/7 → promote that geographic level
location frequency < 4/7  → skip that geographic level
```

Page-published values use provenance `page_declared`. Promoted values use
provenance `agent_discovered`.

## Interpretation

A stable location that conflicts with the submitted page or intended business
is reported as geographic entity misattribution. Artemis records possible
contributing identity signals but does not claim a specific SEO/AEO root cause
without evidence.

## Consequences

- The existing seven `U` runs supply social and location discovery without
  adding another prompt set.
- City, province, and country can have different provenance and confidence.
- A missing or unstable level is skipped and reported as not runnable, not
  scored as zero.
- Equivalent names and abbreviations must be normalized before frequency is
  calculated.
- Promoted location values are intentionally fed into later geography prompts
  and labeled as second-stage tests.

## Related notes

- [[Geography and Language Matrix]]
- [[2026-09-04 Agent-Discovered Social Handle Becomes H|Agent-Discovered Social Handle Becomes H]]
- [[2026-09-04 Seven Runs Per Prompt|Seven Runs Per Prompt]]
- [[Decision Log]]

