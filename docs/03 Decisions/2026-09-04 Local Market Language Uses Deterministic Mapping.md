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
  - geography
---

# Local Market Language Uses Deterministic Mapping

## Context

The local market language could be inferred from the page, copied from
ChatGPT's response language, supplied manually, or derived from the accepted
location. Page and response language can vary between runs and would make the
language layer difficult to reproduce.

## Decision

Artemis will derive the local market language (`LL`) from a deterministic
location-to-language mapping using the accepted page-declared or
agent-discovered geographic values.

The same accepted location must resolve to the same `LL` value across
monitoring cycles unless the mapping dataset itself is versioned and updated.

## Consequences

- Location provenance and language-mapping version must be recorded.
- Rendered page language and ChatGPT response language remain observations, not
  inputs to the `LL` selection rule.
- The mapping must define behavior for multilingual countries and regions.
- If no geographic value reaches the required confidence, `LL` cannot be
  silently guessed.
- English is deduplicated when the mapping resolves `LL` to English.

## Related notes

- [[Geography and Language Matrix]]
- [[2026-09-04 Agent-Discovered Location Requires Four of Seven|Agent-Discovered Location Requires Four of Seven]]
- [[2026-09-04 V1 Tests Local Language and English|V1 Tests Local Language and English]]
- [[Decision Log]]

