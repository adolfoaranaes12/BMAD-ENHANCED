# Index Documentation Templates and Output Formats

All output formats, examples, and templates for the index-docs skill.

---

## Step 1: Load Configuration and Validate Output

**Complete Output Format:**
```
✓ Configuration loaded from .claude/config.yaml
✓ Documentation path: docs/ (exists, 5 files found)
✓ Codebase path: src/ (exists, 247 files found)
✓ Index location: .claude/index/ (writable)
✓ Include code: Yes
✓ Max depth: 3 levels
✓ Existing index found: Yes (last updated: 2025-10-15)
  → Option: [R]efresh existing index | [B]uild from scratch
✓ Ready to index
✓ Duration: 67ms
```

**Example Without Existing Index:**
```
✓ Configuration loaded from .claude/config.yaml
✓ Documentation path: docs/ (exists, 12 files found)
✓ Codebase path: src/ (exists, 389 files found)
✓ Index location: .claude/index/ (writable, creating directory)
✓ Include code: Yes
✓ Max depth: 3 levels
✓ No existing index found
✓ Will build new index from scratch
✓ Ready to index
✓ Duration: 54ms
```

**Error Case Example:**
```
✗ Documentation path not found: docs/
✗ Cannot proceed without documentation
! Halting - Run document-project skill first to generate documentation
```

---

## Step 2: Index Documentation Output

**Complete Output Format:**
```
✓ Documentation indexed: 5 files
✓ Files processed:
  ├─ docs/architecture.md (87 sections, 245 keywords)
  ├─ docs/api-reference.md (124 sections, 189 keywords)
  ├─ docs/data-models.md (45 sections, 167 keywords)
  ├─ docs/patterns.md (32 sections, 98 keywords)
  └─ docs/standards.md (28 sections, 76 keywords)
✓ Total sections extracted: 316
✓ Total keywords identified: 775
✓ Cross-references created: 42
✓ Duration: 1.2s
```

**Detailed Indexing Example:**
```
✓ Indexing docs/architecture.md...
  ├─ Sections extracted: 87
  │   ├─ # System Architecture (Level 1)
  │   ├─ ## Frontend Architecture (Level 2)
  │   ├─ ### React Component Structure (Level 3)
  │   ├─ ## Backend Architecture (Level 2)
  │   └─ [... 83 more sections]
  ├─ Keywords identified: 245
  │   ├─ Technical: React, Redux, Express, PostgreSQL, Docker
  │   ├─ Domain: User, Order, Payment, Inventory
  │   ├─ Patterns: MVC, Repository, Factory, Singleton
  │   └─ APIs: /api/auth, /api/orders, /api/payments
  ├─ Code blocks: 12 examples
  ├─ Cross-references: 8 links
  │   ├─ → data-models.md (User schema)
  │   ├─ → api-reference.md (Auth endpoints)
  │   └─ [... 6 more links]
✓ File indexed in 287ms

✓ Building cross-reference map...
  ├─ architecture.md ↔ data-models.md (12 links)
  ├─ api-reference.md ↔ data-models.md (18 links)
  ├─ architecture.md ↔ patterns.md (7 links)
  └─ [... 39 more cross-references]
✓ Cross-reference map complete
```

**Index Structure Created:**
```json
{
  "documents": [
    {
      "file": "docs/architecture.md",
      "title": "System Architecture",
      "sections": [
        {
          "heading": "Frontend Architecture",
          "level": 2,
          "lineStart": 45,
          "lineEnd": 123,
          "keywords": ["React", "Redux", "Component", "State Management"],
          "codeBlocks": [
            {
              "language": "javascript",
              "lineStart": 67,
              "lineEnd": 89,
              "content": "// React component example..."
            }
          ]
        }
      ],
      "crossReferences": [
        {
          "targetFile": "data-models.md",
          "targetSection": "User Model",
          "context": "References User schema for authentication"
        }
      ]
    }
  ],
  "keywords": {
    "React": ["docs/architecture.md:45", "docs/patterns.md:23"],
    "User": ["docs/data-models.md:12", "docs/api-reference.md:67"]
  }
}
```

