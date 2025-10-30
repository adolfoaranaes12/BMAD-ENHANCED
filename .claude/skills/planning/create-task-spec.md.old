# Planning Skill: Create Task Specification

<!-- BMAD Enhanced Planning Skill -->
<!-- Inspired by BMAD-METHOD SM agent story creation pattern -->
<!-- Version: 1.0 -->

## Purpose

Create hyper-detailed task specifications that embed ALL context needed for implementation, eliminating the need for developers to search for information during coding.

**Key Innovation (BMAD Pattern):**
- SM reads PRD + Architecture + Previous task notes
- Creates detailed task spec with embedded context
- Dev reads ONLY task spec (no architecture lookup)
- Result: Context never lost, implementation never blocked

## When to Use This Skill

Use this skill when you need to:
- Break down a feature into implementable tasks
- Prepare detailed specifications for implementation
- Ensure all architectural context is embedded
- Create clear, unambiguous work items

**Do NOT use this skill for:**
- Quick bug fixes (use simplified approach)
- Urgent hotfixes (too much overhead)
- Exploratory coding (too constrained)

## SEQUENTIAL Task Execution

**CRITICAL:** Do not proceed to next step until current step is complete

### Step 0: Load Configuration and Validate Prerequisites

**Actions:**

1. Load `.claude/config.yaml` from project root
   - If missing: HALT with error "Configuration file not found at .claude/config.yaml"
   - Extract key settings:
     - `documentation.architecture`
     - `documentation.standards`
     - `development.alwaysLoadFiles`
     - `development.taskLocation`
     - `templates.taskSpec`

2. Verify prerequisites:
   - Task location directory exists (create if needed)
   - Template file exists at configured location
   - Architecture documents accessible

3. Check for existing tasks:
   - List files in `taskLocation`
   - Identify highest task number (e.g., task-005.md → 5)
   - Next task ID = highest + 1, zero-padded to 3 digits (e.g., task-006)

**Halt Conditions:**
- Configuration file missing
- Template file missing
- Unable to determine next task ID

### Step 1: Gather Requirements from User

**Actions:**

1. Ask user for feature/requirement description
   - What needs to be implemented?
   - What problem does it solve?
   - Who is the primary user/beneficiary?

2. Clarify acceptance criteria:
   - What defines "done" for this task?
   - What are the testable outcomes?
   - Are there any edge cases to consider?

3. Assess priority and complexity:
   - Priority: P0 (Critical) | P1 (High) | P2 (Medium) | P3 (Low)
   - Complexity estimate: Simple | Medium | Complex
   - Related epic/feature (if applicable)

4. Confirm understanding with user:
   - Restate requirement in user story format
   - Verify acceptance criteria
   - Get approval to proceed with detailed planning

**Output:**
- Clear user story: As a [role], I want [action], so that [benefit]
- 2-5 acceptance criteria (specific, testable)
- Priority and complexity assessment
- User confirmation to proceed

**Halt Conditions:**
- User cannot articulate requirement clearly
- Acceptance criteria are ambiguous
- User does not approve proceeding

### Step 2: Load Architecture Context

**Actions:**

1. Load always-required files:
   - Read each file in `development.alwaysLoadFiles` from config
   - Extract: Coding standards, tech stack, project structure

2. Load architecture documentation:
   - Read `documentation.architecture` (full file or relevant sections)
   - Extract: System design, patterns, conventions

3. Load standards documentation:
   - Read `documentation.standards`
   - Extract: Security rules, performance targets, testing requirements

4. Load previous task insights (if tasks exist):
   - Read most recent task file from `taskLocation`
   - Extract: Completion notes, lessons learned, implementation decisions
   - Identify patterns established in previous work

**Context Gathering Strategy:**

**For ALL Tasks:**
- Tech stack (languages, frameworks, versions)
- Project structure (file organization, naming conventions)
- Coding standards (formatting, patterns, best practices)
- Testing strategy (frameworks, coverage targets, test types)

**For Backend/API Tasks:**
- Data models and schemas
- Database design and relationships
- API endpoint specifications
- External service integrations
- Authentication/authorization patterns

**For Frontend/UI Tasks:**
- Component specifications
- State management patterns
- Routing structure
- UI/UX guidelines
- Accessibility requirements

**For Full-Stack Tasks:**
- Both backend and frontend contexts above

**CRITICAL RULES:**
- ONLY extract information present in source documents
- NEVER invent technical details not in docs
- ALWAYS cite source file and section
- If info missing, note "No guidance found in architecture docs"

