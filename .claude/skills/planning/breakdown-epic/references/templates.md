# Breakdown Epic Templates

This file contains all templates, output formats, and examples for the breakdown-epic skill.

---

## Configuration Format

Expected configuration in `.claude/config.yaml`:

```yaml
planning:
  storiesLocation: .claude/stories
  epicsLocation: .claude/epics
  defaultVelocity: 40  # story points per sprint
  storyPointScale: [1, 2, 3, 5, 8, 13, 21]  # Fibonacci

project:
  techStack:
    - Node.js
    - TypeScript
    - PostgreSQL
    - React
```

---

## Step 0: Configuration Loading

### Bash Command for Config Loading

```bash
python .claude/skills/bmad-commands/scripts/read_file.py \
  --path .claude/config.yaml \
  --output json
```

### Directory Preparation

```bash
mkdir -p {storiesLocation}
mkdir -p {epicsLocation}
```

---

## Step 1: Epic Analysis Example

Complete epic analysis with all components:

```markdown
Epic: User Authentication & Authorization

**Business Goal:** Enable secure user access with multiple auth methods

**Target Users:**
- New users (signup/registration)
- Returning users (login)
- OAuth users (social login)
- Administrators (user management)

## Major Components

### 1. Authentication Flow (Core)
**Sub-features:**
- User signup (email + password)
- User login (credential validation)
- User logout (session termination)
- Password reset (forgot password flow)
- Email verification (account activation)

**Technical Requirements:**
- Password hashing (bcrypt)
- JWT token generation
- Email service integration (SendGrid/Mailgun)
- Rate limiting (prevent brute force)

**Security Requirements:**
- Password strength validation
- SQL injection prevention
- XSS protection
- CSRF tokens

### 2. OAuth Integration (Enhancement)
**Sub-features:**
- OAuth provider setup (Google, GitHub)
- OAuth flow (redirect, callback, token exchange)
- Account linking (connect OAuth to existing account)
- Profile data sync

**Technical Requirements:**
- OAuth 2.0 client libraries
- Provider API integration
- Secure token storage
- Callback URL management

### 3. Authorization & RBAC (Security)
**Sub-features:**
- User roles (admin, user, guest)
- Permission system (granular access control)
- Role-based access control
- Permission middleware

**Technical Requirements:**
- Role database schema
- Permission checking middleware
- Admin management UI

### 4. Session Management (Infrastructure)
**Sub-features:**
- JWT token generation
- Token refresh mechanism
- Session expiration handling
- Multi-device support

**Technical Requirements:**
- JWT library
- Redis for session storage
- Token blacklisting (logout)

## Non-Functional Requirements

**Performance:**
- Login response time <500ms
- Signup response time <1s
- Support 1000 concurrent users

**Scalability:**
- Horizontal scaling for auth service
- Stateless authentication (JWT)

**Reliability:**
- 99.9% uptime for auth endpoints
- Graceful degradation if OAuth providers down

## Complexity Assessment

- **Total Sub-features:** 15-20
- **Estimated Stories:** 10-15
- **Estimated Story Points:** 60-90
- **Estimated Duration:** 2-3 sprints
```

---

## Step 2: User Story Format

### Standard Story Template

```markdown
## Story Title

**As a** [user type],
**I want** [capability],
**So that** [benefit]

**Acceptance Criteria:**
1. [Specific, testable criterion]
2. [Specific, testable criterion]
3. [Specific, testable criterion]

**Priority:** P0 | P1 | P2 | P3

**Component:** [Feature area]
```

### Complete Story Examples

#### Example 1: User Signup (Detailed)

```markdown
**Story 1: User Signup**

**As a** new user,
**I want to** create an account with email and password,
**So that** I can access personalized features and save my preferences.

**Acceptance Criteria:**
1. User can signup with valid email (RFC 5322 format)
2. Password requirements enforced (min 8 chars, 1 uppercase, 1 number, 1 special char)
3. Duplicate emails prevented (409 Conflict error with clear message)
4. Confirmation email sent immediately after registration
5. User account created in "unverified" state until email confirmed
6. Rate limiting applied (max 5 signup attempts per IP per hour)

**Priority:** P0 (Must Have)
**Component:** Authentication
**Estimate:** 8 story points
```

#### Example 2: User Login

