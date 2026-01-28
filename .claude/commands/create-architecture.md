---
description: Design comprehensive system architecture from requirements with technology selection and ADRs
argument-hint: <requirements-file> [--type frontend|backend|fullstack] [--complexity simple|medium|complex]
allowed-tools: Skill
---

Invoke the create-architecture skill:

Use Skill tool: `Skill(command="create-architecture")`

This will execute the architecture design workflow:
1. Load and analyze requirements (PRD or epic)
2. Assess complexity and project type
3. Select technology stack with justifications
4. Design architecture patterns and structure
5. Create Architecture Decision Records (ADRs)
6. Map NFRs to architecture
7. Generate architecture document
8. Create architecture diagrams

The skill will parse $ARGUMENTS for:
- `requirements-file` - Path to PRD or epic file (required)
- `--type` - Project type: frontend, backend, fullstack (auto-detect if not specified)
- `--complexity` - Complexity level: simple, medium, complex (auto-assess if not specified)
- `--depth` - Documentation depth: standard, comprehensive (default: standard)

Output: Architecture document at docs/architecture.md with tech stack, patterns, ADRs, diagrams
