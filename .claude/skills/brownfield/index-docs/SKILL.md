---
name: index-docs
description: Create searchable knowledge base from existing documentation and code for fast context lookup in brownfield projects
---

# Index Documentation and Code Skill

## Purpose

Create a searchable, structured knowledge base from existing documentation and codebase. This enables fast context lookup during task planning and implementation in brownfield projects through semantic search, documentation-to-code mapping, and quick reference systems.

**Core Principle:** In brownfield projects, context discovery is the bottleneck—indexing eliminates repeated searching.

## Prerequisites

- Existing documentation in `docs/` directory
- Structured, readable codebase
- Write access to `.claude/index/` location
- Optional: `document-project` skill completed first

---

## Workflow

### 1. Load Configuration and Validate

**Check prerequisites and configuration:**

```yaml
# .claude/config.yaml
brownfield:
  docsPath: docs/
  codebasePath: src/
  indexLocation: .claude/index/
  includeCode: true
  maxDepth: 3
```

**Validate:**
- Documentation directory exists with files
- Index location is writable
- Check if index exists (offer refresh vs rebuild)

---

### 2. Index Documentation

**Parse and structure documentation content:**

1. **Scan documentation files** (.md files in docs/)
2. **Extract structure:**
   - Headings and sections
   - Code blocks and examples
   - Keywords and concepts (API names, domain terms, technologies)
3. **Build document index** with sections, keywords, line numbers
4. **Create cross-references** between documents

**Output:**
```
✓ Documentation indexed: 5 files
✓ Sections extracted: 87
✓ Keywords identified: 245
✓ Cross-references: 42
```

**See:** `references/indexing-format.md` for index structure details

---

### 3. Index Codebase (Optional)

**Map code to documentation:**

1. **Scan key code files:**
   - Models, schemas, types
   - Routes, controllers, services
2. **Extract code elements:**
   - Exports, imports, functions
   - Map to line numbers
3. **Build code-to-docs mapping:**
   - Find code mentions in docs
   - Create bidirectional links

**Output:**
```
✓ Code files indexed: 247
✓ Exports mapped: 156
✓ Functions mapped: 423
✓ Code → Doc links: 89
```

**See:** `references/code-mapping.md` for mapping strategies

---

### 4. Build Searchable Index

**Create fast lookup structures:**

1. **Create search index:**
   - Keyword → Documents
   - Concept → Sections
   - Code → Documentation
2. **Generate quick reference:**
   - Data models with file locations
   - API endpoints with docs links
   - Patterns and where documented
3. **Create glossary:**
   - Terms and definitions
   - Links to detailed documentation

**Output Files:**
- `.claude/index/search.json` - Searchable index
- `.claude/index/quick-ref.md` - Quick reference guide
- `.claude/index/glossary.md` - Term glossary

---

## Using the Index

**Quick searches:**
```bash
# Find documentation about User model
grep -r "User" .claude/index/search.json

# Look up API endpoint
cat .claude/index/quick-ref.md | grep "/api/auth"

# Find term definition
cat .claude/index/glossary.md | grep -A 3 "Repository Pattern"
```

**Integration with other skills:**
- `create-task-spec` loads relevant docs from index
- `implement-feature` looks up patterns from quick ref
- `document-project` can refresh/update index

---

## Index Maintenance

**When to refresh:**
- Documentation updated significantly
- New code modules added
- Architecture changes
- Quarterly maintenance

**Refresh vs Rebuild:**
- **Refresh:** Update existing index (faster, preserves custom entries)
- **Rebuild:** Full re-index (slower, clean slate)

**Command:**
```bash
# Refresh index
@alex *index-docs --refresh

# Full rebuild
@alex *index-docs --rebuild
```

---

## Best Practices

1. **Index early** - Do this before starting implementation work
2. **Keep docs updated** - Refresh index when docs change
3. **Use quick ref** - Faster than searching full docs
4. **Maintain glossary** - Add project-specific terms
5. **Include code selectively** - Index key files, not everything

---

## Reference Files

- `references/indexing-format.md` - Index structure and format
- `references/code-mapping.md` - Code-to-docs mapping strategies

---

## When to Escalate

- Documentation is sparse or missing (run `document-project` first)
- Codebase structure is unclear or chaotic
- Index becomes too large (>100MB)
- Search performance degrades

---

*Part of BMAD Enhanced Brownfield Suite*
