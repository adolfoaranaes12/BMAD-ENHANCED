# Permissions & Halt Conditions Guide

## Purpose

Define strict permission boundaries for file modifications and halt conditions for error handling.

---

## File Modification Permissions

### AUTHORIZED Modifications

**1. Implementation Record Section**

✅ **Can Edit:**
```markdown
## Implementation Record

### Agent Model Used
[Edit: Add model identifier]

### Debug Log References
[Edit: Add debug entries]

### Completion Notes
[Edit: Add implementation notes]

### Files Modified
[Edit: Add file lists]

### Testing Results
[Edit: Add test results]
```

**2. Task/Subtask Checkboxes**

✅ **Can Edit:**
```markdown
- [ ] Task 1: Description → - [x] Task 1: Description
  - [ ] Subtask 1.1 → - [x] Subtask 1.1
```

**Only change [ ] to [x], never modify descriptions**

**3. Status Line**

✅ **Can Edit:**
```markdown
## Status
Approved → InProgress → Review
```

**Never change to "Done" - only quality skill can do that**

---

### PROHIBITED Modifications

**❌ Cannot Edit:**

**1. Objective Section**
```markdown
## Objective
[NEVER MODIFY THIS]
```

**2. Acceptance Criteria Section**
```markdown
## Acceptance Criteria
1. [NEVER MODIFY THIS]
2. [NEVER MODIFY THIS]
```

**3. Context Section**
```markdown
## Context

### Previous Insights
[NEVER MODIFY THIS]

### Data Models
[NEVER MODIFY THIS]

### API Specifications
[NEVER MODIFY THIS]
```

**4. Task/Subtask Descriptions**
```markdown
- [ ] Task 1: Create user model ← CANNOT MODIFY THIS TEXT
  - [ ] Define User interface ← CANNOT MODIFY THIS TEXT
```

**Can only change [ ] to [x], not the description**

**5. Quality Review Section**
```markdown
## Quality Review
[NEVER MODIFY THIS - quality skill owns this]
```

---

## Permission Enforcement

### Before Each Edit

**1. Verify section:**
```typescript
function canEdit(section: string): boolean {
  const allowedSections = [
    'Implementation Record',
    'Status'
  ];

  return allowedSections.some(allowed =>
    section.includes(allowed)
  );
}
```

**2. Verify operation:**
```typescript
// Checkbox update: OK if only changing [ ] to [x]
function isCheckboxUpdate(before: string, after: string): boolean {
  const beforeUnchecked = before.replace('- [ ]', '');
  const afterChecked = after.replace('- [x]', '');
  return beforeUnchecked === afterChecked;
}
```

### If Permission Violation Detected

**HALT immediately:**
```markdown
⚠️ PERMISSION VIOLATION DETECTED

**Attempted Action:** Modify Acceptance Criteria section
**Reason:** This section is read-only for execute-task skill
**Impact:** Could corrupt task specification

**Authorized Actions Only:**
- Update Implementation Record section
- Update checkboxes ([ ] to [x])
- Update status (Approved → InProgress → Review)

**Execution halted to prevent corruption.**
```

---

## Halt Conditions

### 1. Consecutive Failures

**Trigger:** Same subtask fails 3 times in a row (configurable)

**Halt Message:**
```markdown
⚠️ EXECUTION HALTED

**Reason:** Consecutive Failures (3 attempts)
**Subtask:** Task 2, Subtask 2.3 - Database migration
**Current Task:** Task 2: Implement signup service

**Failure History:**
1. Attempt 1 (11:45 AM): Syntax error in SQL (CREATE TABEL typo)
2. Attempt 2 (11:50 AM): Foreign key constraint error (referenced table not found)
3. Attempt 3 (11:55 AM): Duplicate table error (table already exists from previous attempts)

**Current Issue:**
Cannot determine correct approach:
- Should migration be idempotent (DROP IF EXISTS)?
- Should existing table be kept?
- Should migration be rolled back first?

**Need from User:**
- Confirm migration strategy (idempotent vs. clean slate)
- Or: Provide corrected SQL migration
- Or: Skip this subtask and proceed (not recommended)

**Current Progress:**
- ✓ Task 1 complete (5 subtasks)
- ⏸ Task 2 halted at subtask 2.3 (3 of 4 subtasks)
- ⏹ Task 3-5 not started

**Ready to Resume:** Once migration strategy clarified
```

**User Actions:**
- Provide guidance on approach
- Provide corrected code
- Request skip (not recommended)
- Request abort and task replan

---

### 2. Ambiguous Requirements

**Trigger:** Context insufficient or multiple valid interpretations

**Halt Message:**
```markdown
⚠️ EXECUTION HALTED

**Reason:** Ambiguous Requirements
**Subtask:** Task 3, Subtask 3.2 - Implement rate limiting
**Current Task:** Task 3: Create API endpoint

**Ambiguity:**
Task spec says "Add rate limiting to signup endpoint" but doesn't specify:
1. Rate limit window? (per minute, hour, day?)
2. Rate limit count? (5, 10, 100 requests?)
3. Rate limit scope? (per IP, per email, global?)
4. Rate limit action? (return 429, delay, block?)

**Context Review:**
- Task spec mentions rate limiting but no details
- Always-load files don't specify default rate limits
- No previous task has rate limiting pattern

**Cannot Proceed Because:**
- Multiple valid implementations
- Choice significantly impacts user experience
- Wrong choice could cause production issues

**Need from User:**
- Specify rate limit parameters
- Or: Point to rate limiting standards document
- Or: Defer rate limiting to future task

**Current Progress:**
- ✓ Task 1-2 complete (9 subtasks)
- ⏸ Task 3 halted at subtask 3.2 (2 of 5 subtasks)
- ⏹ Task 4-5 not started

**Ready to Resume:** Once rate limit parameters specified
```

