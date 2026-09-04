---
type: product-design
status: draft
created: 2026-09-04
updated: 2026-09-04
tags:
  - artemis
  - prompts
  - benchmarking
---

# Prompt Test Matrix

> [!success] Canonical semantic task
> Every V1 matrix cell asks a natural-language equivalent of “What do you know
> about `{identity signals}`?” without enumerating attributes or directing
> browsing. See [[2026-09-04 Canonical Prompt Is Open-Ended]].

> [!success] Single-turn policy
> Every scored V1 test consists of one prompt and one answer in a new
> conversation. Follow-ups and other steering are prohibited. See
> [[2026-09-04 V1 Uses Single-Turn Prompts]].

> [!success] Browser isolation
> Every prompt runs in a newly opened Incognito Chrome session that is closed
> after the first answer is captured. See
> [[2026-09-04 Fresh Incognito Session Per Prompt]].

> [!important] Browsing neutrality
> The master prompt must never instruct ChatGPT to browse beyond the exact URL
> supplied for the test. Autonomous browsing is allowed and observed, but never
> encouraged. See [[2026-09-04 V1 Starts From the Supplied URL Only]].

## Test dimensions

V1 uses three controlled layers rather than a full Cartesian product:

```text
Identity:  all non-empty N/U/H combinations
Geography: U × {G0, city, province, country} × local language
Language:  U × G0 × {local language, English}
Repeats:   every selected prompt × 7 independent runs
```

The agent product is fixed to logged-out ChatGPT and the semantic task is fixed
to the open-ended canonical question.

Every selected prompt is executed seven times according to
[[2026-09-04 Seven Runs Per Prompt]].

Exactly identical prompt text is executed once and retains all applicable
matrix labels. This prevents duplicate evidence when identity `U` equals the
English language-layer prompt or when local-language `G0` appears in both the
geography and language layers. See
[[2026-09-04 Identical Prompts Execute Once]].

## Identity seed

The V1 design uses a controlled factorial set of identity clues. See
[[Identity Signal Combination Matrix]].

- Name (`N`)
- Exact submitted URL (`U`)
- One primary social handle from the submitted page (`H`)
- Every non-empty combination of those three signals

The progression measures how much assistance the agent needs before it can
resolve the correct entity.

## Location

See [[Geography and Language Matrix]] for the proposed geographic contexts,
metrics, and combination strategies.

The exact submitted URL (`U`) remains fixed while geographic context changes.
The prompt uses the local market language throughout this layer.

The versioned English template is:

> What do you know about `{URL}` in `{location}`?

This phrasing introduces natural ambiguity and is scored as a response under
supplied location wording, not proof of business scale. See
[[2026-09-04 Geography Prompt Uses Natural In-Location Wording]].

- City
- Province or state
- Country
- No explicit location

Location can mean the business's physical location or the customer's desired
service area. They must be modeled separately for online and service-area
businesses.

## Language

See [[Geography and Language Matrix]] for the proposed language contexts,
metrics, and combination strategies.

The exact submitted URL (`U`) remains fixed while prompt language changes.
No explicit location (`G0`) is included in language-layer prompts.

Before the language layer, the seven URL-only discovery runs use the fixed
English bootstrap prompt “What do you know about `{URL}`?” See
[[2026-09-04 Bootstrap URL Runs Use English]].

- Local market language
- English

Use native phrasing rather than literal translations when possible.
The local market language is selected through a deterministic mapping from the
accepted geographic context.

Every language-specific prompt records a stable template ID and version. A
wording change creates a new benchmark version rather than modifying the
existing time series.

## Canonical semantic task

V1 uses one open-ended task across identity, geography, and language layers:

> What do you know about `{identity signals}`?

Location is added only in the geography layer. The local-language and English
templates express the same meaning naturally rather than translating word for
word.

Structured fact retrieval, category discovery, comparison, recommendation, and
transaction prompts are outside the default V1 matrix.

## Experiment controls

Every execution should record:

- Exact prompt
- Agent product and model, when visible
- Search or browsing state
- Any browsing or link-following initiated autonomously by ChatGPT
- Logged-in, logged-out, or API mode
- Requested and observed location context
- Interface and browser language
- Timestamp
- Run number from `1` through `7`
- Round number and execution order
- Every conceptual matrix label represented by a deduplicated prompt

The evaluator captures the first answer as returned. Clarification prompts,
corrections, follow-ups, and regenerations are not part of the same scored test.

> [!warning]
> A fresh or incognito session is not fully neutral. IP location, browser
> language, time, indexes, and agent version may still affect the answer.

## Related notes

- [[Product Workflow]]
- [[Scoring Model]]
- [[Experiment Log]]
- [[Risks and Constraints]]
