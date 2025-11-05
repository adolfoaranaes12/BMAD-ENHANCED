# BMAD Enhanced V2 Architecture

**Version:** 2.0
**Date:** 2025-02-03
**Status:** Production Ready
**Audience:** Developers, Contributors, Users

---

## Table of Contents

1. [Overview](#overview)
2. [Architecture Layers](#architecture-layers)
3. [V2 Pattern: 7-Step Workflow](#v2-pattern-7-step-workflow)
4. [Complexity Assessment](#complexity-assessment)
5. [Intelligent Routing](#intelligent-routing)
6. [Guardrails Framework](#guardrails-framework)
7. [Telemetry & Observability](#telemetry--observability)
8. [State Management](#state-management)
9. [Subagents Overview](#subagents-overview)
10. [Skills Overview](#skills-overview)
11. [Workflows](#workflows)
12. [Performance](#performance)
13. [Best Practices](#best-practices)
14. [Migration Guide](#migration-guide)

---

## Overview

**BMAD Enhanced V2** is a production-ready architecture for building maintainable applications through intelligent, coordinated workflows. Version 2 introduces systematic complexity assessment, intelligent routing, comprehensive guardrails, and full observability.

### What is V2 Architecture?

V2 architecture is a **specification-based framework** where:
- **Subagents** coordinate workflows with intelligent routing
- **Skills** provide reusable, portable capabilities
- **Primitives** ensure deterministic operations
- **7-step workflow** ensures consistency and quality
- **Telemetry** provides full observability

### Key Improvements Over V1

| Feature | V1 | V2 |
|---------|----|----|
| Routing | Manual | **Intelligent (complexity-based)** |
| Guardrails | None | **Comprehensive (global + strategy)** |
| Verification | Manual | **Automated (acceptance criteria)** |
| Observability | Minimal | **Full (structured telemetry)** |
| State Management | Ad-hoc | **Persistent (YAML checkpoints)** |
| Error Recovery | Manual | **Automated (resume capability)** |

### Architecture Metrics

- **10 Subagents:** 5 core + 5 persona agents (BMAD v4 parity)
  - **Core (5):** orchestrator, alex-planner, winston-architect, james-developer, quinn-quality
  - **Personas (5):** mary-analyst, john-pm, sarah-po, bob-sm, sally-ux-expert
- **30+ Commands:** Complete coverage from discovery → planning → implementation → quality
- **26 Skills:** Reusable, portable capabilities with V2 contracts (22 core + 4 new planning skills)
- **10 Primitives:** Deterministic file and test operations
- **11,679+ lines:** Total specification code (6,779 core + 4,900 personas)

### Related Documentation

**User-Oriented Documentation** (Focus: How to USE the system)
- [Quick Start Guide](./QUICK-START.md) - Get started in 10 minutes with use cases
- [User Guide](./USER-GUIDE.md) - Comprehensive guide for users
- [Workflow Guide](./WORKFLOW-GUIDE.md) - Real-world workflow examples
- [Command Reference](./COMMAND-REFERENCE-SUMMARY.md) - All commands quick reference

**Technical-Oriented Documentation** (Focus: How the system WORKS)
- [3-Layer Architecture](./3-layer-architecture-for-skills.md) - Technical implementation details
- **[This Document - V2 Architecture]** - System architecture and design
- [Agent Reference](./AGENT-REFERENCE.md) - Agent specifications and routing

**Quick Start by Role:**
- [Alex (Planner) Quick Start](./quickstart-alex.md) - Planning & requirements
- [James (Developer) Quick Start](./quickstart-james.md) - Implementation & TDD
- [Quinn (Quality) Quick Start](./quickstart-quinn.md) - Quality & NFR assessment
- [Orchestrator Quick Start](./quickstart-orchestrator.md) - Workflow coordination

**Additional Resources:**
- [Complete Documentation Index](./DOCUMENTATION-INDEX.md) - Master documentation hub
- [README.md](../README.md) - Project overview and getting started
- [ROADMAP.md](./ROADMAP.md) - Project roadmap and phase progress

---

## Architecture Layers

BMAD Enhanced follows a **3-layer architecture** for separation of concerns:

**Note:** This section provides a high-level overview. For detailed technical implementation including how skills dynamically load and execute, see the [3-Layer Architecture](./3-layer-architecture-for-skills.md) document.

```
┌────────────────────────────────────────────────────────┐
│ Layer 3: Subagents (Intelligent Routing & Coordination)│
├────────────────────────────────────────────────────────┤
│ • orchestrator-v2 (2 commands)                         │
│ • alex-planner-v2 (5 commands)                         │
│ • james-developer-v2 (7 commands)                      │
│ • quinn-quality-v2 (5 commands)                        │
│ • winston-architect (optional)                         │
├────────────────────────────────────────────────────────┤
│ Layer 2: Skills (Reusable Workflow Capabilities)       │
├────────────────────────────────────────────────────────┤
│ • Planning Skills (8)                                  │
│ • Quality Skills (9)                                   │
│ • Development Skills (3)                               │
│ • All with V2 contracts                                │
├────────────────────────────────────────────────────────┤
│ Layer 1: Primitives (Deterministic Operations)         │
├────────────────────────────────────────────────────────┤
│ • bmad-commands skill (10 Python scripts)              │
│ • File operations, test execution, architecture tools  │
└────────────────────────────────────────────────────────┘
```

### Layer 1: Primitives (bmad-commands)

**Purpose:** Deterministic, testable operations

**Capabilities:**
- File I/O with JSON output
- Test execution with structured reporting
- Architecture diagram generation
- Tech stack analysis
- ADR extraction
- Pattern validation

**Location:** `.claude/skills/bmad-commands/`

### Layer 2: Skills (Workflows)

**Purpose:** Reusable, portable workflow capabilities

**V2 Contract Structure:**
```yaml
---
name: skill-name
description: "What this skill does"
acceptance:
  criterion_1: "Must achieve X"
  criterion_2: "Must ensure Y"
inputs:
  param_1:
    type: string
    required: true
    description: "..."
outputs:
  result_1:
    type: object
    description: "..."
telemetry:
  emit: "skill.completed"
  track:
    - metric_1
    - metric_2
---
```

**Domains:**
- **Planning (8 skills):** Task specs, epic breakdown, estimation, sprint planning
- **Quality (9 skills):** Reviews, NFR assessment, quality gates, risk profiling
- **Development (3 skills):** Implementation, bug fixes, testing

### Layer 3: Subagents (Coordination)

**Purpose:** Intelligent routing and cross-subagent coordination

**Responsibilities:**
- Assess task complexity
- Route to appropriate skill/strategy
- Enforce guardrails
- Verify acceptance criteria
- Emit telemetry
- Coordinate with other subagents

---

## V2 Pattern: 7-Step Workflow

All 19 commands follow a consistent **7-step workflow pattern**:

```
┌──────────────────────────────────────────────────────┐
│ STEP 1: LOAD                                         │
├──────────────────────────────────────────────────────┤
│ • Parse user input                                   │
│ • Load context (files, task specs, previous state)  │
│ • Validate prerequisites                             │
└──────────────────────────────────────────────────────┘
           ↓
┌──────────────────────────────────────────────────────┐
│ STEP 2: ASSESS COMPLEXITY                            │
├──────────────────────────────────────────────────────┤
│ • Calculate complexity score (0-100)                 │
│ • Use 5 weighted factors                             │
│ • Determine routing category                         │
└──────────────────────────────────────────────────────┘
           ↓
┌──────────────────────────────────────────────────────┐
│ STEP 3: ROUTE                                        │
├──────────────────────────────────────────────────────┤
│ • Select strategy based on complexity:               │
│   - Simple (≤30): Quick approach                     │
│   - Standard (31-60): Detailed approach              │
│   - Complex (>60): Comprehensive + escalation        │
└──────────────────────────────────────────────────────┘
           ↓
┌──────────────────────────────────────────────────────┐
│ STEP 4: CHECK GUARDRAILS                             │
├──────────────────────────────────────────────────────┤
│ • Verify global guardrails                           │
│ • Check strategy-specific guardrails                 │
│ • Trigger escalations if needed                      │
└──────────────────────────────────────────────────────┘
           ↓
┌──────────────────────────────────────────────────────┐
│ STEP 5: EXECUTE                                      │
├──────────────────────────────────────────────────────┤
│ • Invoke selected skill                              │
│ • Apply selected strategy                            │
│ • Track execution metrics                            │
└──────────────────────────────────────────────────────┘
           ↓
┌──────────────────────────────────────────────────────┐
│ STEP 6: VERIFY                                       │
├──────────────────────────────────────────────────────┤
│ • Check acceptance criteria                          │
│ • Validate outputs                                   │
│ • Confirm quality standards met                      │
└──────────────────────────────────────────────────────┘
           ↓
┌──────────────────────────────────────────────────────┐
│ STEP 7: EMIT TELEMETRY                               │
├──────────────────────────────────────────────────────┤
│ • Collect metrics                                    │
│ • Serialize to JSON                                  │
│ • Write to telemetry store                           │
└──────────────────────────────────────────────────────┘
```

### Benefits of 7-Step Pattern

- ✅ **Consistency:** All commands follow same pattern
- ✅ **Observability:** Every step tracked
- ✅ **Quality:** Automated verification
- ✅ **Safety:** Guardrails prevent errors
- ✅ **Efficiency:** Intelligent routing

---

## Complexity Assessment

### Overview

Every command calculates a **complexity score (0-100)** using **5 weighted factors** to determine the appropriate routing strategy.

### Formula

```
complexity_score = (factor_1 × weight_1) +
                   (factor_2 × weight_2) +
                   (factor_3 × weight_3) +
                   (factor_4 × weight_4) +
                   (factor_5 × weight_5)
```

### Standard Weights

- **Factor 1:** 30% (most important)
- **Factor 2:** 25%
- **Factor 3:** 20%
- **Factor 4:** 15%
- **Factor 5:** 10% (least important)

### Example: Orchestrator *workflow Command

**Factors:**
1. **Workflow stages** (30%): 1-2=10, 3-4=40, 5-6=70, 7+=90
2. **Subagents involved** (25%): 1=10, 2=40, 3=70, 4+=90
3. **Dependencies** (20%): None=10, Linear=40, Complex=70, Circular=90
4. **Timeline** (15%): <1hr=10, 1-4hr=40, 4-8hr=70, >8hr=90
5. **Risk** (10%): Low=10, Medium=40, High=70, Critical=90

**Example Calculation (feature-delivery):**
- Stages: 4 → 40 points × 0.30 = 12
- Subagents: 3 → 70 points × 0.25 = 17.5
- Dependencies: Linear → 40 points × 0.20 = 8
- Timeline: 2-4hr → 40 points × 0.15 = 6
- Risk: Medium → 40 points × 0.10 = 4
- **Total: 47.5 (Standard complexity)**

### Example: James *implement Command

**Factors:**
1. **Task complexity** (30%): Simple=10, Standard=40, Complex=70, VeryComplex=90
2. **Risk level** (25%): Low=10, Medium=40, High=70, Critical=90
3. **Scope** (20%): 1-2 files=10, 3-5=40, 6-10=70, 10+=90
4. **Dependencies** (15%): None=10, Few=40, Many=70, External=90
5. **Test coverage** (10%): None=10, Basic=40, Comprehensive=70, Critical=90

---

## Intelligent Routing

### Routing Categories

Based on complexity score, commands route to one of **3 strategies**:

```
 0────────30────────60────────100
 │  SIMPLE │ STANDARD │ COMPLEX │
```

### Route 1: Simple (Complexity ≤ 30)

**Characteristics:**
- Quick, straightforward approach
- Minimal overhead
- Basic validation
- In-memory state

**Example:** `@alex *create-task-spec` for clear, simple requirement

**Typical Time:** <15 minutes

### Route 2: Standard (Complexity 31-60)

**Characteristics:**
- Detailed, methodical approach
- Comprehensive validation
- Persistent state
- Resume capability

**Example:** `@james *implement task-001` for moderate feature

**Typical Time:** 15-60 minutes

### Route 3: Complex (Complexity > 60)

**Characteristics:**
- Comprehensive approach with extra care
- User confirmation required (escalation)
- Full state tracking with checkpoints
- Advanced error recovery
- May recommend splitting

**Example:** `@quinn *review` for large refactoring

**Typical Time:** 60+ minutes

### Routing Logic Example

```python
def route_command(complexity_score):
    if complexity_score <= 30:
        return "simple"
    elif complexity_score <= 60:
        return "standard"
    else:
        # Escalate for user confirmation
        confirm = ask_user(f"Complexity: {complexity_score}. Continue?")
        if not confirm:
            return "abort"
        return "complex"
```

---

## Guardrails Framework

### Overview

**Guardrails** prevent errors, enforce quality standards, and escalate when needed. Every command checks both **global** and **strategy-specific** guardrails.

### Global Guardrails (All Commands)

✅ **Availability:**
- All required subagents operational
- Required skills available
- Primitives accessible

✅ **Prerequisites:**
- Required files exist
- Permissions validated
- State directory accessible

✅ **Safety:**
- No conflicting workflows
- Resource locks available
- Backup/rollback possible

### Strategy-Specific Guardrails

Different strategies have different guardrails:

**Example: James *implement Command**

**Simple Strategy (≤30):**
- Max 3 files per change
- Max 300 diff lines
- Require tests
- Min 80% coverage

**Standard Strategy (31-60):**
- Max 5 files per change
- Max 500 diff lines
- Require tests
- Min 80% coverage

**Complex Strategy (>60):**
- Max 10 files per change
- Max 1000 diff lines
- Require tests
- Min 80% coverage
- May require splitting

### Escalation Triggers

**When to escalate to user:**
- Complexity score > 60
- Guardrail violations detected
- Quality gate failures
- Timeline exceeds 8 hours
- Critical risks identified

### Example Guardrail Check

```python
def check_guardrails(context, strategy):
    # Global guardrails
    if not check_prerequisites(context):
        return False, "Prerequisites not met"

    # Strategy-specific guardrails
    if strategy == "simple":
        if context.file_count > 3:
            return False, "Too many files for simple strategy"

    if strategy == "complex":
        # Require user confirmation
        if not context.user_confirmed:
            return False, "User confirmation required"

    return True, "All guardrails passed"
```

---

## Telemetry & Observability

### Overview

Every command emits **structured JSON telemetry** capturing routing decisions, execution metrics, and acceptance verification.

### Telemetry Structure

```json
{
  "agent": "subagent-name",
  "command": "*command-name",
  "timestamp": "2025-02-03T10:30:00Z",

  "routing": {
    "complexity_score": 47.5,
    "factors": {
      "factor_1": 40,
      "factor_2": 70,
      "factor_3": 40,
      "factor_4": 40,
      "factor_5": 40
    },
    "strategy_selected": "standard",
    "reason": "Standard complexity workflow"
  },

  "guardrails": {
    "checked": true,
    "passed": true,
    "violations": [],
    "escalations": []
  },

  "execution": {
    "duration_ms": 180000,
    "skill_used": "create-task-spec",
    "status": "success"
  },

  "acceptance": {
    "criteria_checked": 6,
    "criteria_passed": 6,
    "verified": true
  },

  "result": {
    "task_id": "task-001",
    "task_file": ".claude/tasks/task-001.md"
  }
}
```

### Telemetry Uses

**Observability:**
- Track command performance
- Monitor routing decisions
- Identify bottlenecks

**Quality Assurance:**
- Verify acceptance criteria met
- Track guardrail violations
- Monitor error rates

**Continuous Improvement:**
- Analyze complexity patterns
- Optimize routing thresholds
- Refine guardrails

### Telemetry Storage

**Location:** `workspace/telemetry/`
**Format:** JSON (one file per command or batch)
**Retention:** Configurable (default: 30 days)

---

## State Management

### Overview

Workflows persist state to enable **resume capability** and **error recovery**.

### State File Format (YAML)

```yaml
workflow_id: workflow-001
workflow_type: feature-delivery
status: in_progress
created_at: "2025-02-03T10:00:00Z"
updated_at: "2025-02-03T10:15:00Z"

input:
  feature_description: "User login with email validation"
  options: {}

phases:
  - id: planning
    subagent: alex-planner
    command: "*create-task-spec"
    status: completed
    started_at: "2025-02-03T10:00:00Z"
    completed_at: "2025-02-03T10:03:00Z"
    duration_ms: 180000
    output:
      task_id: "task-auth-002"
      task_file: ".claude/tasks/task-auth-002.md"

  - id: implementation
    subagent: james-developer-v2
    command: "*implement"
    status: in_progress
    started_at: "2025-02-03T10:03:00Z"
    output: null

  - id: review
    status: pending

  - id: pr_creation
    status: pending

current_phase: implementation
total_duration_ms: 900000
error: null
```

### State Checkpoints

**When state is saved:**
- After each phase completion
- Before starting new phase
- On error/interruption
- Periodically during long operations

### Resume Capability

**Resume workflow:**
```bash
@orchestrator *resume workflow-001
```

**Resume logic:**
1. Load workflow state from file
2. Identify current_phase
3. Skip completed phases
4. Continue from current phase

---

## Subagents Overview

### 1. Orchestrator (Workflow Coordinator)

**Commands:** 2
- `*workflow` - Execute complete workflows
- `*coordinate` - Cross-subagent coordination

**Specialties:**
- Workflow orchestration
- Multi-subagent coordination
- State management
- Error recovery

**Use when:**
- Running complete feature delivery
- Coordinating multiple subagents
- Need automated state management

**Learn more:** [Orchestrator Quick Start](./quickstart-orchestrator.md)

---

### 2. Alex (Planner)

**Commands:** 5
- `*create-task-spec` - Create task specifications
- `*breakdown-epic` - Break epics into stories
- `*estimate` - Estimate story points
- `*refine-story` - Refine vague requirements
- `*plan-sprint` - Create sprint plans

**Specialties:**
- Planning and requirements
- Epic breakdown
- Estimation
- Sprint planning

**Use when:**
- Creating task specifications
- Breaking down large work
- Planning sprints

**Learn more:** [Alex Quick Start](./quickstart-alex.md)

---

### 3. James (Developer)

**Commands:** 7
- `*implement` - Implement features (TDD)
- `*fix` - Fix bugs with tests
- `*test` - Run tests with reporting
- `*refactor` - Refactor code safely
- `*apply-qa-fixes` - Apply QA review fixes
- `*debug` - Interactive debugging
- `*explain` - Code explanation

**Specialties:**
- Test-Driven Development
- Feature implementation
- Bug fixing
- Code refactoring

**Use when:**
- Implementing features
- Fixing bugs
- Running tests
- Refactoring code

**Learn more:** [James Quick Start](./quickstart-james.md)

---

### 4. Quinn (Quality)

**Commands:** 5
- `*review` - Comprehensive quality review
- `*assess-nfr` - Assess non-functional requirements
- `*validate-quality-gate` - Quality gate decisions
- `*trace-requirements` - Requirements traceability
- `*assess-risk` - Risk assessment (P×I)

**Specialties:**
- Quality assurance
- NFR assessment
- Quality gates
- Risk profiling

**Use when:**
- Reviewing code quality
- Assessing NFRs
- Making quality gate decisions
- Assessing risks

**Learn more:** [Quinn Quick Start](./quickstart-quinn.md)

---

### 5. Winston (Architect)

**Commands:** 5
- `*design-architecture` - Create system architecture from requirements
- `*analyze-architecture` - Analyze existing (brownfield) codebase architecture
- `*review-architecture` - Peer review architecture for quality and risks
- `*validate-story` - Validate architecture stories
- `*consult` - Interactive architecture consultation

**Specialties:**
- System architecture design
- Technology stack selection
- Architecture Decision Records (ADRs)
- Brownfield architecture analysis
- Architecture quality assessment

**Use when:**
- Designing system architecture (greenfield or brownfield)
- Analyzing existing codebases
- Reviewing architecture quality
- Making technology decisions

---

## Agent Personas (BMAD v4 Parity)

**Purpose:** Specialized persona-driven agents for power users who prefer BMAD v4's interactive, role-specific workflows.

**When to use personas vs. core agents:**
- **Core agents** (Alex, Winston, James, Quinn, Orchestrator): Default for most workflows, automated routing, comprehensive coverage
- **Persona agents**: When you prefer persona-driven interactions, specific workflow styles, or BMAD v4 familiarity

---

### 6. Mary (Analyst)

**Persona:** Business Analyst specializing in brainstorming, market research, and competitive analysis

**Commands:** 6
- `*brainstorm` - Structured brainstorming sessions
- `*create-competitor-analysis` - Competitive landscape analysis
- `*create-project-brief` - Initial project briefs (pre-PRD)
- `*perform-market-research` - TAM/SAM/SOM market research
- `*research-prompt` - Generate deep research prompts
- `*elicit` - Advanced requirements elicitation (Five Whys, JTBD)

**Specialties:**
- Early-stage discovery (before PRD)
- Brainstorming and ideation
- Market research (TAM/SAM/SOM, PESTLE)
- Competitive analysis (Porter's Five Forces, SWOT)
- Requirements elicitation

**Use when:**
- Starting a new project (before requirements formalization)
- Need brainstorming facilitation
- Conducting market research
- Competitive analysis
- Deep requirements elicitation

**Style:** Analytical, inquisitive, creative, facilitative, data-informed

---

### 7. John (PM)

**Persona:** Product Manager specializing in PRD creation and product strategy

**Commands:** 5
- `*create-prd` - Create greenfield PRD (uses create-prd skill)
- `*create-brownfield-prd` - Generate PRD from existing codebase (uses create-brownfield-prd skill)
- `*shard-prd` - Break large PRDs into shards (uses shard-document skill)
- `*create-brownfield-epic` - Create brownfield epic
- `*create-brownfield-story` - Create brownfield user story

**Specialties:**
- PRD creation (greenfield and brownfield)
- Product strategy and feature prioritization
- MoSCoW prioritization
- Brownfield PRD with confidence scoring
- PRD sharding for large documents

**Use when:**
- Creating comprehensive PRDs
- Generating brownfield PRDs from codebases
- Product strategy and feature prioritization
- Breaking large PRDs into manageable pieces

**Style:** Analytical, inquisitive, data-driven, user-focused, pragmatic

**Key Innovation:** Confidence scoring for brownfield PRDs (High/Medium/Low based on code analysis)

---

### 8. Sarah (PO)

**Persona:** Product Owner specializing in story validation and quality assurance

**Commands:** 5
- `*create-epic` - Create epic from requirements
- `*create-story` - Create user story with acceptance criteria
- `*validate-story-draft` - Validate story using INVEST criteria (uses validate-story skill)
- `*shard-doc` - Break documents into shards (uses shard-document skill)
- `*execute-checklist-po` - PO master checklist (uses interactive-checklist skill)

**Specialties:**
- Story validation (INVEST criteria)
- Backlog management and grooming
- Interactive checklist-driven workflows
- Quality guardian role
- Acceptance criteria definition

**Use when:**
- Validating story quality before sprint commitment
- Interactive checklist-driven validation
- Backlog grooming
- Need quality guardian emphasis

**Style:** Detail-oriented, systematic, collaborative, quality-focused

**Key Strength:** Interactive checklist workflows for comprehensive validation

---

### 9. Bob (SM)

**Persona:** Scrum Master specializing in developer handoff

**Commands:** 2
- `*draft` - Create developer-ready story
- `*story-checklist` - Story draft checklist (uses interactive-checklist skill)

**Specialties:**
- Developer-focused story creation
- Crystal-clear requirements (zero ambiguity)
- Developer handoff optimization
- Story draft checklists

**Use when:**
- Need quick, developer-ready story drafts
- Developer handoff clarity is priority
- Simple, straightforward stories
- Minimal overhead workflows

**Style:** Efficient, precise, direct, developer-focused

**Philosophy:** "Crystal-clear stories for dumb AI agents" - assume literal interpretation, zero ambiguity

---

### 10. Sally (UX Expert)

**Persona:** UX Expert specializing in UI/UX design and accessibility

**Commands:** 2
- `*create-front-end-spec` - Create front-end specification with UX details
- `*generate-ui-prompt` - Generate AI UI prompts (v0, Lovable, Artifacts)

**Specialties:**
- UI/UX design and interaction patterns
- Front-end specifications
- WCAG 2.1 AA accessibility compliance
- AI UI prompt generation (v0, Lovable, Claude Artifacts)
- User experience optimization

**Use when:**
- Designing UI/UX for features
- Creating front-end specifications
- Ensuring accessibility compliance
- Generating AI UI prompts
- User experience focus required

**Style:** Empathetic, creative, detail-oriented, user-obsessed, accessibility-focused

**Philosophy:** "Good UX is invisible. Great UX is delightful."

---

## Skills Overview

### Planning Skills (8)

| Skill | Purpose | Subagent |
|-------|---------|----------|
| create-task-spec | Create detailed task specs | Alex |
| breakdown-epic | Break epics into stories | Alex |
| estimate-stories | Estimate story points | Alex |
| refine-story | Refine vague requirements | Alex |
| sprint-plan | Create sprint plans | Alex |
| validate-story | Validate story quality | Alex |
| document-project | Document existing projects | Alex |
| create-architecture | Create architecture docs | Winston |

### Quality Skills (9)

| Skill | Purpose | Subagent |
|-------|---------|----------|
| review-task | Comprehensive quality review | Quinn |
| nfr-assess | Assess non-functional requirements | Quinn |
| quality-gate | Make quality gate decisions | Quinn |
| trace-requirements | Trace requirements to code | Quinn |
| risk-profile | Assess implementation risks | Quinn |
| test-design | Design test strategies | Quinn |
| refactor-code | Refactor code safely | Quinn |
| validate-architecture | Validate architecture quality | Winston |
| architecture-review | Peer review architecture | Winston |

### Development Skills (3)

| Skill | Purpose | Subagent |
|-------|---------|----------|
| implement-feature | Implement features with TDD | James |
| fix-issue | Fix bugs systematically | James |
| run-tests | Run tests with reporting | James |

---

## Workflows

### Feature-Delivery Workflow

**Purpose:** Complete feature from requirement to PR

**Phases:**
1. **Planning** (alex) → Create task specification
2. **Implementation** (james) → Implement with TDD
3. **Review** (quinn) → Quality review
4. **PR Creation** (orchestrator) → Create pull request

**Usage:**
```bash
@orchestrator *workflow feature-delivery "User login with email validation"
```

**Duration:** 1-4 hours
**Complexity:** 47.5 (Standard)

---

### Epic-to-Sprint Workflow

**Purpose:** Break epic into sprint-ready stories

**Phases:**
1. **Breakdown** (alex) → Break epic into stories
2. **Estimation** (alex) → Estimate story points
3. **Sprint Planning** (alex) → Create sprint plan

**Usage:**
```bash
@orchestrator *workflow epic-to-sprint "Shopping Cart System" --velocity 40
```

**Duration:** 30-90 minutes
**Complexity:** 29.5 (Simple)

---

### Sprint-Execution Workflow

**Purpose:** Execute complete sprint

**Phases:**
1. **Sprint Start** (orchestrator) → Initialize sprint
2. **Story Loop** (orchestrator) → For each story:
   - Implement (james)
   - Review (quinn)
   - Fix issues (james, conditional)
   - Validate (quinn)
3. **Sprint Review** (orchestrator) → Generate review
4. **Sprint Retro** (orchestrator) → Generate retrospective

**Usage:**
```bash
@orchestrator *workflow sprint-execution "Sprint 15" --velocity 40
```

**Duration:** 1-2 weeks
**Complexity:** Variable (60-80)

---

## Performance

### Overhead Targets

| Component | Target | Actual | Status |
|-----------|--------|--------|--------|
| Complexity Assessment | <100ms | 20ms avg | ✅ 80% better |
| Guardrail Validation | <150ms | 25ms avg | ✅ 83% better |
| Telemetry (async) | <50ms | 6ms avg | ✅ 88% better |
| **Total** | **<300ms** | **51ms avg** | ✅ **83% better** |

### Performance by Subagent

- **Orchestrator:** 1-5ms overhead (pure arithmetic)
- **Alex:** 5-20ms overhead (some text analysis)
- **James:** 10-30ms overhead (file I/O, scope analysis)
- **Quinn:** 15-50ms overhead (code analysis, report parsing)

### Optimization Features

**Available in Production:**
- ✅ Async telemetry (80% faster)
- ✅ Filesystem caching (5-10ms savings)
- ✅ Parallel guardrails (36% faster)
- ✅ Batch telemetry writes (amortized savings)

**Learn more:** [Performance Optimization Report](./PHASE-3-PERFORMANCE-OPTIMIZATION-REPORT.md)

---

## Best Practices

### 1. Choose the Right Subagent

- **Planning tasks** → Alex
- **Implementation** → James
- **Quality reviews** → Quinn
- **Complete workflows** → Orchestrator

### 2. Let Complexity Assessment Work

Don't override routing unless necessary. The complexity assessment is designed to select the optimal strategy.

### 3. Respect Guardrails

Guardrails prevent errors. If a guardrail triggers, understand why before proceeding.

### 4. Use Workflows for Multi-Step Tasks

For tasks involving multiple subagents, use `@orchestrator *workflow` rather than invoking subagents manually.

### 5. Monitor Telemetry

Review telemetry to understand:
- Which strategies are most common
- Where bottlenecks occur
- Guardrail violation patterns

### 6. Resume Failed Workflows

If a workflow fails, use `@orchestrator *resume <workflow-id>` to continue from the last checkpoint.

---

## Migration Guide

### From BMAD v4 to BMAD Enhanced V2

**What Changed:**
- ✅ Skills now in `.claude/skills/` (was: various locations)
- ✅ Subagents now in `.claude/agents/` (was: `.claude/subagents/`)
- ✅ All skills have V2 contracts (acceptance, inputs, outputs, telemetry)
- ✅ Commands use 7-step workflow (was: ad-hoc)
- ✅ Intelligent routing (was: manual)

**Migration Steps:**
1. Update skill references to `.claude/skills/`
2. Update subagent invocations (new command syntax)
3. Review V2 contracts for new input/output formats
4. Enable async telemetry in configuration
5. Test workflows end-to-end

**Compatibility:**
- ✅ Workflow concepts preserved (Planning → Development → QA)
- ✅ Agent personas maintained (Alex, James, Quinn)
- ✅ BMAD Method v4 quality standards maintained

---

## Additional Resources

**Quick Start Guides:**
- [Alex (Planner) Quick Start](./quickstart-alex.md)
- [James (Developer) Quick Start](./quickstart-james.md)
- [Quinn (Quality) Quick Start](./quickstart-quinn.md)
- [Orchestrator Quick Start](./quickstart-orchestrator.md)

**Architecture Documentation:**
- [3-Layer Architecture](./3-layer-architecture-for-skills.md)
- [Architecture Compliance](./architecture-claude-code-compliance.md)

**Phase Documentation:**
- [Phase 2 Completion](./PHASE-2-COMPLETION.md)
- [Phase 3 Integration Test Report](./PHASE-3-INTEGRATION-TEST-REPORT.md)
- [Phase 3 Performance Report](./PHASE-3-PERFORMANCE-OPTIMIZATION-REPORT.md)

**Project Status:**
- [Roadmap](./ROADMAP.md)
- [Standards](./standards.md)

---

## Support

**Questions?** Open a GitHub Discussion
**Found a bug?** Open a GitHub Issue
**Contributing?** See CONTRIBUTING.md

---

**BMAD Enhanced V2 Architecture**
*Building Maintainable Applications with Deterministic operations*

**Version:** 2.0
**Last Updated:** 2025-02-03
**Status:** ✅ Production Ready

---

*Part of BMAD Enhanced - A migration of BMAD Method v4 to Claude Code native architecture*
