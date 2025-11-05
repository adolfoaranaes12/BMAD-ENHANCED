# BMAD Enhanced Agent Routing Guide

**Version:** 1.0
**Last Updated:** 2025-11-05
**Status:** Complete
**Audience:** All Users

---

## Purpose

This guide helps you choose the right agent for your task. BMAD Enhanced has **10 subagents** (5 core + 5 personas), and knowing which to use ensures optimal workflows.

---

## Quick Decision Tree

```
┌─────────────────────────────────────────────────────────────┐
│ What do you need to do?                                     │
└─────────────────────────────────────────────────────────────┘
                           │
           ┌───────────────┼───────────────┐
           │               │               │
      Discovery         Planning      Implementation
           │               │               │
           ▼               ▼               ▼
    ┌───────────┐   ┌───────────┐   ┌───────────┐
    │   Mary    │   │   Alex    │   │   James   │
    │ (Analyst) │   │ (Planner) │   │(Developer)│
    └───────────┘   └───────────┘   └───────────┘
           │               │               │
       Brainstorm      Task Specs       Implement
       Research        Epic → Stories   TDD, Fixes

           │               │               │
           ▼               ▼               ▼
    ┌───────────┐   ┌───────────┐   ┌───────────┐
    │   John    │   │  Winston  │   │   Quinn   │
    │   (PM)    │   │(Architect)│   │ (Quality) │
    └───────────┘   └───────────┘   └───────────┘
           │               │               │
       PRD Creation    Architecture    Quality Review
       Product Strat   Tech Decisions   NFR Assessment

           │               │               │
           ▼               ▼               ▼
    ┌───────────┐   ┌───────────┐   ┌───────────┐
    │  Sarah    │   │   Bob     │   │  Sally    │
    │   (PO)    │   │   (SM)    │   │(UX Expert)│
    └───────────┘   └───────────┘   └───────────┘
           │               │               │
     Story Validation  Dev Handoff    UI/UX Design
     Backlog Grooming  Simple Stories Front-End Specs
```

---

## Core Agents (5) - Default for Most Workflows

### When to Use Core Agents
- ✅ Default choice for standard workflows
- ✅ Need automated routing and intelligent complexity assessment
- ✅ Comprehensive coverage without persona overhead
- ✅ Coordinating multiple subagents (use Orchestrator)

---

### 1. Orchestrator - Workflow Coordination

**Use when:**
- Running complete feature delivery workflows
- Coordinating multiple agents
- Need automated state management
- Want hands-off execution

**Commands:**
- `@orchestrator *workflow` - Execute complete workflow
- `@orchestrator *coordinate` - Cross-agent coordination

**Example:**
```
@orchestrator *workflow --type feature-delivery --requirement "User authentication"
```

**Don't use when:**
- Single-agent task (use the specific agent directly)
- Exploratory work (orchestrator is for defined workflows)

---

### 2. Alex (Planner) - Planning Specialist

**Use when:**
- Creating task specifications from requirements
- Breaking down epics into stories
- Estimating story points
- Sprint planning
- Refining vague requirements

**Commands:**
- `*create-task-spec` - Create detailed task specs
- `*breakdown-epic` - Break epics into stories
- `*estimate` - Estimate story points
- `*refine-story` - Refine vague requirements
- `*plan-sprint` - Create sprint plans

**Example:**
```
@alex *create-task-spec "User can reset password via email"
```

**Use Alex (not persona agents) when:**
- Need automated, intelligent routing
- Standard planning tasks
- Don't need persona-specific interactions

**Use persona agents instead when:**
- Want PRD creation (→ John/PM)
- Want interactive story validation (→ Sarah/PO)
- Want simple developer stories (→ Bob/SM)

---

### 3. Winston (Architect) - System Architecture

**Use when:**
- Designing system architecture (greenfield or brownfield)
- Analyzing existing codebases
- Making technology stack decisions
- Creating Architecture Decision Records (ADRs)
- Reviewing architecture quality

**Commands:**
- `*design-architecture` - Create architecture from requirements
- `*analyze-architecture` - Analyze brownfield codebase
- `*review-architecture` - Peer review architecture
- `*consult` - Interactive architecture consultation

**Example:**
```
@winston *design-architecture --prd workspace/prd/enterprise-crm.md
```

**Don't use when:**
- Frontend-only design (use Sally/UX Expert for UI/UX)
- Business requirements (use John/PM for PRDs)

---

### 4. James (Developer) - Implementation

