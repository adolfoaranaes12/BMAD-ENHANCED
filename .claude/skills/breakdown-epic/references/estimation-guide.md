# Estimation Guide

## Purpose

Estimate story points using complexity, effort, and risk factors.

---

## Step 3: Estimate Story Points

### Three-Factor Estimation

**Formula:**
```
Story Points = Complexity + Effort + Risk
Then round to nearest Fibonacci number
```

**Fibonacci Scale:** 1, 2, 3, 5, 8, 13, 21

---

### Factor 1: Complexity (1-5)

**How difficult is the implementation?**

**1 - Trivial:**
- Simple CRUD operation
- No business logic
- Straightforward implementation

**Example:**
```
Story: View User Profile
- Read from database
- Display in UI
- No calculations or transformations
Complexity: 1
```

---

**2 - Simple:**
- Basic business logic
- Single component or service
- Known patterns

**Example:**
```
Story: Update User Email
- Validation (email format)
- Database update
- Success response
Complexity: 2
```

---

**3 - Moderate:**
- Multiple components involved
- Some business logic
- Moderate validation/transformation

**Example:**
```
Story: User Signup
- Email and password validation
- Password hashing
- Database insertion
- Email sending
Complexity: 3
```

---

**4 - Complex:**
- Many components and integrations
- Complex business rules
- Multiple validation layers

**Example:**
```
Story: OAuth Login
- OAuth provider integration
- Token exchange
- Account matching/creation
- Session management
Complexity: 4
```

---

**5 - Very Complex:**
- Novel or unfamiliar patterns
- Many integrations
- Complex algorithms
- Significant technical challenges

**Example:**
```
Story: Multi-Factor Authentication
- SMS provider integration
- TOTP algorithm implementation
- Backup codes generation
- Recovery flow
Complexity: 5
```

---

### Factor 2: Effort (1-5)

**How much time will this take?**

**1 - Minimal (<2 hours):**
- Quick implementation
- Mostly configuration
- Minor changes

**Example:**
```
Story: Add Remember Me Checkbox
- UI change (add checkbox)
- Update cookie expiration
Effort: 1
```

---

**2 - Small (2-4 hours):**
- Half-day work
- Single feature
- Basic testing

**Example:**
```
Story: User Logout
- Clear session/token
- Redirect to login
- Unit tests
Effort: 2
```

---

**3 - Medium (4-8 hours):**
- Half to full day
- Moderate feature
- Comprehensive testing

**Example:**
```
Story: User Login
- Credential validation
- Password comparison
- JWT generation
- Rate limiting
- Unit + integration tests
Effort: 3
```

---

**4 - Large (8-16 hours):**
- 1-2 days
- Substantial feature
- Multiple components
- Full test coverage

**Example:**
```
Story: User Signup
- Model/schema creation
- Service implementation
- API endpoint
- Email integration
- Unit + integration + E2E tests
Effort: 4
```

---

**5 - Very Large (16+ hours):**
- 2+ days
- Major feature
- Many components
- Extensive testing

**Example:**
```
Story: Role-Based Access Control
- Role model/schema
- Permission system
- Middleware implementation
- Admin UI
- Full test suite
- Migration script
Effort: 5
```

---

### Factor 3: Risk (1-3)

**What unknowns or risks exist?**

**1 - Low Risk:**
- Known implementation
- Standard patterns
- Team has experience
- Clear requirements

**Example:**
```
Story: User Login
- Standard auth pattern
- Team has done this before
- Clear requirements
Risk: 1
```

---

**2 - Medium Risk:**
- Some unknowns
- New library/tool
- Moderately clear requirements
- Minor dependencies

**Example:**
```
Story: OAuth Login
- Team hasn't done OAuth before
- External service dependency
- Need to learn OAuth flow
Risk: 2
```

---

**3 - High Risk:**
- Many unknowns
- Unclear requirements
- External dependencies
- Novel implementation
- Blocking dependencies

**Example:**
```
Story: Biometric Authentication
- New technology for team
- Device-specific implementation
- Security concerns
- Unclear browser support
Risk: 3
```

---

## Estimation Examples

### Example 1: User Signup

**Story:** User Signup with email and password

**Analysis:**
- **Complexity: 3** (Moderate)
  - Email/password validation
  - Password hashing
  - Database operations
  - Email sending
  - Multiple components

- **Effort: 4** (8-16 hours)
  - Data model creation
  - Service implementation
  - API endpoint
  - Email integration
  - Comprehensive testing

- **Risk: 1** (Low)
  - Standard auth pattern
  - Team has experience
  - Clear requirements
  - Known tech stack

**Calculation:**
```
Total = 3 + 4 + 1 = 8
Nearest Fibonacci = 8
Story Points = 8
```

