# BMAD Enhanced: AI-Driven Development Framework

## Project Overview

**BMAD Enhanced** is a comprehensive framework for spec-oriented, AI-driven software development using Claude Code. It combines the Breakthrough Method for Agile AI-Driven Development (BMAD) with advanced testing strategies, multi-agent workflows, and production-quality validation.

### Core Architecture

- **32+ Production-Ready Skills:** Automated capabilities spanning planning, architecture, development, and quality assurance
- **10 Specialized Subagents:** Conversational AI agents (Alex, James, Quinn, Winston, Sarah, Bob, Mary, John, Sally, Orchestrator)
- **50+ Slash Commands:** Direct skill invocation with fast execution paths
- **Hybrid Skill Selection:** Pure LLM-based reasoning for skill discovery (no algorithmic routing)

### Technology Stack

- **Framework:** BMAD Method (Agentic Planning + Focused Development)
- **Agents:** Claude Sonnet 4.5 (primary model)
- **Skills:** Python-based execution, Markdown documentation
- **MCP Servers:** vibe-check, GitHub, Playwright, code-checker integration
- **Testing:** Jest, property-based testing frameworks, traffic replay validation

---

## Development Guidelines

### 1. **Explore-Plan-Code-Commit Workflow** (CRITICAL)

**Always follow this 4-phase approach for non-trivial tasks:**

#### Phase 1: Explore (Don't Code Yet)
```
User request → Read relevant files/docs → Understand architecture
               ↓
      Ask Claude to explore codebase
               ↓
      EXPLICITLY: "Do not write any code just yet"
               ↓
      Use Explore subagent for complex investigations
```

**Key principle:** Spend 15-20 minutes on context gathering before any code generation. This consistently produces better outcomes than immediate coding.

#### Phase 2: Plan (Verify Before Proceeding)
```
Create detailed implementation plan
      ↓
Ask Claude to verify reasonableness
      ↓
Review and refine through conversation
      ↓
**ONLY PROCEED AFTER HUMAN APPROVAL**
```

Use `/winston-consult` for architectural planning or `/alex` for task specification planning.

#### Phase 3: Code (Iterate with Feedback)
```
Implement solution following approved plan
      ↓
Have Claude verify reasonableness as it implements
      ↓
Use subagents to check work independently
      ↓
Continue until tests pass and requirements met
```

#### Phase 4: Commit (Document and Review)
```
Run quality gates (Quinn validation)
      ↓
Commit results with descriptive messages
      ↓
Create pull requests if needed
      ↓
Update READMEs and changelogs
```

**Never skip exploration or planning.** The pattern prevents Claude from "jumping straight to coding" and ensures deeper thinking for complex problems.

---

### 2. **Test-Driven Development (TDD) - The Foundation**

**TDD is not optional—it's transformational for AI code reliability.**

#### Why TDD is Critical for AI-Generated Code
AI operates as a black box. TDD establishes clear success criteria BEFORE code generation, creating explicit specifications that guide AI toward solutions meeting actual requirements.

#### Effective TDD Implementation

**Step 1: Write Comprehensive Tests First**
```javascript
// ❌ WRONG: Vague test
test('user can register', () => {
  const user = { email: 'test@example.com', password: 'password123' };
  expect(register(user)).toBe(true);
});

// ✅ RIGHT: Property-based test
test('registration increases user count by exactly 1', () => {
  const initialCount = getUserCount();
  register(randomValidUser());
  expect(getUserCount()).toBe(initialCount + 1);
});

test('duplicate email registration fails', () => {
  const user = randomValidUser();
  register(user);
  expect(() => register(user)).toThrow('Email already exists');
});

test('concurrent registrations maintain data integrity', async () => {
  const users = Array(100).fill(null).map(() => randomValidUser());
  await Promise.all(users.map(u => register(u)));
  expect(getUserCount()).toBe(users.length);
});
```

**Step 2: Run Tests and Confirm Failures**
```bash
npm test  # Verify tests fail before implementation
```
Explicitly tell Claude: "This is test-driven development—avoid creating mock implementations"

**Step 3: Iterative Implementation Against Tests**
```bash
# Implement code that passes tests
# Do NOT modify tests during implementation
# Use independent subagent (@quinn) to verify implementation isn't overfitting
```

