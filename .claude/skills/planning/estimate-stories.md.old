# Estimate Stories Skill

## Purpose
Estimate story points for user stories using a structured formula based on complexity, effort, and risk factors. This skill provides consistent, evidence-based estimations that help with sprint planning and velocity tracking.

## When to Use This Skill
- After user stories have been created from epic breakdown
- When refining existing stories that need estimation
- When re-estimating stories based on new information
- Before sprint planning to prepare stories for commitment
- When comparing similar stories for consistency

## Invocation
```bash
# Single story estimation
@alex *estimate story-auth-001

# Batch estimation (process multiple stories)
@alex *estimate story-auth-001 story-auth-002 story-auth-003

# Re-estimation with context
@alex *estimate story-auth-001 --reason "New dependencies discovered"
```

## Prerequisites
- Story file must exist in `.claude/stories/` directory
- Story must have clear acceptance criteria
- Basic understanding of the codebase/tech stack

## Skill Configuration
```yaml
skill_name: estimate-stories
version: 1.0.0
subagent: alex-planner
execution_mode: sequential
halt_on_error: false
output_directory: .claude/estimations
```

---

## STEP 0: Load Configuration and Story Context

### Actions
1. Validate input story ID(s)
2. Check that story file(s) exist
3. Load story content
4. Load project configuration for baseline context
5. Initialize estimation framework

### Story ID Format
```
story-{component}-{number}-{short-name}.md

Examples:
- story-auth-001-signup.md
- story-payment-003-stripe-integration.md
- story-ui-007-responsive-navbar.md
```

### Load Story Content
Read the complete story file to understand:
- User story narrative (As a... I want... So that...)
- Acceptance criteria (AC-1, AC-2, etc.)
- Dependencies (if any)
- Technical notes
- Priority level
- Current estimation (if exists)

### Configuration Context
Load from `.claude/config.yaml`:
- Team velocity baseline
- Tech stack information
- Known complexity patterns
- Historical estimation data (if available)

### Example Story Structure
```markdown
**Title:** User Signup with Email and Password

**User Story:**
As a new user,
I want to create an account with my email and password
So that I can access the application and save my data.

**Acceptance Criteria:**
- AC-1: User can enter email and password on signup form
- AC-2: Email must be valid format (validated with Zod)
- AC-3: Password hashed with bcrypt (cost 12)
- AC-4: Duplicate emails rejected with 409 error
- AC-5: Success response returns JWT token
- AC-6: User record saved to PostgreSQL database

**Priority:** P0 (Must Have)
**Dependencies:** None
**Technical Notes:** Requires Zod validation, bcrypt, JWT, PostgreSQL
```

---

## STEP 1: Analyze Complexity (1-5 Scale)

### Definition
**Complexity** measures the technical difficulty and cognitive load required to implement the story. This is NOT about time/effort, but about the intricacy of the solution.

### Complexity Scale

#### 1 - Trivial
- **Description:** Straightforward implementation with well-known patterns
- **Characteristics:**
  - Single file change
  - No new dependencies
  - Copy-paste from existing code
  - No edge cases
  - No integration points
- **Examples:**
  - Add a new static field to a form
  - Update button text
  - Add a simple CSS class
  - Create a basic GET endpoint that returns hardcoded data

#### 2 - Simple
- **Description:** Simple implementation requiring basic problem-solving
- **Characteristics:**
  - 2-3 file changes
  - Uses existing patterns/libraries
  - Minimal edge cases
  - Well-documented approach
  - 1-2 integration points
- **Examples:**
  - Basic CRUD endpoint with validation
  - Simple form with validation
  - Add new field to existing model
  - Basic authentication check

#### 3 - Moderate
- **Description:** Moderate complexity requiring careful design
- **Characteristics:**
  - 4-6 file changes
  - May require new library/pattern
  - Multiple edge cases to handle
  - 2-3 integration points
  - Some architectural decisions
- **Examples:**
  - OAuth integration
  - File upload with validation
  - Complex form with conditional logic
  - API integration with error handling
  - Multi-step wizard

#### 4 - Complex
- **Description:** High complexity requiring significant design work
- **Characteristics:**
  - 7-12 file changes
  - Multiple new patterns/abstractions
  - Many edge cases and error paths
  - 4-6 integration points
  - Significant architectural impact
  - Performance considerations
- **Examples:**
  - Real-time notification system
  - Complex state management
  - Multi-tenant architecture changes
  - Advanced caching strategy
  - Complex data transformation pipeline

#### 5 - Very Complex
- **Description:** Very high complexity, may need spike/research
- **Characteristics:**
  - 12+ file changes
  - New architectural patterns
  - Extensive edge cases
  - 6+ integration points
  - Cross-cutting concerns
  - Performance critical
  - Security critical
- **Examples:**
  - Payment processing integration
  - Real-time collaborative editing
  - Complex search with faceting
  - Distributed transaction handling
  - Custom security implementation

### Complexity Analysis Factors
When analyzing complexity, consider:

