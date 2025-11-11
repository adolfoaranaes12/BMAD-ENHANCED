---
description: Create searchable index of documentation for brownfield codebases
argument-hint: "<docs-path> [--format markdown|json]"
allowed-tools: Skill
---

Invoke the index-docs skill:

Use Skill tool with skill="index-docs"

This will execute the documentation indexing workflow:
1. Discover all documentation files in codebase
2. Extract metadata, headers, and cross-references
3. Build searchable index with categorization
4. Generate navigation structure
5. Create index files for easy lookup

The skill will parse $ARGUMENTS for:
- `docs-path` - Path to documentation directory (required)
- `--format` - Index format: markdown or json (optional, default: markdown)

Output: Documentation index files at configured location
