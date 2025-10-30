---
name: sprint-plan
description: Create comprehensive sprint plans by intelligently grouping estimated user stories based on velocity, dependencies, priorities, and risk. Use during sprint planning ceremonies to transform backlog into actionable sprint commitments.
acceptance:
  - velocity_respected: "Total story points ≤ team velocity with 15% buffer"
  - dependencies_satisfied: "All story dependencies respected in sprint ordering"
  - priorities_honored: "P0 stories prioritized over P1/P2/P3"
  - sprint_plan_generated: "Sprint plan file created with goals, stories, risks, and metrics"
inputs:
  sprint_name:
    type: string
    required: true
    description: "Name of sprint (e.g., 'Sprint 1', 'Q1 Sprint 3')"
  velocity:
    type: number
    required: true
    description: "Team velocity in story points (historical or estimated)"
  plan_ahead:
    type: number
    default: 1
    description: "Number of sprints to plan (1-4)"
  stories:
    type: array
    required: false
    description: "Specific story IDs to include (default: auto-select from backlog)"
  buffer:
    type: number
    default: 0.15
    description: "Reserve buffer percentage (default: 15% of velocity)"
outputs:
  sprint_plan:
    type: object
    description: "Sprint plan with goals, stories, capacity, risks"
  commitment:
    type: number
    description: "Total story points committed"
  utilization:
    type: number
    description: "Percentage of velocity utilized"
  sprint_plan_file:
    type: string
    description: "Path to generated sprint plan file"
telemetry:
  emit: "skill.sprint-plan.completed"
  track:
    - sprint_name
    - velocity
    - duration_ms
    - stories_count
    - commitment_points
    - utilization_percent
    - p0_stories_count
    - dependencies_count
---

# Sprint Planning

Create comprehensive sprint plans by intelligently grouping estimated user stories based on team velocity, dependencies, priorities, and risk mitigation.

## Purpose

Transform backlog of estimated stories into actionable sprint commitments:
- Calculate effective capacity (velocity - buffer)
- Select stories respecting dependencies and priorities
- Balance workload and minimize risk
- Generate sprint plan with goals, metrics, and risk mitigation
- Support multi-sprint planning (roadmap view)

## When to Use

Use this skill when:
- Starting a new sprint (during Sprint Planning ceremony)
- Re-planning mid-sprint due to significant changes
- Creating multi-sprint roadmap (2-4 sprints ahead)
- Evaluating sprint capacity and feasibility
- Balancing team workload across multiple teams

Do NOT use when:
- Stories are not yet estimated (use estimate-stories first)
- Stories lack acceptance criteria (use refine-story first)
- No historical velocity data (establish velocity first with 1-2 sprints)

## Prerequisites

- Stories created (via breakdown-epic skill)
- Stories estimated (via estimate-stories skill)
- Clear team velocity (historical average or initial estimate)
- Dependencies identified (in story files or epic summaries)

## Sequential Sprint Planning Process

Execute steps in order - each builds on previous analysis:

### Step 0: Load Configuration and Sprint Context

**Purpose:** Gather all inputs needed for sprint planning.

**Actions:**

1. Validate sprint parameters:
   - Sprint name (must be unique)
   - Velocity (must be > 0)
   - Plan ahead (1-4 sprints)
   - Buffer percentage (default 15%)

2. Load all eligible stories from `.claude/stories/`:
   - Filter: Status = "Ready" or "Backlog"
   - Filter: Has story points estimated
   - Filter: Has acceptance criteria

3. Load dependencies:
   - From story files (Dependencies section)
   - From epic summaries (dependency graphs)
   - Build dependency map

4. Calculate effective capacity:
   ```
   Effective Capacity = Velocity × (1 - Buffer)
   Example: 20 points × (1 - 0.15) = 17 points available
   ```

**Output:**
```
Sprint Planning Context:
- Sprint: Sprint 1
- Velocity: 20 points
- Buffer: 15% (3 points)
- Effective Capacity: 17 points
- Eligible Stories: 24 stories (78 total points)
- Dependencies: 8 blocking relationships identified
```

**Reference:** See [sprint-planning-mechanics.md](references/sprint-planning-mechanics.md) for capacity calculation details.

---

### Step 1: Prioritize and Sort Stories

