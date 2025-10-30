---
name: breakdown-epic
description: Break down epics into implementable user stories with acceptance criteria, estimates, dependencies, and sprint groupings. Use for epic planning and backlog grooming.
acceptance:
  - components_identified: "Major components and sub-features identified from epic"
  - stories_created: "User stories created in proper format with acceptance criteria"
  - estimates_provided: "Story points estimated using complexity/effort/risk"
  - dependencies_mapped: "Dependencies between stories identified and documented"
  - sprints_suggested: "Sprint groupings suggested based on dependencies and priorities"
inputs:
  epic_description:
    type: string
    required: true
    description: "Epic or feature description to break down"
  tech_stack:
    type: array
    required: false
    description: "Technology stack for technical considerations"
outputs:
  story_files:
    type: array
    description: "List of generated story file paths"
  epic_file:
    type: string
    description: "Path to generated epic summary file"
  total_points:
    type: number
    description: "Total story points across all stories"
  story_count:
    type: number
    description: "Number of stories created"
  sprint_count:
    type: number
    description: "Suggested number of sprints"
telemetry:
  emit: "skill.breakdown-epic.completed"
  track:
    - story_count
    - total_points
    - sprint_count
    - priority_distribution
    - dependency_count
    - duration_ms
---

# Breakdown Epic Skill

## Purpose

Transform high-level epics or features into detailed, actionable user stories ready for sprint planning and implementation.

**Core Capabilities:**
- Epic scope analysis and component identification
- User story creation (As a... I want... So that...)
- Story point estimation (complexity/effort/risk)
- Dependency mapping between stories
- Sprint grouping suggestions
- Story and epic file generation

## Prerequisites

- Configuration file (`.claude/config.yaml`) with planning settings
- Epic description (20+ words minimum)
- Story point scale defined (default: Fibonacci 1,2,3,5,8,13,21)

---

## Workflow

### Step 0: Load Configuration and Epic Description

**Action:** Load configuration and parse epic requirements.

**Load config:**
```bash
python .claude/skills/bmad-commands/scripts/read_file.py \
  --path .claude/config.yaml \
  --output json
```

**Extract settings:**
- `planning.storiesLocation`: Where to save story files
- `planning.epicsLocation`: Where to save epic summaries
- `planning.defaultVelocity`: Team velocity (story points per sprint)
- `planning.storyPointScale`: Estimation scale (Fibonacci recommended)
- `project.techStack`: Technology considerations

**Get epic description:**
- From user input (20+ words minimum)
- Parse epic scope: description, business goals, technical requirements
- Identify user types and use cases

**Prepare directories:**
```bash
mkdir -p {storiesLocation}
mkdir -p {epicsLocation}
```

**Halt if:**
- Configuration missing
- Epic description <20 words (too vague)
- Cannot create directories

**See:** `references/epic-analysis-guide.md` for scope analysis

---

### Step 1: Analyze Epic Scope

**Action:** Break down epic into major components and sub-features.

**Identify components:**
1. **Core Features** - What functionality is needed?
2. **User Types** - Who will use this?
3. **Technical Requirements** - What tech/integrations?
4. **Security Requirements** - What needs protection?
5. **Non-Functional Requirements** - Performance, scalability, etc.

**Example analysis:**
```markdown
Epic: User Authentication & Authorization

Major Components:
1. Authentication Flow
   - User signup (email + password)
   - User login (credential validation)
   - User logout (session termination)
   - Password reset (forgot password flow)
   - Email verification

2. OAuth Integration
   - OAuth provider setup (Google, GitHub)
   - OAuth flow (redirect, callback, token exchange)
   - Account linking

3. Authorization & RBAC
   - User roles (admin, user, guest)
   - Permission system
   - Role-based access control

4. Session Management
   - JWT token generation
   - Token refresh
   - Session expiration
```

**Group by themes:**
- Related features together
- Similar technical complexity
- Common user journeys

**See:** `references/epic-analysis-guide.md` for detailed analysis techniques

---

### Step 2: Create User Stories

**Action:** Convert components into user stories with acceptance criteria.

**Story format:**
```markdown
## Story Title

**As a** [user type],
**I want** [capability],
**So that** [benefit]

**Acceptance Criteria:**
1. [Specific, testable criterion]
2. [Specific, testable criterion]
3. [Specific, testable criterion]

**Priority:** P0 | P1 | P2 | P3

**Component:** [Feature area]
```

