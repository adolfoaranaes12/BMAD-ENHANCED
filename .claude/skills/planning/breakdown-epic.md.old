# Skill: Epic Breakdown

## Metadata

**Skill Name:** breakdown-epic
**Version:** 1.0
**Category:** Planning
**Purpose:** Break down epics into implementable user stories with acceptance criteria, priorities, estimates, dependencies, and sprint groupings
**Output:** Multiple story files + epic summary + dependency graph

---

## Overview

This skill transforms high-level epics or features into detailed, actionable user stories ready for sprint planning and implementation.

**Key Capabilities:**
- Analyze epic scope and identify major components
- Create user stories in proper format (As a... I want... So that...)
- Define clear, testable acceptance criteria
- Estimate story points using complexity/effort/risk
- Identify dependencies between stories
- Suggest sprint groupings based on dependencies and priorities
- Generate story files and dependency visualization

**When to Use:**
- Starting new epic or major feature
- During backlog grooming sessions
- Planning multiple sprints ahead
- Breaking down product requirements

**Integration Points:**
- Can be followed by refine-story.md for individual story details
- Feeds into sprint-plan.md for sprint planning
- Stories feed into create-task-spec.md for implementation specs

---

## Execution Process

This skill executes **sequentially** through 7 steps.

### Halt Conditions
- Configuration file missing or invalid
- Epic description too vague (less than 20 words)
- Cannot create output directories

---

## Step 0: Load Configuration and Epic Description

**Purpose:** Load project configuration and parse epic requirements.

**Actions:**

1. **Load Project Configuration:**
   ```yaml
   # Read .claude/config.yaml
   planning:
     storiesLocation: .claude/stories
     epicsLocation: .claude/epics
     defaultVelocity: 40
     storyPointScale: [1, 2, 3, 5, 8, 13, 21]  # Fibonacci

   project:
     name: "My Project"
     type: greenfield | brownfield
     techStack: [Node.js, React, PostgreSQL, etc.]
   ```

2. **Get Epic Description:**
   - From user argument or prompt
   - Example: "User Authentication & Authorization with OAuth"
   - OR from epic file if already exists

3. **Parse Epic Scope:**
   ```markdown
   Epic: User Authentication & Authorization

   Description:
   Users need to be able to create accounts, log in, and manage their sessions.
   System should support email/password auth and OAuth (Google, GitHub).
   Admin users should have role-based access control.

   Business Goals:
   - Enable user accounts for personalization
   - Support SSO for enterprise users
   - Secure user data and prevent unauthorized access

   Technical Scope:
   - Authentication (signup, login, logout)
   - Authorization (roles, permissions)
   - Session management
   - OAuth integration
   - Password security
   ```

4. **Prepare Output Directories:**
   ```bash
   mkdir -p .claude/stories
   mkdir -p .claude/epics
   ```

**Halt If:**
- Config file missing
- Epic description < 20 words (too vague)
- Cannot create directories

**Output:**
```
✓ Configuration loaded
✓ Epic: User Authentication & Authorization
✓ Output directories ready
✓ Tech stack: Node.js, React, PostgreSQL
```

---

## Step 1: Analyze Epic Scope

**Purpose:** Break down the epic into major components and identify sub-features.

**Actions:**

1. **Identify Major Components:**
   From epic description, extract:
   - Core features (what functionality is needed?)
   - User types (who will use this?)
   - Technical requirements (what tech/integrations?)
   - Security requirements (what needs protection?)
   - Non-functional requirements (performance, scalability, etc.)

2. **Example Analysis:**
   ```markdown
   Epic: User Authentication & Authorization

   Major Components Identified:

   1. Authentication Flow
      - User signup (email + password)
      - User login (credential validation)
      - User logout (session termination)
      - Password reset (forgot password flow)
      - Email verification

   2. OAuth Integration
      - OAuth provider setup (Google, GitHub)
      - OAuth flow (redirect, callback, token exchange)
      - Account linking (existing user can add OAuth)

   3. Authorization & Access Control
      - User roles (admin, user, guest)
      - Permissions (CRUD operations per role)
      - Route protection (middleware)

   4. Session Management
      - JWT token generation
      - Token refresh
      - Session expiry
      - Multi-device support

   5. Security Features
      - Password hashing (bcrypt)
      - Rate limiting (prevent brute force)
      - CSRF protection
      - Secure token storage

   6. User Profile Management
      - View profile
      - Update profile
      - Delete account
   ```

