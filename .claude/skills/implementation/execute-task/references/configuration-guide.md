# Configuration Guide

## Purpose

Load configuration, always-load files, verify task status, and initialize execution environment.

---

## Step 0: Load Configuration and Task Specification

### 1. Load Configuration File

**Action:** Read `.claude/config.yaml` to extract development settings.

**Execute:**
```bash
python .claude/skills/bmad-commands/scripts/read_file.py \
  --path .claude/config.yaml \
  --output json
```

**Parse Response:**
```json
{
  "success": true,
  "outputs": {
    "content": "..."
  }
}
```

**Extract Settings:**
```yaml
development:
  alwaysLoadFiles:
    - docs/coding-standards.md
    - docs/project-conventions.md
  debugLog: true

workflow:
  haltOn:
    consecutiveFailures: 3
    ambiguousRequirements: true
    missingDependencies: true

skills:
  implementation:
    autoConfirm: false
    validateBeforeCheckbox: true
```

**Key Settings:**
- `development.alwaysLoadFiles`: Files to load for every task (coding standards)
- `development.debugLog`: Whether to log detailed debug info
- `workflow.haltOn.consecutiveFailures`: How many failures before halting (default: 3)
- `skills.implementation.autoConfirm`: Skip execution plan confirmation (default: false)
- `skills.implementation.validateBeforeCheckbox`: Require validation before marking complete (default: true)

---

### 2. Load Task Specification

**Action:** Read task file and parse structure.

**Get Task File Path:**
- From user input (e.g., `.claude/tasks/task-006-user-signup.md`)
- Verify file exists

**Execute:**
```bash
python .claude/skills/bmad-commands/scripts/read_file.py \
  --path .claude/tasks/task-006-user-signup.md \
  --output json
```

**Parse Task Specification:**

```markdown
## Status
Approved

## Objective
Implement user signup with email and password...

## Acceptance Criteria
1. User can signup with valid email/password
2. Password security requirements enforced
3. Duplicate emails prevented
4. Confirmation email sent

## Context

### Previous Insights
- Used bcrypt from task-003 with cost 12
- Email service already configured

### Data Models
...

### API Specifications
POST /api/auth/signup
...

### Tasks / Subtasks
- [ ] Task 1: Create user model
  - [ ] Define User interface
  - [ ] Create Zod schema
  - [ ] Database migration
  - [ ] Write unit tests
  - [ ] Validate model
- [ ] Task 2: Implement signup service
  ...

## Implementation Record
[To be populated during execution]
```

**Extract:**
- `status`: Current task status (must be "Approved")
- `objective`: What the task aims to achieve
- `acceptance_criteria`: List of ACs to verify
- `context`: Embedded context sections
- `tasks`: Task and subtask list with checkboxes

---

### 3. Verify Task Status

**Action:** Ensure task is ready for implementation.

**Status Check:**

**If status == "Draft":**
```markdown
❌ Task cannot be executed

**Status:** Draft
**Reason:** Task must be approved before implementation

**Next Steps:**
1. Complete task planning
2. Have task spec reviewed
3. Update status to "Approved"
4. Re-run execute-task skill
```
**HALT** - Do not proceed

**If status == "InProgress":**
```markdown
⚠️ Task Already In Progress

**Status:** InProgress
**Reason:** Task execution may have started previously

**Options:**
1. Continue from last checkpoint (recommended)
2. Restart from beginning (will lose progress)

**Continue execution? (yes/no)**
```
**Wait for user confirmation**

**If status == "Review" or "Done":**
```markdown
❌ Task Already Complete

**Status:** Review/Done
**Reason:** Task has already been executed

**If you need to modify:**
1. Create new task with changes
2. Update original task status to "Draft"
3. Re-execute
```
**HALT** - Do not proceed

**If status == "Approved":** ✅ Proceed to next step

---

### 4. Load Always-Load Files

**Action:** Load coding standards and conventions referenced in config.

**For each file in `development.alwaysLoadFiles`:**

```bash
python .claude/skills/bmad-commands/scripts/read_file.py \
  --path docs/coding-standards.md \
  --output json
```

**Parse Content:**
- Extract coding standards
- Extract project conventions
- Extract naming patterns
- Extract testing requirements

**Example Always-Load File:**
```markdown
# Coding Standards

## File Naming
- Components: PascalCase (UserProfile.tsx)
- Services: camelCase with .service (auth.service.ts)
- Tests: .test or .spec suffix (auth.service.test.ts)

## Testing
- All services require unit tests (≥80% coverage)
- All API endpoints require integration tests
- Complex flows require E2E tests

## Error Handling
- Use custom error classes (AuthError, ValidationError)
- Always log errors with context
- Return 4xx for client errors, 5xx for server errors
```

**Purpose:**
These files provide context-agnostic standards that apply to all tasks, avoiding repetition in every task spec.

---

### 5. Update Task Status to "InProgress"

**Action:** Mark task as actively being implemented.

**Edit Task File:**
- Locate "## Status" section
- Change status from "Approved" to "InProgress"
- Add start timestamp to Implementation Record

**Example:**
```markdown
## Status
InProgress

## Implementation Record

**Started:** 2025-10-29 11:30 AM
**Agent:** Claude Code (execute-task skill)
```

**Verification:**
- Read task file again to confirm update
- Proceed only if status successfully updated

---

## Output

After Step 0 completion:

- ✅ Configuration loaded and parsed
- ✅ Task specification loaded and parsed
- ✅ Task status verified (was "Approved")
- ✅ Always-load files (coding standards) loaded
- ✅ Task status updated to "InProgress"
- ✅ Start timestamp recorded

**Ready for:** Step 1 (Review Context and Plan Execution)

---

## Halt Conditions

**Must halt if:**

1. **Configuration file missing**
   - `.claude/config.yaml` not found
   - Action: Create configuration file

2. **Task file missing or unreadable**
   - File path invalid
   - File permissions issue
   - Action: Verify file path and permissions

3. **Task status not "Approved"**
   - Status is Draft, InProgress, Review, or Done
   - Action: See status check section above

4. **Always-load files missing**
   - Files specified in config don't exist
   - Action: Create missing files or update config

5. **bmad-commands not available**
   - read_file.py script not found
   - Action: Verify bmad-commands skill installed

---

## Configuration Examples

### Minimal Configuration

```yaml
development:
  alwaysLoadFiles:
    - docs/standards.md

workflow:
  haltOn:
    consecutiveFailures: 3
```

### Complete Configuration

```yaml
development:
  alwaysLoadFiles:
    - docs/coding-standards.md
    - docs/architecture-patterns.md
    - docs/testing-requirements.md
  debugLog: true
  testFramework: jest

workflow:
  haltOn:
    consecutiveFailures: 3
    ambiguousRequirements: true
    missingDependencies: true
    regressionFailures: true

skills:
  implementation:
    autoConfirm: false
    validateBeforeCheckbox: true
    updateCheckboxes: true
    allowStatusChange: ["Approved->InProgress", "InProgress->Review"]
```

---

## Quick Reference

**Load Configuration:**
```bash
read_file.py --path .claude/config.yaml
```

**Load Task Spec:**
```bash
read_file.py --path {task_file}
```

**Verify Status:**
- Must be "Approved" to proceed
- Update to "InProgress" when starting

**Load Standards:**
- Load each file in `alwaysLoadFiles`
- Apply standards throughout implementation

---

*Part of execute-task skill - Implementation Suite*
