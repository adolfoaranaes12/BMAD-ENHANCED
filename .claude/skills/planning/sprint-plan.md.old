# Sprint Plan Skill

## Purpose
Create a comprehensive sprint plan by intelligently grouping estimated user stories based on velocity, dependencies, priorities, and risk. This skill transforms a backlog of estimated stories into actionable sprint commitments with clear goals and risk mitigation.

## When to Use This Skill
- Before starting a new sprint (during Sprint Planning ceremony)
- When re-planning mid-sprint due to significant changes
- When creating a multi-sprint roadmap
- When evaluating sprint capacity and feasibility
- When balancing team workload across sprints

## Invocation
```bash
# Basic sprint planning
@alex *sprint "Sprint 1" --velocity 20

# Multi-sprint planning
@alex *sprint "Sprint 1" --velocity 20 --plan-ahead 3

# Sprint planning with specific story selection
@alex *sprint "Sprint 1" --velocity 20 --stories story-auth-001,story-auth-002

# Sprint planning with team split
@alex *sprint "Sprint 1" --velocity 20 --teams 2
```

## Prerequisites
- Stories must be created (via `@alex *breakdown`)
- Stories must be estimated (via `@alex *estimate`)
- Clear understanding of team velocity (historical or initial estimate)
- Dependencies identified (via `@alex *dependencies` or during breakdown)

## Skill Configuration
```yaml
skill_name: sprint-plan
version: 1.0.0
subagent: alex-planner
execution_mode: sequential
halt_on_error: false
output_directory: .claude/sprints
```

---

## STEP 0: Load Configuration and Sprint Context

### Actions
1. Validate sprint parameters (name, velocity)
2. Load all estimated stories from `.claude/stories/`
3. Load epic summaries for dependency data
4. Load team configuration
5. Initialize sprint planning framework

### Required Parameters
```yaml
sprint_name: "Sprint 1"
velocity: 20  # Story points team can commit to
```

### Optional Parameters
```yaml
plan_ahead: 1  # Number of sprints to plan (default: 1)
teams: 1  # Number of parallel teams (default: 1)
stories: []  # Specific stories to include (default: auto-select)
start_date: "2025-01-20"  # Sprint start date (default: next Monday)
sprint_duration: 2  # Weeks (default: 2)
buffer: 0.15  # Reserve buffer % (default: 15%)
```

### Load Stories
Scan `.claude/stories/` for all story files with:
- Story points estimated
- Status: "Ready" or "Backlog"
- Valid acceptance criteria

### Story Priority Mapping
```yaml
P0: Must Have (Critical for release)
P1: Should Have (Important but not critical)
P2: Could Have (Nice to have)
P3: Won't Have (Future consideration)
```

### Load Dependencies
From epic summaries (`.claude/epics/*-dependencies.md`) or story metadata:
```yaml
story-auth-001:
  blocks:
    - story-auth-002  # Signup blocks Login
    - story-auth-004  # Signup blocks Email Verification
  blocked_by: []
  parallel: []
```

### Team Configuration
Load from `.claude/config.yaml`:
```yaml
team:
  size: 3  # Number of developers
  velocity_per_person: 7  # Points per person per sprint
  total_velocity: 21  # Team velocity
  specializations:
    - frontend: [dev1, dev2]
    - backend: [dev1, dev3]
    - fullstack: [dev1]
```

---

## STEP 1: Calculate Sprint Capacity

### Capacity Formula
```
Gross Capacity = Team Velocity
Buffer Reserve = Gross Capacity × Buffer %
Net Capacity = Gross Capacity - Buffer Reserve
```

### Default Buffer Sizes
```yaml
Low Risk Sprint (many P1/P2, low complexity): 10%
Medium Risk Sprint (mix of priorities): 15%
High Risk Sprint (many P0, high complexity): 20%
First Sprint (unknown velocity): 25%
```

### Example Calculation
```
Team Velocity: 20 points
Buffer: 15% (medium risk)

Gross Capacity: 20 points
Buffer Reserve: 20 × 0.15 = 3 points
Net Capacity: 20 - 3 = 17 points
```

### Capacity Adjustment Factors
Adjust capacity based on:

1. **Team Availability**
   - Holidays/PTO: -5% to -50%
   - Onboarding new member: -10%
   - Production support rotation: -10%