```markdown
**Story 2: User Login**

**As a** registered user,
**I want to** log in with my credentials,
**So that** I can access my account and protected resources.

**Acceptance Criteria:**
1. User can login with email and password
2. Invalid credentials return 401 Unauthorized with generic message
3. JWT token generated on successful login (1 hour expiration)
4. Token includes user ID, email, and role claims
5. Rate limiting applied (5 attempts per minute per IP)
6. Account lockout after 10 failed attempts (30 min cooldown)

**Priority:** P0 (Must Have)
**Component:** Authentication
**Estimate:** 5 story points
```

#### Example 3: Password Reset

```markdown
**Story 3: Password Reset**

**As a** registered user who forgot their password,
**I want to** reset my password via email,
**So that** I can regain access to my account.

**Acceptance Criteria:**
1. User can request password reset with email address
2. Reset token sent to email (expires in 1 hour)
3. Token is cryptographically secure (random 32 bytes)
4. Reset link directs to password reset form
5. New password validated (same requirements as signup)
6. Old password invalidated immediately after reset
7. Confirmation email sent after successful reset

**Priority:** P1 (Should Have)
**Component:** Authentication
**Estimate:** 8 story points
```

#### Example 4: OAuth Login (Google)

```markdown
**Story 4: OAuth Login with Google**

**As a** user,
**I want to** log in using my Google account,
**So that** I don't need to remember another password.

**Acceptance Criteria:**
1. "Sign in with Google" button displayed on login page
2. OAuth flow redirects to Google authorization page
3. User grants permissions (email, profile)
4. Callback receives authorization code and exchanges for access token
5. User profile created/updated with Google data (email, name, avatar)
6. JWT token generated with user ID and role
7. User redirected to dashboard after successful login

**Priority:** P1 (Should Have)
**Component:** OAuth Integration
**Estimate:** 8 story points
```

#### Example 5: Role-Based Access Control

```markdown
**Story 5: Role-Based Access Control (RBAC)**

**As an** administrator,
**I want to** assign roles to users,
**So that** I can control access to different features.

**Acceptance Criteria:**
1. Roles table created in database (admin, user, guest)
2. Permissions table created (read, write, delete, admin)
3. User-role association created (many-to-many)
4. Middleware checks user role before protected routes
5. API endpoints return 403 Forbidden for insufficient permissions
6. Admin UI displays user roles and allows assignment

**Priority:** P1 (Should Have)
**Component:** Authorization
**Estimate:** 13 story points
```

---

## Step 3: Estimation Factors Template

### Detailed Estimation Breakdown

**Complexity (1-5):**
```
1 - Trivial
    - Simple CRUD operation
    - No business logic
    - Straightforward implementation
    Example: Basic getter/setter API

2 - Simple
    - Basic validation logic
    - Simple database query
    - Minimal integration
    Example: User profile update

3 - Moderate
    - Multiple components involved
    - Some business logic
    - Standard patterns apply
    Example: User signup with email validation

4 - Complex
    - Many integrations required
    - Complex business logic
    - Multiple edge cases
    Example: OAuth integration with profile sync

5 - Very Complex
    - Novel implementation required
    - High uncertainty
    - Many unknowns
    Example: Custom encryption algorithm
```

**Effort (1-5):**
```
1 - Minimal (<2 hours)
    - Trivial implementation
    - No tests needed
    Example: Add simple field to model

2 - Low (2-4 hours)
    - Half day effort
    - Basic tests
    Example: Simple validation endpoint

3 - Medium (4-8 hours)
    - Full day effort
    - Comprehensive tests
    Example: User login with JWT

4 - High (8-16 hours)
    - 1-2 days
    - Integration tests
    - Documentation
    Example: Password reset flow

5 - Very High (16+ hours)
    - 2+ days
    - E2E tests
    - Complex testing
    Example: OAuth integration with multiple providers
```

**Risk (1-3):**
```
1 - Low Risk
    - Well-known implementation
    - Team has experience
    - Clear requirements
    Example: Standard REST API

2 - Medium Risk
    - Some unknowns
    - Limited team experience
    - External dependencies
    Example: Email service integration

3 - High Risk
    - Many unknowns
    - No team experience
    - Complex dependencies
    - Unclear requirements
    Example: New payment gateway integration
```

### Calculation Examples

