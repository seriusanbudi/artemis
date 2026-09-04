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
---

# V1 Tests Local Language and English

## Context

The language layer could test the dynamically rendered website language, the
local market language, English, or no language variation. The rendered website
language may not be stable enough to serve as a controlled prompt context.

## Decision

V1 will test two language contexts:

- `LL`: local market language
- `LE`: English

If both contexts resolve to English, Artemis executes one language prompt set
and retains both semantic labels in the report.

## Consequences

- Language portability compares local-market representation with English
  representation.
- The language rendered by the submitted page is recorded as metadata rather
  than automatically becoming a third test language.
- Additional languages may be added later as optional monitoring dimensions.
- The maximum default layered cycle becomes 91 sessions:

```text
Identity:  7 prompts × 7 runs = 49 sessions
Geography: 4 prompts × 7 runs = 28 sessions
Language:  2 prompts × 7 runs = 14 sessions
Total:                         91 sessions
```

## Related notes

- [[Geography and Language Matrix]]
- [[Prompt Test Matrix]]
- [[2026-09-04 V1 Uses a Layered Test Matrix|V1 Uses a Layered Test Matrix]]
- [[Decision Log]]

