---
type: product-design
status: draft
created: 2026-09-04
updated: 2026-09-04
tags:
  - artemis
  - attribution
  - sources
---

# Source Attribution

## Purpose

Classify every cited or discovered source so Artemis can explain where a
business's observable agent visibility comes from.

## Source channels

| Channel | Examples | Signal |
|---|---|---|
| Owned web presence | Official website and first-party content | Business-controlled identity and facts |
| Local presence | Maps, business listings, directories, reviews | Observable local prominence and consistency |
| Social visibility | Official accounts and third-party social mentions | Social identity, activity, and discussion |
| Earned authority | News, blogs, associations, industry publications | Independent recognition and evidence |
| Commerce presence | Marketplaces, booking sites, product feeds | Availability and transactional readiness |

## Interpretation rules

- Strong Maps and review signals indicate strong observable local presence;
  they do not prove offline popularity.
- Numerous social mentions indicate social visibility; they do not
  automatically indicate positive reputation.
- Media citations indicate earned authority only after source quality,
  independence, and relevance are considered.
- An official source is valuable for factual accuracy but is not independent
  evidence of reputation.
- The same claim repeated by copied directory pages should not be treated as
  independent corroboration.

## Proposed source record

For each source, retain:

- URL and domain
- Page or profile title
- Source channel
- First-party or third-party status
- Business entity matched
- Claims supported
- Citation frequency across tests
- Discovery timestamp
- Confidence and ambiguity notes

## Related notes

- [[Product Workflow]]
- [[Scoring Model]]
- [[Risks and Constraints]]

