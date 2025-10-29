# Quality Skill: Test Design Strategy

<!-- BMAD Enhanced Quality Skill -->
<!-- Inspired by BMAD-METHOD QA test design pattern -->
<!-- Version: 1.0 -->

## Purpose

Create comprehensive test strategies that specify test scenarios, levels (unit/integration/E2E), priorities (P0/P1/P2), mock strategies, and CI/CD integration approaches. Provides clear guidance for what tests to write and how to write them.

**Key Innovation (BMAD Pattern):**
- Test design BEFORE implementation (guides what tests to write)
- Risk-informed prioritization (P0/P1/P2 based on risk scores)
- Level recommendations (unit vs integration vs E2E)
- Mock strategies to enable effective testing
- CI/CD integration for automated validation

## When to Use This Skill

Use this skill when you need to:
- Plan comprehensive test strategy before implementation
- Ensure test coverage aligns with requirements
- Prioritize test scenarios by importance
- Design mock strategies for external dependencies
- Plan CI/CD test integration

**Best Used:**
- After task spec creation, before implementation
- After risk profiling (uses risk scores for prioritization)
- For complex features requiring multiple test levels
- When planning test infrastructure

**Can Skip For:**
- Simple bug fixes with obvious test cases
- Trivial changes with existing test patterns
- Emergency hotfixes (add tests after)

## Test Levels

### Unit Tests
**Purpose:** Test individual functions, methods, classes in isolation

**Characteristics:**
- Fast execution (< 50ms each)
- No external dependencies (mocked)
- Test business logic and algorithms
- High coverage expected (>80%)

**When to use:**
- Business logic validation
- Data transformations
- Validation rules
- Utility functions
- Error handling logic

### Integration Tests
**Purpose:** Test interactions between components/modules

**Characteristics:**
- Moderate execution time (< 500ms each)
- May use test database, test APIs
- Test component interactions
- Focus on integration points

**When to use:**
- API endpoint testing
- Database operations
- Service-to-service communication
- Authentication/authorization flows
- External API interactions (mocked)

### E2E (End-to-End) Tests
**Purpose:** Test complete user journeys through the system

**Characteristics:**
- Slower execution (seconds per test)
- Use real or near-real environment
- Test critical user workflows
- Fewer tests, higher value

**When to use:**
- Critical user journeys
- Multi-step workflows
- UI + backend integration
- Business-critical paths
- Regression prevention for key features

## Test Priority Levels

### P0 (Critical) - Must Have
**Requirements:**
- Tests critical functionality
- Validates security requirements
- Prevents data loss
- Covers high-risk areas (from risk profile)
- Must pass before merge

**Examples:**
- Authentication and authorization
- Payment processing
- Data integrity operations
- Security vulnerability prevention

### P1 (High) - Should Have
**Requirements:**
- Tests important functionality
- Covers medium-risk areas
- Validates key user features
- Should pass before merge (exceptions allowed with justification)

**Examples:**
- Core feature functionality
- Error handling paths
- Performance requirements
- User experience features

### P2 (Medium) - Nice to Have
**Requirements:**
- Tests edge cases
- Covers low-risk areas
- Nice-to-have validations
- Can defer if time-constrained

**Examples:**
- Rare edge cases
- Minor UI variations
- Optional features
- Future enhancements

## SEQUENTIAL Skill Execution

**CRITICAL:** Do not proceed to next step until current step is complete

### Step 0: Load Configuration and Context

**Actions:**

1. Load `.claude/config.yaml`:
   - Extract quality settings
   - Extract test coverage targets

2. Get task file path from user:
   - Example: `.claude/tasks/task-006-user-signup.md`
   - Verify file exists

3. Read task specification:
   - Load objective and acceptance criteria
   - Load context (data models, APIs, components)
   - Load task breakdown

4. Check for risk profile:
   - Look for: `.claude/quality/assessments/{task-id}-risk-*.md`
   - If exists: Load risk scores for prioritization
   - If missing: Can proceed but recommend running risk-profile first

**Output:**
- Configuration loaded
- Task context understood
- Risk profile loaded (if available)

**Halt Conditions:**
- Configuration missing
- Task file missing or unreadable

### Step 1: Analyze Test Requirements

**Actions:**

1. **For each acceptance criterion:**
   - What needs to be validated?
   - What are the testable outcomes?
   - What are the edge cases?
   - What could go wrong?

