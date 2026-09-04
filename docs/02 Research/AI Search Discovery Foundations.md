---
type: research
status: active
created: 2026-09-04
updated: 2026-09-04
tags:
  - artemis
  - research
  - ai-search
---

# AI Search Discovery Foundations

## Summary

Current official guidance supports the premise that AI-search visibility is
shaped by a broader information ecosystem rather than a special piece of
markup. Traditional search foundations, crawl access, clear textual content,
structured data that matches visible facts, business profiles, and relevant
third-party evidence all remain important.

## Observations

### Google AI search

Google states that its AI search features build on core Search systems and can
use query fan-out across subtopics and data sources. Its guidance emphasizes
existing search fundamentals and says there is no special AI-only schema
required.

Source: [AI features and your website](https://developers.google.com/search/docs/appearance/ai-features)

### ChatGPT search discovery

OpenAI states that public websites can appear in ChatGPT search and recommends
allowing OAI-SearchBot to access content. Eligibility does not guarantee
placement, so crawler access is a prerequisite rather than a visibility score.

Sources:

- [Publishers and Developers FAQ](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq)
- [Searching the web with ChatGPT](https://help.openai.com/en/articles/9237897)

## Product implications

- Artemis should test observable agent behavior, not claim access to internal
  model or ranking state.
- Website crawlability is one diagnostic factor, not the entire explanation.
- Source discovery must cover official, local, social, earned, and commercial
  channels. See [[Source Attribution]].
- Repeated prompt experiments are required to distinguish stable behavior from
  generative variation. See [[Prompt Test Matrix]].

## Related notes

- [[Agent Visibility Audit]]
- [[Source Attribution]]
- [[Risks and Constraints]]

