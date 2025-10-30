---
name: document-project
description: Generate comprehensive architecture documentation automatically from existing codebase analysis. Use when working with brownfield projects or updating outdated documentation.
acceptance:
  - documentation_generated: "All three documentation files created (architecture.md, standards.md, patterns.md)"
  - confidence_sufficient: "Overall confidence score ≥70% across all analyzed sections"
  - review_checklist_created: "Human review checklist generated identifying low-confidence areas"
  - configuration_updated: "Project configuration updated with documentation paths and brownfield flag"
inputs:
  codebase_path:
    type: string
    required: true
    description: "Path to codebase to analyze (e.g., src/)"
  existing_docs_mode:
    type: enum
    values: ["merge", "replace", "supplement"]
    default: "merge"
    description: "How to handle existing documentation"
  include_tests:
    type: boolean
    default: true
    description: "Include test file analysis in documentation"
  max_files:
    type: number
    default: 1000
    description: "Maximum files to analyze (safety limit)"
outputs:
  documentation_files:
    type: object
    description: "Paths to generated documentation files"
  confidence_score:
    type: number
    description: "Overall confidence score (0-100%)"
  review_checklist:
    type: string
    description: "Path to human review checklist file"
  analysis_summary:
    type: object
    description: "Summary of analysis (files analyzed, patterns found, etc.)"
telemetry:
  emit: "skill.document-project.completed"
  track:
    - project_name
    - codebase_path
    - duration_ms
    - files_analyzed
    - lines_analyzed
    - confidence_score
    - patterns_identified
---

# Brownfield Project Documentation Generator

Generate comprehensive architecture documentation automatically by analyzing existing codebase structure, patterns, and conventions.

## Purpose

Analyze an existing codebase and generate three comprehensive documentation files:
1. **architecture.md** - Project structure, tech stack, data models, API specifications
2. **standards.md** - Coding standards, best practices, discovered conventions
3. **patterns.md** - Design patterns, architectural patterns, common conventions

This enables BMAD Enhanced to work with brownfield projects by reverse-engineering architecture from code.

## When to Use

Use this skill when:
- Starting BMAD Enhanced with existing project (brownfield onboarding)
- Architecture documentation is outdated or missing
- Need to discover implicit patterns and conventions
- Onboarding to unfamiliar codebase

Do NOT use when:
- Greenfield projects (write docs from scratch instead)
- Project already has current, comprehensive documentation
- Codebase >500K lines (too complex for automated analysis)
- Project has no clear structure

## Project Type Support

**Well-Supported Languages:**
- ✅ Node.js/TypeScript (excellent support)
- ✅ Python (good support)
- ✅ Go (good support)
- ✅ Java/Kotlin (good support)
- ✅ Rust (good support)

**Basic Support:**
- ⚠️ PHP, Ruby, C#/.NET (basic support)

**Optimal Codebase Size:** 10K-100K lines
- Smaller: May lack sufficient patterns to analyze
- Larger: Analysis may be too slow or complex

## Sequential Documentation Generation

Execute steps in order - each builds on previous analysis:

### Step 0: Configuration and Validation

**Purpose:** Verify project is suitable for automated documentation.

**Actions:**

1. Load configuration from `.claude/config.yaml`:
   ```yaml
   brownfield:
     codebasePath: src/
     existingDocs: []
     includeTests: true
     maxFilesToAnalyze: 1000
   ```

2. Validate project structure:
   - Check codebase path exists
   - Identify primary language(s)
   - Count total files and lines of code
   - Verify within supported size (10K-100K lines recommended)

3. Check existing documentation:
   - Look for existing docs at configured paths
   - If found, ask user how to handle:
     - **Merge:** Preserve existing docs, add new findings
     - **Replace:** Generate fresh documentation
     - **Supplement:** Keep existing, create supplemental docs

