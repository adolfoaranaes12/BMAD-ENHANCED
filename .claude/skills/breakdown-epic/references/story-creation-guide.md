# Story Creation Guide

## Purpose

Create user stories in proper format with clear acceptance criteria.

---

## Step 2: Create User Stories

### User Story Format

**Standard format:**
```markdown
## Story Title

**As a** [user type],
**I want** [capability],
**So that** [benefit]
```

**Components:**
- **User type:** Who wants this feature?
- **Capability:** What do they want to do?
- **Benefit:** Why do they want it?

---

### Examples by Feature Area

**Authentication:**
```markdown
**Story: User Signup**
As a new user,
I want to create an account with email and password,
So that I can access personalized features and save my data.
```

```markdown
**Story: User Login**
As a registered user,
I want to log in with my credentials,
So that I can access my account and continue where I left off.
```

**Authorization:**
```markdown
**Story: Role-Based Access Control**
As an admin,
I want to assign roles to users,
So that I can control what features each user can access.
```

**Feature Enhancement:**
```markdown
**Story: OAuth Login**
As a user,
I want to log in with my Google account,
So that I don't need to remember another password.
```

---

## Acceptance Criteria

### Format

**Use specific, testable criteria:**

```markdown
## Acceptance Criteria

1. [Specific condition that must be met]
2. [Specific condition that must be met]
3. [Specific condition that must be met]
```

**Target:** 2-5 criteria per story

---

### Good vs. Bad Criteria

**❌ Bad (vague):**
```
1. Signup should work well
2. Password should be secure
3. System should handle errors
```

**✅ Good (specific):**
```
1. User can signup with valid email (RFC 5322 format) and password (8+ chars)
2. Password requirements enforced: min 8 chars, uppercase, lowercase, number, special char
3. Duplicate emails prevented with 409 Conflict error message
4. Confirmation email sent within 30 seconds of signup
5. Invalid inputs return 400 with specific validation error messages
```

---

### Acceptance Criteria Templates

**Feature Functionality:**
```
1. User can [action] when [condition]
2. System [response] when [trigger]
3. [Component] displays [information] when [state]
```

**Error Handling:**
```
1. Invalid [input] returns [error code] with [message]
2. Missing [field] returns 400 with validation error
3. Duplicate [resource] returns 409 with conflict message
```

**Performance:**
```
1. [Operation] completes in <[time]ms (p95)
2. System handles [N] concurrent [operations]
3. [Query] uses database indexes for <[time]ms execution
```

**Security:**
```
1. [Sensitive data] is [protection method] (e.g., hashed, encrypted)
2. [Endpoint] requires [authentication method]
3. [Input] is validated against [attack] (SQL injection, XSS)
```

---

## Story Properties

### Priority Levels

**P0 (Must Have) - Critical:**
- Core functionality
- Blocking other work
- Security vulnerabilities
- Legal/compliance requirements

**Example:**
```
Story: User Login [P0]
Justification: Cannot use app without login functionality
```

---

**P1 (Should Have) - High:**
- Important features
- Significant value
- Customer requests
- Competitive advantages

**Example:**
```
Story: OAuth Login [P1]
Justification: Improves UX, reduces friction, requested by users
```

---

**P2 (Nice to Have) - Medium:**
- Enhancements
- Optimizations
- Convenience features

**Example:**
```
Story: Remember Me Checkbox [P2]
Justification: Convenience feature, not essential
```

---

**P3 (Future) - Low:**
- Wishlist items
- Minor improvements
- Long-term considerations

**Example:**
```
Story: Biometric Login [P3]
Justification: Future enhancement, not current priority
```

---

### Component Classification

**Group stories by feature area:**

```
Component: Authentication
- story-auth-001: User Signup
- story-auth-002: User Login
- story-auth-003: Email Verification
- story-auth-006: Password Reset

Component: OAuth
- story-oauth-001: OAuth Setup
- story-oauth-002: OAuth Login
- story-oauth-003: Account Linking

Component: Authorization
- story-authz-001: RBAC System
- story-authz-002: Permission Management
```

