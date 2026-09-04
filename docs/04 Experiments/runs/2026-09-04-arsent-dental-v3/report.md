---
type: experiment-run
status: complete
created: 2026-09-04
updated: 2026-09-04
audit_id: 2026-09-04-arsent-dental-v3
target_url: https://www.arsentdental.com/
protocol_version: agent-glasses-v1
accepted_sessions: 77
---

# Arsent Dental Agent Glasses audit

## Executive result

Arsent Dental has a **strong URL-anchored agent identity but weak unanchored
brand and social discoverability** in logged-out ChatGPT.

The exact submitted URL resolved the correct clinic in all 56/56 URL-bearing
observations. By contrast, the business name alone and Instagram handle alone
each resolved the intended clinic in 0/7 observations. When ChatGPT lacked the
URL, it repeatedly found unrelated dental-material records, similarly named
clinics, or an unrelated Russian dental business.

The website itself is highly legible to the agent. Across the 56 URL-bearing
answers, the clinic name and Gianyar appeared 56/56 times; the named dentist,
SIP, services, and published prices each appeared 55/56 times. The weaker layer
is the identity graph outside the URL: the official social account was never
volunteered in either URL-only language test, and one name-plus-handle run mixed
the target with a conflicting phone number and street.

## Test scope

- Product: consumer ChatGPT.com
- State: logged out
- Browser: a completely new Chrome Incognito window per attempt
- Conversation: one exact prompt and one first answer
- Target: `https://www.arsentdental.com/`
- Execution window: 2026-09-04 17:07–17:26 Asia/Makassar
- Schedule: 11 unique prompts across seven round-robin rounds
- Accepted observations: 77
- Conceptual observations: 91

The 13 conceptual prompt variants would produce 91 observations. Two pairs are
exact duplicates: identity `U` equals English language `U+G0`, and Indonesian
geography `U+G0` equals Indonesian language `U+G0`. Each duplicate was executed
once and retained both labels, producing 77 unique browser sessions without
double-counting identical work.

## Run integrity

| Control | Result |
|---|---:|
| Planned sessions accepted | 77/77 |
| Unique prompts repeated exactly seven times | 11/11 |
| Logged-out state verified | 77/77 |
| Incognito state verified | 77/77 |
| Single-turn state verified | 77/77 |
| Completed first answer captured | 77/77 |
| Incognito window closed after capture | 77/77 |
| Protocol validation errors | 0 |
| Total browser attempts | 79 |
| Failed attempts retained | 2 |

Both failures were transient `COMPOSER_NOT_FOUND_AFTER_15S` events. Each failed
window was closed and the same planned session succeeded in a fresh Incognito
window on attempt two. The final Chrome foreground window was non-Incognito.

## Identity resolution

| Signals supplied | Correct target | Interpretation |
|---|---:|---|
| Name (`N`) | 0/7 | Consistently unresolved; unrelated records dominated |
| URL (`U`) | 7/7 | Fully consistent correct clinic |
| Instagram handle (`H`) | 0/7 | Consistently unresolved; no reliable account binding |
| Name + URL | 7/7 | Fully consistent correct clinic |
| Name + handle | 3/7 heuristic | Two aligned clinic matches, one mixed/conflicting match, four unresolved |
| URL + handle | 7/7 | Fully consistent correct clinic |
| Name + URL + handle | 7/7 | Fully consistent correct clinic |

The URL creates a +100 percentage-point recognition lift over either the name
or handle alone. Adding the name or handle to an already supplied URL does not
improve recognition because URL recognition is already 7/7.

### Name-only behavior

All seven name-only answers explicitly said the business could not be clearly
identified. They commonly surfaced `ARSENT` dental materials and sometimes an
unrelated Dental-Studio in Vladivostok. These were generally presented with
caution rather than asserted as the intended clinic, so the result is
**unresolved entity discovery**, not seven hallucinations.

### Social identity behavior

All seven handle-only answers failed to connect `@arsent.dental` to the target
clinic. Name plus handle was unstable:

