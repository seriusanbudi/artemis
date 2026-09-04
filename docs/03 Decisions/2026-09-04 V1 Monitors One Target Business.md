---
type: decision
status: accepted
created: 2026-09-04
updated: 2026-09-04
tags:
  - artemis
  - decision
  - v1
---

# V1 Monitors One Target Business

## Context

Artemis could begin as a one-time diagnostic, a diagnostic with recommendations,
or a continuous-monitoring product. Monitoring could also include competitors,
but that would expand entity discovery, prompt generation, scoring, and report
scope.

## Decision

V1 will continuously monitor the visibility of one target business over time.
Competitor discovery, scoring, comparison, and monitoring are out of scope for
V1.

## Consequences

- The core value is detecting changes in how agents recognize, describe, cite,
  and recommend the target business.
- The system must store timestamped test runs and comparable historical results.
- Reports should emphasize trends, regressions, new factual errors, source
  changes, and visibility changes.
- Comparison-oriented prompts and agent share-of-voice metrics are deferred.
- Competitor monitoring may be reconsidered after the single-business benchmark
  is stable.

## Related notes

- [[Agent Visibility Audit]]
- [[Product Workflow]]
- [[Decision Log]]

