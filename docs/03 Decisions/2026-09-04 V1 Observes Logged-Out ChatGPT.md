---
type: decision
status: accepted
created: 2026-09-04
updated: 2026-09-04
tags:
  - artemis
  - decision
  - v1
  - codex
---

# V1 Observes Logged-Out ChatGPT

## Context

Artemis could observe a consumer-facing agent, a controlled API, or both. The
product's purpose is to act as agent glasses, so the first version should
prioritize the experience a prospective customer may actually encounter.

The intended implementation is a reusable Codex skill that asks Computer Use to
launch Chrome in Incognito mode, open ChatGPT.com while logged out, and execute
the Artemis workflow.

## Decision

V1 will observe ChatGPT through a fresh, logged-out browser session. It will not
use the OpenAI API as its primary observation environment.

The workflow should be packaged as a Codex skill once this exact interaction
path has been proven feasible and repeatable.

## Platform constraint

According to official OpenAI documentation, Computer Use cannot automate
ChatGPT itself. The intended flow uses ChatGPT.com inside an external Incognito
Chrome window, so an experiment must determine whether that restriction also
prevents Computer Use from submitting prompts and reading responses through
Chrome.

Until the experiment passes, the Computer Use mechanism is an implementation
hypothesis rather than a proven platform capability. Incognito mode provides a
fresh local browser profile for the run, but location, language, time, product
rollout, and network-level signals may still affect results.

## Consequences

- The result represents observable consumer-product behavior rather than a
  controlled model benchmark.
- Browser state, location, language, time, product rollout, and interface
  changes become test variables.
- The skill must capture evidence from the visible response and cited sources.
- Computer Use failures, CAPTCHAs, or product restrictions must be
  reported as test failures rather than low business-visibility scores.
- API testing may be added later as a separate observation mode.

## Sources

- [Skills & Plugins](https://learn.chatgpt.com/docs/skills-and-plugins)
- [Browser](https://learn.chatgpt.com/docs/browser)
- [Computer Use](https://learn.chatgpt.com/docs/computer-use)

## Related notes

- [[Agent Visibility Audit]]
- [[Product Workflow]]
- [[Prompt Test Matrix]]
- [[Experiment Log]]
- [[Decision Log]]
