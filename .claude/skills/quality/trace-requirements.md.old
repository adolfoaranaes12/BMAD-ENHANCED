# Skill: Requirements Traceability Analysis

## Metadata

**Skill Name:** trace-requirements
**Version:** 1.0
**Category:** Quality
**Purpose:** Create comprehensive requirements traceability matrix mapping acceptance criteria → implementation → tests with gap analysis and coverage assessment
**Output:** `.claude/quality/assessments/{task-id}-trace-{YYYYMMDD}.md`

---

## Overview

This skill performs **bidirectional requirements traceability analysis** to ensure every acceptance criterion is implemented and tested. It creates an audit-ready traceability matrix showing the complete chain from requirements through implementation to test validation.

**Key Capabilities:**
- Forward traceability: AC → Implementation → Tests
- Backward traceability: Tests → Implementation → AC
- Gap identification with severity ratings (Critical, High, Medium, Low)
- Coverage percentage calculations (implementation coverage, test coverage)
- Evidence-based verification with file/line references
- Integration with risk-profile and test-design outputs
- Audit-ready documentation for compliance

**When to Use:**
- During implementation review to verify all requirements are addressed
- Before quality gate to ensure completeness
- During audit preparation to demonstrate traceability
- After test-design to map tests to requirements
- When coverage gaps need identification and prioritization

**Integration Points:**
- Reads task specification for acceptance criteria
- Reads risk profile for risk-informed gap severity
- Reads test design for test-to-requirement mapping
- Reads actual implementation files for evidence
- Reads test files for test coverage verification

---

## Execution Process

This skill executes **sequentially** through 7 steps. Each step must complete successfully before proceeding to the next. If any halt condition is met, execution stops and the user is informed.

### Halt Conditions
- Task specification file not found or invalid
- No acceptance criteria defined in task
- Cannot read implementation files referenced in task
- Output directory not writable
- Critical gaps identified with no mitigation plan (advisory only, does not halt)

---

## Step 0: Load Configuration and Context

**Purpose:** Load project configuration and all necessary context for traceability analysis.

**Actions:**

1. **Load Project Configuration**
   ```yaml
   # Read .claude/config.yaml
   quality:
     qualityLocation: .claude/quality  # Where to output trace report
     riskScoreThreshold: 6              # For gap severity assessment
   ```

2. **Load Task Specification**
   ```bash
   # Read task file from argument or prompt user
   TASK_FILE=".claude/tasks/{task-id}-{slug}.md"
   ```
   Extract:
   - Task ID, title, type
   - Objective and context
   - **Acceptance Criteria** (primary traceability source)
   - Implementation Record section
   - Quality Review section (if exists)

3. **Load Related Assessments** (if available)
   ```bash
   # Optional: Enhances analysis but not required
   RISK_FILE=".claude/quality/assessments/{task-id}-risk-{date}.md"
   TEST_FILE=".claude/quality/assessments/{task-id}-test-design-{date}.md"
   ```
   - Risk profile: For gap severity assessment (high-risk gaps = higher severity)
   - Test design: For test-to-requirement mapping

4. **Identify Implementation Files**
   From task spec "Implementation Record" section:
   - Files created/modified during implementation
   - Line ranges for each change
   - Component/module structure

5. **Prepare Output**
   ```bash
   OUTPUT_DIR="{qualityLocation}/assessments"
   OUTPUT_FILE="{task-id}-trace-{YYYYMMDD}.md"
   TEMPLATE=".claude/templates/trace-requirements.md"
   ```

**Halt If:**
- Config file missing or invalid
- Task file not found
- Task has no acceptance criteria
- Cannot create output directory

**Output:**
```
✓ Configuration loaded from .claude/config.yaml
✓ Task specification loaded: {task-id} - {title}
✓ Acceptance Criteria: {count} criteria identified
✓ Related assessments: Risk profile [{found/not found}], Test design [{found/not found}]
✓ Implementation files: {count} files identified
✓ Output: {output-file}
```

---

## Step 1: Build Forward Traceability Matrix (AC → Implementation)

**Purpose:** Map each acceptance criterion to its implementation evidence.

**Actions:**

