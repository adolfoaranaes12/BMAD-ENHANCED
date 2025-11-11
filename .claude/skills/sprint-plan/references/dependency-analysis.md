# Dependency Analysis and Resolution

## Purpose

Algorithms and techniques for analyzing story dependencies, detecting issues, and ordering stories for sprint planning.

---

## Dependency Types

### 1. Hard Dependencies (Blocking)
**blocked_by**: Story A cannot start until Story B is complete.

**Example:**
```yaml
story-auth-002:  # Login
  blocked_by: [story-auth-001]  # Cannot login without signup
```

### 2. Soft Dependencies (Preferred)
**depends_on**: Story A could start, but it's better to wait for Story B.

**Example:**
```yaml
story-profile-002:  # Edit Profile
  depends_on: [story-profile-001]  # Better after View Profile, but not required
```

### 3. Blocking Others
**blocks**: Story A blocks progress on Story B.

**Example:**
```yaml
story-auth-001:  # Signup
  blocks: [story-auth-002, story-auth-003]  # Login and Logout depend on signup
```

---

## Building Dependency Graph

### Step 1: Parse Dependencies from Story Files

**Input:** All story files in `.claude/stories/`

**Parse YAML frontmatter:**
```yaml
---
id: story-auth-002
title: User Login
blocked_by: [story-auth-001]
blocks: [story-profile-001]
status: Ready
points: 3
---
```

**Extract:**
- Story ID: `story-auth-002`
- Blocked by: `[story-auth-001]`
- Blocks: `[story-profile-001]`

### Step 2: Create Directed Graph

**Graph Structure:**
```
Node: Story ID
Edge: Dependency relationship (A → B means "A blocks B")

Example:
story-auth-001 → story-auth-002 → story-profile-001
              ↓
         story-auth-003
```

**Data Structure:**
```javascript
dependencies = {
  "story-auth-001": {
    blockedBy: [],
    blocks: ["story-auth-002", "story-auth-003"]
  },
  "story-auth-002": {
    blockedBy: ["story-auth-001"],
    blocks: ["story-profile-001"]
  },
  "story-auth-003": {
    blockedBy: ["story-auth-001"],
    blocks: []
  }
}
```

---

## Dependency Issue Detection

### 1. Circular Dependencies

**Problem:** Story A blocks B, B blocks C, C blocks A (cycle).

**Detection Algorithm (DFS-based):**
```
function detectCycles(graph):
  visited = {}
  recursionStack = {}

  for each node in graph:
    if not visited[node]:
      if hasCycle(node, visited, recursionStack):
        return CYCLE_DETECTED

  return NO_CYCLES

function hasCycle(node, visited, stack):
  visited[node] = true
  stack[node] = true

  for each neighbor in node.blocks:
    if not visited[neighbor]:
      if hasCycle(neighbor, visited, stack):
        return true
    else if stack[neighbor]:
      return true  # Cycle found

  stack[node] = false
  return false
```

**Example Output:**
```
❌ Circular Dependency Detected:
  story-auth-001 → story-profile-001 → story-settings-001 → story-auth-001

Resolution Required: Remove one dependency to break cycle.
```

### 2. Missing Dependencies

**Problem:** Story references non-existent dependency.

**Detection:**
```
for each story:
  for each dep in story.blocked_by:
    if dep not in all_stories:
      ERROR: Missing dependency
```

**Example Output:**
```
❌ Missing Dependency:
  story-auth-002 blocked by story-auth-999 (NOT FOUND)

Resolution: Remove invalid dependency or create missing story.
```

### 3. Long Dependency Chains

**Problem:** Story has deep chain (A → B → C → D → E).

**Detection:**
```
function maxDepth(story):
  if story.blocked_by.isEmpty():
    return 0

  max = 0
  for each dep in story.blocked_by:
    depth = maxDepth(dep) + 1
    if depth > max:
      max = depth

  return max

for each story:
  depth = maxDepth(story)
  if depth > 3:
    WARNING: Long dependency chain
```

**Example Output:**
```
⚠️ Long Dependency Chain (4 levels):
  story-payment-003 → story-payment-002 → story-auth-002 → story-auth-001

Risk: If first story is delayed, all 4 stories slip.
Recommendation: Consider alternative approach or parallelize work.
```

---

## Dependency-Aware Story Ordering

### Priority Calculation with Dependencies

**Base Priority Scores:**
```
P0 (Must Have): 1000
P1 (High):       500
P2 (Medium):     100
P3 (Low):         10
```

**Dependency Bonuses:**
```
Blocks 1+ stories: +50 per story blocked
Blocks P0 story: +200 (critical path)
Blocks P1 story: +100
Has no blockers: +25 (ready to start immediately)
```

**Formula:**
```
Effective Priority = Base Priority
                   + (Blocks Count × 50)
                   + (Critical Blocks × 150)
                   + (No Blockers Bonus)
```

**Example:**
```
story-auth-001 (Signup):
  Base Priority: P0 = 1000
  Blocks: 3 stories (auth-002, auth-003, profile-001)
  Blocks P0: auth-002, auth-003 (2 × 200 = 400)
  No Blockers: +25

  Effective Priority = 1000 + (3 × 50) + 400 + 25 = 1575
```

