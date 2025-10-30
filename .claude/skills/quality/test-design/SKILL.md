---
name: test-design
description: Design comprehensive test strategies with risk-informed prioritization (P0/P1/P2), test levels (unit/integration/E2E), mock strategies, and CI/CD integration before implementation
version: 2.0
category: Quality
acceptance:
  all_acs_have_tests: "All acceptance criteria have test scenarios designed with Given-When-Then format, clear pass/fail criteria, and test data specifications"
  priorities_assigned: "All test scenarios assigned priority levels (P0/P1/P2) based on risk scores from risk-profile or AC criticality"
  mock_strategies_developed: "Mock strategies developed for all external dependencies (APIs, databases, services) with implementation guidance"
  cicd_integration_planned: "CI/CD test execution strategy planned with stages (pre-commit, PR, pre-deployment, production), parallelization, and coverage requirements"
telemetry:
  emit: "skill.test-design.completed"
  track:
    - task_id
    - assessment_mode  # pre-implementation | retrospective
    - total_tests
    - p0_tests_count
    - p1_tests_count
    - p2_tests_count
    - unit_tests_count
    - integration_tests_count
    - e2e_tests_count
    - estimated_execution_time_seconds
    - risk_profile_available
---

# Quality Skill: Test Design Strategy

Design comprehensive test strategies **before implementation** using risk-informed prioritization, test level recommendations (unit/integration/E2E), mock strategies for dependencies, and CI/CD integration planning.

## Purpose

Create test design documents that specify:
- **Test scenarios** with Given-When-Then format for all acceptance criteria
- **Test levels** (unit, integration, E2E) based on what's being tested
- **Test priorities** (P0/P1/P2) based on risk scores and criticality
- **Mock strategies** for external dependencies with implementation guidance
- **CI/CD integration** with execution stages and coverage requirements

**Key Innovation (BMAD Pattern):**
- Test design BEFORE implementation guides what tests to write
- Risk-informed prioritization prevents missing critical tests
- Level recommendations optimize test execution speed
- Mock strategies enable effective testing of complex systems

## When to Use This Skill

**Best Used:**
- After task spec creation, before implementation
- After risk profiling (uses risk scores for prioritization)
- For complex features requiring multiple test levels
- When planning test infrastructure for new components

**Can Skip For:**
- Simple bug fixes with obvious test cases (1-2 tests)
- Trivial changes with existing test patterns
- Emergency hotfixes (add test design after stabilization)

**Triggers:**
- User asks to "design tests", "create test strategy", "plan test cases"
- Before implementing complex features (proactively suggest)
- After risk profile completed (natural next step)

## Test Levels

### Unit Tests
**Purpose:** Test individual functions, methods, classes in isolation

**Characteristics:**
- Fast execution (< 50ms each)
- No external dependencies (fully mocked)
- Test business logic, algorithms, validation rules
- High coverage expected (>80%)

**When to use:** Business logic, data transformations, validation rules, utility functions, error handling

### Integration Tests
**Purpose:** Test interactions between components/modules

**Characteristics:**
- Moderate execution time (< 500ms each)
- May use test database, test APIs
- Test component interactions and integration points
- Focus on service boundaries

**When to use:** API endpoints, database operations, service-to-service communication, authentication flows, external API interactions (mocked)

### E2E (End-to-End) Tests
**Purpose:** Test complete user journeys through the system

**Characteristics:**
- Slower execution (seconds per test)
- Use real or near-real environment
- Test critical user workflows end-to-end
- Fewer tests, higher value (focus on critical paths)

**When to use:** Critical user journeys, multi-step workflows, UI + backend integration, business-critical paths, regression prevention

## Test Priority Levels

### P0 (Critical) - Must Have
**Requirements:**
- Tests critical functionality (authentication, payment, data integrity)
- Validates security requirements (injection, XSS, auth bypass)
- Prevents data loss or corruption
- Covers high-risk areas (score ≥6 from risk profile)
- **Must pass before merge** (CI blocks merge if P0 fails)

**Examples:** Authentication/authorization, payment processing, data integrity operations, security vulnerability prevention

### P1 (High) - Should Have
**Requirements:**
- Tests important functionality (core features)
- Covers medium-risk areas (score 3-5)
- Validates key user features
- **Should pass before merge** (exceptions allowed with justification)

**Examples:** Core feature functionality, error handling paths, performance requirements, user experience features