1. **For Each Acceptance Criterion:**
   ```markdown
   # From task spec
   AC-1: User can sign up with email and password
   AC-2: Password must be at least 8 characters
   AC-3: Email must be validated before account activation
   ```

2. **Search Implementation Files for Evidence:**
   - Read each file from Implementation Record
   - Search for relevant code implementing the AC
   - Record file paths, line ranges, function names
   - Extract code snippets as evidence (5-10 lines context)

3. **Classify Implementation Status:**
   - ✅ **Implemented**: Clear evidence found in code
   - ⚠️ **Partial**: Some evidence but incomplete (e.g., validation missing)
   - ❌ **Not Implemented**: No evidence found
   - ❓ **Unclear**: Code exists but unclear if it satisfies AC

4. **Record Evidence:**
   ```markdown
   AC-1: User can sign up with email and password
   Status: ✅ Implemented
   Evidence:
     - File: src/routes/auth/signup.ts:15-42
       Function: handleSignup()
       Snippet:
         ```typescript
         export async function handleSignup(req: Request, res: Response) {
           const { email, password } = req.body;
           const hashedPassword = await bcrypt.hash(password, 10);
           const user = await prisma.user.create({
             data: { email, password: hashedPassword, emailVerified: false }
           });
           await sendVerificationEmail(user.email);
           return res.status(201).json({ user, token: generateJWT(user) });
         }
         ```
   ```

5. **Calculate Implementation Coverage:**
   ```
   Implementation Coverage = (Implemented + Partial) / Total AC × 100%
   ```

**Output Data Structure:**
```typescript
interface TraceabilityEntry {
  criterionId: string;           // "AC-1"
  criterionText: string;          // "User can sign up..."
  implementationStatus: 'Implemented' | 'Partial' | 'Not Implemented' | 'Unclear';
  evidence: {
    file: string;                 // "src/routes/auth/signup.ts"
    lines: string;                // "15-42"
    function?: string;            // "handleSignup()"
    snippet: string;              // Code excerpt
    description: string;          // How this implements the AC
  }[];
  notes?: string;                 // Any clarifications
}
```

**Halt If:**
- Cannot read implementation files
- More than 50% of ACs have "Unclear" status (ambiguous task, needs clarification)

**Output:**
```
✓ Forward traceability analysis complete
✓ Total Acceptance Criteria: {count}
✓ Implemented: {count} ({percentage}%)
✓ Partial: {count} ({percentage}%)
✓ Not Implemented: {count} ({percentage}%)
✓ Unclear: {count} ({percentage}%)
✓ Implementation Coverage: {percentage}%
```

---

## Step 2: Build Backward Traceability Matrix (Tests → AC)

**Purpose:** Map each test to the acceptance criteria it validates.

**Actions:**

1. **Identify Test Files:**
   - From test-design assessment (if available)
   - From Implementation Record (test files created)
   - From convention: `**/*.test.ts`, `**/*.spec.ts`, `**/__tests__/*`

2. **For Each Test File, Extract Test Cases:**
   ```typescript
   // Read test file: src/routes/auth/__tests__/signup.test.ts
   describe('POST /api/auth/signup', () => {
     it('should create user with valid email and password', async () => {
       // Test case 1
     });

     it('should reject password shorter than 8 characters', async () => {
       // Test case 2
     });

     it('should send verification email', async () => {
       // Test case 3
     });
   });
   ```

3. **Map Tests to Acceptance Criteria:**
   - Analyze test name and assertions
   - Determine which AC(s) the test validates
   - A single test can validate multiple ACs
   - An AC typically has multiple tests (happy path, edge cases, errors)

   ```markdown
   Test: "should create user with valid email and password"
   Validates: AC-1 (User can sign up with email and password)
   File: src/routes/auth/__tests__/signup.test.ts:12-24
   Type: Integration, Priority: P0

   Test: "should reject password shorter than 8 characters"
   Validates: AC-2 (Password must be at least 8 characters)
   File: src/routes/auth/__tests__/signup.test.ts:26-35
   Type: Unit, Priority: P0

   Test: "should send verification email"
   Validates: AC-3 (Email must be validated before account activation)
   File: src/routes/auth/__tests__/signup.test.ts:37-48
   Type: Integration, Priority: P1
   ```