1. **Number of Integration Points**
   - Internal services/modules
   - External APIs
   - Database interactions
   - Event systems

2. **Error Handling Paths**
   - Happy path only = lower complexity
   - Multiple error scenarios = higher complexity

3. **State Management**
   - Stateless = lower complexity
   - Complex state transitions = higher complexity

4. **Algorithmic Complexity**
   - Simple loops = lower complexity
   - Complex algorithms = higher complexity

5. **Novelty**
   - Using existing patterns = lower complexity
   - Creating new patterns = higher complexity

6. **Testing Complexity**
   - Simple unit tests = lower complexity
   - Complex integration tests with mocks = higher complexity

### Example Complexity Analysis

**Story:** User Signup with Email and Password

**Analysis:**
- **Integration Points:** 3 (Validation library, Auth service, Database)
- **Error Paths:** 4 (Invalid email, weak password, duplicate email, DB error)
- **State Management:** Simple (stateless request/response)
- **Algorithm:** None (standard hashing/validation)
- **Novelty:** Low (standard auth pattern)
- **Testing:** Moderate (unit + integration tests needed)

**Complexity Score:** 3 (Moderate)
**Rationale:** Standard implementation with multiple integration points and error paths, but well-established patterns exist.

---

## STEP 2: Analyze Effort (1-5 Scale)

### Definition
**Effort** measures the amount of work (time) required to implement, test, and document the story. This focuses on hours/days needed.

### Effort Scale

#### 1 - Minimal (<1 hour)
- **Description:** Can be completed in under 1 hour
- **Characteristics:**
  - Very few lines of code (<50 lines)
  - No tests needed OR trivial test update
  - No documentation needed
  - No review complexity
- **Examples:**
  - Change button color
  - Update static text
  - Add simple log statement
  - Fix typo in error message

#### 2 - Low (1-2 hours)
- **Description:** Half day or less
- **Characteristics:**
  - 50-150 lines of code
  - 1-2 simple unit tests
  - Minimal documentation
  - Quick review
- **Examples:**
  - Add new API parameter with validation
  - Simple form field addition
  - Basic error message improvement
  - Simple component styling

#### 3 - Medium (2-4 hours)
- **Description:** Half to full day
- **Characteristics:**
  - 150-300 lines of code
  - 3-5 tests (unit + maybe integration)
  - Some documentation needed
  - Standard review
- **Examples:**
  - New CRUD endpoint
  - Form with multiple fields and validation
  - API integration (well-documented)
  - State management for single feature

#### 4 - High (4-8 hours)
- **Description:** 1-2 full days
- **Characteristics:**
  - 300-600 lines of code
  - 6-10 tests (unit + integration)
  - Significant documentation
  - Careful review needed
- **Examples:**
  - Complex feature with multiple components
  - Multi-step workflow
  - Advanced error handling
  - Performance optimization work

#### 5 - Very High (>8 hours)
- **Description:** More than 2 days, consider splitting
- **Characteristics:**
  - 600+ lines of code
  - 10+ comprehensive tests
  - Extensive documentation
  - Multiple review rounds
- **Examples:**
  - Large feature spanning multiple modules
  - Complex refactoring
  - New architectural component
  - Security implementation with audit

### Effort Analysis Factors
When analyzing effort, consider:

1. **Code Volume**
   - Estimate lines of code needed
   - Consider boilerplate vs. logic

2. **Testing Requirements**
   - Unit tests needed
   - Integration tests needed
   - E2E tests needed
   - Mock complexity

3. **Documentation**
   - Code comments
   - API documentation
   - User documentation
   - Architecture decision records

4. **Research/Learning**
   - New library to learn
   - New pattern to understand
   - Domain knowledge needed

5. **Review/Iteration**
   - Expected review rounds
   - Likely changes needed

6. **Coordination**
   - Team dependencies
   - External team coordination

### Example Effort Analysis

**Story:** User Signup with Email and Password

**Analysis:**
- **Code Volume:** ~200 lines
  - API endpoint: 50 lines
  - Validation schema: 30 lines
  - Service layer: 60 lines
  - Database migration: 20 lines
  - Frontend form: 40 lines

- **Testing:** 5 tests needed
  - 3 unit tests (validation, service, controller)
  - 2 integration tests (successful signup, duplicate email)

- **Documentation:** Moderate
  - API endpoint documentation
  - Code comments for security considerations

- **Research:** Minimal
  - Standard bcrypt and JWT patterns

- **Review:** Standard (1 round)

**Effort Score:** 3 (Medium - 2-4 hours)
**Rationale:** Standard implementation requiring frontend + backend + tests + docs, fits within half to full day.

---

## STEP 3: Analyze Risk (0-3 Adjustment)

### Definition
**Risk** represents uncertainty, unknowns, or factors that could cause the story to take longer than expected or require rework. This is an ADJUSTMENT to the base score, not a multiplication factor.

### Risk Scale

#### 0 - No Risk
- **Description:** Completely understood, no unknowns
- **Characteristics:**
  - Exact duplicate of existing work
  - All dependencies in place
  - Well-tested approach
  - No external dependencies
  - Clear acceptance criteria