**Example stories:**
```markdown
**Story 1: User Signup**
As a new user,
I want to create an account with email and password,
So that I can access personalized features.

Acceptance Criteria:
1. User can signup with valid email (RFC 5322 format)
2. Password requirements enforced (8+ chars, complexity)
3. Duplicate emails prevented (409 error)
4. Confirmation email sent

Priority: P0 (Must Have)
Component: Authentication

---

**Story 2: User Login**
As a registered user,
I want to log in with my credentials,
So that I can access my account.

Acceptance Criteria:
1. User can login with email and password
2. Invalid credentials return 401 error
3. JWT token generated on successful login
4. Rate limiting applied (5 attempts per minute)

Priority: P0 (Must Have)
Component: Authentication
```

**Story quality checks:**
- Clear user perspective
- Specific, testable acceptance criteria (2-5 per story)
- Appropriate priority
- Properly scoped (not too large, not too small)

**See:** `references/story-creation-guide.md` for story writing best practices

---

### Step 3: Estimate Story Points

**Action:** Estimate each story using complexity, effort, and risk.

**Estimation factors:**

**1. Complexity (1-5):**
- 1: Trivial (CRUD operation)
- 2: Simple (straightforward logic)
- 3: Moderate (multiple components)
- 4: Complex (many integrations)
- 5: Very complex (new patterns needed)

**2. Effort (1-5):**
- 1: <2 hours
- 2: 2-4 hours
- 3: 4-8 hours (half day to full day)
- 4: 8-16 hours (1-2 days)
- 5: 16+ hours (2+ days)

**3. Risk (1-3):**
- 1: Low (known implementation)
- 2: Medium (some unknowns)
- 3: High (many unknowns, dependencies)

**Calculate story points:**
```
Story Points = Complexity + Effort + Risk
Then round to nearest Fibonacci number
```

**Example:**
```
Story: User Signup
- Complexity: 3 (moderate - validation, hashing, email)
- Effort: 4 (8-16 hours - model, service, API, tests)
- Risk: 1 (low - standard auth pattern)
- Total: 8 → Story Points: 8
```

**Fibonacci scale:** 1, 2, 3, 5, 8, 13, 21

**See:** `references/estimation-guide.md` for detailed estimation techniques

---

### Step 4: Identify Dependencies

**Action:** Map dependencies between stories.

**Dependency types:**

**1. Blocks:** Story A must complete before Story B can start
```
story-auth-001 (Signup) BLOCKS story-auth-003 (Email Verification)
```

**2. Related:** Stories share components but can be done in parallel
```
story-auth-001 (Signup) RELATED story-auth-002 (Login)
```

**Dependency rules:**
- Foundation before features (models before APIs)
- Authentication before authorization
- Core functionality before enhancements
- Infrastructure before applications

**Example dependencies:**
```markdown
Dependencies for User Auth Epic:

story-auth-001 (User Signup)
  └─ BLOCKS story-auth-003 (Email Verification)
  └─ BLOCKS story-auth-002 (User Login)

story-auth-002 (User Login)
  └─ BLOCKS story-auth-006 (Password Reset)

story-auth-004 (JWT Sessions)
  └─ BLOCKS story-auth-005 (Token Refresh)

story-auth-007 (OAuth Setup)
  └─ BLOCKS story-auth-008 (OAuth Login)

story-auth-009 (RBAC System)
  └─ REQUIRES story-auth-001 (User Signup)
  └─ REQUIRES story-auth-002 (User Login)
```

**See:** `references/dependency-mapping-guide.md` for dependency analysis

---

### Step 5: Suggest Sprint Groupings

**Action:** Group stories into sprints based on dependencies, priorities, and velocity.

**Grouping rules:**
1. **Priority first** - P0 stories in early sprints
2. **Dependencies respected** - Blocked stories after blockers
3. **Velocity constraints** - Don't exceed team capacity
4. **Logical grouping** - Related stories together

**Example sprint plan:**
```markdown
Sprint Planning for User Auth Epic

Team Velocity: 40 points per sprint (2 weeks)

Sprint 1 (40 points):
- story-auth-001: User Signup (8 points) [P0]
- story-auth-002: User Login (5 points) [P0]
- story-auth-004: JWT Sessions (5 points) [P0]
- story-auth-006: Password Reset (8 points) [P1]
- story-auth-003: Email Verification (13 points) [P1]

Sprint 2 (39 points):
- story-auth-007: OAuth Setup (8 points) [P1]
- story-auth-008: OAuth Login (5 points) [P1]
- story-auth-009: RBAC System (13 points) [P1]
- story-auth-005: Token Refresh (8 points) [P1]
- story-auth-010: Account Linking (5 points) [P2]

Total: 2 sprints, 79 points (4 weeks)
```

**See:** `references/sprint-grouping-guide.md` for sprint planning techniques

---

### Step 6: Generate Story Files and Epic Summary

**Action:** Create story markdown files and epic summary.

**Generate story files:**
```bash
# For each story
python .claude/skills/bmad-commands/scripts/write_file.py \
  --path {storiesLocation}/story-auth-001-user-signup.md \
  --content "{story_content}" \
  --output json
```

