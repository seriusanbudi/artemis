---
type: experiment
status: complete
created: 2026-09-04
updated: 2026-09-04
tags:
  - artemis
  - experiment
  - agent-glasses
  - comparison
targets:
  - https://www.arsentdental.com/
  - https://www.rover.com/
  - https://supabase.com/
---

# Rover and Supabase Agent Glasses Gap Test

## Verdict

The experiment shows that **Arsent Dental's main website already performs much
closer to the mature benchmarks than its overall visibility initially
suggested**. Its gap is primarily the identity network outside the URL, not the
agent's ability to understand the page after landing on it.

Supabase is the strongest state: name, URL, and social handle independently
resolve the company and yield useful information. Rover also has a strong
identity graph, but its ambiguous name produces a weak one-turn experience:
ChatGPT recognizes the company yet usually asks the user to clarify before
giving a real explanation. Arsent needs its exact URL to achieve reliable
resolution.

## The gap at a glance

| Diagnostic | Arsent Dental | Rover | Supabase |
|---|---:|---:|---:|
| Name resolves correct target | 0/7 | 7/7 | 7/7 |
| Name gives a substantive first answer | 0/7 | 1/7 | 7/7 |
| URL resolves correct target | 7/7 | 7/7 | 7/7 |
| Social handle resolves correct target | 0/7 | 7/7 | 7/7 |
| Name + social resolves correct target | 2 aligned + 1 mixed / 7 | 7/7 | 7/7 |
| URL-bearing conditions resolve target | 56/56 | 49/49 | 28/28 |
| Website's core offering is consistently explained | Strong | Strong | Strong |
| Public identity graph | Fragmented | Strong, but name is ambiguous | Strong and self-sufficient |

The Arsent name-plus-handle denominator is deliberately not reduced to a
simple 3/7: two runs aligned cleanly, one mixed correct and conflicting facts,
and four did not resolve. Treating the mixed observation as a clean success
would hide identity fragmentation.

## What the URL test actually proves

The exact URL is a unique anchor for all three businesses:

- Arsent Dental: the clinic, dentist, SIP, services, and prices appeared in
  55–56 of 56 URL-bearing answers.
- Rover: boarding and house sitting appeared 49/49; dog walking, drop-ins, and
  day care appeared 47/49.
- Supabase: Postgres, Authentication, Data APIs, Edge Functions, Realtime,
  Storage, and open-source positioning appeared 28/28.

This means a small and new business can already match established brands on
**website legibility after URL anchoring**. Popularity is not required for that
layer. What maturity changes is whether the agent can connect other public
clues to the same entity without being handed the URL.

## Three maturity states

### 1. URL-dependent identity — Arsent Dental

The page explains the business well, but the name and Instagram handle do not
reliably lead the agent to it. Search results and external records compete with
the intended identity. The next work is entity consolidation: consistent name,
URL, handle, address, phone, Maps presence, structured data, and independent
citations.

### 2. Recognized but interaction-fragile name — Rover

Rover's URL and social handle are strongly connected, and the company is the
agent's default business interpretation. But “Rover” is inherently ambiguous.
Six of seven native answers chose the correct company while withholding the
actual overview until a hypothetical follow-up. A recognition-only score would
incorrectly call this perfect.

### 3. Self-sufficient identity — Supabase

The bare name yields a detailed and stable category/product explanation without
browsing. URL and handle independently resolve the same company, while retrieval
reinforces the official site. This is the clearest current benchmark for an
agent-ready identity graph.

## Product implications

The scoring system should keep at least four dimensions separate:

1. **Entity recognition** — did the agent select the correct target?
2. **First-answer utility** — did the one allowed answer actually explain the
   business or merely ask for clarification?
3. **Website legibility** — once the URL is supplied, which page-declared facts
   survive consistently?
4. **Cross-surface identity binding** — do name, URL, and social handle
   independently converge on the same entity without conflicts?

Retrieval behavior should remain an observation, not a quality score. Arsent
browsed in 75/77 accepted sessions, Rover in 63/70, and Supabase in 42/49. The
seven Supabase name-only answers were excellent without browsing; browsing
frequency therefore cannot stand in for visibility or answer quality.

Geography must also remain diagnostic rather than a claim of scale. Rover's
Seattle/Washington/United States prompts use page-listed service markets.
Supabase declared no defensible corporate location, and its seven-run bootstrap
found none, so geography was correctly skipped.

## Audit integrity

| Audit | Accepted | Attempts | Status |
|---|---:|---:|---|
| Arsent Dental production v3 | 77/77 | 79 | Pass |
| Rover v1 | 70/70 | 72 | Pass |
| Supabase geography bootstrap | 7/7 | 7 | Pass |
| Supabase v1 | 49/49 | 53 | Pass |

Every accepted observation used a new Chrome Incognito window, logged-out
ChatGPT, one exact prompt, and one completed first answer. All prompts were
repeated seven times in round-robin order. Failed attempts are retained rather
than silently discarded.

## Reports and artifacts

- [Open the visual dashboard](agent-glasses-dashboard.html)
- [Arsent Dental full report](runs/2026-09-04-arsent-dental-v3/report.md)
- [Rover full report](runs/2026-09-04-rover-v1/report.md)
- [Rover protocol audit](runs/2026-09-04-rover-v1/audit.json)
- [Rover raw ledger](runs/2026-09-04-rover-v1/ledger.jsonl)
- [Supabase full report](runs/2026-09-04-supabase-v1/report.md)
- [Supabase protocol audit](runs/2026-09-04-supabase-v1/audit.json)
- [Supabase raw ledger](runs/2026-09-04-supabase-v1/ledger.jsonl)
- [Supabase bootstrap audit](runs/2026-09-04-supabase-v1/bootstrap-audit.json)

## Related notes

- [[2026-09-04 Arsent Dental Full Agent Glasses Audit]]
- [[Scoring Model]]
- [[Identity Signal Combination Matrix]]
- [[Experiment Log]]