2. **Identify test categories:**
   - **Happy path:** Normal, expected usage
   - **Error cases:** Invalid inputs, failures
   - **Edge cases:** Boundaries, limits
   - **Security:** Authentication, authorization, injection
   - **Performance:** Response time, resource usage
   - **Integration:** Component interactions

3. **Map to test levels:**
   - What needs unit tests? (Logic, validation)
   - What needs integration tests? (API, database)
   - What needs E2E tests? (User journeys)

4. **Consider technical constraints:**
   - External dependencies to mock
   - Database interactions
   - Async operations
   - File I/O
   - Network calls

**Output:**
- Test requirements identified per AC
- Test categories mapped
- Test levels determined
- Technical considerations noted

**Example for User Signup:**
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
- Acceptance criteria too vague to test
- Cannot identify testable outcomes

### Step 2: Design Test Scenarios

**Actions:**

For each test requirement from Step 1:

1. **Write test scenario description:**
   - Use Given-When-Then format (for clarity, not BDD code)
   - Specific inputs and expected outputs
   - Clear pass/fail criteria

2. **Assign test level:**
   - Unit, Integration, or E2E
   - Based on what's being tested

3. **Assign priority:**
   - P0 if: Critical functionality, security, high-risk (score ≥6)
   - P1 if: Important functionality, medium-risk (score 3-5)
   - P2 if: Edge cases, low-risk (score 1-2)

4. **Specify test data requirements:**
   - What data is needed?
   - Valid vs invalid samples
   - Edge case values

5. **Identify dependencies:**
   - What needs to be mocked?
   - What requires real services?
   - What fixtures needed?

**Output:**
- Test scenarios with Given-When-Then
- Test level assigned
- Priority assigned
- Test data specified
- Dependencies identified

**Example Test Scenarios:**

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
**Risk:** Linked to AC1 implementation risk
**Test Data:**
- Valid email: user@example.com
- Valid password: SecurePass123! (8+ chars, mixed case, number, special)

**Dependencies:**
- Test database with users table
- Email service mocked (verify queue called)
- JWT secret configured

**File:** src/routes/auth/__tests__/signup.integration.test.ts

---

### Scenario 2: SQL Injection Attempt Rejected (P0, Integration)

**Given** the API is running
**When** POST /api/auth/signup with email "'; DROP TABLE users; --"
**Then**
- Response status is 400 (validation error)
- Error message indicates invalid email format
- Users table still exists (not dropped)
- No database queries executed with malicious input

**Test Level:** Integration
**Priority:** P0 (Critical - security)
**Risk:** Linked to SQL injection risk (score: 6)
**Test Data:**
- Malicious email variations:
  - '; DROP TABLE users; --
  - " OR 1=1 --
  - admin' --

**Dependencies:**
- Test database
- Query logging enabled to verify Prisma parameterization

**File:** tests/security/injection.test.ts

---

### Scenario 3: Weak Password Rejected (P0, Unit)

**Given** password validation function
**When** validate password "password123" (no special char, no uppercase)
**Then**
- Validation fails
- Error message: "Password must contain uppercase, lowercase, number, and special character"

**Test Level:** Unit
**Priority:** P0 (Critical - security requirement)
**Risk:** Linked to weak password risk (score: 4)
**Test Data:**
- Weak passwords:
  - password (no numbers, special, uppercase)
  - Password (no numbers, special)
  - Password1 (no special)
  - Pass1! (too short)

**Dependencies:** None (pure function)

**File:** src/schemas/__tests__/password.test.ts
```

**Halt Conditions:**
- Cannot define clear pass/fail criteria for scenario
- Scenarios too ambiguous to implement

### Step 3: Develop Mock Strategies

**Actions:**

1. **Identify external dependencies:**
   - Third-party APIs
   - External services (email, payment, etc.)
   - Database
   - File system
   - Network resources

2. **For each dependency, decide mocking approach:**

   **Option A: Full Mock**
   - Replace with test double
   - Predictable, fast, isolated
   - Use for: Third-party APIs, external services

   **Option B: Test Instance**
   - Use real implementation with test data
   - More realistic, slower
   - Use for: Database (test DB), file system (temp dirs)

   **Option C: Partial Mock**
   - Real implementation, mock specific parts
   - Balance realism and speed
   - Use for: Service with mostly local logic but external call

3. **Specify mock data/fixtures:**
   - What responses to mock?
   - What fixtures to create?
   - What edge cases to simulate?

4. **Document mock configuration:**
   - How to set up mocks?
   - What libraries to use?
   - How to verify mock interactions?

**Output:**
- Mock strategy for each dependency
- Mock data/fixtures specified
- Configuration documented

**Example Mock Strategies:**

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
import { mockEmailService } from '../setup/mocks/emailService';
jest.mock('@/services/email', () => mockEmailService);
```