### P2 (Medium) - Nice to Have
**Requirements:**
- Tests edge cases and rare scenarios
- Covers low-risk areas (score 1-2)
- Nice-to-have validations
- **Can defer if time-constrained** (implement after main work)

**Examples:** Rare edge cases, minor UI variations, optional features, future enhancements

## SEQUENTIAL Skill Execution

**CRITICAL:** Do not proceed to next step until current step is complete

### Step 0: Load Configuration and Context

**Purpose:** Load task specification, risk profile, and configuration to understand test requirements

**Actions:**

1. **Load configuration from `.claude/config.yaml`:**
   - Extract test coverage targets (overall, critical paths, new code)
   - Extract test timeout limits
   - Extract quality settings

2. **Get task file path from user:**
   - Example: `.claude/tasks/task-006-user-signup.md`
   - Verify file exists and is readable

3. **Read task specification:**
   - Load objective and acceptance criteria
   - Load context (data models, APIs, components)
   - Load task breakdown

4. **Check for risk profile (optional but recommended):**
   - Look for: `.claude/quality/assessments/{task-id}-risk-*.md`
   - If exists: Load risk scores for prioritization
   - If missing: Can proceed but warn user (recommend running risk-profile first)

**Output:**
- Configuration loaded
- Task context understood
- Risk profile loaded (if available)
- Ready to analyze test requirements

**Halt Conditions:**
- Configuration file missing (cannot proceed)
- Task file missing or unreadable (cannot proceed)

**Reference:** See [test-scenarios.md](references/test-scenarios.md) for test scenario design patterns

---

### Step 1: Analyze Test Requirements

**Purpose:** Identify what needs to be tested for each acceptance criterion

**Actions:**

1. **For each acceptance criterion:**
   - What needs to be validated? (testable outcomes)
   - What are the edge cases? (boundaries, limits)
   - What could go wrong? (error scenarios)
   - What are the security considerations? (injection, auth bypass)

2. **Identify test categories:**
   - **Happy path:** Normal, expected usage (most common scenarios)
   - **Error cases:** Invalid inputs, failures, exceptions
   - **Edge cases:** Boundaries, limits, unusual inputs
   - **Security:** Authentication, authorization, injection, XSS
   - **Performance:** Response time, resource usage, scalability
   - **Integration:** Component interactions, service boundaries

3. **Map to test levels:**
   - What needs unit tests? (Logic, validation, algorithms)
   - What needs integration tests? (API, database, service interactions)
   - What needs E2E tests? (User journeys, critical workflows)

4. **Consider technical constraints:**
   - External dependencies to mock (APIs, payment, email)
   - Database interactions (test DB or mock?)
   - Async operations (promises, callbacks)
   - File I/O (temp directories)
   - Network calls (mock or test endpoints?)

**Output:**
- Test requirements identified per acceptance criterion
- Test categories mapped (happy path, error, edge, security, performance, integration)
- Test levels determined (unit, integration, E2E)
- Technical considerations noted (mocking, dependencies)

**Example:**
```
AC1: User can signup with valid email/password

Test Requirements:
- Valid signup creates user record
- Valid signup returns JWT token
- Valid signup sends confirmation email
- Email format validation
- Password strength validation
- Duplicate email rejection

Test Categories:
- Happy path: Valid email/password signup
- Error cases: Invalid email, weak password, duplicate email
- Edge cases: Unicode emails, very long passwords
- Security: SQL injection attempts, XSS in email
- Integration: Email service interaction, database transaction

Test Levels:
- Unit: Email validation logic, password strength logic
- Integration: POST /api/auth/signup endpoint with test DB
- E2E: Complete signup flow from form to confirmation
```

**Halt Conditions:**
- Acceptance criteria too vague to test (cannot identify testable outcomes)
- Missing context to understand what to test

**Reference:** See [test-scenarios.md](references/test-scenarios.md) for test requirement analysis patterns

---

### Step 2: Design Test Scenarios

**Purpose:** Create specific test scenarios with Given-When-Then format, priorities, and test data

**Actions:**

For each test requirement from Step 1:

1. **Write test scenario description:**
   - Use **Given-When-Then** format for clarity (not BDD code, just format)
   - Specify exact inputs and expected outputs
   - Define clear pass/fail criteria
   - Include test data samples

2. **Assign test level:**
   - Unit, Integration, or E2E
   - Based on what's being tested (logic vs interaction vs journey)

