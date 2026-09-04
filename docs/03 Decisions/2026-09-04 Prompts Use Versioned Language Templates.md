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
  - localization
---

# Prompts Use Versioned Language Templates

## Context

Literal translation can produce unnatural prompts, while regenerating prompt
wording during every cycle introduces an uncontrolled variable. Artemis needs
natural wording without sacrificing historical comparability.

## Decision

Each supported language will use a natural, language-specific prompt template
that is created once, assigned a version, and reused unchanged across monitoring
cycles.

Templates should preserve the same semantic task and output requirements rather
than matching English word-for-word.

## Versioning rules

- Record `template_id`, `template_version`, and language code for every run.
- Do not modify a released template in place.
- Wording changes create a new template version.
- Results from different template versions must be visibly separated in trend
  reporting.
- Validate that all language versions request equivalent information before
  release.

## Consequences

- Prompt wording remains stable across monitoring cycles.
- Local-language prompts can sound natural rather than translated mechanically.
- Adding a language requires a new reviewed template.
- Template changes may create a new benchmark baseline.
- Language-template generation happens before a monitoring cycle, not during
  the seven repeated runs.

## Related notes

- [[Geography and Language Matrix]]
- [[Prompt Test Matrix]]
- [[2026-09-04 V1 Tests Local Language and English|V1 Tests Local Language and English]]
- [[Decision Log]]

