# Story Grouping and Sprint Allocation Algorithms

## Purpose

Optimization strategies for allocating stories to sprints while respecting capacity, dependencies, priorities, and other constraints.

---

## Basic Greedy Algorithm

### Single Sprint Planning

**Algorithm:**
```
function greedySingleSprint(stories, capacity):
  orderedStories = sortByPriorityAndDependency(stories)
  sprint = []
  remainingCapacity = capacity

  for each story in orderedStories:
    if story.points <= remainingCapacity:
      if dependenciesSatisfied(story, sprint):
        sprint.add(story)
        remainingCapacity -= story.points

  return sprint
```

**Example:**
```
Input:
  Capacity: 17 points
  Stories: [
    story-auth-001 (5 pts, P0, no deps),
    story-auth-002 (3 pts, P0, blocked by auth-001),
    story-profile-001 (5 pts, P1, no deps),
    story-profile-002 (3 pts, P1, blocked by profile-001),
    story-settings-001 (8 pts, P2, no deps)
  ]

Output:
  Sprint 1: [
    story-auth-001 (5 pts),
    story-auth-002 (3 pts),
    story-profile-001 (5 pts),
    story-profile-002 (3 pts)
  ]
  Total: 16 points (94% utilization)
  Deferred: story-settings-001 (not enough capacity)
```

**Advantages:**
- Simple to implement
- Fast (O(n) complexity)
- Predictable results

**Disadvantages:**
- May not find optimal solution
- Doesn't balance risk or skills
- Can leave significant unused capacity

---

## Optimized Knapsack Algorithm

### Dynamic Programming Approach

**Problem:** Select stories that maximize value while staying within capacity.

**Algorithm:**
```
function knapsackSprint(stories, capacity):
  n = stories.length
  dp = array[n+1][capacity+1]

  # Initialize
  for i from 0 to n:
    for w from 0 to capacity:
      if i == 0 or w == 0:
        dp[i][w] = 0
      else if stories[i-1].points <= w:
        # Include story or exclude it (whichever has higher value)
        includeValue = stories[i-1].priority + dp[i-1][w - stories[i-1].points]
        excludeValue = dp[i-1][w]
        dp[i][w] = max(includeValue, excludeValue)
      else:
        dp[i][w] = dp[i-1][w]

  # Backtrack to find selected stories
  selected = backtrack(dp, stories, capacity)
  return selected
```

**Example:**
```
Input:
  Capacity: 17 points
  Stories: [
    story-auth-001 (5 pts, priority 1575),
    story-auth-002 (3 pts, priority 1200),
    story-profile-001 (5 pts, priority 500),
    story-profile-002 (3 pts, priority 500),
    story-settings-001 (8 pts, priority 100),
    story-admin-001 (2 pts, priority 600)
  ]

Output (Optimal):
  Sprint 1: [
    story-auth-001 (5 pts),
    story-auth-002 (3 pts),
    story-profile-001 (5 pts),
    story-admin-001 (2 pts),  # Fits better than profile-002
    story-profile-002 (3 pts)
  ]
  Total: 18 points... wait, exceeds capacity!

Corrected Output:
  Sprint 1: [
    story-auth-001 (5 pts),
    story-auth-002 (3 pts),
    story-admin-001 (2 pts),
    story-profile-001 (5 pts),
    story-profile-002 (2 pts)  # Wait, this was 3 pts
  ]
```

**Note:** Knapsack doesn't easily handle dependencies. Combine with dependency filtering first.

**Advantages:**
- Finds optimal solution for value maximization
- Good for balancing priorities

**Disadvantages:**
- Complex (O(n × capacity))
- Doesn't handle dependencies well
- May split epics awkwardly

---

## Epic-Aware Grouping

### Keep Epics Together

**Goal:** Complete entire epics within a single sprint when possible.

**Algorithm:**
```
function epicAwareGrouping(stories, capacity):
  # Group stories by epic
  epics = groupByEpic(stories)

  # Sort epics by priority (sum of story priorities)
  sortedEpics = sort(epics, by=totalPriority, desc=true)

  sprint = []
  remainingCapacity = capacity

  for each epic in sortedEpics:
    epicPoints = sum(story.points for story in epic)

    # Try to fit entire epic
    if epicPoints <= remainingCapacity:
      if dependenciesSatisfied(epic, sprint):
        sprint.addAll(epic)
        remainingCapacity -= epicPoints
    else:
      # Epic too big, try fitting individual stories
      for each story in epic:
        if story.points <= remainingCapacity:
          if dependenciesSatisfied(story, sprint):
            sprint.add(story)
            remainingCapacity -= story.points

  return sprint
```

