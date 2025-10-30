# Planning Skill: Document Existing Project (Brownfield)

<!-- BMAD Enhanced Planning Skill -->
<!-- Generate architecture documentation from existing codebase -->
<!-- Version: 1.0 -->

## Purpose

Analyze an existing codebase and generate comprehensive architecture documentation automatically. This skill enables BMAD Enhanced to work with brownfield projects by reverse-engineering architecture, patterns, and standards from code.

**Key Innovation:**
- Automated documentation from code analysis
- Pattern discovery and extraction
- Confidence scoring for accuracy
- Iterative improvement over time

## When to Use This Skill

Use this skill when you need to:
- Start using BMAD Enhanced with existing project
- Update outdated architecture documentation
- Discover implicit patterns and conventions
- Onboard to unfamiliar codebase

**Do NOT use this skill for:**
- Greenfield projects (write docs from scratch)
- Well-documented projects (use existing docs)
- Very large codebases (>500K lines - too complex)
- Projects with no clear structure

## Project Type Support

**Supported Project Types:**
- ✅ Node.js/TypeScript (excellent support)
- ✅ Python (good support)
- ✅ Go (good support)
- ✅ Java/Kotlin (good support)
- ✅ Rust (good support)
- ⚠️ PHP (basic support)
- ⚠️ Ruby (basic support)
- ⚠️ C#/.NET (basic support)

**Optimal Codebase Size:** 10K-100K lines
- Smaller: May not have enough patterns to analyze
- Larger: Analysis may take too long or be too complex

---

## SEQUENTIAL Task Execution

**CRITICAL:** Execute steps in order. Do not skip pattern analysis.

### Step 0: Load Configuration and Validate Project

**Purpose:** Verify project is suitable for automated documentation

**Actions:**

1. **Load Configuration:**
   ```yaml
   # Read .claude/config.yaml
   project:
     type: brownfield
     name: {project-name}

   brownfield:
     codebasePath: src/  # Path to analyze
     existingDocs: []    # Existing docs to preserve
     includeTests: true  # Include test analysis
     maxFilesToAnalyze: 1000

   documentation:
     architecture: docs/architecture.md
     standards: docs/standards.md
     patterns: docs/patterns.md
   ```

2. **Validate Project Structure:**
   - Check codebase path exists
   - Identify primary language(s)
   - Count total files and lines of code
   - Check if within supported size (10K-100K lines recommended)

3. **Check Existing Documentation:**
   - Look for existing docs at configured paths
   - If found, ask user:
     ```
     Existing documentation detected:
     - docs/architecture.md (last modified: 6 months ago)
     - docs/standards.md (missing)

     Options:
     A) Merge: Preserve existing docs, add new findings
     B) Replace: Generate fresh documentation
     C) Supplement: Keep existing, create supplemental docs

     Which option would you like?
     ```

4. **Get User Confirmation:**
   ```
   Project Analysis Summary:
   - Path: src/
   - Language: TypeScript (95%), JavaScript (5%)
   - Total files: 247
   - Total lines: 42,350
   - Estimated analysis time: 5-10 minutes

   Proceed with automated documentation? (yes/no)
   ```

**Halt If:**
- Codebase path not found
- No recognizable project structure
- Codebase too large (>500K lines)
- Unsupported language
- User declines to proceed

**Output:**
```
✓ Project validated: TypeScript project, 42K lines
✓ Existing docs: docs/architecture.md (merge mode)
✓ Analysis scope: src/ (247 files)
✓ Ready to analyze
```

---

### Step 1: Analyze Project Structure

**Purpose:** Map file organization and module structure

**Actions:**

1. **Scan Directory Structure:**
   ```bash
   # Get directory tree
   find src/ -type d | sort
   ```
   - Identify main directories (e.g., routes/, services/, models/)
   - Detect organizational patterns (by feature vs by type)
   - Note depth of nesting