**Example 1: User Signup**
```
- Complexity: 3/5 (Moderate - validation, hashing, email)
- Effort: 4/5 (8-16 hours - model, service, API, tests, email)
- Risk: 1/3 (Low - standard auth pattern)
- Total: 3 + 4 + 1 = 8
- Story Points: 8 (exact Fibonacci match)
```

**Example 2: Simple Profile Update**
```
- Complexity: 2/5 (Simple - basic update logic)
- Effort: 2/5 (2-4 hours - API + tests)
- Risk: 1/3 (Low - straightforward)
- Total: 2 + 2 + 1 = 5
- Story Points: 5 (exact Fibonacci match)
```

**Example 3: OAuth Integration**
```
- Complexity: 4/5 (Complex - OAuth flow, token exchange, profile sync)
- Effort: 4/5 (8-16 hours - provider setup, callback, linking)
- Risk: 2/3 (Medium - external dependency, token handling)
- Total: 4 + 4 + 2 = 10
- Story Points: 8 (round down to nearest Fibonacci)
```

---

## Step 4: Dependency Examples

### Dependency Graph Format

```markdown
Dependencies for User Auth Epic:

story-auth-001 (User Signup) [8 points]
  ├─ BLOCKS story-auth-003 (Email Verification) [5 points]
  ├─ BLOCKS story-auth-002 (User Login) [5 points]
  └─ BLOCKS story-auth-009 (RBAC System) [13 points]

story-auth-002 (User Login) [5 points]
  ├─ BLOCKS story-auth-006 (Password Reset) [8 points]
  └─ BLOCKS story-auth-004 (JWT Sessions) [5 points]

story-auth-004 (JWT Sessions) [5 points]
  └─ BLOCKS story-auth-005 (Token Refresh) [8 points]

story-auth-007 (OAuth Setup) [8 points]
  └─ BLOCKS story-auth-008 (OAuth Login) [5 points]

story-auth-008 (OAuth Login) [5 points]
  └─ RELATED story-auth-010 (Account Linking) [5 points]

story-auth-009 (RBAC System) [13 points]
  ├─ REQUIRES story-auth-001 (User Signup)
  └─ REQUIRES story-auth-002 (User Login)

story-auth-011 (Multi-factor Auth) [13 points]
  ├─ REQUIRES story-auth-002 (User Login)
  └─ RELATED story-auth-005 (Token Refresh)
```

### Dependency Type Definitions

**BLOCKS:**
```
Story A BLOCKS Story B means:
- Story A must be 100% complete before Story B can start
- B cannot be implemented without A's functionality
- Typically: Foundation → Feature relationship

Example:
story-auth-001 (User Signup) BLOCKS story-auth-002 (User Login)
Reason: Login requires existing user accounts
```

**REQUIRES:**
```
Story A REQUIRES Story B means:
- Story A needs Story B's functionality
- Same as BLOCKS but from A's perspective
- Used for readability in dependency documentation

Example:
story-auth-009 (RBAC) REQUIRES story-auth-001 (Signup)
Reason: RBAC assigns roles to existing users
```

**RELATED:**
```
Story A RELATED Story B means:
- Stories share components or context
- Can be implemented in parallel
- Often benefit from coordination
- Not strict dependency

Example:
story-auth-002 (Login) RELATED story-auth-001 (Signup)
Reason: Both use authentication service, share code
```

---

## Step 5: Sprint Grouping Example

Complete sprint plan with reasoning:

```markdown
Sprint Planning for User Auth Epic

**Team Velocity:** 40 story points per sprint (2 weeks)
**Sprint Duration:** 2 weeks
**Total Stories:** 11
**Total Points:** 87 story points
**Estimated Duration:** 3 sprints (6 weeks)

---

### Sprint 1: Foundation (38 points)

**Goal:** Core authentication functionality

**Stories:**
1. story-auth-001: User Signup (8 points) [P0]
   - Foundation for all auth features
   - Must complete first (blocks login, verification)

2. story-auth-002: User Login (5 points) [P0]
   - Depends on: story-auth-001
   - Critical path item

3. story-auth-004: JWT Sessions (5 points) [P0]
   - Depends on: story-auth-002
   - Needed for stateless auth

4. story-auth-003: Email Verification (5 points) [P1]
   - Depends on: story-auth-001
   - Enhances security

5. story-auth-006: Password Reset (8 points) [P1]
   - Depends on: story-auth-002
   - User convenience feature

6. story-auth-011: Rate Limiting (7 points) [P1]
   - Independent work (parallel)
   - Security enhancement

**Dependency Check:** ✓ All dependencies satisfied within sprint
**Risk Assessment:** Low - standard patterns, no external blockers

---

### Sprint 2: Enhancement (40 points)

**Goal:** OAuth integration and session management

**Stories:**
1. story-auth-007: OAuth Setup (8 points) [P1]
   - Independent work (parallel with others)
   - Foundation for OAuth login

2. story-auth-008: OAuth Login (Google) (5 points) [P1]
   - Depends on: story-auth-007
   - Primary OAuth provider

3. story-auth-005: Token Refresh (8 points) [P1]
   - Depends on: story-auth-004 (completed in Sprint 1)
   - Improves UX

4. story-auth-009: RBAC System (13 points) [P1]
   - Depends on: story-auth-001, story-auth-002 (both completed)
   - Major feature, assigned to senior developer

5. story-auth-010: Account Linking (6 points) [P2]
   - Depends on: story-auth-008
   - Nice-to-have feature

**Dependency Check:** ✓ All dependencies satisfied from Sprint 1
**Risk Assessment:** Medium - OAuth has external dependency

---

### Sprint 3: Advanced Features (9 points)

**Goal:** Multi-factor auth and polish

**Stories:**
1. story-auth-012: Multi-Factor Auth (13 points) [P2]
   - Depends on: story-auth-002, story-auth-005
   - Security enhancement
   - Complex implementation

**NOTE:** Sprint 3 under-capacity (9/40 points)
**Options:**
- Pull in story-auth-010 from Sprint 2 (6 points) → 15 points
- Add polish/bug fix stories
- Add admin UI stories (4-8 points each)
- Start next epic (progressive delivery)

**Dependency Check:** ✓ All dependencies satisfied
**Risk Assessment:** Medium - MFA is complex

---

### Sprint Summary

| Sprint | Stories | Points | Completion % | Dependencies Met |
|--------|---------|--------|--------------|------------------|
| 1      | 6       | 38     | 44%          | ✓ All internal   |
| 2      | 5       | 40     | 90%          | ✓ From Sprint 1  |
| 3      | 1       | 9      | 100%         | ✓ From Sprint 1&2|

**Critical Path:**
story-auth-001 → story-auth-002 → story-auth-004 → story-auth-005
(Total: 26 points, ~1.5 sprints minimum)

**Parallel Work Opportunities:**
- Sprint 1: stories 3, 6, 11 can be done in parallel with critical path
- Sprint 2: stories 1, 7 are independent
```

---

## Step 6: Story File Format Template

Complete story file with all sections:

```markdown
# Story: User Signup

**Story ID:** story-auth-001
**Epic:** epic-auth (User Authentication & Authorization)
**Status:** Todo
**Priority:** P0 (Must Have)
**Story Points:** 8
**Component:** Authentication
**Created:** 2025-10-29
**Sprint:** Sprint 1

---

## User Story

As a new user,
I want to create an account with email and password,
So that I can access personalized features and save my preferences.

---

## Acceptance Criteria

1. ✅ User can signup with valid email (RFC 5322 format)
2. ✅ Password requirements enforced (min 8 chars, 1 uppercase, 1 number, 1 special char)
3. ✅ Duplicate emails prevented (409 Conflict error with clear message)
4. ✅ Confirmation email sent immediately after registration
5. ✅ User account created in "unverified" state until email confirmed
6. ✅ Rate limiting applied (max 5 signup attempts per IP per hour)

---

## Technical Notes

**Database Schema:**
```sql
CREATE TABLE users (
  id UUID PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  status ENUM('unverified', 'active', 'suspended') DEFAULT 'unverified',
  created_at TIMESTAMP DEFAULT NOW()
);
```

**API Endpoint:**
```
POST /api/v1/auth/signup
Request Body: { email, password }
Response: 201 Created, { user_id, message }
```

**Dependencies:**
- bcrypt for password hashing
- email service (SendGrid/Mailgun)
- rate limiting middleware (express-rate-limit)

---

## Dependencies

**Blocks:**
- story-auth-003 (Email Verification)
- story-auth-002 (User Login)
- story-auth-009 (RBAC System)

**Blocked By:** None (foundation story)

**Related:**
- story-auth-002 (User Login) - shares authentication service

---

## Estimation Details

**Complexity:** 3/5 (Moderate)
- Email validation logic
- Password hashing
- Email service integration
- Database operations

**Effort:** 4/5 (8-16 hours)
- User model creation (1 hour)
- Signup service implementation (3 hours)
- API endpoint creation (2 hours)
- Unit tests (3 hours)
- Integration tests (2 hours)
- Email template creation (1 hour)
- API documentation (1 hour)

**Risk:** 1/3 (Low)
- Well-known auth pattern
- Team has experience with bcrypt
- Standard email service integration

**Total:** 3 + 4 + 1 = 8 story points

---

## Sprint Assignment

**Sprint 1** (Foundation Sprint)

**Sprint Goals:**
- Core authentication functionality
- Foundation for subsequent auth features

**Team Assignment:** TBD

---

## Definition of Done

- [ ] User model created with proper schema
- [ ] Signup endpoint implemented and tested
- [ ] Password hashing working correctly
- [ ] Email validation enforced
- [ ] Duplicate email check implemented
- [ ] Confirmation email sent successfully
- [ ] Rate limiting applied and tested
- [ ] Unit tests written and passing (>80% coverage)
- [ ] Integration tests written and passing
- [ ] API documentation updated
- [ ] Code reviewed and approved
- [ ] Security review completed
- [ ] Merged to main branch
- [ ] Deployed to staging environment
- [ ] QA testing completed

---

## Testing Checklist

**Unit Tests:**
- [ ] Email validation (valid/invalid formats)
- [ ] Password validation (strength requirements)
- [ ] Password hashing (bcrypt integration)
- [ ] Duplicate email detection
- [ ] Error handling (database errors, email errors)

**Integration Tests:**
- [ ] End-to-end signup flow
- [ ] Email sending (mock service)
- [ ] Database user creation
- [ ] Rate limiting behavior

**Manual Testing:**
- [ ] UI signup form validation
- [ ] Email receipt and format
- [ ] Error message clarity

---

## Implementation Tasks

1. Database migration (user table)
2. User model creation (TypeScript interface)
3. Password hashing utility (bcrypt)
4. Email validation utility
5. Email service integration (SendGrid)
6. Signup service logic
7. Signup API endpoint (Express route)
8. Rate limiting middleware
9. Error handling
10. Unit tests
11. Integration tests
12. API documentation (OpenAPI spec)

---

## Notes

- Consider adding social signup (OAuth) in future story
- Email verification is separate story (story-auth-003)
- Admin user creation is different flow (manual/seed script)

---

*Part of epic-auth - User Authentication & Authorization*
```

---

## Step 6: Epic Summary File Format

Complete epic summary with all sections:

```markdown
# Epic: User Authentication & Authorization

**Epic ID:** epic-auth
**Status:** Planning Complete
**Total Story Points:** 87
**Estimated Duration:** 3 sprints (6 weeks)
**Created:** 2025-10-29
**Owner:** Product Team

---

## Epic Overview

Implement comprehensive user authentication and authorization system supporting email/password auth, OAuth social login, and role-based access control.

**Business Value:**
- Enable secure user access to the application
- Support multiple authentication methods
- Provide granular permission control
- Meet security compliance requirements

**Target Users:**
- New users (signup/registration)
- Returning users (login/password reset)
- OAuth users (social login)
- Administrators (user/role management)

---

## Stories Breakdown

**Total Stories:** 11

**By Priority:**
- P0 (Must Have): 4 stories, 23 story points (26%)
- P1 (Should Have): 6 stories, 56 story points (64%)
- P2 (Nice to Have): 1 story, 8 story points (9%)

**By Component:**
- Authentication: 7 stories, 46 points
- OAuth Integration: 3 stories, 19 points
- Authorization: 1 story, 13 points
- Security: 0 stories (cross-cutting)

**Story List:**
1. story-auth-001: User Signup (8 points, P0)
2. story-auth-002: User Login (5 points, P0)
3. story-auth-003: Email Verification (5 points, P1)
4. story-auth-004: JWT Sessions (5 points, P0)
5. story-auth-005: Token Refresh (8 points, P1)
6. story-auth-006: Password Reset (8 points, P1)
7. story-auth-007: OAuth Setup (8 points, P1)
8. story-auth-008: OAuth Login (Google) (5 points, P1)
9. story-auth-009: RBAC System (13 points, P1)
10. story-auth-010: Account Linking (6 points, P2)
11. story-auth-011: Rate Limiting (7 points, P1)

---

## Sprint Plan

### Sprint 1: Foundation (38 points)
**Stories:** 6
**Focus:** Core authentication
**Stories:**
- story-auth-001: User Signup (8)
- story-auth-002: User Login (5)
- story-auth-004: JWT Sessions (5)
- story-auth-003: Email Verification (5)
- story-auth-006: Password Reset (8)
- story-auth-011: Rate Limiting (7)

### Sprint 2: Enhancement (40 points)
**Stories:** 5
**Focus:** OAuth + RBAC
**Stories:**
- story-auth-007: OAuth Setup (8)
- story-auth-008: OAuth Login (5)
- story-auth-005: Token Refresh (8)
- story-auth-009: RBAC System (13)
- story-auth-010: Account Linking (6)

### Sprint 3: Advanced (9 points)
**Stories:** 1 (under-capacity)
**Focus:** Multi-factor auth
**Stories:**
- story-auth-012: Multi-Factor Auth (9)

---

## Dependency Graph

```
story-auth-001 (Signup)
  ├─ BLOCKS story-auth-002 (Login)
  ├─ BLOCKS story-auth-003 (Email Verification)
  └─ BLOCKS story-auth-009 (RBAC)

