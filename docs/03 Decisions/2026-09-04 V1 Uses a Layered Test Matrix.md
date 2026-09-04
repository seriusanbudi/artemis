---
type: decision
status: accepted
created: 2026-09-04
updated: 2026-09-04
tags:
  - artemis
  - decision
  - v1
  - test-matrix
---

# V1 Uses a Layered Test Matrix

## Context

A full Cartesian product of seven identity combinations, four geographic
contexts, two V1 language contexts, and seven repeated runs could require 392
fresh Incognito sessions. It would also change several variables at once,
making individual effects harder to explain.

## Decision

V1 will use three controlled layers:

1. **Identity layer:** test all seven `N`, `U`, and `H` combinations
2. **Geography layer:** hold identity and language constant while varying
   no-location, city, province, and country context
3. **Language layer:** hold identity and geography constant while varying
   website, local-market, and English language

Only one primary dimension changes within each layer.

## Estimated run volume

Before deduplication or unavailable signals:

```text
Identity:  7 prompts × 7 runs = 49 sessions
Geography: 4 prompts × 7 runs = 28 sessions
Language:  2 prompts × 7 runs = 14 sessions
Total:                         91 sessions
```

The subsequent V1 language decision reduced this layer to local-market language
and English, making the current maximum 91 sessions. If the local language is
English, duplicate language prompts run only once.

## Consequences

- Identity-signal lift, geographic lift, and language portability remain
  separately interpretable.
- V1 does not reveal every possible interaction between identity, geography,
  and language.
- The fixed identity signal used to anchor the geography and language layers
  must be chosen separately.
- More complex cross-dimensional tests may be added later as targeted
  experiments rather than as part of the default monitoring cycle.

## Related notes

- [[Identity Signal Combination Matrix]]
- [[Geography and Language Matrix]]
- [[Prompt Test Matrix]]
- [[Decision Log]]
