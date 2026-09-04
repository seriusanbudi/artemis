---
type: decision
status: accepted
created: 2026-09-04
updated: 2026-09-04
tags:
  - artemis
  - decision
  - v1
  - language
  - bootstrap
---

# Bootstrap URL Runs Use English

## Context

The initial seven URL-only (`U`) runs must execute before Artemis can promote an
agent-discovered location and resolve the local market language. Using that
unknown local language would create a circular dependency.

## Decision

The initial seven URL-only discovery runs use the fixed English template:

> What do you know about `{URL}`?

## Consequences

- Bootstrap wording remains stable across businesses and monitoring cycles.
- The seven answers can discover candidate social handles and locations.
- Local-language performance is measured later in the dedicated language layer.
- English bootstrap results must not be presented as local-language visibility.
- Every run records the English template ID and version.

## Related notes

- [[Prompt Test Matrix]]
- [[2026-09-04 Agent-Discovered Social Handle Becomes H|Agent-Discovered Social Handle Becomes H]]
- [[2026-09-04 Agent-Discovered Location Requires Four of Seven|Agent-Discovered Location Requires Four of Seven]]
- [[2026-09-04 V1 Tests Local Language and English|V1 Tests Local Language and English]]
- [[Decision Log]]