---

## Step 3: Index Codebase Output

**Complete Output Format:**
```
✓ Code files indexed: 247 files
✓ File types processed:
  ├─ TypeScript: 189 files
  ├─ JavaScript: 34 files
  ├─ JSON (schemas): 12 files
  └─ SQL (migrations): 12 files
✓ Code elements extracted:
  ├─ Exports: 156 (classes, functions, constants)
  ├─ Functions: 423 (public functions)
  ├─ Types/Interfaces: 89 (TypeScript types)
  └─ Database models: 24 (Prisma models)
✓ Code → Documentation links: 89 mappings
✓ Duration: 3.4s
```

**Detailed Code Indexing Example:**
```
✓ Indexing src/models/User.ts...
  ├─ Exports found: 3
  │   ├─ class User (line 12)
  │   ├─ interface UserAttributes (line 5)
  │   └─ const UserSchema (line 67)
  ├─ Functions found: 8
  │   ├─ validateEmail (line 34)
  │   ├─ hashPassword (line 45)
  │   ├─ comparePassword (line 56)
  │   └─ [... 5 more functions]
  ├─ Imports from: 5 files
  │   ├─ ../database/connection
  │   ├─ ../utils/validation
  │   └─ [... 3 more imports]
  ├─ Documentation references: 2 found
  │   ├─ Mentioned in: docs/data-models.md:45
  │   └─ Mentioned in: docs/api-reference.md:123
✓ File indexed in 14ms

✓ Building code-to-docs mapping...
  ├─ User model → docs/data-models.md (line 45)
  ├─ Order model → docs/data-models.md (line 156)
  ├─ POST /api/auth → docs/api-reference.md (line 67)
  └─ [... 86 more mappings]
✓ Code-to-docs mapping complete (89 links)
```

**Code Index Structure:**
```json
{
  "codeFiles": [
    {
      "file": "src/models/User.ts",
      "exports": [
        {
          "name": "User",
          "type": "class",
          "line": 12,
          "signature": "class User { id: string; email: string; ... }"
        },
        {
          "name": "UserAttributes",
          "type": "interface",
          "line": 5
        }
      ],
      "functions": [
        {
          "name": "validateEmail",
          "line": 34,
          "params": ["email: string"],
          "returns": "boolean"
        }
      ],
      "documentationLinks": [
        {
          "docFile": "docs/data-models.md",
          "section": "User Model",
          "line": 45
        }
      ]
    }
  ],
  "codeToDocsMap": {
    "src/models/User.ts": ["docs/data-models.md:45", "docs/api-reference.md:123"],
    "src/models/Order.ts": ["docs/data-models.md:156"]
  }
}
```

---

## Step 4: Build Searchable Index Output

**Complete Output Format:**
```
✓ Searchable index built
✓ Output files created:
  ├─ .claude/index/search.json (127 KB)
  ├─ .claude/index/quick-ref.md (34 KB)
  └─ .claude/index/glossary.md (12 KB)
✓ Search index statistics:
  ├─ Keywords: 775 unique terms
  ├─ Documents: 5 files
  ├─ Code files: 247 files
  ├─ Total references: 864 links
✓ Quick reference sections: 8
  ├─ Data Models (24 models)
  ├─ API Endpoints (47 endpoints)
  ├─ Patterns (12 patterns)
  └─ [... 5 more sections]
✓ Glossary terms: 156 definitions
✓ Duration: 456ms
```

---

## Generated Index Files

### search.json Format

