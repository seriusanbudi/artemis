---
type: experiment-synthesis
status: complete
created: 2026-09-04
updated: 2026-09-04
tags:
  - artemis
  - agent-glasses
  - product-learning
  - experiment
---

# Agent Glasses Product Learnings

## Central conclusion

Artemis should begin as an **agent-observability product**, not an AEO score
generator.

Its first job is to show a business exactly where its public identity works or
breaks when viewed through an agent. Optimization recommendations and an
overall score can follow only after the underlying dimensions are measurable,
stable, and connected to changes a business can make.

## Refined product thesis

The starting thesis was that agents will increasingly become the layer between
customers and businesses. Businesses will therefore need something analogous
to SEO for how agents find, understand, compare, and select them.

The experiment supports that direction but makes the role more precise: the
agent does not necessarily replace the human customer. It becomes the
customer's discovery and decision interface.

The product question is therefore not merely:

> Does ChatGPT know this business?

It is:

> Under which supplied clues can an agent resolve this business, what does it
> say in its first answer, which public facts survive, and where does the
> connection between the business's public surfaces break?

## Agent visibility is not one metric

The three-business experiment revealed at least four dimensions that can fail
independently:

| Dimension | Question |
|---|---|
| Entity recognition | Does the agent select the intended business? |
| First-answer utility | Does the single allowed answer explain the business, or require clarification? |
| Website legibility | When given the exact URL, which page-declared facts does the agent recover? |
| Cross-surface identity binding | Do the name, URL, social handle, and location converge on one entity? |

This separation matters. Rover was correctly recognized from its name in 7/7
runs, but only one run gave a substantive overview. Recognition was strong;
one-turn utility was weak.

Source authority, actionability, geographic behavior, language portability,
and consistency remain additional diagnostic dimensions. They should not be
collapsed prematurely into one number.

## Experimental findings

### Arsent Dental: URL-dependent identity

Arsent Dental performed substantially better after URL anchoring than its
overall visibility initially suggested.

Across 56 URL-bearing observations:

- Correct clinic and business name: 56/56
- Gianyar: 56/56
- Named dentist: 55/56
- Exact SIP: 55/56
- Services: 55/56
- Published prices: 55/56
- Street address: 46/56
- Exact phone: 38/56

This means the landing page is already highly legible to the agent. A small,
new business can match mature businesses on page comprehension when the agent
is supplied with its exact URL.

The failure happens before the URL is known:

- Name only: 0/7 correct resolution
- Instagram handle only: 0/7 correct resolution
- Name plus handle: two clean matches, one mixed/conflicting identity, and four
  unresolved observations

The primary weakness is therefore the identity network around the site, not
simply the site's ability to explain the business.

### Rover: recognized but interaction-fragile

Rover's name, URL, Instagram handle, and every combination resolved the correct
pet-care company in 7/7 observations.

However, the word `Rover` is inherently ambiguous. Six of seven name-only
answers selected the intended company but stopped at a clarification-style
teaser instead of giving a real overview. Only one produced a substantive
first answer.

A recognition-only score would incorrectly describe this experience as
perfect. The result validates first-answer utility as a separate measurement.

### Supabase: self-sufficient identity

Supabase demonstrated the strongest state:

- Name only: 7/7 correct and substantive
- Exact URL: 7/7 correct
- X/Twitter handle: 7/7 correctly bound to the company
- Every two- and three-signal combination: 7/7 correct

The name-only answers were detailed without visible browsing. URL and handle
conditions independently converged on the same Postgres-centered company
identity. This is the clearest current benchmark for an agent-ready identity
that does not depend on one anchor.

## Three observed maturity states

| State | Business | Interpretation |
|---|---|---|
| URL-dependent identity | Arsent Dental | The site is understandable, but name and social identity do not reliably lead to it |
| Recognized but interaction-fragile | Rover | Identity signals converge, but the ambiguous name weakens the native one-turn answer |
| Self-sufficient identity | Supabase | Name, URL, and handle independently resolve the same entity and produce useful information |