4. Get user confirmation:
   ```
   Project Analysis Summary:
   - Path: src/
   - Language: TypeScript (95%), JavaScript (5%)
   - Total files: 247
   - Total lines: 42,350
   - Estimated analysis time: 5-10 minutes

   Proceed with automated documentation? (yes/no)
   ```

**Halt if:**
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

**Reference:** See [validation-criteria.md](references/validation-criteria.md) for detailed validation rules.

---

### Step 1: Analyze Project Structure

**Purpose:** Map file organization and module structure.

**Actions:**

1. Scan directory structure:
   ```bash
   find src/ -type d | sort
   ```
   - Identify main directories (routes/, services/, models/, etc.)
   - Detect organizational patterns (by feature vs by type)
   - Note depth of nesting

2. Analyze file organization:
   - Files per directory
   - Naming conventions (camelCase, kebab-case, etc.)
   - File size distribution
   - Co-location patterns (tests with code vs separate)

3. Detect project type:
   - **Backend API:** routes/, controllers/, services/, models/
   - **Frontend App:** components/, pages/, hooks/, context/
   - **Full-Stack:** Both patterns present
   - **Library:** lib/, dist/, no app structure
   - **Monorepo:** packages/, apps/, libs/

4. Map module relationships:
   - Analyze imports/requires
   - Build dependency graph
   - Identify core vs peripheral modules
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
└── utils/          # Utilities (22 files, ~2,100 lines)

Key Patterns:
- Layered architecture (routes → services → repositories)
- Dependency injection pattern detected
- Test co-location: No (separate tests/ directory)
```

**Reference:** See [analysis-techniques.md](references/analysis-techniques.md) for detailed analysis methods.

---

### Step 2: Analyze Technology Stack

**Purpose:** Identify languages, frameworks, and dependencies.

**Actions:**

1. Read package configuration:
   - **Node.js:** package.json
   - **Python:** requirements.txt, pyproject.toml
   - **Go:** go.mod
   - **Java:** pom.xml, build.gradle
   - **Rust:** Cargo.toml

2. Extract dependencies and identify frameworks:
   - Backend: Express, Django, Spring Boot, etc.
   - Frontend: React, Vue, Angular, etc.
   - Database: Prisma, TypeORM, SQLAlchemy, etc.
   - Testing: Jest, Pytest, JUnit, etc.

3. Detect runtime/platform:
   - Node.js/Python/JDK version
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
- jsonwebtoken: 9.0.2 (authentication)

Testing:
- Jest: 29.7.0 (test framework)
- Supertest: 6.3.3 (HTTP testing)

Confidence: High (95%)
```

---

### Step 3: Extract Data Models and Schemas

**Purpose:** Document data structures and validation rules.

**Actions:**

1. Locate data model files:
   - Prisma schema: `prisma/schema.prisma`
   - TypeScript interfaces: `src/types/*.ts`, `src/models/*.ts`
   - Database migrations: `prisma/migrations/`, `migrations/`
   - Validation schemas: Zod, Yup, Joi schemas

2. Parse data models and extract validation rules

3. Analyze relationships:
   - One-to-many, many-to-many
   - Foreign keys and constraints

4. Detect data flow:
   - Request → Validation → Service → Repository → Database
   - Response transformation (DTOs)

**Output:**
```
Data Models:

User Model:
- id: UUID (primary key)
- email: string (unique, validated: RFC 5322 format)
- password: string (hashed with bcrypt)
- createdAt: timestamp (auto-generated)

Validation Rules:
- Email: Must be valid format, max 255 chars
- Password: Min 8 chars, must contain uppercase, lowercase, number, special char

Relationships:
- User hasMany Posts (one-to-many)
- User hasMany Sessions (one-to-many)

Confidence: High (90%)
```

**Reference:** See [analysis-techniques.md](references/analysis-techniques.md) for model extraction patterns.

---

### Step 4: Analyze API Patterns

**Purpose:** Document API structure and conventions.

**Actions:**

1. Locate API definitions:
   - Express routes: `src/routes/**/*.ts`
   - Controllers: `src/controllers/**/*.ts`
   - OpenAPI/Swagger spec (if exists)
   - GraphQL schemas (if exists)

