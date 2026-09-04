---
type: experiment-run
status: complete
created: 2026-09-04
updated: 2026-09-04
audit_id: 2026-09-04-supabase-v1
target_url: https://supabase.com/
protocol_version: agent-glasses-v1
accepted_sessions: 49
bootstrap_sessions: 7
---

# Supabase Agent Glasses audit

## Executive result

Supabase has a **strong, self-sufficient agent identity** in logged-out ChatGPT.

The name, exact URL, X/Twitter handle, and every combination resolved the
correct company in 7/7 observations. Unlike Rover, the name alone produced a
substantive product explanation in all seven runs without visible browsing.
Unlike Arsent Dental, the handle alone was also correctly bound to the company
in every run.

The website's core product model is exceptionally legible. Across 28
URL-bearing observations, Postgres, Authentication, Data APIs, Edge Functions,
Realtime, Storage, and open-source positioning each appeared 28/28 times.
Self-hosting appeared 24/28 and Row Level Security 27/28. Certification details
were rarely volunteered, even when all identity signals were supplied.

## Test scope

- Product: consumer ChatGPT.com
- State: logged out
- Browser: a completely new Chrome Incognito window per attempt
- Conversation: one exact prompt and one first answer
- Target: `https://supabase.com/`
- Bootstrap: seven English URL-only observations to resolve missing geography
- Matrix execution: 2026-09-04 18:47–19:11 Asia/Makassar
- Schedule: 7 unique identity prompts across seven round-robin rounds
- Accepted scored observations: 49
- Accepted bootstrap observations: 7
- Conceptual scored observations: 63

English is both the local-market and comparison language, so exact duplicates
were deduplicated. No location prompt was generated because neither the exact
page nor the bootstrap established a location candidate.

## Run integrity

| Control | Result |
|---|---:|
| Scored planned sessions accepted | 49/49 |
| Bootstrap sessions accepted | 7/7 |
| Unique scored prompts repeated exactly seven times | 7/7 |
| Logged-out state verified | 56/56 |
| Incognito state verified | 56/56 |
| Single-turn state verified | 56/56 |
| Completed first answer captured | 56/56 |
| Incognito window closed after capture | 56/56 |
| Protocol validation errors | 0 |
| Scored browser attempts | 53 |
| Failed scored attempts retained | 4 |

The four scored failures were one malformed/duplicate response container, two
composer timeouts, and one false-positive CAPTCHA classification. The last was
caused by the generated answer mentioning “Cloudflare Workers”; it was not a
human-verification UI. The detector was narrowed to actual verification UI
signals, and the planned session succeeded in a fresh Incognito window. No
actual CAPTCHA or rate limit occurred.

## Identity resolution and first-answer utility

| Signals supplied | Correct target | First-answer behavior |
|---|---:|---|
| Name (`N`) | 7/7 | Detailed product overview 7/7, no visible browsing |
| URL (`U`) | 7/7 | Detailed page-aligned overview 7/7 |
| X/Twitter handle (`H`) | 7/7 | Correct account and company binding 7/7 |
| Name + URL | 7/7 | Detailed company and product overview 7/7 |
| Name + handle | 7/7 | Correct company and social binding 7/7 |
| URL + handle | 7/7 | Correct company and social binding 7/7 |
| Name + URL + handle | 7/7 | Correct company and social binding 7/7 |

Supabase therefore demonstrates the desired mature state: each public identity
signal independently anchors the same entity, and the bare name already
elicits a useful answer from model knowledge.

## Website alignment and volunteered coverage

Counts below aggregate all 28 URL-bearing observations.

| Page-declared field | Volunteered frequency |
|---|---:|
| Correct target entity | 28/28 |
| Postgres | 28/28 |
| Authentication | 28/28 |
| Data APIs | 28/28 |
| Edge Functions | 28/28 |
| Realtime | 28/28 |
| Storage | 28/28 |
| Open-source positioning | 28/28 |
| Row Level Security | 27/28 |
| Self-hosting | 24/28 |

