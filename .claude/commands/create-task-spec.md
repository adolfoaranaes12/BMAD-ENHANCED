---
description: Create hyper-detailed task specifications with embedded context for implementation
argument-hint: <requirement> [--priority P0|P1|P2|P3]
allowed-tools: Skill
---

Invoke the create-task-spec skill:

Use Skill tool: `Skill(command="create-task-spec")`

This will execute the task specification creation workflow:
1. Load configuration and validate prerequisites
2. Gather requirements and context
3. Extract architecture context with source references
4. Analyze components (data models, APIs, UI)
5. Break down into sequential tasks
6. Create specification file
7. Present for user approval

The skill will parse $ARGUMENTS for:
- `requirement` - Feature or requirement to implement (required)
- `--priority` - Priority level: P0 (critical), P1 (high), P2 (normal), P3 (low)

Output: Task specification file at configured location with embedded context