#### Test Coverage Requirements

**Minimum Coverage Thresholds:**
- Overall: 80%
- Critical paths (auth, payment, data integrity): 100%
- New code: 90%
- Security-critical code: 100%

**Test Levels:**
- **Unit tests:** <50ms execution, fully mocked dependencies, >80% coverage
- **Integration tests:** <500ms execution, test database/APIs, service boundaries
- **E2E tests:** Seconds per test, critical user journeys only, business-critical paths

**Test Priorities:**
- **P0 (Critical):** Must pass before merge (auth, payment, security, data integrity)
- **P1 (High):** Should pass before merge (core features, error handling)
- **P2 (Medium):** Can defer if time-constrained (edge cases, optional features)

---

### 3. **Property-Based Testing (Required for Production Code)**

**The Problem with Example-Based Testing:**
- Tests specific cases: "user 'john@example.com' can register"
- Misses edge cases: Unicode emails, +aliasing, concurrent registrations
- Gives false confidence: "tests pass" ≠ production-ready

**Property-Based Testing Approach:**

Instead of testing examples, verify **properties that must always hold:**

```javascript
// Category 1: Invariant Properties
test('password hash length is consistent', () => {
  fc.assert(fc.property(fc.string(), password => {
    const hash = hashPassword(password);
    expect(hash.length).toBe(60); // bcrypt always 60 chars
  }));
});

// Category 2: Inverse Properties
test('JWT encode/decode returns original data', () => {
  fc.assert(fc.property(fc.record({ userId: fc.nat(), role: fc.string() }), data => {
    const token = encodeJWT(data);
    const decoded = decodeJWT(token);
    expect(decoded).toEqual(data);
  }));
});

// Category 3: Equivalence Properties
test('optimized query produces same result as reference query', () => {
  fc.assert(fc.property(fc.nat({ max: 1000 }), userId => {
    const optimized = getUOptimized(userId);
    const reference = getUserReference(userId);
    expect(optimized).toEqual(reference);
  }));
});

// Category 4: Idempotence Properties
test('DELETE request is idempotent', async () => {
  const userId = createUser();
  await deleteUser(userId);
  await deleteUser(userId); // Second call should not error
  expect(userExists(userId)).toBe(false);
});
```

**Property-Based Test Categories:**
1. **Invariants:** "Output always within bounds", "Data structure maintains consistency"
2. **Inverses:** "Encode/decode returns original", "Serialize/deserialize preserves structure"
3. **Equivalence:** "Different paths produce identical results", "Optimized = reference implementation"
4. **Idempotence:** "Multiple calls = single call", "SET operations maintain invariants"

---

### 4. **Reality Validation: Bridging the Specification Gap**

**The Core Challenge:**
- Specifications describe perfect scenarios
- Tests validate specifications
- Production provides imperfect reality
- **Gap:** "Spec says this should work" vs "Production shows this fails"

#### Use `/validate-test-reality` Skill

**Before Quinn's quality gate, ALWAYS run:**
```bash
/quinn validate-test-reality <task-id>
```

**What it does:**
1. Generates 50+ edge cases beyond specification (Unicode, concurrency, failures, security)
2. Validates tests cover production reality, not just spec compliance
3. Identifies specification-reality gaps
4. Creates test deficiency report

**Example Output:**
```
Story: User Registration

Specification says:
✅ User can register with email + password
✅ Password minimum 8 characters

Test Reality Gap Found:
❌ Email with "+" not tested (Gmail aliasing)
❌ Unicode in passwords not tested
❌ Concurrent registration race condition not tested
❌ Database connection failure mid-transaction not tested
❌ Email service timeout handling not tested

Recommendation: Add 12 edge-case tests before QA approval
Reality Coverage: 62% (Target: 80%)
QA Readiness: NOT READY (5 critical gaps)
```

#### Edge Case Categories

**1. Data Reality Gaps:**
- Unicode/emoji in text fields
- Email edge cases (+, subdomain dots, long domains)
- Null/undefined/empty variations
- Extremely long inputs
- SQL/HTML/JS injection characters
- Timezone-specific data

**2. Concurrency Reality Gaps:**
- Simultaneous operations (10/100/1000 users)
- Race conditions on shared resources
- Database connection pool exhaustion
- Optimistic locking failures