4. **Classify Test Coverage:**
   - ✅ **Tested**: AC has at least one test validating it
   - ⚠️ **Partial**: AC has tests but not all scenarios covered (e.g., only happy path)
   - ❌ **Not Tested**: AC has no tests
   - 🔄 **Indirect**: AC tested indirectly through E2E or other tests

5. **Calculate Test Coverage:**
   ```
   Test Coverage = (Tested + Partial) / Total AC × 100%
   ```

**Output Data Structure:**
```typescript
interface TestTraceability {
  criterionId: string;           // "AC-1"
  testCoverage: 'Tested' | 'Partial' | 'Not Tested' | 'Indirect';
  tests: {
    name: string;                // "should create user with..."
    file: string;                // "src/routes/auth/__tests__/signup.test.ts"
    lines: string;               // "12-24"
    type: 'Unit' | 'Integration' | 'E2E';
    priority: 'P0' | 'P1' | 'P2';
    scenario: string;            // "Given valid inputs, When signup called, Then user created"
  }[];
  missingScenarios?: string[];   // ["Error case: duplicate email", "Edge case: special chars in email"]
}
```

**Output:**
```
✓ Backward traceability analysis complete
✓ Total Tests: {count}
✓ Tested ACs: {count} ({percentage}%)
✓ Partial Test Coverage: {count} ({percentage}%)
✓ Not Tested: {count} ({percentage}%)
✓ Test Coverage: {percentage}%
```

---

## Step 3: Identify Coverage Gaps

**Purpose:** Identify and classify gaps in implementation and test coverage with severity ratings.

**Actions:**

1. **Identify Implementation Gaps:**
   ```markdown
   Implementation Gap 1:
   - AC-4: "System must rate-limit login attempts to 5 per minute"
   - Status: Not Implemented
   - Severity: HIGH (security requirement, high risk if missing)
   - Impact: Brute force attacks possible
   - Required Action: Implement rate limiting middleware
   ```

2. **Identify Test Gaps:**
   ```markdown
   Test Gap 1:
   - AC-2: "Password must be at least 8 characters"
   - Implementation: ✅ Implemented (validation in src/validators/auth.ts:23)
   - Test Coverage: ⚠️ Partial
   - Missing Scenarios:
     * Edge case: Password exactly 8 characters (boundary test)
     * Error case: Password with 7 characters (validation error)
     * Edge case: Password with special characters (acceptance)
   - Severity: MEDIUM (core validation, but implementation exists)
   - Required Action: Add missing test scenarios
   ```

3. **Classify Gap Severity:**
   Use risk profile (if available) to inform severity:

   - **CRITICAL** (Score 9):
     - Security requirement not implemented or tested
     - Data integrity requirement missing
     - Core functionality not implemented
     - High-risk area (from risk profile) not tested

   - **HIGH** (Score 6-8):
     - Important requirement not implemented
     - Security test missing (but implementation exists)
     - Performance requirement not validated
     - P0 test missing

   - **MEDIUM** (Score 3-5):
     - Minor requirement not implemented
     - Edge case test missing
     - P1 test missing
     - Partial implementation without full test coverage

   - **LOW** (Score 1-2):
     - Nice-to-have requirement missing
     - P2 test missing
     - Documentation-only gap

4. **Calculate Gap Metrics:**
   ```
   Total Gaps = Implementation Gaps + Test Gaps
   Critical Gaps = Gaps with severity CRITICAL
   High Gaps = Gaps with severity HIGH
   Medium Gaps = Gaps with severity MEDIUM
   Low Gaps = Gaps with severity LOW

   Gap Coverage = (Total AC - Total Gaps) / Total AC × 100%
   ```

5. **Cross-Reference with Risk Profile:**
   If risk profile exists:
   - Gaps in high-risk areas → Increase severity
   - Gaps with existing mitigation → Decrease severity
   - Gaps without test coverage for high-risk area → CRITICAL

**Output Data Structure:**
```typescript
interface CoverageGap {
  gapId: string;                 // "GAP-1"
  type: 'Implementation' | 'Test';
  criterionId: string;           // "AC-4"
  criterionText: string;         // "System must rate-limit..."
  severity: 'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW';
  severityScore: number;         // 1-9
  impact: string;                // "Brute force attacks possible"
  requiredAction: string;        // "Implement rate limiting middleware"
  missingScenarios?: string[];   // For test gaps
  relatedRisk?: string;          // "Risk #3: Brute force attacks (Score: 8)"
  effort: 'Small' | 'Medium' | 'Large';  // Estimated effort to close gap
  priority: 'P0' | 'P1' | 'P2';  // When to address
}
```

