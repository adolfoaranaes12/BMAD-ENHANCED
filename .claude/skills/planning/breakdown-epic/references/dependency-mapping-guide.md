# Dependency Mapping & Sprint Grouping Guide

## Purpose

Identify dependencies between stories and group them into sprints.

---

## Step 4: Identify Dependencies

### Dependency Types

**1. BLOCKS**
- Story A must complete before Story B can start
- Hard dependency
- Cannot parallelize

**Example:**
```
story-auth-001 (User Signup) BLOCKS story-auth-002 (User Login)
Reason: Need users in database before they can log in
```

---

**2. REQUIRES**
- Story B requires Story A to be complete
- Same as BLOCKS, from other perspective

**Example:**
```
story-auth-002 (User Login) REQUIRES story-auth-001 (User Signup)
```

---

**3. RELATED**
- Stories share components/code
- Can be done in parallel
- May want to do together for efficiency

**Example:**
```
story-auth-001 (User Signup) RELATED story-auth-006 (Password Reset)
Reason: Both use email validation, password hashing, similar patterns
```

---

### Dependency Rules

**Foundation First:**
```
Data models → Services → APIs → UI → Integration

Example:
story-auth-001 (User Model)
└─ BLOCKS story-auth-002 (Auth Service)
   └─ BLOCKS story-auth-003 (Signup API)
      └─ BLOCKS story-auth-004 (Signup Form)
```

---

**Authentication Before Authorization:**
```
Auth system → RBAC system

Example:
story-auth-001 (Signup)
└─ BLOCKS story-authz-001 (RBAC)

story-auth-002 (Login)
└─ BLOCKS story-authz-001 (RBAC)
```

---

**Core Before Enhancements:**
```
Basic feature → Enhanced feature

Example:
story-auth-002 (Email/Password Login)
└─ BLOCKS story-oauth-001 (OAuth Login)
```

---

**Infrastructure Before Applications:**
```
Session system → Features using sessions

Example:
story-auth-004 (JWT Sessions)
└─ BLOCKS story-auth-005 (Token Refresh)
└─ BLOCKS story-auth-002 (Login)
```

---

### Dependency Mapping Example

**Epic: User Authentication**

```markdown
Dependencies:

story-auth-001 (User Signup)
├─ BLOCKS story-auth-002 (User Login)
├─ BLOCKS story-auth-003 (Email Verification)
└─ RELATED story-auth-006 (Password Reset)

story-auth-002 (User Login)
├─ BLOCKS story-auth-006 (Password Reset)
├─ BLOCKS story-auth-009 (RBAC System)
└─ REQUIRES story-auth-004 (JWT Sessions)

story-auth-004 (JWT Sessions)
└─ BLOCKS story-auth-005 (Token Refresh)

story-auth-007 (OAuth Setup)
├─ BLOCKS story-auth-008 (OAuth Login)
└─ BLOCKS story-auth-010 (Account Linking)

story-auth-009 (RBAC System)
├─ REQUIRES story-auth-001 (User Signup)
└─ REQUIRES story-auth-002 (User Login)
```

---

### Dependency Graph Visualization

**Text-based graph:**

```
┌─────────────────┐
│ story-auth-001  │ User Signup (8 pts) [P0]
│ (Signup)        │
└────────┬────────┘
         │ BLOCKS
         ├──────────────┐
         │              │
         ▼              ▼
┌─────────────────┐  ┌─────────────────┐
│ story-auth-002  │  │ story-auth-003  │
│ (Login)         │  │ (Email Verify)  │
│ 5 pts [P0]      │  │ 13 pts [P1]     │
└────────┬────────┘  └─────────────────┘
         │ BLOCKS
         │
         ▼
┌─────────────────┐
│ story-auth-006  │ Password Reset (8 pts) [P1]
│ (Reset)         │
└─────────────────┘

┌─────────────────┐
│ story-auth-007  │ OAuth Setup (8 pts) [P1]
│ (OAuth Setup)   │
└────────┬────────┘
         │ BLOCKS
         ├──────────────┐
         │              │
         ▼              ▼
┌─────────────────┐  ┌─────────────────┐
│ story-auth-008  │  │ story-auth-010  │
│ (OAuth Login)   │  │ (Account Link)  │
│ 5 pts [P1]      │  │ 5 pts [P2]      │
└─────────────────┘  └─────────────────┘
```

---

## Step 5: Suggest Sprint Groupings

### Sprint Planning Rules

**1. Priority First**
- P0 stories in early sprints
- P1 stories after P0
- P2/P3 stories last

**2. Respect Dependencies**
- Blocking stories before blocked stories
- Don't schedule blocked story before blocker

**3. Velocity Constraints**
- Don't exceed team capacity
- Leave buffer for unknowns (~10%)