- **Examples:**
  - Copy existing endpoint for new entity
  - Replicate existing form pattern
  - Standard CRUD operation (done 10+ times before)

#### 1 - Low Risk
- **Description:** Minor unknowns, manageable
- **Characteristics:**
  - Mostly familiar territory
  - 1-2 minor unknowns
  - Stable dependencies
  - Clear acceptance criteria
  - Standard patterns apply
- **Examples:**
  - Using a familiar library in a slightly new way
  - Minor edge case handling
  - Well-documented third-party API

#### 2 - Medium Risk
- **Description:** Significant unknowns, may need investigation
- **Characteristics:**
  - 2-3 significant unknowns
  - New library/service (but good docs)
  - Some ambiguity in requirements
  - May need technical spike
  - Dependencies on other work
- **Examples:**
  - First time using a particular library
  - Integration with partially documented API
  - Performance requirements unclear
  - Dependency on in-progress work

#### 3 - High Risk
- **Description:** Major unknowns, likely needs spike first
- **Characteristics:**
  - Many unknowns
  - Poorly documented dependencies
  - Unclear requirements
  - Likely rework needed
  - Complex dependencies
  - Potential architectural impact
- **Examples:**
  - Undocumented third-party API
  - New technology/pattern for the team
  - Vague requirements
  - Known technical debt in affected area
  - Critical security/performance concerns

### Risk Analysis Factors
When analyzing risk, consider:

1. **Requirement Clarity**
   - Clear, specific acceptance criteria = lower risk
   - Vague, ambiguous requirements = higher risk

2. **Technical Uncertainty**
   - Known approach = lower risk
   - New/unknown approach = higher risk

3. **Dependency Stability**
   - Stable, mature dependencies = lower risk
   - New, changing, undocumented = higher risk

4. **Team Familiarity**
   - Done it before = lower risk
   - First time = higher risk

5. **External Factors**
   - No external dependencies = lower risk
   - Depends on external team/API = higher risk

6. **Technical Debt**
   - Clean codebase = lower risk
   - High debt in area = higher risk

### Example Risk Analysis

**Story:** User Signup with Email and Password

**Analysis:**
- **Requirement Clarity:** HIGH
  - Clear acceptance criteria
  - Well-defined error cases
  - Standard signup flow

- **Technical Uncertainty:** LOW
  - Well-established patterns
  - Standard bcrypt + JWT approach
  - Clear validation rules

- **Dependency Stability:** HIGH
  - Mature libraries (bcrypt, jsonwebtoken, Zod)
  - PostgreSQL database already set up

- **Team Familiarity:** MEDIUM
  - Team has done auth before
  - Specific libraries may be new

- **External Factors:** NONE
  - All internal implementation

- **Technical Debt:** LOW
  - New feature in clean area

**Risk Score:** 1 (Low Risk)
**Rationale:** Well-defined requirements with standard approach and stable dependencies. Minor risk due to possible library learning curve.

---

## STEP 4: Calculate Story Points

### Formula
```
Base Score = (Complexity + Effort) / 2
Adjusted Score = Base Score + Risk Adjustment
Story Points = Round to nearest Fibonacci number
```

### Fibonacci Scale
Use the Fibonacci sequence for final story points:
```
1, 2, 3, 5, 8, 13, 21
```

### Why Fibonacci?
- Represents increasing uncertainty at higher estimates
- Forces meaningful distinctions between sizes
- Prevents false precision (no "7 vs 8" debates)
- Industry standard for agile estimation

### Rounding Rules
- **Round to nearest Fibonacci number**
- **For midpoints (e.g., 4, 6.5, 10), round UP** to account for planning uncertainty
- **Maximum story point: 13** - Anything larger should be split

### Example Calculation

**Story:** User Signup with Email and Password

**Step-by-step:**
1. **Complexity:** 3 (Moderate - multiple integration points)
2. **Effort:** 3 (Medium - 2-4 hours of work)
3. **Risk:** +1 (Low - minor library learning)

**Calculation:**
```
Base Score = (3 + 3) / 2 = 3
Adjusted Score = 3 + 1 = 4
Story Points = 5 (round 4 up to nearest Fibonacci)
```

**Final Estimate:** 5 Story Points

### Confidence Level
Provide confidence in the estimation:
- **High Confidence (90%+):** Clear requirements, known approach, team experience
- **Medium Confidence (70-89%):** Most aspects clear, some minor unknowns
- **Low Confidence (<70%):** Significant unknowns, may need spike

For this story: **High Confidence (85%)** - Standard implementation with clear requirements.

---

## STEP 5: Provide Estimation Rationale

### Rationale Structure
A good rationale should explain:
1. **Complexity reasoning** - Why this complexity score?
2. **Effort reasoning** - What work is included?
3. **Risk reasoning** - What could cause variance?
4. **Comparable stories** - Similar past stories (if any)
5. **Assumptions** - What are we assuming?
6. **Splitting recommendation** - Should this be split?

### Example Rationale