**Halt If:**
- More than 50% implementation gaps (incomplete implementation, not ready for traceability)

**Output:**
```
⚠ Coverage gaps identified
⚠ Total Gaps: {count}
⚠ Critical: {count} (Security/core functionality issues)
⚠ High: {count} (Important requirements missing)
⚠ Medium: {count} (Minor gaps, edge cases)
⚠ Low: {count} (Nice-to-have items)
⚠ Gap Coverage: {percentage}%
```

---

## Step 4: Create Traceability Matrix

**Purpose:** Build comprehensive bidirectional traceability matrix combining all data.

**Actions:**

1. **Build Full Traceability Matrix:**
   ```markdown
   | AC | Requirement | Implementation | Tests | Gaps | Status |
   |----|-------------|----------------|-------|------|--------|
   | AC-1 | User can sign up with email and password | ✅ signup.ts:15-42 | ✅ 3 tests (P0) | None | ✅ Complete |
   | AC-2 | Password must be at least 8 characters | ✅ validators/auth.ts:23 | ⚠️ 1 test (missing edge cases) | GAP-2 (MEDIUM) | ⚠️ Partial |
   | AC-3 | Email must be validated | ✅ signup.ts:40, email.ts:12 | ✅ 2 tests (P1) | None | ✅ Complete |
   | AC-4 | Rate-limit login attempts | ❌ Not implemented | ❌ No tests | GAP-1 (HIGH) | ❌ Incomplete |
   ```

2. **Generate Detailed Entries:**
   For each AC, create detailed traceability entry:

   ```markdown
   ## AC-1: User can sign up with email and password

   **Implementation Status:** ✅ Implemented

   **Implementation Evidence:**
   - **File:** src/routes/auth/signup.ts:15-42
   - **Function:** handleSignup()
   - **Description:** Implements signup endpoint accepting email and password, hashing password with bcrypt, creating user in database, and sending verification email
   - **Code Snippet:**
     ```typescript
     export async function handleSignup(req: Request, res: Response) {
       const { email, password } = req.body;
       const hashedPassword = await bcrypt.hash(password, 10);
       const user = await prisma.user.create({
         data: { email, password: hashedPassword, emailVerified: false }
       });
       await sendVerificationEmail(user.email);
       return res.status(201).json({ user, token: generateJWT(user) });
     }
     ```

   **Test Coverage:** ✅ Tested

   **Test Evidence:**
   1. **Test:** "should create user with valid email and password"
      - **File:** src/routes/auth/__tests__/signup.test.ts:12-24
      - **Type:** Integration, Priority: P0
      - **Scenario:** Given valid email and password, When POST /api/auth/signup, Then user created and JWT returned

   2. **Test:** "should return 400 for invalid email format"
      - **File:** src/routes/auth/__tests__/signup.test.ts:26-35
      - **Type:** Integration, Priority: P0
      - **Scenario:** Given invalid email, When POST /api/auth/signup, Then 400 error returned

   3. **Test:** "should return 409 for duplicate email"
      - **File:** src/routes/auth/__tests__/signup.test.ts:37-48
      - **Type:** Integration, Priority: P1
      - **Scenario:** Given existing user email, When POST /api/auth/signup, Then 409 conflict returned

   **Coverage Status:** ✅ Complete
   - Implementation: ✅ Complete
   - Tests: ✅ Complete (3 tests covering happy path, validation, and error cases)
   - Gaps: None

   ---
   ```