3. **Assign priority (risk-informed):**
   - **P0 if:** Critical functionality, security, high-risk (score ≥6), data integrity
   - **P1 if:** Important functionality, medium-risk (score 3-5), core features
   - **P2 if:** Edge cases, low-risk (score 1-2), optional features

4. **Specify test data requirements:**
   - Valid samples (normal inputs)
   - Invalid samples (error scenarios)
   - Edge case values (boundaries, limits)
   - Security payloads (injection, XSS)

5. **Identify dependencies:**
   - What needs to be mocked? (external APIs, payment, email)
   - What requires real services? (database, file system)
   - What fixtures needed? (test data, mocks)

**Output:**
- Test scenarios with Given-When-Then format
- Test level assigned (unit/integration/E2E)
- Priority assigned (P0/P1/P2) with risk linkage
- Test data specified (valid, invalid, edge, security)
- Dependencies identified (mocks, fixtures)

**Example:**
```markdown
### Scenario 1: Valid User Signup (P0, Integration)

**Given** the API is running and database is empty
**When** POST /api/auth/signup with valid email "user@example.com" and strong password "SecurePass123!"
**Then**
- Response status is 201
- Response body contains user object with email
- Response body contains JWT token
- User record exists in database
- Confirmation email queued

**Test Level:** Integration
**Priority:** P0 (Critical - core functionality)
**Risk:** Linked to AC1 implementation risk (score: 5)
**Test Data:**
- Valid email: user@example.com
- Valid password: SecurePass123! (8+ chars, mixed case, number, special)

**Dependencies:**
- Test database with users table
- Email service mocked (verify queue called)
- JWT secret configured

**File:** src/routes/auth/__tests__/signup.integration.test.ts
```

**Halt Conditions:**
- Cannot define clear pass/fail criteria for scenarios
- Scenarios too ambiguous to implement

**Reference:** See [test-scenarios.md](references/test-scenarios.md) for complete scenario examples

---

### Step 3: Develop Mock Strategies

**Purpose:** Define mocking approach for external dependencies to enable effective testing

**Actions:**

1. **Identify external dependencies:**
   - Third-party APIs (Stripe, SendGrid, etc.)
   - External services (email, payment, SMS, etc.)
   - Database (Postgres, MongoDB, etc.)
   - File system (uploads, logs, temp files)
   - Network resources (HTTP calls, websockets)

2. **For each dependency, decide mocking approach:**

   **Option A: Full Mock**
   - Replace with test double (jest.fn(), sinon stub)
   - Predictable, fast, isolated
   - **Use for:** Third-party APIs, external services

   **Option B: Test Instance**
   - Use real implementation with test data
   - More realistic, slower
   - **Use for:** Database (test DB), file system (temp dirs)

   **Option C: Partial Mock**
   - Real implementation, mock specific parts
   - Balance realism and speed
   - **Use for:** Service with mostly local logic but external call

3. **Specify mock data/fixtures:**
   - What responses to mock? (success, failure, timeout)
   - What fixtures to create? (test data, sample files)
   - What edge cases to simulate? (errors, delays)

4. **Document mock configuration:**
   - How to set up mocks? (jest.mock, setup files)
   - What libraries to use? (jest, sinon, nock)
   - How to verify mock interactions? (expect calls, spy on methods)

**Output:**
- Mock strategy for each dependency (full mock, test instance, partial mock)
- Mock data/fixtures specified (success, failure, edge cases)
- Configuration documented (setup, libraries, verification)

**Example:**
```markdown
## Mock Strategy

### Email Service (Full Mock)

**Approach:** Mock email service to prevent sending real emails during tests

**Implementation:**
```typescript
// tests/setup/mocks/emailService.ts
export const mockEmailService = {
  sendEmail: jest.fn().mockResolvedValue({ messageId: 'test-123' }),
  verifyEmail: jest.fn().mockResolvedValue(true)
};

// In test:
jest.mock('@/services/email', () => mockEmailService);
```

**Mock Data:**
- Success: `{ messageId: 'test-123', status: 'sent' }`
- Failure: `{ error: 'Service unavailable' }`
- Timeout: Delay 5000ms then reject

**Verification:**
```typescript
expect(mockEmailService.sendEmail).toHaveBeenCalledWith({
  to: 'user@example.com',
  subject: 'Confirm your email',
  template: 'confirmation'
});
```

---

### Database (Test Instance)

**Approach:** Use real PostgreSQL with test database (not mocked)

**Why not mock:** Database interactions are integration test targets, real DB catches query bugs

**Implementation:**
```typescript
// tests/setup/database.ts
export const testDb = new PrismaClient({
  datasources: { db: { url: process.env.TEST_DATABASE_URL } }
});

