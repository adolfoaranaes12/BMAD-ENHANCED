---
name: refine-story
description: Transform vague or incomplete user stories into sprint-ready stories with clear acceptance criteria, test scenarios, and technical guidance. Use before sprint commitment for definition of ready check.
acceptance:
  - story_quality_improved: "Story quality score increased by at least 1 point on 4-point scale"
  - acceptance_criteria_complete: "At least 5 specific, testable acceptance criteria defined"
  - technical_guidance_provided: "Technical notes added with tech stack, patterns, security, and data models"
  - definition_of_ready_met: "Story meets all 6 INVEST criteria (Independent, Negotiable, Valuable, Estimable, Small, Testable)"
inputs:
  story_id:
    type: string
    required: true
    description: "ID of story file in .claude/stories/"
  focus:
    type: enum
    values: ["all", "acceptance-criteria", "technical-notes", "edge-cases", "test-scenarios"]
    default: "all"
    description: "Specific aspect to focus refinement on"
  interactive:
    type: boolean
    default: false
    description: "Ask user questions during refinement for clarification"
outputs:
  refined_story:
    type: object
    description: "Updated story with enhanced narrative, AC, technical notes, edge cases, test scenarios"
  quality_score_before:
    type: number
    description: "Quality score before refinement (0-4 scale)"
  quality_score_after:
    type: number
    description: "Quality score after refinement (0-4 scale)"
  ready_for_sprint:
    type: boolean
    description: "Whether story meets definition of ready"
  refinement_report:
    type: string
    description: "Path to detailed refinement report file"
telemetry:
  emit: "skill.refine-story.completed"
  track:
    - story_id
    - duration_ms
    - quality_score_before
    - quality_score_after
    - quality_improvement
    - ac_count_before
    - ac_count_after
    - ready_for_sprint
---

# Story Refinement

Transform vague, incomplete, or ambiguous user stories into clear, sprint-ready stories with well-defined acceptance criteria, test scenarios, and technical guidance.

## Purpose

Apply structured refinement techniques to improve story quality:
- Enhance user story narrative (As a... I want... So that...)
- Develop comprehensive acceptance criteria (5-8 specific, testable AC)
- Add technical guidance (tech stack, patterns, security, data models)
- Identify edge cases (boundary conditions, unusual input, concurrency)
- Create test scenarios (unit, integration, E2E)
- Ensure definition of ready compliance (INVEST criteria)

## When to Use

Use this skill when:
- Story has vague or unclear requirements
- Acceptance criteria are missing or incomplete
- Story is too large and needs decomposition
- Technical approach is unclear
- Before sprint commitment (definition of ready check)
- After stakeholder feedback requiring clarification

Do NOT use when:
- Story already has comprehensive AC and technical notes
- Story is just being created (use breakdown-epic first)
- Story is in progress (use refine-task instead)

## Prerequisites

- Story file must exist in `.claude/stories/`
- Basic user story narrative present (or at minimum a title)
- General understanding of feature context

## Sequential Refinement Process

Execute steps in order - each builds on previous enhancements:

### Step 0: Load Story and Assess Quality

**Purpose:** Evaluate current story quality against definition of ready.

**Actions:**

1. Read story file from `.claude/stories/{story-id}.md`

2. Parse story components:
   - Title
   - User story narrative (As a... I want... So that...)
   - Acceptance criteria
   - Technical notes
   - Edge cases
   - Test scenarios
   - Dependencies

3. Assess quality against definition of ready (INVEST):
   - **Independent:** Can be worked on without other stories
   - **Negotiable:** Flexible on implementation details
   - **Valuable:** Delivers clear value to user/business
   - **Estimable:** Team can estimate with confidence
   - **Small:** Fits in one sprint (typically ≤13 points)
   - **Testable:** Clear how to verify it works

4. Calculate quality score (0-4 scale):
   ```
   Quality Score = Average of:
   - Title quality (1-4)
   - Narrative quality (1-4)
   - AC quality (1-4)
   - Technical notes quality (1-4)
   - Edge cases coverage (1-4)
   - Dependencies clarity (1-4)
   ```

5. Identify specific gaps and determine refinement strategy

**Output:**
```
Story Assessment:
- Current Quality: 1.5/4 (Poor)
- Ready for Sprint: ❌ No
- Issues Identified: 6
  * Title too generic (missing "how")
  * Narrative incomplete (no "As a..." format)
  * AC vague and untestable (2 AC, both generic)
  * Missing technical notes
  * No edge cases identified
  * No test scenarios
- Estimated Refinement: 15 minutes
```