3. **Identify User Personas:**
   ```markdown
   Primary Users:
   - End User (needs account to use app)
   - Admin User (needs elevated permissions)
   - Guest User (limited access, no account)
   ```

4. **Extract Technical Constraints:**
   ```markdown
   Technical Requirements:
   - Database: PostgreSQL (user table)
   - Auth: JWT tokens (24h expiry)
   - Password: bcrypt (cost factor 12)
   - Email: Nodemailer or SendGrid
   - OAuth: Google OAuth 2.0, GitHub OAuth
   - Session Storage: Redis (for token blacklist)
   ```

**Output:**
```
✓ Scope analyzed
✓ 6 major components identified
✓ 3 user personas defined
✓ Technical constraints documented
```

---

## Step 2: Create User Stories

**Purpose:** Generate user stories in proper format for each component.

**Actions:**

1. **User Story Template:**
   ```markdown
   **Title:** [Action] with [Method]

   **User Story:**
   As a [persona],
   I want to [action]
   So that [business value/benefit].

   **Acceptance Criteria:**
   - AC-1: [Specific, testable criterion]
   - AC-2: [Another criterion]
   - ...

   **Priority:** P0 (Must Have) | P1 (Should Have) | P2 (Nice to Have)

   **Story Points:** TBD (estimated in Step 3)

   **Dependencies:** [Other stories this depends on]

   **Technical Notes:** [Implementation hints, tech choices]
   ```

2. **Generate Stories for Each Component:**

**Example: Authentication Flow Component**

**Story 1: User Signup**
```markdown
**Title:** User Signup with Email and Password

**User Story:**
As a new user,
I want to create an account with my email and password
So that I can access the application and save my data.

**Acceptance Criteria:**
- AC-1: User can enter email and password on signup form
- AC-2: Email must be valid format (validated with Zod)
- AC-3: Password must be at least 8 characters with mixed case and number
- AC-4: Duplicate emails are rejected with 409 error
- AC-5: Password is hashed with bcrypt (cost 12) before storage
- AC-6: User account created in database with emailVerified: false
- AC-7: Verification email sent with secure token link
- AC-8: JWT token generated and returned in response

**Priority:** P0 (Must Have) - Foundation for all auth features

**Story Points:** TBD (Step 3)

**Dependencies:**
- None (foundational story)

**Technical Notes:**
- Database: Prisma User model with email, password, emailVerified fields
- Validation: Zod schema for email and password
- Hashing: bcrypt with cost factor 12
- Token: JWT with 24h expiry, include userId and role
- Email: Use Nodemailer with HTML template
- Error Handling: Return validation errors with field details

**Definition of Done:**
- [ ] API endpoint implemented (POST /api/auth/signup)
- [ ] Database migration created and run
- [ ] Unit tests for validation logic
- [ ] Integration tests for signup flow
- [ ] Email sending tested (use Mailtrap for dev)
- [ ] API documented in OpenAPI spec
- [ ] Security review passed (password hashing verified)
- [ ] Code reviewed and merged

**File:** .claude/stories/story-auth-001-signup.md
```

**Story 2: User Login**
```markdown
**Title:** User Login with Email and Password

**User Story:**
As a registered user,
I want to log in with my email and password
So that I can access my account and use the application.

**Acceptance Criteria:**
- AC-1: User can enter email and password on login form
- AC-2: Email is case-insensitive for lookup
- AC-3: Password is compared using bcrypt.compare()
- AC-4: Valid credentials return JWT token (24h expiry)
- AC-5: Invalid credentials return 401 "Invalid email or password"
- AC-6: After 5 failed attempts, account locked for 15 minutes
- AC-7: Successful login redirects to dashboard
- AC-8: Failed login attempt is logged for security audit

**Priority:** P0 (Must Have) - Core authentication

**Story Points:** TBD (Step 3)

**Dependencies:**
- story-auth-001-signup (User Signup) - Must complete first

**Technical Notes:**
- Endpoint: POST /api/auth/login
- Rate Limiting: 5 attempts per 15 minutes per IP (use Redis)
- Token: Same JWT format as signup
- Security: Log failed attempts to detect brute force
- Response: { user: { id, email, role }, token: string }

**Definition of Done:**
- [ ] API endpoint implemented (POST /api/auth/login)
- [ ] bcrypt password comparison working
- [ ] Rate limiting middleware implemented and tested
- [ ] Unit tests for login logic
- [ ] Integration tests including rate limit scenarios
- [ ] Failed login logging implemented
- [ ] API documented
- [ ] Security review passed

**File:** .claude/stories/story-auth-002-login.md
```

