# Sprint Feasibility Validation Criteria

## Purpose

Comprehensive validation checks to ensure sprint plans are achievable, well-balanced, and set up for success.

---

## 1. Capacity Validation

### Check: Committed Points ≤ Available Capacity

**Rule:**
```
Committed Points ≤ Sprint Capacity
Sprint Capacity = Velocity × (1 - Buffer)
```

**Example:**
```
Velocity: 20 points
Buffer: 15%
Sprint Capacity: 17 points

Committed: 16 points ✓ (94% utilization)
Committed: 18 points ❌ (106% - overcommitted)
```

### Target Utilization Ranges

| Utilization | Status | Interpretation |
|------------|--------|----------------|
| **<70%** | ⚠️ Undercommitment | Team likely idle, wasting capacity |
| **70-79%** | ⚠️ Conservative | Safe but may be too cautious |
| **80-89%** | ✅ Good | Healthy commitment with buffer |
| **90-95%** | ✅ Optimal | Maximum value without overcommitment |
| **95-100%** | ⚠️ Aggressive | Little buffer, risky |
| **>100%** | ❌ Overcommitted | Team will likely miss commitment |

**Validation Output:**
```
Capacity Validation:
✓ Committed: 16 points
✓ Available: 17 points
✓ Utilization: 94% (Optimal)
✓ Buffer Remaining: 1 point

Status: PASS
```

---

## 2. Dependency Validation

### Check: All Dependencies Satisfied

**Rule:** For every story in sprint, all dependencies must be:
- In the same sprint (and earlier in execution order), OR
- In a previous sprint (already committed), OR
- Already completed (status = "Done")

**Validation Algorithm:**
```
function validateDependencies(sprint, previousSprints):
  violations = []

  for each story in sprint:
    for each dep in story.blocked_by:
      satisfied = false

      # Check if dependency is complete
      if dep.status == "Done":
        satisfied = true

      # Check if in previous sprints
      else if dep in previousSprints:
        satisfied = true

      # Check if in current sprint (and earlier)
      else if dep in sprint:
        depIndex = sprint.indexOf(dep)
        storyIndex = sprint.indexOf(story)
        if depIndex < storyIndex:
          satisfied = true

      if not satisfied:
        violations.add({
          story: story.id,
          dependency: dep.id,
          issue: "Dependency not satisfied"
        })

  return violations
```

**Example Output:**
```
Dependency Validation:

✓ story-auth-001 (Signup) - No dependencies
✓ story-auth-002 (Login) - Blocked by auth-001 (in sprint, order OK)
✓ story-auth-003 (Logout) - Blocked by auth-001 (in sprint, order OK)
✓ story-profile-001 (View) - Blocked by auth-002 (in sprint, order OK)
❌ story-profile-002 (Edit) - Blocked by settings-001 (NOT IN SPRINT)

Status: FAIL - 1 dependency violation
Action Required: Add settings-001 or defer profile-002 to next sprint
```

### Circular Dependency Check

**Rule:** No circular dependencies allowed.

**Output:**
```
Circular Dependency Check:
✓ No cycles detected

Dependency Graph:
  auth-001 → auth-002 → profile-001
          ↓
        auth-003
```

---

## 3. Risk Balance Validation

### Check: Overall Sprint Risk Score in Acceptable Range

**Risk Calculation:**
```
Story Risk: 0-10 scale (estimated during story refinement)

Sprint Risk Score = Σ(story.risk × story.points) / Σ(story.points)

Example:
  story-auth-001 (5 pts, risk 3) = 15 risk-points
  story-auth-002 (3 pts, risk 2) = 6 risk-points
  story-profile-001 (5 pts, risk 5) = 25 risk-points

Sprint Risk = (15 + 6 + 25) / (5 + 3 + 5) = 46 / 13 = 3.5
```

### Risk Score Ranges

| Risk Score | Status | Interpretation | Action |
|------------|--------|----------------|--------|
| **0-2** | ⚠️ Too Low | No challenging work, team bored | Add stretch goals |
| **3-5** | ✅ Good | Balanced risk, sustainable | None |
| **6-7** | ⚠️ High | Risky sprint, may need support | Mitigation plan |
| **8-10** | ❌ Very High | High failure probability | Reduce scope or defer |