**Mock Data:**
- Success response: `{ messageId: 'test-123', status: 'sent' }`
- Failure response: `{ error: 'Service unavailable' }`
- Timeout simulation: Delay 5000ms then reject

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

**Approach:** Use real PostgreSQL with test database

**Implementation:**
```typescript
// tests/setup/database.ts
import { PrismaClient } from '@prisma/client';

export const testDb = new PrismaClient({
  datasources: {
    db: { url: process.env.TEST_DATABASE_URL }
  }
});

// Before each test:
beforeEach(async () => {
  await testDb.user.deleteMany();  // Clean slate
});
```

**Test Data:**
- Fixtures: `tests/fixtures/users.json`
- Seed scripts: `tests/setup/seedTestData.ts`

**Why not mock:**
- Database interactions are integration test targets
- Real DB catches query bugs, constraint violations
- Prisma already provides good test performance

---

### External Payment API (Full Mock)

**Approach:** Mock Stripe API to avoid test charges

**Implementation:**
```typescript
// tests/setup/mocks/stripe.ts
export const mockStripe = {
  customers: {
    create: jest.fn().mockResolvedValue({ id: 'cus_test123' })
  },
  paymentIntents: {
    create: jest.fn().mockResolvedValue({
      id: 'pi_test123',
      status: 'succeeded'
    })
  }
};
```

**Mock Scenarios:**
- Success: Payment succeeds
- Decline: Card declined (simulate error)
- Timeout: API timeout (delay then reject)
- Partial failure: Customer created, payment fails

---

### File System (Test Instance)

**Approach:** Use temp directory for file operations

**Implementation:**
```typescript
// tests/setup/filesystem.ts
import { mkdtemp, rm } from 'fs/promises';
import { join } from 'path';
import { tmpdir } from 'os';

let testDir: string;

beforeEach(async () => {
  testDir = await mkdtemp(join(tmpdir(), 'test-'));
});

afterEach(async () => {
  await rm(testDir, { recursive: true });
});
```

**Why not mock:**
- Tests actual file I/O behavior
- Catches permission, path issues
- Temp dir cleanup prevents pollution
```

**Halt Conditions:**
- Cannot determine appropriate mock strategy
- Dependency too complex to mock or test

### Step 4: Plan CI/CD Integration

**Actions:**

1. **Define test execution strategy:**
   - When do different test types run?
   - What's the trigger for each?
   - What's the failure policy?

2. **Specify test environments:**
   - Local development
   - CI pipeline
   - Pre-deployment
   - Production (smoke tests)

3. **Configure test parallelization:**
   - What can run in parallel?
   - What must run sequentially?
   - Resource requirements?

4. **Define coverage requirements:**
   - Minimum coverage percentage
   - Critical paths requiring 100%
   - Coverage failure policy

5. **Plan test data management:**
   - How to seed test data?
   - How to clean up after tests?
   - How to handle shared resources?

**Output:**
- Test execution strategy
- Environment configuration
- Parallelization plan
- Coverage requirements
- Data management approach

**Example CI/CD Integration:**

```markdown
## CI/CD Test Strategy

### Test Execution Stages

#### Stage 1: Local Development (Pre-commit)
**Trigger:** Before git commit
**Tests:** Unit tests only
**Duration:** < 10 seconds
**Failure:** Block commit
**Coverage:** N/A (quick feedback)

**Configuration:**
```bash
# .husky/pre-commit
npm run test:unit
```

---

#### Stage 2: Pull Request (CI Pipeline)
**Trigger:** On PR creation/update
**Tests:** All tests (unit + integration + E2E)
**Duration:** < 3 minutes
**Failure:** Block merge
**Coverage:** Minimum 80% overall, 100% for critical paths

**Configuration:**
```yaml
# .github/workflows/test.yml
name: Test Suite

on: [pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_DB: test_db
          POSTGRES_PASSWORD: test_password

    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '20'

      - name: Install dependencies
        run: npm ci

      - name: Run unit tests
        run: npm run test:unit

      - name: Run integration tests
        run: npm run test:integration
        env:
          DATABASE_URL: postgresql://postgres:test_password@localhost:5432/test_db

      - name: Run E2E tests
        run: npm run test:e2e

      - name: Check coverage
        run: npm run test:coverage
        # Fails if < 80% overall or < 100% on critical paths
```

