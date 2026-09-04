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

# V1 Is Business-Type Agnostic

## Context

Artemis could be optimized for a specific initial customer segment, such as
local service businesses, SaaS companies, multi-location brands, or agencies.
That framing would make the workflow and scoring more specific, but it would
also move the product away from its primary purpose.

## Decision

Artemis will be a general-purpose **agent glasses** tool. Its core function is
to let any business observe how an agent discovers, identifies, understands,
and describes it.

V1 will not be designed around a specific industry, business model, or customer
segment.

## Consequences

- The core business profile and scoring model must support different business
  types without assuming a physical location, storefront, or online-only model.
- Location, Maps, products, services, and transactional data are optional
  capabilities selected when relevant to the target business.
- Business-specific test plans are generated from the discovered and verified
  profile rather than from a fixed vertical template.
- Vertical-specific scoring and recommendations may be added later without
  changing the core observation model.

## Related notes

- [[Agent Visibility Audit]]
- [[Prompt Test Matrix]]
- [[Decision Log]]