2. Extract endpoints and analyze request/response patterns:
   - Request validation (middleware)
   - Error response format
   - Success response format
   - Status codes used

3. Identify authentication:
   - JWT tokens, session-based, API keys, OAuth

4. Detect rate limiting and other middleware

**Output:**
```
API Specifications:

Base URL: /api

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

Confidence: High (85%)
```

---

### Step 5: Extract Coding Standards and Patterns

**Purpose:** Document implicit conventions and best practices.

**Actions:**

1. Analyze code style:
   - Read `.eslintrc`, `.prettierrc`, `tsconfig.json`
   - Detect: indentation, quotes, semicolons
   - Naming conventions: variables, functions, classes, files

2. Identify architectural patterns:
   - Design patterns: Repository, Factory, Strategy
   - Architectural style: Layered, Clean, Hexagonal

3. Extract error handling patterns:
   - Error classes
   - Centralized error handling
   - Logging patterns

4. Detect testing patterns:
   - Test organization
   - Mocking strategy
   - Test data management

**Output:**
```
Coding Standards:

Code Style:
- Indentation: 2 spaces
- Quotes: Single quotes
- Naming: camelCase (variables), PascalCase (classes), kebab-case (files)

Architectural Patterns:
1. Layered Architecture
   - Routes (presentation layer)
   - Services (business logic layer)
   - Repositories (data access layer)

2. Dependency Injection
3. Repository Pattern

Error Handling:
- Custom error classes (AppError, ValidationError)
- Centralized error handling middleware
- Never expose stack traces to clients

Confidence: High (90%)
```

**Reference:** See [pattern-detection.md](references/pattern-detection.md) for pattern identification techniques.

---

### Step 6: Generate Architecture Documentation

**Purpose:** Create comprehensive architecture.md from findings.

**Actions:**

1. Load architecture template structure

2. Populate sections with analyzed data from Steps 1-5:
   - Overview, tech stack, project structure
   - Data models, API specifications
   - Include confidence scores where applicable
   - Add source file references

3. Generate diagrams (optional):
   - Mermaid diagrams for architecture layers
   - Data model ERD
   - API endpoint map

4. Add human review notes for medium/low confidence sections

5. Write documentation file:
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

**Reference:** See [documentation-templates.md](references/documentation-templates.md) for template structures.

---

### Step 7: Generate Standards Documentation

**Purpose:** Create standards.md from discovered patterns.

**Actions:**

1. Extract standards from code analysis:
   - Security standards (from security practices)
   - Testing standards (from test patterns)
   - Code quality standards (from ESLint rules)
   - Performance standards (from observed patterns)

2. Document best practices:
   - Observed consistently across codebase
   - Mark as "discovered" vs "recommended"

3. Create standards document with examples and consistency scores

**Output:**
```
✓ Standards documentation generated
✓ File: docs/standards.md (850 lines)
✓ Standards extracted: 18
✓ Consistency scores: 75-100%
```

---

### Step 8: Generate Patterns Documentation

**Purpose:** Document discovered design patterns and conventions.

**Actions:**

1. Extract design patterns:
   - Repository, Factory, Strategy, Middleware patterns

2. Document usage examples:
   - Show code examples of each pattern
   - Explain when to use
   - Link to existing implementations

3. Identify anti-patterns:
   - Code smells detected
   - Inconsistencies
   - Technical debt

4. Create patterns document

**Output:**
```
✓ Patterns documentation generated
✓ File: docs/patterns.md (620 lines)
✓ Patterns identified: 8
✓ Anti-patterns noted: 3
```

**Reference:** See [pattern-detection.md](references/pattern-detection.md) for pattern documentation templates.

---

### Step 9: Validation and Confidence Scoring

**Purpose:** Score accuracy and identify areas needing human review.

**Actions:**