2. **Analyze File Organization:**
   ```bash
   # Count files by directory
   find src/ -type f -name "*.ts" -o -name "*.js" | ...
   ```
   - Files per directory
   - Naming conventions (camelCase, kebab-case, etc.)
   - File size distribution
   - Co-location patterns (tests with code vs separate)

3. **Detect Project Type:**
   - **Backend API:** routes/, controllers/, services/, models/
   - **Frontend App:** components/, pages/, hooks/, context/
   - **Full-Stack:** Both patterns present
   - **Library:** lib/, dist/, no app structure
   - **Monorepo:** packages/, apps/, libs/

4. **Map Module Relationships:**
   - Analyze imports/requires
   - Build dependency graph
   - Identify core vs. peripheral modules
   - Detect circular dependencies

**Output:**
```
Project Structure Analysis:

Type: Backend API (Express.js)
Organization: Layered architecture (by type)

Directory Structure:
src/
├── routes/         # API endpoints (12 files, ~2,000 lines)
├── services/       # Business logic (18 files, ~4,500 lines)
├── repositories/   # Data access (8 files, ~1,800 lines)
├── models/         # Data models (15 files, ~3,200 lines)
├── middleware/     # Express middleware (6 files, ~800 lines)
├── utils/          # Utilities (22 files, ~2,100 lines)
└── types/          # TypeScript types (10 files, ~1,500 lines)

tests/
├── unit/           # Unit tests (45 files)
├── integration/    # Integration tests (12 files)
└── e2e/            # E2E tests (5 files)

Key Patterns:
- Layered architecture (routes → services → repositories)
- Dependency injection pattern detected
- Test co-location: No (separate tests/ directory)
- Naming: kebab-case for files, PascalCase for classes
```

---

### Step 2: Analyze Technology Stack

**Purpose:** Identify languages, frameworks, and dependencies

**Actions:**

1. **Read Package Configuration:**
   - **Node.js:** Read package.json
   - **Python:** Read requirements.txt, pyproject.toml, Pipfile
   - **Go:** Read go.mod
   - **Java:** Read pom.xml, build.gradle
   - **Rust:** Read Cargo.toml

2. **Extract Dependencies:**
   ```json
   {
     "dependencies": {
       "express": "^4.18.2",
       "prisma": "^5.6.0",
       "zod": "^3.22.4",
       "bcrypt": "^5.1.1",
       "jsonwebtoken": "^9.0.2"
     },
     "devDependencies": {
       "jest": "^29.7.0",
       "typescript": "^5.3.2",
       "supertest": "^6.3.3"
     }
   }
   ```

3. **Identify Frameworks:**
   - **Backend:** Express, Fastify, Koa, NestJS, Django, Flask, Spring Boot
   - **Frontend:** React, Vue, Angular, Svelte, Next.js
   - **Database:** Prisma, TypeORM, Sequelize, Mongoose, SQLAlchemy
   - **Testing:** Jest, Mocha, Pytest, JUnit

4. **Detect Runtime/Platform:**
   - Node.js version
   - Python version
   - JDK version
   - Database type (PostgreSQL, MySQL, MongoDB)

**Output:**
```
Technology Stack:

Runtime:
- Node.js: >=20.0.0
- TypeScript: 5.3.2

Backend Framework:
- Express.js: 4.18.2 (web framework)
- Prisma: 5.6.0 (ORM)

Key Libraries:
- zod: 3.22.4 (validation)
- bcrypt: 5.1.1 (password hashing)
- jsonwebtoken: 9.0.2 (authentication)

Testing:
- Jest: 29.7.0 (test framework)
- Supertest: 6.3.3 (HTTP testing)

Database:
- PostgreSQL (inferred from Prisma schema)

Confidence: High (95%)
```

---

### Step 3: Extract Data Models and Schemas

**Purpose:** Document data structures and validation rules

**Actions:**

1. **Locate Data Model Files:**
   - Prisma schema: `prisma/schema.prisma`
   - TypeScript interfaces: `src/types/*.ts`, `src/models/*.ts`
   - Database migrations: `prisma/migrations/`, `migrations/`
   - Validation schemas: Zod, Yup, Joi schemas

