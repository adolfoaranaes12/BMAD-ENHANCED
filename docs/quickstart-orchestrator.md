# Orchestrator Quick Start Guide

**Subagent:** orchestrator-v2
**Role:** Workflow Coordinator & Cross-Subagent Router
**Commands:** 2
**Version:** 2.0

---

## Overview

**Orchestrator** is your intelligent workflow coordinator that manages multi-step processes across specialized subagents (Alex, James, Quinn, Winston) with state management, error recovery, and automated handoffs.

### What Orchestrator Does

- ✅ Executes complete end-to-end workflows
- ✅ Coordinates multiple subagents in sequence or parallel
- ✅ Manages workflow state with persistence and resume
- ✅ Automates handoffs between planning, development, and quality
- ✅ Recovers from failures and resumes workflows
- ✅ Provides full observability across workflow execution

### V2 Features

- **Intelligent Workflow Routing:** Complexity-based workflow selection
- **State Management:** Persistent workflow state with resume capability
- **Cross-Subagent Guardrails:** Validation of handoffs and phase transitions
- **Full Telemetry:** Structured observability for workflow execution
- **Automated Recovery:** Resume failed workflows from last successful phase
- **4 Coordination Patterns:** Sequential, Parallel, Iterative, Collaborative

---

## Commands

### 1. `*workflow` - Execute Complete Workflow

**Purpose:** Execute end-to-end workflows coordinating multiple subagents with state management

**Syntax:**
```bash
/orchestrator *workflow <workflow-type> <input>
/orchestrator *workflow feature-delivery "User login with email validation"
/orchestrator *workflow epic-to-sprint "User Authentication System" --velocity 40
/orchestrator *workflow sprint-execution "Sprint 15" --velocity 40
```

**Examples:**
```bash
/orchestrator *workflow feature-delivery "Add shopping cart checkout flow"
/orchestrator *workflow epic-to-sprint "Payment Processing System" --velocity 35
/orchestrator *workflow sprint-execution "Sprint Q1-2025-Sprint-3" --velocity 40
```

**What You Get:**
- Complete workflow execution from start to finish
- Workflow state file (`.claude/workflows/{workflow-id}-state.yaml`)
- Telemetry for each phase
- All intermediate artifacts (task specs, implementations, quality gates)
- Resume capability if interrupted
- Final PR or sprint summary

**Complexity Factors:**
- Workflow stages (30%)
- Subagents involved (25%)
- Dependencies (20%)
- Timeline (15%)
- Risk (10%)

**When to Use:**
- Complete feature delivery (idea → PR)
- Sprint planning and execution
- Epic breakdown to sprint plans
- Multi-phase processes
- Need automated state management

---

### Supported Workflow Types

#### 1. **feature-delivery** - Requirement to PR

**Purpose:** Complete feature implementation from requirement to pull request

**Phases:**
1. **Planning (Alex):** Create detailed task specification
2. **Implementation (James):** Implement with TDD
3. **Quality Review (Quinn):** Comprehensive review with quality gate
4. **Pull Request:** Create PR with changes

**Input:** Feature description or requirement file

**Example:**
```bash
/orchestrator *workflow feature-delivery "User login with OAuth integration"

# Output:
# Phase 1: Task spec created (.claude/tasks/task-001.md)
# Phase 2: Implementation complete with tests (80%+ coverage)
# Phase 3: Quality gate PASS (quality score: 85%)
# Phase 4: PR created (PR #123)
```

**Duration:** 30-90 minutes depending on complexity
**Use When:** Implementing standalone features

---

#### 2. **epic-to-sprint** - Epic Breakdown to Sprint Plan

**Purpose:** Break down large epic into sprint-ready stories with estimates

**Phases:**
1. **Breakdown (Alex):** Decompose epic into user stories
2. **Estimation (Alex):** Estimate each story (story points)
3. **Sprint Planning (Alex):** Create sprint plan based on velocity

**Input:** Epic description or epic file, team velocity

**Example:**
```bash
/orchestrator *workflow epic-to-sprint "E-commerce Shopping Cart" --velocity 40

# Output:
# Phase 1: 8 user stories created (workspace/stories/story-cart-*.md)
# Phase 2: Stories estimated (total: 52 points)
# Phase 3: Sprint plan created (40 points allocated)
```

**Duration:** 20-45 minutes
**Use When:** Starting new epic or feature set

---

#### 3. **sprint-execution** - Execute Complete Sprint

**Purpose:** Execute sprint from start to finish with daily work loops

**Phases:**
1. **Daily Work (James + Quinn):** Implement → Review → Fix cycle
2. **Sprint Review:** Review completed work
3. **Retrospective:** Lessons learned and improvements

**Input:** Sprint name or sprint plan file, velocity