The core category and product architecture survive every URL-bearing prompt.
The page also declares SOC 2 Type 2, HIPAA, and ISO 27001 claims, but each was
volunteered only once, in the same all-signals condition. These omissions
measure salience, not retrievability.

## Geography bootstrap and profile

The exact landing page declares worldwide customer reach but no headquarters
city, state/province, or country. The required seven English URL-only bootstrap
answers volunteered no stable city, state, country, “based in,” or
“headquartered” candidate. Nothing reached the 4/7 promotion threshold.

Geography prompts were therefore skipped instead of inventing a location. This
is a successful protocol outcome, not missing execution. “Worldwide” was not
substituted for a corporate location because it describes customer reach.

## Language portability

The accepted local-market language is English, so local and English prompts
are identical and were correctly deduplicated. This audit contains no
cross-language comparison for Supabase.

## Retrieval and source behavior

Visible autonomous browsing or source UI appeared in 42/49 scored answers. The
seven non-browsing answers were exactly the name-only condition. `Supabase`
appeared as a visible source label 42 times—once per browsing observation.
Other visible labels included X, GitHub, GIGAZINE, TechCrunch, and Axios.

The result shows a clean split: ChatGPT answered the name from internal model
knowledge and used retrieval whenever a URL or handle was supplied. Citation
destinations were not normalized, so this is a source-label observation rather
than a complete authority audit.

## Consistency and runtime

- Median accepted-attempt latency: 12.73 seconds
- 95th percentile: 17.36 seconds
- Maximum: 18.50 seconds
- Autonomous browsing observed: 42/49
- Name-only median answer length: 2,861 characters
- URL-only median answer length: 4,170 characters

Answer length is not scored by itself. Here it supports semantic review: every
name-only answer contained a detailed, correct explanation of the product.

## Diagnostic state

| Dimension | State |
|---|---|
| Recognition from any identity signal | Strong and consistent |
| Name-only first-answer utility | Strong and consistent |
| Website factual legibility | Strong and consistent |
| Social identity binding | Strong and consistent |
| Geography-conditioned recognition | Not measured; no defensible location |
| Cross-language portability | Not measured; LL is English |
| Trust-certification salience | Weak in open-ended answers |
| Independent authority | Visible, but not fully audited |

No composite score is assigned. The current evidence is better represented as
a diagnostic profile than a single business-type-independent number.

## Prioritized actions

1. Preserve the exact `Supabase` / `supabase.com` / `@supabase` identity chain;
   it is independently resolvable from every tested signal.
2. Preserve the stable Postgres-centered product definition across the site,
   documentation, GitHub, and social profile.
3. If compliance salience matters commercially, make certification claims more
   prominent and consistently associated with the main entity definition.
4. Decide whether a corporate location belongs in the public entity profile.
   Do not add one merely to satisfy this matrix; add it only if useful and true.
5. Repeat the fixed benchmark over time to detect model-memory and retrieval
   changes separately.

## Limitations

- Consumer ChatGPT behavior, indexes, UI, and model routing can change.
- Incognito does not remove IP, locale, time, or platform-experiment effects.
- The visible UI did not expose a dependable model identifier.
- The submitted landing page is a claim set, not independently verified truth.
- Geography was intentionally skipped because the accepted evidence did not
  establish a city, state/province, or country.
- The false CAPTCHA record is an instrumentation failure, not platform proof.
- Literal signal counts are deterministic heuristics and were semantically
  reviewed.
- Citation destinations were not opened or normalized.

## Artifacts

- `config.json` — accepted inputs and templates
- `reference.json` — exact-page reference profile and provenance
- `reference-capture.txt` — landing-page accessibility capture
- `bootstrap-plan.json` — seven-run URL bootstrap schedule
- `bootstrap-ledger.jsonl` — bootstrap answers and captures
- `bootstrap-audit.json` — bootstrap integrity result
- `plan.json` — deduplicated scored schedule
- `ledger.jsonl` — all accepted and failed scored attempts
- `audit.json` — scored protocol-integrity result
- `signals.json` — deterministic literal-field patterns
- `analysis.json` — per-prompt counts, source labels, and timing statistics

