# Refactoring Log Template

## Purpose

Document all refactoring sessions with full traceability and rationale.

---

## Log File Location

**Path:** `.claude/quality/refactoring-log.md`

**Behavior:**
- Append new sessions (don't overwrite)
- Preserve history for audit trail
- One session per task or date

---

## Session Template

```markdown
## Refactoring Session: {task-id} - {date}

**Task:** {task-title}
**Date:** {YYYY-MM-DD HH:MM:SS}
**Scope:** {conservative|moderate|aggressive}
**Duration:** {minutes} minutes
**Success Rate:** {applied}/{attempted} refactorings ({percentage}%)

### Configuration

- **Aggressiveness:** {conservative|moderate|aggressive}
- **Allow Refactoring:** {true|false}
- **Test Command:** {npm test|pytest|etc}
- **Quality Gate:** {task-id}-gate.yaml

### Pre-Refactoring State

**Tests:**
- Total: {count}
- Passing: {count}
- Failing: {count}
- Execution time: {seconds}s

**Code Quality Metrics:**
- Lines of code: {count}
- Cyclomatic complexity: {avg}
- Code duplication: {percentage}%
- Test coverage: {percentage}%

### Refactorings Applied

{List of successful refactorings}

### Refactorings Failed

{List of failed refactorings with reasons}

### Refactorings Skipped

{List of skipped refactorings with reasons}

### Post-Refactoring State

**Tests:**
- Total: {count}
- Passing: {count}
- Failing: {count}
- Execution time: {seconds}s

**Code Quality Metrics:**
- Lines of code: {count} ({change}%)
- Cyclomatic complexity: {avg} ({change}%)
- Code duplication: {percentage}% ({change}%)
- Test coverage: {percentage}% ({change}%)

### Files Modified

{List of files with line count changes}

### Quality Impact

{Qualitative assessment of improvements}

### Recommendations

{Suggestions for future refactoring or manual work}

---
```

---

## Detailed Section Examples

### Session Header

**Example:**
```markdown
## Refactoring Session: task-auth-001 - 2025-10-29

**Task:** Implement User Authentication & Authorization
**Date:** 2025-10-29 10:00:00
**Scope:** Moderate (P0 + P1 refactorings)
**Duration:** 15 minutes
**Success Rate:** 4/5 refactorings (80%)
```

---

### Configuration Section

**Example:**
```markdown
### Configuration

- **Aggressiveness:** moderate
- **Allow Refactoring:** true (from .claude/config.yaml)
- **Test Command:** npm test
- **Quality Gate:** task-auth-001-gate.yaml
- **Risk Filter:** P0 + P1 priorities, Low + Medium risk
- **Coverage Threshold:** 70% minimum for Medium risk
```

---

### Pre-Refactoring State

**Example:**
```markdown
### Pre-Refactoring State

**Tests:**
- Total: 45
- Passing: 45
- Failing: 0
- Execution time: 4.2s
- Pass rate: 100%

**Code Quality Metrics:**
- Lines of code: 520
- Cyclomatic complexity: 8.5 (average)
- Code duplication: 15% (78 lines duplicated)
- Test coverage: 85% (442/520 lines)
- Files with issues: 3

**Quality Findings:**
- Critical: 1 (validation in route handler)
- High: 2 (password hashing inline, god object pattern)
- Medium: 4 (unclear naming, minor duplication)
```

---

### Refactorings Applied

**Template for each:**
```markdown
#### {number}. {Refactoring Name}

- **File:** {file-path}:{line-range}
- **Type:** {Extract Method|Rename|etc}
- **Priority:** {P0|P1|P2}
- **Risk:** {Low|Medium|High}
- **Rationale:** {Why this refactoring was needed}
- **Before:** {Brief description of old code}
- **After:** {Brief description of new code}
- **Impact:** {How this improves quality}
- **Tests:** {Test results after applying}
- **Duration:** {seconds}s
```

**Example:**
```markdown
#### 1. Extract Validation Logic

- **File:** src/routes/auth/signup.ts:15-45
- **Type:** Extract Method
- **Priority:** P0 (Critical)
- **Risk:** Low (adjusted from Medium due to good test coverage)
- **Rationale:** Addresses high severity issue "Validation in route handler". Validation logic should be separate from route handling for testability and reusability.
- **Before:** 30 lines of inline validation in route handler with multiple if/return statements
- **After:** 3 lines calling validateSignupRequest() from dedicated validation utility
- **Impact:**
  - Improved separation of concerns (route vs validation)
  - Enhanced testability (validation testable independently)
  - Reduced route handler complexity (30 lines → 8 lines, -73%)
  - Reusable validation logic for other routes
- **Tests:** ✓ All passing (45/45), execution time 4.1s (-0.1s)
- **Files created:** src/utils/validation.ts (35 lines)
- **Duration:** 2.5 minutes

**Code change:**
```typescript
// Before
async function signup(req, res) {
  if (!req.body.email) return res.status(400).json({...});
  if (!isValidEmail(req.body.email)) return res.status(400).json({...});
  // ... 25 more lines of validation
  const user = await createUser(req.body);
}

// After
async function signup(req, res) {
  const validation = validateSignupRequest(req.body);
  if (!validation.valid) return res.status(400).json(validation.errors);
  const user = await createUser(req.body);
}
```
```

---

### Refactorings Failed

**Template:**
```markdown
#### {number}. {Refactoring Name} ✗

- **File:** {file-path}:{line-range}
- **Type:** {pattern}
- **Priority:** {P0|P1|P2}
- **Risk:** {Low|Medium|High}
- **Rationale:** {Why attempted}
- **Failure Reason:** {Why it failed}
- **Test Failures:** {Which tests failed and why}
- **Rollback:** {How rollback was performed}
- **Resolution:** {What needs to happen}
- **Duration:** {seconds}s (includes rollback)
```

**Example:**
```markdown
#### 5. Extract Email Service ✗

- **File:** src/services/auth/signup.service.ts:67-85
- **Type:** Extract Class
- **Priority:** P1 (High)
- **Risk:** Medium
- **Rationale:** Email sending logic should be in dedicated service for reusability and testability. Currently mixed with signup business logic.
- **Failure Reason:** Missing environment variable SENDGRID_API_KEY in test environment
- **Test Failures:**
  - auth/signup.test.ts › sends verification email
    - Error: Cannot initialize SendGrid client without API key
  - auth/signup.test.ts › handles email sending failure
    - Error: Cannot initialize SendGrid client without API key
- **Rollback:** ✓ Successful
  - Restored src/services/auth/signup.service.ts from backup
  - Removed src/services/email.service.ts (new file)
  - Tests passing again: 45/45 (100%)
- **Resolution:** Manual intervention required
  - Add SENDGRID_API_KEY to test environment
  - Or mock SendGrid client in tests
  - Retry refactoring after configuration fixed
- **Duration:** 3 minutes (including rollback)

**Impact:** No changes applied, code reverted to pre-refactoring state
```

---

### Refactorings Skipped

**Template:**
```markdown
#### {number}. {Refactoring Name} (Skipped)

- **File:** {file-path}
- **Type:** {pattern}
- **Priority:** {P0|P1|P2}
- **Risk:** {Low|Medium|High}
- **Reason:** {Why skipped}
- **Recommendation:** {When/how to address}
```

**Example:**
```markdown
#### 6. Extract RBAC Class (Skipped)

- **File:** src/services/auth/authorization.service.ts:120-250
- **Type:** Extract Class
- **Priority:** P2 (Medium)
- **Risk:** High
- **Reason:** Filtered out by Moderate aggressiveness setting (P2 not included)
- **Recommendation:**
  - Consider in future aggressive refactoring session
  - Or address manually when working on authorization features
  - High risk due to complex dependencies and limited test coverage (65%)

**Potential Impact (if applied):**
- Improved single responsibility (authorization logic separate from auth service)
- Better testability (RBAC logic isolated)
- Requires: Comprehensive tests before attempting (target >85% coverage)
```

---

### Post-Refactoring State

**Example:**
```markdown
### Post-Refactoring State

**Tests:**
- Total: 45
- Passing: 45
- Failing: 0
- Execution time: 4.0s (-0.2s, 5% improvement)
- Pass rate: 100%

**Code Quality Metrics:**
- Lines of code: 485 (-35, 7% reduction)
- Cyclomatic complexity: 6.2 (-2.3, 27% improvement)
- Code duplication: 3% (-12%, 80% reduction)
- Test coverage: 87% (+2%, improvement)
- Files with issues: 1 (-2 files)

**Improvements:**
- ✅ Complexity reduced significantly
- ✅ Duplication nearly eliminated
- ✅ Coverage increased
- ✅ Test execution slightly faster
- ✅ Code more maintainable
```

---

### Files Modified

**Example:**
```markdown
### Files Modified

**Modified:**
1. src/routes/auth/signup.ts
   - Before: 45 lines
   - After: 12 lines
   - Change: -33 lines (-73%)
   - Reason: Extracted validation logic

2. src/services/auth/signup.service.ts
   - Before: 87 lines
   - After: 65 lines
   - Change: -22 lines (-25%)
   - Reason: Extracted password hashing, removed duplication

**Created:**
3. src/utils/validation.ts
   - Lines: 35
   - Purpose: Centralized validation logic for auth routes
   - Exports: validateSignupRequest, validateLoginRequest

4. src/utils/password.ts
   - Lines: 20
   - Purpose: Password hashing and comparison utilities
   - Exports: hashPassword, comparePasswords

**Deleted:**
None

**Total Change:**
- Modified: 2 files
- Created: 2 files
- Deleted: 0 files
- Net lines: -35 lines (520 → 485, 7% reduction)
```

---

### Quality Impact

**Example:**
```markdown
### Quality Impact

**Code Organization:**
- ✅ Better separation of concerns (validation separate from routes)
- ✅ Improved modularity (password utilities reusable)
- ✅ Clearer responsibilities (each file has single purpose)

**Maintainability:**
- ✅ Reduced complexity (8.5 → 6.2 cyclomatic complexity)
- ✅ Eliminated duplication (15% → 3%)
- ✅ Improved readability (descriptive function names)
- ✅ Enhanced testability (utilities independently testable)

**Technical Debt:**
- ✅ Resolved: High severity "Validation in route handler"
- ✅ Resolved: High priority "Password hashing inline"
- ✅ Resolved: Medium priority "Unclear variable naming"
- ⚠️ Partially resolved: God object pattern (needs further work)

**Test Quality:**
- ✅ Coverage increased 2% (85% → 87%)
- ✅ Test execution faster (4.2s → 4.0s)
- ✅ No behavioral changes (all tests still passing)

**Security:**
- ✅ Validation logic centralized (easier to audit)
- ✅ Password hashing consistent (single utility function)
- ✅ Reduced attack surface (clearer code boundaries)

**Overall Assessment:**
Significant improvements in code quality, maintainability, and technical debt reduction. The refactorings successfully addressed 3 of 4 targeted issues without introducing any regressions. Remaining issue (god object) can be addressed in future session with higher coverage.
```

---

### Recommendations

**Example:**
```markdown
### Recommendations

**Immediate Actions:**
1. ✓ Review refactored code (git diff)
2. ✓ Verify coding style alignment
3. ✓ Commit changes separately from features
   - Suggested message: "refactor(auth): improve code quality and reduce technical debt"

**Future Refactoring Opportunities:**
1. **Extract RBAC Class** (P2, High Risk)
   - Increase test coverage to >85% first
   - Consider in next aggressive refactoring session
   - Estimated effort: 30 minutes

2. **Simplify Error Handling** (P2, Medium Risk)
   - Standardize error responses across routes
   - Extract to error handling middleware
   - Estimated effort: 20 minutes

**Manual Review Needed:**
1. **Email Service Configuration**
   - Add SENDGRID_API_KEY to test environment
   - Mock email service in tests
   - Then retry "Extract Email Service" refactoring

**Monitoring:**
- Track code quality metrics over time
- Verify maintainability continues to improve
- Watch for new technical debt patterns

**Team Actions:**
- Share refactoring log with team
- Discuss any concerns or improvements
- Update coding standards if needed
```

---

## Compact Session Template

For quick sessions with 1-2 refactorings:

```markdown
## Quick Refactor: {task-id} - {date}

**Task:** {task-title}
**Duration:** {minutes} min
**Refactorings:** {count} applied

{Brief list of refactorings}

**Impact:** {One-sentence summary}
**Tests:** ✓ All passing ({count}/{count})
**Files:** {list}

---
```

---

## Log Maintenance

**When to archive:**
- Log file exceeds 10,000 lines
- Sessions older than 6 months
- Project completed

**Archive format:**
```bash
# Move old entries to archive
mv .claude/quality/refactoring-log.md \
   .claude/quality/archive/refactoring-log-2025-Q1.md
```

**Retention:**
- Keep current quarter in main log
- Archive older quarters
- Preserve for at least 1 year (audit trail)

---

## Integration with Quality Gate

**Update quality gate file after refactoring:**

```yaml
# .claude/quality/gates/task-auth-001-gate.yaml

refactoring:
  applied: true
  date: 2025-10-29
  session_id: task-auth-001-2025-10-29
  refactorings_applied: 4
  refactorings_failed: 1
  success_rate: 0.80
  quality_improvement: significant
  log_file: .claude/quality/refactoring-log.md

code_quality:
  complexity: 6.2  # improved from 8.5
  duplication: 3%  # improved from 15%
  coverage: 87%    # improved from 85%
  maintainability: improved
```

---

## Quick Reference

**Log structure:**
- Session header (task, date, scope, duration, success rate)
- Configuration (aggressiveness, commands)
- Pre-state (tests, metrics)
- Refactorings applied (detailed entries)
- Refactorings failed (with rollback info)
- Refactorings skipped (with reasons)
- Post-state (tests, metrics, improvements)
- Files modified (line counts)
- Quality impact (qualitative assessment)
- Recommendations (next steps)

**Per-refactoring details:**
- File and line range
- Type and priority
- Risk assessment
- Rationale (why)
- Before/after (what changed)
- Impact (how it helps)
- Test results
- Duration

**For failures:**
- Include: Reason, test failures, rollback process, resolution steps
- Never hide failures (transparency for learning)

---

*Part of refactor-code skill - Quality Suite*