---

#### Stage 3: Pre-deployment (Staging)
**Trigger:** Before production deployment
**Tests:** E2E + smoke tests
**Duration:** < 5 minutes
**Failure:** Block deployment
**Coverage:** N/A (validation only)

**Configuration:**
```yaml
# .github/workflows/deploy.yml
pre-deploy-tests:
  runs-on: ubuntu-latest
  steps:
    - name: Run E2E against staging
      run: npm run test:e2e:staging

    - name: Run smoke tests
      run: npm run test:smoke:staging
```

---

#### Stage 4: Post-deployment (Production)
**Trigger:** After production deployment
**Tests:** Smoke tests only
**Duration:** < 1 minute
**Failure:** Alert (rollback manual decision)

**Configuration:**
```yaml
post-deploy-monitoring:
  steps:
    - name: Smoke test production
      run: npm run test:smoke:production

    - name: Alert on failure
      if: failure()
      uses: slack/action@v1
      with:
        message: "Production smoke tests failed!"
```

---

### Test Parallelization

**Unit Tests:** Full parallelization (independent)
```json
{
  "jest": {
    "maxWorkers": "100%"
  }
}
```

**Integration Tests:** Parallel with isolated databases
```json
{
  "jest": {
    "maxWorkers": 4,
    "setupFilesAfterEnv": ["./tests/setup/isolatedDb.ts"]
  }
}
```

**E2E Tests:** Sequential (shared browser state)
```json
{
  "playwright": {
    "workers": 1
  }
}
```

---

### Coverage Requirements

**Minimum Coverage:**
- Overall: 80% statements, 75% branches
- New code: 90% statements, 85% branches
- Critical paths: 100% (authentication, payment, data integrity)

**Coverage Enforcement:**
```json
{
  "jest": {
    "coverageThreshold": {
      "global": {
        "statements": 80,
        "branches": 75,
        "functions": 80,
        "lines": 80
      },
      "src/services/auth/**/*.ts": {
        "statements": 100,
        "branches": 100
      },
      "src/services/payment/**/*.ts": {
        "statements": 100,
        "branches": 100
      }
    }
  }
}
```

**Coverage Gates:**
- CI fails if below minimum
- PR comment shows coverage diff
- Warning if critical path < 100%

---

### Test Data Management

**Setup:**
```typescript
// tests/setup/globalSetup.ts
export default async function globalSetup() {
  // Create test database
  await exec('npm run db:test:create');

  // Run migrations
  await exec('npm run db:test:migrate');

  // Seed base data
  await exec('npm run db:test:seed');
}
```

**Cleanup:**
```typescript
// tests/setup/globalTeardown.ts
export default async function globalTeardown() {
  // Drop test database
  await exec('npm run db:test:drop');
}
```

**Per-test cleanup:**
```typescript
// tests/setup/isolatedDb.ts
beforeEach(async () => {
  await prisma.user.deleteMany();
  await prisma.session.deleteMany();
  // Clean all tables for test isolation
});
```
```

**Halt Conditions:**
- Cannot determine appropriate CI/CD strategy
- Test environment requirements unclear

### Step 5: Calculate Test Summary

**Actions:**

1. **Count tests by level:**
   - Total unit tests
   - Total integration tests
   - Total E2E tests
   - Total all tests

2. **Count tests by priority:**
   - P0 (Critical)
   - P1 (High)
   - P2 (Medium)

3. **Estimate execution time:**
   - Unit: 50ms average × count
   - Integration: 500ms average × count
   - E2E: 5s average × count

4. **Calculate expected coverage:**
   - Based on scenarios vs acceptance criteria
   - Critical path coverage (should be 100%)

**Output:**
- Test count summary
- Priority breakdown
- Estimated execution time
- Expected coverage

**Example Summary:**
```markdown
## Test Summary

**Total Tests:** 24
- Unit: 15
- Integration: 7
- E2E: 2

**By Priority:**
- P0 (Critical): 8 tests
- P1 (High): 10 tests
- P2 (Medium): 6 tests

**Estimated Execution Time:**
- Unit: 0.75s (15 × 50ms)
- Integration: 3.5s (7 × 500ms)
- E2E: 10s (2 × 5s)
- **Total: 14.25s**

