---
type: decision
status: accepted
created: 2026-09-04
updated: 2026-09-04
tags:
  - artemis
  - decision
  - v1
  - geography
  - language
---

# Geography Layer Uses the Local Market Language

## Context

The geography layer needs one fixed prompt language while city, province, and
country context changes. The submitted page's rendered language may vary due to
IP geolocation, browser locale, cookies, content negotiation, or a multilingual
site.

## Decision

The geography layer will use the local market language associated with the
business's geographic context.

```text
URL anchor
× local market language
× {no location, city, province, country}
× 7 independent runs
```

The language actually rendered by the submitted page is recorded as an
observation, not used as the primary geography-layer language control.

## Rationale

- It represents how customers in the relevant market are more likely to ask.
- It is conceptually independent from dynamic website-language behavior.
- It makes the geographic result easier to interpret as local-market agent
  visibility.
- Rendered website language remains observable metadata and may become a future
  optional test language.

## Boundary

Prompting with a city, province, or country does not change the browser's actual
IP location. Prompt geography, IP geography, browser locale, and rendered page
language are separate variables and should not be conflated.

## Related notes

- [[Geography and Language Matrix]]
- [[Prompt Test Matrix]]
- [[Decision Log]]