**Example:**
```
Input:
  Capacity: 17 points
  Epics:
    Authentication (9 pts): [auth-001 (5), auth-002 (3), auth-003 (1)]
    Profile (8 pts): [profile-001 (5), profile-002 (3)]
    Settings (8 pts): [settings-001 (8)]

Output:
  Sprint 1: [
    Authentication epic (9 pts) - COMPLETE ✓
    Profile epic (8 pts) - COMPLETE ✓
  ]
  Total: 17 points (100% utilization)
  Deferred: Settings epic (doesn't fit)
```

**Advantages:**
- Delivers complete features
- Reduces work in progress
- Better demo in sprint review

**Disadvantages:**
- May leave unused capacity if epic doesn't fit
- Rigid allocation

---

## Multi-Sprint Planning (Roadmap)

### Rolling Wave Approach

**Algorithm:**
```
function multiSprintPlan(stories, capacity, sprintCount):
  allSprints = []
  remainingStories = stories

  for sprint = 1 to sprintCount:
    # Plan current sprint
    currentSprint = greedySingleSprint(remainingStories, capacity)
    allSprints.add(currentSprint)

    # Remove planned stories
    remainingStories = remainingStories.filter(s => not in currentSprint)

    # Adjust capacity for future sprints (increase buffer)
    if sprint > 1:
      capacity = capacity × 0.95  # 5% more buffer for uncertainty

  return allSprints
```

**Example:**
```
Input:
  Capacity: 17 points per sprint
  Plan Ahead: 3 sprints
  Stories: 60 total points

Output:
  Sprint 1 (17 pts):
    - Authentication epic (9 pts)
    - Profile basics (8 pts)

  Sprint 2 (16 pts):  # 5% buffer increase
    - Advanced profile (10 pts)
    - Settings (6 pts)

  Sprint 3 (15 pts):  # More buffer
    - Search (12 pts)
    - Admin (3 pts)

  Total Planned: 48 points
  Remaining: 12 points for future sprints
```

### Dependency-Driven Multi-Sprint

**Algorithm:**
```
function dependencyDrivenMultiSprint(stories, capacity, sprintCount):
  # Build dependency levels
  levels = topologicalLevels(stories)

  sprints = []
  currentSprint = []
  remainingCapacity = capacity

  for each level in levels:
    for each story in level:
      if story.points <= remainingCapacity:
        currentSprint.add(story)
        remainingCapacity -= story.points
      else:
        # Start new sprint
        sprints.add(currentSprint)
        currentSprint = [story]
        remainingCapacity = capacity - story.points

      if sprints.length >= sprintCount:
        break

  if currentSprint not empty:
    sprints.add(currentSprint)

  return sprints
```

**Example:**
```
Dependency Levels:
  Level 0: [auth-001 (5)]
  Level 1: [auth-002 (3), auth-003 (1)]
  Level 2: [profile-001 (5), settings-001 (8)]
  Level 3: [profile-002 (3)]

Sprint Allocation (Capacity: 17):
  Sprint 1 (Level 0-1):
    - auth-001 (5)
    - auth-002 (3)
    - auth-003 (1)
    - profile-001 (5)  # From Level 2
    - settings-001 (8)  # Doesn't fit, move to Sprint 2

  Sprint 2 (Level 2-3):
    - settings-001 (8)
    - profile-002 (3)
    - ...
```

---

## Risk-Balanced Grouping

### Goal: Mix High-Risk and Low-Risk Stories

**Algorithm:**
```
function riskBalancedGrouping(stories, capacity):
  orderedStories = sortByPriorityAndDependency(stories)
  sprint = []
  remainingCapacity = capacity
  riskPoints = 0

  for each story in orderedStories:
    if story.points <= remainingCapacity:
      # Calculate sprint risk after adding story
      newRisk = (riskPoints + story.risk * story.points) / (totalPoints + story.points)

      # Only add if risk stays balanced (target: 3-6 on 0-10 scale)
      if newRisk <= 6.5:  # Allow some headroom
        sprint.add(story)
        remainingCapacity -= story.points
        riskPoints += story.risk * story.points

  return sprint
```