### Topological Sort Algorithm

**Purpose:** Order stories so dependencies always come before dependents.

**Algorithm (Kahn's Algorithm):**
```
function topologicalSort(stories):
  # Calculate in-degree (number of blockers)
  inDegree = {}
  for each story:
    inDegree[story] = story.blocked_by.length

  # Queue stories with no dependencies
  queue = []
  for each story:
    if inDegree[story] == 0:
      queue.add(story)

  result = []
  while queue is not empty:
    story = queue.remove()
    result.add(story)

    # Reduce in-degree for stories this one blocks
    for each dependent in story.blocks:
      inDegree[dependent] -= 1
      if inDegree[dependent] == 0:
        queue.add(dependent)

  if result.length != stories.length:
    ERROR: Circular dependency exists

  return result
```

**Example Output:**
```
Ordered Story List (dependency-aware):
1. story-auth-001 (Signup) - No blockers, blocks 3
2. story-auth-002 (Login) - Blocked by signup
3. story-auth-003 (Logout) - Blocked by signup
4. story-profile-001 (View Profile) - Blocked by login
5. story-profile-002 (Edit Profile) - Blocked by view profile
```

### Sorting with Priorities

**Combined Algorithm:**
```
function sortStoriesWithPriority(stories):
  # First: Topological sort (respects dependencies)
  dependencyOrder = topologicalSort(stories)

  # Second: Within dependency levels, sort by priority
  levels = groupByDependencyLevel(dependencyOrder)

  result = []
  for each level in levels:
    # Sort by effective priority (highest first)
    levelSorted = sort(level, by=effectivePriority, desc=true)
    result.addAll(levelSorted)

  return result
```

---

## Dependency Validation During Sprint Planning

### 1. Check Dependencies Are Satisfied

**Rule:** A story can only be added to a sprint if all its dependencies are:
- In the same sprint (earlier in execution order), OR
- In a previous sprint, OR
- Already completed

**Validation:**
```
function canAddToSprint(story, currentSprint, previousSprints):
  for each dep in story.blocked_by:
    if dep.status == "Complete":
      continue  # OK

    if dep in previousSprints:
      continue  # OK

    if dep in currentSprint:
      # Must come before story in execution order
      if currentSprint.indexOf(dep) < currentSprint.indexOf(story):
        continue  # OK
      else:
        return FAIL: "Dependency order violation"

    return FAIL: "Unmet dependency"

  return OK
```

### 2. Identify Critical Path

**Purpose:** Find longest dependency chain that determines minimum sprint count.

**Algorithm:**
```
function criticalPath(stories):
  # Calculate longest path from each story
  longestPath = {}

  for each story in topologicalOrder(stories):
    if story.blocked_by.isEmpty():
      longestPath[story] = story.points
    else:
      maxPath = 0
      for each dep in story.blocked_by:
        if longestPath[dep] > maxPath:
          maxPath = longestPath[dep]
      longestPath[story] = maxPath + story.points

  # Critical path is story with longest path
  criticalStory = max(longestPath)

  return {
    story: criticalStory,
    totalPoints: longestPath[criticalStory],
    minSprints: ceil(longestPath[criticalStory] / sprintCapacity)
  }
```

**Example Output:**
```
Critical Path Analysis:
  Path: story-auth-001 (5) → story-auth-002 (3) → story-profile-001 (5) → story-profile-002 (3)
  Total Points: 16 points
  Sprint Capacity: 17 points
  Minimum Sprints: 1 sprint (all can fit in one sprint if dependencies respected)
```

---

## Handling Dependency Conflicts

### Conflict: Story Doesn't Fit But Dependency Does

**Scenario:**
```
Sprint Capacity: 17 points
Remaining: 4 points

story-auth-003 (3 points, no dependencies) - FITS
story-profile-002 (5 points, blocked by profile-001) - DOESN'T FIT

But profile-001 is already in the sprint.
```

**Resolution Options:**
1. **Defer to Next Sprint:** Move profile-002 to Sprint 2
2. **Swap Stories:** Replace auth-003 with another 1-point story
3. **Accept Partial Epic:** Keep epics split across sprints

**Recommendation:** Prefer completing epics together (option 2).

### Conflict: Dependency in Later Sprint

**Scenario:**
```
story-auth-002 (Login) assigned to Sprint 1
story-auth-001 (Signup) assigned to Sprint 2  ❌ Invalid
```

**Detection:**
```
for each sprint in sprints:
  for each story in sprint:
    for each dep in story.blocked_by:
      if dep.sprint > story.sprint:
        ERROR: Dependency in later sprint
```

**Resolution:** Move dependency to earlier sprint (or same sprint).

---

## Integration with Sprint Planning

**Usage in Grouping Algorithm:**
```
For each story in orderedStories (topological sort with priority):
  if story.points <= availableCapacity:
    # Check dependencies satisfied
    if allDependenciesInThisOrPreviousSprints(story):
      sprint.add(story)
      availableCapacity -= story.points
    else:
      # Defer to next sprint
      nextSprint.candidates.add(story)
```

---

*Part of sprint-plan skill - BMAD Enhanced*