**Purpose:** Create prioritized list respecting business value and dependencies.

**Sorting Criteria (in order):**

1. **Priority Level** (P0 > P1 > P2 > P3)
2. **Dependency Order** (blockers before blocked)
3. **Risk Score** (high-risk early for discovery)
4. **Story Points** (smaller stories for momentum)

**Example Sorted Backlog:**
```
1. story-auth-001 (Signup) - P0, 5 points, blocks 3 stories
2. story-auth-002 (Login) - P0, 3 points, blocked by auth-001
3. story-auth-003 (Logout) - P0, 1 point, blocked by auth-002
4. story-profile-001 (View Profile) - P1, 2 points, blocked by auth-002
5. story-profile-002 (Edit Profile) - P1, 3 points, blocked by profile-001
...
```

**Reference:** See [story-selection-algorithm.md](references/story-selection-algorithm.md) for detailed sorting logic.

---

### Step 2: Select Stories for Sprint

**Purpose:** Fill sprint capacity with highest-value stories respecting constraints.

**Selection Algorithm:**

1. Start with P0 stories in dependency order
2. Add story if:
   - All dependencies already in sprint OR completed
   - Points fit within remaining capacity
   - Doesn't create incomplete feature (orphaned dependencies)
3. Continue with P1, then P2 stories
4. Stop when capacity reached or no more valid stories

**Example Selection:**
```
Sprint 1 Commitment:
1. story-auth-001 (Signup) - 5 points
2. story-auth-002 (Login) - 3 points  
3. story-auth-003 (Logout) - 1 point
4. story-profile-001 (View Profile) - 2 points
5. story-profile-002 (Edit Profile) - 3 points
6. story-settings-001 (Change Password) - 2 points

Total: 16 points / 17 available (94% utilization)
Remaining: 1 point (buffer + small reserve)
```

**Reference:** See [story-selection-algorithm.md](references/story-selection-algorithm.md) for selection rules and edge cases.

---

### Step 3: Validate Dependencies

**Purpose:** Ensure no broken dependencies in sprint plan.

**Validation Checks:**

1. **Blocker Check:** All blocking stories either:
   - Included in current sprint (before blocked story)
   - Already completed (status = Done)

2. **Feature Completeness:** Avoid partial features:
   - If story A blocks B and C, either include all or none
   - Don't leave dependent stories orphaned

3. **Cross-Sprint Dependencies:** For multi-sprint plans:
   - Dependencies can span sprints (A in Sprint 1, B in Sprint 2)
   - But must be in correct order

**Example Validation:**
```
✓ All dependencies satisfied:
  - story-auth-001 (Sprint 1) blocks story-auth-002 (Sprint 1) ✓
  - story-auth-002 (Sprint 1) blocks story-profile-001 (Sprint 1) ✓
  - story-profile-001 (Sprint 1) blocks story-profile-002 (Sprint 1) ✓

✓ No orphaned dependencies
✓ Feature completeness maintained
```

---

### Step 4: Identify Risks and Mitigation

**Purpose:** Surface sprint risks and plan mitigation.

**Risk Categories:**

1. **Capacity Risk:** Sprint over/under-committed
   - Over: >95% utilization (no buffer for unknowns)
   - Under: <75% utilization (team under-utilized)

2. **Dependency Risk:** Critical path dependencies
   - Long chains (A → B → C → D)
   - Single blocker affecting many stories

3. **Technical Risk:** High-risk stories in sprint
   - Stories with risk score > 6 (from estimation)
   - Unproven technology or approach

4. **Scope Risk:** Too many P0 stories
   - Sprint becomes "all or nothing"
   - No flexibility for adjustments

**Example Risk Assessment:**
```
Sprint Risks:

⚠️ MEDIUM: Capacity Risk
- Utilization: 94% (high but acceptable)
- Mitigation: 1-point buffer available, can drop story-settings-001 if needed

⚠️ MEDIUM: Dependency Risk
- Critical path: auth-001 → auth-002 → profile-001 → profile-002 (4 stories)
- Mitigation: Prioritize auth-001 early in sprint, daily progress tracking

✓ LOW: Technical Risk
- Only 1 high-risk story (auth-001, risk=7)
- Mitigation: Pair programming, technical spike planned

✓ LOW: Scope Risk
- 3 P0 stories out of 6 total (50%)
- Flexibility: Can defer profile-002 or settings-001 if needed
```