**Reference:** See [story-quality-assessment.md](references/story-quality-assessment.md) for detailed assessment criteria.

---

### Step 1: Enhance User Story Narrative

**Purpose:** Transform vague narrative into clear, valuable user story.

**Standard Format:**
```
As a [persona],
I want to [action],
So that [benefit/value].
```

**Actions:**

1. **Identify Persona:**
   - Who is the user? (end user, admin, system, developer)
   - Be specific: "registered user" not just "user"

2. **Clarify Action:**
   - What does user want to do?
   - Use specific, action-oriented verbs
   - Avoid technical jargon unless developer story

3. **Articulate Value:**
   - Why does user want this?
   - What problem does it solve?
   - What outcome does it enable?

**Example Refinement:**

**Before:**
```
Users should be able to login.
```

**After:**
```
As a registered user,
I want to log in with my email and password
So that I can access my personalized account and data securely.
```

**Refinement Rationale:**
- Added persona: "registered user"
- Specified action: "log in with email and password"
- Articulated value: "access personalized account and data securely"

---

### Step 2: Develop Comprehensive Acceptance Criteria

**Purpose:** Define specific, testable criteria for "done".

**AC Best Practices:**
- **Specific:** No ambiguity about what needs to be true
- **Testable:** Can verify with a test case
- **Implementation-independent:** What, not how
- **User-focused:** From user perspective when possible
- **Numbered:** For easy reference (AC-1, AC-2, etc.)

**AC Categories to Cover:**

1. **Happy Path** (2-3 AC): Core functionality working correctly
2. **Validation** (2-3 AC): Input validation and format checking
3. **Error Handling** (2-3 AC): Failure scenarios with clear error messages
4. **Security** (1-2 AC): Authentication, authorization, data protection
5. **Performance** (1 AC): Response time or throughput requirements

**Example Expansion:**

**Before (Poor AC):**
```
- Login works
- Error handling
```

**After (Comprehensive AC):**
```
**Happy Path:**
- AC-1: User can enter email and password on login form
- AC-2: Valid credentials return 200 with JWT token
- AC-3: User redirected to dashboard after successful login

**Validation:**
- AC-4: Invalid email format returns 400 with "Invalid email format"
- AC-5: Empty password returns 400 with "Password is required"

**Error Handling:**
- AC-6: Wrong password returns 401 with "Invalid credentials"
- AC-7: Non-existent email returns 401 with "Invalid credentials" (no enumeration)

**Security:**
- AC-8: Password never exposed in logs or responses
- AC-9: Login attempts logged with timestamp, IP, outcome
- AC-10: Account locked for 15 min after 5 failed attempts

**Performance:**
- AC-11: Login response time < 500ms for 95% of requests
```

**Reference:** See [refinement-techniques.md](references/refinement-techniques.md) for AC development patterns.

---

### Step 3: Identify and Document Edge Cases

**Purpose:** Anticipate boundary conditions, unusual inputs, and failure scenarios.

**Edge Case Categories:**

1. **Boundary Conditions:** Min/max lengths, exactly at limit values
2. **Unusual Input:** Special characters, unicode, whitespace
3. **Timing & Concurrency:** Simultaneous requests, race conditions
4. **State Transitions:** User already logged in, account changes mid-operation
5. **External Dependencies:** Database down, Redis unavailable, network failures
6. **Security Scenarios:** Brute force, injection attempts, XSS

**Example Edge Cases:**
```
1. Password exactly 12 characters (minimum length)
2. Email with + symbol (user+tag@domain.com) - should work
3. Whitespace at start/end of inputs - should trim
4. Same user logs in from 2 browsers simultaneously - both should succeed
5. User changes password while login attempt in-flight - may succeed or fail
6. Database connection lost mid-login - return 500, don't lock account
7. 1000 rapid login attempts - rate limit kicks in, IP blocked
```

**Reference:** See [refinement-techniques.md](references/refinement-techniques.md) for edge case identification guide.

---

### Step 4: Add Technical Guidance

**Purpose:** Provide technical context for implementation.

**Technical Notes Structure:**

1. **Technology Stack:** Languages, frameworks, libraries to use
2. **Architecture Patterns:** Repository, service layer, middleware patterns
3. **Security Considerations:** Hashing algorithms, rate limiting, validation
4. **Data Models:** Database schemas, field types, relationships
5. **API Contracts:** Request/response formats, status codes
6. **Performance Requirements:** Response times, throughput, indexes