**Story file format:**
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
2. Password requirements enforced (8+ chars, complexity)
3. Duplicate emails prevented (409 error)
4. Confirmation email sent

## Dependencies

**Blocks:**
- story-auth-003 (Email Verification)
- story-auth-002 (User Login)

## Estimation Details

- Complexity: 3/5 (Moderate)
- Effort: 4/5 (8-16 hours)
- Risk: 1/3 (Low)
- Total: 8 story points

## Sprint Assignment

Sprint 1

## Definition of Done

- [ ] Implementation complete
- [ ] Unit tests written and passing
- [ ] Integration tests written and passing
- [ ] API documented
- [ ] Code reviewed
- [ ] Merged to main
```

**Generate epic summary:**
```markdown
# Epic: User Authentication & Authorization

**Epic ID:** epic-auth
**Status:** Planning Complete
**Total Story Points:** 79
**Estimated Duration:** 2 sprints (4 weeks)

## Stories Breakdown

**Total Stories:** 10
**By Priority:**
- P0 (Must Have): 4 stories (23 points)
- P1 (Should Have): 5 stories (51 points)
- P2 (Nice to Have): 1 story (5 points)

## Sprint Plan

[Include sprint groupings from Step 5]

## Dependency Graph

[Include dependencies from Step 4]
```

---

### Step 7: Present Summary to User

**Action:** Present epic breakdown summary for review.

**Summary format:**
```markdown
## Epic Breakdown Complete

**Epic:** User Authentication & Authorization
**Stories Created:** 10
**Total Story Points:** 79
**Suggested Sprints:** 2 (4 weeks)

**Files Generated:**
- 10 story files: .claude/stories/story-auth-*.md
- Epic summary: .claude/epics/epic-auth.md

**Priority Distribution:**
- P0 (Must Have): 4 stories (23 points)
- P1 (Should Have): 5 stories (51 points)
- P2 (Nice to Have): 1 story (5 points)

**Sprint Plan:**
- Sprint 1: 5 stories, 40 points
- Sprint 2: 5 stories, 39 points

**Dependencies Identified:** 7 blocking relationships

**Ready to proceed with sprint planning? (yes/no)**
```

---

## Output

Return structured output with telemetry:

```json
{
  "story_files": [
    ".claude/stories/story-auth-001-user-signup.md",
    ".claude/stories/story-auth-002-user-login.md",
    ...
  ],
  "epic_file": ".claude/epics/epic-auth.md",
  "total_points": 79,
  "story_count": 10,
  "sprint_count": 2,
  "telemetry": {
    "skill": "breakdown-epic",
    "story_count": 10,
    "total_points": 79,
    "sprint_count": 2,
    "priority_distribution": {"P0": 4, "P1": 5, "P2": 1},
    "dependency_count": 7,
    "duration_ms": 245000
  }
}
```

---

## Best Practices

1. **Epic Scope** - Keep epics focused (10-15 stories max)
2. **Story Size** - Target 3-8 points per story (not too large)
3. **Clear ACs** - 2-5 specific, testable acceptance criteria
4. **Priority Discipline** - Not everything can be P0
5. **Dependency Mapping** - Identify blockers early
6. **Velocity Reality** - Don't overcommit sprint capacity

**See:** `references/story-creation-guide.md` for best practices

---

## Routing Guidance

**Use this skill when:**
- Starting new epic or major feature
- During backlog grooming sessions
- Planning multiple sprints ahead
- Breaking down product requirements

**Always use before:**
- sprint-plan skill (sprint planning)
- refine-story skill (detailed story refinement)

**Feeds into:**
- create-task-spec skill (for implementation specs)

---

## Reference Files

Detailed documentation in `references/`:

- **epic-analysis-guide.md**: Epic scope analysis, component identification
- **story-creation-guide.md**: User story format, acceptance criteria, best practices
- **estimation-guide.md**: Story point estimation techniques
- **dependency-mapping-guide.md**: Dependency types, mapping, sprint grouping

---

## Using This Skill

**From command line:**
```bash
Use .claude/skills/planning/breakdown-epic/SKILL.md with input {epic_description: "User Authentication & Authorization"}
```

---

## Philosophy

This skill embodies BMAD's 3-layer architecture:

- **Uses Commands** (Layer 1): bmad-commands for read_file, write_file
- **Provides Composition** (Layer 2): Epic breakdown + story creation workflow
- **Enables Orchestration** (Layer 3): Used by planning agents/subagents

By breaking down epics systematically, this skill is:
- **Observable**: Telemetry tracks breakdown metrics
- **Testable**: Output format is predictable
- **Composable**: Feeds into sprint planning and task specs
- **Reliable**: Consistent story format

---

*Part of BMAD Enhanced Planning Suite*
