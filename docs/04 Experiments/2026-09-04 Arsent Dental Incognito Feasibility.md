---
type: experiment
status: complete
created: 2026-09-04
updated: 2026-09-04
tags:
  - artemis
  - experiment
  - computer-use
  - browser
  - feasibility
target_url: https://www.arsentdental.com/
prompt_template: bootstrap-url-en-v1
runs: 7
---

# Arsent Dental Incognito Feasibility

## Objective

Validate whether Computer Use can complete the proposed Artemis bootstrap flow
against logged-out ChatGPT.com in an external Chrome Incognito window.

## Target and prompt

- Target: `https://www.arsentdental.com/`
- Prompt: `What do you know about https://www.arsentdental.com/?`
- Language: English
- Conversation policy: one prompt and one answer
- Isolation policy: a completely new Incognito window for every run
- Repetitions: seven

## Method

For each run:

1. Open a new Chrome Incognito window.
2. Navigate to ChatGPT.com.
3. Confirm the interface is logged out by observing the Log in and Sign up
   controls.
4. Submit the exact canonical prompt.
5. Wait for the first answer to finish.
6. Capture the answer through Chrome's accessibility representation.
7. Close the entire Incognito window.

No follow-up, clarification, regeneration, or browsing instruction was used.

## Feasibility result

**Passed: 7/7 complete runs.**

Computer Use successfully created isolated Incognito sessions, operated
logged-out ChatGPT.com, submitted the prompt, captured the completed answer, and
closed the session after every run.

This environment therefore supports the intended mechanism despite official
documentation warning that Computer Use cannot automate ChatGPT itself. The
result should be treated as environment-specific behavior that may remain
unsupported or change later.

## Reference facts visible on the submitted page

The submitted landing page exposed:

- Business name: Arsent Dental
- Address: Jl. Batuyang No. 25, Batubulan Kangin, Sukawati, Gianyar, Bali
- Dentist: drg. I Made Gde Artha Sentana, S.K.G.
- SIP: MR51042607013475
- Phone and WhatsApp: 0812 3837 4696
- Instagram: `@arsent.dental`
- Google Maps link
- Dental services, estimated durations, and price ranges

These observations came from the submitted page only.

## Seven-run consistency

| Volunteered field or behavior | Frequency | Initial interpretation |
|---|---:|---|
| Correct business name | 7/7 | Fully consistent recognition |
| Batubulan/Sukawati/Gianyar/Bali location chain | 7/7 | Fully consistent local identity |
| Named dentist | 7/7 | Fully consistent person association |
| Exact SIP number | 7/7 | Fully consistent license retrieval |
| Core service categories | 7/7 | Fully consistent service understanding |
| Published price examples | 7/7 | Fully consistent price discovery |
| Exact phone number | 4/7 | Inconsistent exact contact coverage |
| WhatsApp mentioned | 6/7 | Strong but incomplete contact coverage |
| Instagram or `@arsent.dental` volunteered | 0/7 | Social identity was not surfaced natively |
| Submitted website cited | 7/7 | Fully consistent first-party sourcing |
| Answer stated that independent search was performed | 6/7 | Autonomous search occurred without instruction |

The Instagram result is particularly useful: the landing page exposed the
account, but none of the seven open-ended answers volunteered it. The handle is
therefore `page_declared` for later `H` tests while its native URL-only coverage
is `0/7`.

## Stable qualitative themes

Across the answers, ChatGPT consistently characterized Arsent Dental as a small,
personal, dentist-led clinic rather than a large chain. It repeatedly treated
the named dentist, SIP, physical address, published prices, and explanation of
the treatment process as positive trust signals.

The answers also consistently avoided making a strong treatment-quality
recommendation from the first-party website alone. They suggested checking
independent reviews, credentials, equipment, materials, treatment plans, or
follow-up policies before major treatment.

## Important findings

### The low-steering prompt still triggered rich retrieval

The simple question produced substantially more than basic identity. ChatGPT
volunteered location, professional identity, services, prices, contact channels,
trust signals, limitations, and an overall assessment without those fields
being enumerated.

### Autonomous browsing is observable

Six answers explicitly referred to an independent search or independent web
results even though the prompt did not ask ChatGPT to browse. This validates the
decision to record agent-initiated discovery separately from instructed access.

### Volunteered coverage is meaningfully variable

Core identity and service facts were stable, while exact contact details and
social identity were less visible. This supports separate recognition,
volunteered-coverage, and consistency metrics.

### Answer length varies materially

The captured answer text varied from approximately 1,857 to 3,813 characters.
Scoring should compare semantic fields and claims rather than raw response
length.

## Limitations

- The experiment recorded normalized field-level results rather than persisting
  production-ready raw response artifacts.
- Source buttons were visible, but citation URLs were not fully normalized into
  structured source records.
- The experiment did not yet test retries, CAPTCHA handling, network failures,
  or partial generations.
- All runs occurred from the same machine, network, date, and broad time window.
- This tested only the English URL-only bootstrap prompt, not the full 91-session
  matrix.

## Outcome

The proposed Chrome-Incognito mechanism is feasible in the current environment.
Before packaging the workflow as a reusable Codex skill, the next technical
step is reliable raw-answer and citation persistence with an auditable record
for every run.

## Related notes

- [[Experiment Log]]
- [[2026-09-04 Bootstrap URL Runs Use English|Bootstrap URL Runs Use English]]
- [[2026-09-04 Fresh Incognito Session Per Prompt|Fresh Incognito Session Per Prompt]]
- [[2026-09-04 Seven Runs Use Round-Robin Execution|Seven Runs Use Round-Robin Execution]]
- [[2026-09-04 Canonical Prompt Is Open-Ended|Canonical Prompt Is Open-Ended]]

