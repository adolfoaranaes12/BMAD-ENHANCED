---
description: Generate sprint plan from estimated stories using allocation algorithm
argument-hint: <stories-dir> --velocity <N> [--sprint-number N]
allowed-tools: Skill
---

Invoke the sprint-plan skill:

Use Skill tool: `Skill(command="sprint-plan")`

This will execute the sprint planning workflow:
1. Load estimated stories
2. Analyze dependencies
3. Apply allocation algorithm based on velocity
4. Group stories into sprints
5. Balance sprint loads
6. Validate feasibility
7. Generate sprint plan document

The skill will parse $ARGUMENTS for:
- `stories-dir` - Directory containing story files (required)
- `--velocity` - Team velocity in story points (required)
- `--sprint-number` - Starting sprint number (default: 1)
- `--buffer` - Capacity buffer percentage (default: 20%)

Output: Sprint plan file with story allocations, timeline, risk assessment
