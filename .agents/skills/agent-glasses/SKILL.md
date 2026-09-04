---
name: agent-glasses
description: Audit how logged-out ChatGPT natively identifies and describes one target business from its name, exact URL, social handle, geography, and prompt language. Use when asked to run, resume, validate, or report an Agent Glasses/AEO visibility experiment through fresh Chrome Incognito sessions. Do not use for competitor research, generic SEO advice, logged-in personalization, multi-turn prompting, or API-only model evaluation.
---

# Agent Glasses

Measure the first answer a prospective customer could receive from logged-out
ChatGPT. Treat the agent response as an observation, not ground truth.

## Required tools

Use Computer Use to operate Chrome Incognito and ChatGPT.com. Use shell or
workspace tools only for planning, artifact persistence, validation, and report
generation. Do not replace the consumer UI with an API unless the user asks for
a separately labeled API benchmark.

Read [references/protocol.md](references/protocol.md) before executing an audit.
Read [references/artifact-schema.md](references/artifact-schema.md) before
creating or resuming run artifacts.

## Workflow

1. Accept one exact target URL.
2. Inspect only the supplied landing page to create a website-derived reference
   profile. Do not intentionally crawl another path.
3. Preserve unknown or ambiguous values as unknown. Never invent a signal to
   make the matrix complete.
4. Resolve `N` (business name), `U` (exact submitted URL), `H` (one primary
   social handle), city, province/state, country, and local market language.
5. If `H` or a geographic value is absent from the page, run the seven English
   `U` bootstrap observations. Promote an agent-discovered candidate only when
   it appears in at least 4/7 answers. Record the provenance as
   `agent_discovered`, not `page_declared`.
6. Create `config.json`, then run `scripts/build_plan.py` to produce the unique
   prompt plan. Identical prompt text must execute once and retain every
   applicable matrix label.
7. Execute the plan in round-robin order. Each row is one new Incognito window,
   one logged-out ChatGPT conversation, one exact prompt, and one first answer.
8. Append every attempt to the ledger immediately. Close the entire Incognito
   window after capture, including failed attempts.
9. Run `scripts/audit_ledger.py` after execution. Do not call the audit complete
   while any planned session is missing, duplicated, out of order, non-isolated,
   multi-turn, or missing its raw answer.
10. Evaluate the complete raw answers against the website-derived reference.
    Keep observation, assessment, and score separate.
    For reproducible literal-field counts, create a run-specific `signals.json`
    and use `scripts/summarize_ledger.py`; label its derived classifications as
    heuristics and review them semantically.
11. Produce a human-readable report plus machine-readable artifacts. State all
    protocol deviations and environmental limitations.

## Non-negotiable controls

- Never tell ChatGPT to browse, search, crawl, cite, follow links, or inspect any
  URL other than the exact URL supplied as an identity signal.
- Allow autonomous browsing, but record it as observed behavior.
- Never enumerate desired facts in the experiment prompt.
- Never use follow-ups, clarification, corrections, regeneration, or a second
  message in the scored conversation.
- Never reuse an Incognito window or conversation.
- Run every unique prompt exactly seven times.
- Capture the exact submitted prompt, complete first answer, timestamp, order,
  visible login state, completion state, autonomous browsing evidence, and any
  visible citations.
- Label a stable wrong entity/account as entity misattribution or identity
  fragmentation. Do not automatically label it hallucination.
- Describe location results as responses under supplied location wording, not
  proof of operational footprint, popularity, or market scale.

## Prompt rules

The semantic task is always the natural-language equivalent of:

> What do you know about `{identity signals}`?

The geography form is:

> What do you know about `{URL}` in `{location}`?

The English identity layer uses all available non-empty combinations of `N`,
`U`, and `H`. The geography layer uses `U` in the local market language for no
location, city, province/state, and country. The language layer compares `U`
with no location in the local market language and English.

Use a mainstream commercial/digital language for the accepted market. Do not
default to a heritage language. For Bali, use Indonesian rather than Balinese.

## Recovery

On a browser or generation failure, record the failed attempt and close the
window. Retry the same planned session in a fresh Incognito window, up to two
retries. Keep attempts in the ledger but mark exactly one successful attempt as
the accepted observation. Stop and report a blocker if CAPTCHA, rate limiting,
or platform state prevents completion after the retry budget.

Detect CAPTCHA or human verification from dedicated browser UI such as a
verification heading, challenge checkbox, challenge frame, or Ray ID. Never
classify a run as CAPTCHA solely because those words or a vendor name appear in
the generated answer.

## Output

Store each audit under `docs/04 Experiments/runs/<audit-id>/` with:

- `config.json`
- `reference.json`
- `reference-capture.txt`
- `plan.json`
- `ledger.jsonl`
- `audit.json`
- `signals.json`
- `analysis.json`
- `report.md`

The report must include coverage frequencies, consistency, signal lift,
geography profile, language portability, source-channel observations,
misattributions, protocol deviations, limitations, and prioritized fixes tied
to evidence.