**Story:** User Signup with Email and Password (5 points)

#### Complexity (3/5 - Moderate)
This story involves multiple integration points (validation, authentication, database) and several error paths (invalid email, weak password, duplicate email, database errors). However, the patterns are well-established in the industry. We're using standard libraries (Zod for validation, bcrypt for hashing, JWT for tokens) which reduces cognitive complexity. The state management is straightforward (stateless request/response). Overall, this is a moderate complexity task that requires careful attention to security and error handling but doesn't involve novel algorithms or architectures.

#### Effort (3/5 - Medium: 2-4 hours)
Estimated work breakdown:
- **Backend API endpoint:** 1 hour
  - Request/response types
  - Controller logic
  - Service layer integration
- **Validation & Security:** 45 minutes
  - Zod schema definition
  - Password strength rules
  - Bcrypt hashing configuration
- **Database Layer:** 30 minutes
  - User model updates
  - Duplicate email handling
- **Testing:** 1 hour
  - Unit tests for validation
  - Unit tests for service layer
  - Integration test for signup flow
  - Integration test for error cases
- **Documentation:** 30 minutes
  - API endpoint documentation
  - Security notes
- **Code review buffer:** 15 minutes

**Total estimated:** 3.5 hours (fits in Medium category)

#### Risk (+1 - Low Risk)
**Risks identified:**
1. **Library learning curve** - Team may need 15-30 minutes to understand Zod syntax if first time using
2. **Password policy** - Requirements might evolve during implementation (but AC is clear)
3. **Database constraints** - Ensuring unique email constraint at DB level

**Mitigation:**
- Zod documentation is excellent
- Password policy is clearly defined in AC
- Standard PostgreSQL unique constraint

**Overall:** Low risk with minor unknowns that won't significantly impact timeline.

#### Comparable Stories
**Similar past stories:**
- "User Login" - estimated 3 points, actual 3 points (similar complexity, less setup)
- "Password Reset" - estimated 5 points, actual 6 points (similar security concerns)

This story aligns with past authentication work, suggesting our estimate is reasonable.

#### Assumptions
1. PostgreSQL database already configured
2. JWT library already integrated
3. Team has basic understanding of authentication flows
4. Frontend form will be separate story (not included here)
5. Email verification will be separate story
6. Rate limiting will be separate story

#### Splitting Recommendation
**Do not split.** This story is well-sized at 5 points and represents a cohesive, deliverable feature. The acceptance criteria are well-defined and splitting would create awkward dependencies. If we were to split, we'd lose the value of a complete signup flow.

If team velocity is very low (<10 points/sprint), consider splitting into:
- Story A: Basic signup (email/password, no validation) - 2 points
- Story B: Add validation and security - 3 points

But this is not recommended as it delays delivering value.

---

## STEP 6: Update Story File with Estimation

### Actions
1. Read the current story file
2. Add or update estimation section
3. Add estimation metadata
4. Preserve all other content
5. Write updated file back

### Estimation Section Format
```markdown
## Estimation

**Story Points:** 5
**Confidence Level:** High (85%)
**Estimated Date:** 2025-01-15
**Estimator:** Alex (Planner)

### Breakdown
- **Complexity:** 3/5 (Moderate)
- **Effort:** 3/5 (Medium - 2-4 hours)
- **Risk:** +1 (Low Risk)
- **Formula:** (3 + 3) / 2 + 1 = 4 → rounds to 5

### Rationale
[Full rationale from Step 5]

### Comparable Stories
- User Login: 3 points
- Password Reset: 5 points

### Assumptions
1. PostgreSQL database already configured
2. JWT library already integrated
[etc.]
```

### Example Updated Story File
```markdown
# Story: User Signup with Email and Password

**ID:** story-auth-001-signup
**Epic:** User Authentication & Authorization
**Priority:** P0 (Must Have)
**Status:** Ready for Sprint

## User Story
As a new user,
I want to create an account with my email and password
So that I can access the application and save my data.

## Acceptance Criteria
- AC-1: User can enter email and password on signup form
- AC-2: Email must be valid format (validated with Zod)
- AC-3: Password must meet strength requirements (min 12 chars, uppercase, lowercase, number, special)
- AC-4: Password hashed with bcrypt (cost 12)
- AC-5: Duplicate emails rejected with 409 error
- AC-6: Success response returns JWT token
- AC-7: User record saved to PostgreSQL database

## Technical Notes
- Use Zod for validation
- Use bcrypt for password hashing (cost factor: 12)
- Use jsonwebtoken for JWT generation
- Store in PostgreSQL users table

## Dependencies
- None (foundational story)

## Estimation

**Story Points:** 5
**Confidence Level:** High (85%)
**Estimated Date:** 2025-01-15
**Estimator:** Alex (Planner)

### Breakdown
- **Complexity:** 3/5 (Moderate)
  - Multiple integration points (validation, auth, database)
  - Standard patterns with well-known libraries
  - Several error paths to handle

- **Effort:** 3/5 (Medium - 2-4 hours)
  - ~200 lines of code (backend + validation)
  - 5 tests (3 unit, 2 integration)
  - Moderate documentation needs

- **Risk:** +1 (Low Risk)
  - Clear requirements
  - Stable, mature dependencies
  - Minor learning curve for Zod

- **Formula:** (3 + 3) / 2 + 1 = 4 → rounds to 5

### Rationale
Standard authentication implementation with multiple integration points but well-established patterns. The complexity is moderate due to security considerations and error handling, but effort is contained (2-4 hours). Low risk due to clear requirements and mature libraries. Comparable to past auth stories that came in on estimate.

### Comparable Stories
- User Login: 3 points (actual 3 - similar but less setup)
- Password Reset: 5 points (actual 6 - similar security needs)

### Assumptions
1. PostgreSQL database already configured
2. JWT library already integrated
3. Team has basic understanding of auth flows
4. Frontend form is separate story
5. Email verification is separate story

## Sprint Assignment
- **Proposed Sprint:** Sprint 1
- **Sprint Theme:** Core Authentication
```

