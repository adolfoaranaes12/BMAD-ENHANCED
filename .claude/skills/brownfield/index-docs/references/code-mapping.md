# Code-to-Documentation Mapping Strategies

Strategies for mapping code elements to documentation and vice versa.

---

## Mapping Approaches

### 1. Name-Based Mapping

**Strategy:** Match code identifiers with documentation mentions

**Example:**
```typescript
// Code: src/models/user.ts
export interface User {
  id: string;
  email: string;
}

// Documentation: docs/architecture.md
# Data Models
## User
The User model represents...
```

**Mapping:**
- Code identifier: `User`
- Doc mention: "User model" in docs/architecture.md#data-models
- **Link:** `src/models/user.ts:User` → `docs/architecture.md#user`

### 2. File Path Mapping

**Strategy:** Map code file paths to documentation sections

**Pattern:**
```
Code Structure          Documentation Section
----------------        --------------------
src/models/           → docs/architecture.md#data-models
src/routes/           → docs/api.md#endpoints
src/services/         → docs/architecture.md#business-logic
src/middleware/       → docs/architecture.md#middleware
```

### 3. Comment-Based Mapping

**Strategy:** Extract documentation links from code comments

**Example:**
```typescript
/**
 * User repository for database operations
 * @see docs/patterns.md#repository-pattern
 * @see docs/architecture.md#data-access-layer
 */
export class UserRepository {
  // ...
}
```

**Extraction:**
- Parse `@see` tags
- Extract documentation references
- Build bidirectional links

---

## Mapping Techniques

### Technique 1: Export Analysis

**Goal:** Map all public exports to documentation

**Process:**
1. Scan code files for exports
2. Search documentation for mentions
3. Create mapping entries

**Example:**
```typescript
// src/models/user.ts
export { User, UserRole, UserSchema };

// Generates mappings:
{
  "User": ["docs/architecture.md#user"],
  "UserRole": ["docs/architecture.md#user-roles"],
  "UserSchema": ["docs/api.md#validation"]
}
```

### Technique 2: Function Signature Mapping

**Goal:** Map API functions to documentation

**Process:**
1. Extract function signatures
2. Match with API documentation
3. Link parameters and return types

**Example:**
```typescript
// Code
export async function createUser(data: UserInput): Promise<User>

// Documentation: docs/api.md
# POST /api/users
Creates a new user
- Request: UserInput
- Response: User

// Mapping:
{
  "function": "createUser",
  "docs": "docs/api.md#post-apiusers",
  "params": { "data": "UserInput" },
  "return": "User"
}
```

### Technique 3: Type/Interface Mapping

**Goal:** Map type definitions to data model docs

**Process:**
1. Extract type/interface definitions
2. Find data model documentation
3. Map fields to documentation

**Example:**
```typescript
// Code
interface User {
  id: string;
  email: string;
  profile: UserProfile;
}

// Documentation: docs/architecture.md
# User Model
- id (string): Unique identifier
- email (string): User email address
- profile (UserProfile): User profile data

// Mapping:
{
  "type": "User",
  "docs": "docs/architecture.md#user-model",
  "fields": {
    "id": "docs/architecture.md#user-model:id",
    "email": "docs/architecture.md#user-model:email",
    "profile": "docs/architecture.md#user-model:profile"
  }
}
```

---

## Bidirectional Linking

### Code → Documentation

**Use case:** "Where is this code documented?"

**Query:**
```javascript
const codeIndex = require('./.claude/index/code-index.json');
const userModel = codeIndex['src/models/user.ts'];
console.log('Documented at:', userModel.doc_refs);
// Output: ["docs/architecture.md#data-models"]
```

### Documentation → Code

**Use case:** "Where is this implemented?"

**Query:**
```javascript
const docsIndex = require('./.claude/index/docs-index.json');
const section = docsIndex['docs/architecture.md'].sections
  .find(s => s.title === 'Data Models');
console.log('Implemented in:', section.code_refs);
// Output: ["src/models/user.ts", "src/models/order.ts"]
```

---

## Mapping Patterns by File Type

### Models/Schemas

**Pattern:**
```
src/models/*.ts      → docs/architecture.md#data-models
src/schemas/*.ts     → docs/api.md#validation
prisma/schema.prisma → docs/database.md#schema
```

### Routes/Controllers

**Pattern:**
```
src/routes/*.ts      → docs/api.md#endpoints
src/controllers/*.ts → docs/api.md#endpoints
```

### Services

**Pattern:**
```
src/services/*.ts    → docs/architecture.md#business-logic
```

### Middleware

**Pattern:**
```
src/middleware/*.ts  → docs/architecture.md#middleware
```

### Utilities

**Pattern:**
```
src/utils/*.ts       → docs/utilities.md
src/helpers/*.ts     → docs/utilities.md
```

---

## Handling Ambiguity

### Problem: Multiple Code Files for One Concept

**Example:**
```
User concept implemented across:
- src/models/user.ts (data model)
- src/controllers/user.controller.ts (API handlers)
- src/services/user.service.ts (business logic)
```

**Solution:** Map all to same doc section, differentiate by role
```json
{
  "User": {
    "docs": "docs/architecture.md#user",
    "implementations": {
      "model": "src/models/user.ts",
      "controller": "src/controllers/user.controller.ts",
      "service": "src/services/user.service.ts"
    }
  }
}
```

### Problem: One Code File Covers Multiple Concepts

**Example:**
```typescript
// src/models/index.ts exports many models
export { User, Order, Product, Category };
```

**Solution:** Create granular mappings
```json
{
  "src/models/index.ts": {
    "exports": {
      "User": "docs/architecture.md#user",
      "Order": "docs/architecture.md#order",
      "Product": "docs/architecture.md#product",
      "Category": "docs/architecture.md#category"
    }
  }
}
```

---

## Validation

**Check mapping quality:**

1. **Coverage:** Are all exports mapped?
2. **Accuracy:** Do links point to correct docs?
3. **Completeness:** Are all docs linked to code?
4. **Freshness:** Are mappings up to date?

**Validation queries:**
```bash
# Find unmapped exports
# (exports that don't appear in any doc)

# Find undocumented code
# (code files with no doc_refs)

# Find broken links
# (doc_refs pointing to non-existent docs)
```

---

## Maintenance

**When to update mappings:**
- New code files added
- Code files renamed/moved
- Documentation restructured
- New exports added
- API changes

**Update strategies:**
- **Incremental:** Update only changed files
- **Full refresh:** Re-map everything (slower but thorough)

**Automation:**
```bash
# Watch for code changes
# Auto-update mappings when files change

# Periodic validation
# Weekly check for broken links
```

---

## Best Practices

1. **Be selective** - Map key files, not everything
2. **Use consistent naming** - Match code and doc terminology
3. **Validate regularly** - Check for broken links
4. **Document patterns** - Note file → doc mapping conventions
5. **Keep fresh** - Update when code or docs change

---

## Tools and Techniques

### Automated Extraction

**Code parsing:**
- Use TypeScript compiler API
- Extract exports, types, functions
- Generate mapping entries

**Documentation parsing:**
- Parse markdown structure
- Extract headings and code blocks
- Build keyword index

### Manual Enhancement

- Add `@see` tags to code comments
- Add file path references in docs
- Maintain mapping overrides file

### Validation Tools

- Link checker for doc references
- Coverage analyzer for unmapped code
- Freshness checker for outdated mappings
