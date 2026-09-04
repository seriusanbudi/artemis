---
type: decision
status: accepted
created: 2026-09-04
updated: 2026-09-04
tags:
  - artemis
  - decision
  - v1
  - prompts
---

# V1 Uses Single-Turn Prompts

## Context

Agent visibility could be tested through isolated prompts or multi-turn customer
journeys. In a multi-turn conversation, earlier messages and answers can steer
the model toward the target business and make later answers appear more
successful than they would be from a clean request.

## Decision

Every scored V1 test will use exactly one prompt and capture exactly one answer.
There will be no follow-up prompt, clarification, correction, regeneration, or
other steering within the scored conversation.

Each prompt begins in a new conversation with no prior conversational context.
Multi-turn journey testing is out of scope for V1.

## Consequences

- Every prompt must contain all information needed for its test case.
- An ambiguous or incomplete answer is scored as returned; the evaluator must
  not ask the agent to clarify.
- "Regenerate" counts as another independent run, not as a continuation of the
  original result.
- Prompt templates must avoid unintentionally disclosing the expected answer.
- The system can compare repeated independent runs without conversation-history
  contamination.

## Related notes

- [[Prompt Test Matrix]]
- [[Product Workflow]]
- [[Scoring Model]]
- [[Decision Log]]