---

### 3. Missing Dependencies

**Trigger:** Required library, service, or configuration not available

**Halt Message:**
```markdown
⚠️ EXECUTION HALTED

**Reason:** Missing Dependencies
**Subtask:** Task 4, Subtask 4.2 - Send confirmation email
**Current Task:** Task 4: Add email verification

**Missing Dependency:**
Email service not configured:
- No SMTP credentials in environment (.env file)
- Email service module exists but not initialized
- Task spec doesn't document email service setup

**Attempted:**
1. Checked .env file: No SMTP_* variables
2. Checked environment: No email service running
3. Checked task spec context: No email setup instructions

**Cannot Proceed Because:**
- Cannot send real emails without SMTP config
- Cannot test email functionality
- Subtask requires working email service

**Need from User:**
- Provide SMTP credentials (host, port, user, pass)
- Or: Use email service mock for now (defer real integration)
- Or: Point to email service setup documentation

**Current Progress:**
- ✓ Task 1-3 complete (14 subtasks)
- ⏸ Task 4 halted at subtask 4.2 (1 of 3 subtasks)
- ⏹ Task 5 not started

**Ready to Resume:** Once email service configured or mock approach approved
```

---

### 4. Regression Failures

**Trigger:** Existing tests start failing

**Halt Message:**
```markdown
⚠️ EXECUTION HALTED

**Reason:** Regression Failures
**Subtask:** Task 2, Subtask 2.2 - Create signup service method
**Current Task:** Task 2: Implement signup service

**Regression Failures:**
2 existing tests started failing:
1. File: src/middleware/__tests__/auth.middleware.test.ts
   Test: "should validate user token"
   Error: TypeError: Cannot read property 'email' of undefined

2. File: src/services/__tests__/auth.service.test.ts
   Test: "should authenticate user"
   Error: Expected object with email property, got different structure

**Root Cause Analysis:**
Changed User interface structure:
- Before: { userId: string, userEmail: string }
- After: { id: string, email: string }

**Breaking Change:**
Auth middleware expects old User interface structure

**Cannot Proceed Because:**
- Breaking existing functionality
- Must maintain backward compatibility
- Need strategy for migration

**Need from User:**
- Should we update auth middleware to new interface? (recommended)
- Should we revert User interface changes?
- Should we support both interfaces temporarily?

**Current Progress:**
- ✓ Task 1 complete (5 subtasks)
- ⏸ Task 2 halted at subtask 2.2 (2 of 4 subtasks)
- ⏹ Task 3-5 not started

**Ready to Resume:** Once migration strategy decided
```

---

### 5. User Interruption

**Trigger:** User requests halt or asks question

**Halt Message:**
```markdown
⚠️ EXECUTION HALTED

**Reason:** User Interruption
**User Question:** [User's question/request]

**Current Progress:**
- ✓ Task 1-2 complete (9 subtasks)
- ⏸ Task 3 in progress at subtask 3.3 (3 of 5 subtasks)
- ⏹ Task 4-5 not started

**Ready to Resume:** After addressing user question
```

---

## Halt Configuration

### Default Settings

```yaml
workflow:
  haltOn:
    consecutiveFailures: 3        # Halt after N failures
    ambiguousRequirements: true   # Halt on ambiguity
    missingDependencies: true     # Halt on missing deps
    regressionFailures: true      # Halt on regression
    userInterruption: true        # Halt on user input
```

### Customization

**In .claude/config.yaml:**
```yaml
workflow:
  haltOn:
    consecutiveFailures: 5        # More tolerant
    ambiguousRequirements: false  # Best-effort interpretation
    missingDependencies: true     # Always halt
    regressionFailures: true      # Always halt
```

---

## Resuming After Halt

### General Resume Pattern

1. **User provides guidance/resolution**
2. **Confirm understanding**
3. **Resume from halted subtask**
4. **Continue sequential execution**

**Example:**
```markdown
✅ Resuming Execution

**Halt Reason:** Ambiguous Requirements (rate limiting)
**Resolution:** User specified rate limits (5 requests per minute per IP)

**Resuming At:**
- Task 3, Subtask 3.2: Implement rate limiting

**Applying Resolution:**
- Rate limit: 5 requests/minute
- Scope: Per IP address
- Action: Return 429 Too Many Requests
- Implementation: Using express-rate-limit middleware

**Continuing execution...**
```

---

## Quick Reference

**Authorized Edits:**
- ✅ Implementation Record section
- ✅ Checkboxes ([ ] → [x])
- ✅ Status (Approved → InProgress → Review)

**Prohibited Edits:**
- ❌ Objective, AC, Context, Task descriptions, Quality Review

**Halt Triggers:**
- 3 consecutive failures
- Ambiguous requirements
- Missing dependencies
- Regression failures
- User interruption

**Halt Response:**
- Stop execution immediately
- Present clear halt message
- Show current progress
- Specify what's needed to resume

---

*Part of execute-task skill - Implementation Suite*
