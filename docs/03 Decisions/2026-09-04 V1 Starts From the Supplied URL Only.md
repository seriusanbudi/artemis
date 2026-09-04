---
type: decision
status: accepted
created: 2026-09-04
updated: 2026-09-04
tags:
  - artemis
  - decision
  - v1
  - website
  - prompts
---

# V1 Starts From the Supplied URL Only

## Context

Artemis could deliberately crawl multiple pages to construct a comprehensive
business profile. That would measure the total information available across the
site, but it would not show how much information the business communicates when
a customer or agent first lands on the submitted page.

## Decision

V1 uses only the exact URL supplied by the user as its intentional website
entry point and reference page.

The master prompt must never instruct ChatGPT to browse another path, crawl the
website, follow internal links, search other sources, or inspect any URL other
than the one explicitly supplied for that test.

If ChatGPT independently chooses to follow a link, open another path, or search
for additional sources, Artemis will allow and record that behavior. It must
not guide, encourage, or correct the browsing decision.

## Measurement boundary

This design separates two signals:

- **Landing-page communication:** information available from the supplied page
- **Agent initiative:** additional discovery actions ChatGPT chooses without
  being instructed

The first is controlled by the business. The second is observed agent behavior.

## Consequences

- Artemis does not pre-crawl the rest of the domain for V1 evaluation.
- The website-derived reference profile contains only claims found on the
  submitted page.
- Missing information may be a meaningful landing-page finding rather than an
  extraction failure.
- Any additional URLs or sources used by ChatGPT must be captured separately as
  agent-discovered evidence.
- Prompts must be audited for implicit browsing instructions, not only explicit
  phrases such as "search the website."

## Related notes

- [[2026-09-04 Website Is the V1 Reference Profile|Website Is the V1 Reference Profile]]
- [[Prompt Test Matrix]]
- [[Product Workflow]]
- [[Decision Log]]

