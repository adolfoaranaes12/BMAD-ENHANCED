---
description: Refine user story for clarity, completeness, and INVEST criteria compliance
argument-hint: <story-file> [--focus <area>]
allowed-tools: Skill
---

Invoke the refine-story skill:

Use Skill tool: `Skill(command="refine-story")`

This will execute the story refinement workflow:
1. Load story file
2. Assess against INVEST criteria:
   - Independent
   - Negotiable
   - Valuable
   - Estimable
   - Small
   - Testable
3. Identify gaps and ambiguities
4. Enhance acceptance criteria
5. Add clarifying details
6. Update story file
7. Generate refinement report

The skill will parse $ARGUMENTS for:
- `story-file` - Path to story file (required)
- `--focus` - Focus area: acceptance-criteria, testability, clarity, all (default: all)

Output: Refined story file, refinement report with improvements made