**Example Technical Notes:**
```markdown
## Technical Notes

**Technology Stack:**
- Node.js 20.x with TypeScript
- Express.js for routing
- PostgreSQL 16 for user storage
- Redis 7 for rate limiting
- bcrypt (cost 12) for password hashing
- jsonwebtoken for JWT generation
- Zod for input validation

**Implementation Approach:**
1. Controller Layer: HTTP request/response handling, input validation
2. Service Layer: Business logic, rate limiting, login attempt logging
3. Repository Layer: Database queries with parameterized queries

**Security Considerations:**
- Password never leaves database unhashed
- JWT secret in environment variable (not committed)
- Rate limiting: 5 attempts / 10 min / IP
- Error messages avoid email enumeration

**Data Models:**
users table:
  - id: UUID (primary key)
  - email: VARCHAR(254) UNIQUE NOT NULL
  - password_hash: VARCHAR(60) NOT NULL
  - is_locked: BOOLEAN DEFAULT FALSE
  - locked_until: TIMESTAMP NULL

**API Contract:**
POST /api/auth/login
Request: { "email": string, "password": string }
Success (200): { "token": string, "expiresIn": number, "user": {...} }
Error (401): { "error": "Invalid credentials", "code": "AUTH_INVALID_CREDENTIALS" }

**Performance:**
- Database query: < 50ms (indexed email lookup)
- Bcrypt comparison: ~200ms (cost 12)
- Total response: < 500ms (p95)
```

**Reference:** See [story-templates.md](references/story-templates.md) for technical notes templates.

---

### Step 5: Create Test Scenarios

**Purpose:** Define how to verify story works correctly.

**Test Types:**

1. **Unit Tests** (Fast, Isolated): Test individual functions
2. **Integration Tests** (Medium, With Dependencies): Test multiple components
3. **E2E Tests** (Slow, Full System): Test complete workflows
4. **Performance Tests** (Optional): Test under load

**Example Test Scenarios:**
```markdown
## Test Scenarios

### Unit Tests
- U-1: Validate email format (valid: "user@example.com", invalid: "invalid")
- U-2: Hash password with bcrypt (returns hash starting with "$2b$12$")
- U-3: Verify password against hash (returns true for correct, false for incorrect)

### Integration Tests
- I-1: Successful login with valid credentials (returns 200 with JWT token)
- I-2: Failed login with wrong password (returns 401, logs failure)
- I-3: Account lockout after 5 failed attempts (returns 429 on 5th attempt)

### E2E Tests
- E-1: Complete signup and login flow (signup → login → access protected route)
```

**Reference:** See [refinement-techniques.md](references/refinement-techniques.md) for test scenario templates.

---

### Step 6: Define Story Size and Splitting Criteria

**Purpose:** Ensure story fits in one sprint (≤13 points).

**Size Categories:**
- **XS (1-2 points):** < 4 hours, minimal complexity
- **S (3-5 points):** 4-8 hours, moderate complexity
- **M (8 points):** 1-2 days, higher complexity
- **L (13 points):** 2-3 days, very complex
- **XL (21+ points):** MUST SPLIT

**Splitting Triggers:**
- Estimated at > 13 points
- More than 10 acceptance criteria
- Involves 3+ distinct components
- Team has low confidence in estimate (<70%)

**Splitting Strategies:**
1. By workflow steps (signup → verify email → complete profile)
2. By CRUD operations (view → edit → delete)
3. By persona (standard user → admin)
4. By priority (MVP → nice-to-have → future)
5. By happy path vs edge cases

**Reference:** See [refinement-techniques.md](references/refinement-techniques.md) for detailed splitting strategies.

---

### Step 7: Update Story File with Refinements

**Purpose:** Save all refinements to story file.

**Updated Story Structure:**
```markdown
# Story: [Title]

**ID:** [story-id]
**Priority:** [P0/P1/P2/P3]
**Status:** Ready
**Estimated:** [Story points] ([Confidence %])

## User Story

As a [persona],
I want to [action],
So that [benefit].

## Acceptance Criteria

[Categorized AC from Step 2]

## Technical Notes

[Technical guidance from Step 4]

## Edge Cases

[Edge cases from Step 3]

## Test Scenarios

[Test scenarios from Step 5]

## Dependencies

**Blocked By:** [story-ids if any]

## Definition of Done

- [ ] All acceptance criteria met
- [ ] Code reviewed and approved
- [ ] Tests written and passing (>80% coverage)
- [ ] Documentation updated
```

