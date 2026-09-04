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

# Language Layer Uses No Location Context

## Context

The language layer must hold geography constant while comparing the local
market language with English. Adding city, province, or country context would
change two dimensions at once.

## Decision

The V1 language layer uses no explicit location context (`G0`).

```text
URL + no location + local market language × 7 runs
URL + no location + English               × 7 runs
```

The exact submitted URL remains the identity anchor.

## Consequences

- Differences between the two prompt sets can be attributed primarily to
  language rather than explicit geographic wording.
- The browser's actual IP geography and locale are still recorded as
  environmental context when observable.
- Location-specific language behavior is outside the default V1 matrix and may
  be tested later as a targeted experiment.

## Related notes

- [[Geography and Language Matrix]]
- [[2026-09-04 V1 Tests Local Language and English|V1 Tests Local Language and English]]
- [[2026-09-04 Geography and Language Layers Use the URL Anchor|Geography and Language Layers Use the URL Anchor]]
- [[Decision Log]]