**Reference:** See [sprint-risk-assessment.md](references/sprint-risk-assessment.md) for risk scoring methodology.

---

### Step 5: Define Sprint Goal

**Purpose:** Articulate clear, measurable sprint goal.

**Sprint Goal Formula:**
```
[Action Verb] [Feature/Outcome] so that [Business Value]
```

**Examples:**
- "Implement core authentication so that users can securely access the platform"
- "Enable user profile management so that users can personalize their experience"
- "Complete payment integration so that customers can purchase products"

**Good Sprint Goals:**
- **Specific:** Clear what will be delivered
- **Measurable:** Can verify if goal achieved
- **Valuable:** Business value is clear
- **Achievable:** Realistic given velocity
- **Focused:** 1-2 main themes, not scattered

**Poor Sprint Goals:**
- ❌ "Complete as many stories as possible"
- ❌ "Work on authentication and profiles and settings and..."
- ❌ "Make progress on the backlog"

**Example for Our Sprint:**
```
Sprint 1 Goal:
"Implement core authentication and basic profile management so that users can securely 
register, log in, and view/edit their profiles."

Success Criteria:
- Users can sign up with email/password
- Users can log in and log out
- Users can view and edit their profile
- All authentication flows are secure (bcrypt, JWT, rate limiting)
```

**Reference:** See [sprint-goals-and-metrics.md](references/sprint-goals-and-metrics.md) for goal-setting patterns.

---

### Step 6: Calculate Sprint Metrics

**Purpose:** Provide quantitative sprint health indicators.

**Key Metrics:**

1. **Commitment:** Total story points committed
2. **Utilization:** Percentage of velocity used
3. **P0 Coverage:** Percentage of P0 stories included
4. **Dependency Depth:** Longest dependency chain
5. **Risk Score:** Weighted average of story risks

**Example Metrics:**
```yaml
Sprint Metrics:

Capacity:
  velocity: 20
  buffer: 3 (15%)
  effectiveCapacity: 17
  commitment: 16
  utilization: 94%
  remaining: 1

Stories:
  total: 6
  p0: 3 (50%)
  p1: 2 (33%)
  p2: 1 (17%)

Dependencies:
  totalRelationships: 4
  longestChain: 4 (auth-001 → auth-002 → profile-001 → profile-002)
  averageDepth: 2

Risk:
  averageRiskScore: 4.2/10
  highRiskStories: 1
  overallRisk: MEDIUM
```

---

### Step 7: Generate Sprint Plan Document

**Purpose:** Create comprehensive sprint plan file.

**File:** `.claude/sprints/sprint-{sprint-name}-{date}.md`

**Sprint Plan Structure:**
```markdown
# Sprint Plan: {Sprint Name}

**Sprint Dates:** {start-date} to {end-date}
**Velocity:** {velocity} points
**Commitment:** {commitment} points ({utilization}% utilization)
**Status:** Planned

---

## Sprint Goal

{Sprint goal statement}

**Success Criteria:**
- {Criterion 1}
- {Criterion 2}
- {Criterion 3}

---

## Committed Stories

| Story ID | Title | Priority | Points | Dependencies |
|----------|-------|----------|--------|--------------|
| story-auth-001 | User Signup | P0 | 5 | None |
| story-auth-002 | User Login | P0 | 3 | auth-001 |
| story-auth-003 | User Logout | P0 | 1 | auth-002 |
| story-profile-001 | View Profile | P1 | 2 | auth-002 |
| story-profile-002 | Edit Profile | P1 | 3 | profile-001 |
| story-settings-001 | Change Password | P1 | 2 | auth-002 |

**Total:** 16 points

---

## Sprint Metrics

{Metrics from Step 6}

---

## Risks and Mitigation

{Risks from Step 4}

---

## Sprint Schedule (Recommended)

**Week 1:**
- Days 1-2: story-auth-001 (Signup) - 5 points
- Days 3-4: story-auth-002 (Login) - 3 points
- Day 5: story-auth-003 (Logout) - 1 point

**Week 2:**
- Days 1-2: story-profile-001 (View Profile) - 2 points
- Days 3-4: story-profile-002 (Edit Profile) - 3 points
- Day 5: story-settings-001 (Change Password) - 2 points

---

## Definition of Done (Sprint-Level)

- [ ] All committed stories meet their individual DoD
- [ ] Sprint goal achieved
- [ ] No critical/high bugs remain
- [ ] Code reviewed and merged
- [ ] Documentation updated
- [ ] Demo prepared for stakeholders

---

**Generated:** {date}
**Planner:** Alex (Planning Agent)
```