3. **Generate Gap Details:**
   For each gap, create detailed entry:

   ```markdown
   ## GAP-1: Rate Limiting Not Implemented (HIGH)

   **Type:** Implementation Gap
   **Severity:** HIGH (Score: 7)
   **Criterion:** AC-4 - "System must rate-limit login attempts to 5 per minute"

   **Impact:**
   - Brute force attacks possible on login endpoint
   - Potential account takeover vulnerability
   - No protection against credential stuffing

   **Related Risk:** Risk #3 from risk profile: "Brute force attacks" (Score: 8)

   **Required Action:**
   1. Implement rate limiting middleware using express-rate-limit or similar
   2. Configure limit: 5 requests per minute per IP
   3. Apply to /api/auth/login endpoint
   4. Add tests for rate limiting behavior

   **Effort:** Medium (2-4 hours)
   **Priority:** P0 (Must fix before merge - security issue)

   **Recommended Implementation:**
   ```typescript
   // src/middleware/rateLimit.ts
   import rateLimit from 'express-rate-limit';

   export const loginLimiter = rateLimit({
     windowMs: 60 * 1000,  // 1 minute
     max: 5,               // 5 requests per window
     message: 'Too many login attempts, please try again later',
     standardHeaders: true,
     legacyHeaders: false,
   });
   ```

   **Recommended Tests:**
   - Test: 5 attempts succeed, 6th attempt fails with 429
   - Test: Rate limit resets after 1 minute
   - Test: Rate limit is per-IP (different IPs have separate limits)

   ---
   ```

4. **Calculate Overall Traceability Score:**
   ```
   Traceability Score = (
     (Implementation Coverage × 0.5) +
     (Test Coverage × 0.4) +
     (Gap Coverage × 0.1)
   )

   Example:
   - Implementation Coverage: 85%
   - Test Coverage: 80%
   - Gap Coverage: 90% (10% gaps)

   Traceability Score = (85 × 0.5) + (80 × 0.4) + (90 × 0.1)
                      = 42.5 + 32 + 9
                      = 83.5%
   ```

**Output:**
```
✓ Traceability matrix complete
✓ Total Entries: {count} acceptance criteria
✓ Complete: {count} ({percentage}%)
✓ Partial: {count} ({percentage}%)
✓ Incomplete: {count} ({percentage}%)
✓ Overall Traceability Score: {percentage}%
```

---

## Step 5: Generate Recommendations

**Purpose:** Provide actionable recommendations for closing gaps and improving traceability.

**Actions:**

1. **Prioritize Gaps:**
   Sort gaps by:
   1. Severity (CRITICAL → HIGH → MEDIUM → LOW)
   2. Priority (P0 → P1 → P2)
   3. Effort (Small → Medium → Large)

2. **Generate Action Plan:**
   ```markdown
   ## Immediate Actions (Before Merge - P0)

   1. **[GAP-1] Implement Rate Limiting (HIGH)**
      - Impact: Security vulnerability
      - Effort: Medium (2-4 hours)
      - Action: Add rate limiting middleware to /api/auth/login
      - Tests: Add 3 tests for rate limit behavior

   2. **[GAP-4] Add Input Sanitization Tests (CRITICAL)**
      - Impact: XSS vulnerability untested
      - Effort: Small (1-2 hours)
      - Action: Implementation exists, add tests for XSS/SQL injection attempts
      - Tests: Add 5 tests for malicious inputs

   ## Short-Term Actions (Before Release - P1)

   3. **[GAP-2] Complete Password Validation Tests (MEDIUM)**
      - Impact: Edge cases not validated
      - Effort: Small (30 min - 1 hour)
      - Action: Add boundary and edge case tests
      - Tests: Add 2 tests (exactly 8 chars, special characters)

   ## Long-Term Actions (Future Enhancement - P2)

   4. **[GAP-7] Add Email Bounce Handling (LOW)**
      - Impact: Nice-to-have feature
      - Effort: Large (1-2 days)
      - Action: Implement email bounce webhook
      - Tests: Add integration tests for bounce handling
   ```

3. **Quality Gate Impact:**
   ```markdown
   ## Impact on Quality Gate

   **Current Status:** CONCERNS

   **Reasoning:**
   - 2 HIGH-severity gaps (GAP-1, GAP-3) present security risks
   - 1 CRITICAL gap (GAP-4) has untested security implementation
   - Implementation coverage at 85% (above threshold)
   - Test coverage at 80% (above threshold)
   - But gaps in critical security areas

   **To Achieve PASS:**
   1. Close all CRITICAL gaps (GAP-4)
   2. Close all HIGH gaps (GAP-1, GAP-3) OR provide waiver with mitigation
   3. Achieve implementation coverage ≥90%
   4. Achieve test coverage ≥85%

   **Estimated Effort to PASS:** 4-6 hours (close GAP-1, GAP-3, GAP-4)
   ```