2. **Parse Data Models:**
   ```typescript
   // Extract from TypeScript
   interface User {
     id: string;
     email: string;
     password: string;
     createdAt: Date;
   }
   ```

3. **Extract Validation Rules:**
   ```typescript
   // From Zod schemas
   const userSchema = z.object({
     email: z.string().email(),
     password: z.string().min(8)
   });
   ```

4. **Analyze Relationships:**
   - One-to-many: User → Posts
   - Many-to-many: Users ↔ Roles
   - Foreign keys and constraints

5. **Detect Data Flow:**
   - Request → Validation → Service → Repository → Database
   - Response transformation (DTOs)

**Output:**
```
Data Models:

User Model:
- id: UUID (primary key)
- email: string (unique, validated: RFC 5322 format)
- password: string (hashed with bcrypt)
- emailVerified: boolean (default: false)
- createdAt: timestamp (auto-generated)
- updatedAt: timestamp (auto-updated)

Validation Rules:
- Email: Must be valid format, max 255 chars
- Password: Min 8 chars, must contain uppercase, lowercase, number, special char

Relationships:
- User hasMany Posts (one-to-many)
- User hasMany Sessions (one-to-many)

Source Files:
- prisma/schema.prisma (Prisma model)
- src/types/user.ts (TypeScript interface)
- src/schemas/auth.schema.ts (Zod validation)

Confidence: High (90%)
```

---

### Step 4: Analyze API Patterns

**Purpose:** Document API structure and conventions

**Actions:**

1. **Locate API Definitions:**
   - Express routes: `src/routes/**/*.ts`
   - Controllers: `src/controllers/**/*.ts`
   - OpenAPI/Swagger spec (if exists)
   - GraphQL schemas (if exists)

2. **Extract Endpoints:**
   ```typescript
   // From route files
   router.post('/api/auth/signup', signupHandler);
   router.post('/api/auth/login', loginHandler);
   ```

3. **Analyze Request/Response Patterns:**
   - Request validation (middleware)
   - Error response format
   - Success response format
   - Status codes used

4. **Identify Authentication:**
   - JWT tokens
   - Session-based
   - API keys
   - OAuth

5. **Detect Rate Limiting:**
   - Rate limit middleware
   - Throttling patterns

**Output:**
```
API Specifications:

Base URL: /api

Authentication Endpoints:
- POST /api/auth/signup
  Request: { email: string, password: string }
  Response (201): { user: UserResponse, token: string }
  Response (400): { error: string, details: string[] }

- POST /api/auth/login
  Request: { email: string, password: string }
  Response (200): { user: UserResponse, token: string }
  Response (401): { error: string }

Authentication:
- Type: JWT (Bearer token)
- Header: Authorization: Bearer <token>
- Token expiry: 7 days

Error Response Format:
{
  "error": "Error message",
  "details": ["Detail 1", "Detail 2"],
  "code": "ERROR_CODE"
}

Success Response Format:
{
  "data": {...},
  "meta": {...}  // pagination, etc.
}

Rate Limiting:
- Not detected (confidence: Medium)

Source Files:
- src/routes/auth/*.ts (route definitions)
- src/middleware/auth.ts (JWT verification)

Confidence: High (85%)
```

---

### Step 5: Extract Coding Standards and Patterns

**Purpose:** Document implicit conventions and best practices

**Actions:**

1. **Analyze Code Style:**
   - Read `.eslintrc`, `.prettierrc`, `tsconfig.json`
   - Detect: indentation, quotes, semicolons
   - Naming conventions: variables, functions, classes, files

2. **Identify Architectural Patterns:**
   - **Design Patterns:**
     - Repository pattern (detected in repositories/)
     - Factory pattern (detected in factories/)
     - Strategy pattern (detected in strategies/)
   - **Architectural Style:**
     - Layered architecture (routes → services → repositories)
     - Clean architecture
     - Hexagonal architecture

3. **Extract Error Handling:**
   ```typescript
   // Common pattern
   try {
     // operation
   } catch (error) {
     logger.error('Error:', error);
     throw new AppError(500, 'Internal server error');
   }
   ```

