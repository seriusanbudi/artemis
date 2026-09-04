---
type: product-design
status: active
created: 2026-09-04
updated: 2026-09-04
tags:
  - artemis
  - prompts
  - geography
  - language
  - combinations
---

# Geography and Language Matrix

> [!success] V1 decision
> V1 uses separate identity, geography, and language layers. Only one primary
> dimension changes in each layer. See
> [[2026-09-04 V1 Uses a Layered Test Matrix]].

> [!success] Identity anchor
> Both layers hold the exact submitted URL (`U`) constant. See
> [[2026-09-04 Geography and Language Layers Use the URL Anchor]].

> [!success] Geography-layer language
> The geography layer holds the local market language (`LL`) constant while
> geographic context changes. See
> [[2026-09-04 Geography Layer Uses the Local Market Language]].

> [!success] Language-layer geography
> The language layer holds no explicit location (`G0`) constant while prompt
> language changes. See [[2026-09-04 Language Layer Uses No Location Context]].

> [!success] Local market language
> `LL` comes from a deterministic mapping of the accepted geographic values,
> not from the rendered page or ChatGPT's response language. See
> [[2026-09-04 Local Market Language Uses Deterministic Mapping]].

> [!success] Regional specificity
> Use the most specific mainstream commercial language, with a country fallback.
> Do not select traditional or heritage languages by default. See
> [[2026-09-04 LL Uses the Mainstream Market Language]].

## Purpose

Measure how geographic framing and prompt language affect ChatGPT's ability to
recognize and describe the target business.

## Geographic contexts

| Code | Context | What it measures |
|---|---|---|
| `G0` | No location supplied | Baseline recognition without geographic assistance |
| `GC` | City | City-level recognition and disambiguation |
| `GP` | Province or state | Regional recognition and disambiguation |
| `GN` | Country | National recognition and disambiguation |

City, province, and country values should be extracted from the exact submitted
page. When a level is absent, it can be promoted from the seven URL-only answers
only if the same normalized value appears at least 4/7 times. See
[[2026-09-04 Agent-Discovered Location Requires Four of Seven]].

## Geographic metrics

- Recognition rate at each level, from `0/7` to `7/7`
- Geographic lift relative to the `G0` baseline
- Identity consistency across geographic contexts
- Location-fact agreement with the submitted page
- Changes in cited or autonomously discovered sources
- **Observed reach profile:** city, province, and country contexts in which the
  business is consistently recognized

V1 uses the natural template “What do you know about `{URL}` in
`{location}`?” The resulting metric is explicitly labeled as a response under
supplied location wording because the phrase can imply location, service area,
or local relevance.

> [!warning]
> The observed reach profile is not proof that the business operates or is
> popular at that scale. A location can improve entity disambiguation without
> demonstrating market reach.

## Language contexts

| Code | Context | Purpose |
|---|---|---|
| `LL` | Local market language | Visibility in the language associated with the extracted location |
| `LE` | English | Cross-language visibility baseline |

If both contexts resolve to English, run that language only once and retain both
semantic labels in the report. The website's rendered language remains recorded
metadata, not a separate V1 prompt language. See
[[2026-09-04 V1 Tests Local Language and English]].

## Language metrics

- Recognition rate per language
- Entity consistency across languages
- Fact completeness and website alignment per language
- Citation consistency per language
- **Language portability:** whether the same business identity and core facts
  survive translation into another prompt language

Prompts should use natural phrasing for each language. Literal word-for-word
translation can create an artificial performance difference. Each language uses
a stable, versioned template. See
[[2026-09-04 Prompts Use Versioned Language Templates]].

## Combination approaches

### A. Full Cartesian matrix

Run every identity combination across every geography and language.

```text
7 identity combinations
× 4 geographic contexts
× 2 language contexts
× 7 repeated runs
= 392 maximum browser executions
```

Duplicate languages may reduce the actual total. This provides the most
complete interaction data but has high runtime and failure exposure.

### B. Layered controlled matrices

Run the full identity matrix once, then hold a selected identity signal constant
while testing geography and language separately.

Example maximum:

```text
Identity: 7 combinations × 7 runs = 49
Geography: 4 contexts × 7 runs = 28
Language: 2 contexts × 7 runs = 14
Total = 91 browser executions
```

This is easier to interpret because only one dimension changes at a time.

### C. Adaptive expansion

Run the layered matrix first, then expand only where recognition is inconsistent
or where a geographic or language context produces meaningful lift.

This reduces routine execution volume but makes monitoring cycles less uniform.

## Neutrality constraint

Location and language may be supplied as context, but prompts must not instruct
ChatGPT to browse beyond the exact submitted URL. Autonomous browsing remains
an observed behavior. See [[2026-09-04 V1 Starts From the Supplied URL Only|V1 Starts From the Supplied URL Only]].

## Related notes

- [[Identity Signal Combination Matrix]]
- [[Prompt Test Matrix]]
- [[Scoring Model]]
- [[2026-09-04 Seven Runs Per Prompt|Seven Runs Per Prompt]]