**Reference:** See [sprint-plan-template.md](references/sprint-plan-template.md) for complete template.

---

### Step 8: Multi-Sprint Planning (Optional)

**Purpose:** Plan 2-4 sprints ahead for roadmap visibility.

**When to Use:**
- plan_ahead parameter > 1
- Creating quarterly roadmap
- Long-range feature planning

**Process:**
1. Plan Sprint 1 (as above)
2. Mark Sprint 1 stories as "allocated"
3. Repeat Steps 1-7 for Sprint 2 with remaining stories
4. Continue for Sprint 3, 4 as needed

**Multi-Sprint Output:**
```
Sprint 1 (20 points): Core Authentication
- 6 stories, 16 points committed

Sprint 2 (20 points): Advanced Features
- 5 stories, 18 points committed

Sprint 3 (20 points): Integration & Polish
- 4 stories, 15 points committed

Total Roadmap: 15 stories, 49 points across 3 sprints
```

**Reference:** See [sprint-planning-mechanics.md](references/sprint-planning-mechanics.md) for multi-sprint algorithm.

---

### Step 9: Present Sprint Plan Summary

**Purpose:** Communicate sprint plan clearly to team.

**Summary Format:**
```
✅ Sprint Plan Complete

Sprint: Sprint 1
Dates: Jan 20 - Feb 2, 2025 (2 weeks)

Commitment:
- Stories: 6 (3 P0, 2 P1, 1 P2)
- Points: 16 / 17 available (94% utilization)
- Buffer: 1 point remaining

Sprint Goal:
"Implement core authentication and basic profile management so that users can 
securely register, log in, and view/edit their profiles."

Top Stories:
1. story-auth-001: User Signup (5 pts, P0)
2. story-auth-002: User Login (3 pts, P0)  
3. story-auth-003: User Logout (1 pt, P0)
4. story-profile-001: View Profile (2 pts, P1)
5. story-profile-002: Edit Profile (3 pts, P1)
6. story-settings-001: Change Password (2 pts, P1)

Risks: 2 MEDIUM (capacity, dependencies), 0 HIGH

Sprint Plan: .claude/sprints/sprint-sprint-1-20250120.md

Next Steps:
1. Review sprint plan with team
2. Begin Sprint 1 on Jan 20
3. Start with story-auth-001 (highest priority)
```

---

## Integration with Other Skills

**Before Sprint Planning:**
- `breakdown-epic` → Create stories from epics
- `refine-story` → Ensure stories are sprint-ready
- `estimate-stories` → Estimate story points

**After Sprint Planning:**
- `implement-feature` → Implement stories from sprint
- `review-task` → Quality check completed stories
- (Next sprint) → `sprint-plan` again with updated velocity

---

## Best Practices

1. **Respect Velocity:** Don't over-commit (keep 10-15% buffer)
2. **Honor Dependencies:** Never break dependency chains
3. **Focus on Value:** Prioritize P0/P1 stories over P2/P3
4. **Balance Risk:** Mix high-risk and low-risk stories
5. **Complete Features:** Avoid half-done features across sprint boundaries
6. **Review and Adapt:** Update velocity based on actual completion

**Reference:** See [sprint-goals-and-metrics.md](references/sprint-goals-and-metrics.md) for planning best practices.

---

## References

- [sprint-planning-mechanics.md](references/sprint-planning-mechanics.md) - Capacity calculation, multi-sprint algorithm, velocity tracking
- [story-selection-algorithm.md](references/story-selection-algorithm.md) - Sorting criteria, selection rules, edge cases
- [sprint-risk-assessment.md](references/sprint-risk-assessment.md) - Risk categories, scoring methodology, mitigation strategies
- [sprint-goals-and-metrics.md](references/sprint-goals-and-metrics.md) - Goal-setting patterns, metrics definitions, best practices