**4. Logical Grouping**
- Related stories together
- Complete features, not partial

---

### Sprint Planning Example

**Given:**
- Team Velocity: 40 points per sprint (2 weeks)
- Epic: User Authentication (79 points total)
- 10 stories with dependencies

**Sprint 1 (40 points):**
```markdown
Focus: Core Authentication

- story-auth-001: User Signup (8 pts) [P0]
  No dependencies, foundational

- story-auth-004: JWT Sessions (5 pts) [P0]
  No dependencies, needed for login

- story-auth-002: User Login (5 pts) [P0]
  Requires: Signup, JWT Sessions (both in sprint)

- story-auth-006: Password Reset (8 pts) [P1]
  Requires: Signup, Login (both in sprint)

- story-auth-003: Email Verification (13 pts) [P1]
  Requires: Signup (in sprint)

Total: 39 points (within capacity)
Dependencies: All satisfied
```

---

**Sprint 2 (39 points):**
```markdown
Focus: OAuth & Advanced Features

- story-auth-007: OAuth Setup (8 pts) [P1]
  No blockers

- story-auth-008: OAuth Login (5 pts) [P1]
  Requires: OAuth Setup (in sprint)

- story-auth-009: RBAC System (13 pts) [P1]
  Requires: Signup, Login (completed Sprint 1)

- story-auth-005: Token Refresh (8 pts) [P1]
  Requires: JWT Sessions (completed Sprint 1)

- story-auth-010: Account Linking (5 pts) [P2]
  Requires: OAuth Login (in sprint)

Total: 39 points (within capacity)
Dependencies: All satisfied
```

---

### Dependency Conflict Resolution

**Problem: Blocked story scheduled too early**

```
❌ Bad:
Sprint 1:
- story-auth-002 (Login) - requires Signup
- story-auth-006 (Password Reset) - requires Login

Sprint 2:
- story-auth-001 (Signup) - blocks Login and Reset

Result: Sprint 1 stories cannot start
```

**Solution: Reorder based on dependencies**

```
✅ Good:
Sprint 1:
- story-auth-001 (Signup)
- story-auth-002 (Login) - now unblocked
- story-auth-006 (Password Reset) - now unblocked
```

---

### Sprint Capacity Management

**Buffer for Unknowns:**
```
Team velocity: 40 points per sprint
Planned capacity: 36 points (90%)
Buffer: 4 points for unknowns, bugs, unplanned work
```

**Adjust for:**
- New team members (reduced velocity)
- Holidays/PTO (reduced availability)
- Technical debt work (reserve capacity)
- Production support (ongoing commitment)

---

### Sprint Grouping Checklist

For each sprint:

- [ ] **Priority:** P0 stories in early sprints
- [ ] **Capacity:** Total points ≤ team velocity
- [ ] **Dependencies:** All blockers scheduled before blocked stories
- [ ] **Buffer:** 10% capacity reserved for unknowns
- [ ] **Completeness:** Stories form complete features where possible
- [ ] **Balance:** Mix of different story types/sizes

---

## Dependency Patterns

### Pattern 1: Sequential Chain

```
A → B → C → D

Sprint 1: A
Sprint 2: B
Sprint 3: C
Sprint 4: D
```

**Challenge:** Long critical path
**Solution:** Parallelize where possible

---

### Pattern 2: Fan-Out

```
     A
    /│\
   / │ \
  B  C  D

Sprint 1: A
Sprint 2: B, C, D (parallel)
```

**Benefit:** Parallelization after foundation
**Optimal:** Maximize throughput

---

### Pattern 3: Fan-In

```
  A  B  C
   \ | /
    \|/
     D

Sprint 1: A, B, C (parallel)
Sprint 2: D
```

**Challenge:** D blocked until all complete
**Solution:** Ensure A, B, C in same/consecutive sprints

---

### Pattern 4: Independent Streams

```
A → B → C
D → E → F

Sprint 1: A, D
Sprint 2: B, E
Sprint 3: C, F
```

**Benefit:** Maximum parallelization
**Optimal:** Fully utilize capacity

---

## Quick Reference

**Dependency Types:**
- BLOCKS: Must complete before
- REQUIRES: Same as blocks (other direction)
- RELATED: Shares code/patterns

**Dependency Rules:**
- Foundation first (models → services → APIs)
- Auth before authz
- Core before enhancements
- Infrastructure before applications

**Sprint Grouping:**
- Priority first (P0 early)
- Respect dependencies
- Velocity constraints (≤capacity)
- Logical grouping (related stories)
- 10% buffer for unknowns

**Patterns:**
- Sequential: A→B→C→D
- Fan-Out: A→B,C,D
- Fan-In: A,B,C→D
- Independent: A→B, C→D

---

*Part of breakdown-epic skill - Planning Suite*
