---
type: product-design
status: draft
created: 2026-09-04
updated: 2026-09-04
tags:
  - artemis
  - product
  - workflow
---

# Product Workflow

## Summary

```text
Website URL
→ candidate business profile
→ website-derived reference profile
→ generated prompt matrix
→ seven independent runs per prompt
→ evaluated answers and sources
→ diagnostic report and recommendations
```

## 1. Business intake

The user enters a website URL. Artemis inspects only that exact page and
discovers candidate business information available there:

- Official and alternative business names
- Domain and relevant pages
- Business category
- Products and services
- Service areas
- Physical address and map presence
- Public business contacts
- Opening hours
- Social-media accounts and usernames
- Marketplace and directory profiles
- Reviews
- Independent media coverage and mentions
- Structured data and other machine-readable information

## 2. Entity resolution

Artemis determines which discovered profiles, pages, names, and mentions refer
to the same business. It builds a canonical profile and records the source and
confidence level for every field.

One business may be represented by its legal name, trading name, website,
social handles, map listing, marketplace store, and third-party directory
entries. Name collisions and ambiguous profiles must be surfaced rather than
silently merged.

## 3. Reference profile extraction

V1 automatically constructs the reference profile from the official website.
The user does not verify or manually enter the extracted information. See
[[2026-09-04 Website Is the V1 Reference Profile]].

Artemis does not intentionally crawl other paths. See
[[2026-09-04 V1 Starts From the Supplied URL Only]].

This profile represents the business's official published claims, not
independently verified real-world truth. Every extracted field retains its
source URL and supporting text. Missing or ambiguous website information must
remain explicitly unknown.

## 4. Prompt generation

Artemis generates prompts from the dimensions documented in
[[Prompt Test Matrix]]. The identity layer varies the supplied name, URL, and
social-handle signals; the geography and language layers hold the URL constant.

V1 uses one open-ended canonical semantic task across all matrix cells. It does
not enumerate desired fields or request browsing. See
[[2026-09-04 Canonical Prompt Is Open-Ended]].

No prompt may instruct ChatGPT to browse beyond the exact URL supplied for that
test. If ChatGPT independently searches or follows links, Artemis observes and
records that behavior without steering it.

The default monitoring cycle proceeds from the identity layer to the geography
layer and then the language layer.

The seven URL-only runs execute first within the identity layer. If the supplied
page omits a social handle or geographic value, those same answers provide
native discovery candidates. A candidate must reach a 4/7 majority before it is
used in a later prompt.

These bootstrap `U` runs use the fixed English template before the local market
language is known. See [[2026-09-04 Bootstrap URL Runs Use English]].

## 5. Agent testing

> [!success] V1 decision
> V1 observes logged-out ChatGPT through an Incognito Chrome session launched
> with Computer Use. The mechanism passed both a seven-run feasibility test and
> a complete 77-session production audit in the current environment. See
> [[2026-09-04 V1 Observes Logged-Out ChatGPT]] and
> [[2026-09-04 Arsent Dental Full Agent Glasses Audit]].

For each test, record:

- Complete response
- Whether the target business appears
- Position and prominence in the answer
- Facts stated about the business
- Confidence or qualifying language
- Recommended alternatives
- Sources and citations
- Prompt, language, location context, agent, model, and timestamp

Execute every unique prompt seven times because generative responses vary. Each
run receives its own new Incognito Chrome session. See
[[2026-09-04 Seven Runs Per Prompt]].

Eligible prompts execute once per round across seven rounds. Prompts derived
from 4/7 agent-discovery results execute afterward in a second round-robin
stage. See [[2026-09-04 Seven Runs Use Round-Robin Execution]].

Every scored test is single-turn: one prompt produces one captured answer in a
new conversation. See [[2026-09-04 V1 Uses Single-Turn Prompts]].

Every prompt also receives a separate Incognito Chrome session. The session is
closed after its first answer is captured and is never reused. See
[[2026-09-04 Fresh Incognito Session Per Prompt]].

Exactly identical prompts across layers execute once and keep every conceptual
label. See [[2026-09-04 Identical Prompts Execute Once]].

### Reproducible benchmark

Use a controlled API or search pipeline with recorded inputs and configuration.
This possible future mode supports comparable scores and regression testing; it
is not the primary V1 observation environment.

### Real-user simulation

Test a consumer-facing agent experience, such as a fresh or logged-out browser
session. This approximates a prospective customer's experience but is less
reproducible.

If both modes are supported later, they must remain separately labeled in
reports.

## 6. Evaluation

Compare every agent answer against the website-derived reference profile and
the expected behavior of its test case. Use the dimensions in [[Scoring Model]].

Evaluation should preserve the underlying response, supporting evidence, and
uncertainty rather than returning only a score.

## 7. Source attribution

Extract cited and discovered sources, resolve their domains and entities, and
classify them using [[Source Attribution]]. This shows which parts of the
business's digital presence contribute to the observed result.

## 8. Report

Recommended report sections:

1. Executive summary and overall visibility state
2. Business identity reconstructed by agents
3. Incorrect, conflicting, and missing facts
4. Branded discoverability
5. Unbranded and category discoverability
6. Visibility by location and language
7. Competitor share of agent recommendations
8. Source and channel contribution
9. Stability across agents and repeated runs
10. Prioritized recommendations

Recommendations should connect a problem to evidence:

> [!example]
> **Finding:** Agents repeatedly report an outdated address.
>
> **Evidence:** The old address appears on three directories and one social
> profile.
>
> **Recommended action:** Make the verified address consistent across the
> official website, structured data, map listing, and major directories.

## Related notes

- [[Agent Visibility Audit]]
- [[Prompt Test Matrix]]
- [[Scoring Model]]
- [[Source Attribution]]
- [[Risks and Constraints]]
