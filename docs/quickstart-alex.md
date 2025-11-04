# Alex (Planner) Quick Start Guide

**Subagent:** alex-planner-v2
**Role:** Planning & Requirements Specialist
**Commands:** 5
**Version:** 2.0

---

## Overview

**Alex** is your intelligent planning assistant that transforms high-level requirements into actionable, well-structured deliverables using complexity-based routing and comprehensive guardrails.

### What Alex Does

- ✅ Creates detailed task specifications
- ✅ Breaks down large epics into manageable stories
- ✅ Estimates story points systematically
- ✅ Refines vague requirements
- ✅ Generates sprint plans with velocity management

### V2 Features

- **Intelligent Routing:** Automatically selects appropriate strategy (simple/standard/complex)
- **Complexity Assessment:** 0-100 scale using 5 weighted factors
- **Guardrails:** Prevents over-scoping and unrealistic plans
- **Full Telemetry:** Every operation tracked and observable

---

## Commands

### 1. `*create-task-spec` - Create Task Specifications

**Purpose:** Transform requirements into detailed, actionable task specifications

**Syntax:**
```bash
@alex *create-task-spec "<requirement-description>"
```

**Examples:**
```bash
@alex *create-task-spec "User login with email validation"
@alex *create-task-spec "Add shopping cart checkout flow"
@alex *create-task-spec "Implement password reset feature"
```

**What You Get:**
- Detailed task specification file (`.claude/tasks/task-{id}.md`)
- Clear acceptance criteria
- Technical approach
- Dependencies identified
- Estimated effort
- Test requirements

**When to Use:**
- Converting user stories into implementable tasks
- Need detailed technical specifications
- Before starting implementation

---

### 2. `*breakdown-epic` - Break Down Epics

**Purpose:** Decompose large epics into manageable user stories

**Syntax:**
```bash
@alex *breakdown-epic "<epic-description>"
@alex *breakdown-epic docs/epics/epic-name.md
```

**Examples:**
```bash
@alex *breakdown-epic "User Authentication System"
@alex *breakdown-epic "E-commerce Shopping Cart"
@alex *breakdown-epic docs/epics/epic-payment-processing.md
```

**What You Get:**
- 5-15 user stories
- Story files in `workspace/stories/`
- Dependencies mapped
- Acceptance criteria per story
- Priority ranking

**When to Use:**
- Starting a new feature or epic
- Need to estimate total effort
- Planning sprint allocation

---

### 3. `*estimate` - Estimate Story Points

**Purpose:** Systematically estimate effort for stories using established patterns

**Syntax:**
```bash
@alex *estimate "<story-id-or-description>"
@alex *estimate workspace/stories/story-*.md
```

**Examples:**
```bash
@alex *estimate story-login-001
@alex *estimate "Implement user profile editing"
@alex *estimate workspace/stories/story-*.md
```

**What You Get:**
- Story point estimate (1, 2, 3, 5, 8, 13, 21)
- Justification for estimate
- Risk factors identified
- Complexity breakdown
- Updated story file with estimates

**When to Use:**
- After breaking down an epic
- Before sprint planning
- When backlog grooming

---

### 4. `*refine-story` - Refine Requirements

**Purpose:** Transform vague or incomplete requirements into clear, actionable stories

**Syntax:**
```bash
@alex *refine-story "<vague-requirement>"
@alex *refine-story workspace/stories/story-draft.md
```

**Examples:**
```bash
@alex *refine-story "Users need better security"
@alex *refine-story "Improve performance"
@alex *refine-story workspace/stories/story-vague-001.md
```

**What You Get:**
- Clarified requirements
- Specific acceptance criteria
- Measurable success metrics
- Technical constraints identified
- Ready-to-implement story

**When to Use:**
- Requirements are unclear or vague
- Acceptance criteria missing
- Before estimation or implementation

---

### 5. `*plan-sprint` - Create Sprint Plans

**Purpose:** Generate sprint plans based on velocity and story priorities

**Syntax:**
```bash
@alex *plan-sprint --velocity <points> --duration <days>
@alex *plan-sprint --velocity 40
```

**Examples:**
```bash
@alex *plan-sprint --velocity 40 --duration 14
@alex *plan-sprint --velocity 25
```

**What You Get:**
- Sprint plan document
- Stories allocated by priority
- Velocity management (≤95% capacity)
- Sprint goals defined
- Daily breakdown (optional)
- Burn-down projections

**When to Use:**
- Starting a new sprint
- Need to allocate backlog items
- Planning team capacity

---

## Common Workflows