**Validation Output:**
```
Risk Balance Validation:

Overall Risk Score: 3.5/10 (Good)

Risk Breakdown:
  Low Risk (0-3): 2 stories (8 points, 47%)
  Medium Risk (4-6): 3 stories (9 points, 53%)
  High Risk (7-10): 0 stories (0 points, 0%)

High-Risk Stories:
  None

Status: PASS
Recommendation: Risk well-balanced
```

### High-Risk Story Limit

**Rule:** No more than 30% of sprint capacity should be high-risk stories.

**Example:**
```
Sprint Capacity: 17 points
High-Risk Limit: 17 × 0.30 = 5 points

Actual High-Risk: 0 points ✓
Status: PASS
```

---

## 4. Priority Balance Validation

### Check: Appropriate Mix of Priorities

**Target Distribution:**
```
P0 (Must Have): ≥50% of capacity
P1 (High):       30-40% of capacity
P2 (Medium):     ≤20% of capacity
P3 (Low):        0-10% of capacity
```

**Validation:**
```
function validatePriorityBalance(sprint, capacity):
  p0Points = sum(story.points where priority = "P0")
  p1Points = sum(story.points where priority = "P1")
  p2Points = sum(story.points where priority = "P2")
  p3Points = sum(story.points where priority = "P3")

  p0Percentage = p0Points / capacity
  p1Percentage = p1Points / capacity
  p2Percentage = p2Points / capacity

  issues = []

  if p0Percentage < 0.50:
    issues.add("Warning: Too little P0 work ({p0Percentage})")

  if p2Percentage > 0.20:
    issues.add("Warning: Too much P2 work ({p2Percentage})")

  return issues
```

**Example Output:**
```
Priority Balance Validation:

Distribution:
  P0 (Must Have):  10 points (59%) ✓ [Target: ≥50%]
  P1 (High):        7 points (41%) ✓ [Target: 30-40%]
  P2 (Medium):      0 points (0%)  ✓ [Target: ≤20%]

Status: PASS
Recommendation: Priority balance is healthy
```

**Warning Cases:**
```
Case 1: Too Little P0 Work
  P0: 6 points (35%) ⚠️
  Issue: Not enough critical work
  Action: Prioritize must-have features

Case 2: Too Much P2 Work
  P2: 5 points (29%) ⚠️
  Issue: Too much low-priority work
  Action: Focus on high-value features
```

---

## 5. Team Capacity Validation

### Check: Workload Balanced Across Team Skills

**Rule:** No skill should be overloaded >20% more than others.

**Validation:**
```
function validateTeamBalance(sprint, team):
  skillLoad = {}

  for each skill in ["frontend", "backend", "devops", "fullstack"]:
    pointsForSkill = sum(story.points where story.primarySkill == skill)
    membersWithSkill = team.membersWithSkill(skill)
    loadPerMember = pointsForSkill / membersWithSkill

    skillLoad[skill] = {
      points: pointsForSkill,
      members: membersWithSkill,
      loadPerMember: loadPerMember
    }

  avgLoad = average(skillLoad.loadPerMember)
  issues = []

  for each skill in skillLoad:
    deviation = (skillLoad[skill].loadPerMember - avgLoad) / avgLoad

    if deviation > 0.20:
      issues.add("Warning: {skill} overloaded by {deviation}%")

    if deviation < -0.20:
      issues.add("Info: {skill} underutilized by {deviation}%")

  return issues
```

**Example Output:**
```
Team Capacity Validation:

Team: 3 developers
  - 2 frontend (Alice, Bob)
  - 2 backend (Bob, Charlie)
  - 1 devops (Charlie)

Skill Workload:
  Frontend:  12 points / 2 members = 6 pts/member
  Backend:    5 points / 2 members = 2.5 pts/member ⚠️
  Devops:     0 points / 1 member = 0 pts/member

Average Load: 4.25 pts/member

Deviation:
  Frontend: +41% (overloaded) ⚠️
  Backend:  -41% (underutilized)
  Devops:   -100% (idle)

Status: WARNING - Skill imbalance detected
Recommendation: Swap frontend story for backend story
  Consider replacing story-ui-002 (3 pts FE) with story-api-003 (3 pts BE)
```

---

## 6. Story Size Validation

### Check: All Stories Are Appropriately Sized

**Rule:** Stories should be ≤13 points (Small enough for one sprint).