---

## STEP 7: Generate Estimation Report

### Report Structure
Create a comprehensive estimation report that can be:
- Shared with the team
- Referenced during sprint planning
- Used for velocity tracking
- Archived for future comparison

### Report Filename
```
.claude/estimations/{story-id}-estimate-{date}.md
```

Example: `.claude/estimations/story-auth-001-estimate-2025-01-15.md`

### Full Report Template

```markdown
# Story Estimation Report

**Story ID:** story-auth-001-signup
**Story Title:** User Signup with Email and Password
**Epic:** User Authentication & Authorization
**Estimation Date:** 2025-01-15
**Estimator:** Alex (Planner)

---

## Executive Summary

**Story Points:** 5
**Confidence:** High (85%)
**Recommendation:** Ready for sprint commitment
**Splitting:** Not recommended

This story represents a standard user signup implementation with email and password. The estimate of 5 points reflects moderate complexity due to multiple integration points (validation, authentication, database), medium effort (2-4 hours), and low risk due to clear requirements and mature libraries.

---

## Estimation Breakdown

### Complexity: 3/5 (Moderate)

**Factors:**
- 3 integration points (Zod validation, bcrypt hashing, PostgreSQL)
- 4 error paths (invalid email, weak password, duplicate email, DB error)
- Standard authentication patterns (well-established)
- Straightforward state management (request/response)
- No novel algorithms

**Analysis:**
The story involves careful coordination between validation, security, and data layers. While each component is straightforward, the integration and error handling add moderate complexity. The use of established libraries (Zod, bcrypt, jsonwebtoken) reduces complexity compared to custom implementations.

**Complexity Score:** 3/5

---

### Effort: 3/5 (Medium - 2-4 hours)

**Work Breakdown:**
| Task | Estimated Time |
|------|----------------|
| Backend API endpoint (controller + types) | 1h 0m |
| Validation schema (Zod) | 30m |
| Security implementation (bcrypt, JWT) | 15m |
| Service layer (business logic) | 30m |
| Database integration | 30m |
| Unit tests (3 tests) | 30m |
| Integration tests (2 tests) | 30m |
| API documentation | 20m |
| Security documentation | 10m |
| Code review buffer | 15m |
| **Total** | **3h 30m** |

**Lines of Code Estimate:** ~200 lines
- API endpoint: 50 lines
- Validation: 30 lines
- Service layer: 60 lines
- Database layer: 20 lines
- Tests: 40 lines

**Effort Score:** 3/5

---

### Risk: +1 (Low Risk)

**Risk Factors:**

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Zod learning curve | Low | Low | Excellent documentation |
| Password policy changes | Low | Medium | Clear AC, unlikely to change |
| Database constraint issues | Very Low | Low | Standard PostgreSQL patterns |
| Library version conflicts | Very Low | Low | Stable, mature libraries |

**Unknowns:**
- Team's familiarity with Zod (minor)
- Exact password complexity requirements (but AC is clear)

**Dependencies:**
- None (foundational feature)

**Technical Debt in Area:**
- None (new code)

**Risk Score:** +1 (Low Risk)

---

## Story Point Calculation

```
Base Score = (Complexity + Effort) / 2
           = (3 + 3) / 2
           = 3

Adjusted Score = Base Score + Risk
               = 3 + 1
               = 4

Story Points = Round to nearest Fibonacci
             = 5 (round 4 up to 5)
