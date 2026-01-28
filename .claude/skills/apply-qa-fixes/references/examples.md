# Usage Examples

Real-world examples of apply-qa-fixes skill in action.

---

## Example 1: High Severity Security Issues

### Scenario

Quinn reviews task-auth-001 and finds FAIL status with 3 high-severity security issues.

### Quality Gate Summary

```yaml
decision: FAIL
overall_score: 45
top_issues:
  - id: SEC-001
    severity: high
    description: "SQL injection in user login"
  - id: SEC-002
    severity: high
    description: "Missing input validation"
  - id: SEC-003
    severity: high
    description: "Hardcoded secret in config"
```

### User Invocation

```bash
@james *apply-qa-fixes task-auth-001
```

### James Execution

```
✅ Quality gate loaded: FAIL (45/100)
✅ Parsed findings: 3 high severity issues

=== Fix Plan ===
Priority 1 (High Severity): 3 issues
1. SEC-001: SQL injection (src/auth/login.ts:45)
2. SEC-002: Missing validation (src/api/user.ts:23)
3. SEC-003: Hardcoded secret (config/auth.ts:12)

Estimated: 3 files, ~150 lines, 0 tests
Guardrails: ✅ PASS

Proceed? (y/n)
```

### User Response

```
y
```

### Fix Application

```
⏳ Applying fixes...

✅ Fix 1/3: SEC-001 - Added parameterized queries
   File: src/auth/login.ts
   Changed: Line 45
   Before: db.query(`SELECT * FROM users WHERE email = '${email}'`)
   After: db.query('SELECT * FROM users WHERE email = ?', [email])

✅ Fix 2/3: SEC-002 - Added Joi validation
   File: src/api/user.ts
   Added: validation middleware
   Schema: email, password, username validation

✅ Fix 3/3: SEC-003 - Moved secret to environment
   File: config/auth.ts
   Removed: hardcoded JWT secret
   Added: process.env.JWT_SECRET

⏳ Validating...
✅ Lint: 0 problems
✅ Tests: 45/45 passed
✅ Coverage: 82% (no change)

✅ Task file updated
```

### Completion Summary

```
=== QA Fixes Complete ===

✅ 3 fixes applied
✅ 0 tests added
✅ Coverage: 82% (unchanged)
✅ Validation: Clean

Files modified:
- src/auth/login.ts
- src/api/user.ts
- config/auth.ts
- .env.example (new)

Next: @quinn *review task-auth-001
```

---

## Example 2: NFR Failures + Coverage Gaps

### Scenario

Quinn reviews task-payment-005 and finds CONCERNS with NFR failures and missing tests.

### Quality Gate Summary

```yaml
decision: CONCERNS
overall_score: 68
nfr_validation:
  security:
    status: FAIL
    concerns: ["No rate limiting", "Missing HTTPS check"]
  performance:
    status: CONCERNS
    concerns: ["No caching"]
test_design:
  coverage_gaps:
    - ac_id: AC2
      missing_tests: ["Should handle payment timeout", "Should retry failed payment"]
```

### User Invocation

```bash
@james *apply-qa-fixes task-payment-005 --scope all
```

### Fix Plan

```
=== Fix Plan ===
Priority 2 (NFR Failures): 2 issues
1. NFR-SEC-001: Add rate limiting
2. NFR-SEC-002: Enforce HTTPS

Priority 3 (Coverage Gaps): 2 tests
3. TEST-AC2-001: Payment timeout test
4. TEST-AC2-002: Payment retry test

Priority 4 (NFR Concerns): 1 issue
5. NFR-PERF-001: Add response caching

Estimated: 5 files, ~300 lines, 2 tests
Guardrails: ✅ PASS
```

### Fix Application

```
✅ Fix 1/5: Added rate limiting middleware
   Files: src/middleware/rate-limit.ts (new)
          src/app.ts (updated)
   Config: 100 requests per 15 minutes

✅ Fix 2/5: Added HTTPS enforcement
   File: src/middleware/https-check.ts (new)
   Redirects: HTTP → HTTPS in production

✅ Fix 3/5: Added payment timeout test
   File: tests/payment/payment.test.ts
   Scenario: Should handle 30s timeout gracefully

✅ Fix 4/5: Added payment retry test
   File: tests/payment/payment.test.ts
   Scenario: Should retry failed payment up to 3 times

✅ Fix 5/5: Added response caching
   File: src/middleware/cache.ts (new)
   Cache: 5min TTL for GET endpoints

✅ Validation passed
   Tests: 52/52 passed
   Coverage: 79% → 84% (+5%)
```