beforeEach(async () => {
  await testDb.user.deleteMany();  // Clean slate
});
```
```

**Halt Conditions:**
- Cannot determine appropriate mock strategy for critical dependency
- Dependency too complex to mock or test

**Reference:** See [mock-strategies.md](references/mock-strategies.md) for complete mock strategy patterns

---

### Step 4: Plan CI/CD Integration

**Purpose:** Define test execution strategy for CI/CD pipeline with stages, parallelization, and coverage

**Actions:**

1. **Define test execution strategy:**
   - When do different test types run? (pre-commit, PR, pre-deploy, production)
   - What's the trigger for each? (git hook, PR event, deployment event)
   - What's the failure policy? (block merge, alert, rollback)

2. **Specify test environments:**
   - Local development (fast feedback)
   - CI pipeline (comprehensive validation)
   - Pre-deployment (staging verification)
   - Production (smoke tests only)

3. **Configure test parallelization:**
   - What can run in parallel? (unit tests - fully parallel)
   - What must run sequentially? (E2E tests - shared state)
   - Resource requirements? (CPU, memory, database)

4. **Define coverage requirements:**
   - Minimum coverage percentage (overall, new code)
   - Critical paths requiring 100% (security, payment, data integrity)
   - Coverage failure policy (block merge, warning)

5. **Plan test data management:**
   - How to seed test data? (global setup, fixtures)
   - How to clean up after tests? (global teardown, beforeEach)
   - How to handle shared resources? (isolated databases per worker)

**Output:**
- Test execution strategy (stages, triggers, failure policy)
- Environment configuration (local, CI, staging, production)
- Parallelization plan (parallel vs sequential, resources)
- Coverage requirements (minimums, critical paths, policy)
- Data management approach (seed, cleanup, isolation)

**Example:**
```markdown
## CI/CD Test Strategy

### Test Execution Stages

**Stage 1: Pre-commit (Local)**
- Trigger: Before git commit
- Tests: Unit tests only
- Duration: < 10 seconds
- Failure: Block commit

**Stage 2: Pull Request (CI)**
- Trigger: On PR creation/update
- Tests: All tests (unit + integration + E2E)
- Duration: < 3 minutes
- Failure: Block merge
- Coverage: Minimum 80% overall, 100% critical paths

**Stage 3: Pre-deployment (Staging)**
- Trigger: Before production deployment
- Tests: E2E + smoke tests on staging
- Duration: < 5 minutes
- Failure: Block deployment

**Stage 4: Post-deployment (Production)**
- Trigger: After production deployment
- Tests: Smoke tests only
- Duration: < 1 minute
- Failure: Alert (manual rollback decision)

---

### Parallelization

**Unit Tests:** Full parallelization (100% workers)
**Integration Tests:** Parallel with isolated databases (4 workers)
**E2E Tests:** Sequential (1 worker, shared browser state)

---

### Coverage Requirements

**Minimum Coverage:**
- Overall: 80% statements, 75% branches
- New code: 90% statements, 85% branches
- Critical paths (auth, payment): 100% (blocks merge if below)
```

**Halt Conditions:**
- Cannot determine appropriate CI/CD strategy for project
- Test environment requirements unclear

**Reference:** See [cicd-integration.md](references/cicd-integration.md) for complete CI/CD integration patterns

---

### Step 5: Calculate Test Summary

**Purpose:** Calculate test counts, priorities, and execution time estimates

**Actions:**

1. **Count tests by level:**
   - Total unit tests
   - Total integration tests
   - Total E2E tests
   - Total all tests

2. **Count tests by priority:**
   - P0 (Critical) - must pass before merge
   - P1 (High) - should pass before merge
   - P2 (Medium) - can defer if needed

3. **Estimate execution time:**
   - Unit: 50ms average × count
   - Integration: 500ms average × count
   - E2E: 5s average × count
   - Total execution time

4. **Calculate expected coverage:**
   - Based on scenarios vs acceptance criteria
   - Critical path coverage (should be 100%)
   - Overall coverage estimate (based on scope)

**Output:**
- Test count summary (by level and priority)
- Priority breakdown (P0/P1/P2 counts)
- Estimated execution time (by level and total)
- Expected coverage (overall and critical paths)

