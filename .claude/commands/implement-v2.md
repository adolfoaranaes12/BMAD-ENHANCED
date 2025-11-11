---
description: Implement feature with V2 intelligent routing and TDD workflow
argument-hint: "<task-spec-file> [--mode standard|tdd|fast] [--subtask <id>]"
allowed-tools: Skill
---

Invoke the implement-v2 skill:

Use Skill tool with skill="implement-v2"

This will execute the V2 implementation workflow:
1. Load task specification and assess complexity
2. Route to appropriate implementation strategy
3. Execute TDD workflow (Red-Green-Refactor)
4. Apply refactoring patterns for quality
5. Validate against acceptance criteria

The skill will parse $ARGUMENTS for:
- `task-spec-file` - Path to task specification file (required)
- `--mode` - Implementation mode: standard, tdd, or fast (optional, default: standard)
- `--subtask` - Specific subtask ID to implement (optional)

Output: Implemented feature with comprehensive tests and refactoring applied