### Task Update

```markdown
### QA Fixes Applied (2025-01-15)

**Quality Gate:** .claude/quality/gates/task-payment-005-gate-2025-01-15.yaml
**Status Before:** CONCERNS (68/100)
**Status After:** Ready for re-review

**Fixes Applied (5 total):**

**Priority 2 (NFR Failures): 2 issues**
1. NFR-SEC-001: Added rate limiting middleware
2. NFR-SEC-002: Added HTTPS enforcement

**Priority 3 (Coverage Gaps): 2 tests added**
3. AC2: Payment timeout handling test
4. AC2: Payment retry logic test

**Priority 4 (NFR Concerns): 1 issue**
5. NFR-PERF-001: Added response caching

**Validation Results:**
- ✅ Lint: 0 problems
- ✅ Tests: 52/52 passed
- ✅ Coverage: 79% → 84% (+5%)

**Files Modified:**
- src/app.ts
- src/middleware/rate-limit.ts (new)
- src/middleware/https-check.ts (new)
- src/middleware/cache.ts (new)
- tests/payment/payment.test.ts

**Next Steps:**
- Ready for Quinn re-review: @quinn *review task-payment-005
```

---

## Example 3: Mixed Priorities

### Scenario

Quinn reviews task-user-api-003 and finds CONCERNS with issues across all priority levels.

### Quality Gate Summary

```yaml
decision: CONCERNS
overall_score: 72
top_issues:
  - id: PERF-001
    severity: high
    description: "N+1 query pattern"
nfr_validation:
  reliability:
    status: FAIL
    concerns: ["No error logging"]
  performance:
    status: CONCERNS
test_design:
  coverage_gaps:
    - ac_id: AC3
      missing_tests: ["Should validate email format"]
trace:
  ac_gaps:
    - ac_id: AC5
      coverage: partial
      missing: ["Email verification not implemented"]
```

### Fix Plan

```
=== Fix Plan ===

Total Issues: 8

Priority 1 (High Severity): 1 issue
- PERF-001: N+1 query in user fetch (src/services/user.ts)

Priority 2 (NFR Failures): 1 issue
- NFR-REL-001: No error logging

Priority 3 (Coverage Gaps): 1 test
- TEST-AC3-001: Email validation test

Priority 4 (NFR Concerns): 1 issue
- NFR-PERF-001: Missing query caching

Priority 5 (Trace Gaps): 1 issue
- TRACE-AC5: Email verification implementation

Priority 6 (Medium Severity): 2 issues
- ERR-001: Missing null checks
- DOC-001: Missing JSDoc

Priority 7 (Low Severity): 1 issue
- STYLE-001: Inconsistent indentation

Estimated: 6 files, ~450 lines, 1 test
Guardrails: ✅ PASS

Proceed? (y/n)
```

### Fix Application Summary

```
✅ Fix 1/8: P1 - Optimized user query with eager loading
✅ Fix 2/8: P2 - Added Winston error logger
✅ Fix 3/8: P3 - Added email validation test
✅ Fix 4/8: P4 - Added Redis caching for user queries
✅ Fix 5/8: P5 - Implemented email verification flow
✅ Fix 6/8: P6 - Added null checks in user service
✅ Fix 7/8: P6 - Added JSDoc for all public methods
✅ Fix 8/8: P7 - Fixed indentation (Prettier)

⏳ Validating...
✅ All tests passing (58/58)
✅ Coverage: 82% → 87% (+5%)
```

---

## Example 4: Guardrail Violation

### Scenario

Quinn reviews large refactoring task with 25 issues identified.

### Quality Gate Summary

```yaml
decision: FAIL
overall_score: 55
top_issues: [15 high/medium severity issues]
nfr_validation: [5 NFR failures]
test_design:
  coverage_gaps: [8 missing tests]
```