story-auth-002 (Login)
  ├─ BLOCKS story-auth-004 (JWT Sessions)
  └─ BLOCKS story-auth-006 (Password Reset)

story-auth-004 (JWT)
  └─ BLOCKS story-auth-005 (Token Refresh)

story-auth-007 (OAuth Setup)
  └─ BLOCKS story-auth-008 (OAuth Login)

story-auth-008 (OAuth Login)
  └─ RELATED story-auth-010 (Account Linking)
```

**Critical Path:**
story-auth-001 → story-auth-002 → story-auth-004 → story-auth-005
(26 points, ~1.5 sprints minimum)

---

## Technical Architecture

**Tech Stack:**
- Node.js + TypeScript
- Express.js (API framework)
- PostgreSQL (user storage)
- Redis (session storage)
- JWT (token authentication)
- bcrypt (password hashing)
- Passport.js (OAuth integration)
- SendGrid (email service)

**Key Components:**
- User model (database schema)
- Authentication service (signup, login, logout)
- Authorization middleware (role checking)
- Session management (JWT, refresh tokens)
- Email service (verification, reset)
- OAuth integration (Google, GitHub)

---

## Success Metrics

**Functionality:**
- [ ] Users can signup with email/password
- [ ] Users can login and receive JWT token
- [ ] Users can reset forgotten passwords
- [ ] Users can login via OAuth (Google)
- [ ] Admins can assign roles to users
- [ ] Rate limiting prevents brute force attacks

**Performance:**
- Login response time <500ms (target: 200ms)
- Signup response time <1s (target: 500ms)
- Support 1000 concurrent users
- 99.9% uptime for auth endpoints

**Security:**
- Passwords hashed with bcrypt (12 rounds)
- JWT tokens expire after 1 hour
- Refresh tokens stored securely
- Rate limiting applied to all auth endpoints
- No sensitive data in logs

---

## Risks & Mitigation

**Risk 1: OAuth Provider Outage**
- Impact: High (users can't login via OAuth)
- Probability: Low
- Mitigation: Graceful fallback to email/password, status page

**Risk 2: Email Service Downtime**
- Impact: Medium (signup/reset delayed)
- Probability: Medium
- Mitigation: Queue email jobs, retry logic, alternative provider

**Risk 3: Token Security Breach**
- Impact: Critical (unauthorized access)
- Probability: Low
- Mitigation: Short token expiration, refresh token rotation, monitoring

---

## Definition of Done (Epic Level)

- [ ] All 11 stories completed and deployed
- [ ] All acceptance criteria met
- [ ] Integration tests passing
- [ ] E2E tests passing
- [ ] Security audit completed
- [ ] Performance benchmarks met
- [ ] Documentation complete (API, user guide, admin guide)
- [ ] Monitoring and alerting configured
- [ ] Rollout plan approved
- [ ] Stakeholder demo completed

---

## Related Epics

**Depends On:** None (foundational epic)

**Blocks:**
- epic-profile: User profile management (requires auth)
- epic-admin: Admin dashboard (requires RBAC)

**Related:**
- epic-security: Security enhancements (2FA, biometrics)

---

*Part of BMAD Enhanced Planning Suite*
```

