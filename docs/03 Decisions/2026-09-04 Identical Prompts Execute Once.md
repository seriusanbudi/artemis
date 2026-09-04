---
type: decision
status: accepted
created: 2026-09-04
updated: 2026-09-04
tags:
  - decision
  - prompts
  - deduplication
---

# Identical Prompts Execute Once

## Context

The layered identity, geography, and language matrix contains overlapping
cells. Identity `U` is exactly the English language-layer `U+G0` prompt, while
the Indonesian geography `U+G0` prompt is exactly the Indonesian language-layer
prompt.

Executing both copies would add no controlled difference, consume fourteen
extra Incognito sessions per cycle, and risk presenting duplicate responses as
independent evidence.

## Decision

Execute identical prompt text once per repeat and attach every applicable
matrix label to that observation.

For the complete Arsent Dental matrix this changes 91 conceptual observations
into 77 unique browser sessions without removing any conceptual comparison.

## Alternatives considered

### Execute all 91 cells

- Benefit: each conceptual layer has its own physical session count.
- Cost: identical work is repeated and can be double-counted.

### Deduplicate exact prompt text

- Benefit: lower runtime, cleaner statistics, and no duplicate evidence.
- Cost: reporting must preserve multiple labels on one observation.

## Consequences

- The plan generator deduplicates exact prompt text.
- Reports distinguish conceptual observations from unique sessions.
- A wording difference, however small, remains a separate prompt and is not
  deduplicated.

## Evidence

- [Arsent Dental production audit](../04%20Experiments/runs/2026-09-04-arsent-dental-v3/report.md)

## Related notes

- [[Decision Log]]
- [[Prompt Test Matrix]]
- [[2026-09-04 V1 Uses a Layered Test Matrix]]
