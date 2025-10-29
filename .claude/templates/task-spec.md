# Task: {{TASK_TITLE}}

<!-- BMAD Enhanced Task Specification -->
<!-- Version: 1.0 -->
<!-- This file follows the BMAD context embedding pattern -->

## Metadata

- **Task ID:** {{TASK_ID}}
- **Created:** {{DATE}}
- **Last Updated:** {{DATE}}
- **Related Epic/Feature:** {{EPIC_OR_FEATURE}}
- **Priority:** {{PRIORITY}}  <!-- P0 (Critical) | P1 (High) | P2 (Medium) | P3 (Low) -->

## Status

{{STATUS}}  <!-- Draft | Approved | InProgress | Review | Done -->

---

## Objective

**As a** {{ROLE}},
**I want** {{ACTION}},
**so that** {{BENEFIT}}.

---

## Acceptance Criteria

<!-- Copy from epic/requirements and make specific to this task -->

1. {{CRITERION_1}}
2. {{CRITERION_2}}
3. {{CRITERION_3}}

---

## Context (Embedded from Architecture)

<!-- CRITICAL: This section contains ALL context needed for implementation -->
<!-- Implementation skill should NOT need to read architecture docs -->
<!-- Every technical detail MUST include source reference -->

### Previous Task Insights

<!-- Key learnings from previous implementation that inform this task -->

{{PREVIOUS_INSIGHTS}}

<!-- Example:
- Authentication middleware pattern established in task-001
- Use existing error handling utilities in src/utils/errors.ts
- Database connection pooling configured with max 20 connections
-->

### Data Models

<!-- Specific schemas, validation rules, relationships -->

{{DATA_MODELS}}

<!-- Example:
User Model:
- id: UUID (primary key)
- email: string (unique, validated with Zod email schema)
- password: string (hashed with bcrypt, cost: 12)
- createdAt: timestamp (auto-generated)
- updatedAt: timestamp (auto-updated)

Validation Rules:
- Email: Must match RFC 5322 format
- Password: Min 8 chars, must contain uppercase, lowercase, number, special char