**Complete Search Index Structure:**
```json
{
  "version": "1.0",
  "created": "2025-10-30T14:32:15Z",
  "project": "MyApp",
  "statistics": {
    "totalDocuments": 5,
    "totalSections": 316,
    "totalKeywords": 775,
    "totalCodeFiles": 247,
    "totalCrossReferences": 131
  },
  "documents": [
    {
      "id": "doc-001",
      "file": "docs/architecture.md",
      "title": "System Architecture",
      "summary": "High-level overview of system architecture including frontend, backend, and database layers",
      "sections": [
        {
          "id": "sec-001",
          "heading": "Frontend Architecture",
          "level": 2,
          "lineStart": 45,
          "lineEnd": 123,
          "content": "The frontend is built using React with Redux for state management...",
          "keywords": ["React", "Redux", "Frontend", "Components", "State Management"],
          "codeReferences": [
            "src/components/App.tsx",
            "src/store/index.ts"
          ]
        }
      ],
      "keywords": ["Architecture", "System Design", "React", "Express", "PostgreSQL"],
      "crossReferences": [
        {
          "targetDoc": "doc-002",
          "targetSection": "sec-045",
          "relationship": "references",
          "context": "User model definition"
        }
      ]
    }
  ],
  "keywords": {
    "React": {
      "category": "technology",
      "references": [
        { "doc": "doc-001", "section": "sec-001", "line": 45 },
        { "doc": "doc-004", "section": "sec-089", "line": 23 }
      ]
    },
    "User": {
      "category": "domain",
      "references": [
        { "doc": "doc-002", "section": "sec-045", "line": 12 },
        { "code": "src/models/User.ts", "line": 12 }
      ]
    }
  },
  "codeIndex": {
    "src/models/User.ts": {
      "type": "model",
      "exports": ["User", "UserAttributes", "UserSchema"],
      "functions": ["validateEmail", "hashPassword", "comparePassword"],
      "documentationReferences": [
        { "doc": "doc-002", "section": "sec-045", "line": 45 }
      ]
    }
  },
  "quickLookup": {
    "dataModels": {
      "User": {
        "file": "src/models/User.ts",
        "line": 12,
        "docs": "docs/data-models.md:45"
      },
      "Order": {
        "file": "src/models/Order.ts",
        "line": 8,
        "docs": "docs/data-models.md:156"
      }
    },
    "apiEndpoints": {
      "/api/auth/login": {
        "file": "src/routes/auth.ts",
        "line": 34,
        "docs": "docs/api-reference.md:67",
        "method": "POST"
      }
    }
  }
}
```

---

### quick-ref.md Format

