# Sprint Planning Parameters Guide

## Purpose

Guidelines for calculating sprint capacity, velocity, and buffer sizing for effective sprint planning.

---

## Team Velocity

### Definition
**Velocity**: The amount of work (story points) a team can complete in one sprint, based on historical data or initial estimates.

### Calculating Historical Velocity

**Formula:**
```
Velocity = Average(story points completed per sprint over last 3-5 sprints)
```

**Example:**
```
Sprint 1: 22 points completed
Sprint 2: 18 points completed
Sprint 3: 20 points completed
Sprint 4: 19 points completed

Velocity = (22 + 18 + 20 + 19) / 4 = 19.75 ≈ 20 points
```

### Initial Velocity Estimation (New Teams)

When no historical data exists:

**Method 1: Team Capacity-Based**
```
Velocity = Team Size × Available Days × Points per Day

Example:
- 3 developers
- 8 available days per sprint (2 weeks - meetings/support)
- 1 point ≈ 3 hours of work
- 8 hours per day / 3 hours per point = 2.67 points per day

Velocity = 3 × 8 × 2.67 ≈ 64 points
```

**Method 2: Conservative Start**
```
Start with: 5-8 points per developer per sprint

For 3-person team: 15-24 points initial velocity
```

**Recommendation:** Start conservatively (15-20 points for 3-person team) and adjust after 2-3 sprints.

---

## Sprint Capacity Calculation

### Capacity Formula
```
Sprint Capacity = Velocity × (1 - Buffer)
```

**Example:**
```
Velocity: 20 points
Buffer: 15% (0.15)
Sprint Capacity = 20 × (1 - 0.15) = 20 × 0.85 = 17 points
```

### Buffer Sizing Guidelines

| Buffer % | Use Case | Risk Tolerance |
|----------|----------|----------------|
| **10%** | Stable team, mature product, low unknowns | High confidence |
| **15%** | **Standard** - most teams, balanced | Medium confidence |
| **20%** | New team, high complexity, many unknowns | Low confidence |
| **25%** | Brownfield, tech debt heavy, frequent interruptions | Very low confidence |

**Buffer Purposes:**
- Production hotfixes
- Unplanned support requests
- Estimation errors
- Technical unknowns
- Team member availability (sick, vacation)

---

## Sprint Duration

### Standard Durations

**2 Weeks (10 working days):**
- Most common
- Good balance of planning overhead vs. flexibility
- Enough time to complete meaningful work
- Frequent feedback cycles

**1 Week (5 working days):**
- Fast-paced projects
- High uncertainty requiring frequent pivots
- Small stories only (1-3 points)

**3 Weeks (15 working days):**
- Longer stories acceptable (8-13 points)
- Less planning overhead
- Slower feedback cycles

**Recommendation:** Start with 2 weeks for most teams.

---

## Available Capacity Per Developer

### Calculating Available Hours

**Formula:**
```
Available Hours = Sprint Days × Hours per Day × Availability Factor
```

**Example (2-week sprint):**
```
Sprint Days: 10 days
Hours per Day: 8 hours
Availability Factor: 0.75 (25% for meetings, emails, support)

Available Hours = 10 × 8 × 0.75 = 60 hours per developer
```

### Availability Factors

| Factor | Scenario |
|--------|----------|
| **0.80** | Senior team, minimal meetings, few distractions |
| **0.75** | Standard - includes daily standup, refinement, retro |
| **0.70** | Many meetings, support-heavy, context switching |
| **0.60** | Heavy operational load, on-call rotation |

### Converting Hours to Story Points

**Common Scales:**
```
1 point = 2-3 hours
2 points = 4-6 hours (half day)
3 points = 1 day
5 points = 2-3 days
8 points = 3-5 days
13 points = 5+ days (should be split)
```

**Example Calculation:**
```
Developer Available: 60 hours per sprint
1 point = 3 hours

Capacity per Developer = 60 / 3 = 20 points
```

---

## Team Size Considerations

### Small Team (2-3 developers)
- **Velocity:** 15-30 points
- **Sprint Capacity:** 12-25 points (with buffer)
- **Story Count:** 3-6 stories per sprint
- **Challenges:** Limited parallel work, single points of failure
- **Advantages:** Fast communication, easy coordination

### Medium Team (4-6 developers)
- **Velocity:** 30-60 points
- **Sprint Capacity:** 25-50 points
- **Story Count:** 6-12 stories per sprint
- **Challenges:** Coordination overhead, merge conflicts
- **Advantages:** Parallel streams, skill diversity

### Large Team (7+ developers)
- **Velocity:** 60+ points
- **Sprint Capacity:** 50+ points
- **Story Count:** 12+ stories per sprint
- **Challenges:** High coordination cost, communication complexity
- **Advantages:** High throughput, specialized roles
- **Recommendation:** Consider splitting into sub-teams

---

## Configuration Example

**File:** `.claude/config.yaml`

```yaml
team:
  size: 3
  velocity_historical: [18, 22, 20, 19]  # Last 4 sprints
  velocity_current: 20  # Average
  sprint_duration: 2  # weeks
  buffer_percentage: 0.15  # 15%
  availability_factor: 0.75

sprint_defaults:
  capacity: 17  # 20 × 0.85
  start_day: "Monday"
  duration_weeks: 2
  target_utilization: 0.85  # 85%
```

---

## Adjusting Velocity Over Time

### When to Increase Velocity
- Team consistently completes all committed stories
- Capacity utilization >95% for 3+ sprints
- Team requests more work
- Technical debt reduced

**Adjustment:** Increase by 10-15% (e.g., 20 → 22 points)

### When to Decrease Velocity
- Team frequently misses sprint commitments
- Capacity utilization <70% consistently
- Technical debt increasing
- Team expressing burnout

**Adjustment:** Decrease by 10-15% (e.g., 20 → 17 points)

### When to Keep Velocity Stable
- Capacity utilization 80-95%
- Predictable delivery
- Team satisfied with pace

---

## Multi-Sprint Planning Parameters

### Planning Ahead (2-3 Sprints)

**Velocity Trends:**
```
If velocity increasing (18 → 20 → 22):
  Use conservative estimate (20) for future sprints

If velocity stable (20 → 19 → 20):
  Use current velocity (20)

If velocity decreasing (22 → 20 → 18):
  Use lower estimate (18) and investigate causes
```

**Buffer Increase for Future Sprints:**
```
Current Sprint: 15% buffer
Next Sprint: 15% buffer
Sprint 3+: 20% buffer (more uncertainty)
```

---

*Part of sprint-plan skill - BMAD Enhanced*