```

**Final Story Points:** 5

---

## Confidence Assessment

**Confidence Level:** High (85%)

**Confidence Factors:**

✅ **High Confidence:**
- Clear, specific acceptance criteria
- Well-documented libraries
- Standard authentication pattern
- No external dependencies
- Team has done similar work

⚠️ **Moderate Confidence:**
- First time using Zod (minor learning needed)
- Security considerations require careful attention

**Overall:** High confidence in this estimate. The story is well-defined with clear requirements and established patterns. Minor risk from library familiarity doesn't significantly impact confidence.

---

## Comparable Stories

### Historical Reference

| Story | Estimated | Actual | Variance | Notes |
|-------|-----------|--------|----------|-------|
| User Login (story-auth-002) | 3 | 3 | 0% | Similar pattern, less setup |
| Password Reset (story-auth-006) | 5 | 6 | +20% | Similar security needs, took longer due to email |
| OAuth Integration (story-auth-009) | 8 | 7 | -12% | More complex but well-documented |

**Analysis:** This story aligns with past authentication work. The 5-point estimate is consistent with similar stories. Password Reset took slightly longer due to email integration (not in scope here), suggesting our estimate may be conservative.

---

## Assumptions

**Technical Assumptions:**
1. PostgreSQL database is already configured
2. JWT library (jsonwebtoken) already integrated
3. Express/Fastify already set up
4. TypeScript configuration in place
5. Testing framework (Jest) configured

**Scope Assumptions:**
1. Frontend form is a separate story (story-auth-001-ui)
2. Email verification is a separate story (story-auth-004)
3. Rate limiting is a separate story (story-auth-008)
4. Password reset is a separate story (story-auth-006)
5. User profile management is separate

**Team Assumptions:**
1. Developer has basic understanding of authentication
2. Code review will be available same day
3. No major blockers or competing priorities

**Requirements Assumptions:**
1. Password complexity rules won't change during implementation
2. Acceptance criteria are complete and won't expand
3. No GDPR/compliance requirements beyond basic security

---

## Splitting Recommendation

**Recommendation:** DO NOT SPLIT

**Rationale:**
- Story is well-sized at 5 points (ideal sprint commitment size)
- Represents a cohesive, deliverable feature (complete signup flow)
- Acceptance criteria are tightly coupled
- Splitting would create awkward dependencies
- Delivers clear value as a single story

**If Splitting Were Required:**
If team velocity is very low (<10 points/sprint), could split into:

**Option A: Technical Layers**
- Story A: Basic signup endpoint (no validation) - 2 points
- Story B: Add validation and security - 3 points
⚠️ **Not recommended:** Story A has limited value without validation

**Option B: Feature Slicing**
- Story A: Signup with basic validation - 3 points
- Story B: Enhanced security (bcrypt, JWT) - 2 points
⚠️ **Not recommended:** Security should be in from the start

**Conclusion:** Keep as single 5-point story.

---

## Sprint Planning Notes

**Sprint Readiness:** ✅ Ready

**Pre-requisites:**
- None (foundational feature)

**Blocking Stories:**
- None

**Blocked Stories:**
- story-auth-002-login (depends on signup)
- story-auth-004-email-verification (depends on signup)
- story-profile-001 (depends on signup)

**Sprint Velocity Impact:**
- Occupies 5 points of sprint capacity
- Can be completed in 1 day by 1 developer
- Low risk of spillover

**Testing Requirements:**
- 3 unit tests
- 2 integration tests
- No E2E tests needed (frontend is separate)

**Documentation Requirements:**
- API endpoint documentation
- Security notes (password hashing, JWT)
- Code comments for security-critical sections

---

## Risk Mitigation Plan

### Risk 1: Zod Learning Curve
- **Mitigation:** Allocate 30 minutes for Zod documentation review
- **Fallback:** Use simpler validation library (validator.js) if needed
- **Owner:** Developer

### Risk 2: Password Policy Evolution
- **Mitigation:** Confirm password requirements with PO before starting
- **Fallback:** AC is clear, push back on scope creep
- **Owner:** Developer + PO

### Risk 3: Database Constraint Issues
- **Mitigation:** Review database schema before implementation
- **Fallback:** Standard PostgreSQL unique constraint patterns
- **Owner:** Developer

---

## Approval

**Status:** ✅ Approved for Sprint Planning

**Approved By:** Alex (Planner)
**Date:** 2025-01-15

**Notes:**
- Ready for sprint commitment
- No concerns or blockers
- Recommend prioritizing in Sprint 1 as foundational feature

---

## Metadata

```yaml
story_id: story-auth-001-signup
epic_id: epic-auth
story_points: 5
complexity: 3
effort: 3
risk: 1
confidence: 0.85
estimation_date: 2025-01-15
estimator: alex-planner
status: ready
splitting_recommended: false
sprint_ready: true
```

---

## Next Steps

1. ✅ Story estimated and documented
2. ⏭️ Add to sprint backlog for Sprint Planning
3. ⏭️ Confirm with team during planning session
4. ⏭️ Assign to developer during sprint
5. ⏭️ Track actual effort for velocity refinement

---

*Generated by: `.claude/skills/planning/estimate-stories.md` v1.0.0*
*Subagent: Alex (Planner)*
```

---

## STEP 8: Present Summary to User

### Summary Format
Present a concise summary to the user with key information:

