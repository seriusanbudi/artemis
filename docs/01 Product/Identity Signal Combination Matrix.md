---
type: product-design
status: active
created: 2026-09-04
updated: 2026-09-04
tags:
  - artemis
  - prompts
  - identity-resolution
  - combinations
---

# Identity Signal Combination Matrix

> [!success] V1 decision
> The fixed V1 signals are name (`N`), exact submitted URL (`U`), and one
> primary social handle (`H`) found on the submitted page. See
> [[2026-09-04 Core Identity Matrix Uses Name URL and Handle]].

## Purpose

Measure how each supplied identity clue changes ChatGPT's ability to recognize
and describe the target business.

The semantic task remains constant. Only the supplied identity signals change,
so differences between results can be attributed to those signals.

## Proposed core signals

| Code | Signal | Example |
|---|---|---|
| `N` | Official business name | `Example Company` |
| `U` | Exact submitted URL | `https://example.com` |
| `H` | Primary social handle with platform and provenance | `Instagram: @example` |

## Full core combination set

Three binary signals produce seven non-empty combinations:

| Test | Supplied signals | What it measures |
|---|---|---|
| `N` | Name | Recognition from the brand name alone |
| `U` | URL | Understanding from the supplied page alone |
| `H` | Social handle | Entity resolution from social identity alone |
| `N+U` | Name and URL | Lift produced by connecting brand and website |
| `N+H` | Name and handle | Lift produced by connecting brand and social identity |
| `U+H` | URL and handle | Cross-channel resolution without giving the name |
| `N+U+H` | All three | Best informed identity-resolution condition |

Each combination runs seven times according to [[2026-09-04 Seven Runs Per Prompt|Seven Runs Per Prompt]]. The
core identity matrix therefore requires `7 combinations × 7 runs = 49` fresh
Incognito sessions before adding location, language, or intent variants.

### Social-handle provenance

`H` may come from either:

- `page_declared`: published on the exact submitted page
- `agent_discovered`: the most consistently returned candidate from the seven
  URL-only runs when the page does not publish one

When `H` is agent-discovered, `U` must run first. The selected candidate is then
fed into the remaining `H` combinations as an explicitly labeled second-stage
test. The same normalized platform-and-username pair must appear in at least
four of seven `U` answers. See
[[2026-09-04 Agent-Discovered H Requires Four of Seven]].

## Proposed metrics

### Recognition rate

The number of runs that resolve the intended business, expressed as `0/7`
through `7/7`.

### Field recovery

Which business attributes appear under each signal combination, such as name,
type, products, services, location, contact information, and social profiles.

### Consistency

How stable the entity, facts, sources, and answer structure are across the seven
runs for the same combination.

### Signal lift

The change observed when adding one identity clue to another. Examples:

- URL lift: compare `N` with `N+U`
- Social lift: compare `N` with `N+H`
- Name lift: compare `U` with `N+U`
- Combined lift: compare the strongest two-signal result with `N+U+H`

### Identifier dependency profile

A summary of which clues ChatGPT needs to identify the business reliably. For
example:

> The business is inconsistently recognized by name (`3/7`), reliably
> recognized by URL (`7/7`), and gains no additional recognition from its
> social handle.

### Social entity attribution

Report whether ChatGPT returns a stable social account for the business, which
account it selects, and whether the association conflicts with the submitted
page's identity signals. A stable but unintended association is an entity
misattribution finding.

## Possible later signals

- Alternative or legal business name
- Phone number
- Physical address or exact map URL
- Product or service name
- Business category
- Tagline
- Marketplace username

These should not all enter a full combination matrix. Five binary signals
already create 31 non-empty combinations, or 217 Incognito sessions before
location and language variants. Later signals should use a capped or pairwise
experimental design.

## Design constraint

Prompts that include `U` may provide only the exact submitted URL. They must not
instruct ChatGPT to browse other paths or sources. See
[[2026-09-04 V1 Starts From the Supplied URL Only|V1 Starts From the Supplied URL Only]].

## Related notes

- [[Prompt Test Matrix]]
- [[Scoring Model]]
- [[2026-09-04 Seven Runs Per Prompt|Seven Runs Per Prompt]]
- [[2026-09-04 V1 Starts From the Supplied URL Only|V1 Starts From the Supplied URL Only]]