4. **Best Practices:**
   ```markdown
   ## Traceability Best Practices

   **For Future Tasks:**
   1. Write tests alongside implementation (TDD approach)
   2. Reference AC IDs in commit messages ("Implements AC-1, AC-3")
   3. Reference AC IDs in test names ("test should satisfy AC-2")
   4. Update traceability matrix as you implement
   5. Run trace-requirements skill before marking task as "Review"

   **For This Task:**
   1. Close P0 gaps before requesting review
   2. Document any waived gaps with rationale
   3. Update Implementation Record with gap closure evidence
   4. Re-run trace-requirements after closing gaps
   ```

**Output:**
```
✓ Recommendations generated
✓ P0 Actions: {count} (must complete before merge)
✓ P1 Actions: {count} (should complete before release)
✓ P2 Actions: {count} (future enhancements)
✓ Estimated Effort to Close P0 Gaps: {hours} hours
✓ Quality Gate Prediction: {PASS/CONCERNS/FAIL}
```

---

## Step 6: Generate Traceability Report

**Purpose:** Create comprehensive traceability report using template.

**Actions:**

1. **Load Template:**
   ```bash
   TEMPLATE=".claude/templates/trace-requirements.md"
   ```

2. **Populate Template Variables:**
   Replace all template variables with computed data:

   ```markdown
   # From Step 0
   {{TASK_ID}} → "task-007"
   {{TASK_TITLE}} → "User Authentication API"
   {{DATE}} → "2025-10-28"
   {{ASSESSOR}} → "Claude (Sonnet 4.5)"

   # From Step 1
   {{TOTAL_AC}} → "6"
   {{IMPLEMENTED_COUNT}} → "5"
   {{PARTIAL_COUNT}} → "0"
   {{NOT_IMPLEMENTED_COUNT}} → "1"
   {{IMPLEMENTATION_COVERAGE}} → "83%"

   # From Step 2
   {{TOTAL_TESTS}} → "12"
   {{TESTED_COUNT}} → "5"
   {{PARTIAL_TEST_COUNT}} → "1"
   {{NOT_TESTED_COUNT}} → "0"
   {{TEST_COVERAGE}} → "100%"

   # From Step 3
   {{TOTAL_GAPS}} → "4"
   {{CRITICAL_GAPS}} → "1"
   {{HIGH_GAPS}} → "2"
   {{MEDIUM_GAPS}} → "1"
   {{LOW_GAPS}} → "0"
   {{GAP_COVERAGE}} → "93%"

   # From Step 4
   {{TRACEABILITY_SCORE}} → "83.5%"
   {{TRACEABILITY_MATRIX_ROWS}} → [detailed matrix data]
   {{DETAILED_ENTRIES}} → [full traceability entries]

   # From Step 5
   {{RECOMMENDATIONS}} → [action plan]
   {{QUALITY_GATE_IMPACT}} → "CONCERNS"
   {{QUALITY_GATE_REASONING}} → "..."
   ```

3. **Generate Full Report:**
   Write to output file with all sections populated.

4. **Validate Report:**
   - All template variables replaced
   - No placeholder text remaining
   - All file references valid
   - All code snippets formatted correctly

**Output File Structure:**
```markdown
# Requirements Traceability Matrix: {task-title}

## Summary
- Total AC: 6
- Implementation Coverage: 83%
- Test Coverage: 100%
- Traceability Score: 83.5%
- Gaps: 4 (1 CRITICAL, 2 HIGH, 1 MEDIUM)

## Traceability Matrix
[Matrix table]

## Detailed Traceability Entries
[Full entries for each AC]

## Coverage Gaps
[Detailed gap analysis]

## Recommendations
[Action plan]

## Quality Gate Impact
[Gate prediction]
```

**Output:**
```
✓ Traceability report generated
✓ Output: .claude/quality/assessments/{task-id}-trace-{date}.md
✓ Report size: {lines} lines
✓ Validation: PASSED
```

---

## Step 7: Present Summary to User

**Purpose:** Provide concise summary with key metrics and next steps.

**Actions:**