**Use when:**
- Implementing features with TDD
- Fixing bugs systematically
- Running tests with comprehensive reporting
- Refactoring code safely
- Applying QA review fixes
- Debugging issues
- Explaining code

**Commands:**
- `*implement` - Implement features (TDD)
- `*fix` - Fix bugs with tests
- `*test` - Run tests with reporting
- `*refactor` - Refactor code safely
- `*apply-qa-fixes` - Apply QA review fixes
- `*debug` - Interactive debugging
- `*explain` - Code explanation

**Example:**
```
@james *implement "workspace/stories/story-password-reset.md"
```

**Don't use when:**
- Planning phase (use Alex or persona agents)
- Architecture design (use Winston)
- Quality review only (use Quinn)

---

### 5. Quinn (Quality) - Quality Assurance

**Use when:**
- Reviewing code quality
- Assessing non-functional requirements (NFRs)
- Making quality gate decisions
- Tracing requirements to implementation
- Risk assessment (Probability × Impact)

**Commands:**
- `*review` - Comprehensive quality review
- `*assess-nfr` - Assess NFRs
- `*validate-quality-gate` - Quality gate decisions
- `*trace-requirements` - Requirements traceability
- `*assess-risk` - Risk assessment

**Example:**
```
@quinn *review "src/auth/password-reset.ts"
```

**Don't use when:**
- Story validation (use Sarah/PO for INVEST criteria)
- Implementation (use James)

---

## Persona Agents (5) - BMAD v4 Parity

### When to Use Persona Agents
- ✅ Prefer persona-driven interactions
- ✅ Need specific workflow styles from BMAD v4
- ✅ Want role-specific communication patterns
- ✅ Power user workflows with nuanced control

---

### 6. Mary (Analyst) - Discovery & Research

**Use when:**
- **Starting a new project** (before PRD creation)
- Brainstorming features or product directions
- Conducting market research (TAM/SAM/SOM)
- Competitive analysis
- Deep requirements elicitation (Five Whys, JTBD)
- Creating project briefs (lighter than PRDs)

**Commands:**
- `*brainstorm` - Structured brainstorming
- `*create-competitor-analysis` - Competitive landscape
- `*create-project-brief` - Initial project brief
- `*perform-market-research` - Market research
- `*research-prompt` - Deep research prompts
- `*elicit` - Advanced elicitation

**Example:**
```
@mary *brainstorm "Ways to improve user onboarding"
```

**Use Mary (not other agents) when:**
- **Early-stage discovery** (before requirements are formalized)
- Need facilitated brainstorming
- Competitive or market analysis

**Don't use Mary when:**
- Requirements are clear → Use Alex (task specs) or John (PRDs)
- Need architecture design → Use Winston

---

### 7. John (PM) - Product Requirements

**Use when:**
- **Creating comprehensive PRDs** (greenfield or brownfield)
- Product strategy and feature prioritization
- Reverse-engineering PRDs from existing codebases
- Breaking large PRDs into manageable shards
- Brownfield epic/story creation

**Commands:**
- `*create-prd` - Create greenfield PRD
- `*create-brownfield-prd` - Generate PRD from codebase
- `*shard-prd` - Break large PRDs
- `*create-brownfield-epic` - Brownfield epic
- `*create-brownfield-story` - Brownfield story

**Example:**
```
@john *create-prd "B2B SaaS platform for customer success teams"
```

**Use John (not other agents) when:**
- Need formal PRD documentation
- Want brownfield PRD with confidence scoring
- Product strategy emphasis

**Don't use John when:**
- Task specifications (use Alex - John creates PRDs, Alex creates task specs)
- Architecture design (use Winston)
- Initial brainstorming (use Mary)

---

### 8. Sarah (PO) - Story Validation

**Use when:**
- **Validating story quality** before sprint commitment
- Interactive checklist-driven validation
- Backlog grooming and prioritization
- Need comprehensive INVEST criteria validation
- Creating epics or stories with quality emphasis

**Commands:**
- `*create-epic` - Create epic
- `*create-story` - Create story with acceptance criteria
- `*validate-story-draft` - Validate story (INVEST)
- `*shard-doc` - Break documents
- `*execute-checklist-po` - PO master checklist

**Example:**
```
@sarah *validate-story-draft "workspace/stories/story-password-reset.md"
```

**Use Sarah (not other agents) when:**
- Need **interactive checklist** validation
- Want quality guardian emphasis
- Backlog grooming focus

**Don't use Sarah when:**
- Simple story creation → Use Bob (faster, developer-focused)
- Epic breakdown → Use Alex (automated decomposition)

---

