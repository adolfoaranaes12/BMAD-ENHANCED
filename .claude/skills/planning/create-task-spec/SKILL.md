---
name: create-task-spec
description: Create hyper-detailed task specifications with embedded context, eliminating implementation lookups. Use for breaking features into implementable tasks with complete architecture references.
acceptance:
  - task_file_created: "Task specification file created in configured location"
  - context_embedded: "All technical context embedded with source references"
  - tasks_defined: "3-15 sequential tasks with validation checkpoints"
  - user_approved: "User reviewed and approved specification"
inputs:
  requirement:
    type: string
    required: true
    description: "Feature or requirement to implement"
  priority:
    type: string
    required: false
    description: "Priority level (P0/P1/P2/P3)"
    default: "P2"
outputs:
  task_file:
    type: string
    description: "Path to created task specification file"
  task_id:
    type: string
    description: "Generated task ID (e.g., task-006)"
  task_count:
    type: number
    description: "Number of tasks in breakdown"
  status:
    type: string
    description: "Task status (Draft or Approved)"
telemetry:
  emit: "skill.create-task-spec.completed"
  track:
    - task_id
    - task_count
    - subtask_count
    - priority
    - status
    - duration_ms
---

# Create Task Specification Skill

## Purpose

Create hyper-detailed task specifications that embed ALL context needed for implementation, eliminating the need for developers to search for information during coding.

**Core Capabilities:**
- Requirement gathering and clarification
- Architecture context extraction with source references
- Component analysis (data models, APIs, UI)
- Sequential task breakdown with validation checkpoints
- Self-contained specifications

**BMAD Pattern (Key Innovation):**
- SM reads PRD + Architecture + Previous task notes
- Creates detailed task spec with embedded context
- Dev reads ONLY task spec (no architecture lookup)
- Result: Context never lost, implementation never blocked

## Prerequisites

- Configuration file (`.claude/config.yaml`) with task settings
- Task template (`.claude/templates/task-spec.md`)
- Architecture documentation (optional but recommended)
- Project coding standards

---

## Workflow

### Step 0: Load Configuration and Validate Prerequisites

**Action:** Load configuration and verify prerequisites.

**Execute:**
```bash
python .claude/skills/bmad-commands/scripts/read_file.py \
  --path .claude/config.yaml \
  --output json
```

**Extract Settings:**
- `documentation.architecture`: Architecture doc paths
- `development.alwaysLoadFiles`: Coding standards files
- `development.taskLocation`: Where to save task files
- `templates.taskSpec`: Task template location

**Verify:**
- Task location directory exists (create if needed)
- Template file exists
- Determine next task ID (highest existing + 1)

**Halt if:**
- Configuration file missing
- Template file missing
- Unable to determine next task ID

**See:** `references/requirements-gathering-guide.md` for detailed requirement clarification

---

### Step 1: Gather Requirements from User

**Action:** Clarify requirement, acceptance criteria, and priority.

**Ask user:**
1. **What needs to be implemented?**
   - Feature description
   - Problem it solves
   - Primary user/beneficiary

2. **What defines "done"?**
   - Testable outcomes
   - Acceptance criteria (2-5 specific criteria)
   - Edge cases to consider

3. **Priority and complexity?**
   - Priority: P0 (Critical) | P1 (High) | P2 (Medium) | P3 (Low)
   - Complexity: Simple | Medium | Complex
   - Related epic/feature

**Confirm understanding:**
- Restate as user story: As a [role], I want [action], so that [benefit]
- Verify acceptance criteria
- Get approval to proceed

**Halt if:**
- User cannot articulate requirement clearly
- Acceptance criteria are ambiguous
- User does not approve proceeding

**See:** `references/requirements-gathering-guide.md` for detailed gathering techniques

---

### Step 2: Load Architecture Context

**Action:** Load architecture documentation and previous task learnings.

**Load files:**

1. **Always-required files** (coding standards):
   ```bash
   python .claude/skills/bmad-commands/scripts/read_file.py \
     --path {always_load_file} \
     --output json
   ```

2. **Architecture documentation**:
   - Read `documentation.architecture` files
   - Extract: System design, patterns, conventions

3. **Previous task insights**:
   - Read most recent task file from `taskLocation`
   - Extract: Completion notes, lessons learned, patterns

**Context categories:**

**For ALL Tasks:**
- Tech stack (languages, frameworks, versions)
- Project structure (file organization)
- Coding standards (formatting, patterns)
- Testing strategy (frameworks, coverage)

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