**Expected Coverage:**
- Overall: ~85-90%
- Critical paths (auth, payment): 100%
- Business logic: 95%
- Error handling: 85%
```

**Halt Conditions:**
- None (calculation always possible)

### Step 6: Generate Test Design Document

**Actions:**

1. Load test design template:
   - Read `.claude/templates/test-design.md`

2. Populate all sections:
   - Test summary (from Step 5)
   - Test scenarios by AC (from Step 2)
   - Mock strategies (from Step 3)
   - CI/CD integration (from Step 4)
   - Risk-test mapping (if risk profile available)

3. Generate file path:
   - Format: `{qualityLocation}/assessments/{taskId}-test-design-{YYYYMMDD}.md`
   - Example: `.claude/quality/assessments/task-006-test-design-20251028.md`

4. Write test design file

**Output:**
- Complete test design document
- All test scenarios specified
- Mock strategies documented
- CI/CD plan included

**Halt Conditions:**
- Template missing
- File write fails

### Step 7: Present Summary to User

**Actions:**

Generate concise summary:

```markdown
## Test Design Complete

**Task:** User Signup Implementation
**File:** .claude/quality/assessments/task-006-test-design-20251028.md

---

### Test Summary

**Total Tests:** 24 scenarios designed
- Unit: 15 (business logic, validation)
- Integration: 7 (API endpoints, database)
- E2E: 2 (complete user journeys)

**Priority Breakdown:**
- 🔴 P0 (Critical): 8 tests - Must pass before merge
- 🟠 P1 (High): 10 tests - Should pass before merge
- 🟡 P2 (Medium): 6 tests - Nice to have

**Estimated Time:** 14 seconds total execution

---

### Key Test Scenarios

**Security (P0):**
- SQL injection attempts rejected
- Password strength validation
- Rate limiting prevents brute force

**Functionality (P0):**
- Valid signup creates user and returns token
- Duplicate email rejected with 409
- Email confirmation sent

**Performance (P1):**
- Signup response < 200ms
- No N+1 queries in user listing
- Concurrent signups handled correctly

---

### Mock Strategy

**Email Service:** Full mock with success/failure scenarios
**Database:** Test instance with isolated data
**JWT Service:** Real implementation (deterministic in tests)

---

### CI/CD Integration

**Pre-commit:** Unit tests (< 10s)
**Pull Request:** All tests + coverage check (< 3min)
**Pre-deployment:** E2E + smoke tests (< 5min)

**Coverage Requirements:**
- Overall: 80% minimum
- Critical paths (auth): 100% required

---

### Risk-Test Mapping

Based on risk profile, tests address:
- 🔴 Critical Risk (Score 9): Password logging → Security test
- 🟠 High Risk (Score 6): SQL injection → Security tests
- 🟠 High Risk (Score 6): N+1 query → Performance test

All high-risk areas have corresponding P0/P1 tests.

---

### Next Steps

1. Review full test design document
2. Begin implementation with test-first approach
3. Write tests for each scenario as you implement
4. Run tests frequently during development
5. Verify all P0 tests pass before marking ready for review

**Ready to begin implementation with this test strategy? (yes/no)**
```

**Output:**
- Summary presented
- User has clear test guidance
- Ready to implement with tests

**Halt Conditions:**
- None (design complete)

## Completion Criteria

Test design is complete when:

- [ ] All acceptance criteria have test scenarios
- [ ] Test levels assigned (unit/integration/E2E)
- [ ] Priorities assigned (P0/P1/P2)
- [ ] Mock strategies developed
- [ ] CI/CD integration planned
- [ ] Test summary calculated
- [ ] Test design document generated
- [ ] Summary presented to user

## Usage Examples

### Example 1: After Risk Profiling

**User:** "Create test design for task-006, we have the risk profile"

**Test Design Skill:**
1. Loads task-006 and risk profile
2. Uses risk scores to prioritize tests:
   - Critical risk (score 9) → P0 test
   - High risks (score 6) → P0/P1 tests
3. Designs 24 test scenarios
4. Maps risks to tests
5. Generates test design document
6. Presents summary with risk-test mapping

**Result:** Test strategy informed by actual risks

### Example 2: Without Risk Profile

**User:** "Design tests for payment integration"

**Test Design Skill:**
1. Loads task specification
2. No risk profile found (recommends running risk-profile first)
3. Proceeds with test design based on ACs and context
4. Identifies high-priority scenarios (security, money handling)
5. Assigns P0 to critical areas (security, transaction integrity)
6. Generates test design
7. Recommends running risk profile for better prioritization

**Result:** Test strategy without risk input (still valuable)

### Example 3: Complex Integration

**User:** "Test strategy for multi-service checkout flow"

**Test Design Skill:**
1. Analyzes complex workflow across services
2. Identifies integration points (payment, inventory, shipping, email)
3. Designs mock strategies for each service
4. Heavy focus on integration and E2E tests
5. Plans test data fixtures for complex scenarios
6. CI/CD strategy includes service containerization
7. Generates comprehensive test design

**Result:** Test strategy for complex distributed system

## Integration with Other Skills

### After Risk Profile Skill

```markdown
Risk profile identified high-risk areas:
- File: .claude/quality/assessments/task-006-risk-20251028.md
- Critical risks: 1 (score 9)
- High risks: 3 (score 6)