3. **Continue for All Components:**
   - Generate 1-3 stories per major component
   - Ensure each story is independently implementable
   - Keep stories small (ideally < 13 story points)
   - Split large stories into smaller ones

4. **Story Naming Convention:**
   ```
   story-<component>-<number>-<short-name>.md

   Examples:
   story-auth-001-signup.md
   story-auth-002-login.md
   story-auth-003-logout.md
   story-oauth-001-google.md
   story-rbac-001-roles.md
   ```

**Output:**
```
✓ 8 user stories created
✓ All stories have acceptance criteria
✓ All stories have priorities assigned
✓ Definition of done defined for each
```

---

## Step 3: Estimate Story Points

**Purpose:** Assign story points to each story using complexity, effort, and risk.

**Actions:**

1. **Story Point Estimation Formula:**
   ```
   Base Score = (Complexity + Effort) / 2
   Risk Adjustment = +0 to +3 (based on risk level)
   Story Points = Round to nearest Fibonacci number

   Complexity (1-5):
   1 = Trivial (copy-paste, config change)
   2 = Simple (CRUD, standard patterns)
   3 = Moderate (some logic, multiple components)
   4 = Complex (algorithms, integrations, edge cases)
   5 = Very Complex (novel solutions, high uncertainty)

   Effort (1-5):
   1 = < 1 hour
   2 = 1-2 hours
   3 = 2-4 hours
   4 = 4-8 hours
   5 = > 8 hours (consider splitting)

   Risk (0-3):
   0 = No risk (standard implementation)
   1 = Low risk (well-known tech, clear requirements)
   2 = Medium risk (new tech for team, some unknowns)
   3 = High risk (external dependencies, major unknowns)
   ```

2. **Example Estimations:**

**Story: User Signup**
```
Complexity: 3 (Moderate)
- Email/password validation (Zod schemas)
- Password hashing (bcrypt)
- Database insertion (Prisma)
- Email sending (Nodemailer)
- JWT generation
- Multiple components, some logic

Effort: 4 (4-8 hours)
- Prisma schema: 30 min
- Validation schemas: 30 min
- Signup endpoint: 2 hours
- Email template + sending: 1 hour
- Unit tests: 1-2 hours
- Integration tests: 1-2 hours
- Total: 6-8 hours

Risk: 1 (Low)
- Standard auth patterns
- Well-documented libraries
- Team has experience

Story Points:
Base = (3 + 4) / 2 = 3.5
Risk adjustment = +1
Total = 4.5 → Round to 5 story points
```

**Story: User Login**
```
Complexity: 2 (Simple)
- Email lookup (simple query)
- Password comparison (bcrypt.compare)
- JWT generation (reuse from signup)
- Standard login pattern

Effort: 3 (2-4 hours)
- Login endpoint: 1 hour
- Rate limiting: 1 hour
- Tests: 1-2 hours
- Total: 3-4 hours

Risk: 0 (No risk)
- Simple implementation
- No external dependencies
- Clear requirements

Story Points:
Base = (2 + 3) / 2 = 2.5
Risk adjustment = +0
Total = 2.5 → Round to 3 story points
```

**Story: OAuth Google Integration**
```
Complexity: 4 (Complex)
- OAuth flow (redirect, callback, token exchange)
- Multiple steps and error cases
- Profile data mapping
- Account linking logic

Effort: 4 (4-8 hours)
- OAuth provider setup: 1 hour
- Flow implementation: 3-4 hours
- Testing: 2 hours
- Edge cases: 1-2 hours
- Total: 7-9 hours

Risk: 2 (Medium)
- External dependency (Google OAuth)
- OAuth debugging can be tricky
- Need Google developer account

Story Points:
Base = (4 + 4) / 2 = 4
Risk adjustment = +2
Total = 6 → Round to 8 story points
```

