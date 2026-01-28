---
description: Break down epic into user stories with dependency analysis
argument-hint: <epic-file> [--max-stories N]
allowed-tools: Skill
---

Invoke the breakdown-epic skill:

Use Skill tool: `Skill(command="breakdown-epic")`

This will execute the epic breakdown workflow:
1. Load and analyze epic requirements
2. Identify major features and capabilities
3. Generate user stories following INVEST criteria
4. Analyze dependencies between stories
5. Prioritize using MoSCoW method
6. Create story files
7. Generate breakdown summary

The skill will parse $ARGUMENTS for:
- `epic-file` - Path to epic file (required)
- `--max-stories` - Maximum number of stories to generate (default: auto)

Output: User story files, dependency graph, breakdown summary report