**CRITICAL RULES:**
- ONLY extract information present in source documents
- NEVER invent technical details
- ALWAYS cite source file and section
- If info missing, note "No guidance found in architecture docs"

**See:** `references/context-extraction-guide.md` for detailed extraction strategies

---

### Step 3: Analyze Relevant Components

**Action:** Identify affected components and extract specific technical details.

**Identify components:**
- What data models are involved?
- What API endpoints need creation/modification?
- What UI components are affected?
- What external services are used?

**Extract details:**

**Data Models:**
- Schema definitions with types
- Validation rules
- Relationships and constraints
- [Source: architecture doc reference]

**API Specifications:**
- Endpoint paths and methods
- Request/response formats
- Authentication requirements
- Error handling patterns
- [Source: architecture doc reference]

**Component Specifications:**
- Component location and name
- Props and state shape
- Event handlers
- Styling approach
- [Source: architecture doc reference]

**File Locations:**
- Exact paths for new files
- Existing files to modify
- Test file locations
- [Source: project structure doc reference]

**Constraints:**
- **Performance:** Response time targets, query limits
- **Security:** Validation rules, authentication, authorization
- **Reliability:** Error handling, retry logic, fallbacks
- **Testing:** Test types required, coverage targets, mock strategies

**See:** `references/context-extraction-guide.md` for component analysis patterns

---

### Step 4: Create Sequential Task Breakdown

**Action:** Break requirement into 3-15 sequential tasks with subtasks.

**Task breakdown:**

1. **Break into 3-15 tasks:**
   - Each task implements specific functionality
   - Tasks build on each other logically
   - Each task maps to one or more acceptance criteria

2. **Create subtasks for each task:**
   - Specific implementation steps
   - Test writing requirements
   - Validation checkpoints

3. **Structure in implementation order:**
   - Data layer first (models, migrations)
   - Business logic second (services, utilities)
   - API layer third (routes, controllers)
   - UI layer fourth (components, pages)
   - Integration last (E2E tests, documentation)

4. **Link to acceptance criteria:**
   - Example: "Task 1: Create user model (AC: 1, 2)"

**Task structure example:**
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
```

**Halt if:**
- Unable to break down into coherent tasks
- Task count exceeds 15 (too complex, needs splitting)
- Task count less than 3 (too simple, doesn't need task spec)

**See:** `references/task-breakdown-guide.md` for detailed breakdown strategies

---

### Step 5: Populate Task Specification Template

**Action:** Generate task file from template with all context embedded.

**Load template:**
```bash
python .claude/skills/bmad-commands/scripts/read_file.py \
  --path .claude/templates/task-spec.md \
  --output json
```

**Replace placeholders:**
- `{{TASK_ID}}`: Generated task ID (e.g., task-006)
- `{{TASK_TITLE}}`: Brief, descriptive title
- `{{DATE}}`: Current date (YYYY-MM-DD)
- `{{PRIORITY}}`: P0/P1/P2/P3
- `{{STATUS}}`: "Draft" (always starts as draft)
- `{{USER_STORY}}`: As a [role], I want [action], so that [benefit]
- `{{ACCEPTANCE_CRITERIA}}`: List of 2-5 ACs
- `{{CONTEXT}}`: Embedded technical context with source references
- `{{TASKS}}`: Sequential task breakdown
- `{{VALIDATION}}`: Validation requirements

**Ensure context includes:**
- Previous task insights (patterns, learnings)
- Data models (with schemas)
- API specifications (with examples)
- Component specifications (with structure)
- File locations (exact paths)
- Testing requirements (types, coverage)
- Technical constraints (performance, security)
- ALL with [Source: filename#section] references

---

### Step 6: Validate Task Specification Completeness

**Action:** Verify all required elements are present and properly formatted.

**Validation checklist:**

**Required Sections:**
- [ ] Status (Draft)
- [ ] Objective (clear user story)
- [ ] Acceptance Criteria (2-5 specific criteria)
- [ ] Context section with embedded details
- [ ] Tasks / Subtasks (3-15 tasks)
- [ ] Implementation Record (empty placeholder)

**Context Completeness:**
- [ ] Previous insights referenced
- [ ] Data models included (if applicable)
- [ ] API specs included (if applicable)
- [ ] Component specs included (if applicable)
- [ ] File locations specified
- [ ] Testing requirements documented
- [ ] All context has [Source: ...] references

**Task Quality:**
- [ ] Tasks in logical implementation order
- [ ] Each task linked to acceptance criteria
- [ ] Subtasks include test writing steps
- [ ] Validation checkpoints included
- [ ] File paths are specific, not generic

**Halt if:**
- Critical sections missing
- Context lacks source references
- Tasks are ambiguous or generic
- No validation checkpoints

**See:** `references/validation-approval-guide.md` for validation details

---

### Step 7: Save Task Specification and Get User Approval

**Action:** Save task file and present summary for approval.

**Save file:**
```bash
python .claude/skills/bmad-commands/scripts/write_file.py \
  --path {taskLocation}/{task_id}.md \
  --content "{task_spec}" \
  --output json