**Output:**
- Extracted technical context organized by category
- All context includes source references [Source: filename#section]
- Previous task insights and patterns identified
- Gaps in architecture documentation noted

**Halt Conditions:**
- Architecture documents not found
- Architecture documents unreadable/corrupted
- Critical information missing (user decides if halt needed)

### Step 3: Analyze Relevant Components

**Actions:**

1. Identify affected components based on requirement:
   - What data models are involved?
   - What API endpoints need creation/modification?
   - What UI components are affected?
   - What external services are used?

2. Extract specific technical details for each component:
   - **Data Models:**
     - Schema definitions with types
     - Validation rules
     - Relationships and constraints
     - [Source: architecture doc reference]

   - **API Specifications:**
     - Endpoint paths and methods
     - Request/response formats
     - Authentication requirements
     - Error handling patterns
     - [Source: architecture doc reference]

   - **Component Specifications:**
     - Component location and name
     - Props and state shape
     - Event handlers
     - Styling approach
     - [Source: architecture doc reference]

   - **File Locations:**
     - Exact paths for new files
     - Existing files to modify
     - Test file locations
     - [Source: project structure doc reference]

3. Extract constraints and requirements:
   - **Performance:** Response time targets, query limits
   - **Security:** Validation rules, authentication, authorization
   - **Reliability:** Error handling, retry logic, fallbacks
   - **Testing:** Test types required, coverage targets, mock strategies

4. Cross-reference with previous implementations:
   - What patterns were established?
   - What libraries/utilities already exist?
   - What lessons learned apply?

**Output:**
- Detailed technical specifications for each component
- All specs include source references
- Constraints and requirements documented
- Previous patterns identified for reuse

**Halt Conditions:**
- Unable to identify affected components
- Critical technical details missing from architecture
- Conflicting information in architecture docs

### Step 4: Create Sequential Task Breakdown

**Actions:**

1. Break requirement into 3-15 sequential tasks:
   - Each task implements a specific piece of functionality
   - Tasks build on each other logically
   - Each task maps to one or more acceptance criteria

2. For each task, create subtasks:
   - Specific implementation steps
   - Test writing requirements
   - Validation checkpoints

3. Structure tasks in implementation order:
   - Data layer first (models, migrations, repositories)
   - Business logic second (services, utilities)
   - API layer third (routes, controllers)
   - UI layer fourth (components, pages)
   - Integration last (E2E tests, documentation)

4. Reference acceptance criteria:
   - Link each task to applicable AC numbers
   - Example: "Task 1: Create user model (AC: 1, 2)"

5. Include validation steps:
   - After each task: Write tests + Run validations
   - Before marking complete: Verify acceptance criteria

**Task Structure Example:**
```markdown
- [ ] Task 1: Create user data model (AC: 1, 2)
  - [ ] Define User interface in src/types/user.ts
  - [ ] Create user schema with Zod validation
  - [ ] Add database migration for users table
  - [ ] Write unit tests for validation logic
  - [ ] Validate: Model matches architecture spec

- [ ] Task 2: Implement signup service logic (AC: 1, 3)
  - [ ] Create signup.service.ts with user creation logic
  - [ ] Implement password hashing with bcrypt
  - [ ] Add duplicate email check
  - [ ] Write unit tests for service methods
  - [ ] Validate: All edge cases covered

- [ ] Task 3: Create signup API endpoint (AC: 1, 4)
  - [ ] Add POST /api/auth/signup route
  - [ ] Implement request validation middleware
  - [ ] Connect route to signup service
  - [ ] Add error handling
  - [ ] Write integration tests for endpoint
  - [ ] Validate: API matches spec from architecture
```

**Output:**
- 3-15 sequential tasks with subtasks
- Each task linked to acceptance criteria
- Validation checkpoints included
- Tasks follow logical implementation order

**Halt Conditions:**
- Unable to break down into coherent tasks
- Task count exceeds 15 (too complex, needs splitting)
- Task count less than 3 (too simple, doesn't need task spec)

### Step 5: Populate Task Specification Template

**Actions:**

1. Load template from configured location:
   - Read `.claude/templates/task-spec.md`

2. Replace template placeholders:
   - `{{TASK_ID}}`: Generated task ID (e.g., task-006)
   - `{{TASK_TITLE}}`: Brief, descriptive title
   - `{{DATE}}`: Current date (YYYY-MM-DD)
   - `{{EPIC_OR_FEATURE}}`: Related epic/feature name
   - `{{PRIORITY}}`: P0/P1/P2/P3
   - `{{STATUS}}`: "Draft" (always starts as draft)
   - `{{ROLE}}`: User role from story
   - `{{ACTION}}`: Action from story
   - `{{BENEFIT}}`: Benefit from story

3. Populate Acceptance Criteria section:
   - List all criteria from Step 1
   - Ensure specific and testable

4. Populate Context section with extracted details:
   - **Previous Task Insights:** Learnings from Step 2
   - **Data Models:** Schemas and validation from Step 3
   - **API Specifications:** Endpoint details from Step 3
   - **Component Specifications:** UI details from Step 3 (if applicable)
   - **File Locations:** Exact paths from Step 3
   - **Testing Requirements:** Test strategy from Step 2
   - **Technical Constraints:** Performance, security, etc. from Step 3
   - **CRITICAL:** Every technical detail includes [Source: filename#section]

5. Populate Tasks / Subtasks section:
   - Copy task breakdown from Step 4
   - Ensure all checkboxes are unchecked ([ ])
   - Verify AC references included

6. Leave Implementation Record empty:
   - This section is for implementation skill only
   - Template placeholders remain

7. Leave Quality Review empty:
   - This section is for quality skill only
   - Template placeholders remain

8. Populate Change Log:
   - First entry: "Initial task specification created"
   - Author: planning-skill-v1.0
   - Date: Current date

**Output:**
- Complete task specification file
- All context embedded with source references
- Tasks clearly defined and sequenced
- Placeholders for implementation and review sections

**Halt Conditions:**
- Template file malformed or unreadable
- Unable to populate required sections

### Step 6: Validate Task Specification Completeness

**Actions:**

1. Run completeness checklist:
   - [ ] Objective clearly states user story
   - [ ] 2-5 specific, testable acceptance criteria
   - [ ] Context section contains relevant technical details
   - [ ] All technical details include source references
   - [ ] Tasks are sequential and logical
   - [ ] Each task links to applicable AC
   - [ ] Validation steps included after each task
   - [ ] No invented information (all from source docs)
   - [ ] Gaps in architecture explicitly noted

2. Verify source references:
   - Each technical claim includes [Source: ...]
   - Source files are accessible
   - Sections can be verified

3. Check for ambiguities:
   - Are requirements clear and unambiguous?
   - Could implementation proceed without questions?
   - Are all file paths specific?
   - Are all schemas fully defined?

4. Assess context sufficiency:
   - Would implementation skill need to read architecture docs?
   - Are all patterns and standards embedded?
   - Are previous learnings incorporated?

**Self-Assessment Questions:**
- Can this task be implemented without loading architecture docs?
- Are all technical decisions explained with rationale?
- Are edge cases and error conditions addressed?
- Is the task breakdown logical and complete?

**Output:**
- Completeness checklist results
- List of any gaps or ambiguities
- Recommendation: Proceed or revise

**Halt Conditions:**
- Critical completeness checks failed
- Major ambiguities identified
- Context insufficient for implementation

### Step 7: Save Task Specification and Get User Approval

**Actions:**

1. Generate task file path:
   - Format: `{taskLocation}/{taskId}-{slug}.md`
   - Example: `.claude/tasks/task-006-user-signup.md`
   - Slug: lowercase, hyphenated title (max 50 chars)

2. Write task specification to file

3. Present summary to user:
   ```markdown
   ## Task Specification Created

   **File:** .claude/tasks/task-006-user-signup.md
   **Status:** Draft
   **Priority:** P1 (High)

   **Objective:**
   As a new user, I want to create an account with email and password,
   so that I can access the application features.

   **Acceptance Criteria:**
   1. User can signup with valid email and password
   2. Password meets security requirements (8+ chars, complexity)
   3. Duplicate emails prevented
   4. Confirmation email sent after signup

   **Context Embedded:**
   - Data Models: User schema with validation rules
   - API Specs: POST /api/auth/signup endpoint details
   - File Locations: Exact paths for implementation
   - Testing: 12 test scenarios across unit/integration/E2E
   - Previous Patterns: Reusing auth middleware from task-003

   **Task Breakdown:**
   - 5 main tasks with 18 subtasks total
   - Maps to all 4 acceptance criteria
   - Includes comprehensive test coverage

   **Completeness Check:**
   ✓ All context embedded with source references
   ✓ No architecture lookup needed during implementation
   ✓ Clear, sequential task structure

   **Next Steps:**
   1. Review task specification file
   2. If approved, mark status as "Approved"
   3. Hand off to implementation skill for execution

   **Review the task? (yes/no)**
   ```

4. Get user feedback:
   - If user requests changes: Return to appropriate step
   - If user approves: Mark status as "Approved" in file
   - If user wants to review file first: Wait for user to read and approve

5. Update status to "Approved" if user confirms:
   - Edit task file status line from "Draft" to "Approved"
   - Add change log entry for approval

**Output:**
- Task specification file saved
- User presented with clear summary
- Status updated based on user approval

**Halt Conditions:**
- File write fails
- User requests major revisions (restart from appropriate step)

## Completion Criteria

Task specification creation is complete when:

- [ ] Task file created in configured location
- [ ] All context embedded with source references
- [ ] Sequential tasks with validation checkpoints
- [ ] Completeness validation passed
- [ ] User reviewed and approved
- [ ] Status updated to "Approved"

## Usage Example

**User:** "I need to implement user signup functionality"

**Planning Skill:**

1. Clarifies requirements:
   - User story: As a new user, I want to create account...
   - AC: Valid email/password, security requirements, duplicate prevention, email confirmation
   - Priority: P1 (High)

2. Loads architecture context:
   - User model schema from docs/architecture/data-models.md
   - Auth API spec from docs/architecture/rest-api-spec.md
   - Testing strategy from docs/standards.md
   - Previous auth patterns from task-003

3. Extracts technical details:
   - Data model: User interface, Zod validation schema
   - API: POST /api/auth/signup with request/response formats
   - Files: Exact paths for services, routes, tests
   - Security: bcrypt cost 12, input validation, rate limiting
   - Testing: 12 scenarios across unit/integration/E2E

4. Creates task breakdown:
   - Task 1: Create user model (AC: 1, 2)
   - Task 2: Implement signup service (AC: 1, 3)
   - Task 3: Create API endpoint (AC: 1, 4)
   - Task 4: Add email verification (AC: 4)
   - Task 5: Write comprehensive tests (AC: all)

5. Generates task specification:
   - File: `.claude/tasks/task-006-user-signup.md`
   - All context embedded
   - All technical details have [Source: ...] references
   - Ready for implementation without architecture lookup

6. Gets user approval → Status: Approved

**Result:** Complete, self-contained task specification ready for implementation skill

## Best Practices

1. **Context Embedding is Critical:**
   - Implementation skill should NEVER need to read architecture docs
   - Embed specific technical details, not general guidance
   - Include source references for traceability

2. **Be Specific, Not Generic:**
   - Bad: "Create user model"
   - Good: "Create User interface with id (UUID), email (string, unique), password (string, bcrypt hashed) in src/types/user.ts [Source: docs/architecture/data-models.md#user]"

3. **Source Everything:**
   - Every technical claim needs [Source: filename#section]
   - If no source exists, note: "No guidance in architecture docs"
   - Never invent technical details

4. **Learn from Previous Tasks:**
   - Read most recent task completion notes
   - Identify established patterns
   - Reuse successful approaches
   - Avoid repeating mistakes

5. **Validation Checkpoints:**
   - Every task needs validation step
   - Every task needs tests written
   - Final validation checks all acceptance criteria

6. **Task Granularity:**
   - 3-15 tasks (if >15, task is too complex)
   - Each task completable in reasonable session
   - Each task produces testable output

7. **Halt When Uncertain:**
   - Missing critical architecture info: Halt, ask user
   - Ambiguous requirements: Halt, clarify
   - Conflicting information: Halt, resolve

## Common Pitfalls to Avoid

1. **Inventing Technical Details:**
   - ❌ Don't: Assume database schema if not in docs
   - ✅ Do: Note "No user schema found in architecture docs" and ask user

2. **Generic Context:**
   - ❌ Don't: "Follow REST best practices"
   - ✅ Do: "POST /api/auth/signup returns 201 with user object and JWT token [Source: docs/architecture/rest-api-spec.md#auth]"

3. **Missing Source References:**
   - ❌ Don't: "Password must be hashed with bcrypt"
   - ✅ Do: "Password must be hashed with bcrypt, cost 12 [Source: docs/standards.md#security]"

4. **Skipping Previous Learnings:**
   - ❌ Don't: Start fresh without checking previous tasks
   - ✅ Do: Review most recent task completion notes and reuse patterns

5. **Ambiguous Tasks:**
   - ❌ Don't: "Implement authentication"
   - ✅ Do: "Create signup endpoint with email validation, password hashing, and duplicate email prevention (AC: 1, 2, 3)"

6. **Missing Validation:**
   - ❌ Don't: Just list implementation steps
   - ✅ Do: Include test writing and validation checkpoints after each task

## Integration with Other Skills

**Before This Skill:**
- User provides requirement or feature request
- Optional: Architecture documents reviewed by user

**After This Skill:**
- Task specification file exists with status "Approved"
- Implementation skill can execute without context lookup
- Quality skill can later validate against embedded context

**Handoff to Implementation Skill:**
```
Task specification ready for implementation:
- File: .claude/tasks/task-006-user-signup.md
- Status: Approved
- All context embedded
- Ready for sequential execution

Next: Use implementation skill to execute tasks
```

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-10-28 | Initial planning skill based on BMAD SM agent pattern |

---

**End of Planning Skill**