**3. System Reality Gaps:**
- Database connection failures mid-transaction
- Third-party API timeouts/rate limits
- Disk space exhaustion
- Memory pressure
- Network partitions

**4. Performance Reality Gaps:**
- Response time under 10x expected load
- Query performance with millions of records
- Cache invalidation timing

**5. Security Reality Gaps:**
- SQL injection variants
- XSS payloads (DOM-based, stored, reflected)
- Auth bypass attempts
- Authorization boundary violations
- CSRF attacks

**6. Integration Reality Gaps:**
- API version changes
- Schema evolution (new/removed fields)
- Certificate expiration
- Backwards compatibility breaks

---

### 5. **Code Quality Standards**

#### Naming Conventions
- **Variables:** camelCase (`userId`, `isActive`)
- **Functions:** camelCase with action verbs (`getUserById`, `validateEmail`)
- **Classes:** PascalCase (`UserRepository`, `AuthService`)
- **Constants:** SCREAMING_SNAKE_CASE (`MAX_LOGIN_ATTEMPTS`, `JWT_SECRET`)
- **Files:** kebab-case (`user-repository.ts`, `auth-service.ts`)

#### Code Patterns (Enforce)
- **Single Responsibility:** Functions do one thing well
- **DRY:** No code duplication (use utilities)
- **Error Handling:** All async operations wrapped in try-catch
- **Logging:** Info for normal flow, Error for exceptions, Debug for troubleshooting
- **Security:** Input validation on ALL user inputs, no SQL string concatenation, no eval()

#### Anti-Patterns (Reject)
- **God Objects:** Classes >500 lines or >20 methods
- **Deep Nesting:** >3 levels of indentation
- **Magic Numbers:** Use named constants
- **Callback Hell:** Use async/await
- **Silent Failures:** Always log errors

---

### 6. **Security Requirements**

**Security is P0 - Never compromise.**

#### Input Validation
```javascript
// ✅ ALWAYS validate and sanitize
function createUser(input) {
  const schema = z.object({
    email: z.string().email().max(255),
    password: z.string().min(8).max(128),
  });
  const validated = schema.parse(input); // Throws on invalid
  // ... proceed with validated data
}
```

#### Authentication & Authorization
- **Authentication:** JWT with RS256 asymmetric signing (never HS256)
- **Passwords:** bcrypt with cost factor 12+
- **Sessions:** Secure, HttpOnly, SameSite cookies
- **Authorization:** Role-based access control (RBAC), verify on EVERY request

#### Data Protection
- **In Transit:** TLS 1.2+ mandatory
- **At Rest:** Encrypt sensitive fields (PII, payment data)
- **Secrets:** Never commit secrets, use environment variables

#### OWASP Top 10 Validation
Quinn automatically checks for:
1. Injection (SQL, NoSQL, Command)
2. Broken Authentication
3. Sensitive Data Exposure
4. XML External Entities (XXE)
5. Broken Access Control
6. Security Misconfiguration
7. Cross-Site Scripting (XSS)
8. Insecure Deserialization
9. Using Components with Known Vulnerabilities
10. Insufficient Logging & Monitoring

---

### 7. **Performance Requirements**

#### Response Time Targets
- **API Endpoints:** <200ms p95 (simple queries), <500ms p95 (complex queries)
- **Database Queries:** <50ms p95 (indexed), optimize N+1 queries
- **File Operations:** Async with progress tracking for >1MB files
- **Cache Hit Rate:** >90% for frequently accessed data

#### Optimization Patterns
```javascript
// ✅ Database: Use indexes, avoid N+1
const users = await db.user.findMany({
  include: { posts: true } // Single query, not N+1
});

// ✅ Caching: Redis for hot data
const cachedUser = await cache.get(`user:${id}`);
if (!cachedUser) {
  cachedUser = await db.user.findUnique({ where: { id } });
  await cache.set(`user:${id}`, cachedUser, { ttl: 300 });
}

// ✅ Pagination: Always paginate list endpoints
const users = await db.user.findMany({
  skip: (page - 1) * limit,
  take: limit,
});
```

---

### 8. **Workflow Patterns with BMAD Enhanced**

#### Direct Skills Workflow (Fast Path)
```bash
# When requirements are clear and straightforward
/create-task-spec "User login endpoint with JWT"
/implement-feature task-007 --mode tdd
/run-tests task-007 --coverage
/quinn *validate-quality-gate task-007
```

