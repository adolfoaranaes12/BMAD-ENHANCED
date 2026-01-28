---
description: Estimate user stories using Fibonacci scale with complexity analysis
argument-hint: <story-files> [--velocity N]
allowed-tools: Skill
---

Invoke the estimate-stories skill:

Use Skill tool: `Skill(command="estimate-stories")`

This will execute the story estimation workflow:
1. Load story files
2. Analyze complexity factors (technical, scope, risk, dependencies)
3. Calculate Fibonacci estimates (1, 2, 3, 5, 8, 13, 21)
4. Identify stories needing split (>13 points)
5. Generate estimation report
6. Calculate sprint capacity

The skill will parse $ARGUMENTS for:
- `story-files` - Paths to story files or directory (required)
- `--velocity` - Team velocity for capacity planning (optional)

Output: Estimation report with story points, split recommendations, capacity analysis