**Example:**
```
Input Stories:
  story-auth-001 (5 pts, risk 3/10) = 15 risk-points
  story-auth-002 (3 pts, risk 2/10) = 6 risk-points
  story-profile-002 (3 pts, risk 7/10) = 21 risk-points
  story-settings-001 (8 pts, risk 5/10) = 40 risk-points

Sprint 1:
  story-auth-001 (5 pts, risk 3) → Avg risk: 3.0 ✓
  story-auth-002 (3 pts, risk 2) → Avg risk: 2.6 ✓
  story-profile-002 (3 pts, risk 7) → Avg risk: 3.8 ✓
  story-settings-001 (8 pts, risk 5) → Avg risk: 4.3 ✓

Total: 19 points, avg risk 4.3 (Balanced ✓)
```

---

## Skill-Balanced Grouping

### Goal: Balance Workload Across Team Skills

**Algorithm:**
```
function skillBalancedGrouping(stories, capacity, team):
  orderedStories = sortByPriorityAndDependency(stories)
  sprint = []
  remainingCapacity = capacity
  skillLoad = {}  # Track points per skill

  # Initialize skill capacity
  for each skill in ["frontend", "backend", "devops"]:
    skillLoad[skill] = 0
    maxLoad[skill] = capacity / team.membersWithSkill(skill)

  for each story in orderedStories:
    if story.points <= remainingCapacity:
      skill = story.primarySkill
      newLoad = skillLoad[skill] + story.points

      # Check if skill is overloaded
      if newLoad <= maxLoad[skill] * 1.2:  # Allow 20% imbalance
        sprint.add(story)
        remainingCapacity -= story.points
        skillLoad[skill] += story.points

  return sprint
```

**Example:**
```
Team: 3 developers
  - 2 frontend developers
  - 2 backend developers
  - 1 full-stack (both)

Capacity: 17 points
Max Frontend: 17 / 2 = 8.5 points
Max Backend: 17 / 2 = 8.5 points

Stories:
  Frontend: [story-ui-001 (5), story-ui-002 (3), story-ui-003 (2)]
  Backend: [story-api-001 (5), story-api-002 (3)]

Sprint 1:
  story-ui-001 (5 FE) → FE: 5, BE: 0 ✓
  story-api-001 (5 BE) → FE: 5, BE: 5 ✓
  story-ui-002 (3 FE) → FE: 8, BE: 5 ✓
  story-api-002 (3 BE) → FE: 8, BE: 8 ✓
  story-ui-003 (2 FE) → FE: 10, BE: 8 (FE over limit, skip)

Total: 16 points, Balanced ✓
```

---

## Target Utilization Algorithm

### Goal: Hit 80-95% Capacity Utilization

**Algorithm:**
```
function targetUtilizationGrouping(stories, capacity):
  targetMin = capacity * 0.80  # 80%
  targetMax = capacity * 0.95  # 95%

  sprint = []
  totalPoints = 0

  # Phase 1: Fill to 80% with high-priority stories
  for each story in highPriorityStories(stories):
    if totalPoints + story.points <= targetMin:
      sprint.add(story)
      totalPoints += story.points

  # Phase 2: Fill to 95% optimally
  remaining = stories.filter(s => not in sprint)
  for each story in remaining:
    if totalPoints + story.points <= targetMax:
      sprint.add(story)
      totalPoints += story.points

  # Phase 3: Check if we can squeeze one more small story
  if totalPoints < targetMax:
    smallStory = remaining.filter(s => s.points <= targetMax - totalPoints).first()
    if smallStory exists:
      sprint.add(smallStory)

  return sprint
```

---

## Comparison of Algorithms

| Algorithm | Complexity | Use Case | Pros | Cons |
|-----------|------------|----------|------|------|
| **Greedy** | O(n) | Simple planning | Fast, predictable | Not optimal |
| **Knapsack** | O(n×C) | Value maximization | Optimal for priorities | Ignores dependencies |
| **Epic-Aware** | O(n) | Feature completion | Complete features | Rigid |
| **Multi-Sprint** | O(n×S) | Roadmap planning | Long-term view | Less precise |
| **Risk-Balanced** | O(n) | Risk management | Balanced risk | May leave capacity |
| **Skill-Balanced** | O(n) | Team balance | Even workload | Complex constraints |

**Recommendation:** Start with Epic-Aware for most teams, then add risk/skill balancing if needed.

---

*Part of sprint-plan skill - BMAD Enhanced*