Test design uses risk scores for prioritization:
- Critical risks → P0 tests (must have)
- High risks → P0/P1 tests (should have)
- Medium/low risks → P2 tests (nice to have)

Next: Implement with test-first approach using test design
```

### Before Implementation

```markdown
Test design complete:
- File: .claude/quality/assessments/task-006-test-design-20251028.md
- 24 test scenarios specified
- Mock strategies documented
- CI/CD integration planned

Implementation should:
1. Write tests following these scenarios
2. Use specified mock strategies
3. Achieve P0 tests first
4. Target 80%+ coverage

Next: Begin implementation with test-first approach
```

### Integration with Trace Requirements Skill

```markdown
Test design provides test scenarios:
- 24 tests across 3 levels
- Mapped to acceptance criteria

Trace requirements skill will verify:
- All scenarios implemented
- All ACs covered by tests
- Coverage gaps identified

Next: After implementation, run trace-requirements to verify
```

## Best Practices

1. **Test-First Approach:**
   - Design tests before implementation
   - Tests guide implementation decisions
   - Prevents "testing afterthought"

2. **Risk-Informed Prioritization:**
   - Use risk profile if available
   - Critical risks → P0 tests
   - Don't skip high-risk tests

3. **Appropriate Test Levels:**
   - Unit for logic and algorithms
   - Integration for component interactions
   - E2E for critical user journeys
   - Don't over-rely on E2E (slow, brittle)

4. **Realistic Mock Strategies:**
   - Mock external dependencies
   - Use real implementations when practical (database)
   - Document mock data and scenarios

5. **CI/CD Integration:**
   - Fast feedback loops (unit tests pre-commit)
   - Comprehensive validation (all tests on PR)
   - Production smoke tests post-deployment

6. **Coverage vs Quality:**
   - 100% coverage doesn't guarantee quality
   - Focus on meaningful scenarios
   - Critical paths should have 100% coverage

## Common Pitfalls to Avoid

1. **Too Many E2E Tests:**
   - ❌ Don't: Test everything through UI
   - ✅ Do: Unit test logic, E2E test critical journeys

2. **Under-Mocking:**
   - ❌ Don't: Hit real external APIs in tests
   - ✅ Do: Mock external dependencies, use test instances locally

3. **Brittle Tests:**
   - ❌ Don't: Hard-code IDs, dates, specific strings
   - ✅ Do: Use factories, fixtures, flexible assertions

4. **Ignoring Test Performance:**
   - ❌ Don't: Accept slow test suite ("we'll fix it later")
   - ✅ Do: Keep unit tests < 50ms, integration < 500ms

5. **Testing Implementation Details:**
   - ❌ Don't: Test private methods, internal state
   - ✅ Do: Test public API, observable behavior

6. **No CI/CD Integration:**
   - ❌ Don't: Only run tests locally
   - ✅ Do: Automate tests in CI/CD pipeline

## Configuration

### In `.claude/config.yaml`

```yaml
quality:
  # Test coverage targets
  testCoverage:
    overall: 80
    criticalPaths: 100
    newCode: 90

  # Test execution timeouts
  testTimeouts:
    unit: 5000      # 5 seconds total
    integration: 30000   # 30 seconds total
    e2e: 60000      # 60 seconds total
```

### In `.claude/templates/test-design.md`

Template for test design output (to be created)

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-10-28 | Initial test design skill based on BMAD QA test strategy pattern |

---

**End of Test Design Skill**
