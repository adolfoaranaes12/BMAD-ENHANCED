# BMAD Enhanced - Best Practices Guide

**World-class patterns and practices for software product development with AI agents**

Version: 2.0
Last Updated: 2025-11-05

---

## Table of Contents

1. [Core Principles](#core-principles)
2. [Planning Best Practices](#planning-best-practices)
3. [Development Best Practices](#development-best-practices)
4. [Quality Assurance Best Practices](#quality-assurance-best-practices)
5. [Architecture Best Practices](#architecture-best-practices)
6. [Team Collaboration](#team-collaboration)
7. [Configuration Management](#configuration-management)
8. [Testing Strategy](#testing-strategy)
9. [CI/CD Integration](#cicd-integration)
10. [Performance Optimization](#performance-optimization)
11. [Security Practices](#security-practices)
12. [Anti-Patterns to Avoid](#anti-patterns-to-avoid)
13. [Production Readiness](#production-readiness)
14. [Maintenance and Support](#maintenance-and-support)

---

## Core Principles

### Principle 1: AI Assists, Developers Decide

**Guideline:** AI agents provide recommendations and automation, but developers make final decisions.

**Practice:**
```bash
# Good: Review AI output
/alex *create-task-spec "feature"
# Then review and adjust .claude/tasks/task-001.md

# Bad: Blindly accept all AI suggestions
/james *implement task-001  # Without reviewing spec
```

**Why:** AI can miss context, business rules, or architectural constraints known to human developers.

---

### Principle 2: Quality First, Speed Second

**Guideline:** Never sacrifice quality for speed.

**Practice:**
```bash
# Good: Always run quality gate
/james *implement task-001
/quinn *review task-001
# Wait for PASS before merging

# Bad: Skip quality checks
/james *implement task-001
git commit && git push  # No review
```

**Why:** Technical debt accumulates quickly. Quality gates prevent it.

---

### Principle 3: Test-Driven Development

**Guideline:** Tests before implementation, always.

**Practice:**
```yaml
# James follows TDD cycle automatically:
# 1. RED: Write failing test
# 2. GREEN: Implement minimal code to pass
# 3. REFACTOR: Clean up code
```

**Why:** TDD ensures testability, prevents regressions, documents behavior.

---

### Principle 4: Progressive Complexity

**Guideline:** Start simple, add complexity when needed.

**Practice:**
```bash
# Good: Simple first
/alex *create-task-spec "User login with email"
# Then expand
/alex *create-task-spec "Add OAuth providers"

# Bad: Everything at once
/alex *create-task-spec "Complete authentication system with OAuth, 2FA, SSO, LDAP, SAML"
```

**Why:** Simple solutions are easier to build, test, and maintain.

---

### Principle 5: Observability by Default

**Guideline:** Enable telemetry and monitoring from the start.

**Practice:**
```yaml
# .claude/config.yaml
telemetry:
  enabled: true
  track_token_usage: true
  track_quality_metrics: true
```

**Why:** Can't improve what can't be measured.

---

## Planning Best Practices

### BP-P1: Clear, Testable Acceptance Criteria

**Practice:**
```yaml
# Good acceptance criteria
acceptance_criteria:
  - User can submit form with valid email
  - System displays error for invalid email format
  - Success message appears after submission
  - Form clears after successful submission

# Bad acceptance criteria
acceptance_criteria:
  - Form works correctly
  - Email validation is good
```

**Template:**
- Use "User can..." format
- Make criteria verifiable (pass/fail)
- Be specific, not vague
- Include happy and error paths

---

### BP-P2: Right-Size Tasks

**Practice:**
```bash
# Good: 1-3 days of work
/alex *create-task-spec "Add search to product listing"

# Too Large (>5 days)
/alex *breakdown-epic "Complete e-commerce platform"
# Generates multiple right-sized tasks

# Too Small (<4 hours)
# Combine with related work
```

**Guidelines:**
- **Simple:** 4-8 hours (1 day)
- **Standard:** 1-3 days
- **Complex:** 3-5 days
- **Epic:** Break down into stories

---

### BP-P3: Risk Assessment Before Implementation

**Practice:**
```bash
# Always assess risk for new features
/alex *create-task-spec "Payment processing integration"
/quinn *risk-profile .claude/tasks/task-001.md
# Review risks before starting
/james *implement task-001
```

**When to Skip:** Only for trivial tasks (simple CRUD, UI updates)

---

### BP-P4: Estimation Consistency

**Practice:**
```yaml
# Use consistent scale
estimation_scale: fibonacci  # 1, 2, 3, 5, 8, 13, 21

# Relative sizing
1 point: Simple button addition
2 points: Form with validation
3 points: API endpoint with tests
5 points: Feature with multiple files
8 points: Complex feature requiring research
```

**Tip:** Establish baseline stories for reference.

---

## Development Best Practices

### BP-D1: TDD Always

**Practice:**
```bash
# James does this automatically
/james *implement task-001

# Follows:
# 1. Write test (RED)
# 2. Implement (GREEN)
# 3. Refactor (REFACTOR)
```

**Benefits:**
- Testable design by default
- Documentation through tests
- Confidence in refactoring
- Regression prevention

---

### BP-D2: Small, Focused Commits

**Practice:**
```bash
# Good: One logical change
git commit -m "Add email validation to registration form"

# Bad: Multiple unrelated changes
git commit -m "Add email validation, fix bug, refactor utils"
```

**Template:**
```bash
# Feature
git commit -m "feat: Add search functionality to product list"

# Fix
git commit -m "fix: Resolve null pointer in user service"

# Refactor
git commit -m "refactor: Extract validation logic to helper"

# Test
git commit -m "test: Add integration tests for checkout flow"
```

---

### BP-D3: Code Review Before Merge

**Practice:**
```bash
# Automated review
/quinn *review task-001

# Human review (still recommended)
# Create PR for team review
```

**Checklist:**
-  All tests passing
-  Quality gate PASS
-  Coverage e 80%
-  No security vulnerabilities
-  Documentation updated
-  Acceptance criteria met

---

### BP-D4: Refactor Continuously

**Practice:**
```bash
# After feature completion
/james *refactor task-001

# Or specific areas
/james *refactor src/services/user-service.ts
```

**When to Refactor:**
- After adding feature (clean up)
- When complexity increases
- When patterns emerge
- Before adding new feature to same area

---

### BP-D5: Error Handling Everywhere

**Practice:**
```typescript
// Good: Comprehensive error handling
async function fetchUser(id: string): Promise<User> {
  try {
    const response = await api.get(`/users/${id}`);
    if (!response.data) {
      throw new Error('User not found');
    }
    return response.data;
  } catch (error) {
    logger.error('Failed to fetch user', { id, error });
    throw new AppError('User fetch failed', 'USER_FETCH_ERROR');
  }
}

// Bad: Silent failures
async function fetchUser(id: string) {
  const response = await api.get(`/users/${id}`);
  return response.data;
}
```

---

## Quality Assurance Best Practices

### BP-Q1: Quality Gate for Every Feature

**Practice:**
```bash
# Always before merge
/quinn *quality-gate task-001

# If PASS ’ merge
# If CONCERNS ’ review and decide
# If FAIL ’ fix issues
```

**Never Skip:** Quality gates prevent technical debt.

---

### BP-Q2: NFR Assessment for Critical Features

**Practice:**
```bash
# Always for:
/quinn *nfr-assess task-payment    # Payment/financial
/quinn *nfr-assess task-auth       # Authentication
/quinn *nfr-assess task-api        # Public APIs
/quinn *nfr-assess task-data       # Data processing

# Optional for:
# - Simple UI components
# - Internal tools
# - Prototypes
```

---

### BP-Q3: Security Scanning

**Practice:**
```yaml
# .claude/config.yaml
quality:
  security_scan: true
  scan_dependencies: true
  check_owasp_top10: true
```

**Tools Integration:**
- Dependency scanning (npm audit, safety)
- SAST (static analysis)
- Secret detection
- License compliance

---

### BP-Q4: Performance Testing

**Practice:**
```bash
# For APIs and critical paths
/quinn *nfr-assess task-api-001

# Manually add performance tests
# Test with realistic load
```

**Thresholds:**
```yaml
performance:
  api_response_time: 200ms  # p95
  page_load_time: 3000ms    # p95
  database_query: 100ms     # p95
```

---

### BP-Q5: Test Coverage Monitoring

**Practice:**
```yaml
# Minimum thresholds
quality:
  min_test_coverage: 80
  statement_coverage: 80
  branch_coverage: 75
  function_coverage: 80
```

**Track Over Time:**
```bash
# View coverage trends
cat .claude/telemetry/coverage-history.jsonl
```

---

## Architecture Best Practices

### BP-A1: Architecture Review for Major Changes

**Practice:**
```bash
# Before implementing major features
/design-architecture requirements.md

# Review existing architecture
/review-architecture docs/architecture.md

# For brownfield systems
/analyze-architecture src/
```

**When Required:**
- New services/modules
- Database schema changes
- External integrations
- Technology migrations

---

### BP-A2: Document Architectural Decisions

**Practice:**
```markdown
# ADR Template (Architecture Decision Record)
# docs/adr/001-use-postgresql.md

## Context
Need database for user data with ACID guarantees

## Decision
Use PostgreSQL for primary database

## Consequences
- Positive: Strong ACID compliance, rich feature set
- Negative: Requires more resources than SQLite
- Risks: Team needs PostgreSQL expertise
```

**Generate ADRs:**
```bash
/design-architecture requirements.md
# Automatically includes ADRs
```

---

### BP-A3: API Design Standards

**Practice:**
```yaml
api_design:
  versioning: url_path  # /api/v1/users
  naming: kebab-case    # /user-profiles
  http_methods: REST    # GET, POST, PUT, DELETE
  response_format: json
  error_format: rfc7807  # Problem Details

# Example
GET /api/v1/user-profiles/123
POST /api/v1/user-profiles
PUT /api/v1/user-profiles/123
DELETE /api/v1/user-profiles/123
```

---

### BP-A4: Database Design

**Practice:**
```sql
-- Use meaningful names
CREATE TABLE user_profiles (
  id UUID PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Add indexes for queries
CREATE INDEX idx_user_profiles_email ON user_profiles(email);

-- Use constraints
ALTER TABLE user_profiles
  ADD CONSTRAINT check_email_format
  CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$');
```

---

## Team Collaboration

### BP-T1: Shared Task Specifications

**Practice:**
```bash
# Developer A creates spec
/alex *create-task-spec "User authentication"
git add .claude/tasks/task-001.md
git commit -m "feat: Add authentication task spec"
git push

# Developer B implements
git pull
/james *implement task-001
```

**Benefits:**
- Consistent understanding
- Clear acceptance criteria
- Traceable requirements

---

### BP-T2: Code Review Workflow

**Practice:**
```bash
# Developer implements
/james *implement task-001

# Automated review
/quinn *review task-001

# Create PR
git push origin feature/auth
# Open PR for human review

# Address feedback
/james *apply-qa-fixes task-001
```

---

### BP-T3: Documentation Standards

**Practice:**
```bash
# Always document
docs/
   README.md              # Project overview
   GETTING-STARTED.md     # Setup instructions
   API.md                 # API documentation
   ARCHITECTURE.md        # System design
   adr/                   # Architecture decisions
```

**Generated by:**
```bash
/design-architecture requirements.md
# Creates comprehensive documentation
```

---

## Configuration Management

### BP-C1: Environment-Specific Configuration

**Practice:**
```yaml
# .claude/config.yaml (committed)
project:
  name: "My Project"

# .claude/config.local.yaml (ignored)
development:
  database_url: "postgres://localhost/dev"
  api_key: "dev-key-123"

# .claude/config.production.yaml
production:
  database_url: ${DB_URL}  # From environment
  api_key: ${API_KEY}
```

---

### BP-C2: Quality Threshold Configuration

**Practice:**
```yaml
# Adjust per project needs
quality:
  min_test_coverage: 80     # Standard
  max_complexity: 10        # Cyclomatic complexity
  quality_gate_threshold: 70

# Stricter for critical systems
quality:
  min_test_coverage: 90
  max_complexity: 8
  quality_gate_threshold: 80
```

---

## Testing Strategy

### BP-TS1: Test Pyramid

**Practice:**
```
         /\
        /  \  E2E (5%)
       /____\
      /      \ Integration (15%)
     /________\
    /          \ Unit (80%)
   /____________\
```

**Distribution:**
- **80% Unit Tests:** Fast, focused, isolated
- **15% Integration Tests:** Component interaction
- **5% E2E Tests:** Critical user journeys

---

### BP-TS2: Test Naming Convention

**Practice:**
```python
# Pattern: test_<function>_<scenario>_<expected>

def test_login_with_valid_credentials_returns_token():
    pass

def test_login_with_invalid_password_returns_401():
    pass

def test_login_with_missing_email_returns_400():
    pass
```

---

### BP-TS3: Test Data Management

**Practice:**
```python
# Good: Fixtures for reusable test data
@pytest.fixture
def valid_user():
    return {
        "email": "test@example.com",
        "password": "SecurePass123!"
    }

def test_login_success(valid_user):
    response = login(valid_user)
    assert response.status_code == 200

# Bad: Hardcoded test data everywhere
def test_login():
    response = login({"email": "test@example.com", "password": "pass"})
```

---

## CI/CD Integration

### BP-CI1: Automated Quality Gates

**Practice:**
```yaml
# .github/workflows/quality.yml
name: Quality Gate

on: [pull_request]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Run Tests
        run: /james *test

      - name: Quality Gate
        run: /quinn *quality-gate task-${{ github.event.pull_request.number }}

      - name: Block if FAIL
        run: |
          if grep "FAIL" quality-gate-report.md; then
            exit 1
          fi
```

---

### BP-CI2: Automated Documentation

**Practice:**
```yaml
# Generate docs on merge
on:
  push:
    branches: [main]

jobs:
  docs:
    runs-on: ubuntu-latest
    steps:
      - name: Generate API Docs
        run: npm run docs:generate

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
```

---

## Performance Optimization

### BP-PO1: Token Usage Optimization

**Practice:**
```bash
# Use haiku for simple tasks
/alex *create-task-spec "simple CRUD" --model haiku

# Use sonnet for standard tasks (default)
/james *implement task-001

# Use opus only for complex tasks
/james *implement task-complex --model opus
```

---

### BP-PO2: Progressive Disclosure

**Practice:**
```bash
# Skills use references/ for large docs
.claude/skills/planning/validate-story/
   SKILL.md                    # Core workflow (< 500 lines)
   references/
       validation-checklist.md # Detailed criteria
       templates.md            # Output formats
```

**Benefits:**
- Smaller context windows
- Faster loading
- Lower token usage

---

## Security Practices

### BP-S1: Input Validation Always

**Practice:**
```typescript
// Good: Validate all inputs
function createUser(email: string, password: string) {
  // Validate email format
  if (!isValidEmail(email)) {
    throw new ValidationError('Invalid email format');
  }

  // Validate password strength
  if (password.length < 12) {
    throw new ValidationError('Password too weak');
  }

  // Sanitize inputs
  const sanitizedEmail = sanitize(email);

  return userRepository.create(sanitizedEmail, hashPassword(password));
}
```

---

### BP-S2: Secrets Management

**Practice:**
```bash
# NEVER commit secrets
# Use environment variables
API_KEY=xxx
DB_PASSWORD=yyy

# Or secret management service
aws secretsmanager get-secret-value --secret-id prod/api-key
```

**.gitignore:**
```
.env
.env.local
*.key
*.pem
secrets/
```

---

### BP-S3: Dependency Scanning

**Practice:**
```yaml
# .claude/config.yaml
security:
  scan_dependencies: true
  fail_on_high: true
  fail_on_critical: true
```

**Tools:**
```bash
# JavaScript
npm audit fix

# Python
safety check

# Java
mvn dependency-check:check
```

---

## Anti-Patterns to Avoid

### AP-1: Skipping Planning

**Anti-Pattern:**
```bash
# Bad: Jump straight to coding
/james *implement "Add user authentication"
# No task spec, no acceptance criteria
```

**Best Practice:**
```bash
# Good: Plan first
/alex *create-task-spec "Add user authentication"
# Review spec
/james *implement task-001
```

**Why:** Without clear requirements, implementation will be wrong.

---

### AP-2: Ignoring Quality Gates

**Anti-Pattern:**
```bash
/james *implement task-001
# Quality gate shows FAIL
git push  # Merge anyway
```

**Best Practice:**
```bash
/james *implement task-001
/quinn *quality-gate task-001
# If FAIL, fix issues
/james *apply-qa-fixes task-001
# Verify PASS before merge
```

**Why:** Technical debt compounds quickly.

---

### AP-3: No Tests or Low Coverage

**Anti-Pattern:**
```bash
# Bad: Skip tests
/james *implement task-001 --skip-tests
```

**Best Practice:**
```bash
# Good: TDD always
/james *implement task-001
# James writes tests automatically
# Coverage e 80%
```

**Why:** Untested code is legacy code from day one.

---

### AP-4: Over-Engineering

**Anti-Pattern:**
```yaml
# Bad: Complex solution for simple problem
"Add logout button" ’
  - Microservices architecture
  - Event-driven design
  - Redis caching
  - Kubernetes deployment
```

**Best Practice:**
```bash
# Good: Simple solution
/alex *create-task-spec "Add logout button"
# Generates appropriately scoped solution
```

**Why:** Complexity without need is technical debt.

---

### AP-5: Not Using Orchestrator for Complex Workflows

**Anti-Pattern:**
```bash
# Bad: Manual coordination of multiple agents
/alex *create-task-spec "feature"
# Wait...
/james *implement task-001
# Wait...
/quinn *review task-001
# Forget steps, lose state
```

**Best Practice:**
```bash
# Good: Use orchestrator
/orchestrator *workflow feature-delivery "feature"
# Handles coordination automatically
```

**Why:** Orchestrator ensures completeness and handles state.

---

## Production Readiness

### BP-PR1: Production Readiness Checklist

**Before Deployment:**
```yaml
functionality:
  - [ ] All acceptance criteria met
  - [ ] All tests passing
  - [ ] Manual testing completed

quality:
  - [ ] Quality gate: PASS
  - [ ] Test coverage e 80%
  - [ ] No critical security issues
  - [ ] Performance targets met

documentation:
  - [ ] API documentation updated
  - [ ] README updated
  - [ ] Deployment guide created
  - [ ] Runbook for operations

operations:
  - [ ] Monitoring configured
  - [ ] Logging enabled
  - [ ] Alerts defined
  - [ ] Rollback plan documented
```

---

### BP-PR2: Deployment Strategy

**Practice:**
```yaml
deployment:
  strategy: blue-green  # or canary, rolling

  steps:
    1. Deploy to staging
    2. Run smoke tests
    3. Deploy to production (10% traffic)
    4. Monitor metrics
    5. Increase to 50% if healthy
    6. Full rollout if stable
    7. Rollback if issues
```

---

## Maintenance and Support

### BP-MS1: Regular Refactoring

**Practice:**
```bash
# Schedule refactoring sprints
# Every 3-4 sprints, dedicate time to:
/james *refactor src/services/
/james *refactor src/components/

# Address technical debt
/quinn *review src/ --focus technical-debt
```

---

### BP-MS2: Documentation Updates

**Practice:**
```bash
# Update docs with every feature
/james *implement task-001
# Also update:
docs/API.md        # If API changed
docs/README.md     # If setup changed
docs/ARCHITECTURE.md  # If design changed
```

---

### BP-MS3: Telemetry Review

**Practice:**
```bash
# Weekly review
cat .claude/telemetry/*.jsonl | jq
# Look for:
# - Performance trends
# - Quality gate pass rates
# - Common failure patterns
# - Token usage patterns
```

---

## Summary

### Top 10 Must-Follow Practices

1. ** Always plan before implementing** (/alex first)
2. ** Use TDD** (tests before code)
3. ** Run quality gates** (before merge)
4. ** Maintain 80% test coverage** (minimum)
5. ** Review all AI output** (human oversight)
6. ** Use orchestrator for complex workflows** (coordination)
7. ** Document architecture decisions** (ADRs)
8. ** Security scan dependencies** (no vulnerabilities)
9. ** Monitor with telemetry** (observability)
10. ** Refactor continuously** (technical debt)

### Key Metrics to Track

```yaml
quality_metrics:
  test_coverage: e 80%
  quality_gate_pass_rate: e 95%
  code_complexity: d 10
  security_vulnerabilities: 0 critical, 0 high

performance_metrics:
  build_time: < 10 minutes
  test_execution_time: < 5 minutes
  quality_gate_time: < 2 minutes

business_metrics:
  time_to_feature: < 1 hour
  bug_fix_time: < 30 minutes
  deployment_frequency: daily
  change_failure_rate: < 5%
```

---

**Follow these practices for world-class software development with BMAD Enhanced!**

---

**Version:** 2.0
**Status:** Production Ready
**Last Updated:** 2025-11-05
