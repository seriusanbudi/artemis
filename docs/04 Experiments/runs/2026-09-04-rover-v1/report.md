---
type: experiment-run
status: complete
created: 2026-09-04
updated: 2026-09-04
audit_id: 2026-09-04-rover-v1
target_url: https://www.rover.com/
protocol_version: agent-glasses-v1
accepted_sessions: 70
---

# Rover Agent Glasses audit

## Executive result

Rover has a **strong agent-visible identity graph with a weak name-only answer
experience** in logged-out ChatGPT.

Every identity signal resolved the intended pet-care business in all seven
observations: name, URL, Instagram handle, and every combination. The important
exception is answer usefulness. Six of seven name-only answers merely said, in
effect, “if you mean the pet-care Rover, I can explain it,” and invited another
turn. Only one gave a substantive overview. Because this benchmark permits no
follow-up, recognition is 7/7 while first-answer usefulness is 1/7.

Once the exact URL was supplied, the site consistently exposed Rover's core
offering. Across 49 URL-bearing observations, boarding and house sitting
appeared 49/49 times; dog walking, drop-in visits, and day care each appeared
47/49 times. The Rover Guarantee appeared 37/49 and the book-and-pay model
27/49. This is strong website legibility with less consistent trust and
transaction detail.

## Test scope

- Product: consumer ChatGPT.com
- State: logged out
- Browser: a completely new Chrome Incognito window per attempt
- Conversation: one exact prompt and one first answer
- Target: `https://www.rover.com/`
- Execution window: 2026-09-04 18:46–19:18 Asia/Makassar
- Schedule: 10 unique prompts across seven round-robin rounds
- Accepted observations: 70
- Conceptual observations: 84

Because English is both the local-market and comparison language, the identity
URL prompt, geography-without-location prompt, and language prompt collapse to
one exact text. The plan executed each identical prompt once while retaining
all conceptual labels.

## Run integrity

| Control | Result |
|---|---:|
| Planned sessions accepted | 70/70 |
| Unique prompts repeated exactly seven times | 10/10 |
| Logged-out state verified | 70/70 |
| Incognito state verified | 70/70 |
| Single-turn state verified | 70/70 |
| Completed first answer captured | 70/70 |
| Incognito window closed after capture | 70/70 |
| Protocol validation errors | 0 |
| Total browser attempts | 72 |
| Failed attempts retained | 2 |

One failed attempt could not find the composer and one exceeded the generation
completion timeout. Each failed window was closed; the same planned session
then succeeded in a fresh Incognito window.

## Identity resolution and first-answer utility

| Signals supplied | Correct target | First-answer behavior |
|---|---:|---|
| Name (`N`) | 7/7 | 6 short clarification-style teasers; 1 substantive overview |
| URL (`U`) | 7/7 | Detailed business overview 7/7 |
| Instagram handle (`H`) | 7/7 | Correct account and business binding 7/7 |
| Name + URL | 7/7 | Detailed business overview 7/7 |
| Name + handle | 7/7 | Correct business and social binding 7/7 |
| URL + handle | 7/7 | Correct business and social binding 7/7 |
| Name + URL + handle | 7/7 | Correct business and social binding 7/7 |

The deterministic name-only heuristic undercounted correct recognition because
six answers used short phrases such as “pet-sitting and dog-walking platform”
without the longer marketplace vocabulary expected by the regex. Semantic
review overrides that heuristic: all seven selected the intended company as
the first interpretation while acknowledging that “Rover” is ambiguous.

This creates a useful product distinction. **Entity recognition** asks whether
the agent selected the right business. **First-answer utility** asks whether a
user received useful information without steering or a follow-up. Rover passes
the first test and is weak on the second under name-only wording.

## Website alignment and volunteered coverage

Counts below aggregate all 49 URL-bearing observations.

| Page-declared field | Volunteered frequency |
|---|---:|
| Correct target entity | 49/49 |
| Boarding | 49/49 |
| House sitting | 49/49 |
| Dog walking | 47/49 |
| Drop-in visits | 47/49 |
| Doggy day care | 47/49 |
| Training | 35/49 |
| Rover Guarantee | 37/49 |
| Book-and-pay model | 27/49 |