1. **Display Summary:**
   ```
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   Requirements Traceability Analysis Complete
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   Task: task-007 - User Authentication API
   Date: 2025-10-28

   📊 Coverage Metrics:
   ├─ Implementation Coverage: 83% (5/6 AC implemented)
   ├─ Test Coverage: 100% (6/6 AC tested)
   ├─ Gap Coverage: 93% (4 gaps identified)
   └─ Overall Traceability Score: 83.5%

   ⚠️  Coverage Gaps Identified:
   ├─ CRITICAL: 1 gap (untested security implementation)
   ├─ HIGH: 2 gaps (missing security features)
   ├─ MEDIUM: 1 gap (incomplete test scenarios)
   └─ LOW: 0 gaps

   🎯 Quality Gate Impact: CONCERNS

   Reasoning:
   - 2 HIGH-severity gaps present security risks
   - 1 CRITICAL gap has untested security implementation
   - Implementation and test coverage above thresholds
   - But critical gaps in security areas require attention

   ✅ To Achieve PASS:
   1. Close GAP-4 (CRITICAL): Add XSS/injection tests [1-2h]
   2. Close GAP-1 (HIGH): Implement rate limiting [2-4h]
   3. Close GAP-3 (HIGH): Add session management [3-5h]

   Estimated effort: 6-11 hours

   📄 Full Report:
   .claude/quality/assessments/task-007-trace-20251028.md

   💡 Next Steps:
   1. Review detailed traceability matrix in report
   2. Prioritize P0 gaps (before merge)
   3. Close critical and high-severity gaps
   4. Re-run trace analysis after closing gaps
   5. Update task file Implementation Record with gap closure

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   ```

2. **Ask User:**
   ```
   Would you like me to:
   A) Show details of specific gaps
   B) Generate implementation plan for closing gaps
   C) Re-run analysis after you close gaps
   D) Continue with next skill (nfr-assess or quality-gate)
   ```

**Execution Complete.**

---

## Integration with Other Skills

### Integration with risk-profile.md

**Input from risk-profile:**
- Risk scores for each risk area
- High-risk areas (score ≥6) requiring extra test coverage
- Mitigation strategies that may be implemented

**How traceability uses it:**
- Gaps in high-risk areas → Increase gap severity
- Missing tests for high-risk areas → CRITICAL severity
- Risk mitigation → Cross-reference with implementation evidence

**Example:**
```markdown
Risk Profile says:
  Risk #3: Brute force attacks (Score: 8, HIGH)
  Mitigation: Implement rate limiting

Traceability Analysis finds:
  AC-4: "Rate-limit login attempts" → Not Implemented

Gap Severity Calculation:
  Base severity: HIGH (security requirement)
  Risk amplification: +1 (high-risk area from risk profile)
  Final severity: CRITICAL (Score: 9)
```

### Integration with test-design.md

**Input from test-design:**
- Test scenarios with priorities (P0, P1, P2)
- Test files and locations
- Mock strategies
- CI/CD integration plan

**How traceability uses it:**
- Maps test scenarios to acceptance criteria
- Validates all P0 tests have corresponding AC
- Identifies test scenarios not linked to any AC (over-testing)
- Validates coverage matches test design plan

**Example:**
```markdown
Test Design says:
  Scenario 1: Valid signup (P0, Integration)
  - Validates: User can sign up with email and password
  - File: src/routes/auth/__tests__/signup.test.ts

Traceability confirms:
  AC-1: "User can sign up..." → ✅ Tested
  - Test: "should create user with valid email and password"
  - File: src/routes/auth/__tests__/signup.test.ts:12-24
  - Priority: P0 ✓ (matches test design)
```

### Integration with quality-gate.md

**Output to quality-gate:**
- Traceability score (contributes to gate decision)
- Coverage gaps (may block gate if critical)
- Action items for closing gaps
- Evidence for requirements traceability section

**How quality-gate uses it:**
```markdown
Quality Gate Decision Process:
1. Check traceability score:
   - Score ≥95% → PASS (excellent traceability)
   - Score 80-94% → CONCERNS (good but has gaps)
   - Score <80% → FAIL (poor traceability)

2. Check critical gaps:
   - 0 critical gaps → continue evaluation
   - 1+ critical gaps → CONCERNS (or FAIL if security)

3. Check overall coverage:
   - Implementation ≥90% AND Test ≥85% → PASS
   - Implementation ≥80% OR Test ≥70% → CONCERNS
   - Implementation <80% OR Test <70% → FAIL
```