```markdown
✅ Story Estimation Complete

**Story:** story-auth-001-signup - User Signup with Email and Password
**Story Points:** 5 (High confidence: 85%)

**Breakdown:**
- Complexity: 3/5 (Moderate - multiple integrations)
- Effort: 3/5 (Medium - 2-4 hours)
- Risk: +1 (Low - clear requirements)
- Formula: (3+3)/2+1 = 4 → 5 points

**Key Insights:**
- Standard auth implementation with well-established patterns
- Comparable to past stories (Login: 3pts, Password Reset: 5pts)
- Ready for sprint commitment
- No splitting recommended

**Files Updated:**
- `.claude/stories/story-auth-001-signup.md` (updated with estimation)
- `.claude/estimations/story-auth-001-estimate-2025-01-15.md` (detailed report)

**Next Steps:**
- Add to sprint backlog
- Confirm during sprint planning
- Can be completed in 1 day by 1 developer
```

### Batch Estimation Summary
When estimating multiple stories:

```markdown
✅ Batch Estimation Complete (3 stories)

| Story ID | Title | Points | Confidence |
|----------|-------|--------|------------|
| story-auth-001 | User Signup | 5 | High (85%) |
| story-auth-002 | User Login | 3 | High (90%) |
| story-auth-003 | Password Reset | 5 | Medium (75%) |

**Total Story Points:** 13
**Average Confidence:** 83%

**Sprint Impact:**
- Total: 13 points (fits in typical 20-point sprint with buffer)
- All stories are foundational auth features
- Logical sequencing: Signup → Login → Password Reset

**Recommendations:**
- All ready for sprint commitment
- Recommend Sprint 1 (core authentication)
- No splitting needed for any story

**Files Created:**
- 3 story files updated with estimations
- 3 detailed estimation reports in `.claude/estimations/`
```

---

## Error Handling

### Story File Not Found
```
❌ Error: Story file not found

Story ID: story-auth-001
Expected path: .claude/stories/story-auth-001-signup.md

Possible issues:
1. Story has not been created yet (run @alex *breakdown first)
2. Story ID is incorrect (check .claude/stories/ directory)
3. File was moved or deleted

Suggestions:
- List available stories: ls .claude/stories/
- Create story from epic: @alex *breakdown "<epic>"
- Check story ID format: story-{component}-{number}-{name}
```

### Invalid Story Format
```
❌ Error: Story file is missing required sections

Story ID: story-auth-001
Missing sections:
- User Story narrative
- Acceptance Criteria

This story cannot be accurately estimated without clear requirements.

Suggestions:
- Refine story with: @alex *refine story-auth-001
- Manually add missing sections to story file
- Re-generate from epic breakdown
```

### Ambiguous Requirements
```
⚠️ Warning: Low confidence estimation

Story ID: story-auth-001
Confidence: 45% (below 70% threshold)

Issues identified:
- Vague acceptance criteria
- Multiple technical unknowns
- High risk factors

Recommendations:
1. Refine story with PO/team to clarify requirements
2. Consider creating a technical spike (2-3 points)
3. Break down into smaller, clearer stories

Estimation provided, but NOT recommended for sprint commitment without refinement.
```

---

## Best Practices

### 1. Estimate Collaboratively (When Possible)
While this skill provides algorithmic estimation, the best estimates come from:
- **Team discussion** (Planning Poker)
- **Multiple perspectives** (developer + QA + architect)
- **Historical data** (past velocity)

Use this skill as:
- **Starting point** for team discussion
- **Consistency check** for team estimates
- **Quick estimate** for backlog refinement
- **Solo estimation** when needed

### 2. Use Historical Data
Track actual effort vs. estimated:
```yaml
story-auth-001:
  estimated: 5
  actual: 5
  variance: 0%
  notes: "Came in exactly on estimate"

story-auth-002:
  estimated: 3
  actual: 4
  variance: +33%
  notes: "Underestimated test complexity"
```

Adjust future estimates based on patterns.

### 3. Re-estimate When Needed
Re-estimate if:
- Requirements change significantly
- New dependencies discovered
- Technical approach changes
- Team discovers unknowns during refinement

Use: `@alex *estimate story-auth-001 --reason "Requirements updated"`

### 4. Watch for Estimation Smells
**Red Flags:**
- Story points > 13 (split it)
- Confidence < 70% (refine requirements)
- Risk = 3 (consider spike first)
- Effort = 5 (>8 hours, split it)
- Many assumptions (requirements unclear)

**Green Flags:**
- Story points 3-5 (sweet spot)
- Confidence > 80%
- Risk ≤ 1
- Clear, testable acceptance criteria
- Similar to past stories

### 5. Velocity Calibration
Over time, calibrate the estimation formula to your team:
- If consistently over-estimating, adjust complexity/effort weights
- If consistently under-estimating, increase risk adjustments
- Track variance and refine

---

## Integration with Other Skills

### Before Estimation
1. **@alex *breakdown** - Create stories from epic
   - Generates initial story files
   - Provides rough estimation
   - estimate-stories.md refines the estimate

2. **@alex *refine** - Refine vague stories
   - Clarifies requirements
   - Makes estimation more accurate
   - Reduces risk

### After Estimation
1. **@alex *sprint** - Create sprint plan
   - Uses story point estimates
   - Groups stories by velocity
   - Respects dependencies

