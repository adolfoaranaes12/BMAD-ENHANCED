---
description: Break large documents into manageable shards with navigation
argument-hint: "<document-path> [--max-size <KB>]"
allowed-tools: Skill
---

Invoke the shard-document skill:

Use Skill tool with skill="shard-document"

This will execute the document sharding workflow:
1. Analyze document structure and identify logical breakpoints
2. Calculate optimal shard sizes (respecting context window limits)
3. Create shard files with consistent naming convention
4. Generate navigation index and cross-references
5. Validate shard integrity and completeness

The skill will parse $ARGUMENTS for:
- `document-path` - Path to document to shard (required)
- `--max-size` - Maximum shard size in KB (optional, default: 100KB)

Output: Multiple shard files with navigation index at configured location