These states are more informative than a generic good/bad visibility score.

## AEO is an identity-graph problem

The results suggest that agent readiness is not achieved merely by publishing
more website content. It depends on consistent relationships among public
surfaces:

```text
Business name
↕
Canonical website
↕
Social accounts
↕
Location and Maps
↕
Directories and marketplaces
↕
Independent mentions
↕
Structured data
```

The website can be individually excellent while the external identity graph
remains fragmented. Conversely, an established name can be recognized while
still producing an unhelpful first interaction.

## Browsing is behavior, not quality

Visible autonomous browsing or source UI appeared in:

- Arsent Dental: 75/77 accepted observations
- Rover: 63/70
- Supabase: 42/49

Supabase's seven name-only answers were excellent without browsing. Arsent
frequently browsed while still failing its unanchored identity tests.

Browsing frequency must therefore remain a recorded behavior. It must not be
used as a proxy for visibility, correctness, or answer quality.

## Geography does not prove market strength

The geographic layer measures whether business recognition and factual
coverage remain stable when location wording is added. It does not establish:

- Offline popularity
- Google Maps ranking
- Market share
- Operational scale
- Recommendation strength

Rover remained correctly resolved under Seattle, Washington, and United States
wording, but these were page-declared service-market contexts. Supabase had no
defensible corporate location on the submitted page, and no location reached
the 4/7 bootstrap threshold. Skipping its geographic prompts was the correct
result.

Unknown is valid data. Artemis must not invent a location or substitute
worldwide customer reach merely to complete the matrix.

## What the current product can claim

The validated workflow can answer:

> When logged-out ChatGPT receives different public identifiers for this
> business, can it identify the correct entity and provide accurate, useful,
> and consistent information in one answer?

It can currently diagnose:

- URL dependency
- Name ambiguity
- Social-account fragmentation
- Website information coverage
- Conflicting business facts
- Location and language portability
- Source-label behavior
- Response consistency

It cannot yet establish:

- Whether ChatGPT will recommend the business for an unbranded customer intent
- How the business ranks against competitors
- Whether the business is popular offline
- Which remediation will causally improve agent behavior
- A universal or permanent AEO score

Those require later recommendation, intent, longitudinal, cross-agent, and
possibly competitive experiments. They remain outside the target-only v1
measurement.

## Product direction

The first commercial output should be framed as an **Agent Identity and
Visibility Audit**. Its primary output should be an explainable diagnostic
profile containing:

1. Entity recognition
2. First-answer utility
3. Website legibility
4. Cross-surface identity binding
5. Geographic behavior
6. Language portability
7. Actionability
8. Source authority
9. Seven-run consistency

An overall score may eventually help communication, but it should not hide the
component observations. Business-type-specific weighting should wait until the
dimensions have been repeated across more targets and dates.

## Best next validation

The strongest next experiment is a controlled before-and-after test using
Arsent Dental:

1. Make the canonical name, URL, Instagram handle, address, phone, Maps
   presence, and structured data consistent.
2. Improve relevant independent citations without changing the benchmark.
3. Repeat the exact same prompts and seven-run schedule.
4. Measure movement in name-only and handle-only resolution.
5. Record which sources begin appearing and whether conflicting identity facts
   disappear.

This would test whether Artemis recommendations lead to measurable improvement
instead of merely describing correlation.

## Final learning

The experiment validates the agent-glasses concept. The most valuable result is
not simply whether an agent can read a website. It is identifying where the
connection between the website and the rest of the business's public identity
breaks—and whether that break changes the first answer a customer receives.

## Related notes

- [[Agent Visibility Audit]]
- [[Product Workflow]]
- [[Scoring Model]]
- [[Identity Signal Combination Matrix]]
- [[2026-09-04 Rover and Supabase Agent Glasses Gap Test]]
- [[2026-09-04 Arsent Dental Full Agent Glasses Audit]]
- [Visual dashboard](agent-glasses-dashboard.html)