- Two runs found the correct Arsent Dental business listing and core target
  details.
- Four runs remained unresolved or discussed similarly named alternatives.
- One run produced a mixed identity: it correctly named Arsent Dental and
  Batubulan/Gianyar but associated the account with `+62 813-5896-2542`,
  `Jl. Tukad Pakerisan`, soft/grand-opening claims, and different account
  activity. Those facts disagree with the submitted page's
  `+62 812-3837-4696` and `Jl. Batuyang No. 25` reference.

This is best labeled **social entity misattribution or identity fragmentation**.
The test does not establish the technical root cause.

URL plus handle resolved the clinic 7/7, showing that the URL supplies the
missing identity anchor. In the `N+U+H` condition, answers often ignored the
handle, so correct business recognition must not be misread as proof that the
social account itself was validated.

## Website alignment and volunteered coverage

Counts below aggregate all 56 URL-bearing observations.

| Website-derived field | Volunteered frequency |
|---|---:|
| Correct target entity | 56/56 |
| Business name | 56/56 |
| Gianyar | 56/56 |
| Bali | 55/56 |
| Batubulan | 54/56 |
| Named dentist | 55/56 |
| Exact SIP | 55/56 |
| Core services | 55/56 |
| Published price examples | 55/56 |
| Street address | 46/56 |
| Exact phone number | 38/56 |
| WhatsApp | 36/56 |
| Google Maps wording/link | 9/56 |

The website succeeds at machine-readable business explanation: identity,
professional attribution, license, services, and prices are exceptionally
stable once the URL is provided. Contact/actionability facts are substantially
less stable.

The official Instagram handle appeared 0/14 times in the English and
Indonesian URL-only tests. This is volunteered coverage, not proof that ChatGPT
could never return the handle under a targeted request.

## Geography profile

These are responses under supplied location wording, not proof of business
scale or popularity.

| Indonesian URL condition | Recognition | Dentist / SIP | Services / prices | Exact phone |
|---|---:|---:|---:|---:|
| No location | 7/7 | 7/7 / 7/7 | 7/7 / 7/7 | 7/7 |
| Gianyar | 7/7 | 6/7 / 6/7 | 6/7 / 6/7 | 6/7 |
| Bali | 7/7 | 7/7 / 7/7 | 7/7 / 7/7 | 1/7 |
| Indonesia | 7/7 | 7/7 / 7/7 | 7/7 / 7/7 | 6/7 |

Recognition is fully portable across every location context. The large phone
coverage drop under the Bali wording demonstrates that stable recognition does
not guarantee stable actionability.

## Language portability

| URL with no location | English | Indonesian |
|---|---:|---:|
| Correct recognition | 7/7 | 7/7 |
| Named dentist | 7/7 | 7/7 |
| Exact SIP | 7/7 | 7/7 |
| Services | 7/7 | 7/7 |
| Prices | 7/7 | 7/7 |
| Exact phone | 6/7 | 7/7 |
| WhatsApp | 6/7 | 6/7 |
| Median answer length | 2,384 chars | 2,324 chars |

Core identity and factual coverage are fully portable between English and
Indonesian in this sample. Small contact differences should be treated as
seven-run variance, not a durable language effect, until replicated over time.

## Retrieval and source behavior

Visible autonomous browsing or source UI appeared in 75/77 accepted answers.
Neither of the two prompts without visible browsing evidence was instructed to
browse; both were unresolved `N+H` observations.

An official-site source label (`Arsent Dental` or `arsentdental.com`) appeared
in 55/56 URL-bearing sessions. Name-only citations were dominated by unrelated
labels such as Kapuashulu, Iprim/IPRIM.RU, and Scribd. Handle-only citations
included unrelated or ambiguous labels such as Milkshake and IPRIM.RU.

The accessibility capture retained visible citation labels, but not normalized
destination URLs for every source button. Therefore this run supports
source-label and channel observations, not a complete citation-domain audit.

## Consistency and runtime