```

**Present summary:**
```markdown
## Task Specification Created

**Task ID:** task-006-user-signup
**File:** .claude/tasks/task-006-user-signup.md
**Status:** Draft

**Objective:**
As a new user, I want to create an account with email and password,
so that I can access personalized features.

**Acceptance Criteria:**
1. User can signup with valid email/password
2. Password security requirements enforced
3. Duplicate emails prevented
4. Confirmation email sent

**Task Breakdown:**
- Task 1: Create user model (AC: 1, 2)
- Task 2: Implement signup service (AC: 1, 3)
- Task 3: Create API endpoint (AC: 1, 4)
- Task 4: Add email verification (AC: 4)
- Task 5: Write comprehensive tests (AC: all)

**Total:** 5 tasks, 20 subtasks

**Context Embedded:**
- User model schema [Source: docs/architecture/data-models.md#user]
- Auth API spec [Source: docs/architecture/rest-api-spec.md#auth]
- Testing strategy [Source: docs/standards.md#testing]
- Previous auth patterns [Source: task-003 completion notes]

**Ready for implementation? (yes/no)**
```

**Update status if approved:**
- Change status from "Draft" to "Approved"
- Task ready for execute-task skill

**See:** `references/validation-approval-guide.md` for approval workflow

---

## Output

Return structured output with telemetry:

```json
{
  "task_file": ".claude/tasks/task-006-user-signup.md",
  "task_id": "task-006",
  "task_count": 5,
  "status": "Approved",
  "telemetry": {
    "skill": "create-task-spec",
    "task_id": "task-006",
    "task_count": 5,
    "subtask_count": 20,
    "priority": "P1",
    "status": "Approved",
    "duration_ms": 325000
  }
}
```

---

## Best Practices

1. **Context Embedding is Critical** - Implementation skill should NEVER need to read architecture docs
2. **Be Specific, Not Generic** - Include exact file paths, schemas, API specs
3. **Source Everything** - Every technical claim needs [Source: filename#section]
4. **Learn from Previous Tasks** - Read most recent task completion notes
5. **Validation Checkpoints** - Every task needs tests and validation steps
6. **Task Granularity** - 3-15 tasks (if >15, too complex; if <3, too simple)
7. **Halt When Uncertain** - Missing critical info: halt and ask user

**See:** `references/task-breakdown-guide.md` for detailed best practices

---

## Routing Guidance

**Use this skill when:**
- Breaking features into implementable tasks
- Creating detailed specifications for development
- Embedding architectural context for implementation
- Need clear, unambiguous work items

**Always use before:**
- execute-task skill (implementation)
- Task must be "Approved" status

**Do not use for:**
- Quick bug fixes (too much overhead)
- Urgent hotfixes (too structured)
- Exploratory coding (too constrained)

---

## Reference Files

Detailed documentation in `references/`:

- **requirements-gathering-guide.md**: Clarifying requirements, acceptance criteria, user stories
- **context-extraction-guide.md**: Loading architecture, extracting technical details, sourcing
- **task-breakdown-guide.md**: Creating sequential tasks, granularity, validation checkpoints
- **validation-approval-guide.md**: Completeness validation, saving, approval workflow

---

## Using This Skill

**From command line:**
```bash
Use .claude/skills/planning/create-task-spec/SKILL.md with input {requirement: "User signup with email/password"}
```

---

## Philosophy

This skill embodies BMAD's 3-layer architecture:

- **Uses Commands** (Layer 1): bmad-commands for read_file, write_file
- **Provides Composition** (Layer 2): Planning + context extraction workflow
- **Enables Orchestration** (Layer 3): Used by planning agents/subagents

By embedding context, this skill is:
- **Observable**: Telemetry tracks task creation metrics
- **Testable**: Output format is predictable
- **Composable**: Feeds into execute-task skill
- **Reliable**: Context embedded at planning time

---

*Part of BMAD Enhanced Planning Suite*