2. **Sprint Characteristics**
   - First sprint of quarter: -5% (planning overhead)
   - End of release: +5% (focus boost)
   - Spike work planned: -20% (research uncertainty)

3. **Technical Debt**
   - High debt area: -10%
   - Refactoring sprint: -15%
   - Greenfield work: +5%

### Example with Adjustments
```
Base Velocity: 20 points
Adjustments:
  - Holiday (1 person out 1 week): -3 points
  - Production support: -2 points
  - First sprint: -1 point

Adjusted Velocity: 14 points
Buffer (15%): 2 points
Net Capacity: 12 points
```

---

## STEP 2: Prioritize and Filter Stories

### Prioritization Algorithm

**Priority Score** = (Priority Weight × 100) + (Risk Factor × 10) + (Dependency Factor × 5)

#### Priority Weights
```yaml
P0: 4.0  # Must Have
P1: 3.0  # Should Have
P2: 2.0  # Could Have
P3: 1.0  # Won't Have this sprint
```

#### Risk Factors
```yaml
High Risk (3): -2  # Deprioritize slightly (needs more prep)
Medium Risk (2): 0
Low Risk (1): 0
No Risk (0): +1  # Slight boost for low-risk quick wins
```

#### Dependency Factors
```yaml
Blocks Many Stories: +3  # Prioritize enablers
Blocks Some Stories: +2
No Blockers: 0
Blocked By Others: -5  # Deprioritize until dependencies resolved
```

### Example Prioritization

**Story: story-auth-001-signup**
```yaml
Priority: P0 (Weight: 4.0)
Risk: Low (1) → Factor: 0
Dependencies: Blocks 3 stories → Factor: +3

Priority Score = (4.0 × 100) + (0 × 10) + (3 × 5)
               = 400 + 0 + 15
               = 415
```

**Story: story-auth-005-2fa**
```yaml
Priority: P1 (Weight: 3.0)
Risk: High (3) → Factor: -2
Dependencies: Blocked by story-auth-001 → Factor: -5

Priority Score = (3.0 × 100) + (-2 × 10) + (-5 × 5)
               = 300 - 20 - 25
               = 255
```

### Filtering Rules

**Exclude from Sprint:**
1. Stories with unresolved blocking dependencies
2. Stories without estimates
3. Stories marked "Blocked" or "On Hold"
4. Stories with confidence < 50% (need refinement)
5. P3 stories (unless excess capacity)

**Include in Sprint:**
1. P0 stories (always evaluate)
2. P1 stories (high priority)
3. Foundation stories (block many others)
4. Quick wins (1-2 points, low risk)

---

## STEP 3: Build Dependency Graph

### Graph Structure
Create a directed acyclic graph (DAG) of story dependencies:

```
story-auth-001 (signup)
  ├─> story-auth-002 (login)
  ├─> story-auth-004 (email-verify)
  └─> story-profile-001 (profile)

story-auth-002 (login)
  ├─> story-auth-003 (logout)
  └─> story-auth-006 (password-reset)

story-auth-008 (rate-limit)
  [parallel - no dependencies]
```

### Dependency Types

