# Agent Glasses protocol v1

## Measurement target

Observe logged-out ChatGPT in a fresh Chrome Incognito window. The unit of
measurement is one exact prompt and its first completed answer.

The experiment concerns one target business only. Competitor discovery and
unbranded category prompts are outside v1.

## Reference extraction

Open the submitted landing page directly. Record only claims visible on that
page, including machine-readable data rendered by the page when accessible.
Do not intentionally navigate to internal paths, social pages, Maps, directory
pages, or search results. Links on the page can be recorded without opening
them.

Each reference field needs `value`, `status`, `source_url`, and optional
`evidence`. Allowed status values are `page_declared`, `agent_discovered`,
`ambiguous`, and `unknown`.

## Identity matrix

Use every available non-empty combination:

| ID | Signals |
|---|---|
| N | business name |
| U | exact submitted URL |
| H | primary social handle and platform |
| N+U | name and URL |
| N+H | name and social identity |
| U+H | URL and social identity |
| N+U+H | all three |

Skip combinations containing an unavailable signal. Do not substitute another
kind of clue.

## Geography and language layers

- Geography: `U × {G0, city, province/state, country} × LL`
- Language: `U × G0 × {LL, English}`
- `LL` is the deterministic mainstream market language.
- If `LL` is English, deduplicate it.
- More generally, any exactly identical prompt text is one execution target
  carrying multiple conceptual matrix labels.

For Arsent Dental, the natural Indonesian templates are:

- `Apa yang kamu ketahui tentang {identity}?`
- `Apa yang kamu ketahui tentang {url} di {location}?`

## Seven-run schedule

Generate all eligible unique prompts, then execute one observation per prompt
in round 1, one per prompt in round 2, and so on through round 7. Derived prompts
that depend on bootstrap discovery run in a later stage using the same
round-robin rule.

## Session procedure

For every planned observation:

1. Open a completely new Chrome Incognito window.
2. Navigate to `https://chatgpt.com/`.
3. Verify logged-out UI, normally through visible Log in and Sign up controls.
4. Enter the exact planned prompt without additions.
5. Submit once.
6. Wait for generation to stop.
7. Capture the complete first answer and visible citation/source indicators.
8. Record whether ChatGPT autonomously searched or browsed.
9. Close the entire Incognito window.

Never send a second message or use regenerate.

Human-verification detection must inspect dedicated browser UI outside the
assistant answer. Keywords in generated prose—for example a product name that
contains a verification vendor's name—are not sufficient CAPTCHA evidence.

## Evaluation semantics

- Recognition: the correct target is identified.
- Website alignment: claims agree with the submitted page.
- Volunteered coverage: facts offered without being requested.
- Consistency: frequency and semantic stability across seven observations.
- Signal lift: change as N, U, or H is added.
- Geographic profile: response behavior under each supplied location wording.
- Language portability: recognition and factual stability between LL and English.
- Actionability: the answer enables a public business action such as visiting,
  calling, messaging, booking, or purchasing.
- Source channel: owned web, local presence, social visibility, earned authority,
  or commerce presence.

An omitted field measures volunteered coverage only; it does not prove that the
agent could not retrieve the field under a targeted prompt.

Do not treat the submitted page as independently verified truth. Report answer
differences as disagreement with the website-derived reference.
