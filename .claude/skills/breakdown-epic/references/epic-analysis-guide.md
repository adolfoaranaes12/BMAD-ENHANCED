# Epic Analysis Guide

## Purpose

Analyze epic scope and identify major components for story breakdown.

---

## Step 1: Analyze Epic Scope

### Component Identification

**Extract from epic description:**

**1. Core Features**
- What functionality is needed?
- What are the main capabilities?
- What problems does this solve?

**Example:**
```
Epic: User Authentication & Authorization

Core Features:
- User signup (create accounts)
- User login (authenticate users)
- User logout (end sessions)
- Password reset (recover access)
- Email verification (confirm identity)
```

---

**2. User Types**
- Who will use this feature?
- What are their roles?
- What permissions do they need?

**Example:**
```
User Types:
- New users (signing up)
- Registered users (logging in)
- Authenticated users (using features)
- Admin users (managing system)
- OAuth users (external auth)
```

---

**3. Technical Requirements**
- What technologies are involved?
- What integrations are needed?
- What infrastructure is required?

**Example:**
```
Technical Requirements:
- Password hashing (bcrypt)
- JWT token management
- Email service integration (SendGrid)
- OAuth providers (Google, GitHub)
- Database schema (users, sessions, roles)
- API endpoints (signup, login, logout)
```

---

**4. Security Requirements**
- What needs protection?
- What compliance is required?
- What attack vectors exist?

**Example:**
```
Security Requirements:
- Password security (8+ chars, complexity, hashing)
- SQL injection prevention (parameterized queries)
- XSS prevention (input sanitization)
- CSRF protection (tokens)
- Rate limiting (5 requests/minute)
- Session management (secure tokens, expiration)
```

---

**5. Non-Functional Requirements**
- Performance targets?
- Scalability needs?
- Availability requirements?

**Example:**
```
Non-Functional Requirements:
- Response time: <200ms for login
- Availability: 99.9% uptime
- Concurrent users: 10,000+
- Password hashing: ~150ms acceptable
```

---

### Grouping by Themes

**Organize components into logical groups:**

**Example:**
```markdown
Epic: User Authentication & Authorization

Theme 1: Authentication Flow (Core)
- User signup (email + password)
- User login (credential validation)
- User logout (session termination)
- Password reset (forgot password flow)
- Email verification (confirm email)

Theme 2: OAuth Integration (Enhanced)
- OAuth provider setup (Google, GitHub)
- OAuth flow (redirect, callback, token exchange)
- Account linking (connect existing account to OAuth)

Theme 3: Authorization & RBAC (Advanced)
- User roles (admin, user, guest)
- Permission system (resource-based)
- Role-based access control

Theme 4: Session Management (Infrastructure)
- JWT token generation
- Token refresh mechanism
- Session expiration handling
- Token revocation (logout)
```

---

### Sub-Feature Identification

**Break themes into specific features:**

**Example for Authentication Flow:**
```markdown
Theme: Authentication Flow

Sub-Features:

1. User Signup
   - Email/password input form
   - Email format validation
   - Password strength validation
   - Duplicate email check
   - Password hashing (bcrypt)
   - User record creation
   - Confirmation email sending
   - Success response with JWT

2. User Login
   - Email/password input
   - Credential lookup in database
   - Password hash comparison
   - JWT token generation
   - Login attempt tracking
   - Rate limiting application
   - Error handling (invalid credentials)

3. Email Verification
   - Verification token generation
   - Email with verification link
   - Token validation on click
   - Account activation
   - Token expiration (24 hours)
```

---

## Analysis Techniques

### Technique 1: User Journey Mapping

**Map complete user flows:**

```
New User Journey:
1. Visit signup page
2. Enter email and password
3. Submit form
4. Receive confirmation email
5. Click verification link
6. Account activated
7. Redirected to dashboard

Login Journey:
1. Visit login page
2. Enter credentials
3. Submit form
4. Receive JWT token
5. Access protected resources
```

**Extract stories from each step**

---

### Technique 2: Component Matrix

**Matrix of features × requirements:**

```
                Signup  Login  Reset  OAuth  RBAC
Data Model        ✓       ✓      ✓      ✓      ✓
API Endpoint      ✓       ✓      ✓      ✓      ✓
UI Component      ✓       ✓      ✓      ✓      ✗
Email Service     ✓       ✗      ✓      ✗      ✗
Security          ✓       ✓      ✓      ✓      ✓
Testing           ✓       ✓      ✓      ✓      ✓
```

**Each ✓ may become a story or subtask**

---

### Technique 3: Technical Layer Analysis

**Analyze by technical layers:**

```
Data Layer:
- User model/schema
- Session model
- Role/permission model

Business Logic Layer:
- Authentication service
- Authorization service
- Token service
- Email service

API Layer:
- Signup endpoint
- Login endpoint
- Logout endpoint
- Password reset endpoint

UI Layer:
- Signup form
- Login form
- Password reset form
- OAuth buttons
```

**Each layer may generate stories**

---

## Scope Boundaries

### Epic Too Large

**Indicators:**
- More than 15 stories identified
- Multiple distinct user journeys
- Too many technical integrations
- Estimated >100 story points

**Action:**
```markdown
Split into multiple epics:
- Epic 1: Basic Auth (Signup, Login, Logout)
- Epic 2: Advanced Auth (OAuth, Password Reset)
- Epic 3: Authorization (RBAC, Permissions)
```

---

### Epic Too Small

**Indicators:**
- Fewer than 3 stories identified
- Single technical component
- Estimated <10 story points

**Action:**
```markdown
Combine with related epics or create single large story instead
```

---

## Quick Reference

**Component Checklist:**
- [ ] Core features identified
- [ ] User types defined
- [ ] Technical requirements listed
- [ ] Security requirements documented
- [ ] Non-functional requirements specified

**Grouping:**
- [ ] Features grouped by theme
- [ ] Themes have 3-5 sub-features each
- [ ] Sub-features are specific and actionable

**Scope:**
- [ ] 3-15 stories expected
- [ ] Reasonable for 2-5 sprints
- [ ] Not too broad, not too narrow

---

*Part of breakdown-epic skill - Planning Suite*