4. **Identify Logging Patterns:**
   - Logger library (winston, pino, etc.)
   - Log levels used
   - Structured logging

5. **Detect Testing Patterns:**
   - Test organization (describe/it blocks)
   - Mocking strategy (jest.mock, sinon)
   - Test data management
   - Setup/teardown patterns

**Output:**
```
Coding Standards:

Language: TypeScript
- Strict mode: Enabled
- No implicit any: Enabled
- Target: ES2022

Code Style:
- Indentation: 2 spaces
- Quotes: Single quotes
- Semicolons: Required
- Line length: 100 characters

Naming Conventions:
- Variables/Functions: camelCase
- Classes/Interfaces: PascalCase
- Constants: UPPER_SNAKE_CASE
- Files: kebab-case.ts
- Test files: *.test.ts or *.spec.ts

Architectural Patterns:
1. Layered Architecture
   - Routes (presentation layer)
   - Services (business logic layer)
   - Repositories (data access layer)

2. Dependency Injection
   - Constructor injection
   - Interface-based dependencies

3. Repository Pattern
   - Data access abstraction
   - Separate concerns

Error Handling:
- Custom error classes (AppError, ValidationError)
- Centralized error handling middleware
- Never expose stack traces to clients
- Always log errors with context

Logging:
- Library: winston
- Levels: error, warn, info, debug
- Format: JSON structured logging
- Never log passwords or sensitive data

Testing:
- Framework: Jest
- Coverage target: Not explicitly defined (inferred: 80%+)
- Organization: Separate tests/ directory
- Mocking: jest.mock() for external dependencies
- Test data: Factories in tests/factories/

Source Files:
- .eslintrc.json (linting rules)
- tsconfig.json (TypeScript config)
- src/**/*.ts (code analysis)
- tests/**/*.test.ts (test patterns)

Confidence: High (90%)
```

---

### Step 6: Generate Architecture Documentation

**Purpose:** Create comprehensive architecture.md from findings

**Actions:**

1. **Load Template:**
   - Use architecture template structure
   - Sections: Overview, Tech Stack, Project Structure, Data Models, API Specs, etc.

2. **Populate Sections with Findings:**
   - Fill each section with analyzed data from Steps 1-5
   - Add confidence scores where applicable
   - Include source file references

3. **Generate Diagrams (Optional):**
   - Mermaid diagrams for architecture layers
   - Data model ERD
   - API endpoint map

4. **Add Human Review Notes:**
   ```markdown
   ## Human Review Required

   The following sections have medium/low confidence and should be reviewed:

   - [ ] API rate limiting (not detected - verify if implemented)
   - [ ] Caching strategy (not clearly evident - document if exists)
   - [ ] Deployment architecture (not in codebase - add manually)
   ```

5. **Write Documentation File:**
   - Create `docs/architecture.md`
   - Or merge with existing docs if "merge" mode selected

**Output:**
```
✓ Architecture documentation generated
✓ File: docs/architecture.md (2,450 lines)
✓ Sections: 12
✓ Overall confidence: 85%
✓ Human review items: 5
```

---

### Step 7: Generate Standards Documentation

**Purpose:** Create standards.md from discovered patterns

**Actions:**

1. **Extract Standards from Code Analysis:**
   - Security standards (from security practices)
   - Testing standards (from test patterns)
   - Code quality standards (from ESLint rules)
   - Performance standards (from observed patterns)

2. **Document Best Practices:**
   - Observed consistently across codebase
   - Mark as "discovered" vs "recommended"