1. Calculate overall confidence:
   ```
   Confidence Scoring:

   Tech Stack:         95% (explicit in package.json)
   Project Structure:  90% (clear file organization)
   Data Models:        85% (some inferred relationships)
   API Specifications: 80% (missing OpenAPI spec)
   Coding Standards:   90% (ESLint + observed patterns)

   Overall Confidence: 88%
   ```

2. Identify low-confidence areas:
   - Sections with <70% confidence
   - Conflicting patterns found
   - Sparse or missing information

3. Generate human review checklist:
   ```markdown
   ## Human Review Required

   High Priority:
   - [ ] Verify API rate limiting implementation
   - [ ] Document deployment architecture
   - [ ] Confirm database connection pooling settings

   Medium Priority:
   - [ ] Verify password requirements match security policy
   - [ ] Document caching strategy (if exists)
   ```

4. Create validation report

**Output:**
```
✓ Validation complete
✓ Overall confidence: 88%
✓ High-priority review items: 3
✓ Medium-priority review items: 3
```

**Reference:** See [confidence-scoring.md](references/confidence-scoring.md) for scoring guidelines.

---

### Step 10: Summary and Next Steps

**Purpose:** Provide user with clear summary and action items.

**Actions:**

1. Generate summary report:
   ```markdown
   ## Automated Documentation Complete

   **Project:** {project-name}
   **Analysis Duration:** 8 minutes
   **Files Analyzed:** 247
   **Overall Confidence:** 88%

   **Generated Documentation:**
   - ✅ docs/architecture.md (2,450 lines)
   - ✅ docs/standards.md (850 lines)
   - ✅ docs/patterns.md (620 lines)

   **Key Findings:**
   - Project Type: Backend API (Express.js)
   - Architecture: Layered architecture
   - Tech Stack: TypeScript, Express, Prisma, PostgreSQL
   - Test Coverage: 78%

   **Next Steps:**
   1. Review generated documentation (especially low-confidence sections)
   2. Complete human review checklist (docs/REVIEW_CHECKLIST.md)
   3. Update configuration with correct paths
   4. Begin creating task specifications using architecture docs
   ```

2. Create review checklist file: `docs/REVIEW_CHECKLIST.md`

3. Update configuration:
   - Set `project.type: brownfield`
   - Set documentation paths
   - Set `brownfield.documented: true`

4. Prompt for next action:
   ```
   Documentation generation complete!

   Would you like to:
   A) Review high-priority items now
   B) Create first task specification using generated docs
   C) Run index-docs skill to create searchable knowledge base
   D) Exit (review later)
   ```

**Output:**
```
✓ Summary report generated
✓ Review checklist created: docs/REVIEW_CHECKLIST.md
✓ Configuration updated
✓ Ready for next phase
```

---

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
- **MUST be reviewed by human**

**Reference:** See [confidence-scoring.md](references/confidence-scoring.md) for detailed scoring methodology.

---

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

1. **Run Periodically:** Re-run every 3-6 months to keep docs fresh
2. **Always Review:** Don't trust 100% - always review low-confidence sections
3. **Supplement with Manual Docs:** Add business context, deployment details
4. **Use as Starting Point:** Generated docs are foundation, enhance with team input

## Integration with Planning Workflow

**Brownfield Workflow:**
1. **document-project** → Generate architecture docs
2. **index-docs** → Create searchable knowledge base
3. **create-task-spec** → Use docs for task creation

**Greenfield vs Brownfield:**
- **Greenfield:** Write architecture docs manually first
- **Brownfield:** Generate architecture docs from code, then refine

## References

- [analysis-techniques.md](references/analysis-techniques.md) - Detailed analysis methods for structure, tech stack, models, APIs
- [pattern-detection.md](references/pattern-detection.md) - Pattern identification and documentation techniques
- [documentation-templates.md](references/documentation-templates.md) - Templates for architecture, standards, patterns docs
- [confidence-scoring.md](references/confidence-scoring.md) - Confidence calculation methodology and validation criteria