---

## Step 7: Summary Output Template

Presentation to user after breakdown:

```markdown
## Epic Breakdown Complete

**Epic:** User Authentication & Authorization
**Stories Created:** 11
**Total Story Points:** 87
**Suggested Sprints:** 3 (6 weeks)
**Team Velocity:** 40 points/sprint

---

### Files Generated

**Story Files:**
- .claude/stories/story-auth-001-user-signup.md
- .claude/stories/story-auth-002-user-login.md
- .claude/stories/story-auth-003-email-verification.md
- .claude/stories/story-auth-004-jwt-sessions.md
- .claude/stories/story-auth-005-token-refresh.md
- .claude/stories/story-auth-006-password-reset.md
- .claude/stories/story-auth-007-oauth-setup.md
- .claude/stories/story-auth-008-oauth-login-google.md
- .claude/stories/story-auth-009-rbac-system.md
- .claude/stories/story-auth-010-account-linking.md
- .claude/stories/story-auth-011-rate-limiting.md

**Epic Summary:**
- .claude/epics/epic-auth.md

---

### Priority Distribution

| Priority | Stories | Points | Percentage |
|----------|---------|--------|------------|
| P0       | 4       | 23     | 26%        |
| P1       | 6       | 56     | 64%        |
| P2       | 1       | 8      | 9%         |
| **Total**| **11**  | **87** | **100%**   |

---

### Sprint Plan

**Sprint 1: Foundation (38 points)**
- 6 stories focusing on core authentication
- Critical path: Signup → Login → JWT Sessions

**Sprint 2: Enhancement (40 points)**
- 5 stories adding OAuth and RBAC
- Parallel work opportunities

**Sprint 3: Advanced (9 points)**
- 1 story for multi-factor auth
- Under-capacity, consider pulling forward stories

---

### Dependencies Identified

**Total Dependencies:** 7 blocking relationships

**Critical Path:**
story-auth-001 → story-auth-002 → story-auth-004 → story-auth-005
(26 points, ~1.5 sprints minimum)

**Foundation Stories (no dependencies):**
- story-auth-001 (User Signup)
- story-auth-007 (OAuth Setup)
- story-auth-011 (Rate Limiting)

---

### Next Steps

1. **Review Stories:** Validate acceptance criteria and estimates with team
2. **Refine Priorities:** Confirm P0/P1/P2 with product owner
3. **Sprint Planning:** Schedule Sprint 1 planning meeting
4. **Assign Stories:** Allocate stories to developers
5. **Setup Infrastructure:** Prepare dev/staging environments

**Ready to proceed with Sprint 1 planning?**

```

---

## JSON Output Format

Telemetry and output structure:

```json
{
  "status": "success",
  "story_files": [
    ".claude/stories/story-auth-001-user-signup.md",
    ".claude/stories/story-auth-002-user-login.md",
    ".claude/stories/story-auth-003-email-verification.md",
    ".claude/stories/story-auth-004-jwt-sessions.md",
    ".claude/stories/story-auth-005-token-refresh.md",
    ".claude/stories/story-auth-006-password-reset.md",
    ".claude/stories/story-auth-007-oauth-setup.md",
    ".claude/stories/story-auth-008-oauth-login-google.md",
    ".claude/stories/story-auth-009-rbac-system.md",
    ".claude/stories/story-auth-010-account-linking.md",
    ".claude/stories/story-auth-011-rate-limiting.md"
  ],
  "epic_file": ".claude/epics/epic-auth.md",
  "total_points": 87,
  "story_count": 11,
  "sprint_count": 3,
  "telemetry": {
    "skill": "breakdown-epic",
    "epic_id": "epic-auth",
    "story_count": 11,
    "total_points": 87,
    "sprint_count": 3,
    "priority_distribution": {
      "P0": 4,
      "P1": 6,
      "P2": 1
    },
    "component_distribution": {
      "Authentication": 7,
      "OAuth Integration": 3,
      "Authorization": 1
    },
    "dependency_count": 7,
    "critical_path_length": 4,
    "critical_path_points": 26,
    "duration_ms": 328000,
    "timestamp": "2025-10-29T12:45:00Z"
  }
}
```

---

*Part of BMAD Enhanced Planning Suite - breakdown-epic skill*