### Fix Plan

```
=== Fix Plan ===

Total Issues: 28

Priority 1: 8 issues
Priority 2: 5 issues
Priority 3: 8 issues
Priority 4-7: 7 issues

Estimated Impact:
- Files to modify: 18
- Estimated diff: ~1200 lines
- Tests to add: 8

⚠️ Guardrail Violations:
- max_files: 18 (limit: 10) ❌
- max_diff_lines: 1200 (limit: 800) ❌
```

### Guardrail Response

```
⚠️ Fix plan exceeds guardrails

Recommendation: Split into multiple sessions

Suggested Split:

Session 1 (P1 + P2):
- 13 fixes
- 8 files
- ~600 lines
- Guardrails: ✅ PASS

Session 2 (P3 + P4-7):
- 15 fixes
- 10 files
- ~600 lines
- Guardrails: ✅ PASS

Would you like to:
1. Apply Session 1 now, Session 2 later
2. Override guardrails (requires confirmation)
3. Defer low priority fixes (P5-7)
4. Cancel
```

### User Choice

```
1
```

### Session 1 Execution

```
=== Applying Session 1 (P1 + P2) ===

✅ 13 fixes applied
✅ 3 tests added
✅ Coverage: 75% → 81% (+6%)

Files modified: 8
Next: @james *apply-qa-fixes task-xxx --resume session-2
```

---

## Example 5: Fix Scope Filtering

### Scenario

User wants to fix only high-severity issues first, defer others.

### User Invocation

```bash
@james *apply-qa-fixes task-data-007 --scope high_severity
```

### Fix Plan

```
=== Fix Plan (high_severity scope) ===

Priority 1 (High Severity): 4 issues
1. SEC-001: SQL injection
2. SEC-002: Missing auth
3. DATA-001: Data loss risk
4. PERF-001: Infinite loop

Skipping:
- Priority 2-7 (12 issues)

Estimated: 4 files, ~250 lines
Guardrails: ✅ PASS
```

### Completion

```
✅ 4 high-severity fixes applied
⏭️ 12 issues remaining (run without --scope to address all)

Next:
- Re-review high-severity: @quinn *review task-data-007
- Apply remaining fixes: @james *apply-qa-fixes task-data-007
```

---

## Example 6: Tests Fail After Fixes

### Scenario

Fixes applied but tests fail during validation.

### Fix Application

```
✅ Fix 1/5: Added input validation
✅ Fix 2/5: Added SQL parameterization
✅ Fix 3/5: Added rate limiting
✅ Fix 4/5: Added error logging
✅ Fix 5/5: Added caching

⏳ Validating...
❌ Tests failed: 2/47
```

### Failing Tests

```
Failed Tests:
1. tests/api/user.test.ts: "Should accept valid email"
   Error: Validation schema too strict, rejects valid emails

2. tests/db/query.test.ts: "Should fetch user by ID"
   Error: Parameterized query syntax error
```

### Iteration 1

```
⏳ Debugging failing tests...

Fix 1: Relaxed email validation regex
File: src/middleware/validation.ts
Issue: Regex rejected "user+tag@example.com" format

Fix 2: Corrected parameterized query syntax
File: src/db/queries.ts
Issue: Used wrong placeholder format for PostgreSQL

⏳ Re-running tests...
✅ Tests passed: 47/47
```

### Completion

```
✅ All fixes applied
✅ Validation clean (after 1 iteration)
✅ Coverage: 80% → 85%
```

---

## Example 7: No Fixes Needed

### Scenario

User tries to apply fixes but gate status is PASS.

### User Invocation

```bash
@james *apply-qa-fixes task-simple-001
```

### Response

```
✅ Quality gate loaded: PASS (92/100)

ℹ️ No fixes needed
Quality gate status is PASS, task is ready for merge.

Gate summary:
- Risk management: 90
- Test coverage: 95
- Traceability: 100
- NFR compliance: 88
- Implementation quality: 92
- Compliance: 95

Next: Proceed to merge or deployment
```

---

## Example 8: Integration with James Routing

### Scenario

User calls James *apply-qa-fixes, James routes with guardrails.