#### Subagent Workflow (Exploration Path)
```bash
# When exploring solutions or unclear requirements
@alex "I need authentication but unsure JWT vs sessions"
# Alex provides analysis and recommendation
@james *implement task-spec-from-alex.md
@quinn *review task-007
```

#### Orchestrator Workflow (Full Automation)
```bash
# For complete feature delivery pipeline
@orchestrator *workflow feature-delivery "Social login with OAuth"
# Orchestrator coordinates: planning → architecture → dev → QA → deployment
```

#### Quality Gate Workflow (Production Readiness)
```bash
# Complete quality validation before merge
/quinn *assess-risk task-007
/test-design task-007  # Generate test strategy
# Implement tests following test design
/validate-test-reality task-007  # Check reality gaps
/quinn *validate-quality-gate task-007  # Final decision
```

---

### 9. **MCP Server Integration**

**Active MCP Servers:**

#### 1. vibe-check (Chain-Pattern Interrupt)
```javascript
// Use for assumption validation
vibe_check({
  goal: "Ship CPI v2.5 with zero regressions",
  plan: "1) Write tests 2) Refactor 3) Canary rollout",
  progress: "Finished step 1"
});

// Captures mistakes and patterns
vibe_learn({
  mistake: "Skipped writing tests",
  category: "Premature Implementation",
  solution: "Added regression tests"
});
```

**When to use:**
- After planning, before major actions (challenge assumptions)
- After resolving issues (capture learnings)
- Set constitutional rules at workflow start

#### 2. GitHub (Repository Operations)
- Create PRs, issues, branches
- Review code, manage labels
- Automated quality gates in CI/CD

#### 3. code-checker (Quality Validation)
- Runs pylint with LLM-friendly prompts
- Executes pytest to identify failures
- Type checking with mypy
- Generates fix suggestions

---

### 10. **Documentation Standards**

**Every feature/change requires:**

#### 1. Code Documentation
```javascript
/**
 * Authenticates user with email/password credentials
 * @param {string} email - User email address (validated)
 * @param {string} password - Plain text password (will be hashed)
 * @returns {Promise<{ token: string, user: User }>} JWT token and user object
 * @throws {AuthError} If credentials invalid or account locked
 */
async function authenticateUser(email, password) {
  // Implementation
}
```

#### 2. README Updates
- Update FEATURES section for new capabilities
- Add usage examples
- Document configuration options

#### 3. CHANGELOG Entries
```markdown
## [1.2.0] - 2025-11-11

### Added
- JWT authentication with RS256 signing
- User registration with email validation
- Property-based tests for auth flows

### Changed
- Improved password hashing (bcrypt cost 12→14)

### Fixed
- Race condition in concurrent registrations
```

#### 4. Architecture Decision Records (ADRs)
Use `/create-adr` for significant technical decisions:
```bash
/create-adr "Why JWT over sessions for authentication"
```

---

### 11. **Git Workflow**

#### Commit Message Format
```
<type>(<scope>): <subject>

<body>

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

**Types:** feat, fix, docs, style, refactor, test, chore

**Example:**
```
feat(auth): implement JWT authentication with RS256

- Add user registration with email/password
- Implement JWT token generation and validation
- Add property-based tests for auth flows
- Include edge case tests (Unicode, concurrency)

Fixes #42

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

#### Branch Naming
- Features: `feature/user-authentication`
- Fixes: `fix/registration-race-condition`
- Experiments: `experiment/redis-caching`

---

### 12. **Critical Success Metrics**

**Track these to validate quality improvements:**

| Metric | Target | How to Measure |
|--------|--------|----------------|
| **Skill Trigger Accuracy** | >95% | Inverse trigger tests pass |
| **Production Bug Detection** | <5 bugs/100 features | Bugs found in prod vs pre-deployment |
| **Specification Completeness** | >90% | Test deficiency report <10 issues/100 lines spec |
| **Test-Production Alignment** | >85% | Production telemetry deviations from test expectations |
| **Coverage Diversity** | 3+ modes/scenario | Unit + integration + property + BDD per story |
| **Reality Coverage** | >80% | validate-test-reality edge case coverage |
| **Quality Gate Pass Rate** | >70% first attempt | Quinn quality-gate PASS decisions |