### Workflow 1: Plan a New Feature

**Goal:** From idea to implementable tasks

```bash
# Step 1: Refine the idea
@alex *refine-story "Add user notifications"

# Step 2: Create detailed spec
@alex *create-task-spec "Send email notifications for important events"

# Step 3: Ready for James to implement
```

**Duration:** 5-10 minutes
**Output:** Ready-to-implement task specification

---

### Workflow 2: Break Down an Epic

**Goal:** Epic to sprint-ready stories

```bash
# Step 1: Break down epic
@alex *breakdown-epic "User Authentication System"
# Output: story-001 through story-008

# Step 2: Estimate each story
@alex *estimate workspace/stories/story-auth-*.md
# Output: All stories with estimates

# Step 3: Create sprint plan
@alex *plan-sprint --velocity 40
# Output: Sprint plan with allocated stories
```

**Duration:** 15-30 minutes
**Output:** Sprint-ready backlog with estimates

---

### Workflow 3: Prepare for Sprint Planning

**Goal:** Backlog ready for sprint

```bash
# Step 1: Estimate all stories
@alex *estimate workspace/stories/*.md

# Step 2: Create sprint plan
@alex *plan-sprint --velocity 40 --duration 14

# Output: Sprint plan document ready for team review
```

**Duration:** 10-20 minutes
**Output:** Sprint plan

---

## Complexity Assessment

Alex calculates complexity using **5 weighted factors**:

1. **Requirement Clarity** (30%): Clear=10, Vague=40, Incomplete=70, Unclear=90
2. **Scope Size** (25%): Small=10, Medium=40, Large=70, XLarge=90
3. **Dependencies** (20%): None=10, Few=40, Many=70, Complex=90
4. **Technical Risk** (15%): Low=10, Medium=40, High=70, Critical=90
5. **Time Constraints** (10%): Flexible=10, Standard=40, Tight=70, Critical=90

**Routing:**
- **Simple (≤30):** Quick approach, minimal detail
- **Standard (31-60):** Detailed analysis, comprehensive output
- **Complex (>60):** Deep dive, user confirmation required

---

## Tips & Best Practices

### ✅ Do's

- **Be specific:** Clear requirements → better specs
- **Start with epics:** Break large work into manageable pieces
- **Estimate systematically:** Use Alex's patterns for consistency
- **Review estimates:** Adjust velocity based on team capacity
- **Use refinement:** Turn vague ideas into clear requirements

### ❌ Don'ts

- **Don't over-scope:** Keep stories small (≤13 points ideal)
- **Don't skip estimation:** Needed for sprint planning
- **Don't ignore dependencies:** Alex identifies them for a reason
- **Don't exceed capacity:** Keep sprint load ≤95% velocity

---

## Configuration

### Velocity Settings

Set team velocity in `.claude/config.yaml`:

```yaml
team:
  velocity: 40          # Team's avg story points per sprint
  sprint_duration: 14   # Days per sprint
  capacity_limit: 0.95  # Max 95% of velocity
```

### Planning Templates

Customize templates in `.claude/templates/`:
- `epic-template.md` - Epic structure
- `story-template.md` - Story format
- `task-template.md` - Task specification format

---

## Troubleshooting

### Issue: "Requirements Too Vague"

**Solution:** Use `*refine-story` first
```bash
@alex *refine-story "Your vague requirement"
# Then: @alex *create-task-spec with refined output
```

### Issue: "Epic Too Large"

**Solution:** Break into smaller epics
```bash
# Instead of one massive epic:
@alex *breakdown-epic "Phase 1: Core Authentication"
@alex *breakdown-epic "Phase 2: Social Login"
```

### Issue: "Estimates Inconsistent"

**Solution:** Calibrate using past sprints
```bash
# Review completed stories
# Adjust velocity based on actual completion rates
# Use Alex's estimates as baseline, team adjusts
```

---

## Next Steps

**After Planning:**
1. **Architecture (if needed):** Use Winston for system design
2. **Implementation:** Use James to implement tasks
3. **Quality Review:** Use Quinn to review completed work

**Related Guides:**
- [James (Developer) Quick Start](./quickstart-james.md)
- [Quinn (Quality) Quick Start](./quickstart-quinn.md)
- [Orchestrator Quick Start](./quickstart-orchestrator.md)
- [V2 Architecture](./V2-ARCHITECTURE.md)

---

**Questions?** See [V2 Architecture Documentation](./V2-ARCHITECTURE.md)

**Alex (Planner) Quick Start Guide**
*Part of BMAD Enhanced V2 Architecture*