**Validation:**
```
function validateStorySizes(sprint):
  oversized = []

  for each story in sprint:
    if story.points > 13:
      oversized.add({
        story: story.id,
        points: story.points,
        issue: "Story too large (>13 points)"
      })

  return oversized
```

**Example Output:**
```
Story Size Validation:

✓ story-auth-001 (5 points)
✓ story-auth-002 (3 points)
✓ story-profile-001 (5 points)
✓ story-profile-002 (3 points)

Status: PASS
All stories appropriately sized
```

**Warning Case:**
```
Story Size Validation:

✓ story-auth-001 (5 points)
❌ story-dashboard-001 (21 points) - TOO LARGE

Status: FAIL
Action Required: Split story-dashboard-001 into smaller stories
```

---

## 7. Epic Coherence Validation

### Check: Epics Are Either Complete or Logically Split

**Preferred:** Complete entire epic in one sprint.
**Acceptable:** Split epic across sprints with clear boundaries.
**Avoid:** Random partial epic completion.

**Validation:**
```
function validateEpicCoherence(sprint, allStories):
  epics = groupByEpic(allStories)
  issues = []

  for each epic in epics:
    storiesInSprint = sprint.filter(s => s.epic == epic.id)
    totalStoriesInEpic = epic.stories.length

    if storiesInSprint.length > 0 and storiesInSprint.length < totalStoriesInEpic:
      # Epic is partially included
      completionRate = storiesInSprint.length / totalStoriesInEpic

      if completionRate < 0.50:
        issues.add("Warning: Epic '{epic.name}' only {completionRate}% included")

  return issues
```

**Example Output:**
```
Epic Coherence Validation:

Authentication Epic:
  Total Stories: 3
  In Sprint: 3 (100%) ✓ COMPLETE

Profile Epic:
  Total Stories: 4
  In Sprint: 2 (50%) ⚠️ PARTIAL

Settings Epic:
  Total Stories: 2
  In Sprint: 0 (0%) ✓ NOT STARTED

Status: WARNING - Profile epic partially complete
Recommendation: Consider deferring profile-003 and profile-004 to Sprint 2
```

---

## 8. Velocity Historical Consistency

### Check: Sprint Commitment Consistent with Historical Velocity

**Rule:** Committed points should be within ±20% of historical velocity.

**Validation:**
```
function validateVelocityConsistency(sprint, historicalVelocity):
  committed = sum(story.points for story in sprint)

  lowerBound = historicalVelocity × 0.80
  upperBound = historicalVelocity × 1.20

  if committed < lowerBound:
    return "WARNING: Undercommitment ({committed} vs {historicalVelocity} historical)"

  if committed > upperBound:
    return "WARNING: Overcommitment ({committed} vs {historicalVelocity} historical)"

  return "PASS: Commitment consistent with historical velocity"
```

**Example Output:**
```
Velocity Consistency Check:

Historical Velocity: [18, 22, 20, 19] → Average: 19.75
Current Sprint Commitment: 17 points

Range: 15.8 - 23.7 points (±20%)
Status: ✓ PASS (17 within range)
```

---

## Summary Validation Report

### Overall Feasibility Assessment

**Template:**
```markdown
# Sprint Feasibility Report

**Sprint:** Sprint 1
**Date:** 2025-01-15

## Validation Results

| Check | Status | Details |
|-------|--------|---------|
| Capacity | ✅ PASS | 94% utilization (16/17 points) |
| Dependencies | ✅ PASS | All dependencies satisfied |
| Risk Balance | ✅ PASS | Risk score 3.5/10 (Good) |
| Priority Balance | ✅ PASS | P0=59%, P1=41% (Healthy) |
| Team Capacity | ⚠️ WARNING | Frontend overloaded (+41%) |
| Story Size | ✅ PASS | All stories ≤13 points |
| Epic Coherence | ⚠️ WARNING | Profile epic 50% complete |
| Velocity Consistency | ✅ PASS | 17 pts within historical range |

## Overall Feasibility: FEASIBLE with Minor Concerns

**Pass Rate:** 6/8 checks passed (75%)

## Recommendations:
1. Swap story-ui-002 (FE) for story-api-003 (BE) to balance team workload
2. Consider deferring profile-003 and profile-004 to complete epic in Sprint 2

## Action Required:
- [ ] Review team workload balance with team leads
- [ ] Decide on profile epic completion strategy
```

---

*Part of sprint-plan skill - BMAD Enhanced*