3. **Assign Points to All Stories:**
   Update each story file with estimated points.

**Output:**
```
✓ All stories estimated
✓ Story point distribution:
  - 1-3 points: 3 stories (simple)
  - 5 points: 3 stories (moderate)
  - 8 points: 2 stories (complex)
✓ Total: 50 story points
```

---

## Step 4: Identify Dependencies

**Purpose:** Map dependencies between stories and create implementation order.

**Actions:**

1. **Dependency Types:**
   - **Hard Dependency:** Story B cannot start until Story A is complete
   - **Soft Dependency:** Story B is easier if Story A is done first
   - **Parallel:** Stories can be done simultaneously
   - **Blocking:** Story A blocks multiple other stories

2. **Analyze Each Story:**
   For each story, ask:
   - What must exist before this can be implemented?
   - What does this story enable/unblock?
   - Can this be done in parallel with others?

3. **Example Dependency Mapping:**

```markdown
Dependency Analysis:

story-auth-001-signup (User Signup)
  Depends on: NONE (foundational)
  Blocks:
    - story-auth-002-login (needs user accounts to exist)
    - story-auth-006-password-reset (needs user model)
    - story-auth-010-email-verification (needs signup flow)
    - story-oauth-001-google (needs user model)
  Can be done in parallel with: NONE (must be first)

story-auth-002-login (User Login)
  Depends on: story-auth-001-signup (HARD)
  Blocks:
    - story-auth-003-logout (needs login to test)
    - story-auth-007-session-mgmt (needs JWT tokens)
    - story-auth-008-rate-limiting (applies to login)
    - story-rbac-001-roles (needs authentication)
  Can be done in parallel with:
    - story-auth-006-password-reset (independent flows)
    - story-auth-010-email-verification (independent flows)

story-auth-003-logout (User Logout)
  Depends on: story-auth-002-login (HARD)
  Blocks: NONE
  Can be done in parallel with:
    - story-auth-007-session-mgmt
    - story-auth-008-rate-limiting

story-auth-006-password-reset (Password Reset)
  Depends on: story-auth-001-signup (SOFT - needs user model)
  Blocks: NONE
  Can be done in parallel with:
    - story-auth-002-login
    - story-auth-010-email-verification

story-auth-007-session-mgmt (Session Management)
  Depends on: story-auth-002-login (HARD - needs JWT implementation)
  Blocks: NONE
  Can be done in parallel with:
    - story-auth-003-logout
    - story-auth-008-rate-limiting

story-auth-008-rate-limiting (Rate Limiting)
  Depends on: story-auth-002-login (SOFT - applies to login, but can be built standalone)
  Blocks: NONE
  Can be done in parallel with:
    - story-auth-003-logout
    - story-auth-007-session-mgmt

story-auth-010-email-verification (Email Verification)
  Depends on: story-auth-001-signup (HARD - needs signup flow)
  Blocks: NONE
  Can be done in parallel with:
    - story-auth-002-login
    - story-auth-006-password-reset

story-oauth-001-google (OAuth Google)
  Depends on:
    - story-auth-001-signup (HARD - needs user model)
    - story-auth-002-login (SOFT - should exist for testing)
  Blocks:
    - story-oauth-002-github (similar pattern)
  Can be done in parallel with:
    - story-auth-007-session-mgmt
    - story-rbac-001-roles

story-oauth-002-github (OAuth GitHub)
  Depends on: story-oauth-001-google (SOFT - reuse patterns)
  Blocks: NONE
  Can be done in parallel with: Most other stories

story-rbac-001-roles (Role-Based Access Control)
  Depends on:
    - story-auth-001-signup (HARD - needs user model)
    - story-auth-002-login (HARD - needs authentication)
  Blocks: NONE (this is usually a later feature)
  Can be done in parallel with:
    - story-oauth-001-google
    - story-oauth-002-github
```

4. **Create Dependency Graph:**
   ```
   START
     ↓
   story-auth-001 (Signup) [5 pts]
     ↓
     ├─→ story-auth-002 (Login) [3 pts]
     │      ↓
     │      ├─→ story-auth-003 (Logout) [2 pts]
     │      ├─→ story-auth-007 (Session Mgmt) [8 pts]
     │      ├─→ story-auth-008 (Rate Limiting) [3 pts]
     │      ├─→ story-oauth-001 (Google) [8 pts]
     │      │      ↓
     │      │      └─→ story-oauth-002 (GitHub) [5 pts]
     │      └─→ story-rbac-001 (RBAC) [13 pts]
     │
     ├─→ story-auth-006 (Password Reset) [5 pts]
     └─→ story-auth-010 (Email Verification) [8 pts]

   Critical Path: Signup → Login → OAuth → RBAC
   Total Points on Critical Path: 29 points
   ```

