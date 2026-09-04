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

# Geography and Language Layers Use the URL Anchor

## Context

The layered test design requires one fixed identity signal while geographic or
language context changes. A business name can be ambiguous, while the exact
submitted URL deterministically identifies the web resource under test.

Name-only recognition is already measured separately in the identity layer.

## Decision

The geography and language layers will use the exact submitted URL (`U`) as
their fixed identity anchor.

```text
Geography layer: U × geographic context
Language layer:  U × prompt language
```

## Rationale

- The URL minimizes accidental resolution to a different business with a
  similar name.
- It isolates the effect of geography or language instead of mixing that effect
  with name ambiguity.
- It directly tests what ChatGPT can understand from the business's supplied
  landing page under different contexts.
- It does not duplicate the name-only discoverability question already covered
  by the identity matrix.

## Boundary

A URL is a unique experimental anchor for a web resource, but it does not by
itself prove legal ownership, business identity, or factual correctness. Those
limitations remain visible in the report.

ChatGPT may autonomously follow links or search after receiving the URL, but the
prompt must not instruct it to do so. See
[[2026-09-04 V1 Starts From the Supplied URL Only]].

## Related notes

- [[Geography and Language Matrix]]
- [[Identity Signal Combination Matrix]]
- [[Prompt Test Matrix]]
- [[Decision Log]]