**Complete Quick Reference Document:**
```markdown
# Quick Reference Guide

*Generated: 2025-10-30 | Index Version: 1.0*

---

## Data Models

### User Model
**File:** `src/models/User.ts:12`
**Documentation:** `docs/data-models.md:45`

**Attributes:**
- id: string (UUID)
- email: string (unique)
- passwordHash: string
- status: 'active' | 'inactive' | 'pending'
- createdAt: Date

**Key Functions:**
- `validateEmail(email)` - Email format validation
- `hashPassword(password)` - Bcrypt password hashing
- `comparePassword(input, hash)` - Password verification

**Related:**
- Used in: Authentication endpoints
- References: Session model, Token model

---

### Order Model
**File:** `src/models/Order.ts:8`
**Documentation:** `docs/data-models.md:156`

**Attributes:**
- id: string (UUID)
- userId: string (foreign key → User)
- status: 'pending' | 'paid' | 'shipped' | 'completed'
- total: number
- items: OrderItem[]

**Key Functions:**
- `calculateTotal()` - Calculate order total
- `updateStatus(newStatus)` - Update order status
- `addItem(item)` - Add item to order

**Related:**
- Used in: Order endpoints, Payment processing
- References: User model, Product model, OrderItem model

---

## API Endpoints

### Authentication

#### POST /api/auth/login
**File:** `src/routes/auth.ts:34`
**Documentation:** `docs/api-reference.md:67`

**Request:**
```json
{
  "email": "user@example.com",
  "password": "SecurePass123!"
}
```

**Response (200):**
```json
{
  "user": { "id": "...", "email": "..." },
  "token": "eyJhbGciOiJIUzI1NiIs..."
}
```

**Authentication:** Public endpoint
**Rate Limit:** 5 requests per minute per IP

---

#### POST /api/auth/signup
**File:** `src/routes/auth.ts:89`
**Documentation:** `docs/api-reference.md:123`

**Request:**
```json
{
  "email": "user@example.com",
  "password": "SecurePass123!"
}
```

**Response (201):**
```json
{
  "user": { "id": "...", "email": "...", "status": "pending" },
  "message": "Confirmation email sent"
}
```

**Authentication:** Public endpoint
**Rate Limit:** 3 requests per hour per IP

---

### Orders

#### GET /api/orders
**File:** `src/routes/orders.ts:12`
**Documentation:** `docs/api-reference.md:234`

**Query Parameters:**
- `status` (optional): Filter by status
- `page` (optional): Page number (default: 1)
- `limit` (optional): Items per page (default: 20)

**Response (200):**
```json
{
  "orders": [...],
  "pagination": { "page": 1, "totalPages": 5, "totalItems": 87 }
}
```

**Authentication:** Required (JWT token)

---

## Design Patterns

### Repository Pattern
**Documentation:** `docs/patterns.md:23`
**Implementation:** `src/repositories/*.ts`

**Purpose:** Abstracts data access logic from business logic

**Example:**
```typescript
// src/repositories/UserRepository.ts
class UserRepository {
  async findById(id: string): Promise<User | null> {
    return await db.user.findUnique({ where: { id } });
  }

  async create(data: UserAttributes): Promise<User> {
    return await db.user.create({ data });
  }
}
```

**Used in:**
- User service (`src/services/UserService.ts`)
- Order service (`src/services/OrderService.ts`)

---

### Factory Pattern
**Documentation:** `docs/patterns.md:67`
**Implementation:** `src/factories/*.ts`

**Purpose:** Create objects without specifying exact class

**Example:**
```typescript
// src/factories/NotificationFactory.ts
class NotificationFactory {
  static create(type: 'email' | 'sms'): INotificationService {
    if (type === 'email') return new EmailService();
    if (type === 'sms') return new SMSService();
    throw new Error('Unknown notification type');
  }
}
```

**Used in:**
- Notification system (`src/services/NotificationService.ts`)

---

## Configuration

### Environment Variables
**Documentation:** `docs/standards.md:45`
**File:** `.env.example`

**Database:**
- `DATABASE_URL` - PostgreSQL connection string
- `DATABASE_POOL_SIZE` - Connection pool size (default: 10)

**Authentication:**
- `JWT_SECRET` - JWT signing secret (required)
- `JWT_EXPIRY` - Token expiration time (default: '24h')

**Email:**
- `SENDGRID_API_KEY` - SendGrid API key
- `EMAIL_FROM` - Default sender email

---

## Testing

### Test Structure
**Documentation:** `docs/standards.md:123`

**Unit Tests:** `src/**/*.test.ts`
**Integration Tests:** `src/**/*.integration.test.ts`
**E2E Tests:** `tests/e2e/**/*.spec.ts`

**Running Tests:**
```bash
npm run test           # All tests
npm run test:unit      # Unit tests only
npm run test:integration # Integration tests
npm run test:e2e       # E2E tests
```

---

## Common Tasks

### Adding a New Model

1. Create model file: `src/models/NewModel.ts`
2. Define schema in Prisma: `prisma/schema.prisma`
3. Run migration: `npm run db:migrate`
4. Create repository: `src/repositories/NewModelRepository.ts`
5. Update documentation: `docs/data-models.md`
6. Refresh index: Run `index-docs --refresh`

**References:**
- Pattern: Repository Pattern (`docs/patterns.md:23`)
- Example: User Model (`src/models/User.ts`)

---

### Adding a New API Endpoint

1. Create route handler: `src/routes/newRoute.ts`
2. Add validation schema: `src/validation/newRoute.ts`
3. Write tests: `src/routes/__tests__/newRoute.test.ts`
4. Update API docs: `docs/api-reference.md`
5. Refresh index: Run `index-docs --refresh`

**References:**
- Pattern: Express Router (`docs/patterns.md:89`)
- Example: Auth Routes (`src/routes/auth.ts`)

---

*Quick Reference automatically generated by index-docs skill*
*Last updated: 2025-10-30*
*Index version: 1.0*
```

