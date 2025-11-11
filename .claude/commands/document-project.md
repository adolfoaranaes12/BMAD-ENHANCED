---
description: Generate comprehensive project documentation from codebase analysis
argument-hint: "[codebase-path] [--depth quick|standard|comprehensive]"
allowed-tools: Skill
---

Invoke the document-project skill:

Use Skill tool with skill="document-project"

This will execute the project documentation workflow:
1. Analyze codebase structure and patterns
2. Extract architecture, APIs, and component relationships
3. Generate documentation with confidence scoring
4. Create README, architecture docs, and development guides
5. Validate documentation completeness

The skill will parse $ARGUMENTS for:
- `codebase-path` - Path to codebase to document (optional, defaults to current directory)
- `--depth` - Documentation depth: quick, standard, or comprehensive (optional, default: standard)

Output: Comprehensive project documentation at configured location
