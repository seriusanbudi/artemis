---
type: product-design
status: draft
created: 2026-09-04
updated: 2026-09-04
tags:
  - artemis
  - risks
  - constraints
---

# Risks and Constraints

## Measurement reliability

- Generative variability makes single-run scores unreliable.
- Different agents use different retrieval systems and sources.
- Results can change with location, language, time, model, and index state.
- Prompt wording can unintentionally favor or disadvantage a business.
- Citations may vary between runs or fail to expose every retrieval source.
- Creating a new Incognito Chrome session for every prompt increases runtime
  and the likelihood of browser startup, consent-dialog, or CAPTCHA failures.

## Entity and data quality

- A website may contain incorrect or outdated information.
- Public sources may contradict each other.
- Entity names may collide with unrelated businesses.
- Copied third-party pages can create false corroboration.
- Digital evidence cannot prove offline popularity.

## Platform constraints

- Consumer-agent interfaces may be technically brittle or inappropriate to
  automate at scale.
- Logged-out or incognito tests are not fully neutral.
- Proprietary ranking and model behavior cannot be directly inspected.
- A reproducible API benchmark may not perfectly represent the consumer UI.

## Scoring risk

A single score can imply false precision. Reports must expose component scores,
sample sizes, run variance, source evidence, and known test conditions.

## Privacy

Collect only public business contact information by default. Do not infer,
enrich, or expose personal contact data without a clear lawful purpose and
appropriate consent.

## Related notes

- [[Agent Visibility Audit]]
- [[Product Workflow]]
- [[Prompt Test Matrix]]
- [[Scoring Model]]