3. **Create Standards Document:**
   ```markdown
   # Development Standards

   ## Security Standards

   ### Password Security
   - Hashing: bcrypt with cost factor 12
   - Source: Observed in src/services/auth/signup.service.ts
   - Consistency: 100% (all password operations use bcrypt cost 12)

   ### Input Validation
   - Library: Zod
   - Location: src/schemas/*.schema.ts
   - Pattern: Validate at route handler before service call
   - Consistency: 90% (2 endpoints missing validation)

   ## Testing Standards

   ### Test Coverage
   - Current coverage: 78% (measured)
   - Inferred target: 80%+ (based on PR patterns)
   - Minimum enforced: None (no coverage gate detected)

   ### Test Organization
   - Structure: Separate tests/ directory
   - Naming: *.test.ts
   - Framework: Jest + Supertest
   ```

4. **Write Standards File:**
   - Create `docs/standards.md`

**Output:**
```
✓ Standards documentation generated
✓ File: docs/standards.md (850 lines)
✓ Standards extracted: 18
✓ Consistency scores: 75-100%
```

---

### Step 8: Generate Patterns Documentation

**Purpose:** Document discovered design patterns and conventions

**Actions:**

1. **Extract Design Patterns:**
   - Repository pattern
   - Factory pattern
   - Strategy pattern
   - Middleware pattern
   - etc.

2. **Document Usage Examples:**
   - Show code examples of each pattern
   - Explain when to use
   - Link to existing implementations

3. **Identify Anti-patterns:**
   - Code smells detected
   - Inconsistencies
   - Technical debt

4. **Create Patterns Document:**
   ```markdown
   # Design Patterns & Conventions

   ## Repository Pattern

   Used for data access abstraction.

   **Implementation:**
   ```typescript
   interface UserRepository {
     findByEmail(email: string): Promise<User | null>;
     create(data: CreateUserDto): Promise<User>;
   }
   ```

   **Usage:**
   - All database operations go through repositories
   - Services depend on repository interfaces (DI)
   - Enables easy testing with mocks

   **Examples:**
   - src/repositories/user.repository.ts
   - src/repositories/session.repository.ts

   **Consistency:** 95% (most data access uses this pattern)
   ```

5. **Write Patterns File:**
   - Create `docs/patterns.md`

**Output:**
```
✓ Patterns documentation generated
✓ File: docs/patterns.md (620 lines)
✓ Patterns identified: 8
✓ Anti-patterns noted: 3
```

---

### Step 9: Validation and Confidence Scoring

**Purpose:** Score accuracy and identify areas needing human review

**Actions:**

1. **Calculate Overall Confidence:**
   ```
   Confidence Scoring:

   Tech Stack:         95% (explicit in package.json)
   Project Structure:  90% (clear file organization)
   Data Models:        85% (some inferred relationships)
   API Specifications: 80% (missing OpenAPI spec)
   Coding Standards:   90% (ESLint + observed patterns)

   Overall Confidence: 88%
   ```

2. **Identify Low-Confidence Areas:**
   - Sections with <70% confidence
   - Conflicting patterns found
   - Sparse or missing information

3. **Generate Human Review Checklist:**
   ```markdown
   ## Human Review Required

   High Priority:
   - [ ] Verify API rate limiting implementation
   - [ ] Document deployment architecture
   - [ ] Confirm database connection pooling settings

   Medium Priority:
   - [ ] Verify password requirements match security policy
   - [ ] Document caching strategy (if exists)
   - [ ] Add monitoring and alerting documentation

   Low Priority:
   - [ ] Document code review process
   - [ ] Add contribution guidelines
   - [ ] Document release process
   ```

4. **Create Validation Report:**
   - Summary of analysis
   - Confidence scores by section
   - Files analyzed count
   - Time taken
   - Recommendations for improvement

**Output:**
```
✓ Validation complete
✓ Overall confidence: 88%
✓ High-priority review items: 3
✓ Medium-priority review items: 3
✓ Low-priority review items: 3
```

---

### Step 10: Summary and Next Steps

**Purpose:** Provide user with clear summary and action items

**Actions:**

