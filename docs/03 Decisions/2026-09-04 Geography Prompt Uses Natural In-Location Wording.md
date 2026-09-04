---
type: decision
status: accepted
created: 2026-09-04
updated: 2026-09-04
tags:
  - artemis
  - decision
  - v1
  - prompts
  - geography
---

# Geography Prompt Uses Natural In-Location Wording

## Context

Geographic context can be introduced with experimentally explicit wording or a
shorter phrase that resembles a natural user question. The shorter wording is
more ambiguous but less engineered.

## Decision

The V1 geography template will use the natural pattern:

> What do you know about `{URL}` in `{location}`?

Natural local-language versions must preserve this simple meaning rather than
adding assumptions or extra instructions.

## Interpretation boundary

The phrase “in `{location}`” may be interpreted as physical location, service
area, local relevance, or a regional branch. Artemis must therefore label the
result as a **response under supplied location wording**.

It must not claim that the result proves:

- The business operates in that location
- The business is popular at that geographic level
- A person physically browsing from that location would receive the same answer
- The agent interpreted the location phrase in one specific way

## Consequences

- The prompt remains short and similar to natural user behavior.
- City, province, and country tests use the same grammatical pattern.
- Prompt geography remains distinct from actual browser IP geography.
- A more explicit “in the context of” template may be tested later as a new
  version without changing historical V1 results.

## Related notes

- [[2026-09-04 Canonical Prompt Is Open-Ended|Canonical Prompt Is Open-Ended]]
- [[Geography and Language Matrix]]
- [[2026-09-04 Prompts Use Versioned Language Templates|Prompts Use Versioned Language Templates]]
- [[Decision Log]]

