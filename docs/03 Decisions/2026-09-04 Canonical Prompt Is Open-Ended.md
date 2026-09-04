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
  - measurement-integrity
---

# Canonical Prompt Is Open-Ended

## Context

A structured prompt could explicitly request the business name, type, products,
services, location, contacts, and social accounts. That would improve response
coverage, but it would steer ChatGPT toward those fields rather than reveal what
it naturally chooses to say about the business.

## Decision

V1 uses a minimally steering, open-ended canonical question equivalent to:

> What do you know about `{identity signals}`?

The prompt must not:

- Enumerate desired business attributes
- Request a particular output format
- Ask for citations or sources
- Tell ChatGPT to browse, search, crawl, or follow links
- Suggest an expected answer or business category
- Ask a follow-up question

## Synthetic prompt generation

Synthetic prompts are deterministic substitutions into versioned templates, not
new prompts freely generated during every monitoring cycle.

Examples:

- `N`: What do you know about Example Company?
- `U`: What do you know about https://example.com?
- `H`: What do you know about @example on Instagram?
- `N+U`: What do you know about Example Company (https://example.com)?

Geographic phrasing and language-specific templates preserve the same open-ended
intent.

## Evaluation

After the first answer is captured, Artemis extracts and compares whatever
ChatGPT volunteered, including:

- Business identity and type
- Products and services
- Location
- Contact information
- Social accounts
- Other claims
- Citations and autonomously visited sources, when present

Missing fields are meaningful volunteered-coverage findings; Artemis does not
ask ChatGPT to fill them in.

## Consequences

- The benchmark measures ChatGPT's natural representation rather than prompted
  field retrieval.
- One canonical semantic task is reused across all matrix cells.
- Attribute coverage may be lower, but that absence is part of the result.
- Source behavior is observed without being induced by a citation request.
- Future structured retrieval tests, if added, must be reported separately.

## Related notes

- [[Prompt Test Matrix]]
- [[Scoring Model]]
- [[2026-09-04 Prompts Use Versioned Language Templates|Prompts Use Versioned Language Templates]]
- [[Decision Log]]