---

## Story Quality Checks

### INVEST Criteria

**Independent:**
- Story can be developed independently
- Minimal dependencies on other stories
- Can be completed in isolation

**Negotiable:**
- Details can be refined during sprint
- Implementation approach flexible
- ACs are outcomes, not implementation

**Valuable:**
- Delivers user or business value
- Clear benefit stated in "So that" clause
- Stakeholders understand value

**Estimable:**
- Team can estimate effort
- Requirements clear enough
- Unknowns identified

**Small:**
- Can complete in one sprint
- Target: 3-8 story points
- Not too large, not too small

**Testable:**
- Acceptance criteria are testable
- Can verify completion
- Clear definition of done

---

### Story Size Guidelines

**Too Small (<2 points):**
```
❌ Story: Change button color
Solution: Combine with related stories or make it a task
```

**Good Size (3-8 points):**
```
✅ Story: User Signup (8 points)
- Substantial work
- Completable in sprint
- Clear value
```

**Too Large (>13 points):**
```
❌ Story: Complete Authentication System (34 points)
Solution: Break into multiple stories (Signup, Login, Reset, etc.)
```

---

## Story File Format

**Complete story file:**
```markdown
# Story: User Signup

**Story ID:** story-auth-001
**Epic:** epic-auth (User Authentication & Authorization)
**Status:** Todo
**Priority:** P0 (Must Have)
**Story Points:** 8
**Component:** Authentication

## User Story

As a new user,
I want to create an account with email and password,
So that I can access personalized features.

## Acceptance Criteria

1. User can signup with valid email (RFC 5322 format)
2. Password requirements enforced (8+ chars, uppercase, lowercase, number, special char)
3. Duplicate emails prevented (return 409 Conflict)
4. Confirmation email sent within 30 seconds
5. Invalid inputs return 400 with specific validation errors

## Dependencies

**Blocks:**
- story-auth-003 (Email Verification) - needs signup to exist
- story-auth-002 (User Login) - needs users to log in

**Related:**
- story-auth-006 (Password Reset) - similar validation logic

## Technical Notes

- Use bcrypt for password hashing (cost 12)
- Validate email with Zod schema (RFC 5322)
- Use SendGrid for confirmation emails
- JWT token generation on successful signup

## Definition of Done

- [ ] Implementation complete
- [ ] Unit tests written and passing (≥80% coverage)
- [ ] Integration tests written and passing
- [ ] API endpoint documented (OpenAPI spec)
- [ ] Code reviewed and approved
- [ ] Merged to main branch
- [ ] Deployed to staging environment

## Estimation Details

- Complexity: 3/5 (Moderate - validation, hashing, email)
- Effort: 4/5 (8-16 hours)
- Risk: 1/3 (Low - standard pattern)
- Total: 8 story points

## Sprint Assignment

Sprint 1
```

---

## Common Story Types

**1. Feature Story:**
```
As a [user],
I want [new capability],
So that [benefit]
```

**2. Enhancement Story:**
```
As a [user],
I want [improvement to existing feature],
So that [better experience/outcome]
```

**3. Technical Story:**
```
As a [developer/system],
I want [technical improvement],
So that [technical benefit]
```

**4. Bug Fix Story:**
```
As a [user],
I want [issue resolved],
So that [system works correctly]
```

---

## Quick Reference

**Story Format:**
- As a [user type]
- I want [capability]
- So that [benefit]

**Good ACs:**
- Specific (not vague)
- Testable (can verify)
- Complete (covers story)
- 2-5 per story

**Story Properties:**
- Priority: P0/P1/P2/P3
- Points: 3-8 (ideal range)
- Component: Feature area
- Dependencies: Blocks/Related

**INVEST:**
- Independent
- Negotiable
- Valuable
- Estimable
- Small
- Testable

---

*Part of breakdown-epic skill - Planning Suite*