### 9. Bob (SM) - Developer Handoff

**Use when:**
- Need **quick, developer-ready story drafts**
- Developer handoff clarity is priority
- Simple, straightforward stories
- Want minimal overhead (no extensive validation)
- Story draft checklists

**Commands:**
- `*draft` - Create developer-ready story
- `*story-checklist` - Story draft checklist

**Example:**
```
@bob *draft "Add pagination to user list table"
```

**Use Bob (not other agents) when:**
- Need fast, clear story drafts
- Developer handoff is the priority
- Don't need comprehensive validation

**Don't use Bob when:**
- Complex stories requiring validation → Use Sarah/PO
- Epic breakdown → Use Alex
- PRD creation → Use John

**Bob's Philosophy:** "Crystal-clear stories for dumb AI agents" - zero ambiguity, maximum clarity.

---

### 10. Sally (UX Expert) - UI/UX Design

**Use when:**
- **Designing UI/UX** for features
- Creating front-end specifications
- Ensuring WCAG 2.1 AA accessibility compliance
- Generating AI UI prompts (v0, Lovable, Claude Artifacts)
- User experience optimization

**Commands:**
- `*create-front-end-spec` - Front-end specification
- `*generate-ui-prompt` - AI UI prompts

**Example:**
```
@sally *create-front-end-spec "User dashboard with activity feed"
```

**Use Sally (not other agents) when:**
- UI/UX design required
- Front-end specifications needed
- Accessibility is critical
- Generating prompts for AI UI tools

**Don't use Sally when:**
- Backend architecture → Use Winston
- General planning → Use Alex
- Product requirements → Use John

---

## Routing Scenarios

### Scenario 1: New Feature from Scratch

**Workflow:**
```
1. Mary (*brainstorm) → Ideate feature concepts
2. John (*create-prd) → Formalize into PRD
3. Winston (*design-architecture) → Design system architecture
4. Alex (*breakdown-epic) → Break into stories
5. Sarah (*validate-story-draft) → Validate story quality
6. James (*implement) → Implement with TDD
7. Quinn (*review) → Quality review
8. Orchestrator (*workflow) → Coordinate end-to-end (optional)
```

**Alternative (Core Agents Only):**
```
1. Skip Mary (go straight to requirements)
2. Skip John (use Alex for task specs instead of PRDs)
3. Winston (*design-architecture)
4. Alex (*breakdown-epic)
5. James (*implement)
6. Quinn (*review)
7. Orchestrator (*workflow) for automation
```

---

### Scenario 2: Brownfield Project Enhancement

**Workflow:**
```
1. Winston (*analyze-architecture) → Understand existing codebase
2. John (*create-brownfield-prd) → Generate PRD with confidence scoring
3. Alex (*breakdown-epic) → Break into stories
4. Bob (*draft) → Create developer-ready stories
5. James (*implement) → Implement changes
6. Quinn (*review) → Quality review
```

---

### Scenario 3: Simple Bug Fix

**Direct Approach:**
```
@james *fix "Bug: Password reset link expires too quickly"
```

**If more context needed:**
```
1. Bob (*draft) → Create clear story for the fix
2. James (*fix) → Implement fix
3. Quinn (*review) → Review fix quality (optional for simple bugs)
```

---

### Scenario 4: UI/UX Design Project

**Workflow:**
```
1. Mary (*brainstorm) → Ideate UX improvements
2. Sally (*create-front-end-spec) → Design UI/UX with accessibility
3. Sally (*generate-ui-prompt) → Generate v0/Lovable prompt
4. James (*implement) → Implement UI
5. Quinn (*review) → Accessibility and quality review
```

---

### Scenario 5: Product Strategy Session

**Workflow:**
```
1. Mary (*perform-market-research) → Market analysis
2. Mary (*create-competitor-analysis) → Competitive landscape
3. John (*create-prd) → Formalize product strategy
4. John (*shard-prd) → Break into shards for stakeholder review
5. Alex (*breakdown-epic) → Create roadmap (epics + stories)
```

---

## Routing Decision Matrix

| Need | Core Agent | Persona Agent | Reason |
|------|------------|---------------|--------|
| **Task specification** | Alex | Bob (if simple) | Alex has intelligent routing, Bob is faster for simple stories |
| **PRD creation** | ❌ | John | Only John creates PRDs |
| **Story validation** | ❌ | Sarah | Sarah has interactive checklist workflows |
| **Brainstorming** | ❌ | Mary | Mary facilitates structured ideation |
| **Architecture** | Winston | ❌ | Winston is core, no persona equivalent |
| **Implementation** | James | ❌ | James is core, no persona equivalent |
| **Quality review** | Quinn | ❌ | Quinn is core, no persona equivalent |
| **UI/UX design** | ❌ | Sally | Sally specializes in front-end specs |
| **Market research** | ❌ | Mary | Mary has research frameworks |
| **Epic breakdown** | Alex | ❌ | Alex has automated decomposition |
| **Sprint planning** | Alex | ❌ | Alex has velocity-based planning |