### User Invocation

```bash
@james *apply-qa-fixes task-complex-012
```

### James Routing

```
✅ Task loaded: task-complex-012
✅ Quality gate found: CONCERNS (65/100)

Complexity Assessment:
- High severity issues: 5
- NFR failures: 3
- Total fixes: 18

Routing Decision:
- Route to: apply-qa-fixes skill
- Guardrails: Extended (10 files, 800 lines)
- Reason: High issue count requires extended limits

⚠️ Complexity HIGH - User confirmation required
Proceed? (y/n)
```

### After Confirmation

```
✅ Routing to apply-qa-fixes skill...

[Standard apply-qa-fixes execution]

✅ Complete
✅ 18 fixes applied
✅ Validation clean
```

---

## Example 9: Manual Fix Required (Escalation)

### Scenario

Some fixes require architectural changes and can't be automated.

### Fix Plan

```
=== Fix Plan ===

Priority 1: 3 fixes
1. SEC-001: SQL injection ✅ (auto-fixable)
2. SEC-002: Auth redesign ⚠️ (requires architecture change)
3. PERF-001: Database schema ⚠️ (requires migration)

Priority 2-7: 10 fixes ✅
```

### Execution

```
✅ Fix 1/13: SEC-001 applied

⚠️ Fix 2/13: SEC-002 requires architecture change
   Issue: Current auth system fundamentally flawed
   Recommendation: Redesign with OAuth2/JWT
   Action: Escalating to user

⚠️ Fix 3/13: PERF-001 requires database migration
   Issue: Need to add indexes, requires schema change
   Action: Escalating to user

✅ Fixes 4-13: Applied successfully

=== Execution Summary ===
✅ Auto-fixed: 11 issues
⚠️ Manual review needed: 2 issues

Manual Fixes Required:
1. SEC-002: Auth redesign (architectural)
2. PERF-001: Database schema (migration required)

Next:
1. Address manual fixes
2. Re-run: @james *apply-qa-fixes task-xxx
3. Or proceed to re-review: @quinn *review task-xxx
```

---

## Example 10: End-to-End Workflow

### Complete Quality Feedback Loop

```bash
# Step 1: Implement feature
@james *implement task-checkout-009

# James implements, returns success

# Step 2: Quality review
@quinn *review task-checkout-009

# Quinn finds CONCERNS (73/100)
# - 2 high severity issues
# - 1 NFR failure
# - 3 coverage gaps

# Step 3: Apply QA fixes
@james *apply-qa-fixes task-checkout-009

# James:
# ✅ 6 fixes applied
# ✅ 3 tests added
# ✅ Coverage: 78% → 86%

# Step 4: Re-review
@quinn *review task-checkout-009

# Quinn re-assesses:
# ✅ PASS (91/100)
# All issues resolved

# Step 5: Ready for merge
git add .
git commit -m "Implement checkout flow with QA fixes"
git push
```

---

## Quick Reference

### Basic Usage

```bash
# Auto-detect gate and fix all issues
@james *apply-qa-fixes task-001

# Specify gate file
@james *apply-qa-fixes task-001 --gate .claude/quality/gates/task-001-gate-2025-01-15.yaml

# Fix only high-severity
@james *apply-qa-fixes task-001 --scope high_severity

# Fix only NFR failures
@james *apply-qa-fixes task-001 --scope nfr_only

# Fix only coverage gaps
@james *apply-qa-fixes task-001 --scope coverage_only
```

### Common Patterns

**Pattern 1: Full Fix**
```bash
@quinn *review task-001          # Review
@james *apply-qa-fixes task-001  # Fix all
@quinn *review task-001          # Re-review
```

**Pattern 2: Incremental Fix**
```bash
@james *apply-qa-fixes task-001 --scope high_severity  # Fix critical first
@james *apply-qa-fixes task-001 --scope nfr_only       # Fix NFRs
@james *apply-qa-fixes task-001                        # Fix remaining
```

**Pattern 3: Split Sessions**
```bash
@james *apply-qa-fixes task-001  # Session 1 (P1-P2)
# ... after session 1 complete
@james *apply-qa-fixes task-001 --resume  # Session 2 (P3-7)
```

---