**Reference:** See [story-templates.md](references/story-templates.md) for complete story template.

---

### Step 8: Generate Refinement Report

**Purpose:** Document changes made and quality improvement.

**Report File:** `.claude/refinements/{story-id}-refinement-{date}.md`

**Report Contents:**
```markdown
# Story Refinement Report

**Story ID:** {story-id}
**Refinement Date:** {YYYY-MM-DD}

## Summary

**Quality Before:** 1.5/4 (Poor)
**Quality After:** 3.5/4 (Excellent)
**Improvement:** +2.0 points

**Ready for Sprint:**
- Before: ❌ No
- After: ✅ Yes

## Key Improvements

- Added complete "As a... I want... So that..." narrative
- Expanded from 2 vague AC to 11 specific, testable AC
- Added comprehensive technical notes
- Identified 7 edge cases
- Created 6 test scenarios

## Specific Changes

### Enhanced Narrative
[Before/after comparison]

### Expanded Acceptance Criteria
[New AC added, existing AC clarified]

### Added Technical Guidance
[Technical notes added]

## Definition of Ready Assessment

| Criterion | Before | After |
|-----------|--------|-------|
| Independent | ❌ | ✅ |
| Negotiable | ✅ | ✅ |
| Valuable | ⚠️ | ✅ |
| Estimable | ❌ | ✅ |
| Small | ❌ | ✅ |
| Testable | ❌ | ✅ |

## Next Steps

- Estimate story points
- Add to sprint backlog
- Assign to developer
```

---

### Step 9: Present Refinement Summary to User

**Purpose:** Communicate improvements clearly.

**Summary Format:**
```
✅ Story Refinement Complete

Story: {story-id} - {Title}

Quality Improvement:
- Before: 1.5/4 (Poor)
- After: 3.5/4 (Excellent)
- Change: +2.0 points

Key Enhancements:
- ✅ Added complete user story narrative
- ✅ Expanded from 2 vague AC to 11 specific, testable AC
- ✅ Added comprehensive technical notes
- ✅ Identified 7 edge cases
- ✅ Created 6 test scenarios

Ready for Sprint: ✅ Yes (high confidence)

Files Updated:
- .claude/stories/{story-id}.md (refined story)
- .claude/refinements/{story-id}-refinement-{date}.md (detailed report)

Next Steps:
1. Estimate story points: @alex *estimate {story-id}
2. Add to sprint: @alex *sprint "Sprint 1"
3. Begin implementation: @james *implement {story-id}
```

---

## Common Refinement Patterns

**Pattern 1: The "Login Story"**
- Start: "Users can log in"
- Refined: Clear persona, specific mechanism (email+password), detailed AC for validation/errors/security, technical notes for JWT/bcrypt/rate limiting

**Pattern 2: The "CRUD Story"**
- Start: "Users can manage their profile"
- Refined: Split into View/Edit/Delete (3 stories), each with specific AC, API contracts, validation rules

**Pattern 3: The "Integration Story"**
- Start: "Integrate with payment processor"
- Refined: Clear value, detailed AC for success/failures/refunds, technical notes for API keys/webhooks/PCI compliance

**Reference:** See [integration-patterns.md](references/integration-patterns.md) for more patterns.

---

## Integration with Other Skills

**Before Refinement:**
- `breakdown-epic` → Create initial stories from epic (stories start rough, need refinement)

**After Refinement:**
- `estimate-stories` → Estimate refined stories (refinement increases confidence)
- `sprint-plan` → Add to sprint plan
- `implement-feature` → Implement with clear guidance

---

## Best Practices

1. **Refine Collaboratively:** Involve developers (feasibility), QA (testability), PO (value)
2. **Keep Stories Independent:** Minimize dependencies, deliver standalone value
3. **Make AC Testable:** Use specific numbers, define error messages exactly
4. **Document Assumptions:** What exists? What are we NOT building?
5. **Balance Detail vs Flexibility:** Enough to estimate/implement, not so much to constrain creativity

**Reference:** See [integration-patterns.md](references/integration-patterns.md) for workflow integration details.

---

## References

- [story-quality-assessment.md](references/story-quality-assessment.md) - Quality matrix, definition of ready, assessment criteria
- [refinement-techniques.md](references/refinement-techniques.md) - AC development, edge case identification, test scenarios, splitting strategies
- [story-templates.md](references/story-templates.md) - Before/after examples, story structures, technical notes templates
- [integration-patterns.md](references/integration-patterns.md) - Common patterns, workflow integration, best practices
