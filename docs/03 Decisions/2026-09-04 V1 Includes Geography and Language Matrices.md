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
  - language
---

# V1 Includes Geography and Language Matrices

## Context

Identity testing alone shows whether ChatGPT can recognize a business from its
name, URL, or social handle. It does not show whether that recognition changes
when the business is framed at city, province, or country level, or when the
question is asked in different languages.

## Decision

V1 will include both geographic-context and language dimensions in addition to
the core identity matrix.

The precise combination strategy remains open because a complete Cartesian
product may require hundreds of fresh Incognito sessions per monitoring cycle.

## Intended outcomes

- Identify whether recognition is strongest at city, province, or country level
- Measure whether location context helps disambiguate the business
- Detect facts that change or disappear at broader geographic levels
- Measure whether the business remains recognizable across languages
- Detect language-specific inconsistencies in identity, facts, and citations

## Measurement language

These results represent **observed geographic reach in ChatGPT answers**, not
proof of operational business scale, market share, or offline popularity.

## Related notes

- [[Geography and Language Matrix]]
- [[Identity Signal Combination Matrix]]
- [[Prompt Test Matrix]]
- [[Decision Log]]