---

## When to Use Orchestrator vs. Direct Agents

### Use Orchestrator when:
- ✅ Running complete feature delivery (planning → implementation → review)
- ✅ Coordinating multiple agents
- ✅ Need automated state management
- ✅ Want hands-off, automated execution

### Use Direct Agents when:
- ✅ Single-agent task (e.g., just brainstorming, just implementation)
- ✅ Exploratory work
- ✅ Need fine-grained control over each step
- ✅ Learning or understanding workflows

**Example (Orchestrator):**
```
@orchestrator *workflow --type feature-delivery --requirement "User can export data to CSV"
```
This automatically routes to: Alex (planning) → Winston (architecture) → James (implementation) → Quinn (quality)

**Example (Direct Agents):**
```
@alex *create-task-spec "User can export data to CSV"
@winston *design-architecture --story workspace/stories/story-csv-export.md
@james *implement workspace/stories/story-csv-export.md
@quinn *review src/export/csv-exporter.ts
```

---

## Common Mistakes & How to Avoid Them

### Mistake 1: Using Wrong Agent for Planning

❌ **Wrong:**
```
@john *create-task-spec "User authentication"
```

✅ **Right:**
```
@alex *create-task-spec "User authentication"  # Task specs → Alex
@john *create-prd "User authentication system" # PRDs → John
```

**Why:** John creates PRDs (product-level), Alex creates task specs (implementation-level).

---

### Mistake 2: Skipping Architecture Design

❌ **Wrong:**
```
@alex *breakdown-epic → @james *implement
```
(No architecture design step)

✅ **Right:**
```
@alex *breakdown-epic → @winston *design-architecture → @james *implement
```

**Why:** Winston ensures technical design is sound before implementation begins.

---

### Mistake 3: Using Core Agent When Persona is Better

❌ **Wrong:**
```
@alex *brainstorm "Product ideas for Q1"
```

✅ **Right:**
```
@mary *brainstorm "Product ideas for Q1"
```

**Why:** Mary has structured brainstorming workflows (Mind Mapping, SCAMPER, etc.), Alex is for task specs.

---

### Mistake 4: Using Persona Agent When Core is Sufficient

❌ **Wrong:**
```
@bob *draft "Complex authentication epic with 15 stories"
```

✅ **Right:**
```
@alex *breakdown-epic "workspace/epics/authentication-epic.md"
```

**Why:** Bob is for simple, single-story drafts. Alex handles epic breakdown with intelligent routing.

---

## Quick Reference Table

| Task | Agent | Command | Time |
|------|-------|---------|------|
| Brainstorm features | Mary | `*brainstorm` | 10-30 min |
| Create PRD | John | `*create-prd` | 30-60 min |
| Create task spec | Alex | `*create-task-spec` | 5-15 min |
| Break down epic | Alex | `*breakdown-epic` | 15-30 min |
| Design architecture | Winston | `*design-architecture` | 20-40 min |
| Validate story | Sarah | `*validate-story-draft` | 5-10 min |
| Create simple story | Bob | `*draft` | 3-5 min |
| Create UI spec | Sally | `*create-front-end-spec` | 20-40 min |
| Implement feature | James | `*implement` | 30-120 min |
| Fix bug | James | `*fix` | 10-30 min |
| Quality review | Quinn | `*review` | 10-20 min |
| Complete workflow | Orchestrator | `*workflow` | 60-180 min |

---

## Summary

**Core Agents (5):** Default choice, automated routing, comprehensive coverage
- Orchestrator, Alex, Winston, James, Quinn

**Persona Agents (5):** BMAD v4 parity, role-specific workflows, power user focus
- Mary, John, Sarah, Bob, Sally

**Rule of Thumb:**
- **Start with core agents** unless you specifically need persona-driven workflows
- **Use personas** when you want BMAD v4 familiarity or need specialized interactions
- **Use orchestrator** for complete, automated workflows
- **Use direct agents** for fine-grained control

---

**Agent Routing Guide**
**Version:** 1.0
**Status:** Complete
**Last Updated:** 2025-11-05