[Source: docs/architecture/data-models.md#user-model]
-->

### API Specifications

<!-- Endpoint details, request/response formats, auth requirements -->

{{API_SPECIFICATIONS}}

<!-- Example:
POST /api/auth/signup
Request:
  {
    "email": "string",
    "password": "string"
  }
Response (201):
  {
    "user": { "id": "uuid", "email": "string" },
    "token": "jwt_token"
  }
Response (400):
  {
    "error": "string",
    "details": ["validation errors"]
  }

Authentication: None (public endpoint)
Rate Limit: 5 requests per minute per IP

[Source: docs/architecture/rest-api-spec.md#auth-endpoints]
-->

### Component Specifications

<!-- UI component details, props, state management (if applicable) -->

{{COMPONENT_SPECIFICATIONS}}

<!-- Example:
SignupForm Component:
- Location: src/components/auth/SignupForm.tsx
- Props:
  - onSuccess: (user: User) => void
  - onError: (error: Error) => void
- State:
  - email: string
  - password: string
  - isSubmitting: boolean
  - errors: { email?: string, password?: string }
- Validation: Real-time on blur, submit on form submit

[Source: docs/architecture/components.md#signup-form]
-->

### File Locations

<!-- Exact paths where new code should be created based on project structure -->

{{FILE_LOCATIONS}}

<!-- Example:
Implementation Files:
- Route handler: src/routes/auth/signup.ts
- Service logic: src/services/auth/signup.service.ts
- Database operations: src/repositories/user.repository.ts
- Validation schemas: src/schemas/auth.schema.ts

Test Files:
- Unit tests: src/services/auth/__tests__/signup.service.test.ts
- Integration tests: src/routes/auth/__tests__/signup.integration.test.ts
- E2E tests: tests/e2e/auth/signup.e2e.test.ts

[Source: docs/architecture/project-structure.md]
-->

### Testing Requirements

<!-- Specific test cases, strategies, frameworks from testing standards -->

{{TESTING_REQUIREMENTS}}

<!-- Example:
Testing Strategy:
- Framework: Jest + Supertest
- Coverage Target: >80% for new code
- Test Levels:
  - Unit: Service logic, validation, utilities
  - Integration: API endpoints with test database
  - E2E: User journeys with Playwright

Required Test Cases:
1. Valid signup creates user and returns token (AC: 1)
2. Invalid email format rejected with 400 (AC: 2)
3. Weak password rejected with validation errors (AC: 2)
4. Duplicate email prevented with 409 (AC: 3)
5. Email verification email sent (AC: 4)

Mock Strategy:
- Email service: Mock in unit/integration, real in E2E
- Database: In-memory SQLite for unit, test DB for integration

[Source: docs/architecture/testing-strategy.md]
-->

### Technical Constraints

<!-- Version requirements, performance considerations, security rules -->

{{TECHNICAL_CONSTRAINTS}}

<!-- Example:
Performance:
- API response time: <200ms for p95
- Database queries: Max 3 per request (prevent N+1)
- Password hashing: Use bcrypt with cost 12 (balance security/performance)

Security:
- All inputs validated with Zod schemas
- SQL injection prevented via parameterized queries (Prisma)
- Passwords never logged or exposed in errors
- Rate limiting on auth endpoints: 5 req/min

Dependencies:
- Node.js: >=20.0.0
- bcrypt: ^5.1.1
- zod: ^3.22.4

[Source: docs/architecture/tech-stack.md, docs/standards.md#security]
-->

---

## Tasks / Subtasks

<!-- Sequential tasks with clear validation points -->
<!-- Each task should reference applicable acceptance criteria -->
<!-- Check off boxes as implementation progresses -->

- [ ] **Task 1:** {{TASK_1_DESCRIPTION}} (AC: {{AC_NUMBERS}})
  - [ ] Subtask 1.1: {{SUBTASK_DESCRIPTION}}
  - [ ] Subtask 1.2: {{SUBTASK_DESCRIPTION}}
  - [ ] Write unit tests for Task 1
  - [ ] Validate Task 1 implementation

- [ ] **Task 2:** {{TASK_2_DESCRIPTION}} (AC: {{AC_NUMBERS}})
  - [ ] Subtask 2.1: {{SUBTASK_DESCRIPTION}}
  - [ ] Subtask 2.2: {{SUBTASK_DESCRIPTION}}
  - [ ] Write integration tests for Task 2
  - [ ] Validate Task 2 implementation

- [ ] **Task 3:** {{TASK_3_DESCRIPTION}} (AC: {{AC_NUMBERS}})
  - [ ] Subtask 3.1: {{SUBTASK_DESCRIPTION}}
  - [ ] Write E2E tests for Task 3
  - [ ] Validate Task 3 implementation

- [ ] **Final Validation:**
  - [ ] All acceptance criteria verified
  - [ ] All tests passing (unit + integration + E2E)
  - [ ] Code follows project standards
  - [ ] Documentation updated

---

## Implementation Record

<!-- IMPORTANT: This section is ONLY modified by implementation skill -->
<!-- Planning skill does NOT populate this section -->

### Agent Model Used

<!-- Record the specific AI model used for implementation -->

{{AGENT_MODEL}}  <!-- e.g., claude-sonnet-4-5 -->

### Debug Log References

<!-- Links to detailed debug logs if needed -->

{{DEBUG_LOG_REFERENCES}}

<!-- Example:
- See .claude/debug-log.md lines 145-289 for database connection issues
-->

### Completion Notes

<!-- Notes about implementation, deviations, decisions -->

{{COMPLETION_NOTES}}

<!-- Example:
- Changed password validation library from validator to zod for consistency
- Added extra logging for email service failures
- Discovered edge case with unicode emails, added handling
- Performance note: bcrypt cost 12 adds ~150ms, acceptable for auth endpoint
-->

### Files Modified

<!-- List all files created, modified, or deleted -->

{{FILES_MODIFIED}}

<!-- Example:
Created:
- src/routes/auth/signup.ts
- src/services/auth/signup.service.ts
- src/schemas/auth.schema.ts
- src/services/auth/__tests__/signup.service.test.ts
- src/routes/auth/__tests__/signup.integration.test.ts
- tests/e2e/auth/signup.e2e.test.ts

Modified:
- src/routes/auth/index.ts (added signup route)
- src/types/user.ts (added User interface)
- README.md (updated API documentation)
-->

### Testing Results

<!-- Summary of test execution -->

{{TESTING_RESULTS}}

<!-- Example:
Unit Tests:
- 12 tests, 12 passed, 0 failed
- Coverage: 94% statements, 89% branches, 100% functions

Integration Tests:
- 5 tests, 5 passed, 0 failed
- Database operations verified

E2E Tests:
- 2 tests, 2 passed, 0 failed
- Complete signup flow validated

Total Execution Time: 4.2s
-->

---

## Quality Review

<!-- IMPORTANT: This section is ONLY modified by quality skill -->
<!-- Populated after implementation is marked "Ready for Review" -->

### Review Date

{{REVIEW_DATE}}

### Reviewer

{{REVIEWER}}  <!-- e.g., quality-skill-v1.0 -->

### Quality Gate Decision

{{GATE_DECISION}}  <!-- PASS | CONCERNS | FAIL | WAIVED -->

### Quality Gate File

{{GATE_FILE_PATH}}  <!-- e.g., .claude/quality/gates/task-001-gate.yaml -->

### Summary

{{REVIEW_SUMMARY}}

<!-- Example:
CONCERNS: Implementation meets functional requirements but performance
issue identified. N+1 query pattern in user listing endpoint should be
optimized before production deployment. All tests passing, security
requirements met.

See quality gate file for detailed findings and recommendations.
-->

---

## Change Log

<!-- Track changes to this task specification -->

| Date | Version | Description | Author |
|------|---------|-------------|--------|
| {{DATE}} | 1.0 | Initial task specification created | {{AUTHOR}} |

---

<!-- End of Task Specification -->