- Median accepted-attempt latency: 11.48 seconds
- 95th percentile: 21.65 seconds
- Maximum: 26.89 seconds
- Answer-length range: 669–9,464 characters
- Autonomous browsing observed: 75/77

Answer length is too variable to be a quality score. The analysis uses semantic
field coverage and seven-run distributions instead.

## Diagnostic state

| Dimension | State |
|---|---|
| URL-anchored recognition | Strong and consistent |
| Website factual legibility | Strong and consistent |
| Name-only discovery | Weak; 0/7 correct resolution |
| Handle-only discovery | Weak; 0/7 correct resolution |
| Social identity binding | Weak and occasionally conflicting |
| Geography recognition | Strong across tested wording |
| Language portability | Strong for English and Indonesian |
| Contact/actionability coverage | Moderate and variable |
| Independent authority | Insufficiently established by this run |

No composite score is assigned yet. The evidence does not justify stable
business-type weights, and a single number would hide the decisive difference
between URL-anchored and unanchored discovery.

## Prioritized actions

1. **Unify the public identity graph.** Use the exact `Arsent Dental` name,
   canonical URL, `@arsent.dental`, Batuyang address, and `0812 3837 4696`
   consistently across the website, Instagram bio/posts, Google Business
   Profile, Maps, and directories.
2. **Investigate the conflicting social result.** Search owned and third-party
   profiles for `+62 813-5896-2542` and `Jl. Tukad Pakerisan`. Correct, remove,
   or clearly disambiguate any stale or unrelated association.
3. **Strengthen explicit entity markup.** Verify `Dentist`/`LocalBusiness` and
   `Organization` structured data with canonical name, URL, postal country,
   phone, map identifier, and `sameAs` links to the exact social account.
4. **Make the country explicit.** Add `Indonesia` to the visible postal address
   and structured address instead of requiring inference from Bali, language,
   or telephone formatting.
5. **Build independent local authority.** Earn consistent reviews and relevant
   citations that use the exact clinic name and link to the canonical site.
   This should help name-only discovery outrank unrelated product and Russian
   business records.
6. **Preserve the website's current strengths.** Keep the dentist name, SIP,
   services, prices, address, and booking channel crawlable and consistent;
   these fields drove near-perfect URL-anchored answers.
7. **Repeat the identical benchmark after changes.** Keep templates and
   protocol version fixed so movement can be distinguished from prompt drift.

## Limitations

- Consumer ChatGPT behavior, indexes, UI, and model routing can change.
- Incognito is not neutral: IP location, browser language, time, and platform
  experiments can still affect responses.
- The visible UI did not expose a dependable model identifier.
- The submitted page is an official claim set, not independently verified
  truth.
- `Gianyar` occupies the v1 city slot although it is a regency-level label in
  the visible address hierarchy.
- `Indonesia` was promoted from the preceding seven-run feasibility bootstrap
  because the visible landing-page address does not explicitly state country.
- Literal field counts are deterministic regex observations. Entity resolution
  and the mixed social result were reviewed semantically.
- Citation destinations were not opened or normalized, preserving single-turn
  answer capture but limiting full source attribution.

## Engineering run history

| Run | Audit status | Accepted | Attempts | Purpose/outcome |
|---|---|---:|---:|---|
| v1 | Fail | 1/77 | 13 | Exposed polling-without-delay bug |
| v2 | Fail | 33/77 | 43 | Exposed timing, kernel, clipboard, and proxy issues |
| v3 | Pass | 77/77 | 79 | Hardened production execution |

The failed engineering runs remain in sibling folders; their ledgers and audit
files were not deleted or rewritten.

## Artifacts

- `config.json` — accepted inputs and templates
- `reference.json` — exact-page reference profile and provenance
- `plan.json` — deduplicated round-robin schedule
- `ledger.jsonl` — complete answers and accessibility captures for 79 attempts
- `audit.json` — protocol-integrity result
- `signals.json` — deterministic literal-field patterns
- `analysis.json` — per-prompt counts, source labels, and timing statistics
