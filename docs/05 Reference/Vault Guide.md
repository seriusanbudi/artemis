---
type: reference
status: active
created: 2026-09-04
updated: 2026-09-04
tags:
  - artemis
  - documentation
---

# Vault Guide

## Purpose

This vault is the product memory for Artemis. It should make the current thesis,
evidence, choices, and validation work easy to find without requiring community
plugins.

## Structure

| Area | Purpose |
|---|---|
| `Inbox` | Unprocessed ideas and quick capture |
| `01 Product` | Product vision, flows, requirements, and models |
| `02 Research` | External evidence and customer learning |
| `03 Decisions` | Durable product and technical decisions |
| `04 Experiments` | Hypotheses, test plans, and results |
| `05 Reference` | Shared terminology and operating guidance |
| `Templates` | Reusable note structures |
| `Attachments` | Images, PDFs, and other embedded files |

Numbered folders provide a stable reading order. Links—not folders—should carry
most relationships between ideas.

## Standard properties

Use these properties where applicable:

| Property | Purpose |
|---|---|
| `type` | Note role, such as `research`, `decision`, or `experiment` |
| `status` | Lifecycle state |
| `created` | Creation date in `YYYY-MM-DD` format |
| `updated` | Last meaningful revision date |
| `tags` | Broad topics used across note types |
| `aliases` | Alternative terms or product names |

Recommended statuses:

- Product notes: `draft`, `active`, `deprecated`
- Decisions: `proposed`, `accepted`, `rejected`, `superseded`
- Experiments: `planned`, `running`, `complete`, `abandoned`
- Research: `planned`, `active`, `complete`, `stale`

## Writing conventions

- Give each note one clear purpose.
- Link the first meaningful mention of another concept using an Obsidian
  wikilink, for example `[[Home]]`.
- Record sources next to the claims they support.
- Separate observations, interpretations, and decisions.
- Put durable conclusions in product or decision notes rather than leaving them
  only in research notes.
- Update `updated` after meaningful changes, not minor formatting edits.
- Prefer descriptive titles over identifiers. Decision and experiment notes may
  add a date prefix when chronology matters.

## Workflow

1. Capture an idea in [[Inbox]].
2. Convert it into a product, research, decision, or experiment note.
3. Add relevant links in both the note and its area index.
4. Record evidence before drawing conclusions.
5. Update affected product notes after a decision is accepted.
6. Keep superseded decisions for historical context.

## Obsidian setup

Open the `docs` directory as a vault. Enable the core **Templates** plugin and
set its folder to `Templates` if Obsidian does not load the included setting
automatically. New notes and attachments are configured to go to `Inbox` and
`Attachments` respectively.

Transient workspace state and local trash are excluded from version control;
portable vault settings may remain tracked.