**Example:**
```markdown
## Test Summary

**Total Tests:** 24
- Unit: 15
- Integration: 7
- E2E: 2

**By Priority:**
- P0 (Critical): 8 tests - Must pass before merge
- P1 (High): 10 tests - Should pass before merge
- P2 (Medium): 6 tests - Can defer if needed

**Estimated Execution Time:**
- Unit: 0.75s (15 × 50ms)
- Integration: 3.5s (7 × 500ms)
- E2E: 10s (2 × 5s)
- **Total: 14.25s** (fast test suite)

**Expected Coverage:**
- Overall: ~85-90%
- Critical paths (auth, payment): 100%
- Business logic: 95%
- Error handling: 85%
```

**Halt Conditions:**
- None (calculation always possible from scenario counts)

---

### Step 6: Generate Test Design Document and Present Summary

**Purpose:** Generate complete test design document and present concise summary to user

**Actions:**

1. **Load test design template:**
   - Read `.claude/templates/test-design.md` (if exists)
   - Use default structure if template missing

2. **Populate all sections:**
   - Test summary (from Step 5)
   - Test scenarios by acceptance criterion (from Step 2)
   - Mock strategies (from Step 3)
   - CI/CD integration plan (from Step 4)
   - Risk-test mapping (if risk profile available)

3. **Generate file path:**
   - Format: `.claude/quality/assessments/{taskId}-test-design-{YYYYMMDD}.md`
   - Example: `.claude/quality/assessments/task-006-test-design-20251029.md`
   - Create directory if needed

4. **Write test design file**

5. **Present concise summary to user:**
   - Test counts and priorities
   - Key test scenarios (security, functionality, performance)
   - Mock strategy summary
   - CI/CD integration summary
   - Risk-test mapping (if available)
   - Next steps guidance

**Output:**
- Complete test design document written to file
- Concise summary presented to user
- User has clear guidance for implementation

**Example Summary:**
```markdown
## Test Design Complete

**Task:** User Signup Implementation
**File:** .claude/quality/assessments/task-006-test-design-20251029.md

---

### Test Summary

**Total Tests:** 24 scenarios designed
- Unit: 15 (business logic, validation)
- Integration: 7 (API endpoints, database)
- E2E: 2 (complete user journeys)

**Priority Breakdown:**
- 🔴 P0 (Critical): 8 tests - Must pass before merge
- 🟠 P1 (High): 10 tests - Should pass before merge
- 🟡 P2 (Medium): 6 tests - Can defer if needed

**Estimated Time:** 14 seconds total execution (fast suite)

---

### Key Test Scenarios

**Security (P0):**
- SQL injection attempts rejected
- Password strength validation enforced
- Rate limiting prevents brute force

**Functionality (P0):**
- Valid signup creates user and returns token
- Duplicate email rejected with 409
- Email confirmation sent successfully

**Performance (P1):**
- Signup response < 200ms (target)
- No N+1 queries in user operations
- Concurrent signups handled correctly

---

### Mock Strategy

**Email Service:** Full mock with success/failure scenarios
**Database:** Test instance with isolated data per test
**JWT Service:** Real implementation (deterministic in tests)

---

### CI/CD Integration

**Pre-commit:** Unit tests only (< 10s)
**Pull Request:** All tests + coverage check (< 3min)
**Pre-deployment:** E2E + smoke tests (< 5min)

**Coverage Requirements:**
- Overall: 80% minimum (blocks merge if below)
- Critical paths (auth): 100% required

---

### Risk-Test Mapping

Based on risk profile, tests address:
- 🔴 Critical Risk (Score 9): Password logging → Security test (P0)
- 🟠 High Risk (Score 6): SQL injection → Security tests (P0)
- 🟠 High Risk (Score 6): N+1 query → Performance test (P1)

All high-risk areas have corresponding P0/P1 tests.

---

### Next Steps

1. Review full test design document for details
2. Begin implementation with test-first approach
3. Write tests for each scenario as you implement
4. Run tests frequently during development
5. Verify all P0 tests pass before marking ready for review

**Ready to begin implementation with this test strategy?**
```

**Halt Conditions:**
- File write fails (cannot save test design document)

**Reference:** See [test-examples.md](references/test-examples.md) for complete test design examples

---

## Integration with Other Skills

### After Risk Profile Skill