**Example:**
```bash
/orchestrator *workflow sprint-execution "Sprint 15" --velocity 40

# Output:
# Phase 1: All sprint stories implemented and reviewed
# Phase 2: Sprint review report (.claude/sprints/sprint-15-review.md)
# Phase 3: Retrospective (.claude/sprints/sprint-15-retro.md)
```

**Duration:** Full sprint duration (depends on velocity and story count)
**Use When:** Executing planned sprints

---

### 2. `*coordinate` - Cross-Subagent Coordination

**Purpose:** Coordinate multiple subagents for specific cross-cutting tasks

**Syntax:**
```bash
/orchestrator *coordinate <task-description> --subagents <list>
/orchestrator *coordinate "Validate architecture and create implementation plan" --subagents winston,alex
/orchestrator *coordinate "Quality improvement cycle" --subagents quinn,james
```

**Examples:**
```bash
/orchestrator *coordinate "Architecture review + planning" --subagents winston,alex
/orchestrator *coordinate "Fix quality issues and re-review" --subagents james,quinn
/orchestrator *coordinate "Design API + implement + validate" --subagents winston,james,quinn
```

**What You Get:**
- Coordinated execution across subagents
- Automated handoffs with validation
- Shared state management
- Telemetry for coordination points
- Results from all subagents synthesized

**Complexity Factors:**
- Subagent count (30%)
- Coordination points (25%)
- Dependencies (20%)
- State sharing (15%)
- Conflict potential (10%)

**When to Use:**
- Cross-cutting tasks requiring multiple subagents
- Quality improvement cycles (Quinn → James → Quinn)
- Architecture + planning (Winston → Alex)
- Tasks with complex handoffs

---

## Coordination Patterns

Orchestrator uses 4 coordination patterns based on task characteristics:

### 1. Sequential Coordination (A → B → C)

**Pattern:** Linear handoffs, output of A becomes input of B

**Characteristics:**
- Clear dependencies
- Each phase completes before next starts
- Output → Input mapping explicit

**Example:**
```bash
# Winston designs architecture → Alex creates tasks → James implements
/orchestrator *coordinate "Full-stack feature" --subagents winston,alex,james
```

**Use When:** Clear sequential dependencies exist

---

### 2. Parallel Coordination (A ∥ B ∥ C → Synthesize)

**Pattern:** Independent tasks executed simultaneously, results combined

**Characteristics:**
- No dependencies between tasks
- All run in parallel
- Results synthesized at end

**Example:**
```bash
# Multiple features implemented in parallel
/orchestrator *coordinate "Parallel feature implementation" --subagents james,james,james
# (3 separate James instances for 3 independent features)
```

**Use When:** Tasks are truly independent

---

### 3. Iterative Coordination (A → B → A until done)

**Pattern:** Cycles with feedback loops until criteria met

**Characteristics:**
- Feedback loop
- Termination condition
- State tracked across iterations

**Example:**
```bash
# Quinn reviews → James fixes → Quinn validates (repeat until PASS)
/orchestrator *coordinate "Quality improvement cycle" --subagents quinn,james
```

**Use When:** Iterative refinement needed

---

### 4. Collaborative Coordination (A ⇄ B)

**Pattern:** Bidirectional collaboration with shared decision-making

**Characteristics:**
- Continuous back-and-forth
- Shared context
- Joint decisions

**Example:**
```bash
# Winston and Alex collaborate on complex system design
/orchestrator *coordinate "Complex system architecture + planning" --subagents winston,alex
```

**Use When:** Complex decisions requiring collaboration

---

## Common Workflows

### Workflow 1: Ship a Complete Feature

**Goal:** From idea to production-ready PR

```bash
# Single command executes entire workflow
/orchestrator *workflow feature-delivery "Add user profile editing"

# Orchestrator handles:
# 1. Alex creates task spec
# 2. James implements with TDD
# 3. Quinn reviews with quality gate
# 4. PR created if quality gate PASS
```

**Duration:** 30-90 minutes
**Output:** Pull request ready for merge

---

### Workflow 2: Plan a Sprint from Epic

**Goal:** Epic to sprint-ready backlog

```bash
# Step 1: Break down epic and plan sprint
/orchestrator *workflow epic-to-sprint "Mobile App MVP" --velocity 40

# Output:
# - 12 user stories with estimates
# - Sprint plan with 40 points allocated
# - Remaining stories in backlog

# Step 2: Execute sprint
/orchestrator *workflow sprint-execution "Sprint 16" --velocity 40
```

**Duration:** Planning: 30 min, Execution: Full sprint
**Output:** Planned and executed sprint

---

### Workflow 3: Quality Improvement Cycle

**Goal:** Fix quality issues iteratively

