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
  - localization
---

# LL Uses the Mainstream Market Language

## Context

A location-to-language mapping can become overly specific by assigning a
traditional, indigenous, or heritage language that is not the mainstream
language customers use for commercial and digital queries.

## Decision

Artemis will select the most specific **mainstream market language** available:

1. Use a city or province override only when its mainstream commercial and
   digital language materially differs from the country default.
2. Otherwise, use the country-level mainstream market language.
3. Do not select a traditional or heritage language solely because it is
   culturally associated with the location.

For example, Bali should normally resolve to Indonesian rather than Balinese.

## Consequences

- The mapping represents likely customer-query language, not every language
  spoken in the region.
- Every mapping entry should record its geographic scope, language code,
  rationale, and dataset version.
- Regional overrides should remain uncommon and evidence-based.
- Traditional and additional languages may be supported later as optional tests
  rather than as the default `LL` value.
- English remains a separate language-layer context when `LL` is not English.

## Related notes

- [[2026-09-04 Local Market Language Uses Deterministic Mapping|Local Market Language Uses Deterministic Mapping]]
- [[Geography and Language Matrix]]
- [[2026-09-04 V1 Tests Local Language and English|V1 Tests Local Language and English]]
- [[Decision Log]]