The service catalog is highly legible. Trust and transaction facts are real
but less likely to be volunteered in an open-ended first answer. Omission here
does not mean ChatGPT could not retrieve a fact under a targeted question.

## Geography profile

Rover's landing page lists many markets. Seattle, Washington, and United States
were therefore tested as **service-market contexts**, not headquarters claims
or evidence of market scale.

| URL condition | Recognition | Supplied location repeated | Boarding | Rover Guarantee |
|---|---:|---:|---:|---:|
| No location | 7/7 | — | 7/7 | 6/7 |
| Seattle | 7/7 | 7/7 | 7/7 | 4/7 |
| Washington | 7/7 | 7/7 | 7/7 | 6/7 |
| United States | 7/7 | 7/7 | 7/7 | 7/7 |

Recognition is fully stable across the tested location wording. The results do
not establish popularity, ranking, supply, or competitive strength in those
markets.

## Language portability

The accepted local-market language is English, so local and English prompts
are identical and were correctly deduplicated. This audit therefore contains
no cross-language comparison for Rover.

## Retrieval and source behavior

Visible autonomous browsing or source UI appeared in 63/70 accepted answers.
The seven non-browsing observations were exactly the name-only condition.
`Rover.com` appeared as a visible source label 62 times and `Rover Support` 30
times across the run. Other labels included Instagram, Wikipedia, Blackstone,
and SEC.

The accessibility capture retained source labels but did not normalize every
citation destination. These counts describe visible source behavior, not a
complete domain-level authority audit.

## Consistency and runtime

- Median accepted-attempt latency: 9.20 seconds
- 95th percentile: 17.01 seconds
- Maximum: 18.85 seconds
- Autonomous browsing observed: 63/70
- Name-only median answer length: 271 characters
- URL-only median answer length: 2,552 characters

The roughly ninefold median length difference between name-only and URL-only
answers reinforces the utility gap. Answer length itself is not a quality
score; the underlying answers were also reviewed semantically.

## Diagnostic state

| Dimension | State |
|---|---|
| Recognition from any identity signal | Strong and consistent |
| Website factual legibility | Strong and consistent |
| Name-only first-answer utility | Weak despite correct recognition |
| Social identity binding | Strong and consistent |
| Geography-conditioned recognition | Strong across tested wording |
| Cross-language portability | Not measured; LL is English |
| Trust and transaction coverage | Moderate and variable |
| Independent authority | Visible, but not fully audited |

No composite score is assigned. Combining recognition and useful answer depth
would conceal Rover's most informative failure mode.

## Prioritized actions

1. Make the canonical one-sentence definition—pet-care marketplace connecting
   owners with sitters and walkers—consistent across high-authority profiles.
2. Strengthen the brand-name association enough that a name-only first answer
   explains Rover directly instead of asking for another turn.
3. Preserve the strong URL-to-social relationship around `rover.com` and
   `@roverdotcom`.
4. Keep trust and transaction claims explicit and consistent so the Guarantee,
   support, and book/pay model are volunteered more often.
5. Repeat the identical name-only condition over time; it is the clearest
   leading indicator for native answer usefulness.

## Limitations

- Consumer ChatGPT behavior, indexes, UI, and model routing can change.
- Incognito does not remove IP, locale, time, or platform-experiment effects.
- The visible UI did not expose a dependable model identifier.
- The submitted landing page is a claim set, not independently verified truth.
- Rover is an ambiguous common word, which materially affects name-only style.
- Seattle and Washington are page-declared service-market examples, not proof
  of headquarters, popularity, or scale.
- The Instagram target was truncated in the accessibility output;
  `@roverdotcom` was inferred from the footer target and consistent social-link
  naming. This should be recaptured if exact handle provenance becomes scored.
- Literal signal counts are deterministic heuristics; name-only resolution was
  corrected through semantic review.
- Citation destinations were not opened or normalized.

## Artifacts

- `config.json` — accepted inputs and templates
- `reference.json` — exact-page reference profile and provenance
- `reference-capture.txt` — landing-page accessibility capture
- `plan.json` — deduplicated round-robin schedule
- `ledger.jsonl` — all accepted and failed browser attempts
- `audit.json` — protocol-integrity result
- `signals.json` — deterministic literal-field patterns
- `analysis.json` — per-prompt counts, source labels, and timing statistics