---

### glossary.md Format

**Complete Glossary Document:**
```markdown
# Project Glossary

*Generated: 2025-10-30 | Index Version: 1.0*

---

## A

### Authentication
**Category:** Security
**Definition:** Process of verifying a user's identity through credentials (email/password, OAuth, etc.)

**Related Terms:** Authorization, JWT, Session
**Documentation:** `docs/api-reference.md:67`
**Code:** `src/services/AuthService.ts:12`

---

### Authorization
**Category:** Security
**Definition:** Process of determining what resources an authenticated user can access

**Related Terms:** Authentication, Permissions, Roles
**Documentation:** `docs/patterns.md:145`
**Code:** `src/middleware/auth.ts:34`

---

## B

### Bcrypt
**Category:** Technology
**Definition:** Password hashing library using blowfish cipher for secure password storage

**Related Terms:** Password, Security, Hashing
**Documentation:** `docs/standards.md:89`
**Code:** `src/utils/password.ts:23`
**External:** https://github.com/kelektiv/node.bcrypt.js

---

## D

### Data Model
**Category:** Architecture
**Definition:** Representation of domain entities with attributes, relationships, and business logic

**Related Terms:** Entity, Schema, ORM
**Documentation:** `docs/data-models.md:12`
**Code:** `src/models/*.ts`

---

### DTO (Data Transfer Object)
**Category:** Pattern
**Definition:** Object that carries data between processes, typically used for API request/response

**Related Terms:** API, Validation, Serialization
**Documentation:** `docs/patterns.md:234`
**Code:** `src/dto/*.ts`

---

## E

### Express
**Category:** Technology
**Definition:** Fast, unopinionated web framework for Node.js

**Related Terms:** Node.js, REST API, Middleware
**Documentation:** `docs/architecture.md:123`
**Code:** `src/app.ts:5`
**External:** https://expressjs.com

---

## F

### Factory Pattern
**Category:** Pattern
**Definition:** Creational design pattern that provides interface for creating objects without specifying exact class

**Related Terms:** Design Pattern, Abstraction
**Documentation:** `docs/patterns.md:67`
**Code:** `src/factories/*.ts`

---

## J

### JWT (JSON Web Token)
**Category:** Technology/Security
**Definition:** Open standard (RFC 7519) for securely transmitting information as JSON object

**Structure:** header.payload.signature
**Used For:** Authentication, authorization, information exchange

**Related Terms:** Authentication, Token, Bearer
**Documentation:** `docs/api-reference.md:89`
**Code:** `src/services/jwt.ts:12`
**External:** https://jwt.io

---

## M

### Middleware
**Category:** Architecture
**Definition:** Functions that have access to request/response objects and can execute code, modify objects, or end request-response cycle

**Related Terms:** Express, Request Pipeline, Chain of Responsibility
**Documentation:** `docs/architecture.md:234`
**Code:** `src/middleware/*.ts`

---

## O

### ORM (Object-Relational Mapping)
**Category:** Technology
**Definition:** Technique for converting data between incompatible type systems (database and programming language)

**Our ORM:** Prisma
**Related Terms:** Database, Data Model, Query Builder
**Documentation:** `docs/data-models.md:23`
**Code:** `src/database/client.ts:5`

---

## P

### Prisma
**Category:** Technology
**Definition:** Next-generation ORM for Node.js and TypeScript with type safety and auto-completion

**Related Terms:** ORM, Database, TypeScript
**Documentation:** `docs/data-models.md:23`
**Code:** `prisma/schema.prisma`
**External:** https://www.prisma.io

---

## R

### Repository Pattern
**Category:** Pattern
**Definition:** Mediates between domain and data mapping layers, acting like in-memory collection of domain objects

**Benefits:** Decouples business logic from data access, improves testability

**Related Terms:** Data Access Layer, Abstraction
**Documentation:** `docs/patterns.md:23`
**Code:** `src/repositories/*.ts`

---

### REST (Representational State Transfer)
**Category:** Architecture
**Definition:** Architectural style for designing networked applications using HTTP methods

**Principles:** Stateless, client-server, cacheable, layered system
**Related Terms:** API, HTTP, Resource

**Documentation:** `docs/api-reference.md:12`
**Code:** `src/routes/*.ts`

---

## S

### Schema
**Category:** Database
**Definition:** Structure that defines organization of data in database, including tables, columns, relationships, constraints

**Related Terms:** Data Model, Database, Prisma
**Documentation:** `docs/data-models.md:34`
**Code:** `prisma/schema.prisma`

---

### Service Layer
**Category:** Architecture
**Definition:** Layer that contains business logic, coordinates application activities, and transactions

**Related Terms:** Business Logic, Architecture, Separation of Concerns
**Documentation:** `docs/architecture.md:145`
**Code:** `src/services/*.ts`

---

## T

### TypeScript
**Category:** Technology
**Definition:** Typed superset of JavaScript that compiles to plain JavaScript, adding static type definitions

**Related Terms:** JavaScript, Type Safety, Compilation
**Documentation:** `docs/standards.md:12`
**Code:** `tsconfig.json`, all `.ts` files
**External:** https://www.typescriptlang.org

---

## U

### UUID (Universally Unique Identifier)
**Category:** Technology
**Definition:** 128-bit identifier guaranteed to be unique across space and time

**Format:** 8-4-4-4-12 hex digits (e.g., `550e8400-e29b-41d4-a716-446655440000`)
**Used For:** Primary keys, unique identifiers

**Related Terms:** Primary Key, Identifier
**Documentation:** `docs/data-models.md:67`
**Code:** Used throughout `src/models/*.ts`

---

## V

### Validation
**Category:** Security/Quality
**Definition:** Process of ensuring data meets required format, type, and business rules before processing

**Libraries Used:** Zod, Joi
**Related Terms:** Input Validation, Security, Data Integrity

**Documentation:** `docs/standards.md:156`
**Code:** `src/validation/*.ts`

---

*Glossary automatically generated by index-docs skill*
*Last updated: 2025-10-30*
*Total terms: 156*
```

---

## Search Examples

### Searching with grep

**Find all documentation about "User model":**
```bash
$ grep -i "user" .claude/index/search.json | jq '.documents[] | select(.keywords[] | contains("User"))'

Result:
{
  "id": "doc-002",
  "file": "docs/data-models.md",
  "title": "Data Models",
  "sections": [...],
  "keywords": ["User", "Model", "Authentication", "Database"]
}
```

**Find API endpoint documentation:**
```bash
$ cat .claude/index/quick-ref.md | grep -A 10 "/api/auth/login"

Result:
#### POST /api/auth/login
**File:** `src/routes/auth.ts:34`
**Documentation:** `docs/api-reference.md:67`

**Request:**
```json
{
  "email": "user@example.com",
  "password": "SecurePass123!"
}
```
```

**Find term definition:**
```bash
$ cat .claude/index/glossary.md | grep -A 5 "### JWT"

Result:
### JWT (JSON Web Token)
**Category:** Technology/Security
**Definition:** Open standard (RFC 7519) for securely transmitting information as JSON object

**Structure:** header.payload.signature
**Used For:** Authentication, authorization, information exchange
```

---

## Index Maintenance

### Refresh Index

**When to refresh:**
- Documentation files updated
- New code files added
- After running document-project skill
- Quarterly maintenance

**Refresh vs Rebuild:**

**Refresh (Incremental):**
- Faster (~2-5 seconds)
- Updates only changed files
- Preserves manual customizations
- Recommended for regular updates

**Rebuild (Full):**
- Slower (~10-20 seconds)
- Recreates entire index from scratch
- Removes any manual customizations
- Recommended when structure changes significantly

**Commands:**
```bash
# Refresh existing index (incremental)
@alex *index-docs --refresh

# Full rebuild
@alex *index-docs --rebuild

# Check index status
@alex *index-docs --status
```

**Refresh Output:**
```
✓ Index refresh started
✓ Comparing with previous index (last updated: 2025-10-15)
✓ Changes detected:
  ├─ Modified: docs/api-reference.md (2 days ago)
  ├─ New: docs/deployment.md
  ├─ Deleted: docs/old-patterns.md
  └─ Unchanged: 3 files
✓ Reindexing modified files...
  ├─ docs/api-reference.md (124 sections, 189 keywords)
  └─ docs/deployment.md (45 sections, 98 keywords)
✓ Updating search index...
✓ Updating quick reference...
✓ Updating glossary...
✓ Index refreshed successfully
✓ Total duration: 2.3s
```

---

## Integration with Other Skills

### With document-project

**Workflow:**
```
document-project → Generates comprehensive documentation
                    ↓
              index-docs → Creates searchable index from docs
                    ↓
         create-task-spec → Uses index to find relevant context
```

**Example:**
```markdown
User runs: @alex *document-project

Result: Creates docs/architecture.md, docs/data-models.md, etc.

User runs: @alex *index-docs

Result: Creates .claude/index/ with searchable index of all documentation

User runs: @alex *create-task-spec for "add user profile editing"

create-task-spec skill:
1. Searches index for "User" and "profile"
2. Finds: docs/data-models.md:45 (User model definition)
3. Finds: docs/api-reference.md:123 (related endpoints)
4. Includes relevant context in task spec
```

---

### With implement-feature

**Workflow:**
```
implement-feature → Needs to look up pattern
                    ↓
        quick-ref.md → Fast lookup of Repository Pattern
                    ↓
implement-feature → Applies pattern from example
```

**Example:**
```markdown
Developer implementing new feature needs to add data access layer.

Quickly checks: cat .claude/index/quick-ref.md | grep "Repository Pattern"

Finds:
- Pattern documentation: docs/patterns.md:23
- Example implementation: src/repositories/UserRepository.ts
- Usage examples in services

Implements using established pattern.
```

---

## JSON Output Format

**Complete Skill Output:**
```json
{
  "skill": "index-docs",
  "version": "1.0",
  "status": "completed",
  "timestamp": "2025-10-30T14:32:15Z",
  "duration_ms": 5234,
  "configuration": {
    "docsPath": "docs/",
    "codebasePath": "src/",
    "indexLocation": ".claude/index/",
    "includeCode": true,
    "maxDepth": 3
  },
  "results": {
    "documentation": {
      "files_indexed": 5,
      "sections_extracted": 316,
      "keywords_identified": 775,
      "cross_references": 42
    },
    "codebase": {
      "files_indexed": 247,
      "exports_mapped": 156,
      "functions_mapped": 423,
      "code_to_docs_links": 89
    },
    "index_files": {
      "search_json": {
        "path": ".claude/index/search.json",
        "size_bytes": 130048
      },
      "quick_ref_md": {
        "path": ".claude/index/quick-ref.md",
        "size_bytes": 34816
      },
      "glossary_md": {
        "path": ".claude/index/glossary.md",
        "size_bytes": 12288
      }
    }
  },
  "telemetry": {
    "event": "skill.index-docs.completed",
    "files_indexed": 252,
    "keywords_count": 775,
    "references_count": 864,
    "duration_ms": 5234
  }
}
```

---

*Complete templates and output formats for index-docs skill*
