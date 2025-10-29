# Brownfield Skill: Index Documentation and Code

<!-- BMAD Enhanced Brownfield Skill -->
<!-- Create searchable knowledge base from docs and code -->
<!-- Version: 1.0 -->

## Purpose

Create a searchable, structured knowledge base from existing documentation and code. This skill enables fast context lookup during task planning and implementation in brownfield projects.

**Key Innovation:**
- Semantic search capabilities
- Documentation → Code mapping
- Concept extraction and indexing
- Quick reference system

## When to Use This Skill

Use this skill when you need to:
- Enable fast context lookup in large brownfield project
- Create searchable knowledge base from docs
- Map documentation to code implementation
- Build terminology glossary

**Prerequisites:**
- Run `document-project` skill first (or have existing docs)
- Documentation exists in docs/ directory
- Codebase is structured and readable

---

## SEQUENTIAL Task Execution

### Step 0: Load Configuration and Validate

**Actions:**

1. **Load Configuration:**
   ```yaml
   brownfield:
     docsPath: docs/
     codebasePath: src/
     indexLocation: .claude/index/
     includeCode: true
     maxDepth: 3  # Directory depth to scan
   ```

2. **Validate Prerequisites:**
   - Check docs directory exists
   - Verify documentation files present
   - Check index location writable

3. **Check Existing Index:**
   - If index exists, offer to refresh vs rebuild

**Output:**
```
✓ Configuration loaded
✓ Documentation: docs/ (5 files)
✓ Codebase: src/ (247 files)
✓ Index location: .claude/index/
✓ Ready to index
```

---

### Step 1: Index Documentation Files

**Purpose:** Parse and structure documentation content

**Actions:**

1. **Scan Documentation:**
   - Find all .md files in docs/
   - Read each file
   - Extract headings, sections, code blocks

2. **Build Document Index:**
   ```json
   {
     "docs/architecture.md": {
       "sections": [
         {
           "title": "Data Models",
           "level": 2,
           "content": "...",
           "line_start": 45,
           "line_end": 120,
           "keywords": ["user", "model", "database", "schema"]
         }
       ]
     }
   }
   ```

3. **Extract Keywords and Concepts:**
   - Technical terms (API, database, authentication)
   - Domain concepts (user, order, payment)
   - Technology names (Express, Prisma, PostgreSQL)

4. **Build Cross-Reference Map:**
   - Which docs mention which concepts
   - Links between documents

**Output:**
```
✓ Documentation indexed: 5 files
✓ Sections extracted: 87
✓ Keywords identified: 245
✓ Cross-references: 42
```

---

### Step 2: Index Codebase (Optional)

**Purpose:** Map code to documentation

**Actions:**

1. **Scan Key Files:**
   - Models, schemas, types
   - Routes, controllers
   - Services, repositories

2. **Extract Code Elements:**
   ```json
   {
     "src/models/user.ts": {
       "exports": ["User", "UserRole"],
       "imports": ["prisma"],
       "functions": ["createUser", "findByEmail"],
       "line_map": {
         "User": 15,
         "createUser": 45
       }
     }
   }
   ```

3. **Map Code → Docs:**
   - Find mentions of code elements in docs
   - Build bidirectional links

**Output:**
```
✓ Code files indexed: 247
✓ Exports mapped: 156
✓ Functions mapped: 423
✓ Code → Doc links: 89
```

---

### Step 3: Build Searchable Index

**Purpose:** Create fast lookup structures

**Actions:**

1. **Create Search Index:**
   - Keyword → Documents
   - Concept → Sections
   - Code → Documentation

2. **Build Quick Reference:**
   ```markdown
   # Quick Reference

   ## Data Models
   - User: docs/architecture.md#data-models (src/models/user.ts)
   - Order: docs/architecture.md#data-models (src/models/order.ts)

   ## API Endpoints
   - POST /api/auth/signup: docs/architecture.md#api-specs (src/routes/auth/signup.ts)

   ## Patterns
   - Repository Pattern: docs/patterns.md#repository-pattern
   ```

3. **Create Glossary:**
   - Terms and definitions
   - Links to detailed docs

**Output:**
```
✓ Search index created: .claude/index/search.json
✓ Quick reference: .claude/index/quick-ref.md
✓ Glossary: .claude/index/glossary.md
```

---

## Completion Criteria

- [ ] Documentation indexed
- [ ] Code mapped to docs
- [ ] Search structures created
- [ ] Quick reference generated

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-10-28 | Initial indexing skill |

---

**End of Index Docs Skill**