```markdown
Risk profile identified high-risk areas:
- File: .claude/quality/assessments/task-006-risk-20251029.md
- Critical risks: 1 (score 9)
- High risks: 3 (score 6)

Test design uses risk scores for prioritization:
- Critical risks → P0 tests (must pass before merge)
- High risks → P0/P1 tests (should pass before merge)
- Medium/low risks → P2 tests (can defer if needed)

Next: Implement with test-first approach using test design guidance
```

### Before Implementation

```markdown
Test design complete:
- File: .claude/quality/assessments/task-006-test-design-20251029.md
- 24 test scenarios specified with Given-When-Then
- Mock strategies documented for email, database
- CI/CD integration planned (pre-commit → PR → staging → production)

Implementation should:
1. Write tests following these scenarios
2. Use specified mock strategies
3. Achieve P0 tests first (critical functionality)
4. Target 80%+ overall coverage, 100% critical paths

Next: Begin implementation with test-first approach
```

### Integration with Trace Requirements Skill

```markdown
Test design provides 24 test scenarios:
- Mapped to acceptance criteria
- Prioritized by risk (P0/P1/P2)

Trace requirements skill will verify:
- All scenarios implemented as tests
- All acceptance criteria covered by passing tests
- Coverage gaps identified and addressed

Next: After implementation, run trace-requirements to verify AC coverage
```

## Best Practices

1. **Test-First Approach:**
   - Design tests before implementation
   - Tests guide implementation decisions and prevent "testing afterthought"

2. **Risk-Informed Prioritization:**
   - Use risk profile for prioritization (critical risks → P0 tests)
   - Don't skip high-risk tests even if time-constrained

3. **Appropriate Test Levels:**
   - Unit for logic and algorithms (fast, isolated)
   - Integration for component interactions (realistic, moderate speed)
   - E2E for critical user journeys (slow, high value)
   - Don't over-rely on E2E (slow, brittle)

4. **Realistic Mock Strategies:**
   - Mock external dependencies (APIs, payment, email)
   - Use real implementations when practical (database, file system with test instances)
   - Document mock data and scenarios clearly

5. **CI/CD Integration:**
   - Fast feedback loops (unit tests pre-commit)
   - Comprehensive validation (all tests on PR)
   - Production smoke tests post-deployment

6. **Coverage vs Quality:**
   - 100% coverage doesn't guarantee quality
   - Focus on meaningful scenarios (security, critical paths, edge cases)
   - Critical paths should have 100% coverage (security, payment, data integrity)

## Common Pitfalls to Avoid

1. **Too Many E2E Tests:**
   - ❌ Don't test everything through UI (slow, brittle)
   - ✅ Unit test logic, E2E test critical journeys only

2. **Under-Mocking:**
   - ❌ Don't hit real external APIs in tests (slow, flaky, expensive)
   - ✅ Mock external dependencies, use test instances for local services

3. **Brittle Tests:**
   - ❌ Don't hard-code IDs, dates, specific strings (breaks easily)
   - ✅ Use factories, fixtures, flexible assertions

4. **Ignoring Test Performance:**
   - ❌ Don't accept slow test suite ("we'll fix it later" never happens)
   - ✅ Keep unit tests < 50ms, integration < 500ms

5. **Testing Implementation Details:**
   - ❌ Don't test private methods, internal state (brittle)
   - ✅ Test public API, observable behavior (robust)

6. **No CI/CD Integration:**
   - ❌ Don't only run tests locally (manual, error-prone)
   - ✅ Automate tests in CI/CD pipeline (consistent, reliable)

## Configuration

### In `.claude/config.yaml`

```yaml
quality:
  # Test coverage targets
  testCoverage:
    overall: 80              # Minimum overall coverage
    criticalPaths: 100       # Critical paths must have 100%
    newCode: 90              # New code held to higher standard

  # Test execution timeouts
  testTimeouts:
    unit: 5000               # 5 seconds total for all unit tests
    integration: 30000       # 30 seconds total for integration tests
    e2e: 60000               # 60 seconds total for E2E tests

  # Test assessment location
  assessmentLocation: ".claude/quality/assessments"
```

### Template File

`.claude/templates/test-design.md` - Template for test design output (optional)

---

**Version:** 2.0 (Refactored for skill-creator compliance and Minimal V2 architecture)
**Category:** Quality
**Depends On:** risk-profile (optional but recommended for risk-informed prioritization)
**Used By:** trace-requirements (verifies test coverage of acceptance criteria)