#### 1. Hard Dependencies (Blocking)
- **Definition:** Story B cannot start until Story A is complete
- **Example:** Login depends on Signup (can't log in without accounts)
- **Sprint Impact:** Must sequence stories in correct order
- **Notation:** `story-auth-002 BLOCKED_BY story-auth-001`

#### 2. Soft Dependencies (Preferred)
- **Definition:** Story B is easier if Story A is done first, but not required
- **Example:** Password Reset is easier after Login is done (shared patterns)
- **Sprint Impact:** Try to sequence, but not critical
- **Notation:** `story-auth-006 PREFERS story-auth-002`

#### 3. Parallel Dependencies (Can Work Simultaneously)
- **Definition:** Stories can be worked on at the same time
- **Example:** Rate Limiting and Email Verification (independent features)
- **Sprint Impact:** Can assign to different developers
- **Notation:** `story-auth-004 PARALLEL story-auth-008`

### Dependency Validation

**Check for Issues:**

1. **Circular Dependencies** ❌
   ```
   story-A depends on story-B
   story-B depends on story-C
   story-C depends on story-A  # CIRCULAR!
   ```
   **Resolution:** Break the cycle, likely requirements issue

2. **Dependency Chain Too Long** ⚠️
   ```
   story-A → story-B → story-C → story-D → story-E
   ```
   **Risk:** Cannot parallelize work, low throughput
   **Resolution:** Look for opportunities to work in parallel

3. **External Dependencies** ⚠️
   ```
   story-X depends on: "API team to provide endpoint"
   ```
   **Risk:** Outside team's control
   **Resolution:** Create mock/stub, mark as risk

### Topological Sort
Order stories so dependencies are satisfied:

```
Level 0 (No dependencies):
  - story-auth-001-signup
  - story-auth-008-rate-limit

Level 1 (Depends on Level 0):
  - story-auth-002-login (depends on signup)
  - story-auth-004-email-verify (depends on signup)

Level 2 (Depends on Level 1):
  - story-auth-003-logout (depends on login)
  - story-auth-006-password-reset (depends on login)
```

---

## STEP 4: Select Stories for Sprint

### Selection Algorithm

**Greedy approach with constraints:**

1. **Initialize:**
   - Remaining Capacity = Net Capacity
   - Selected Stories = []
   - Current Level = 0

2. **For each dependency level:**
   - Get stories at this level
   - Sort by Priority Score (descending)
   - For each story:
     - If story points ≤ remaining capacity:
       - Add to selected stories
       - Reduce remaining capacity
     - If remaining capacity < smallest story:
       - Move to next level

3. **Post-processing:**
   - Check for "orphan" dependencies (blocking story selected, but not blocked stories)
   - Add quick wins (1-2 points) if capacity remains
   - Balance story types (frontend/backend/infrastructure)

### Example Selection

**Input:**
```yaml
Velocity: 20 points
Buffer: 15% (3 points)
Net Capacity: 17 points

Available Stories (sorted by priority):
  1. story-auth-001-signup (5 pts, P0, Level 0) - Score: 415
  2. story-auth-008-rate-limit (3 pts, P0, Level 0) - Score: 410
  3. story-auth-002-login (3 pts, P0, Level 1) - Score: 405
  4. story-auth-004-email-verify (5 pts, P1, Level 1) - Score: 305
  5. story-auth-003-logout (1 pt, P1, Level 2) - Score: 300
  6. story-auth-006-password-reset (5 pts, P1, Level 2) - Score: 295
```

**Selection Process:**

**Round 1 - Level 0 (Foundation):**
```
Add story-auth-001-signup (5 pts)
  Remaining: 17 - 5 = 12 pts

Add story-auth-008-rate-limit (3 pts)
  Remaining: 12 - 3 = 9 pts
```

**Round 2 - Level 1 (Depends on Level 0):**
```
Add story-auth-002-login (3 pts)
  Remaining: 9 - 3 = 6 pts

Add story-auth-004-email-verify (5 pts)
  Remaining: 6 - 5 = 1 pt
```

**Round 3 - Level 2 (Depends on Level 1):**
```
Add story-auth-003-logout (1 pt)
  Remaining: 1 - 1 = 0 pts

Cannot add story-auth-006-password-reset (5 pts, exceeds capacity)
```

**Final Selection:**
```yaml
Selected Stories:
  - story-auth-001-signup (5 pts, P0)
  - story-auth-008-rate-limit (3 pts, P0)
  - story-auth-002-login (3 pts, P0)
  - story-auth-004-email-verify (5 pts, P1)
  - story-auth-003-logout (1 pt, P1)

Total Committed: 17 points
Buffer Remaining: 3 points
Utilization: 85%
```

### Capacity Utilization Targets

```yaml
Under-committed (<70%): ⚠️ Add more stories or reduce buffer
Well-balanced (70-90%): ✅ Healthy sprint commitment
Over-committed (>90%): ⚠️ High risk, consider removing lowest priority
At-capacity (100%): ❌ No buffer, very risky
```

---

## STEP 5: Create Sprint Goals

### Sprint Goal Definition
A sprint goal is a concise, outcome-focused statement that describes what the team aims to achieve. It should:
- Be achievable within the sprint
- Provide focus and direction
- Allow flexibility in implementation
- Create value for stakeholders

### Sprint Goal Formula
```
Sprint Goal = Outcome + Value + Success Criteria

Example:
"Enable user authentication so new users can create accounts and access the platform securely."
```

### Deriving Goals from Stories

**Selected Stories:**
```
- story-auth-001-signup (5 pts)
- story-auth-002-login (3 pts)
- story-auth-003-logout (1 pt)
- story-auth-008-rate-limit (3 pts)
- story-auth-004-email-verify (5 pts)
```

**Analysis:**
- **Theme:** User Authentication
- **Primary Outcome:** Users can create accounts and authenticate
- **Secondary Outcome:** Security (rate limiting, email verification)

**Primary Sprint Goal:**
```
"Deliver a complete user authentication flow that allows new users to sign up,
log in, and log out securely, with email verification and rate limiting to
prevent abuse."
```

**Alternative Format:**
```yaml
Sprint Goal: Launch User Authentication System

Outcomes:
  - New users can create accounts with email/password
  - Existing users can log in and log out
  - Email verification ensures valid addresses
  - Rate limiting prevents brute force attacks

Success Criteria:
  - 100% of authentication stories completed
  - All P0 acceptance criteria met
  - Security review passed
  - Integration tests passing

Value Delivered:
  - Platform can onboard real users
  - Foundation for all user-related features
  - Security baseline established
```

### Goal Validation

**Good Sprint Goals:**
✅ "Enable users to authenticate and access their personalized dashboard"
✅ "Deliver payment processing for subscription purchases"
✅ "Improve homepage load time to under 2 seconds"

**Poor Sprint Goals:**
❌ "Complete 5 stories" (output-focused, not outcome)
❌ "Work on authentication" (vague, no success criteria)
❌ "Build backend APIs" (technical, no user value)

---

## STEP 6: Assign Stories to Developers

### Assignment Strategy

**Consider:**
1. **Developer Skills**
   - Frontend vs. Backend vs. Full-stack
   - Domain expertise (auth, payments, etc.)
   - Technology familiarity

2. **Workload Balance**
   - Distribute points evenly
   - Account for capacity variations

3. **Dependencies**
   - Assign dependent stories to same developer (if possible)
   - Minimize handoffs

4. **Learning Goals**
   - Pair experienced with less experienced
   - Rotate domains for growth

### Assignment Algorithm

**Step 1: Categorize Stories**
```yaml
Frontend Stories:
  - story-ui-001 (form components)

Backend Stories:
  - story-auth-001 (signup API)
  - story-auth-002 (login API)

Full-stack Stories:
  - story-auth-004 (email verify - backend + email templates)
```

**Step 2: Match Skills**
```yaml
Developer A (Full-stack, Auth expert):
  - story-auth-001-signup (5 pts)
  - story-auth-002-login (3 pts)
  Total: 8 pts

Developer B (Full-stack, Security focus):
  - story-auth-008-rate-limit (3 pts)
  - story-auth-004-email-verify (5 pts)
  Total: 8 pts

Developer C (Full-stack):
  - story-auth-003-logout (1 pt)
  - [Reserve capacity for support/unplanned work]
  Total: 1 pt
```

**Step 3: Balance Load**
```yaml
Team Velocity: 20 pts
Average per Developer: 20 / 3 = 6.67 pts

Developer A: 8 pts (120% of average) - Slightly high
Developer B: 8 pts (120% of average) - Slightly high
Developer C: 1 pt (15% of average) - Very low

Adjustment:
  Move story-auth-002-login (3 pts) from A to C
  Move story-auth-004-email-verify (5 pts) from B to C

Result:
  Developer A: 5 pts (75%)
  Developer B: 3 pts (45%)
  Developer C: 9 pts (135%)

Further Adjustment:
  Move story-auth-008-rate-limit (3 pts) from B to A

Final:
  Developer A: 8 pts (120%) ✓
  Developer B: 0 pts → Add quick wins or support role
  Developer C: 9 pts (135%) ✓
```

### Unassigned Stories
- Keep as pool for:
  - Developer finishes early
  - Blocked story needs replacement
  - Capacity opens up

---

## STEP 7: Create Risk Mitigation Plan

### Identify Sprint Risks

**Risk Categories:**

#### 1. Dependency Risks
```yaml
Risk: story-auth-002 cannot start until story-auth-001 is merged
Impact: High (blocks 3 other stories)
Probability: Medium (signup could take longer)
Mitigation:
  - Prioritize story-auth-001 for day 1
  - Daily check-ins on progress
  - Have backup stories ready (parallel work)
```

#### 2. Technical Risks
```yaml
Risk: Email service integration may be complex
Impact: Medium (delays story-auth-004)
Probability: Medium (first time using SendGrid)
Mitigation:
  - Create technical spike (2 hours) before starting story
  - Use email stub/mock if needed
  - Pair with senior developer
```

#### 3. Capacity Risks
```yaml
Risk: Developer A out sick for 2 days
Impact: High (8 points at risk)
Probability: Low (but possible)
Mitigation:
  - Cross-train Developer B on auth patterns
  - Keep stories well-documented
  - Have Developer B as backup
```

#### 4. Requirement Risks
```yaml
Risk: Password complexity requirements may change
Impact: Low (minor code change)
Probability: Medium (stakeholder feedback expected)
Mitigation:
  - Confirm requirements with PO before sprint
  - Make password rules configurable
  - Keep validation logic isolated
```

#### 5. External Risks
```yaml
Risk: Database migration delayed by DBA team
Impact: High (blocks all stories)
Probability: Low (DBA confirmed availability)
Mitigation:
  - Schedule migration for Sprint Day 0
  - Have DBA on standby
  - Use local DB for development
```

### Risk Response Strategies

**1. Avoid** - Eliminate the risk
- Don't include risky stories in sprint
- Wait for dependencies to be resolved

**2. Mitigate** - Reduce probability or impact
- Add technical spike
- Pair programming
- Early prototyping

**3. Transfer** - Move risk elsewhere
- Outsource complex work
- Use third-party service

**4. Accept** - Acknowledge and monitor
- Document risk
- Have contingency plan
- Monitor daily

### Example Risk Register

```markdown
| Risk ID | Description | P | I | Score | Strategy | Owner |
|---------|-------------|---|---|-------|----------|-------|
| R-001 | Signup blocks login | M | H | 6 | Mitigate | Dev A |
| R-002 | Email service complexity | M | M | 4 | Mitigate | Dev B |
| R-003 | Developer A sick | L | H | 3 | Accept | TL |
| R-004 | Requirement change | M | L | 2 | Accept | PO |
| R-005 | DB migration delay | L | H | 3 | Mitigate | DBA |

P = Probability (L/M/H), I = Impact (L/M/H), Score = P×I (1-9)
```

---

## STEP 8: Generate Sprint Artifacts

### Artifact 1: Sprint Plan Summary

**File:** `.claude/sprints/sprint-01-plan.md`

```markdown
# Sprint 1 Plan: User Authentication Foundation

**Sprint Duration:** January 20 - February 2, 2025 (2 weeks)
**Team Velocity:** 20 points
**Committed:** 17 points (85% utilization)
**Buffer:** 3 points (15%)

---

## Sprint Goal

**Primary Goal:**
Deliver a complete user authentication flow that allows new users to sign up,
log in, and log out securely, with email verification and rate limiting to
prevent abuse.

**Success Criteria:**
- ✅ New users can create accounts with email/password
- ✅ Users can log in and receive JWT token
- ✅ Users can log out and invalidate session
- ✅ Email verification prevents fake accounts
- ✅ Rate limiting prevents brute force attacks
- ✅ All authentication endpoints secured
- ✅ Integration tests passing for all flows

**Value Delivered:**
- Platform ready to onboard real users
- Foundation for all user-related features
- Security baseline established
- Enables next sprint: User Profiles & Authorization

---

## Committed Stories

### Must Have (P0) - 11 points

| Story ID | Title | Points | Owner | Priority |
|----------|-------|--------|-------|----------|
| story-auth-001 | User Signup | 5 | Dev A | P0 |
| story-auth-002 | User Login | 3 | Dev C | P0 |
| story-auth-008 | Rate Limiting | 3 | Dev A | P0 |

### Should Have (P1) - 6 points

| Story ID | Title | Points | Owner | Priority |
|----------|-------|--------|-------|----------|
| story-auth-004 | Email Verification | 5 | Dev C | P1 |
| story-auth-003 | User Logout | 1 | Dev C | P1 |

**Total Committed:** 17 points

---

## Team Capacity

| Developer | Capacity | Assigned | Utilization | Status |
|-----------|----------|----------|-------------|--------|
| Developer A | 7 pts | 8 pts | 114% | ⚠️ Slightly over |
| Developer B | 7 pts | 0 pts | 0% | Support role |
| Developer C | 7 pts | 9 pts | 129% | ⚠️ Over capacity |

**Notes:**
- Developer B available for unplanned work, code reviews, and support
- Developer C is experienced with auth, can handle higher load
- 3 points buffer available for unknowns

---

## Dependency Sequencing

**Week 1 (Days 1-5):**
```
Day 1-3: story-auth-001-signup (Dev A) ← CRITICAL PATH
Day 1-2: story-auth-008-rate-limit (Dev A, parallel)
Day 3-5: story-auth-002-login (Dev C, after signup merged)
```

**Week 2 (Days 6-10):**
```
Day 6-8: story-auth-004-email-verify (Dev C)
Day 9: story-auth-003-logout (Dev C)
Day 10: Testing, refinement, documentation
```

**Critical Dependencies:**
- story-auth-002 (Login) ← Blocked by story-auth-001 (Signup)
- story-auth-003 (Logout) ← Blocked by story-auth-002 (Login)
- story-auth-004 (Email Verify) ← Blocked by story-auth-001 (Signup)

---

## Risk Register

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Signup delays login development | Medium | High | Prioritize signup for Day 1, daily standup tracking |
| Email service integration complex | Medium | Medium | 2-hour spike before starting, use stub if needed |
| Developer A overcommitted | Low | Medium | Developer B as backup, pair programming option |
| Password requirements change | Medium | Low | Confirm with PO before sprint, configurable rules |

---

## Definition of Done

**Story Level:**
- ✅ All acceptance criteria met
- ✅ Unit tests written and passing (>80% coverage)
- ✅ Integration tests written and passing
- ✅ Code reviewed and approved
- ✅ API documentation updated
- ✅ No critical or high severity bugs
- ✅ Merged to main branch

**Sprint Level:**
- ✅ All P0 stories completed
- ✅ Sprint goal achieved
- ✅ All tests passing in CI/CD
- ✅ Security review completed
- ✅ Demo ready for stakeholders
- ✅ Documentation published

---

## Next Sprint Preview

**Sprint 2 Focus:** User Profiles & Authorization

**Potential Stories:**
- story-profile-001: View user profile (3 pts)
- story-profile-002: Edit user profile (5 pts)
- story-auth-005: Role-based access control (8 pts)
- story-auth-007: Social login (OAuth) (8 pts)

**Dependencies:**
- All Sprint 2 stories depend on Sprint 1 auth foundation

---

## Meeting Schedule

| Event | Day/Time | Duration |
|-------|----------|----------|
| Sprint Planning | Day 0, 9:00 AM | 2 hours |
| Daily Standup | Every day, 9:30 AM | 15 min |
| Sprint Review | Day 10, 2:00 PM | 1 hour |
| Sprint Retro | Day 10, 3:30 PM | 1 hour |

---

**Generated:** 2025-01-15
**Generated By:** Alex (Planner)
**Version:** 1.0
```

### Artifact 2: Sprint Board Configuration

**File:** `.claude/sprints/sprint-01-board.yaml`

```yaml
sprint:
  name: "Sprint 1: User Authentication Foundation"
  id: sprint-01
  start_date: "2025-01-20"
  end_date: "2025-02-02"
  duration_weeks: 2
  status: planned

capacity:
  team_velocity: 20
  committed_points: 17
  buffer_points: 3
  utilization: 0.85

goal:
  primary: "Deliver complete user authentication flow"
  success_criteria:
    - "New users can sign up"
    - "Users can log in/log out"
    - "Email verification active"
    - "Rate limiting prevents abuse"

stories:
  committed:
    - id: story-auth-001
      title: "User Signup"
      points: 5
      priority: P0
      owner: dev-a
      status: todo
      dependencies: []

    - id: story-auth-008
      title: "Rate Limiting"
      points: 3
      priority: P0
      owner: dev-a
      status: todo
      dependencies: []

    - id: story-auth-002
      title: "User Login"
      points: 3
      priority: P0
      owner: dev-c
      status: todo
      dependencies: [story-auth-001]

    - id: story-auth-004
      title: "Email Verification"
      points: 5
      priority: P1
      owner: dev-c
      status: todo
      dependencies: [story-auth-001]

    - id: story-auth-003
      title: "User Logout"
      points: 1
      priority: P1
      owner: dev-c
      status: todo
      dependencies: [story-auth-002]

  backlog:
    - id: story-auth-006
      title: "Password Reset"
      points: 5
      priority: P1
      reason: "Didn't fit in velocity"

team:
  members:
    - id: dev-a
      name: "Developer A"
      capacity: 7
      assigned: 8
      specialization: fullstack

    - id: dev-b
      name: "Developer B"
      capacity: 7
      assigned: 0
      specialization: fullstack

    - id: dev-c
      name: "Developer C"
      capacity: 7
      assigned: 9
      specialization: fullstack

risks:
  - id: R-001
    description: "Signup blocks login"
    probability: medium
    impact: high
    mitigation: "Prioritize signup, daily tracking"

  - id: R-002
    description: "Email service complexity"
    probability: medium
    impact: medium
    mitigation: "Spike before starting, use stub"

definition_of_done:
  story:
    - "All AC met"
    - "Tests passing (>80% coverage)"
    - "Code reviewed"
    - "Documentation updated"
    - "Merged to main"
  sprint:
    - "All P0 stories completed"
    - "Sprint goal achieved"
    - "Security review passed"
    - "Demo ready"

metadata:
  generated_date: "2025-01-15"
  generated_by: "alex-planner"
  version: "1.0"
```

### Artifact 3: Daily Standup Template

**File:** `.claude/sprints/sprint-01-standup-template.md`

```markdown
# Daily Standup - Sprint 1

**Date:** [Fill in]
**Sprint Day:** [1-10]

---

## Developer A

**Yesterday:**
- [What did you complete?]

**Today:**
- [What will you work on?]

**Blockers:**
- [Any impediments?]

**Story Status:**
- story-auth-001 (Signup): [Todo/In Progress/Done]
- story-auth-008 (Rate Limit): [Todo/In Progress/Done]

---

## Developer B

**Yesterday:**
- [What did you complete?]

**Today:**
- [What will you work on?]

**Blockers:**
- [Any impediments?]

**Story Status:**
- [Supporting other developers]

---

## Developer C

**Yesterday:**
- [What did you complete?]

**Today:**
- [What will you work on?]

**Blockers:**
- [Any impediments?]

**Story Status:**
- story-auth-002 (Login): [Todo/In Progress/Done]
- story-auth-004 (Email Verify): [Todo/In Progress/Done]
- story-auth-003 (Logout): [Todo/In Progress/Done]

---

## Sprint Health

**Burndown:**
- Remaining: [X] points
- Expected: [Y] points
- Status: [On Track / Behind / Ahead]

**Risks:**
- [Any new risks identified?]

**Adjustments:**
- [Any changes to plan?]
```

---

## STEP 9: Multi-Sprint Planning (Optional)

### When to Plan Multiple Sprints

**Use Cases:**
- **Quarterly Planning:** Plan 6 sprints (3 months) for roadmap visibility
- **Release Planning:** Plan sprints leading to major release
- **Team Coordination:** Align multiple teams on dependencies
- **Stakeholder Communication:** Show longer-term delivery plan

### Multi-Sprint Algorithm

**For each sprint:**
1. Calculate capacity (may vary per sprint)
2. Select highest priority stories with resolved dependencies
3. Account for stories in-flight from previous sprint
4. Reserve capacity for bug fixes (increases over time)
5. Adjust velocity based on historical actuals

### Example: 3-Sprint Plan

**Sprint 1 (Current):**
```yaml
Velocity: 20 points
Focus: Core Authentication
Stories: story-auth-001 through story-auth-004
Goal: "Users can sign up and log in"
```

**Sprint 2 (Next):**
```yaml
Velocity: 20 points (no adjustment yet)
Focus: User Profiles & Authorization
Stories: story-profile-001, story-profile-002, story-auth-005
Goal: "Users can manage profiles and access control"
Dependencies: Sprint 1 auth foundation must be complete
```

**Sprint 3 (Future):**
```yaml
Velocity: 18 points (adjusted down for historical under-delivery)
Focus: Advanced Authentication
Stories: story-auth-007 (OAuth), story-auth-009 (SSO)
Goal: "Enterprise authentication features"
Dependencies: Sprint 1 & 2 foundations
Risk: Higher complexity, more unknowns
```

### Confidence Levels

```yaml
Sprint 1: High Confidence (90%) - immediate, well-understood
Sprint 2: Medium Confidence (75%) - dependencies clear, requirements solid
Sprint 3: Low Confidence (60%) - longer horizon, more unknowns
```

### Replanning Triggers

**Replan when:**
- Sprint 1 actuals vary >20% from estimate
- Major requirement changes
- Team composition changes
- Dependencies shift
- Stakeholder priorities change

---

## STEP 10: Present Sprint Plan to User

### Summary Format

```markdown
✅ Sprint Plan Created

**Sprint:** Sprint 1 - User Authentication Foundation
**Duration:** January 20 - February 2, 2025 (2 weeks)
**Velocity:** 20 points
**Committed:** 17 points (85% utilization)

**Sprint Goal:**
Deliver complete user authentication flow for signup, login, logout,
with email verification and rate limiting.

**Committed Stories (5):**
- story-auth-001: User Signup (5 pts, P0) → Dev A
- story-auth-008: Rate Limiting (3 pts, P0) → Dev A
- story-auth-002: User Login (3 pts, P0) → Dev C
- story-auth-004: Email Verification (5 pts, P1) → Dev C
- story-auth-003: User Logout (1 pt, P1) → Dev C

**Key Dependencies:**
- Login depends on Signup (Dev C waits for Dev A)
- Logout depends on Login
- Email Verify depends on Signup

**Top Risks:**
1. Signup blocks other stories (High impact, Medium probability)
   → Mitigation: Prioritize for Day 1
2. Email service complexity (Medium impact/probability)
   → Mitigation: Technical spike, use stub if needed

**Team Capacity:**
- Developer A: 8 points (auth expert)
- Developer B: 0 points (support role)
- Developer C: 9 points (execution lead)

**Files Generated:**
- `.claude/sprints/sprint-01-plan.md` (detailed plan)
- `.claude/sprints/sprint-01-board.yaml` (board config)
- `.claude/sprints/sprint-01-standup-template.md` (daily template)

**Next Steps:**
1. Review plan with team in Sprint Planning meeting
2. Confirm story assignments
3. Validate sprint goal with stakeholders
4. Start Sprint on January 20
```

---

## Integration with Other Skills

### Before Sprint Planning
1. **@alex *breakdown** - Create stories from epics
2. **@alex *estimate** - Estimate all stories
3. **@alex *refine** - Clarify vague stories
4. **@alex *dependencies** - Map dependencies

### During Sprint
1. **@james *implement** - Execute stories
2. **@quinn *review** - Quality gates
3. **Daily standups** - Track progress
4. **@alex *adjust** - Replan if needed

### After Sprint
1. **Sprint Review** - Demo completed work
2. **Sprint Retro** - Lessons learned
3. **Velocity Tracking** - Update historical data
4. **@alex *sprint** - Plan next sprint

---

## Best Practices

### 1. Respect Team Velocity
- Don't over-commit (>90% utilization)
- Reserve buffer for unknowns
- Adjust based on historical actuals

### 2. Honor Dependencies
- Don't commit blocked stories
- Sequence work properly
- Minimize handoffs

### 3. Balance Risk
- Mix P0 (critical) with P1/P2 (lower risk)
- Don't pack sprint with all high-risk stories
- Include quick wins for momentum

### 4. Focus on Value
- Sprint goal should be outcome-focused
- Each story should contribute to goal
- Avoid "leftover work" syndrome

### 5. Keep Team Engaged
- Involve team in planning
- Respect individual capacity
- Balance learning and delivery

---

## Common Issues

### Issue 1: Over-Commitment
**Symptom:** >95% velocity utilization
**Problem:** No buffer for unknowns
**Solution:** Remove lowest priority story or increase buffer

### Issue 2: Under-Commitment
**Symptom:** <70% velocity utilization
**Problem:** Team won't be fully engaged
**Solution:** Add more stories from backlog

### Issue 3: Dependency Hell
**Symptom:** All stories depend on one story
**Problem:** No parallel work possible
**Solution:** Look for independent stories or split blocking story

### Issue 4: Unbalanced Assignments
**Symptom:** One developer at 150%, another at 20%
**Problem:** Inefficient use of team
**Solution:** Redistribute work, pair programming

---

## Skill Metadata

```yaml
skill_name: sprint-plan
version: 1.0.0
subagent: alex-planner
category: planning
execution_mode: sequential

inputs:
  required:
    - sprint_name
    - velocity
  optional:
    - plan_ahead
    - teams
    - stories
    - start_date

outputs:
  - Sprint plan (markdown)
  - Sprint board (YAML)
  - Standup template
  - Velocity report

dependencies:
  - breakdown-epic.md (creates stories)
  - estimate-stories.md (provides story points)

execution_time: 5-10 minutes per sprint
```

---

*This skill is part of the BMAD Enhanced Planning Suite.*
*For issues or improvements, see `.claude/skills/planning/README.md`*