---

## Output Template Reference

The skill uses `.claude/templates/trace-requirements.md` for report generation. The template includes:

**Sections:**
1. **Header**: Task metadata, assessment date, assessor
2. **Summary**: Quick metrics (coverage percentages, gap counts)
3. **Traceability Matrix**: Table showing AC → Implementation → Tests → Gaps
4. **Detailed Traceability Entries**: Full evidence for each AC
5. **Coverage Gaps**: Detailed gap analysis with severity and actions
6. **Recommendations**: Prioritized action plan
7. **Quality Gate Impact**: Predicted gate status and reasoning
8. **Appendices**: Test inventory, file inventory, risk cross-reference

**Template Variables:**
- Metadata: `{{TASK_ID}}`, `{{TASK_TITLE}}`, `{{DATE}}`, `{{ASSESSOR}}`
- Metrics: `{{IMPLEMENTATION_COVERAGE}}`, `{{TEST_COVERAGE}}`, `{{TRACEABILITY_SCORE}}`
- Counts: `{{TOTAL_AC}}`, `{{TOTAL_GAPS}}`, `{{CRITICAL_GAPS}}`, etc.
- Data: `{{TRACEABILITY_MATRIX_ROWS}}`, `{{DETAILED_ENTRIES}}`, `{{GAP_DETAILS}}`

---

## Best Practices

### For Task Implementers:
1. **Reference AC IDs in code comments:**
   ```typescript
   // Implements AC-1: User signup with email and password
   export async function handleSignup(req: Request, res: Response) {
     // ...
   }
   ```

2. **Reference AC IDs in commit messages:**
   ```bash
   git commit -m "feat: implement user signup (AC-1, AC-2, AC-3)"
   ```

3. **Reference AC IDs in test names:**
   ```typescript
   it('should satisfy AC-1: user can sign up with email and password', async () => {
     // ...
   });
   ```

4. **Run traceability analysis before marking task as "Review":**
   ```bash
   # Before changing task status to "Review"
   Check traceability → Close gaps → Re-run traceability → Mark "Review"
   ```

### For Reviewers:
1. **Start review with traceability report:**
   - Verify all AC implemented and tested
   - Check gap severity and mitigation plans
   - Validate evidence quality

2. **Cross-reference with risk profile:**
   - Ensure high-risk areas fully tested
   - Verify mitigation strategies implemented

3. **Use traceability for audit trail:**
   - Demonstrate requirements → implementation → test chain
   - Show evidence for compliance

---

## Error Handling

### Common Errors:

1. **Task file not found:**
   ```
   ERROR: Task file not found at {path}

   Action: Verify task ID and file location
   ```

2. **No acceptance criteria in task:**
   ```
   ERROR: Task has no acceptance criteria defined

   Action: Task must have "Acceptance Criteria" section with at least one AC
   ```

3. **Cannot read implementation files:**
   ```
   ERROR: Cannot read implementation file: {file}

   Action: Verify file exists and is readable. Check Implementation Record section.
   ```

4. **Too many unclear mappings:**
   ```
   HALT: More than 50% of ACs have "Unclear" implementation status

   Action: Task is ambiguous. Clarify requirements and implementation before traceability analysis.
   ```

5. **Output directory not writable:**
   ```
   ERROR: Cannot write to {output-dir}

   Action: Check directory permissions or create directory
   ```

---

## Skill Complete

This skill is now ready for use. To execute:

1. **Direct invocation** (when subagents built):
   ```
   @quinn *trace task-007
   ```

2. **Manual invocation** (current):
   ```
   I'd like to run requirements traceability analysis on task-007
   ```

The skill will execute all 7 steps sequentially and generate a comprehensive traceability report.

---

## Version History

**Version 1.0** (2025-10-28)
- Initial skill implementation
- 7-step sequential execution
- Bidirectional traceability (forward and backward)
- Gap analysis with severity ratings
- Integration with risk-profile and test-design
- Audit-ready documentation
- Quality gate impact assessment

---

<!-- End of Skill -->