5. **Identify Implementation Waves:**
   ```markdown
   Wave 1 (Must do first):
   - story-auth-001-signup (5 pts)
   Total: 5 points

   Wave 2 (After Wave 1):
   - story-auth-002-login (3 pts)
   - story-auth-006-password-reset (5 pts) [parallel]
   - story-auth-010-email-verification (8 pts) [parallel]
   Total: 16 points

   Wave 3 (After Wave 2):
   - story-auth-003-logout (2 pts)
   - story-auth-007-session-mgmt (8 pts) [parallel]
   - story-auth-008-rate-limiting (3 pts) [parallel]
   Total: 13 points

   Wave 4 (After Wave 2):
   - story-oauth-001-google (8 pts)
   Total: 8 points

   Wave 5 (After Wave 4):
   - story-oauth-002-github (5 pts)
   - story-rbac-001-roles (13 pts) [parallel, but large]
   Total: 18 points
   ```

**Output:**
```
✓ Dependencies mapped for all stories
✓ Critical path identified (29 points)
✓ 5 implementation waves defined
✓ No circular dependencies found
```

---

## Step 5: Suggest Sprint Groupings

**Purpose:** Group stories into recommended sprints based on dependencies, priorities, and typical velocity.

**Actions:**

1. **Sprint Planning Rules:**
   - Assume velocity from config (default: 40 points)
   - Group by dependencies (don't split dependent stories)
   - Balance sprint load (aim for 90-95% capacity)
   - Prioritize P0 stories first
   - Keep related stories together

2. **Example Sprint Groupings:**

```markdown
Recommended Sprint Plan:

Sprint 1: Foundation (Authentication Core)
Goal: Deliver basic authentication (signup, login, password reset)

Stories:
- story-auth-001-signup (5 pts, P0)
- story-auth-002-login (3 pts, P0)
- story-auth-006-password-reset (5 pts, P1)
- story-auth-008-rate-limiting (3 pts, P0)

Total: 16 points (40% capacity)
Duration: ~1 week
Rationale: Core auth foundation, enables all other work

---

Sprint 2: Security & Enhanced Auth
Goal: Add email verification, session management, and security controls

Stories:
- story-auth-010-email-verification (8 pts, P1)
- story-auth-007-session-mgmt (8 pts, P1)
- story-auth-003-logout (2 pts, P1)

Total: 18 points (45% capacity)
Duration: ~1 week
Dependencies: Sprint 1 complete

---

Sprint 3: OAuth Integration
Goal: Add social login (Google, GitHub)

Stories:
- story-oauth-001-google (8 pts, P1)
- story-oauth-002-github (5 pts, P2)

Total: 13 points (33% capacity)
Duration: ~3-4 days
Dependencies: Sprint 1 complete (user model exists)
Note: Can work in parallel with Sprint 2 after Sprint 1

---

Sprint 4: Authorization (RBAC)
Goal: Implement role-based access control

Stories:
- story-rbac-001-roles (13 pts, P1)

Total: 13 points (33% capacity)
Duration: ~3-4 days
Dependencies: Sprint 1 complete
Note: Large story, consider breaking down further or pairing

---

Total Epic:
- 4 sprints
- 60 story points (updated after adding stories)
- 8-10 weeks estimated (with testing, reviews, deployment)
- Can be compressed with parallel work on Sprints 2 & 3
```

3. **Alternative: Aggressive Timeline:**
   ```markdown
   Aggressive Sprint Plan (if needed):

   Sprint 1 (Week 1-2):
   - All of original Sprint 1 + Sprint 2
   - Total: 34 points (85% capacity with 40-point velocity)
   - Risky but achievable with focused team

   Sprint 2 (Week 3):
   - OAuth Google + GitHub
   - Total: 13 points
   - Can start after Sprint 1 Week 1 (signup/login done)

   Sprint 3 (Week 4):
   - RBAC
   - Total: 13 points

   Total: 3 sprints, 4 weeks (vs 4 sprints, 8-10 weeks)
   ```

**Output:**
```
✓ Sprint groupings suggested
✓ Recommended: 4 sprints, 8-10 weeks
✓ Aggressive option: 3 sprints, 4 weeks
✓ All dependencies satisfied within sprint boundaries
```

---

## Step 6: Generate Story Files and Epic Summary

**Purpose:** Create all story files and epic summary documentation.

**Actions:**

1. **Generate Individual Story Files:**
   For each story, create file at `.claude/stories/story-{component}-{number}-{name}.md`

2. **Story File Format:**
   ```markdown
   # Story: [Title]

   **Story ID:** story-auth-001
   **Epic:** User Authentication & Authorization
   **Priority:** P0 (Must Have)
   **Story Points:** 5
   **Status:** Ready for Development

   ## User Story

   As a [persona],
   I want to [action]
   So that [benefit].

   ## Acceptance Criteria

   - AC-1: [Criterion 1]
   - AC-2: [Criterion 2]
   ...

   ## Dependencies

   **Depends On:**
   - None (or list of story IDs)

   **Blocks:**
   - story-auth-002 (User Login)
   - story-auth-006 (Password Reset)

   ## Technical Notes

   [Implementation hints, tech choices, references]

   ## Definition of Done

   - [ ] Implementation complete
   - [ ] Unit tests written and passing
   - [ ] Integration tests written and passing
   - [ ] API documented
   - [ ] Code reviewed
   - [ ] Merged to main

   ## Estimation Details

   **Complexity:** 3/5 (Moderate)
   **Effort:** 4/5 (4-8 hours)
   **Risk:** 1/3 (Low)
   **Total:** 5 story points

   ## Related Documents

   - Epic: .claude/epics/epic-auth.md
   - Architecture: docs/architecture.md
   - API Design: docs/api-design.md
   ```

3. **Generate Epic Summary:**
   Create `.claude/epics/epic-auth.md`:

   ```markdown
   # Epic: User Authentication & Authorization

   **Epic ID:** epic-auth
   **Status:** Planning Complete
   **Total Story Points:** 60
   **Estimated Duration:** 4 sprints (8-10 weeks)

   ## Epic Description

   Users need to be able to create accounts, log in, and manage their sessions.
   System should support email/password auth and OAuth (Google, GitHub).
   Admin users should have role-based access control.

   ## Business Goals

   - Enable user accounts for personalization
   - Support SSO for enterprise users
   - Secure user data and prevent unauthorized access

   ## Stories Breakdown

   **Total Stories:** 10
   **By Priority:**
   - P0 (Must Have): 4 stories (16 points)
   - P1 (Should Have): 5 stories (39 points)
   - P2 (Nice to Have): 1 story (5 points)

   **By Component:**
   - Authentication: 6 stories (34 points)
   - OAuth: 2 stories (13 points)
   - Authorization: 1 story (13 points)

   ## Sprint Plan

   [Include sprint groupings from Step 5]

   ## Dependency Graph

   [Include ASCII dependency graph from Step 4]

   ## Risk Assessment

   **High Risk:**
   - OAuth integration depends on external services (mitigation: test thoroughly)

   **Medium Risk:**
   - RBAC is large story (13 points) - consider breaking down further

   **Low Risk:**
   - Core auth is standard implementation

   ## Related Documents

   - Stories: .claude/stories/story-auth-*.md
   - Architecture: docs/architecture.md
   - Sprint Plans: .claude/sprints/sprint-15-plan.md (when created)
   ```

4. **Generate Dependency Graph Visualization:**
   Create `.claude/epics/epic-auth-dependencies.md`:

   ```markdown
   # Dependency Graph: User Authentication Epic

   [Include detailed dependency graph from Step 4]

   ## Critical Path

   Signup → Login → OAuth Google → GitHub → RBAC
   Total: 29 points

   ## Parallelization Opportunities

   After Signup complete:
   - Login + Password Reset + Email Verification (parallel)

   After Login complete:
   - Logout + Session Mgmt + Rate Limiting (parallel)

   ## Implementation Order Recommendation

   Wave 1: Signup (5 pts)
   Wave 2: Login, Password Reset, Email Verification (16 pts total, can parallelize)
   Wave 3: Logout, Session Mgmt, Rate Limiting (13 pts total, can parallelize)
   Wave 4: OAuth Google (8 pts)
   Wave 5: OAuth GitHub, RBAC (18 pts total, can parallelize)
   ```

**Output:**
```
✓ 10 story files created (.claude/stories/)
✓ Epic summary created (.claude/epics/epic-auth.md)
✓ Dependency graph created (.claude/epics/epic-auth-dependencies.md)
```

---

## Step 7: Present Summary to User

**Purpose:** Provide concise summary with key information and next steps.

**Actions:**

1. **Display Summary:**
   ```
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   Epic Breakdown Complete
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   Epic: User Authentication & Authorization

   📊 Summary:
   ├─ Total Stories: 10
   ├─ Total Story Points: 60
   ├─ Estimated Duration: 4 sprints (8-10 weeks)
   └─ Status: Ready for sprint planning

   📋 Stories by Priority:
   ├─ P0 (Must Have): 4 stories (16 points)
   ├─ P1 (Should Have): 5 stories (39 points)
   └─ P2 (Nice to Have): 1 story (5 points)

   📦 Stories by Component:
   ├─ Authentication: 6 stories (34 points)
   ├─ OAuth: 2 stories (13 points)
   └─ Authorization: 1 story (13 points)

   🎯 Recommended Sprint Plan:

   Sprint 1: Foundation (16 points, ~1 week)
   - User Signup (5 pts)
   - User Login (3 pts)
   - Password Reset (5 pts)
   - Rate Limiting (3 pts)

   Sprint 2: Enhanced Auth (18 points, ~1 week)
   - Email Verification (8 pts)
   - Session Management (8 pts)
   - Logout (2 pts)

   Sprint 3: OAuth (13 points, ~3-4 days)
   - OAuth Google (8 pts)
   - OAuth GitHub (5 pts)

   Sprint 4: Authorization (13 points, ~3-4 days)
   - RBAC (13 pts)

   📁 Files Generated:
   ├─ Stories: .claude/stories/story-auth-*.md (10 files)
   ├─ Epic Summary: .claude/epics/epic-auth.md
   └─ Dependencies: .claude/epics/epic-auth-dependencies.md

   🔗 Dependencies:
   ├─ Critical Path: Signup → Login → OAuth → RBAC (29 points)
   ├─ Parallel Opportunities: Yes (after Signup, can parallelize)
   └─ No Circular Dependencies: ✓

   ⚠️  Risks:
   ├─ OAuth depends on external services (test thoroughly)
   └─ RBAC is large (13 pts) - consider breaking down

   💡 Next Steps:
   1. Review stories with Product Owner for priorities
   2. Start Sprint 1: @alex *sprint "Sprint 15" --velocity 40
   3. Or refine individual stories: @alex *refine story-auth-001
   4. Or create task specs: @alex *plan story-auth-001

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   ```

2. **Ask User for Next Action:**
   ```
   What would you like to do next?

   A) Start sprint planning for Sprint 1
   B) Refine specific stories for more detail
   C) Create task specifications for immediate implementation
   D) Review and adjust story priorities
   E) View dependency graph in detail
   ```

**Execution Complete.**

---

## Best Practices

1. **Story Size:** Keep stories ≤13 points (if larger, break down)
2. **Dependencies:** Always identify before sprint planning
3. **Priorities:** Align with business value and technical dependencies
4. **Acceptance Criteria:** Make them specific, testable, and complete
5. **Technical Notes:** Include enough detail for developers
6. **Estimation:** Use team's historical velocity as reference

---

## Integration with Other Skills

### Followed By:

**refine-story.md:**
```
Epic breakdown done, but story-auth-005 needs more detail.
Use: @alex *refine story-auth-005
```

**sprint-plan.md:**
```
Epic broken down into 10 stories. Ready for sprint planning.
Use: @alex *sprint "Sprint 15" --velocity 40
```

**create-task-spec.md:**
```
Story ready for implementation.
Use: @alex *plan story-auth-001
```

---

## Version History

**Version 1.0** (2025-10-28)
- Initial skill implementation
- 7-step sequential execution
- Epic → Stories → Dependencies → Sprint groupings
- Story point estimation
- File generation

---

<!-- End of Skill -->
