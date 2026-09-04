---
type: product-design
status: draft
created: 2026-09-04
updated: 2026-09-04
tags:
  - artemis
  - scoring
  - benchmarking
---

# Scoring Model

## Principle

Show diagnostic dimensions before an overall score. The benchmark must remain
explainable through observations, source evidence, and uncertainty.

Only the first answer to an isolated prompt is scored. The evaluator must not
steer, clarify, correct, or regenerate the answer within the same test.

Every prompt score is based on seven independent runs. Consistency is calculated
from the distribution of outcomes across those runs, not from a single answer.

## Proposed dimensions

| Dimension | Question answered |
|---|---|
| Recognition | Can the agent identify the business from its name, URL, or username? |
| First-answer utility | Does the single allowed answer explain the business, or merely ask the user to clarify or continue? |
| Website alignment | Do the name, category, address, contacts, products, and other facts match the official website? |
| Volunteered coverage | Which business attributes does the agent choose to mention without being asked? |
| Local visibility | Does the business appear in relevant geographic searches? |
| Category visibility | Does it appear when the brand is not explicitly named? |
| Recommendation strength | Is it merely mentioned or actively recommended? |
| Source authority | Are answers supported by relevant official and independent sources? |
| Consistency | Are results stable across runs, languages, locations, and agents? |
| Actionability | Can the agent direct a user to call, visit, book, or purchase? |
| Social entity attribution | Does the agent consistently associate the URL with the intended social identity? |
| Cross-surface identity binding | Do the name, URL, and social handle independently converge on the same entity? |

For identity tests, Artemis should also measure **signal lift**: the change in
recognition, field recovery, and consistency when name, URL, or social-handle
clues are added. See [[Identity Signal Combination Matrix]].

Geography and language tests add two derived profiles:

- **Observed geographic reach:** recognition and stability across city,
  province, and country contexts
- **Language portability:** recognition and factual stability across prompt
  languages

See [[Geography and Language Matrix]].

Agent-initiated browsing should be reported as an observed behavior alongside
the answer. It must not be treated as equivalent to information understood from
the supplied landing page.

When the page does not declare a social account, Artemis reports the discovered
account, its seven-run frequency, its evidence, and any identity conflict. It
should call a wrong association entity misattribution rather than automatically
assigning a technical root cause.

An agent-discovered handle is eligible for later identity tests only at a
frequency of at least 4/7. Lower-frequency candidates remain visible but are not
promoted to `H`.

The same rule applies independently to agent-discovered city, province, and
country values. A stable but conflicting location is reported as geographic
entity misattribution.

## Evaluation levels

Each dimension should preserve three layers:

1. **Observation** — what the agent actually returned
2. **Assessment** — how that response compares with official website claims or
   expected test behavior
3. **Score** — a normalized summary suitable for comparison

The score must never replace the first two layers.

Recognition and first-answer utility must remain separate. An agent may select
the correct business while returning only a clarification-style teaser that
requires a prohibited second turn. That is successful recognition but weak
one-turn utility, not a failed entity match.

Because the canonical prompt does not enumerate attributes, an omitted field is
a volunteered-coverage result. It should not be treated as proof that ChatGPT
could never retrieve the field under a targeted prompt.

## Overall score

An overall score may be useful for communication and monitoring, but weights
should depend on business type. For example, local visibility matters more to a
restaurant than to a location-independent SaaS product.

Avoid finalizing weights until repeated experiments demonstrate that the
dimensions are measurable, stable, and connected to actionable improvements.

## Uncertainty

Report uncertainty using the number of runs, variance between runs, source
coverage, and confidence in entity matching. Do not imply that a single
generative answer is a precise or permanent measurement.

V1 must not describe disagreement with the website as proven factual error. The
correct label is disagreement with, or deviation from, the official website.

## Related notes

- [[Prompt Test Matrix]]
- [[Source Attribution]]
- [[Risks and Constraints]]
- [[Experiment Log]]
