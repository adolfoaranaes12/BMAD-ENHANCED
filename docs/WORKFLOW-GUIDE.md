# BMAD Enhanced - Workflow Guide

**Detailed workflow scenarios with step-by-step instructions**

**Version:** 2.0 | **Last Updated:** 2025-11-05

---

## Table of Contents

**Planning Workflows:**
1. [Create Task Specification from Vague Requirement](#1-create-task-specification-from-vague-requirement)
2. [Break Down Epic into Sprint-Ready Stories](#2-break-down-epic-into-sprint-ready-stories)
3. [Plan Two-Week Sprint with Velocity](#3-plan-two-week-sprint-with-velocity)

**Development Workflows:**
4. [Implement Feature with TDD](#4-implement-feature-with-test-driven-development)
5. [Fix Production Bug with Root Cause Analysis](#5-fix-production-bug-with-root-cause-analysis)
6. [Refactor Legacy Code Safely](#6-refactor-legacy-code-safely)

**Quality Workflows:**
7. [Complete Quality Review Cycle](#7-complete-quality-review-cycle)
8. [NFR Assessment and Validation](#8-nfr-assessment-and-validation)
9. [Risk Assessment for Major Change](#9-risk-assessment-for-major-change)

**Architecture Workflows:**
10. [Analyze Existing Codebase Architecture](#10-analyze-existing-codebase-architecture)
11. [Design Greenfield System Architecture](#11-design-greenfield-system-architecture)
12. [Compare Architecture Options for Modernization](#12-compare-architecture-options-for-modernization)

**End-to-End Workflows:**
13. [Complete Feature Delivery (Automated)](#13-complete-feature-delivery-automated)
14. [Brownfield System Modernization](#14-brownfield-system-modernization)
15. [Sprint Execution with Daily Automation](#15-sprint-execution-with-daily-automation)

---

## Planning Workflows

### 1. Create Task Specification from Vague Requirement

**Goal:** Transform vague requirement into detailed, actionable task specification

**When to Use:**
- Received ambiguous feature request
- Need to clarify requirements before implementation
- Want structured approach to planning

**Duration:** 5-10 minutes

**Complexity:** Simple (score: 15-25)

---

#### Steps:

**Step 1: Initial Specification**

```bash
/alex *create-task-spec "Users want better security"
```

**What Happens:**
- Alex identifies ambiguities
- Creates initial specification with best assumptions
- Flags areas needing clarification

**Output Example:**
```
✓ Task specification created: .claude/tasks/task-sec-001.md

Specification includes:
- Objective: Enhance user authentication security
- Acceptance Criteria (3 preliminary):
  1. Multi-factor authentication implemented
  2. Password strength requirements enforced
  3. Session timeout after 15 minutes of inactivity

⚠️ Clarification Needed:
- Which authentication methods? (SMS, email, authenticator app?)
- Password policy specifics? (length, complexity, history?)
- Session timeout value? (suggested: 15 min, adjust if needed)
```

**Step 2: Refine with Clarification**

```bash
/alex *refine-story task-sec-001 --context "Focus on authenticator app MFA, minimum 12-char passwords with uppercase/lowercase/numbers/symbols, 30-minute session timeout"
```

**What Happens:**
- Alex incorporates specific requirements
- Updates acceptance criteria
- Adds technical approach details

**Updated Output:**
```
✓ Task specification refined: .claude/tasks/task-sec-001.md

Updated specification:
- Objective: Implement authenticator app-based MFA with enhanced password policy
- Acceptance Criteria (5 refined):
  1. TOTP-based MFA using authenticator apps (Google Authenticator, Authy)
  2. Password minimum 12 characters
  3. Password must contain uppercase, lowercase, numbers, symbols
  4. Session timeout after 30 minutes of inactivity
  5. Password history: prevent reuse of last 5 passwords

Technical Approach:
- Use speakeasy library for TOTP generation
- Store MFA secrets encrypted in database
- Implement password validation middleware
- Use Redis for session management with TTL

Test Strategy:
- Unit tests for password validation
- Integration tests for MFA flow
- E2E test for complete authentication

Estimated Effort: 5 story points
```

---

#### Expected Output:

**File:** `.claude/tasks/task-sec-001.md`

**Contents:**
- Clear objective statement
- 5-7 testable acceptance criteria
- Technical approach with specific libraries/frameworks
- Comprehensive test strategy
- Story point estimate (Fibonacci scale)
- Dependencies identified
- Implementation notes

---

#### Next Steps:

```bash
# Option A: Implement immediately
/james *implement task-sec-001

# Option B: Get estimate first
/alex *estimate task-sec-001

# Option C: Review before committing
# (Review specification file manually, then proceed)
```

---

### 2. Break Down Epic into Sprint-Ready Stories

**Goal:** Transform large epic into manageable, estimated user stories

**When to Use:**
- Planning major feature or initiative
- Epic too large for single sprint
- Need to estimate total effort

**Duration:** 20-30 minutes

**Complexity:** Standard (score: 40-55)

---

#### Steps:

**Step 1: Break Down Epic**

```bash
/alex *breakdown-epic "E-commerce Shopping Cart System"
```

**What Happens:**
- Alex analyzes epic scope
- Identifies natural story boundaries
- Creates 5-12 user stories
- Maps dependencies
- Recommends implementation order

**Output:**
```
✓ Epic broken down into 9 user stories

Stories created:
1. Cart item management (add/remove/update) - 3 pts
2. Cart persistence across sessions - 2 pts
3. Quantity selector with inventory validation - 3 pts
4. Cart subtotal and tax calculation - 5 pts
5. Shipping cost estimation - 5 pts
6. Promo code application - 3 pts
7. Cart abandonment email notifications - 5 pts
8. Guest checkout cart handling - 3 pts
9. Cart migration on user login - 3 pts

Total: 32 story points

Dependency Map:
- Stories 1, 2, 3 are independent (can be parallel)
- Story 4 depends on Story 3 (quantity needed for calculations)
- Story 5 depends on Story 4 (needs subtotal)
- Stories 6, 7, 8 can be developed in parallel
- Story 9 depends on Stories 2, 8

Recommended Order (3 sprints at 12-15 velocity):
Sprint 1: Stories 1, 2, 3 (8 pts - foundation)
Sprint 2: Stories 4, 5, 6 (13 pts - calculations)
Sprint 3: Stories 7, 8, 9 (11 pts - advanced features)
```

**Step 2: Estimate Each Story**

```bash
# Estimate story 1
/alex *estimate .claude/stories/story-cart-001.md

# Output:
# ✓ Story estimated: 3 story points
# Complexity factors:
# - Technical complexity: Medium (CRUD operations)
# - Scope: Small (single feature)
# - Dependencies: None
# - Uncertainty: Low (standard patterns)
# - Testing: Standard (unit + integration)

# Repeat for remaining stories (or use batch)
/alex *estimate .claude/stories/story-cart-*.md
```

**Step 3: Validate Dependencies**

```bash
# Review dependency graph
cat .claude/planning/epic-cart-dependencies.md

# Output shows:
# Story 1 [Cart CRUD] ────┐
#                         │
# Story 2 [Persistence] ──┼──> Story 4 [Calculations] ──> Story 5 [Shipping]
#                         │
# Story 3 [Quantity] ─────┘
#
# Story 6 [Promo] ─────> (Independent)
# Story 7 [Emails] ────> (Independent)
# Story 8 [Guest] ─────> Story 9 [Migration]
```

---

#### Expected Output:

**Files Created:**
- `.claude/stories/story-cart-001.md` through `story-cart-009.md` (9 user stories)
- `.claude/planning/epic-cart-breakdown.md` (breakdown summary)
- `.claude/planning/epic-cart-dependencies.md` (dependency graph)

**Each Story Contains:**
- User story format ("As a [user], I want [feature] so that [benefit]")
- Acceptance criteria (3-5 testable conditions)
- Technical notes
- Dependencies
- Estimate (story points)

---

#### Next Steps:

```bash
# Create sprint plan
/alex *plan-sprint --velocity 12 --stories .claude/stories/story-cart-*.md

# Or use orchestrator for complete planning
/orchestrator *workflow epic-to-sprint "E-commerce Shopping Cart" --velocity 12
```

---

### 3. Plan Two-Week Sprint with Velocity

**Goal:** Create detailed sprint plan with story allocation and capacity management

**When to Use:**
- Beginning new sprint
- Have estimated stories in backlog
- Know team velocity

**Duration:** 15-25 minutes

**Complexity:** Standard (score: 30-45)

---

#### Steps:

**Step 1: Sprint Planning**

```bash
/alex *plan-sprint --velocity 40 --sprint-length 2-weeks --team-size 4
```

**What Happens:**
- Alex loads backlog (estimated stories)
- Prioritizes by value and dependencies
- Allocates stories to fit velocity (≤95% capacity)
- Creates daily breakdown
- Identifies risks and buffers

**Output:**
```
✓ Sprint plan created: .claude/sprints/sprint-15-plan.md

Sprint 15 Summary:
- Duration: 2 weeks (10 working days)
- Team: 4 developers
- Velocity: 40 story points
- Committed: 38 points (95% capacity)
- Buffer: 2 points for unknowns

Stories Selected (8 total):
1. User authentication enhancement (5 pts) - HIGH PRIORITY
2. Password reset flow (3 pts)
3. MFA with authenticator apps (8 pts)
4. Session management improvements (5 pts)
5. API rate limiting (5 pts)
6. Email notifications refactor (3 pts)
7. Admin dashboard updates (5 pts)
8. Bug fix: Login timeout issue (2 pts)

Daily Breakdown:
Week 1:
- Mon-Tue: Stories 1, 2 (8 pts)
- Wed-Thu: Story 3 (8 pts)
- Fri: Story 4 start (2 pts)

Week 2:
- Mon: Story 4 complete (3 pts)
- Tue-Wed: Stories 5, 6 (8 pts)
- Thu: Story 7 (5 pts)
- Fri: Story 8, buffer (2-4 pts)

Team Allocation:
- Developer A: Stories 1, 4, 7 (15 pts)
- Developer B: Stories 2, 6, 8 (8 pts)
- Developer C: Story 3 (8 pts)
- Developer D: Story 5 (5 pts)
- Pair programming: Stories 3, 7 (complex)

Dependencies:
- Story 2 depends on Story 1
- Story 4 can start in parallel
- No blocking dependencies for Week 2

Risks Identified:
- Story 3 (MFA) is complex - consider splitting if issues arise
- Story 5 (rate limiting) needs infrastructure changes
- Buffer time allocated for Story 1 unknowns

Sprint Goal:
"Enhance user authentication security with MFA and improve system reliability through rate limiting and session management."
```

**Step 2: Create Task Specifications for Sprint Stories**

```bash
# Generate detailed task specs for all sprint stories
for story in .claude/stories/story-auth-001.md .claude/stories/story-auth-002.md; do
  /alex *create-task-spec --from-story $story
done

# Or batch create
/alex *create-task-spec --from-sprint .claude/sprints/sprint-15-plan.md
```

**Output:**
```
✓ Task specifications created for 8 stories

Tasks created:
- task-auth-001: User authentication enhancement (5 pts)
- task-auth-002: Password reset flow (3 pts)
- task-auth-003: MFA with authenticator apps (8 pts)
- task-auth-004: Session management improvements (5 pts)
- task-infra-001: API rate limiting (5 pts)
- task-email-001: Email notifications refactor (3 pts)
- task-admin-001: Admin dashboard updates (5 pts)
- task-bug-001: Fix login timeout issue (2 pts)

All tasks ready for implementation.
```

---

#### Expected Output:

**File:** `.claude/sprints/sprint-15-plan.md`

**Contents:**
- Sprint summary (duration, velocity, capacity)
- Story list with estimates
- Daily breakdown for 2 weeks
- Team allocation
- Dependency mapping
- Risk identification
- Sprint goal statement
- Definition of Done checklist

---

#### Next Steps:

```bash
# Option A: Execute sprint manually (implement each task)
/james *implement task-auth-001
/james *implement task-auth-002
# ... continue for all tasks

# Option B: Use orchestrator for automated sprint execution
/orchestrator *workflow sprint-execution "Sprint 15" --velocity 40
```

---

## Development Workflows

### 4. Implement Feature with Test-Driven Development

**Goal:** Implement feature following strict TDD principles (RED-GREEN-REFACTOR)

**When to Use:**
- Implementing new feature from task specification
- Want high test coverage (80%+)
- Following TDD best practices

**Duration:** 20-60 minutes (depending on complexity)

**Complexity:** Variable (score: 20-70)

---

#### Steps:

**Step 1: Implement with TDD**

```bash
/james *implement task-auth-003
```

**What Happens:**
James follows TDD workflow:

**Phase 1: RED (Write Failing Tests)**
```
⏳ TDD Phase 1: RED - Writing failing tests

Writing tests for acceptance criteria:
1. MFA setup flow test
2. TOTP code generation test
3. TOTP code validation test
4. MFA login flow test
5. MFA recovery codes test

Creating test files:
- tests/auth/test_mfa_setup.py (45 lines)
- tests/auth/test_mfa_validation.py (60 lines)
- tests/integration/test_mfa_flow.py (80 lines)

Running tests...
✗ 18 tests written, 18 failing (expected)
```

**Phase 2: GREEN (Implement Minimum Code)**
```
⏳ TDD Phase 2: GREEN - Implementing code

Implementing MFA functionality:
- src/auth/mfa_manager.py (120 lines)
- src/auth/totp_generator.py (45 lines)
- src/api/routes/mfa.py (90 lines)

Dependencies added:
- pyotp==2.8.0 (TOTP generation)
- qrcode==7.4.2 (QR code generation)

Running tests...
✓ 18 tests passing
```

**Phase 3: REFACTOR (Improve Code Quality)**
```
⏳ TDD Phase 3: REFACTOR - Improving code quality

Refactoring improvements:
- Extracted TOTP validation to separate function
- Simplified MFA setup controller logic
- Improved error handling consistency
- Added type hints throughout

Running tests after refactor...
✓ 18 tests still passing

Code quality metrics:
- Cyclomatic complexity: 4 (excellent)
- Maintainability index: 85 (good)
- Test coverage: 95%
```

**Final Output:**
```
✓ Implementation complete: task-auth-003

Files created:
- src/auth/mfa_manager.py (120 lines)
- src/auth/totp_generator.py (45 lines)
- src/api/routes/mfa.py (90 lines)
- tests/auth/test_mfa_setup.py (45 lines)
- tests/auth/test_mfa_validation.py (60 lines)
- tests/integration/test_mfa_flow.py (80 lines)

Test Results:
- Total tests: 18
- Passing: 18 (100%)
- Coverage: 95% (target: 80%)
- Duration: 2.3s

All acceptance criteria met:
✓ MFA setup with QR code
✓ TOTP validation
✓ Backup codes generation
✓ MFA-enabled login flow
✓ MFA recovery options

Ready for review.
```

**Step 2: Run Full Test Suite**

```bash
/james *test --all
```

**Output:**
```
✓ Full test suite execution

Test Results:
- Unit tests: 142/142 passing
- Integration tests: 35/35 passing
- E2E tests: 12/12 passing

Total: 189 tests passing (0 failures)

Coverage: 87% overall
- src/auth/: 95%
- src/api/: 82%
- src/utils/: 78%

Coverage gaps identified:
- src/utils/validators.py (lines 45-52): Edge case handling
- src/api/routes/admin.py (lines 120-130): Error path

Performance:
- Duration: 8.2 seconds
- Average test time: 43ms
- Slowest test: test_mfa_full_flow (850ms)

No issues found. Ready for quality review.
```

---

#### Expected Output:

**Implementation Files:**
- Source code (3 files, ~255 lines total)
- Test files (3 files, ~185 lines total)
- Coverage ≥ 80% (typically 90-95% with TDD)
- All acceptance criteria met
- All tests passing

**Telemetry File:** `.claude/telemetry/implement-task-auth-003.json`
```json
{
  "task_id": "task-auth-003",
  "complexity": 45,
  "routing": "standard",
  "tdd_cycle": {
    "red_tests": 18,
    "green_tests": 18,
    "refactor_iterations": 2
  },
  "coverage_percent": 95,
  "duration_ms": 1800000
}
```

---

#### Next Steps:

```bash
# Quality review
/quinn *review task-auth-003

# If issues found
/james *apply-qa-fixes task-auth-003

# Final validation
/quinn *validate-quality-gate task-auth-003
```

---

### 5. Fix Production Bug with Root Cause Analysis

**Goal:** Systematically diagnose and fix production bug with regression prevention

**When to Use:**
- Production issue reported
- Bug reproduction steps available
- Need root cause analysis

**Duration:** 15-45 minutes

**Complexity:** Variable (score: 25-65)

---

#### Steps:

**Step 1: Bug Reproduction and Root Cause Analysis**

```bash
/james *fix bug-login-memory-leak --reproduce-steps "1. Login as admin\n2. Navigate to dashboard\n3. Memory usage grows by 100MB every 5 minutes\n4. After 4 hours, application crashes with OOM"
```

**What Happens:**

**Phase 1: Reproduction**
```
⏳ Reproducing bug...

Steps executed:
1. Login as admin ✓
2. Navigate to dashboard ✓
3. Monitoring memory usage...

Memory profile:
- Initial: 250MB
- After 5 min: 350MB (+100MB)
- After 10 min: 450MB (+100MB)
- After 15 min: 550MB (+100MB)

✓ Bug reproduced successfully
Pattern: Linear memory growth, ~20MB/minute
```

**Phase 2: Root Cause Analysis**
```
⏳ Analyzing root cause...

Investigation steps:
1. Profiling memory allocations
2. Reviewing dashboard event listeners
3. Checking WebSocket connections
4. Analyzing cache management

Findings:
- Event listeners not cleaned up on component unmount
- Location: src/dashboard/components/MetricsWidget.tsx:67
- Each navigation creates new listeners
- Listeners hold references to large data objects
- Garbage collector cannot reclaim memory

Root Cause:
useEffect hook missing cleanup function for setInterval and WebSocket subscriptions

Evidence:
- 240+ active event listeners after 4 hours
- Each listener holds ~420KB of historical data
- Total leak: 240 * 420KB ≈ 100MB/5min

Severity: HIGH (production crashes)
```

**Phase 3: Fix Implementation**
```
⏳ Implementing fix...

Changes made:
File: src/dashboard/components/MetricsWidget.tsx

BEFORE:
useEffect(() => {
  const interval = setInterval(fetchMetrics, 5000);
  const ws = new WebSocket(WS_URL);
  ws.onmessage = handleUpdate;
}, []);

AFTER:
useEffect(() => {
  const interval = setInterval(fetchMetrics, 5000);
  const ws = new WebSocket(WS_URL);
  ws.onmessage = handleUpdate;

  // Cleanup function
  return () => {
    clearInterval(interval);
    ws.close();
  };
}, []);

Fix validates:
✓ Memory stable after 1 hour (no growth)
✓ Event listeners properly cleaned (count stays constant)
✓ WebSocket connections closed on unmount
```

**Phase 4: Regression Tests**
```
⏳ Adding regression tests...

Tests created:
- tests/dashboard/test_metrics_memory_leak.test.tsx
  * Test 1: Verify cleanup on unmount
  * Test 2: Verify no memory growth over 30 minutes
  * Test 3: Verify event listener count stays constant

Running tests...
✓ 3 new tests passing
✓ All existing tests passing (142/142)
```

**Final Output:**
```
✓ Bug fix complete: bug-login-memory-leak

Root Cause:
Missing cleanup in useEffect hook causing event listener and WebSocket memory leak

Fix Applied:
- Added return cleanup function in useEffect
- Clears interval timers
- Closes WebSocket connections

Files Changed:
- src/dashboard/components/MetricsWidget.tsx (3 lines added)
- tests/dashboard/test_metrics_memory_leak.test.tsx (85 lines added)

Verification:
✓ Bug no longer reproduces
✓ Memory stable over 2-hour test
✓ 3 new regression tests passing
✓ All existing tests passing

Impact Analysis:
- Similar pattern found in 2 other components
- Recommended: Apply same fix to StockWidget and AlertsWidget
- Created tasks: task-bug-002, task-bug-003
```

---

#### Expected Output:

**Documentation:** `.claude/bugs/bug-login-memory-leak-analysis.md`
```markdown
# Bug Analysis: bug-login-memory-leak

## Summary
Memory leak in dashboard metrics widget causing OOM crashes after 4 hours

## Root Cause
Missing cleanup function in useEffect hook. Event listeners and WebSocket connections not disposed on component unmount.

## Fix
Added return cleanup function to properly dispose resources

## Regression Prevention
- 3 new tests added
- Similar patterns identified in 2 other components
- Follow-up tasks created

## Related Issues
- task-bug-002: Fix same issue in StockWidget
- task-bug-003: Fix same issue in AlertsWidget
```

---

#### Next Steps:

```bash
# Address related issues
/james *fix task-bug-002
/james *fix task-bug-003

# Quality review
/quinn *review bug-login-memory-leak
```

---

### 6. Refactor Legacy Code Safely

**Goal:** Improve code quality while maintaining behavior (all tests passing)

**When to Use:**
- Code has quality issues (high complexity, duplication)
- Need to reduce technical debt
- Before adding new features to legacy code

**Duration:** 20-60 minutes

**Complexity:** Variable (score: 30-75)

---

#### Steps:

**Step 1: Establish Baseline**

```bash
/james *test --all --record-baseline
```

**Output:**
```
✓ Baseline recorded

Test Results:
- Total: 189 tests
- Passing: 189 (100%)
- Coverage: 87%

Baseline saved: .claude/testing/baseline-20251105.json

Performance baseline:
- Duration: 8.2s
- Average test: 43ms
```

**Step 2: Assess Current State**

```bash
/quinn *review src/payment/processor.py --scope code-quality
```

**Output:**
```
✓ Code quality review complete

Quality Score: 45/100 (FAIL)

Issues Identified (12 total):

HIGH SEVERITY (3):
1. Cyclomatic complexity: 18 (target: ≤10)
   - Function: process_payment() (lines 45-180)
   - Too many conditional branches

2. Function length: 135 lines (target: ≤50)
   - Function: process_payment()
   - Violates single responsibility

3. Duplication: 45% duplicate code
   - Repeated validation logic in 3 places
   - Repeated error handling in 5 places

MEDIUM SEVERITY (5):
4. Missing type hints (12 functions)
5. Inconsistent naming conventions
6. No docstrings (8 functions)
7. Magic numbers used (6 instances)
8. Deep nesting (4 levels in 3 places)

LOW SEVERITY (4):
9-12. Various style issues

Recommendations:
- Extract validation to separate function
- Extract error handling to decorator
- Break process_payment() into smaller functions
- Add type hints and docstrings
```

**Step 3: Safe Refactoring**

```bash
/james *refactor src/payment/processor.py --scope moderate --preserve-behavior=true
```

**What Happens:**

**Phase 1: Extract Functions**
```
⏳ Refactoring: Extract method

Extracting functions:
1. validate_payment_request() (lines 52-68)
2. calculate_fees() (lines 70-88)
3. process_card_payment() (lines 90-115)
4. process_bank_payment() (lines 117-140)
5. send_confirmation() (lines 142-160)

New structure:
- Original: 1 function, 135 lines, complexity 18
- Refactored: 6 functions, avg 22 lines, max complexity 4
```

**Phase 2: Remove Duplication**
```
⏳ Refactoring: Remove duplication

Extracting shared logic:
- validation_decorator.py (centralized validation)
- error_handler.py (centralized error handling)

Duplication reduced:
- Before: 45% duplicate code
- After: 0% duplicate code
- Lines saved: 67 lines removed
```

**Phase 3: Improve Readability**
```
⏳ Refactoring: Improve readability

Improvements:
- Added type hints to all functions
- Added comprehensive docstrings
- Replaced magic numbers with named constants
- Improved variable names
- Reduced nesting levels (4 → 2 max)
```

**Phase 4: Verify Behavior Preservation**
```
⏳ Running tests against baseline...

Test Results:
- Total: 189 tests
- Passing: 189 (100%)
- Changed: 0 (behavior preserved)

✓ All tests passing
✓ No behavior changes detected
✓ Performance maintained (8.1s vs 8.2s baseline)
```

**Final Output:**
```
✓ Refactoring complete: src/payment/processor.py

Changes Summary:
- Functions: 1 → 6 (better separation)
- Lines: 135 → 95 (40 lines removed)
- Complexity: 18 → 4 max (78% reduction)
- Duplication: 45% → 0% (eliminated)

Quality Improvement:
- Before: 45/100 (FAIL)
- After: 90/100 (PASS)
- Improvement: +45 points

Files Modified:
- src/payment/processor.py (refactored)
- src/payment/validation_decorator.py (new)
- src/payment/error_handler.py (new)

Tests:
✓ All 189 tests passing (unchanged)
✓ Behavior preserved
✓ Performance maintained

Code Metrics:
- Maintainability: 55 → 92 (+37)
- Complexity: 18 → 4 (-14)
- Test coverage: 87% (maintained)
```

**Step 4: Final Verification**

```bash
/james *test --all --compare-baseline
```

**Output:**
```
✓ Baseline comparison complete

Results vs Baseline:
- Tests passing: 189/189 (same)
- Coverage: 87% (same)
- Performance: 8.1s vs 8.2s (1.2% faster)

Behavior Changes: 0 detected
✓ All behavior preserved
✓ Refactoring safe
```

---

#### Expected Output:

**Before Refactoring:**
- Complexity: 18
- Lines: 135
- Duplication: 45%
- Score: 45/100

**After Refactoring:**
- Complexity: 4
- Lines: 95
- Duplication: 0%
- Score: 90/100

**Guarantees:**
- All tests passing (behavior preserved)
- Performance maintained or improved
- Code quality significantly improved

---

#### Next Steps:

```bash
# Quality review to confirm
/quinn *review src/payment/processor.py --scope code-quality

# Expected: Quality score 85-95/100
```

---

## Quality Workflows

### 7. Complete Quality Review Cycle

**Goal:** Comprehensive quality review with iterative improvement until gate passes

**When to Use:**
- Feature implementation complete
- Need quality validation before merge
- Want comprehensive assessment

**Duration:** 25-50 minutes

**Complexity:** Standard (score: 40-60)

---

#### Steps:

**Iteration 1: Initial Review**

```bash
/quinn *review task-checkout-001 --scope comprehensive
```

**Output:**
```
✓ Quality review complete: task-checkout-001

Quality Score: 68/100 (CONCERNS)

Assessment by Dimension:

1. Functionality (85/100) - PASS
   ✓ All 6 acceptance criteria met
   ✓ Feature works as specified
   ⚠️ Missing error handling for edge case (empty cart)

2. Code Quality (60/100) - CONCERNS
   ⚠️ Cyclomatic complexity: 12 (target: ≤10)
   ⚠️ Function length: 75 lines (target: ≤50)
   ✓ Naming conventions good
   ⚠️ Missing docstrings (5 functions)

3. Test Coverage (90/100) - PASS
   ✓ Coverage: 92% (exceeds 80%)
   ✓ Unit tests comprehensive
   ✓ Integration tests present
   ⚠️ Missing E2E test for complete checkout flow

4. Security (75/100) - PASS
   ✓ Input validation present
   ✓ SQL injection prevention
   ⚠️ CSRF token not validated
   ⚠️ Rate limiting not implemented

5. Performance (65/100) - CONCERNS
   ⚠️ N+1 query problem in cart loading
   ⚠️ No caching for product prices
   ✓ Response time acceptable (< 200ms)

6. Documentation (50/100) - FAIL
   ✗ README not updated
   ✗ API documentation missing
   ⚠️ Inline comments sparse

Issues Summary:
- Critical: 0
- High Severity: 3 (CSRF, N+1 queries, docs)
- Medium Severity: 5
- Low Severity: 2

Gate Decision: CONCERNS
Recommendation: Address high-severity issues before merge

Detailed report: .claude/quality/review-checkout-001-iter1.md
```

**Iteration 2: Apply QA Fixes**

```bash
/james *apply-qa-fixes task-checkout-001 --scope high_severity
```

**Output:**
```
✓ QA fixes applied: task-checkout-001

Fixes Applied (3 high-severity issues):

1. CSRF Protection
   - Added CSRF token validation to checkout endpoint
   - File: src/api/routes/checkout.py (5 lines added)
   - Test: tests/api/test_checkout_csrf.py (new file)

2. N+1 Query Optimization
   - Replaced loop queries with single JOIN query
   - File: src/services/cart_service.py (lines 45-60 refactored)
   - Performance: 850ms → 95ms (89% improvement)
   - Test: tests/services/test_cart_performance.py (new file)

3. Documentation
   - Updated README with checkout feature
   - Added API documentation (OpenAPI spec)
   - Added inline docstrings to 5 functions
   - Files: README.md, docs/api/checkout.yaml

Test Results:
- New tests: 8 added
- All tests: 197/197 passing
- Coverage: 93% (+1%)

Re-run review to validate fixes.
```

**Iteration 3: Verify Fixes**

```bash
/quinn *review task-checkout-001 --scope comprehensive
```

**Output:**
```
✓ Quality review complete: task-checkout-001

Quality Score: 85/100 (PASS)

Assessment by Dimension:

1. Functionality (90/100) - PASS
   ✓ All acceptance criteria met
   ✓ Edge case handling added

2. Code Quality (80/100) - PASS
   ✓ Complexity reduced: 12 → 8
   ✓ Docstrings added
   ⚠️ One function still long (60 lines)

3. Test Coverage (95/100) - PASS
   ✓ Coverage: 93%
   ✓ All test types present

4. Security (90/100) - PASS
   ✓ CSRF protection added
   ✓ Input validation comprehensive
   ⚠️ Rate limiting recommended (not blocking)

5. Performance (90/100) - PASS
   ✓ N+1 query fixed
   ✓ Response time excellent (95ms avg)
   ✓ Caching implemented

6. Documentation (85/100) - PASS
   ✓ README updated
   ✓ API docs complete
   ✓ Inline comments good

Issues Remaining:
- Critical: 0
- High Severity: 0
- Medium Severity: 2 (non-blocking)
- Low Severity: 1

Gate Decision: PASS
Recommendation: Approved for merge
Minor improvements can be addressed in follow-up

Improvement vs Iteration 1:
- Score: 68 → 85 (+17 points)
- Issues resolved: 8/10 (80%)
- Time invested: 22 minutes

Detailed report: .claude/quality/review-checkout-001-iter2.md
```

**Iteration 4: NFR Assessment**

```bash
/quinn *assess-nfr task-checkout-001 --categories "security,performance,reliability"
```

**Output:**
```
✓ NFR assessment complete: task-checkout-001

NFR Results:

Security (90/100) - PASS
✓ Authentication required
✓ Authorization checked
✓ CSRF protection implemented
✓ SQL injection prevented
✓ XSS protection present
⚠️ Rate limiting recommended (non-critical)

Performance (92/100) - PASS
✓ Response time: 95ms avg (target: <200ms)
✓ Database queries optimized (1 query vs 15)
✓ Caching implemented (Redis, 5min TTL)
✓ No memory leaks detected
✓ Concurrent user handling: 500+ users

Reliability (88/100) - PASS
✓ Error handling comprehensive
✓ Graceful degradation (fallback to cache)
✓ Transaction rollback on failure
✓ Idempotent operations
⚠️ Logging could be more detailed

Overall NFR Score: 90/100 (PASS)

All critical NFRs met.
Minor recommendations for future improvement.
```

**Final: Quality Gate Validation**

```bash
/quinn *validate-quality-gate task-checkout-001 --threshold 80
```

**Output:**
```
✓ Quality Gate: PASS

Scorecard:
- Overall Quality: 85/100 (exceeds 80 threshold)
- Functionality: 90/100 ✓
- Code Quality: 80/100 ✓
- Test Coverage: 95/100 ✓
- Security: 90/100 ✓
- Performance: 92/100 ✓
- Documentation: 85/100 ✓
- NFR Assessment: 90/100 ✓

Gate Criteria:
✓ All acceptance criteria met
✓ Quality score ≥ 80
✓ Test coverage ≥ 80% (actual: 93%)
✓ No critical security vulnerabilities
✓ No blocking NFR failures
✓ Documentation complete

Blockers: 0
Concerns: 2 (non-blocking, future improvements)

Decision: APPROVED FOR MERGE

Next Steps:
1. Merge to main branch
2. Deploy to staging
3. Monitor performance metrics
4. Address non-blocking concerns in next sprint
```

---

#### Expected Output:

**Review Iterations:**
- Iteration 1: Score 68, CONCERNS decision, 10 issues
- Iteration 2: Fixes applied, 8 issues resolved
- Iteration 3: Score 85, PASS decision, 2 minor issues remain
- Iteration 4: NFR assessment confirms quality

**Final State:**
- Quality score: 85/100 (PASS)
- Test coverage: 93%
- All critical issues resolved
- Gate decision: APPROVED

**Documents Generated:**
- `.claude/quality/review-checkout-001-iter1.md` (initial review)
- `.claude/quality/review-checkout-001-iter2.md` (post-fixes review)
- `.claude/quality/nfr-assessment-checkout-001.md` (NFR assessment)
- `.claude/quality/gate-decision-checkout-001.md` (final gate decision)

---

#### Next Steps:

```bash
# Create pull request
git add .
git commit -m "feat: Implement checkout feature (task-checkout-001)"
git push origin feature/checkout
gh pr create --title "Checkout feature" --body "Quality gate: PASS (85/100)"
```

---

### 8. NFR Assessment and Validation

**Goal:** Comprehensive non-functional requirements assessment

**When to Use:**
- Need to validate NFRs before production
- Assessing system readiness
- Compliance requirements

**Duration:** 15-30 minutes

**Complexity:** Standard (score: 35-50)

---

#### Steps:

**Step 1: Comprehensive NFR Assessment**

```bash
/quinn *assess-nfr task-api-001 --categories "security,performance,reliability,scalability,maintainability,usability"
```

**Output:**
```
✓ NFR assessment complete: task-api-001

Category Assessments:

1. SECURITY (85/100) - PASS
   ✓ Authentication: JWT tokens with refresh
   ✓ Authorization: Role-based access control
   ✓ Encryption: TLS 1.3, AES-256 for sensitive data
   ✓ Input Validation: Comprehensive, sanitization applied
   ✓ SQL Injection: Parameterized queries, ORM used
   ✓ XSS Prevention: Output encoding implemented
   ⚠️ Rate Limiting: Basic (100 req/min), consider tiered limits
   ⚠️ Security Headers: Missing HSTS, X-Frame-Options

   Recommendations:
   - Add HSTS header (max-age=31536000)
   - Implement tiered rate limiting (by user role)
   - Add security.txt for vulnerability reporting

2. PERFORMANCE (92/100) - PASS
   ✓ Response Time: P50: 45ms, P95: 120ms, P99: 180ms (target: <200ms)
   ✓ Throughput: 1,500 req/sec sustained
   ✓ Database Queries: Optimized, indexed, avg 8ms
   ✓ Caching: Redis, 95% hit rate
   ✓ Memory Usage: 450MB avg, no leaks
   ✓ CPU Usage: 35% avg at peak load

   Load Test Results:
   - Concurrent users: 1,000 (max tested)
   - Success rate: 99.8%
   - Error rate: 0.2% (mostly timeouts)

3. RELIABILITY (88/100) - PASS
   ✓ Error Handling: Try-catch blocks, graceful failures
   ✓ Logging: Structured, centralized (ELK stack)
   ✓ Monitoring: Prometheus metrics, Grafana dashboards
   ✓ Health Checks: /health endpoint, 5s interval
   ✓ Circuit Breaker: Implemented for external services
   ✓ Retry Logic: Exponential backoff, max 3 retries
   ⚠️ Chaos Testing: Not performed

   Uptime Target: 99.9% (8.76 hours/year downtime)
   Current Uptime: 99.7% (based on 30-day monitoring)

4. SCALABILITY (80/100) - PASS
   ✓ Horizontal Scaling: Stateless, supports load balancer
   ✓ Database: Read replicas configured (1 master, 2 replicas)
   ✓ Caching: Distributed (Redis Cluster)
   ✓ Queue: Async jobs (Celery + RabbitMQ)
   ⚠️ Auto-Scaling: Manual scaling only
   ⚠️ Load Testing: Max 1,000 concurrent, need 5,000+ test

   Current Capacity: ~1,500 req/sec
   Estimated Max: ~3,000 req/sec (with 3 instances)

5. MAINTAINABILITY (90/100) - PASS
   ✓ Code Quality: Complexity avg 4, maintainability 85
   ✓ Documentation: API docs, README, architecture diagrams
   ✓ Test Coverage: 93% (unit + integration + E2E)
   ✓ Code Style: Linting enforced (Black, Flake8)
   ✓ Dependency Management: requirements.txt, version pinned
   ✓ CI/CD: GitHub Actions, automated tests

6. USABILITY (82/100) - PASS
   ✓ API Design: RESTful, consistent naming
   ✓ Error Messages: Clear, actionable
   ✓ Response Format: JSON, standardized structure
   ✓ Versioning: API v1, v2 (backwards compatible)
   ⚠️ Documentation: Missing examples for 3 endpoints
   ⚠️ Rate Limit Headers: Not exposed to clients

Overall NFR Score: 86/100 (PASS)

Critical NFRs: 6/6 met
Recommended NFRs: 8/10 met
Optional NFRs: 5/8 met

Gate Decision: PASS (ready for production)

Recommendations for Future:
- Add security headers (HSTS, X-Frame-Options)
- Implement auto-scaling
- Perform chaos engineering tests
- Complete API documentation
- Load test at 5,000+ concurrent users
```

**Step 2: Specific Deep Dives (if needed)**

**Security Deep Dive:**
```bash
/quinn *assess-nfr task-api-001 --categories security --depth comprehensive
```

**Performance Deep Dive:**
```bash
/quinn *assess-nfr task-api-001 --categories performance --depth comprehensive
```

---

#### Expected Output:

**NFR Report:** `.claude/quality/nfr-assessment-api-001.md`

**Contents:**
- 6 NFR category assessments (0-100 scores)
- Detailed findings per category
- Compliance status (met/not met)
- Recommendations prioritized
- Gate decision (PASS/CONCERNS/FAIL)
- Remediation plan for gaps

---

#### Next Steps:

```bash
# Address high-priority recommendations
/james *implement task-security-headers
/james *implement task-auto-scaling-config

# Re-assess after fixes
/quinn *assess-nfr task-api-001 --categories security,scalability
```

---

### 9. Risk Assessment for Major Change

**Goal:** Identify and quantify risks before implementing major architectural change

**When to Use:**
- Planning major refactoring
- Considering technology migration
- Evaluating architecture changes

**Duration:** 15-30 minutes

**Complexity:** Standard (score: 40-55)

---

#### Steps:

**Step 1: Risk Assessment**

```bash
/quinn *assess-risk "Migrate from monolithic architecture to microservices" --scope architecture --impact high
```

**Output:**
```
✓ Risk assessment complete

Change: Migrate from monolithic architecture to microservices
Scope: Architecture
Impact Level: High

Identified Risks (12 total):

=== HIGH RISK (P×I > 12) ===

1. Data Consistency Across Services
   Probability: 4/5 (likely)
   Impact: 5/5 (critical)
   Risk Score: 20 (CRITICAL)

   Description:
   Multiple services accessing shared data without distributed transaction management

   Consequences:
   - Data inconsistency between services
   - Race conditions on concurrent updates
   - Potential data loss in failure scenarios

   Mitigation Strategies:
   - Implement event sourcing pattern
   - Use Saga pattern for distributed transactions
   - Add eventual consistency with compensating transactions
   - Implement strict API contracts

   Estimated Mitigation Cost: $25K, 6-8 weeks
   Residual Risk After Mitigation: 8 (Medium)

2. Service Discovery and Communication
   Probability: 3/5 (moderate)
   Impact: 4/5 (high)
   Risk Score: 12 (HIGH)

   Description:
   Services unable to locate and communicate with each other reliably

   Consequences:
   - Service downtime during discovery failures
   - Cascading failures across services
   - Increased latency from service lookups

   Mitigation Strategies:
   - Implement service mesh (Istio or Linkerd)
   - Add health checks and circuit breakers
   - Use DNS-based service discovery
   - Implement retry logic with exponential backoff

   Estimated Mitigation Cost: $15K, 3-4 weeks
   Residual Risk After Mitigation: 4 (Low)

3. Deployment Complexity
   Probability: 4/5 (likely)
   Impact: 3/5 (moderate)
   Risk Score: 12 (HIGH)

   Description:
   Managing deployments of 15+ independent services with dependencies

   Consequences:
   - Deployment failures
   - Version incompatibilities
   - Rollback complexity

   Mitigation Strategies:
   - Implement Kubernetes for orchestration
   - Use Helm charts for deployment
   - Add comprehensive deployment testing
   - Implement blue-green deployments

   Estimated Mitigation Cost: $20K, 4-5 weeks
   Residual Risk After Mitigation: 6 (Medium)

=== MEDIUM RISK (P×I: 6-12) ===

4. Testing Complexity
   Probability: 4/5 (likely)
   Impact: 3/5 (moderate)
   Risk Score: 12 (MEDIUM)

   Mitigation: Contract testing (Pact), service virtualization

5. Monitoring and Observability
   Probability: 3/5 (moderate)
   Impact: 3/5 (moderate)
   Risk Score: 9 (MEDIUM)

   Mitigation: Distributed tracing (Jaeger), centralized logging (ELK)

6. Team Learning Curve
   Probability: 3/5 (moderate)
   Impact: 2/5 (minor)
   Risk Score: 6 (MEDIUM)

   Mitigation: Training, documentation, gradual migration

=== LOW RISK (P×I < 6) ===

7. Infrastructure Costs
   Probability: 2/5 (unlikely)
   Impact: 2/5 (minor)
   Risk Score: 4 (LOW)

8. Documentation Overhead
   Probability: 2/5 (unlikely)
   Impact: 1/5 (minimal)
   Risk Score: 2 (LOW)

[... 4 more low risks]

=== RISK SUMMARY ===

Overall Risk Score: 72/100 (HIGH)

Risk Distribution:
- Critical (P×I > 15): 1 risk
- High (P×I 12-15): 2 risks
- Medium (P×I 6-11): 6 risks
- Low (P×I < 6): 3 risks

Total Mitigation Cost Estimate: $90K - $120K
Total Mitigation Timeline: 16-24 weeks

Recommendation: PROCEED WITH CAUTION

Before proceeding:
1. Implement high-risk mitigations first (data consistency, service discovery)
2. Create detailed migration plan with rollback points
3. Conduct proof-of-concept for 2-3 critical services
4. Train team on microservices patterns
5. Establish monitoring and observability infrastructure

Alternative Approaches:
- Modular monolith (lower risk, gradual decomposition)
- Service-oriented architecture (SOA) as intermediate step
- Strangler fig pattern (gradual migration)

Detailed risk register: .claude/quality/risk-assessment-microservices.md
```

**Step 2: Create Mitigation Plan**

```bash
/alex *create-task-spec "Microservices Migration - Risk Mitigation Phase 1" --context "Address 3 high-risk items from risk assessment"
```

**Output:**
```
✓ Task specification created: task-migration-001

Task: Microservices Migration - Risk Mitigation Phase 1

Objective:
Implement critical risk mitigations before starting microservices migration

Acceptance Criteria:
1. Event sourcing framework implemented and tested
2. Service mesh (Istio) deployed and configured
3. Kubernetes cluster operational with Helm charts
4. Proof-of-concept: 2 services migrated successfully
5. Monitoring infrastructure complete (Jaeger, ELK)

Technical Approach:
Phase 1: Event Sourcing (2 weeks)
- Implement event store (PostgreSQL + Kafka)
- Create event publishing library
- Add event replay capability
- Test with sample service

Phase 2: Service Mesh (2 weeks)
- Deploy Istio to Kubernetes cluster
- Configure traffic management
- Implement circuit breakers
- Add health checks

Phase 3: Deployment Infrastructure (2 weeks)
- Create Helm charts template
- Implement CI/CD pipeline
- Add blue-green deployment
- Test rollback procedures

Phase 4: POC Migration (2 weeks)
- Migrate auth service (low risk)
- Migrate notifications service (medium risk)
- Validate communication patterns
- Performance testing

Estimated Effort: 21 story points (8 weeks)
Risk Reduction: 72 → 35 (48% reduction)

Dependencies:
- Kubernetes cluster provisioning (1 week, DevOps)
- Kafka cluster setup (3 days, DevOps)
- Team training (1 week, ongoing)

Next Steps:
1. Get budget approval ($60K for mitigation)
2. Provision infrastructure
3. Start Phase 1 (event sourcing)
```

---

#### Expected Output:

**Risk Assessment Document:** `.claude/quality/risk-assessment-microservices.md`

**Contents:**
- 12 identified risks with P×I scores
- Risk categorization (Critical/High/Medium/Low)
- Detailed mitigation strategies
- Cost and timeline estimates
- Residual risk after mitigation
- Overall recommendation (Proceed/Proceed with Caution/Don't Proceed)

**Mitigation Plan:** `.claude/tasks/task-migration-001.md`

---

#### Next Steps:

```bash
# Implement mitigation plan
/james *implement task-migration-001

# Monitor risks during implementation
/quinn *assess-risk "Phase 1 Complete" --update task-migration-001
```

---

## Architecture Workflows

### 10. Analyze Existing Codebase Architecture

**Goal:** Comprehensive analysis of existing (brownfield) system architecture

**When to Use:**
- Joining existing project
- Planning modernization
- Assessing production readiness

**Duration:** 10-20 minutes

**Complexity:** Standard (score: 45-60)

---

#### Steps:

**Step 1: Comprehensive Analysis**

```bash
/winston *analyze-architecture . --depth comprehensive --focus all
```

**What Happens:**

**Phase 1: Project Detection**
```
⏳ Analyzing project structure...

Project Type Detected: Fullstack Application
- Frontend: React 18.2 (TypeScript)
- Backend: Express 4.18 (Node.js)
- Database: PostgreSQL 15.2
- Architecture Pattern: Layered + Domain-Driven Design

Tech Stack (32 dependencies detected):
Frontend (18):
- react: 18.2.0
- react-router-dom: 6.8.1
- axios: 1.3.4
- tailwindcss: 3.2.7
[... 14 more]

Backend (14):
- express: 4.18.2
- typeorm: 0.3.12
- passport: 0.6.0
[... 11 more]
```

**Phase 2: Architecture Analysis**
```
⏳ Analyzing architecture patterns...

Detected Patterns:
✓ Layered Architecture (Controllers → Services → Repositories)
✓ Domain-Driven Design (Aggregates, Entities, Value Objects)
✓ CQRS (Partial - read/write separation in services)
✓ Dependency Injection (Using tsyringe)
⚠️ Event Sourcing (Not present, opportunity for async operations)

Architecture Quality: 85/100 (Very Good)
- Separation of Concerns: 90/100 ✓
- Modularity: 85/100 ✓
- Coupling: 80/100 ✓ (low coupling)
- Cohesion: 90/100 ✓ (high cohesion)
```

**Phase 3: Code Quality Analysis**
```
⏳ Analyzing code quality...

Code Quality: 78/100 (Good)

Files Analyzed: 248
- TypeScript: 185 files
- JavaScript: 32 files
- Test files: 31 files

Metrics:
- Avg Complexity: 6.2 (target: <10) ✓
- Avg Function Length: 18 lines (target: <50) ✓
- Max Complexity: 15 (location: src/services/payment.ts:45)
- Duplication: 3.2% (target: <5%) ✓

Top Issues:
1. High complexity in PaymentService.processPayment() (15)
2. Large file: src/api/routes/admin.ts (450 lines)
3. Missing error handling: 12 functions
```

**Phase 4: Test Coverage Analysis**
```
⏳ Analyzing test coverage...

Test Coverage: 76/100 (Good)

Overall Coverage: 76%
- Statements: 78%
- Branches: 72%
- Functions: 80%
- Lines: 76%

Coverage by Module:
- auth: 92% ✓
- users: 85% ✓
- products: 68% ⚠️
- orders: 72% ⚠️
- payments: 58% ⚠️ (needs improvement)
- admin: 45% ⚠️ (needs significant improvement)

Missing Coverage:
- Error paths (22% uncovered)
- Edge cases (18% uncovered)
- Admin functionality (55% uncovered)
```

**Phase 5: Security Analysis**
```
⏳ Analyzing security...

Security: 82/100 (Good)

Authentication:
✓ JWT-based (RS256 algorithm)
✓ Refresh token rotation
✓ Password hashing (bcrypt, 12 rounds)

Authorization:
✓ Role-based access control (3 roles)
⚠️ Missing fine-grained permissions

Vulnerabilities:
✓ No known CVEs in dependencies (npm audit: 0 issues)
✓ SQL injection prevention (TypeORM parameterized queries)
✓ XSS prevention (React auto-escaping)
⚠️ CSRF protection not implemented (4 endpoints vulnerable)
⚠️ Rate limiting basic (global only, no per-user)

Security Headers:
⚠️ Missing: HSTS, X-Frame-Options, Content-Security-Policy
✓ Present: X-Content-Type-Options, X-XSS-Protection
```

**Phase 6: Performance Analysis**
```
⏳ Analyzing performance...

Performance: 72/100 (Good)

Response Times (from logs):
- P50: 85ms ✓
- P95: 240ms ⚠️ (target: <200ms)
- P99: 650ms ⚠️ (spikes detected)

Bottlenecks Identified:
1. N+1 queries in order listing (src/services/orders.ts:120)
2. Missing indexes on products.category, orders.user_id
3. No caching layer (Redis opportunity)
4. Large payload responses (orders API: 2.5MB avg)

Database:
- Queries: 1,850/day avg
- Slow queries: 12% > 100ms
- Connection pool: 10 (may need increase)
```

**Phase 7: Scalability Analysis**
```
⏳ Analyzing scalability...

Scalability: 65/100 (Needs Improvement)

Current Limitations:
- Stateful sessions (in-memory, not horizontally scalable)
- Single database instance (no read replicas)
- Synchronous background jobs (blocks requests)
- No load balancing configured

Estimated Capacity:
- Current: ~150 concurrent users
- With optimizations: ~500 concurrent users
- With architecture changes: 2,000+ concurrent users

Recommendations for Scaling:
1. Migrate sessions to Redis (horizontal scaling)
2. Add database read replicas
3. Implement async job queue (Bull + Redis)
4. Add load balancer (Nginx or AWS ALB)
```

**Phase 8: Technical Debt Analysis**
```
⏳ Analyzing technical debt...

Technical Debt: 70/100 (Moderate)

Debt Items (15 identified):
1. Outdated dependencies (5 packages, 6-12 months old)
2. Missing API documentation (12 endpoints)
3. Inconsistent error handling patterns
4. No integration tests (only unit + E2E)
5. Frontend state management complexity

Estimated Remediation:
- Time: 3-4 weeks
- Cost: $15K - $20K
- Priority: Medium
```

**Final Report:**
```
✓ Architecture analysis complete

=== PRODUCTION READINESS SCORE: 74/100 ⭐⭐⭐ ===

Dimension Scores:
1. Architecture Quality: 85/100 ✓ Very Good
2. Code Quality: 78/100 ✓ Good
3. Test Coverage: 76/100 ✓ Good
4. Security: 82/100 ✓ Good
5. Performance: 72/100 ⚠️ Good (needs optimization)
6. Scalability: 65/100 ⚠️ Needs Improvement
7. Maintainability: 80/100 ✓ Good
8. Technical Debt: 70/100 ⚠️ Moderate

=== TOP 5 PRIORITIES ===

1. SCALABILITY (Priority: HIGH)
   - Migrate to Redis sessions (enables horizontal scaling)
   - Add database read replicas
   - Implement async job queue
   Estimated Impact: +15 points (65 → 80)

2. PERFORMANCE (Priority: HIGH)
   - Fix N+1 queries (3 locations)
   - Add database indexes
   - Implement Redis caching
   Estimated Impact: +10 points (72 → 82)

3. SECURITY (Priority: MEDIUM)
   - Add CSRF protection
   - Implement security headers
   - Add per-user rate limiting
   Estimated Impact: +8 points (82 → 90)

4. TEST COVERAGE (Priority: MEDIUM)
   - Increase payments module coverage (58% → 80%)
   - Add admin module tests (45% → 75%)
   - Add integration tests
   Estimated Impact: +9 points (76 → 85)

5. TECHNICAL DEBT (Priority: LOW)
   - Update outdated dependencies
   - Add API documentation
   - Standardize error handling
   Estimated Impact: +10 points (70 → 80)

=== MODERNIZATION OPPORTUNITIES ===

1. Add Real-Time Features
   - Implement WebSocket support for live updates
   - Use Socket.IO or native WebSockets
   - Estimated effort: 2-3 weeks

2. Implement Caching Strategy
   - Redis for sessions, query cache, API cache
   - Estimated effort: 1-2 weeks
   - Performance impact: 40% response time reduction

3. Microservices Potential
   - Auth service (well-isolated)
   - Notifications service (async-friendly)
   - Consider for future scaling
   - Estimated effort: 8-12 weeks

=== NEXT STEPS ===

Immediate (Week 1):
1. Review detailed report
2. Prioritize improvements with team
3. Create improvement backlog

Short-Term (Weeks 2-4):
1. Fix N+1 queries and add indexes
2. Migrate sessions to Redis
3. Add CSRF protection

Medium-Term (Months 2-3):
1. Implement caching layer
2. Add database read replicas
3. Increase test coverage to 85%+

=== FILES GENERATED ===

✓ docs/architecture-analysis-20251105.md (complete report)
✓ docs/architecture-diagrams/ (C4 diagrams)
  - system-context.png
  - container-diagram.png
  - component-diagram.png
✓ docs/tech-stack-inventory.md (32 dependencies)
✓ docs/architecture-decision-records/ (5 ADRs discovered)
✓ docs/improvement-roadmap.md (prioritized recommendations)

Total Duration: 12 minutes
```

---

#### Expected Output:

**Main Report:** `docs/architecture-analysis-20251105.md`

**Contents:**
- Production readiness score (0-100) with ⭐ rating
- 8 dimension assessments (0-100 each)
- Top 5 priorities with impact estimates
- Modernization opportunities
- Next steps roadmap
- Detailed findings per dimension

**Architecture Diagrams:** `docs/architecture-diagrams/`
- System context diagram (C4 Level 1)
- Container diagram (C4 Level 2)
- Component diagrams (C4 Level 3)

**Supporting Documents:**
- `docs/tech-stack-inventory.md` (all dependencies)
- `docs/architecture-decision-records/` (discovered ADRs)
- `docs/improvement-roadmap.md` (prioritized plan)

---

#### Next Steps:

```bash
# Option A: Create improvement plan
/alex *breakdown-epic "Architecture Improvement Plan" --context docs/architecture-analysis-20251105.md

# Option B: Compare modernization options
/winston *compare-architectures "Improve scalability and performance" --current docs/architecture-analysis-20251105.md

# Option C: Implement highest priority improvement
/james *implement "Migrate sessions to Redis for horizontal scaling"
```

---

### 11. Design Greenfield System Architecture

**Goal:** Design complete system architecture from requirements

**When to Use:**
- Starting new project
- Designing new major feature
- Need comprehensive architecture document

**Duration:** 15-25 minutes

**Complexity:** Standard (score: 50-65)

---

#### Steps:

**Step 1: Create PRD (if not exists)**

```bash
/alex *create-prd "E-commerce Platform for Handmade Crafts"
```

**Output:**
```
✓ PRD created: docs/prd-ecommerce-platform.md

PRD Summary:
- Vision: Marketplace connecting craftspeople with buyers
- Target Users: Craftspeople (sellers), Buyers, Admins
- Core Features (8):
  1. User registration/authentication
  2. Seller storefronts
  3. Product listings with photos
  4. Shopping cart and checkout
  5. Payment processing (Stripe)
  6. Order management
  7. Reviews and ratings
  8. Admin dashboard

- Non-Functional Requirements:
  - Security: PCI DSS compliant
  - Performance: < 200ms response time
  - Scalability: Support 10,000 concurrent users
  - Availability: 99.9% uptime

- Constraints:
  - Budget: $100K for 6 months
  - Technology: Must use AWS
  - Timeline: MVP in 3 months
```

**Step 2: Design Architecture**

```bash
/winston *create-architecture docs/prd-ecommerce-platform.md --type fullstack --depth comprehensive
```

**What Happens:**

**Phase 1: Requirements Analysis**
```
⏳ Analyzing requirements...

Identified Requirements:
- Functional: 8 core features
- Non-Functional: 6 categories
- Constraints: Budget, timeline, technology

Architecture Complexity: MODERATE
- Users: 10K concurrent (medium scale)
- Features: 8 (standard complexity)
- Integrations: 3 (Stripe, Email, Storage)
```

**Phase 2: Architecture Pattern Selection**
```
⏳ Selecting architecture patterns...

Recommended Patterns:
1. Overall: Layered Architecture (3-tier)
   - Justification: Standard complexity, team familiarity, maintainability
   - Alternative considered: Microservices (rejected: over-engineering for MVP)

2. Frontend: Component-Based (React + Redux)
   - Justification: Rich UI requirements, state management needs
   - Alternative considered: Vue (rejected: team expertise in React)

3. Backend: RESTful API (Express.js)
   - Justification: Standard CRUD operations, stateless
   - Alternative considered: GraphQL (deferred to v2.0)

4. Data: Relational Database (PostgreSQL)
   - Justification: Strong consistency needs, complex relationships
   - Alternative considered: MongoDB (rejected: ACID requirements)

5. Caching: Redis
   - Justification: Session management, query cache, rate limiting

6. Storage: S3 (object storage)
   - Justification: Product images, scalable, cost-effective

7. Async Jobs: Bull Queue + Redis
   - Justification: Email sending, image processing, order notifications
```

**Phase 3: Technology Stack Selection**
```
⏳ Selecting technology stack...

Frontend:
- Framework: React 18.2 (component-based UI)
- State Management: Redux Toolkit (centralized state)
- Routing: React Router 6 (client-side routing)
- Styling: Tailwind CSS (utility-first, rapid development)
- HTTP Client: Axios (API communication)
- Build Tool: Vite (fast development, optimized builds)

Backend:
- Runtime: Node.js 18 LTS (JavaScript full-stack)
- Framework: Express 4.18 (mature, flexible)
- ORM: TypeORM (TypeScript support, migrations)
- Validation: Joi (schema validation)
- Authentication: Passport.js + JWT (industry standard)
- API Documentation: Swagger/OpenAPI (auto-generated docs)

Database:
- Primary: PostgreSQL 15 (relational, ACID compliance)
- Cache: Redis 7 (in-memory, pub/sub, queues)
- Search: ElasticSearch (product search, optional v2.0)

Infrastructure (AWS):
- Compute: EC2 + Auto Scaling Group (horizontal scaling)
- Load Balancer: Application Load Balancer (ALB)
- Storage: S3 (images), RDS PostgreSQL (database)
- CDN: CloudFront (static asset delivery)
- DNS: Route 53 (domain management)
- Monitoring: CloudWatch (logs, metrics, alarms)

Third-Party Services:
- Payments: Stripe (PCI compliant payment processing)
- Email: SendGrid (transactional emails)
- Image Processing: Sharp (server-side) + S3 (storage)
```

**Phase 4: System Design**
```
⏳ Designing system architecture...

System Context (C4 Level 1):
- Users: Buyers, Sellers, Admins
- External Systems: Stripe, SendGrid, AWS S3
- System: E-commerce Platform

Container Architecture (C4 Level 2):
1. Web Application (React SPA)
   - User interface
   - Hosted on CloudFront + S3
   - Communicates with API via HTTPS

2. API Server (Express)
   - RESTful API
   - Authentication/Authorization
   - Business logic
   - Hosted on EC2 (Auto Scaling)

3. Database (PostgreSQL)
   - Relational data storage
   - RDS Multi-AZ for high availability

4. Cache (Redis)
   - Session storage
   - Query cache
   - Job queue
   - ElastiCache

5. Object Storage (S3)
   - Product images
   - User avatars
   - Static assets

6. Background Workers (Node.js)
   - Email sending
   - Image processing
   - Order notifications
   - Hosted on EC2
```

**Phase 5: Data Model Design**
```
⏳ Designing data model...

Entities (9 total):
1. User
   - id, email, password_hash, role (buyer/seller/admin)
   - created_at, updated_at

2. Seller
   - id, user_id, shop_name, description, logo_url
   - stripe_account_id

3. Product
   - id, seller_id, title, description, price, quantity
   - images (JSON array), category_id, tags (JSON array)

4. Category
   - id, name, slug, parent_category_id (self-referential)

5. Cart
   - id, user_id, created_at, updated_at

6. CartItem
   - id, cart_id, product_id, quantity

7. Order
   - id, buyer_id, seller_id, total_amount, status
   - stripe_payment_id, created_at

8. OrderItem
   - id, order_id, product_id, quantity, price_at_purchase

9. Review
   - id, product_id, user_id, rating, comment
   - created_at

Relationships:
- User 1:1 Seller (optional)
- Seller 1:N Products
- Product N:1 Category
- User 1:1 Cart
- Cart 1:N CartItems
- CartItem N:1 Product
- User 1:N Orders (as buyer)
- Seller 1:N Orders (as seller)
- Order 1:N OrderItems
- Product 1:N Reviews
```

**Phase 6: API Design**
```
⏳ Designing API contracts...

API Endpoints (24 total):

Authentication:
POST /api/auth/register
POST /api/auth/login
POST /api/auth/refresh-token
POST /api/auth/logout

Users:
GET    /api/users/me
PUT    /api/users/me
DELETE /api/users/me

Sellers:
GET    /api/sellers
GET    /api/sellers/:id
POST   /api/sellers (authenticated)
PUT    /api/sellers/:id (owner only)

Products:
GET    /api/products (with pagination, filtering)
GET    /api/products/:id
POST   /api/products (seller only)
PUT    /api/products/:id (owner only)
DELETE /api/products/:id (owner only)

Cart:
GET    /api/cart (authenticated)
POST   /api/cart/items (add to cart)
PUT    /api/cart/items/:id (update quantity)
DELETE /api/cart/items/:id (remove from cart)

Orders:
GET    /api/orders (authenticated, filtered by role)
GET    /api/orders/:id
POST   /api/orders (create from cart)

[... 6 more endpoint groups]

All endpoints documented in OpenAPI 3.0 spec.
```

**Phase 7: Security Design**
```
⏳ Designing security architecture...

Security Measures:

1. Authentication:
   - JWT tokens (access token + refresh token)
   - Access token: 15-minute expiry
   - Refresh token: 7-day expiry, stored in httpOnly cookie
   - Password hashing: bcrypt (12 rounds)

2. Authorization:
   - Role-based access control (RBAC)
   - Roles: Buyer, Seller, Admin
   - Permissions: Resource-based (can only edit own products)

3. Input Validation:
   - Joi schemas for all request bodies
   - Sanitization to prevent XSS
   - Parameterized queries (SQL injection prevention)

4. Rate Limiting:
   - Global: 100 requests/minute/IP
   - Authentication: 5 login attempts/15 minutes
   - API: 1,000 requests/hour/user

5. HTTPS:
   - TLS 1.3 required
   - HSTS header enabled

6. Security Headers:
   - Content-Security-Policy
   - X-Frame-Options: DENY
   - X-Content-Type-Options: nosniff

7. PCI DSS Compliance:
   - Use Stripe (handles payment data)
   - No credit card storage
   - Tokenization for saved payment methods

8. GDPR Compliance:
   - User data export endpoint
   - Account deletion endpoint
   - Cookie consent
   - Privacy policy
```

**Phase 8: NFR Mapping**
```
⏳ Mapping non-functional requirements to architecture...

Performance (<200ms response time):
- Redis caching (90% hit rate target)
- Database indexing (primary keys, foreign keys, search columns)
- CDN for static assets (CloudFront)
- Connection pooling (database)
- Query optimization (N+1 prevention)

Scalability (10K concurrent users):
- Horizontal scaling (Auto Scaling Group: 2-8 instances)
- Stateless API (sessions in Redis)
- Database read replicas (2 replicas)
- Load balancer (ALB with health checks)
- Async background jobs (Bull queue)

Availability (99.9% uptime):
- Multi-AZ deployment (database, load balancer)
- Health checks (ALB, EC2, RDS)
- Auto-recovery (Auto Scaling Group)
- Monitoring and alerting (CloudWatch)
- Backup strategy (RDS automated backups, S3 versioning)

Security (PCI DSS):
- Stripe integration (handles sensitive data)
- HTTPS everywhere
- Security headers
- Input validation
- Rate limiting

Maintainability:
- Code quality standards (ESLint, Prettier)
- Comprehensive testing (unit, integration, E2E)
- API documentation (Swagger)
- ADRs for key decisions
- CI/CD pipeline (GitHub Actions)
```

**Phase 9: Architecture Decision Records (ADRs)**
```
⏳ Creating Architecture Decision Records...

ADRs Created (8):

1. ADR-001: Use Layered Architecture
   - Context: Need maintainable architecture for MVP
   - Decision: 3-tier layered architecture
   - Alternatives: Microservices (overkill), Monolith (rejected)
   - Consequences: Easy to maintain, but may need decomposition at scale

2. ADR-002: PostgreSQL for Primary Database
   - Context: Need ACID compliance, complex relationships
   - Decision: PostgreSQL 15
   - Alternatives: MongoDB (weak consistency), MySQL (less features)
   - Consequences: Strong consistency, but vertical scaling limits

3. ADR-003: React for Frontend
   - Context: Need rich UI, team expertise
   - Decision: React 18 + Redux Toolkit
   - Alternatives: Vue (team unfamiliar), Angular (over-engineered)
   - Consequences: Large ecosystem, but learning curve for Redux

4. ADR-004: Express.js for Backend
   - Context: Need flexible API framework
   - Decision: Express 4.18
   - Alternatives: NestJS (more structure), Fastify (less mature)
   - Consequences: Flexibility, but manual structuring needed

5. ADR-005: Stripe for Payment Processing
   - Context: Need PCI compliant payment solution
   - Decision: Stripe
   - Alternatives: PayPal (less developer-friendly), Braintree (more complex)
   - Consequences: Easy integration, but 2.9% + $0.30 fee

6. ADR-006: Redis for Caching and Sessions
   - Context: Need fast cache and session store
   - Decision: Redis 7
   - Alternatives: Memcached (less features), DynamoDB (overkill)
   - Consequences: Fast, but single point of failure (mitigate with ElastiCache)

7. ADR-007: S3 for Object Storage
   - Context: Need scalable image storage
   - Decision: AWS S3
   - Alternatives: Local filesystem (not scalable), EFS (expensive)
   - Consequences: Scalable and cheap, but added latency (mitigate with CloudFront)

8. ADR-008: Bull Queue for Background Jobs
   - Context: Need async job processing (emails, image processing)
   - Decision: Bull + Redis
   - Alternatives: AWS SQS (more complex), RabbitMQ (over-engineered)
   - Consequences: Simple and reliable, but requires Redis
```

**Phase 10: Deployment Architecture**
```
⏳ Designing deployment architecture...

Deployment Strategy:
- Environment: Production, Staging, Development
- Deployment Model: Blue-Green
- CI/CD: GitHub Actions
- Infrastructure as Code: Terraform

Production Architecture:
- Region: us-east-1 (primary), us-west-2 (DR)
- Availability Zones: 2 AZs for high availability

Components:
1. CloudFront + S3 (Frontend)
   - S3 bucket: static website hosting
   - CloudFront: CDN distribution
   - ACM: SSL certificate

2. Application Load Balancer
   - HTTPS listener (port 443)
   - Target Group: API servers
   - Health checks: /health endpoint

3. Auto Scaling Group (API Servers)
   - Min: 2 instances (high availability)
   - Desired: 2 instances
   - Max: 8 instances (scale on CPU > 70%)
   - Instance Type: t3.medium (2 vCPU, 4 GB RAM)

4. RDS PostgreSQL
   - Instance: db.t3.medium (2 vCPU, 4 GB RAM)
   - Multi-AZ: Yes (automatic failover)
   - Backups: Daily automated, 7-day retention
   - Read Replicas: 2 (for scaling reads)

5. ElastiCache Redis
   - Node: cache.t3.medium
   - Replication: 2 replicas (high availability)
   - Auto failover: Enabled

6. S3 Buckets
   - Product images bucket
   - Static assets bucket
   - Backup bucket
   - Versioning: Enabled
   - Lifecycle: 90-day archive to Glacier

7. Background Workers (EC2)
   - Min: 1 instance
   - Max: 4 instances (scale on queue depth)
   - Instance Type: t3.small
```

**Final Output:**
```
✓ Architecture design complete

=== ARCHITECTURE SUMMARY ===

System: E-commerce Platform for Handmade Crafts
Architecture Pattern: Layered (3-tier)
Type: Fullstack Web Application
Scale: 10,000 concurrent users

Technology Stack:
- Frontend: React 18 + Redux + Tailwind CSS
- Backend: Node.js 18 + Express + TypeORM
- Database: PostgreSQL 15 (RDS Multi-AZ)
- Cache: Redis 7 (ElastiCache)
- Storage: S3 + CloudFront
- Infrastructure: AWS (us-east-1)

Components:
- Web App (CloudFront + S3)
- API Server (EC2 Auto Scaling)
- Database (RDS PostgreSQL Multi-AZ + 2 read replicas)
- Cache (ElastiCache Redis with replication)
- Object Storage (S3)
- Background Workers (EC2 Auto Scaling)
- Load Balancer (ALB)

Data Model: 9 entities, 12 relationships

API: 24 RESTful endpoints (OpenAPI 3.0 documented)

Security:
- Authentication: JWT (access + refresh tokens)
- Authorization: RBAC (3 roles)
- PCI DSS compliant (via Stripe)
- HTTPS/TLS 1.3 required
- Rate limiting enabled

NFR Compliance:
✓ Performance: <200ms (caching, CDN, optimization)
✓ Scalability: 10K users (horizontal scaling, read replicas)
✓ Availability: 99.9% (Multi-AZ, auto-recovery)
✓ Security: PCI DSS (Stripe integration)
✓ Maintainability: High (testing, documentation, standards)

Estimated Costs:
- Development: $80K (6 developers, 3 months)
- Infrastructure: $800/month (AWS services)
- Third-Party: $500/month (Stripe fees, SendGrid)
- Total Year 1: $95K (within $100K budget)

=== FILES GENERATED ===

✓ docs/architecture.md (complete architecture document, 45 pages)
✓ docs/architecture-diagrams/ (C4 diagrams)
  - system-context.svg
  - container-diagram.svg
  - component-diagram-api.svg
  - component-diagram-frontend.svg
  - deployment-diagram.svg
✓ docs/data-model.svg (ER diagram)
✓ docs/api-specification.yaml (OpenAPI 3.0)
✓ docs/architecture-decision-records/ (8 ADRs)
  - ADR-001-layered-architecture.md
  - ADR-002-postgresql-database.md
  - ADR-003-react-frontend.md
  - [... 5 more ADRs]
✓ docs/tech-stack.md (complete technology inventory)
✓ docs/nfr-mapping.md (NFR to architecture mapping)
✓ docs/deployment-guide.md (infrastructure setup)
✓ docs/security-architecture.md (security design)

Total Duration: 18 minutes
```

---

#### Expected Output:

**Main Document:** `docs/architecture.md` (45 pages)

**Sections:**
1. Executive Summary
2. System Context
3. Container Architecture
4. Component Design
5. Data Model
6. API Design
7. Security Architecture
8. NFR Mapping
9. Deployment Architecture
10. Technology Stack
11. ADRs (8 decisions)
12. Cost Estimates
13. Migration Strategy (if applicable)
14. Next Steps

**Diagrams (6 total):**
- System context (C4 Level 1)
- Container diagram (C4 Level 2)
- Component diagrams (C4 Level 3)
- Data model (ER diagram)
- Deployment diagram
- Security architecture diagram

**Supporting Documents:**
- OpenAPI specification (24 endpoints)
- 8 Architecture Decision Records
- Technology stack inventory
- NFR mapping document
- Deployment guide
- Security architecture document

---

#### Next Steps:

```bash
# Option A: Validate architecture
/winston *review-architecture docs/architecture.md

# Option B: Create implementation plan
/alex *breakdown-epic docs/architecture.md --type architecture

# Option C: Start MVP development
/james *implement task-mvp-001
```

---

### 12. Compare Architecture Options for Modernization

**Goal:** Generate and compare 3 architecture options with trade-offs analysis

**When to Use:**
- Modernizing existing system
- Evaluating technology migration
- Making major architectural decisions

**Duration:** 10-15 minutes

**Complexity:** Standard (score: 45-55)

---

#### Steps:

**Step 1: Compare Architecture Options**

```bash
/winston *compare-architectures "Scale to 50K users and add real-time features" --current docs/architecture-analysis-20251105.md
```

**What Happens:**

**Phase 1: Analyze Current State**
```
⏳ Analyzing current architecture...

Current System:
- Type: Layered monolith (React + Express + PostgreSQL)
- Capacity: 1,500 req/sec (~1,000 concurrent users)
- Gaps:
  * No real-time capabilities
  * Limited horizontal scaling (stateful sessions)
  * Single database (no read replicas)

Target Requirements:
- Scale to 50K concurrent users (~75K req/sec)
- Add real-time features (WebSocket support)
- Maintain or improve performance (<200ms)
```

**Phase 2: Generate Options**
```
⏳ Generating architecture options...

=== OPTION A: MINIMAL CHANGES (Quick Wins) ===

Strategy: Incremental improvements to existing architecture

Changes:
1. Add Socket.IO for real-time features
   - WebSocket server on existing Express instances
   - Shared Redis for pub/sub across instances

2. Migrate sessions to Redis
   - Enables stateless API servers
   - Horizontal scaling possible

3. Add read replicas (2 replicas)
   - Offload read traffic from primary
   - Use read replica for product queries

4. Implement basic caching (Redis)
   - Cache frequently accessed data (products, categories)
   - 5-minute TTL

Architecture Diagram:
```
┌──────────────┐
│  CloudFront  │
│   (CDN)      │
└──────┬───────┘
       │
┌──────▼───────┐
│ Load Balancer│
└──────┬───────┘
       │
       ├─────────────────┐
       │                 │
┌──────▼──────┐   ┌─────▼───────┐
│   API       │   │   API       │
│ + WebSocket │   │ + WebSocket │
└──────┬──────┘   └──────┬──────┘
       │                 │
       └─────────┬───────┘
                 │
         ┌───────▼────────┐
         │  Redis Cluster │
         │ (Sessions,     │
         │  Cache, PubSub)│
         └───────┬────────┘
                 │
       ┌─────────┴─────────┐
       │                   │
┌──────▼──────┐     ┌──────▼──────┐
│ PostgreSQL  │────▶│ Read Replica│
│  (Primary)  │     │   (x2)      │
└─────────────┘     └─────────────┘
```

**Benefits:**
✓ Fast implementation (4-6 weeks)
✓ Low risk (incremental changes)
✓ Immediate value (real-time features working)
✓ Low cost ($25K - $40K)
✓ Team familiarity (minimal learning curve)

**Drawbacks:**
⚠️ Limited scalability (~15K concurrent users max)
⚠️ Monolith constraints remain
⚠️ Single database bottleneck at scale
⚠️ WebSocket connections limited per server

**Trade-Offs:**
- Cost: $$$ (LOW)
- Timeline: 4-6 weeks (FAST)
- Risk: ⚠️ Low
- Scalability: 15K users (LIMITED)
- Performance: 150ms P95 (GOOD)
- Maintainability: Same (UNCHANGED)
- Technical Debt: Increases slightly

**Cost Breakdown:**
- Development: 3 developers × 6 weeks = $25K
- Infrastructure (monthly): $600 (+$200/month)
- Total Year 1: $28K

**Recommendation:** Good for MVP or temporary solution while planning larger refactor.

---

=== OPTION B: MODERATE REFACTOR (Balanced Approach) ✅ RECOMMENDED ===

Strategy: Strategic decomposition with modern practices

Changes:
1. Real-Time Microservice
   - Dedicated Node.js service for WebSocket connections
   - Redis pub/sub for message distribution
   - Horizontal scaling: 2-10 instances

2. API Gateway (Kong or AWS API Gateway)
   - Route management
   - Rate limiting
   - Authentication offload

3. Caching Layer (Redis Cluster)
   - Multi-tier caching (L1: API, L2: Redis)
   - Cache invalidation patterns
   - Session management

4. Database Scaling
   - Primary + 2 read replicas
   - Connection pooling (PgBouncer)
   - Sharding preparation (not implemented yet)

5. Message Queue (RabbitMQ or AWS SQS)
   - Async operations (emails, notifications)
   - Event-driven architecture foundation

Architecture Diagram:
```
┌──────────────┐
│  CloudFront  │
│   (CDN)      │
└──────┬───────┘
       │
┌──────▼───────┐
│ API Gateway  │
│   (Kong)     │
└──────┬───────┘
       │
       ├──────────────────────┐
       │                      │
┌──────▼──────┐     ┌─────────▼────────┐
│   API       │     │   Real-Time      │
│  Service    │     │   Microservice   │
│ (2-6 inst)  │     │  (WebSocket)     │
└──────┬──────┘     │   (2-10 inst)    │
       │            └─────────┬────────┘
       │                      │
       └──────────┬───────────┘
                  │
       ┌──────────▼──────────┐
       │  Redis Cluster      │
       │ (Cache, Sessions,   │
       │  Pub/Sub, Queue)    │
       └──────────┬──────────┘
                  │
       ┌──────────▼──────────┐
       │  Message Queue      │
       │   (RabbitMQ)        │
       └──────────┬──────────┘
                  │
       ┌──────────┴──────────┐
       │                     │
┌──────▼──────┐       ┌──────▼──────┐
│ PostgreSQL  │──────▶│ Read Replica│
│  (Primary)  │       │   (x2)      │
└─────────────┘       └─────────────┘
```

**Benefits:**
✓ Scales to 50K+ concurrent users
✓ Real-time features performant (dedicated service)
✓ Reduces technical debt significantly
✓ Prepares for future microservices (gradual path)
✓ Improved monitoring and observability
✓ Better separation of concerns

**Drawbacks:**
⚠️ Medium complexity (2-3 months development)
⚠️ Learning curve (API gateway, message queue)
⚠️ Increased operational overhead (more services)
⚠️ Migration effort required

**Trade-Offs:**
- Cost: $$$$ (MEDIUM)
- Timeline: 2-3 months (MODERATE)
- Risk: ⚠️⚠️ Medium
- Scalability: 50K+ users (EXCELLENT)
- Performance: 95ms P95 (EXCELLENT)
- Maintainability: Improved (BETTER)
- Technical Debt: Reduced significantly

**Cost Breakdown:**
- Development: 4 developers × 3 months = $60K
- Infrastructure (monthly): $1,200 (+$800/month)
- Migration effort: $15K
- Total Year 1: $85K

**Why Recommended:**
- Best balance of cost, timeline, and outcome
- Achieves 50K user goal with headroom
- Reduces technical debt
- Foundation for future growth
- Proven architecture patterns
- Manageable complexity

**Migration Strategy:**
Phase 1 (Month 1): Infrastructure setup (Redis, API gateway, message queue)
Phase 2 (Month 2): Real-time microservice development and deployment
Phase 3 (Month 3): Database scaling, optimization, cutover

---

=== OPTION C: FULL MODERNIZATION (Best Long-Term) ===

Strategy: Complete microservices architecture with event sourcing

Changes:
1. Decompose into 6 Microservices
   - Auth Service
   - User Service
   - Product Service
   - Order Service
   - Payment Service
   - Real-Time Notification Service

2. Event-Driven Architecture
   - Kafka for event streaming
   - Event sourcing for order/payment domains
   - CQRS pattern (separate read/write models)

3. API Gateway + Service Mesh
   - Kong API Gateway
   - Istio service mesh (traffic management, security)

4. Advanced Caching
   - Redis Cluster (distributed cache)
   - CDN (CloudFront) for API responses
   - Client-side caching (service workers)

5. Polyglot Persistence
   - PostgreSQL (transactional data: orders, payments)
   - MongoDB (product catalog: flexible schema)
   - ElasticSearch (product search)
   - Redis (sessions, cache)

6. Kubernetes Orchestration
   - EKS (managed Kubernetes)
   - Auto-scaling (HPA + Cluster Autoscaler)
   - Blue-green deployments

Architecture Diagram:
```
┌──────────────┐
│  CloudFront  │
│   (CDN)      │
└──────┬───────┘
       │
┌──────▼───────┐
│ API Gateway  │
│   (Kong)     │
└──────┬───────┘
       │
┌──────▼───────────────────────────────────┐
│          Service Mesh (Istio)            │
│                                          │
│  ┌───────┐ ┌────────┐ ┌────────┐       │
│  │ Auth  │ │ User   │ │Product │       │
│  │Service│ │Service │ │Service │       │
│  └───┬───┘ └───┬────┘ └───┬────┘       │
│      │         │           │            │
│  ┌───▼────┐ ┌─▼──────┐ ┌─▼────────┐   │
│  │Order   │ │Payment │ │Real-Time │   │
│  │Service │ │Service │ │Service   │   │
│  └───┬────┘ └───┬────┘ └───┬──────┘   │
└──────┼─────────┼──────────┼───────────┘
       │         │          │
       └─────────┼──────────┘
                 │
       ┌─────────▼──────────┐
       │   Kafka Cluster    │
       │  (Event Stream)    │
       └─────────┬──────────┘
                 │
       ┌─────────┼──────────────────┐
       │         │                  │
┌──────▼──────┐ │ ┌────────▼──────┐│
│ PostgreSQL  │ │ │   MongoDB     ││
│  Cluster    │ │ │   Cluster     ││
└─────────────┘ │ └───────────────┘│
                │                   │
         ┌──────▼──────┐  ┌────────▼──────┐
         │    Redis    │  │ ElasticSearch │
         │   Cluster   │  │    Cluster    │
         └─────────────┘  └───────────────┘
```

**Benefits:**
✓ Scales to 100K+ concurrent users
✓ Best performance (50ms P95)
✓ Independent service scaling
✓ Technology flexibility (polyglot)
✓ Fault isolation
✓ Future-proof architecture
✓ Excellent observability

**Drawbacks:**
⚠️ High complexity (4-6 months)
⚠️ Significant learning curve
⚠️ Operational overhead (many services)
⚠️ High cost ($150K+)
⚠️ Testing complexity (contract tests, service mocks)
⚠️ Data consistency challenges (distributed transactions)

**Trade-Offs:**
- Cost: $$$$$ (HIGH)
- Timeline: 4-6 months (LONG)
- Risk: ⚠️⚠️⚠️ High
- Scalability: 100K+ users (OUTSTANDING)
- Performance: 50ms P95 (OUTSTANDING)
- Maintainability: Best (service isolation)
- Technical Debt: Eliminated

**Cost Breakdown:**
- Development: 6 developers × 6 months = $150K
- Infrastructure (monthly): $2,500 (+$2,100/month)
- Migration effort: $40K
- Training: $10K
- Total Year 1: $220K

**When to Choose:**
- Planning for 100K+ users in near future
- Have budget and timeline flexibility
- Team experienced with microservices
- Complex domain requiring service isolation
- Long-term strategic investment

**Migration Strategy:**
Phase 1 (Months 1-2): Infrastructure (Kubernetes, Kafka, service mesh)
Phase 2 (Months 3-4): Microservices development (strangler fig pattern)
Phase 3 (Months 5-6): Migration, optimization, cutover

---

=== COMPARISON MATRIX ===

| Dimension | Option A (Minimal) | Option B (Moderate) ✅ | Option C (Full) |
|-----------|-------------------|------------------------|-----------------|
| **Cost (Year 1)** | $28K | $85K | $220K |
| **Timeline** | 4-6 weeks | 2-3 months | 4-6 months |
| **Risk** | Low | Medium | High |
| **Max Users** | 15K | 50K+ | 100K+ |
| **Performance (P95)** | 150ms | 95ms | 50ms |
| **Scalability** | Limited | Excellent | Outstanding |
| **Maintainability** | Same | Improved | Best |
| **Technical Debt** | +10% | -40% | -90% |
| **Learning Curve** | None | Medium | High |
| **Operational Overhead** | +10% | +40% | +100% |

=== EVIDENCE-BASED RECOMMENDATION ===

**RECOMMENDED: Option B (Moderate Refactor)**

**Confidence:** 90%

**Justification:**
1. **Meets Requirements:** Scales to 50K+ users with headroom
2. **Achieves Real-Time:** Dedicated microservice handles WebSocket connections
3. **Cost-Effective:** $85K vs $220K (61% savings vs Option C)
4. **Faster Time-to-Market:** 3 months vs 6 months (50% faster)
5. **Balanced Risk:** Medium complexity manageable by experienced team
6. **Reduces Debt:** Significant improvement without over-engineering
7. **Foundation for Future:** Can evolve to Option C incrementally if needed

**Why Not Option A:**
- Doesn't achieve 50K user goal (only 15K)
- Increases technical debt
- Short-term solution requiring future rework

**Why Not Option C:**
- Over-engineered for 50K user requirement (designed for 100K+)
- 2.6x more expensive ($220K vs $85K)
- 2x longer timeline (6 months vs 3 months)
- Higher operational complexity
- Team may lack microservices experience

**Next Steps if Option B Selected:**
1. Review detailed architecture design
2. Create migration plan with risk mitigation
3. Provision infrastructure (Month 1)
4. Develop real-time microservice (Month 2)
5. Implement database scaling (Month 3)
6. Cutover with blue-green deployment

=== FILES GENERATED ===

✓ docs/architecture-comparison-20251105.md (complete comparison, 28 pages)
✓ docs/architecture-options/ (3 detailed designs)
  - option-a-minimal.md
  - option-b-moderate.md (recommended)
  - option-c-full.md
✓ docs/architecture-diagrams/ (9 diagrams)
  - option-a-architecture.svg
  - option-b-architecture.svg (recommended)
  - option-c-architecture.svg
  - comparison-matrix.svg
  - [... 5 more diagrams]
✓ docs/trade-offs-analysis.md (detailed trade-offs)
✓ docs/cost-comparison.md (cost breakdown)
✓ docs/migration-strategy-option-b.md (recommended option migration plan)

Total Duration: 12 minutes
```

---

#### Expected Output:

**Main Document:** `docs/architecture-comparison-20251105.md` (28 pages)

**Contents:**
- Current state analysis
- 3 architecture options (Minimal, Moderate, Full)
- Architecture diagrams for each option
- Benefits/drawbacks for each
- Trade-offs analysis (cost, timeline, risk, scalability, etc.)
- Comparison matrix
- Evidence-based recommendation with confidence score
- Next steps for selected option

**Supporting Documents:**
- 3 detailed architecture designs (1 per option)
- 9 architecture diagrams
- Trade-offs analysis
- Cost comparison
- Migration strategy for recommended option

---

#### Next Steps:

```bash
# Option A: Proceed with recommended option
/winston *create-architecture --option moderate --requirements "Scale to 50K users + real-time"

# Option B: Get detailed migration plan
/alex *breakdown-epic "Modernization - Option B Implementation"

# Option C: Interactive consultation
/winston-consult "I want to proceed with Option B, what's the risk mitigation strategy?"
```

---

## End-to-End Workflows

### 13. Complete Feature Delivery (Automated)

**Goal:** Fully automated feature delivery from requirement to pull request

**When to Use:**
- Want complete automation
- Have clear requirement
- Trust workflow orchestration

**Duration:** 30-120 minutes (depending on complexity)

**Complexity:** Variable (score: 35-75)

---

#### Steps:

**Single Command:**

```bash
/orchestrator *workflow feature-delivery "Add user profile page with avatar upload and bio editing"
```

**What Happens:**

[Full workflow execution with all 4 phases as shown in previous examples]

---

#### Expected Output:

**Complete Deliverables:**
- Task specification (.claude/tasks/)
- Implementation (src/)
- Tests (tests/)
- Quality review (.claude/quality/)
- Pull request (GitHub)
- Telemetry (.claude/telemetry/)

---

#### Next Steps:

Review PR and merge when approved.

---

### 14. Brownfield System Modernization

**Goal:** Complete modernization workflow from analysis to implementation plan

**When to Use:**
- Modernizing existing system
- Need comprehensive approach
- Want interactive decision-making

**Duration:** 41-63 minutes (full) or 18-25 minutes (quick)

**Complexity:** Standard (score: 49)

---

#### Steps:

**Interactive Workflow:**

```bash
/orchestrator *workflow modernize . "Scale to 100K users and add real-time features"
```

[Full interactive workflow with 5 phases and user decision point as shown in orchestrator examples]

---

#### Expected Output:

**Generated Documents (5 total):**
- Architecture analysis (production readiness score)
- Brownfield PRD (current features documented)
- Architecture comparison (3 options)
- Detailed architecture (selected option)
- Implementation plan (epic breakdown)

---

#### Next Steps:

```bash
# Start implementation
/alex *breakdown-epic .claude/epics/modernization-plan.md
/alex *plan-sprint --velocity 25
/james *implement task-modernization-001
```

---

### 15. Sprint Execution with Daily Automation

**Goal:** Execute complete 2-week sprint with automated daily coordination

**When to Use:**
- Running formal sprints
- Want automated progress tracking
- Need daily standup automation

**Duration:** 2 weeks (with automated checkpoints)

**Complexity:** Complex (score: 60-80)

---

#### Steps:

**Sprint Kickoff:**

```bash
/orchestrator *workflow sprint-execution "Sprint 15" --velocity 40 --daily-standups=true
```

[Full sprint execution with daily loops as shown in orchestrator examples]

---

#### Expected Output:

**Sprint Artifacts:**
- Sprint plan
- Daily progress reports
- Sprint review document
- Sprint retrospective
- Burndown data
- Velocity tracking

---

#### Next Steps:

Review sprint retrospective and apply learnings to next sprint.

---

## Summary

This workflow guide provides 15 detailed scenarios covering:
- **Planning:** Task specs, epic breakdown, sprint planning
- **Development:** TDD implementation, bug fixes, refactoring
- **Quality:** Review cycles, NFR assessment, risk analysis
- **Architecture:** Analysis, design, comparison
- **End-to-End:** Complete automation for complex workflows

Each workflow includes:
- Clear goal and use case
- Step-by-step instructions with commands
- Expected outputs and durations
- Next steps and related workflows

For additional examples, see:
- [Example Workflows](./EXAMPLE-WORKFLOWS.md) - 11 copy-paste workflows
- [Quick Start Guide](./QUICK-START.md) - Getting started
- [User Guide](./USER-GUIDE.md) - Comprehensive reference

---

**BMAD Enhanced Workflow Guide**
*Version 2.0 | Last Updated: 2025-11-05*