2. **@alex *dependencies** - Analyze dependencies
   - Identifies blocking relationships
   - Helps with sprint sequencing

3. **@james *implement** - Execute story
   - Track actual effort vs. estimated
   - Update velocity data

### Workflow Example
```bash
# 1. Break down epic
@alex *breakdown "User Authentication System"

# 2. Estimate all stories
@alex *estimate story-auth-001 story-auth-002 story-auth-003

# 3. Plan sprint
@alex *sprint "Sprint 1" --velocity 20

# 4. Implement
@james *implement story-auth-001

# 5. Compare actual vs. estimate
# (automatic tracking)
```

---

## Configuration

### Estimation Weights (Advanced)
If your team finds estimates consistently off, you can adjust weights in `.claude/config.yaml`:

```yaml
estimation:
  complexity_weight: 0.5  # Default: 0.5 (equal weight)
  effort_weight: 0.5      # Default: 0.5 (equal weight)
  risk_adjustment: 1.0    # Default: 1.0 (linear)

  # Fibonacci rounding preference
  rounding: "conservative"  # Options: conservative (round up), aggressive (round down), nearest

  # Confidence thresholds
  confidence_high: 0.80
  confidence_medium: 0.60
  confidence_low: 0.60

  # Historical velocity tracking
  velocity_tracking: true
  velocity_window: 6  # sprints to average
```

### Team Calibration
After 2-3 sprints, review variance:

```bash
# Generate velocity report
@alex *velocity-report

# Output:
Sprint 1: Estimated 20, Actual 18 (-10%)
Sprint 2: Estimated 22, Actual 25 (+14%)
Sprint 3: Estimated 20, Actual 21 (+5%)

Average variance: +3%
Recommendation: Estimates are well-calibrated
```

---

## Skill Metadata

```yaml
skill_name: estimate-stories
version: 1.0.0
subagent: alex-planner
category: planning
execution_mode: sequential
halt_on_error: false

inputs:
  required:
    - story_id
  optional:
    - reason (for re-estimation)
    - batch (multiple story IDs)

outputs:
  - Updated story file with estimation
  - Detailed estimation report (.md)
  - Estimation metadata (.yaml)

dependencies:
  - breakdown-epic.md (creates stories to estimate)
  - refine-story.md (clarifies requirements)

integrations:
  - sprint-plan.md (uses story points)
  - GitHub MCP (story point labels)

execution_time: 2-5 minutes per story
```

---

## Examples

### Example 1: Simple Story
```bash
@alex *estimate story-ui-001-button-color
```

**Output:**
```
✅ Story Estimation Complete

Story: story-ui-001-button-color
Story Points: 1
Confidence: Very High (95%)

Breakdown:
- Complexity: 1/5 (Trivial - CSS change)
- Effort: 1/5 (Minimal - <1 hour)
- Risk: +0 (No risk)
- Formula: (1+1)/2+0 = 1

Files Updated:
- .claude/stories/story-ui-001-button-color.md
- .claude/estimations/story-ui-001-estimate-2025-01-15.md
```

### Example 2: Complex Story
```bash
@alex *estimate story-payment-001-stripe
```

**Output:**
```
✅ Story Estimation Complete

Story: story-payment-001-stripe
Story Points: 13
Confidence: Medium (70%)

Breakdown:
- Complexity: 5/5 (Very Complex - payment integration)
- Effort: 5/5 (Very High - >8 hours)
- Risk: +3 (High - security critical, first integration)
- Formula: (5+5)/2+3 = 8 → 13

⚠️ Recommendations:
- Consider technical spike first (3 points)
- Split into smaller stories if possible
- High risk due to payment handling

Files Updated:
- .claude/stories/story-payment-001-stripe.md
- .claude/estimations/story-payment-001-estimate-2025-01-15.md
```

### Example 3: Batch Estimation
```bash
@alex *estimate story-auth-001 story-auth-002 story-auth-003
```

**Output:**
```
✅ Batch Estimation Complete (3 stories)

| Story | Points | Confidence |
|-------|--------|------------|
| story-auth-001 (Signup) | 5 | High (85%) |
| story-auth-002 (Login) | 3 | High (90%) |
| story-auth-003 (Logout) | 1 | Very High (95%) |

Total: 9 story points
Average Confidence: 90%

All stories ready for sprint planning.
```

---

## Success Criteria

This skill is successful when:

✅ **Consistent Estimates**
- Similar stories get similar estimates
- Team agrees with estimates 80%+ of the time

✅ **Accurate Velocity**
- Actual effort matches estimated within ±20%
- Velocity becomes predictable after 3 sprints

✅ **Sprint Predictability**
- Team consistently completes committed points
- Few spillovers or under-commits

✅ **Clear Rationale**
- Estimates are understandable and defensible
- Team can discuss and adjust with clear reasoning

✅ **Fast Turnaround**
- Estimation takes 2-5 minutes per story
- No manual calculation errors

---

*This skill is part of the BMAD Enhanced Planning Suite.*
*For issues or improvements, see `.claude/skills/planning/README.md`*