```bash
# Coordinate Quinn and James in feedback loop
/orchestrator *coordinate "Fix all quality issues" --subagents quinn,james

# Orchestrator executes:
# 1. Quinn reviews (finds 5 issues)
# 2. James applies fixes
# 3. Quinn re-reviews (2 issues remain)
# 4. James applies fixes
# 5. Quinn re-reviews (PASS)
```

**Duration:** 30-90 minutes depending on issues
**Output:** Quality gate PASS

---

### Workflow 4: Architecture-Driven Development

**Goal:** Architecture → Planning → Implementation

```bash
# Coordinate Winston, Alex, and James sequentially
/orchestrator *coordinate "Full system design and implementation" --subagents winston,alex,james

# Orchestrator executes:
# 1. Winston creates architecture design
# 2. Alex breaks down into tasks based on architecture
# 3. James implements according to architecture
```

**Duration:** 2-4 hours depending on scope
**Output:** Architecturally sound implementation

---

## State Management

### Workflow State Files

Orchestrator creates state files for every workflow:

**Location:** `.claude/workflows/{workflow-id}-state.yaml`

**Contents:**
```yaml
workflow_id: wf-feature-login-20250203
workflow_type: feature-delivery
status: in_progress
current_phase: implementation
completed_phases:
  - planning:
      status: completed
      output: .claude/tasks/task-001.md
      duration: 8m 32s
phases_remaining:
  - implementation
  - quality_review
  - pull_request
created_at: 2025-02-03T10:30:00Z
updated_at: 2025-02-03T10:38:32Z
```

### Resume Capability

If workflow is interrupted, resume with:

```bash
# Orchestrator detects incomplete workflow and prompts
/orchestrator *workflow feature-delivery "User login"
# > Found incomplete workflow wf-feature-login-20250203
# > Resume from last checkpoint? (y/n)

# Or explicitly resume
/orchestrator *resume wf-feature-login-20250203
```

**Benefits:**
- No lost work
- Resume from last successful phase
- Complete telemetry preserved

---

## Guardrails & Validation

### Global Orchestration Guardrails

- **Max 4 subagents:** Escalate if coordination requires >4 subagents
- **No circular dependencies:** Without termination condition
- **All subagents operational:** Validate before execution
- **State persistence:** Every phase checkpoint saved
- **Handoff validation:** Output of phase N validates as input for phase N+1

### Phase Transition Validation

**Before Starting Phase:**
- Prerequisites met
- Input validated
- Subagent available

**After Completing Phase:**
- Acceptance criteria met
- Output artifacts created
- State checkpoint saved
- Next phase ready

### Escalation Triggers

Orchestrator escalates to user when:
- ❗ Workflow complexity > 60 (requires confirmation)
- ❗ Coordination involves 4+ subagents
- ❗ Circular dependencies detected
- ❗ Phase fails 3+ times
- ❗ Quality gate FAIL (blocks PR)

---

## Tips & Best Practices

### ✅ Do's

- **Use workflows for complete features:** Let orchestrator manage handoffs
- **Trust state management:** Workflows can be interrupted and resumed
- **Review workflow types:** Choose the right workflow for your goal
- **Use coordinate for custom orchestration:** When workflows don't fit
- **Monitor telemetry:** Track workflow execution and bottlenecks
- **Let orchestrator handle failures:** Automated recovery works

### ❌ Don'ts

- **Don't micromanage phases:** Let orchestrator coordinate
- **Don't skip state checkpoints:** They enable resume
- **Don't use for single-subagent tasks:** Call subagent directly
- **Don't ignore escalations:** User confirmation needed for high complexity
- **Don't override quality gates:** If Quinn says FAIL, fix issues first

---

## Workflow Selection Guide

**When to use `*workflow feature-delivery`:**
- ✅ Implementing standalone feature
- ✅ Want complete automation (requirement → PR)
- ✅ Need quality gate enforcement
- ✅ Standard implementation workflow

**When to use `*workflow epic-to-sprint`:**
- ✅ Starting new epic or feature set
- ✅ Need backlog breakdown
- ✅ Planning sprint with velocity
- ✅ Want story estimation

**When to use `*workflow sprint-execution`:**
- ✅ Executing planned sprint
- ✅ Want automated daily loops
- ✅ Need sprint review/retro
- ✅ Managing multiple stories

**When to use `*coordinate`:**
- ✅ Custom multi-subagent coordination
- ✅ Workflow types don't fit
- ✅ Need specific coordination pattern
- ✅ Cross-cutting concerns

**When to use subagents directly:**
- ✅ Single isolated task
- ✅ Manual control preferred
- ✅ Exploratory work
- ✅ One-off operations

---

## Configuration

### Orchestrator Settings

Configure in `.claude/config.yaml`:

```yaml
orchestrator:
  enabled: true
  max_subagents: 4              # Max concurrent subagents
  max_workflow_duration: 480    # Max minutes (8 hours)
  max_phase_retries: 3          # Max retries per phase
  state_persistence: true       # Enable state files
  auto_resume: true             # Auto-detect incomplete workflows

  workflows:
    feature-delivery:
      enabled: true
      quality_gate_enforced: true   # Block PR if Quinn FAIL
      auto_pr: true                 # Auto-create PR if PASS

    epic-to-sprint:
      enabled: true
      default_velocity: 40
      max_stories_per_sprint: 15

    sprint-execution:
      enabled: true
      daily_loop: true              # James → Quinn daily loops

  coordination:
    max_iterations: 10              # For iterative patterns
    parallel_max: 4                 # Max parallel tasks
    timeout_per_phase: 60           # Minutes per phase
```

---

## Troubleshooting

### Issue: "Workflow Stuck in Phase"

**Solution:** Check subagent output and retry or skip phase
```bash
# View workflow state
cat .claude/workflows/wf-feature-*.yaml

# If phase failed, retry
/orchestrator *retry-phase wf-feature-login-20250203 implementation

# Or skip phase (with confirmation)
/orchestrator *skip-phase wf-feature-login-20250203 implementation
```

### Issue: "Quality Gate Blocks PR Creation"

**Solution:** Fix quality issues before proceeding
```bash
# Workflow stops at quality review with FAIL
# Phase: quality_review - Status: FAIL

# Step 1: Apply QA fixes
/james *apply-qa-fixes task-id

# Step 2: Resume workflow (will re-run Quinn review)
/orchestrator *resume wf-feature-login-20250203
```

### Issue: "Coordination Pattern Unclear"

**Solution:** Be explicit about coordination needs
```bash
# Instead of vague coordination
/orchestrator *coordinate "Do planning and implementation"

# Be explicit about pattern
/orchestrator *coordinate "Sequential: Architecture (winston) → Planning (alex) → Implementation (james)" --subagents winston,alex,james
```

### Issue: "Workflow Complexity Too High"

**Solution:** Break down into smaller workflows
```bash
# Instead of one massive workflow
/orchestrator *workflow feature-delivery "Entire Payment System"

# Break into multiple features
/orchestrator *workflow feature-delivery "Payment Gateway Integration"
/orchestrator *workflow feature-delivery "Payment History View"
/orchestrator *workflow feature-delivery "Refund Processing"
```

---

## Advanced: Custom Workflows

You can define custom workflow templates in `.claude/workflows/templates/`:

**Example: `custom-ci-cd-workflow.yaml`**
```yaml
workflow_type: ci-cd-pipeline
phases:
  - name: build
    subagent: james
    command: "*test --all"
    acceptance:
      - all_tests_passing: true

  - name: quality
    subagent: quinn
    command: "*review {task-id}"
    acceptance:
      - quality_gate: PASS

  - name: deploy
    subagent: orchestrator
    command: "deploy to staging"
    acceptance:
      - deployment_successful: true
```

**Usage:**
```bash
/orchestrator *workflow ci-cd-pipeline task-001
```

---

## Telemetry & Observability

### Workflow Telemetry

Every workflow generates comprehensive telemetry:

**Location:** `.claude/telemetry/workflows/{workflow-id}.json`

**Contents:**
```json
{
  "workflow_id": "wf-feature-login-20250203",
  "workflow_type": "feature-delivery",
  "total_duration": "45m 22s",
  "phases": [
    {
      "phase": "planning",
      "subagent": "alex-planner",
      "duration": "8m 32s",
      "status": "completed"
    },
    {
      "phase": "implementation",
      "subagent": "james-developer",
      "duration": "28m 15s",
      "status": "completed"
    },
    {
      "phase": "quality_review",
      "subagent": "quinn-quality",
      "duration": "8m 35s",
      "status": "completed",
      "quality_score": 85
    }
  ]
}
```

**Use telemetry to:**
- Identify bottlenecks
- Track workflow efficiency
- Monitor subagent performance
- Optimize future workflows

---

## Next Steps

**After Orchestration:**
1. **Monitor Workflows:** Review telemetry and state files
2. **Optimize Patterns:** Identify inefficient coordination
3. **Create Custom Workflows:** For repeated patterns

**Related Guides:**
- [Alex (Planner) Quick Start](./quickstart-alex.md)
- [James (Developer) Quick Start](./quickstart-james.md)
- [Quinn (Quality) Quick Start](./quickstart-quinn.md)
- [V2 Architecture](./V2-ARCHITECTURE.md)

---

**Questions?** See [V2 Architecture Documentation](./V2-ARCHITECTURE.md)

**Orchestrator Quick Start Guide**
*Part of BMAD Enhanced V2 Architecture*
