---
type: product-concept
status: draft
created: 2026-09-04
updated: 2026-09-04
tags:
  - artemis
  - product
  - agent-visibility
aliases:
  - AEO audit
  - AI discoverability audit
  - Agent share of voice
  - Agent glasses
---

# Agent Visibility Audit

## Background

As AI agents increasingly search for, compare, recommend, and eventually
transact with businesses on behalf of people, a company's effective audience
is no longer limited to human visitors. Agents are becoming an intermediary—or
gatekeeper—between customer intent and businesses.

This creates a new business question:

> When an agent is asked to find, understand, compare, or recommend this
> business, what does it know, how accurate is that knowledge, which sources
> shape its answer, and when does it choose a competitor instead?

Artemis would answer that question by auditing how a business appears from an
agent's point of view.

The product is best understood as **agent glasses**: a general-purpose
instrument that lets any business inspect the public identity an agent can
observe. It is not designed around a particular industry or customer segment.

The concept overlaps with [[Glossary#Answer Engine Optimization (AEO)|AEO]] and
[[Glossary#Generative Engine Optimization (GEO)|GEO]], but its initial function
is broader than optimization. It combines business-entity discovery, local
visibility, source attribution, competitive benchmarking, and agent-response
testing.

## Core product promise

A user provides only their website URL. Artemis discovers the business's public
identity, asks AI agents a controlled set of questions, and reports:

- Whether agents can identify the business
- What agents believe the business does
- Whether important facts are correct and complete
- Where the agents obtained those facts
- In which locations and languages the business is visible
- Whether it appears in unbranded recommendations
- Which competitors appear instead
- Which digital channels contribute to its visibility
- What the business can improve

The product should move beyond the basic question, "Does ChatGPT know my
business?" Its most valuable question is:

> Under which customer intents will an agent select this business, when will it
> select a competitor, and what evidence causes that decision?

## Product principles

### Measure behavior, not an unknowable model state

Artemis can observe agent outputs and their cited evidence. It cannot reliably
claim to know what a proprietary model has memorized or how an internal ranking
system works.

### Separate recognition from recommendation

An agent may know that a business exists without recommending it. Recognition,
factual understanding, discoverability, and recommendation visibility must be
measured separately.

### Use official website claims as the V1 reference

V1 automatically extracts its reference profile from the official website. The
profile represents the business's own published claims, not independently
verified real-world truth. See
[[2026-09-04 Website Is the V1 Reference Profile]].

### Explain every score

An overall number may be commercially useful, but it must remain explainable
through component scores, observations, source evidence, and uncertainty.

### Preserve historical context

Agent behavior, source indexes, and business information change. Every result
must be timestamped so users can distinguish improvement from test variability.

## Initial product scope options

> [!success] V1 decision
> V1 will provide continuous monitoring for one target business. Competitor
> discovery and monitoring are deferred. See
> [[2026-09-04 V1 Monitors One Target Business]].

> [!success] Observation environment
> V1 will observe logged-out ChatGPT through a fresh browser session. The
> workflow is intended to become a reusable Codex skill. See
> [[2026-09-04 V1 Observes Logged-Out ChatGPT]].

### One-time diagnostic report

Audit one business and produce a snapshot of its current agent visibility,
alignment with the official website, and cited sources.

### Diagnostic plus recommendations

Add a prioritized action plan covering website content, business listings,
identity consistency, source gaps, and content opportunities.

### Continuous monitoring

Repeat the benchmark on a schedule and report visibility changes, new factual
errors, and source changes for the target business.

## Open product decisions

- Which countries and languages should be supported first?
- Which findings should affect the overall score, and how should uncertainty be
  represented?

## Related notes

- [[Product Workflow]]
- [[Prompt Test Matrix]]
- [[Scoring Model]]
- [[Source Attribution]]
- [[Risks and Constraints]]
- [[Decision Log]]
- [[2026-09-04 V1 Is Business-Type Agnostic]]