1. **Generate Summary Report:**
   ```markdown
   ## Automated Documentation Complete

   **Project:** {project-name}
   **Analysis Duration:** 8 minutes
   **Files Analyzed:** 247
   **Lines Analyzed:** 42,350
   **Overall Confidence:** 88%

   **Generated Documentation:**
   - ✅ docs/architecture.md (2,450 lines)
   - ✅ docs/standards.md (850 lines)
   - ✅ docs/patterns.md (620 lines)

   **Key Findings:**
   - Project Type: Backend API (Express.js)
   - Architecture: Layered architecture
   - Primary Patterns: Repository, Dependency Injection
   - Tech Stack: TypeScript, Express, Prisma, PostgreSQL
   - Test Coverage: 78% (measured)
   - Code Quality: Good (few anti-patterns)

   **Human Review Required:**
   - 3 high-priority items (API rate limiting, deployment, connection pooling)
   - 3 medium-priority items (caching, monitoring)
   - 3 low-priority items (processes and guidelines)

   **Next Steps:**
   1. Review generated documentation (especially low-confidence sections)
   2. Complete human review checklist (docs/REVIEW_CHECKLIST.md)
   3. Update configuration with correct paths
   4. Begin creating task specifications using architecture docs
   5. Consider running document-project skill periodically to keep docs fresh

   **Documentation Quality:**
   - Ready to use: Yes (with review)
   - Suitable for task creation: Yes
   - Suitable for onboarding: Yes (after review)
   ```

2. **Create Review Checklist File:**
   - Write `docs/REVIEW_CHECKLIST.md`
   - Markdown checklist format
   - Organized by priority

3. **Update Configuration:**
   - Set `project.type: brownfield`
   - Set documentation paths
   - Set `brownfield.documented: true`

4. **Prompt for Next Action:**
   ```
   Documentation generation complete!

   Would you like to:
   A) Review high-priority items now
   B) Create first task specification using generated docs
   C) Run index-docs skill to create searchable knowledge base
   D) Exit (review later)

   Select option:
   ```

**Output:**
```
✓ Summary report generated
✓ Review checklist created: docs/REVIEW_CHECKLIST.md
✓ Configuration updated
✓ Ready for next phase
```

---

## Completion Criteria

Project documentation is complete when:

- [ ] All three documentation files generated (architecture, standards, patterns)
- [ ] Confidence score ≥70% overall
- [ ] Human review checklist created
- [ ] Configuration updated with doc paths
- [ ] User informed of next steps

## Confidence Scoring Guidelines

**High Confidence (85-100%):**
- Information explicitly in code or config files
- Consistent patterns observed across codebase
- No conflicting information found

**Medium Confidence (70-84%):**
- Information inferred from patterns
- Some inconsistencies observed
- Requires validation

**Low Confidence (<70%):**
- Information missing or unclear
- Conflicting patterns
- High uncertainty
- MUST be reviewed by human

## Limitations

**This skill cannot:**
- ❌ Understand business logic without code context
- ❌ Document deployment infrastructure (not in code)
- ❌ Capture tribal knowledge
- ❌ Understand legacy decisions
- ❌ Document external integrations perfectly

**This skill requires:**
- ✅ Readable, structured codebase
- ✅ Standard project organization
- ✅ Supported language/framework
- ✅ 10K-100K lines (optimal)

## Best Practices

1. **Run Periodically:**
   - Re-run every 3-6 months
   - Update docs as code evolves
   - Track confidence scores over time

2. **Always Review:**
   - Don't trust 100% - always review
   - Focus on low-confidence sections first
   - Validate against team knowledge

3. **Supplement with Manual Docs:**
   - Add business context
   - Document deployment
   - Capture architecture decisions (ADRs)

4. **Use as Starting Point:**
   - Generated docs are foundation
   - Enhance with team input
   - Iterate and improve

## Integration with Planning Workflow

**Brownfield Workflow:**
1. **document-project** → Generate architecture docs
2. **index-docs** → Create searchable knowledge base
3. **create-task-spec** → Use docs for task creation
4. (Regular workflow continues)

**Greenfield vs Brownfield:**
- **Greenfield:** Write architecture docs manually first
- **Brownfield:** Generate architecture docs from code, then refine

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-10-28 | Initial brownfield documentation skill |

---

**End of Document Project Skill**