---

### Example 2: OAuth Login

**Story:** Login with Google OAuth

**Analysis:**
- **Complexity: 4** (Complex)
  - OAuth flow (redirect, callback)
  - Token exchange with Google
  - Account matching/creation
  - Session generation
  - Many integration points

- **Effort: 3** (4-8 hours)
  - OAuth library integration
  - Callback endpoint
  - Account linking logic
  - Testing with mock OAuth

- **Risk: 2** (Medium)
  - Team hasn't done OAuth
  - External service dependency
  - Need to learn flow

**Calculation:**
```
Total = 4 + 3 + 2 = 9
Nearest Fibonacci = 8
Story Points = 8
```

---

### Example 3: Password Reset

**Story:** Forgot password flow with email

**Analysis:**
- **Complexity: 3** (Moderate)
  - Reset token generation
  - Email sending
  - Token validation
  - Password update
  - Security considerations

- **Effort: 4** (8-16 hours)
  - Token system implementation
  - Email templates
  - Reset endpoints (request + confirm)
  - Comprehensive testing

- **Risk: 1** (Low)
  - Standard pattern
  - Team has experience
  - Clear requirements

**Calculation:**
```
Total = 3 + 4 + 1 = 8
Nearest Fibonacci = 8
Story Points = 8
```

---

## Estimation Techniques

### Planning Poker

**Process:**
1. Read story aloud
2. Discuss complexity, effort, risk
3. Each team member selects estimate (Fibonacci card)
4. Reveal simultaneously
5. Discuss differences
6. Re-estimate if needed
7. Converge on consensus

**Benefits:**
- Team alignment
- Identifies unknowns
- Knowledge sharing

---

### Reference Stories

**Establish baseline stories:**

```
Reference: User Login = 5 points
- Use as comparison point
- "Is this story more or less complex than User Login?"

Small stories (3 points):
- Simpler than Login
- Example: Logout

Large stories (8 points):
- More complex than Login
- Example: Signup

Very large stories (13 points):
- Significantly more complex
- Example: RBAC system
```

---

### T-Shirt Sizing (Initial Pass)

**For quick estimation:**

```
XS (1-2 points): Trivial changes
S (3 points): Simple features
M (5 points): Moderate features
L (8 points): Complex features
XL (13 points): Very complex features
XXL (21+ points): Too large - break down
```

**Then refine with Complexity/Effort/Risk**

---

## Estimation Guidelines

### Story Size Targets

**Ideal Range: 3-8 points**
- Completable in one sprint
- Not too small (overhead)
- Not too large (risk)

**Too Small (<2 points):**
```
Action: Combine with related stories or make it a task
```

**Too Large (>13 points):**
```
Action: Break into multiple stories
Example: "RBAC System" (21 points)
→ Break into:
  - Role Model (5 points)
  - Permission System (8 points)
  - Admin UI (5 points)
  - RBAC Middleware (3 points)
```

---

### Velocity Consideration

**Track team velocity:**
```
Sprint 1: 42 points completed
Sprint 2: 38 points completed
Sprint 3: 45 points completed
Average: ~42 points per sprint
```

**Use for sprint planning:**
```
Sprint capacity = Average velocity
Don't overcommit
```

---

### Re-Estimation

**Re-estimate when:**
- Requirements change significantly
- Unknowns are clarified
- Team learns more about problem
- After spike/research story

**Example:**
```
Initial estimate: OAuth Login = 13 points (high risk/unknown)
After OAuth spike: OAuth Login = 8 points (risk reduced)
```

---

## Common Pitfalls

**1. Estimating Time, Not Complexity**
```
❌ "This will take 2 days" = X points
✅ "This has moderate complexity + large effort + low risk" = Y points
```

**2. Perfectionism**
```
❌ Including "nice-to-have" features in estimate
✅ Estimate only what's in acceptance criteria
```

**3. Ignoring Risk**
```
❌ "We'll figure it out" = underestimate
✅ "Unknown OAuth flow" = add risk factor
```

**4. Not Discussing**
```
❌ Silent individual estimates
✅ Team discussion and alignment
```

---

## Quick Reference

**Three Factors:**
- Complexity (1-5): How difficult?
- Effort (1-5): How long?
- Risk (1-3): What unknowns?

**Formula:**
```
Story Points = Complexity + Effort + Risk
Round to Fibonacci: 1, 2, 3, 5, 8, 13, 21
```

**Target Size:**
- Ideal: 3-8 points
- Too small: <2 points (combine)
- Too large: >13 points (break down)

**Techniques:**
- Planning poker (team consensus)
- Reference stories (comparison)
- T-shirt sizing (quick pass)

---

*Part of breakdown-epic skill - Planning Suite*
