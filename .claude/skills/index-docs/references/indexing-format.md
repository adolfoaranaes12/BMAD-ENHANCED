# Index Structure and Format

Format specifications for documentation and code indexes.

---

## Document Index Format

**File:** `.claude/index/docs-index.json`

```json
{
  "docs/architecture.md": {
    "sections": [
      {
        "title": "Data Models",
        "level": 2,
        "content": "User model represents...",
        "line_start": 45,
        "line_end": 120,
        "keywords": ["user", "model", "database", "schema"],
        "code_refs": ["src/models/user.ts"]
      }
    ],
    "last_updated": "2025-10-28T10:30:00Z",
    "file_size": 15420
  }
}
```

**Fields:**
- `sections`: Array of document sections
- `title`: Section heading text
- `level`: Heading level (1-6)
- `content`: First 200 chars of content
- `line_start/end`: Line number range
- `keywords`: Extracted keywords (lowercase)
- `code_refs`: Links to related code files

---

## Code Index Format

**File:** `.claude/index/code-index.json`

```json
{
  "src/models/user.ts": {
    "exports": ["User", "UserRole", "UserSchema"],
    "imports": ["@prisma/client", "zod"],
    "functions": [
      {
        "name": "createUser",
        "line": 45,
        "signature": "createUser(data: UserInput): Promise<User>"
      }
    ],
    "types": [
      {
        "name": "User",
        "line": 15,
        "kind": "interface"
      }
    ],
    "doc_refs": ["docs/architecture.md#data-models"]
  }
}
```

**Fields:**
- `exports`: Public exports from file
- `imports`: Dependencies
- `functions`: Function definitions with signatures
- `types`: Type/interface definitions
- `doc_refs`: Links to documentation

---

## Search Index Format

**File:** `.claude/index/search.json`

```json
{
  "keywords": {
    "user": {
      "docs": ["docs/architecture.md#45", "docs/api.md#120"],
      "code": ["src/models/user.ts#15", "src/controllers/user.controller.ts#30"]
    },
    "authentication": {
      "docs": ["docs/security.md#10"],
      "code": ["src/middleware/auth.ts#5"]
    }
  },
  "concepts": {
    "Repository Pattern": {
      "definition": "docs/patterns.md#repository-pattern",
      "implementations": ["src/repositories/user.repository.ts"]
    }
  }
}
```

---

## Quick Reference Format

**File:** `.claude/index/quick-ref.md`

```markdown
# Quick Reference

## Data Models

- **User**: `src/models/user.ts:15`
  - Docs: docs/architecture.md#data-models
  - Fields: id, email, password, profile
  - Relations: orders[], sessions[]

- **Order**: `src/models/order.ts:20`
  - Docs: docs/architecture.md#data-models
  - Fields: id, userId, items[], total
  - Relations: user, orderItems[]

## API Endpoints

- **POST /api/auth/signup**: `src/routes/auth/signup.ts:10`
  - Docs: docs/api.md#authentication
  - Request: {email, password}
  - Response: {token, user}

## Patterns

- **Repository Pattern**: docs/patterns.md#repository-pattern
  - Implementations: src/repositories/*.ts
  - Example: UserRepository

## Technologies

- **PostgreSQL**: Database
  - Schema: prisma/schema.prisma
  - Migrations: prisma/migrations/
- **Express**: Web framework
  - Setup: src/app.ts
  - Routes: src/routes/
```

---

## Glossary Format

**File:** `.claude/index/glossary.md`

```markdown
# Glossary

## A

**Authentication**: Process of verifying user identity
- Related: docs/security.md#authentication
- Code: src/middleware/auth.ts

**Authorization**: Process of verifying user permissions
- Related: docs/security.md#authorization
- Code: src/middleware/authorize.ts

## R

**Repository Pattern**: Data access abstraction layer
- Related: docs/patterns.md#repository-pattern
- Implementations: src/repositories/*.ts
- Example: Separates business logic from data access
```

---

## Index Metadata Format

**File:** `.claude/index/metadata.json`

```json
{
  "created_at": "2025-10-28T10:00:00Z",
  "last_updated": "2025-10-28T15:30:00Z",
  "version": "1.0",
  "stats": {
    "docs_indexed": 5,
    "code_files_indexed": 247,
    "sections": 87,
    "keywords": 245,
    "cross_references": 42,
    "code_exports": 156,
    "code_functions": 423
  },
  "config": {
    "docs_path": "docs/",
    "code_path": "src/",
    "include_code": true,
    "max_depth": 3
  }
}
```

---

## File Organization

```
.claude/index/
├── docs-index.json      (Documentation index)
├── code-index.json      (Code index)
├── search.json          (Search structures)
├── quick-ref.md         (Quick reference)
├── glossary.md          (Term glossary)
└── metadata.json        (Index metadata)
```

---

## Usage

**Load document section:**
```javascript
const index = require('./.claude/index/docs-index.json');
const section = index['docs/architecture.md'].sections[0];
console.log(`${section.title} at lines ${section.line_start}-${section.line_end}`);
```

**Search by keyword:**
```javascript
const search = require('./.claude/index/search.json');
const results = search.keywords['user'];
console.log('Found in:', results.docs, results.code);
```

**Quick lookup:**
```bash
# Find User model
grep "User:" .claude/index/quick-ref.md -A 3

# Find authentication docs
grep "authentication" .claude/index/glossary.md -A 2
```