---

### 13. **Common Pitfalls to Avoid**

#### ❌ **DON'T:**
1. Skip exploration/planning phases (causes rework)
2. Write example-based tests only (misses edge cases)
3. Assume specification is complete (production reveals gaps)
4. Test implementation details (brittle tests)
5. Use too many E2E tests (slow, brittle)
6. Mock everything (integration gaps)
7. Ignore production patterns (synthetic data ≠ reality)
8. Skip security edge cases (injection, XSS, auth bypass)
9. Generate new code instead of refactoring (technical debt)
10. Rely on AI without understanding (comprehension gap)

#### ✅ **DO:**
1. Follow Explore-Plan-Code-Commit workflow
2. Write property-based tests for invariants
3. Run validate-test-reality before quality gate
4. Test public API/behavior, not private methods
5. Use E2E for critical journeys only, unit for logic
6. Mock external APIs, use real test DB
7. Validate with production traffic patterns
8. Always generate security tests (OWASP)
9. Mandate refactoring reviews
10. Require developers to explain AI-generated approaches

---

### 14. **Module-Specific Context**

Create `.claude/tasks/{task-id}.md` files for task-specific context:

```markdown
# Task 007: User Authentication

## Context
- Uses existing `UserRepository` for database access
- JWT secrets stored in environment (`JWT_SECRET`, `JWT_PUBLIC_KEY`)
- Password hashing uses `bcrypt-adapter.ts` wrapper

## Dependencies
- Database: PostgreSQL via Prisma
- Libraries: jsonwebtoken, bcrypt, zod

## Testing Requirements
- Property-based tests required (fast-check library)
- Mock Stripe API calls (use nock)
- Test database: `test.db` (auto-cleared between tests)

## Known Issues
- Existing user table lacks `locked` field (add migration first)
- Email service occasionally times out (implement retry logic)
```

---

### 15. **Skill Selection Guidelines**

**How Claude Selects Skills:**
Skills are selected through **pure LLM reasoning** (not algorithmic routing). Claude scans all skill descriptions and decides which to invoke.

**To ensure correct skill selection:**

1. **Use Trigger-Complete Descriptions:**
   - Include what the skill does
   - Include all linguistic variations of user intent
   - Include non-triggers: "This skill does NOT handle X"

2. **Example:**
```markdown
❌ BAD: "Creates authentication systems"
✅ GOOD: "Creates JWT authentication with RS256 signing. Handles user registration, login, token generation/validation. Use when implementing authentication, JWT tokens, user login systems, secure API access. Does NOT handle OAuth (use oauth-integration skill) or session-based auth (use session-auth skill)."
```

3. **Test Skill Triggering:**
Use vibe-check after skill execution:
```
Did Claude select the right skill for "implement JWT authentication"?
What alternative skills could have worked?
Why didn't Claude choose X skill instead?
```

---

### 16. **Continuous Improvement**

**After Each Major Feature:**

1. Run retrospective:
   - What worked well?
   - What could be improved?
   - Did tests catch issues before production?
   - Were reality gaps identified?

2. Update metrics:
   - Skill trigger accuracy
   - Production bug rate
   - Test-reality coverage
   - Quality gate pass rate

3. Refine processes:
   - Update skill descriptions if triggering issues
   - Add production patterns to validate-test-reality
   - Enhance property-based test library
   - Update CLAUDE.md with learnings

---

## Quick Reference Commands

### Planning
```bash
/alex *create-task-spec "requirement description"
/winston *design-architecture requirements.md
/alex *breakdown-epic epic.md
```

### Development
```bash
/james *implement task-spec.md --mode tdd
/test-design task-007
/run-tests task-007 --coverage
```

### Quality
```bash
/validate-test-reality task-007
/quinn *review task-007
/quinn *assess-nfr task-007
/quinn *validate-quality-gate task-007
```

### Architecture
```bash
/winston *design-architecture requirements.md --type fullstack
/create-adr "decision context"
/winston *validate-architecture arch.md
```

---

**Version:** 2.0
**Last Updated:** 2025-11-11
**Framework:** BMAD Enhanced with Reality Validation

_This CLAUDE.md file ensures Claude Code has comprehensive project context for production-quality AI-driven development._
