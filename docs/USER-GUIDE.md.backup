# BMAD Enhanced - User Guide

**Comprehensive guide to creating and maintaining software products with AI agents**

**Version:** 2.0 | **Status:** Production Ready | **Last Updated:** 2025-11-05

---

## Table of Contents

1. [Introduction & Overview](#1-introduction--overview)
2. [Architecture Explained](#2-architecture-explained)
3. [Getting Started](#3-getting-started)
4. [Working with Each Agent](#4-working-with-each-agent)
5. [Common Workflows](#5-common-workflows)
6. [Slash Commands Reference](#6-slash-commands-reference)
7. [Configuration & Customization](#7-configuration--customization)
8. [Troubleshooting](#8-troubleshooting)
9. [Best Practices](#9-best-practices)

---

## 1. Introduction & Overview

### 1.1 What is BMAD Enhanced?

BMAD Enhanced is a production-ready AI agent system built natively for Claude Code that transforms traditional software development workflows. By coordinating specialized AI agents through an intelligent 3-layer architecture, it reduces development time by 85-90% while maintaining high quality standards.

**Break My AGILE Down - Enhanced Edition**

The name reflects the core mission: break down complex AGILE ceremonies (sprint planning, story breakdown, estimation, implementation, QA) into AI-assisted workflows that complete in minutes rather than hours.

### 1.2 Key Benefits

**For Developers:**
- **Faster Implementation:** TDD-driven feature development in 20-30 minutes
- **Better Quality:** Automated testing with 80%+ coverage guaranteed
- **Reduced Context Switching:** Agents handle coordination and handoffs
- **Learning Aid:** Explains code, generates documentation, teaches patterns

**For Teams:**
- **Consistent Quality:** Every feature follows same high standards
- **Predictable Velocity:** Complexity assessment provides accurate estimates
- **Reduced Technical Debt:** Quality gates prevent shortcuts
- **Better Documentation:** Automatically generated and maintained

**For Projects:**
- **85-90% Time Savings:** From requirement to production-ready code
- **Higher Test Coverage:** TDD enforcement ensures 80%+ coverage
- **Observable Workflows:** Full telemetry tracks every operation
- **Portable Skills:** Reusable capabilities across projects

### 1.3 Core Metrics

| Metric | Before BMAD | After BMAD | Improvement |
|--------|-------------|------------|-------------|
| **Planning Time** | 2-4 hours | 8-12 minutes | 83% reduction |
| **Implementation Time** | 4-8 hours | 20-30 minutes | 87% reduction |
| **Review Time** | 2-3 hours | 10-15 minutes | 83% reduction |
| **Total Feature Time** | 10-17 hours | 48-63 minutes | 85-90% reduction |
| **Test Coverage** | 40-60% | 80-95% | 2x improvement |
| **Quality Score** | Variable | Consistent 80+ | Standardized |

### 1.4 Use Cases

**Primary Use Case: Software Product Development**

BMAD Enhanced excels at:
- Creating new features from requirements
- Fixing bugs systematically
- Improving code quality
- Planning sprints and epics
- Analyzing and modernizing codebases
- Designing system architecture
- Maintaining documentation

**When to Use BMAD Enhanced:**
- Building greenfield applications
- Maintaining brownfield systems
- Modernizing legacy codebases
- Improving quality standards
- Scaling development velocity
- Learning best practices

---

## 2. Architecture Explained

### 2.1 The 3-Layer Architecture

BMAD Enhanced uses a unique 3-layer architecture where skills remain portable and packageable - the layers define HOW skills work together, not different file structures.

**Note for Users:** This section provides a simplified overview focused on understanding use cases. For technical details about how skills dynamically load and execute, see the [3-Layer Architecture](./3-layer-architecture-for-skills.md) document.

```
┌─────────────────────────────────────────────────────┐
│  Layer 3: SUBAGENTS (Coordination)                  │
│  ┌───────────────────────────────────────────────┐  │
│  │  orchestrator, alex, james, quinn, winston    │  │
│  │  • Assess complexity                          │  │
│  │  • Route to appropriate skill                 │  │
│  │  • Enforce guardrails                         │  │
│  │  • Verify acceptance criteria                 │  │
│  └───────────────────────────────────────────────┘  │
│                         ↓                            │
├─────────────────────────────────────────────────────┤
│  Layer 2: SKILLS (Workflows)                        │
│  ┌───────────────────────────────────────────────┐  │
│  │  31 skills across 5 domains                   │  │
│  │  • Planning (13): PRD, stories, estimation    │  │
│  │  • Development (3): implement, fix, test      │  │
│  │  • Quality (9): review, NFR, gates            │  │
│  │  • Brownfield (4): analysis, PRD, compare     │  │
│  │  • Implementation (1): execute tasks          │  │
│  └───────────────────────────────────────────────┘  │
│                         ↓                            │
├─────────────────────────────────────────────────────┤
│  Layer 1: PRIMITIVES (Atomic Operations)            │
│  ┌───────────────────────────────────────────────┐  │
│  │  bmad-commands skill (10 operations)          │  │
│  │  • File I/O with validation                   │  │
│  │  • Test execution (framework-agnostic)        │  │
│  │  • Architecture diagrams                      │  │
│  │  • Tech stack analysis                        │  │
│  └───────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────┘
```

**Layer 1: Primitives** - Atomic, testable operations
- 10 Python scripts in `bmad-commands` skill
- Deterministic: same inputs → same outputs
- Observable: structured JSON output with telemetry
- Framework-agnostic: supports ANY test framework

**Layer 2: Skills** - Reusable workflow capabilities
- 31 skills in `.claude/skills/` directory
- Portable: packageable as .zip files
- Composable: skills call other skills
- Token-efficient: progressive disclosure (52% average reduction)

**Layer 3: Subagents** - Intelligent coordination
- 5 core + 5 persona agents in `.claude/agents/`
- Intelligent routing based on complexity
- Comprehensive guardrails
- Full telemetry and observability

### 2.2 Core Subagents

**Orchestrator (Coordinator)**
- **Role:** Workflow orchestration and cross-subagent coordination
- **Commands:** 2 (*workflow, *coordinate)
- **Use When:** Running complete workflows, coordinating multiple agents
- **Complexity Factors:** Workflow stages, subagents involved, dependencies

**Alex (Planner)**
- **Role:** Planning, requirements, and estimation
- **Commands:** 5 (*create-task-spec, *breakdown-epic, *estimate, *refine-story, *plan-sprint)
- **Use When:** Planning features, breaking down work, estimating effort
- **Complexity Factors:** Requirement clarity, scope size, dependencies

**James (Developer)**
- **Role:** Implementation with Test-Driven Development
- **Commands:** 7 (*implement, *fix, *test, *refactor, *apply-qa-fixes, *debug, *explain)
- **Use When:** Writing code, fixing bugs, running tests
- **Complexity Factors:** Files affected, database changes, API changes
- **Framework Support:** Auto-detects Jest, Pytest, JUnit, GTest, Cargo, Go test

**Quinn (Quality)**
- **Role:** Quality assurance and risk assessment
- **Commands:** 5 (*review, *assess-nfr, *validate-quality-gate, *trace-requirements, *assess-risk)
- **Use When:** Reviewing code, assessing quality, making gate decisions
- **Complexity Factors:** Code volume, quality issues, NFR categories

**Winston (Architect)**
- **Role:** System architecture and design
- **Commands:** 5 (*analyze-architecture, *create-architecture, *review-architecture, *validate-story, *compare-architectures)
- **Use When:** Designing systems, analyzing codebases, making technology decisions
- **Complexity Factors:** System size, architecture complexity, technology choices

### 2.3 Persona Agents (BMAD v4 Parity)

5 additional persona-driven agents for power users:
- **Mary (Analyst):** Brainstorming, market research, competitive analysis
- **John (PM):** PRD creation (greenfield + brownfield)
- **Sarah (PO):** Story validation with INVEST criteria
- **Bob (SM):** Developer-ready story drafts
- **Sally (UX):** UI/UX design, accessibility compliance

### 2.4 V2 Pattern: 7-Step Workflow

Every command follows a consistent 7-step pattern:

1. **LOAD:** Parse input and load context
2. **ASSESS:** Calculate complexity (0-100 scale)
3. **ROUTE:** Select strategy (Simple/Standard/Complex)
4. **GUARD:** Check guardrails and safety constraints
5. **EXECUTE:** Run selected skill/strategy
6. **VERIFY:** Validate acceptance criteria
7. **TELEMETRY:** Emit structured observability data

**Complexity Categories:**
- **Simple (≤30):** Quick approach, minimal overhead, in-memory state
- **Standard (31-60):** Detailed approach, persistent state, resume capability
- **Complex (>60):** Comprehensive approach, user confirmation, advanced recovery

### 2.5 Skills Overview

**31 Skills Organized by Domain:**

**Planning Skills (13):**
- create-task-spec, breakdown-epic, estimate-stories, refine-story
- document-project, sprint-plan, create-architecture, validate-story
- analyze-architecture, create-prd, create-brownfield-prd
- shard-document, interactive-checklist

**Development Skills (3):**
- implement-feature, fix-issue, run-tests

**Quality Skills (9):**
- review-task, refactor-code, quality-gate, nfr-assess
- trace-requirements, risk-profile, test-design
- validate-architecture, architecture-review

**Brownfield Skills (4):**
- analyze-architecture, create-brownfield-prd
- compare-architectures, shard-document

**Implementation Skills (1):**
- execute-task

**Primitives (1):**
- bmad-commands (10 atomic operations)

---

## 3. Getting Started

### 3.1 Installation

**Prerequisites:**
- Claude Code CLI installed
- Git repository
- Test framework (optional but recommended)

**Setup Steps:**

```bash
# 1. Clone repository
git clone <your-bmad-repo>
cd bmad-enhanced

# 2. Verify structure
ls .claude/
# Should see: agents/, commands/, skills/

# 3. Create workspace (optional)
mkdir -p workspace/{tasks,stories,epics,sprints}

# 4. Configure (optional)
cp .claude/skills/bmad-commands/config.example.yaml .claude/config.yaml
# Edit config.yaml with your preferences
```

### 3.2 Configuration

Create `.claude/config.yaml` for custom settings:

```yaml
# Workspace Configuration
workspaceRoot: "./workspace"
epicTemplate: ".claude/templates/epic-template.md"
storyTemplate: ".claude/templates/story-template.md"
taskTemplate: ".claude/templates/task-template.md"

# Testing Configuration
testing:
  framework: "auto-detect"  # or specific: jest, pytest, junit, gtest, cargo, go
  coverageThreshold: 80
  frameworks:
    jest:
      command: ["npm", "test", "--", "--coverage", "--json"]
    pytest:
      command: ["pytest", "--json-report", "--cov"]

# Quality Configuration
quality:
  min_coverage: 80
  max_complexity: 10
  qualityStandards: ".claude/templates/quality-checklist.md"

# Development Configuration
development:
  tdd_required: true
  max_files_simple: 5
  max_files_standard: 7
  max_files_complex: 10
  allowRefactoring: true

# Guardrails
guardrails:
  block_sensitive_files: true
  require_task_spec: true
  never_commit_failing: true
```

### 3.3 First Steps

**Step 1: Verify Installation**

```bash
# Test that agents are accessible
/alex --help
/james --help
/quinn --help
/orchestrator --help
```

**Step 2: Run Your First Command**

```bash
# Create a simple task specification
/alex *create-task-spec "Add a logout button to the navbar"
```

**Step 3: Complete Your First Feature**

```bash
# Option A: Automated (fastest)
/orchestrator *workflow feature-delivery "Add logout button to navbar"

# Option B: Step-by-step (learning mode)
/alex *create-task-spec "Add logout button to navbar"
/james *implement task-generated-id
/quinn *review task-generated-id
```

### 3.4 Understanding Output

**Task Specifications** are created in `.claude/tasks/`
```markdown
# Task: task-ui-001
## Objective
Add logout button to navbar for user authentication

## Acceptance Criteria
1. Button displays "Logout" text
2. Clicking button logs out user
3. User redirected to login page
4. Session cleared completely

## Technical Approach
- React component: LogoutButton
- API call: POST /api/auth/logout
- Redirect: useNavigate() to /login

## Test Strategy
- Unit tests for component
- Integration tests for logout flow
- E2E test for complete UX
```

**Implementation Results** from James:
```
✓ TDD Cycle Complete:
  RED: 8 tests written (all failing)
  GREEN: Implementation complete (all passing)
  REFACTOR: Code optimized

Files:
- src/components/LogoutButton.tsx (45 lines)
- src/components/__tests__/LogoutButton.test.tsx (120 lines)

Coverage: 95%
Quality: PASS
```

**Quality Reviews** from Quinn:
```
Quality Score: 88/100
- Functionality: ✓ PASS (all acceptance criteria met)
- Code Quality: ✓ PASS (complexity: 4, maintainability: 92)
- Test Coverage: ✓ PASS (95%, exceeds 80% threshold)
- Security: ✓ PASS (no vulnerabilities)

Gate Decision: PASS
Ready for production
```

---

## 4. Working with Each Agent

### 4.1 Alex (Planner)

**Purpose:** Transform vague requirements into clear, actionable task specifications.

#### 4.1.1 Creating Task Specifications

```bash
/alex *create-task-spec "User authentication with email and password"
```

**Output Structure:**
- **Objective:** Clear goal statement
- **Acceptance Criteria:** 3-7 testable conditions
- **Technical Approach:** Implementation strategy
- **Test Strategy:** Testing approach
- **Estimated Effort:** Story points (1-13 scale)

**Best Practices:**
- Provide context in requirement description
- Be specific about constraints
- Mention existing systems/frameworks
- Include business context when relevant

#### 4.1.2 Breaking Down Epics

```bash
/alex *breakdown-epic "User Authentication System"
```

**Complexity Assessment:**
- Epic size and scope (30%)
- Dependency complexity (25%)
- Technical uncertainty (20%)
- Team capacity (15%)
- Timeline constraints (10%)

**Output:**
- 5-12 user stories
- Dependency mapping
- Recommended implementation order
- Total story point estimate

#### 4.1.3 Estimating Stories

```bash
/alex *estimate story-auth-001
```

**Estimation Formula:**
Uses 5 factors with weighted scoring:
- Technical complexity
- Scope and effort
- Dependencies
- Uncertainty
- Testing requirements

**Result:** Fibonacci-scale story points (1, 2, 3, 5, 8, 13)

#### 4.1.4 Refining Vague Requirements

```bash
/alex *refine-story "Users need better security"
```

**Clarification Process:**
1. Identifies ambiguities
2. Asks clarifying questions
3. Proposes specific requirements
4. Creates refined specification

#### 4.1.5 Sprint Planning

```bash
/alex *plan-sprint --velocity 40
```

**Planning Process:**
1. Loads backlog stories
2. Prioritizes by value/dependencies
3. Allocates based on velocity
4. Identifies risks and blockers
5. Creates sprint plan document

**Learn More:** [Alex Quick Start Guide](./quickstart-alex.md)

---

### 4.2 James (Developer)

**Purpose:** Implement features using Test-Driven Development with comprehensive quality standards.

#### 4.2.1 Implementing Features

```bash
/james *implement task-auth-001
/james *implement task-auth-001 --subtask subtask-1  # Implement specific subtask
```

**TDD Workflow:**
1. **RED:** Write failing tests first
2. **GREEN:** Implement minimum code to pass
3. **REFACTOR:** Improve code quality
4. **VERIFY:** Run full test suite

**Subtask Support:**
- Use `--subtask <subtask-id>` to implement only a specific subtask from a larger task
- Enables incremental development and easier code review
- Each subtask can be implemented and tested independently

**Complexity Factors:**
- Files affected (30%)
- Database changes (25%)
- API changes (20%)
- Dependencies (15%)
- Test complexity (10%)

**Guardrails:**
- Max 5-10 files per change (based on complexity)
- Test coverage ≥ 80% required
- All tests must pass
- No syntax errors tolerated

**Framework Support (Auto-Detected):**
- Jest (JavaScript/TypeScript)
- Pytest (Python)
- JUnit (Java/Kotlin)
- Google Test (C/C++)
- Cargo test (Rust)
- Go test (Go)

**Custom Framework Example:**
```yaml
# .claude/config.yaml
testing:
  frameworks:
    mocha:
      adapter: ".claude.custom_adapters.mocha_adapter.MochaAdapter"
      command: ["npm", "run", "test:mocha", "--", "--reporter", "json"]
      patterns:
        source: ["**/*.test.js"]
```

#### 4.2.2 Fixing Bugs

```bash
/james *fix bug-login-timeout
```

**Systematic Process:**
1. Reproduce bug
2. Write failing test
3. Root cause analysis
4. Implement fix
5. Verify fix
6. Add regression tests

**Output:**
- Bug root cause documented
- Fix implemented with tests
- Related code reviewed
- Prevention recommendations

#### 4.2.3 Running Tests

```bash
# Auto-detect framework
/james *test task-001

# Explicit framework
/james *test task-001 --framework pytest

# Run all tests
/james *test --all

# Specific scope
/james *test src/auth/**
```

**Test Report Includes:**
- Pass/fail status
- Coverage percentage
- Performance metrics
- Failed test details
- Coverage gaps identified
- Missing test suggestions

#### 4.2.4 Refactoring Code

```bash
/james *refactor task-001 --scope moderate
```

**Refactoring Scopes:**
- **Conservative:** Minimal changes, very safe
- **Moderate:** Standard improvements (default)
- **Aggressive:** Extensive refactoring

**Safety Guarantees:**
- All tests must pass before and after
- Behavior preservation verified
- Performance regression checked
- Code metrics improved

#### 4.2.5 Applying QA Fixes

```bash
/james *apply-qa-fixes task-001
```

**Systematic Fix Process:**
1. Load Quinn's review findings
2. Prioritize by severity (high → low)
3. Apply fixes systematically
4. Re-run tests after each fix
5. Document changes

**Complexity Scoring:**
- High severity: 20 points each
- NFR failures: 15 points each
- P0 coverage gaps: 10 points each
- NFR concerns: 5 points each

#### 4.2.6 Debugging Issues

```bash
/james *debug "Login tests failing intermittently"
```

**Hypothesis-Driven Debugging:**
1. Analyze symptoms
2. Generate hypotheses
3. Design experiments
4. Test hypotheses
5. Identify root cause
6. Implement fix

#### 4.2.7 Explaining Code

```bash
/james *explain src/auth/oauth.py --audience developer
```

**Audiences:**
- **Technical Expert:** Brief, assumes deep knowledge
- **Developer:** Standard detail with examples
- **Non-Technical:** Plain language
- **Beginner:** Tutorial style

**Learn More:** [James Quick Start Guide](./quickstart-james.md)

---

### 4.3 Quinn (Quality)

**Purpose:** Ensure quality through comprehensive reviews, NFR assessment, and risk analysis.

#### 4.3.1 Comprehensive Quality Review

```bash
/quinn *review task-001
```

**Review Dimensions:**
1. **Functionality:** Acceptance criteria met?
2. **Code Quality:** Complexity, maintainability, style
3. **Test Coverage:** Percentage and quality
4. **Security:** Vulnerabilities, best practices
5. **Performance:** Efficiency, scalability
6. **Documentation:** Completeness, clarity

**Quality Score (0-100):**
- 90-100: Excellent (Grade A)
- 80-89: Good (Grade B)
- 70-79: Acceptable (Grade C)
- 60-69: Concerns (Grade D)
- 0-59: Fail (Grade F)

**Gate Decisions:**
- **PASS:** Quality score ≥ 80, ready for production
- **CONCERNS:** Score 60-79, issues should be addressed
- **FAIL:** Score < 60, must fix before proceeding

#### 4.3.2 NFR Assessment

```bash
/quinn *assess-nfr task-001
```

**NFR Categories:**
- **Security:** Authentication, authorization, encryption, input validation
- **Performance:** Response time, throughput, resource usage
- **Reliability:** Error handling, fault tolerance, recovery
- **Scalability:** Horizontal/vertical scaling, load handling
- **Maintainability:** Code clarity, documentation, modularity
- **Usability:** UX, accessibility, error messages
- **Compliance:** GDPR, WCAG, industry standards

**Assessment Process:**
1. Identify relevant NFR categories
2. Check compliance for each
3. Identify gaps and risks
4. Provide recommendations
5. Score each category

#### 4.3.3 Quality Gate Validation

```bash
/quinn *validate-quality-gate task-001 --threshold 80
```

**Gate Criteria:**
- Functionality complete (all acceptance criteria met)
- Code quality score ≥ threshold
- Test coverage ≥ 80%
- No critical security vulnerabilities
- No blocking NFR failures

**Output:**
- PASS/FAIL decision
- Detailed scorecard
- Blocker items (if any)
- Recommendations

#### 4.3.4 Requirements Traceability

```bash
/quinn *trace-requirements task-001
```

**Traceability Matrix:**
- Requirement → Test case mapping
- Test coverage per requirement
- Implementation completeness
- Gap identification

#### 4.3.5 Risk Assessment

```bash
/quinn *assess-risk task-001
```

**P×I Methodology:**
- **Probability (P):** 1-5 scale (1=unlikely, 5=certain)
- **Impact (I):** 1-5 scale (1=minor, 5=critical)
- **Risk Score:** P × I (1-25 scale)

**Risk Categories:**
- **High Risk:** P×I > 12 (requires mitigation)
- **Medium Risk:** P×I 6-12 (monitor closely)
- **Low Risk:** P×I < 6 (accept)

**Output:**
- Risk identification
- P×I scoring
- Mitigation strategies
- Monitoring recommendations

**Learn More:** [Quinn Quick Start Guide](./quickstart-quinn.md)

---

### 4.4 Winston (Architect)

**Purpose:** Design system architecture, analyze codebases, and make technology decisions.

#### 4.4.1 Analyzing Existing Architecture

```bash
/winston *analyze-architecture .
```

**Analysis Dimensions (8 quality scores):**
1. **Architecture Quality (0-100):** Patterns, modularity, separation of concerns
2. **Code Quality (0-100):** Complexity, maintainability, style
3. **Test Coverage (0-100):** Percentage and quality
4. **Security (0-100):** Vulnerabilities, best practices
5. **Performance (0-100):** Efficiency, bottlenecks
6. **Scalability (0-100):** Horizontal/vertical scaling capability
7. **Maintainability (0-100):** Documentation, clarity
8. **Technical Debt (0-100):** Accumulated issues

**Production Readiness Score:**
Weighted average of 8 dimensions (0-100)
- 90-100: ⭐⭐⭐⭐⭐ Excellent
- 75-89: ⭐⭐⭐⭐ Very Good
- 60-74: ⭐⭐⭐ Good
- 45-59: ⭐⭐ Needs Improvement
- 0-44: ⭐ Significant Issues

**Output:**
- Detailed analysis document
- Architecture diagrams (C4 model)
- Technology stack inventory
- ADRs (Architecture Decision Records)
- Prioritized recommendations
- Modernization opportunities

#### 4.4.2 Designing Architecture

```bash
/winston *create-architecture requirements.md
```

**Design Process:**
1. Analyze requirements
2. Select architecture patterns
3. Choose technology stack
4. Design data model
5. Create API contracts
6. Document ADRs
7. Generate diagrams

**Output Components:**
- System context diagram (C4 Level 1)
- Container diagram (C4 Level 2)
- Component diagrams (C4 Level 3)
- Technology stack with justifications
- ADRs for key decisions
- Migration strategy (if brownfield)
- Non-functional requirements mapping

#### 4.4.3 Comparing Architecture Options

```bash
/winston *compare-architectures "Scale to 50K users + add real-time"
```

**Generates 3 Options:**

**Option A: Minimal Changes**
- Lowest cost and timeline
- Minimal risk
- Limited long-term benefits
- Quick wins

**Option B: Moderate Refactor** (Usually Recommended)
- Balanced cost/benefit
- Medium timeline
- Good ROI
- Sustainable solution

**Option C: Full Modernization**
- Highest cost and timeline
- Best long-term outcome
- Higher risk
- Future-proof solution

**Trade-Offs Analysis:**
- Cost estimates
- Timeline projections
- Risk assessment
- Performance impact
- Maintainability implications
- Scalability limits

**Recommendation:**
Evidence-based recommendation with confidence score and justification

#### 4.4.4 Reviewing Architecture

```bash
/winston *review-architecture docs/architecture.md
```

**Peer Review Dimensions:**
- Completeness (all required elements present)
- Quality (patterns, practices, decisions)
- Risks (security, performance, scalability)
- Opportunities (optimizations, improvements)
- Compliance (standards, regulations)

**Output:**
- Completeness checklist
- Quality scorecard
- Risk identification
- Optimization recommendations
- Pass/fail decision

#### 4.4.5 Interactive Consultation

```bash
/winston-consult "How do I add real-time features to my app?"
```

**Consultation Patterns:**
1. **Analysis:** "Analyze my architecture for..."
2. **Design:** "Design a system for..."
3. **Comparison:** "Compare options for..."
4. **Advice:** "How do I..." or "What's the best way to..."

**Intelligent Routing:**
- Routes to appropriate workflow based on question
- Asks clarifying questions
- Provides tailored recommendations
- Links to relevant documentation

**Learn More:** [Winston Quick Start Guide](./quickstart-winston.md)

---

### 4.5 Orchestrator (Coordinator)

**Purpose:** Execute complete workflows and coordinate multiple subagents.

#### 4.5.1 Complete Workflows

**Feature Delivery Workflow**
```bash
/orchestrator *workflow feature-delivery "User profile page with avatar upload"
```

**Phases:**
1. Planning (alex) - Create task spec
2. Implementation (james) - TDD implementation
3. Review (quinn) - Quality validation
4. PR Creation - Automated PR with description

**Duration:** 30-120 minutes
**Complexity:** 47.5 (Standard)

---

**Epic to Sprint Workflow**
```bash
/orchestrator *workflow epic-to-sprint "Shopping Cart System" --velocity 40
```

**Phases:**
1. Breakdown (alex) - Break epic into stories
2. Estimation (alex) - Estimate story points
3. Sprint Planning (alex) - Create sprint plan

**Duration:** 30-60 minutes
**Complexity:** 29.5 (Simple)

---

**Sprint Execution Workflow**
```bash
/orchestrator *workflow sprint-execution "Sprint 15" --velocity 40
```

**Phases:**
1. Sprint Start - Initialize sprint state
2. Story Loop - For each story:
   - Implement (james)
   - Review (quinn)
   - Fix issues (james, if needed)
   - Validate (quinn)
3. Sprint Review - Generate review report
4. Sprint Retro - Generate retrospective

**Duration:** 1-2 weeks (automated checkpoints)
**Complexity:** 60-80 (Complex)

---

**Modernization Workflow**
```bash
/orchestrator *workflow modernize . "Scale to 100K users + real-time features"
```

**Phases:**
1. Architecture Analysis (winston) - Analyze existing system
2. Brownfield PRD (alex) - Document current features
3. Architecture Comparison (winston) - Generate 3 options
4. **Interactive Checkpoint:** User selects preferred option
5. Detailed Architecture (winston) - Complete design
6. Implementation Plan (alex) - Epic breakdown

**Duration:** 41-63 minutes
**Complexity:** 49 (Standard)

**Variants:**
- `--interactive`: User input at decision points (default)
- `--quick`: High-level assessment only (18-25 min)
- `--analysis-only`: Only Phase 1 (10-15 min)
- `--auto`: Auto-select recommended option

#### 4.5.2 Cross-Subagent Coordination

```bash
/orchestrator *coordinate "Validate architecture and create plan" --subagents winston,alex
```

**Coordination Patterns:**
- **Sequential:** A → B → C (linear handoffs)
- **Parallel:** A ∥ B ∥ C (independent tasks)
- **Iterative:** A → B → A (feedback loops)
- **Collaborative:** A ⇄ B (bidirectional)

**Use Cases:**
- Architecture validation + implementation planning
- Quality improvement cycles (quinn → james → quinn)
- Parallel feature development

#### 4.5.3 State Management

**Workflow State Persisted:**
- Location: `.claude/orchestrator/workflow-{id}.yaml`
- Checkpoints after each phase
- Resume capability on failure
- Full audit trail

**Resume Failed Workflow:**
```bash
/orchestrator *resume workflow-003
```

**Abort Workflow:**
```bash
/orchestrator *abort workflow-003
```

**Learn More:** [Orchestrator Quick Start Guide](./quickstart-orchestrator.md)

---

## 5. Common Workflows

### 5.1 Greenfield Feature Development

**Scenario:** Build new feature from scratch

```bash
# Automated (fastest)
/orchestrator *workflow feature-delivery "User notifications system"

# Manual (more control)
/alex *create-task-spec "User notifications system"
/james *implement task-notif-001
/james *test task-notif-001
/quinn *review task-notif-001
/james *apply-qa-fixes task-notif-001  # If needed
/quinn *validate-quality-gate task-notif-001
```

**Duration:** 30-120 minutes
**Output:** Production-ready feature with 80%+ test coverage

---

### 5.2 Bug Fix Workflow

**Scenario:** Fix production bug

```bash
# Simple bug
/james *fix bug-login-timeout

# Complex bug requiring investigation
/james *debug "Memory leak in background worker"
/james *implement task-fix-memory-leak
/quinn *review task-fix-memory-leak
```

**Duration:** 10-45 minutes
**Output:** Bug fixed with regression tests

---

### 5.3 Code Quality Improvement

**Scenario:** Improve existing codebase quality

```bash
# Review code
/quinn *review src/payment/

# Refactor
/james *refactor src/payment/processor.py --scope moderate

# Verify improvements
/james *test src/payment/**
/quinn *review src/payment/
```

**Duration:** 20-60 minutes
**Output:** Improved code quality metrics

---

### 5.4 Sprint Planning

**Scenario:** Plan 2-week sprint

```bash
# Complete planning workflow
/orchestrator *workflow epic-to-sprint "Shopping Cart Feature" --velocity 40

# OR Manual planning
/alex *breakdown-epic "Shopping Cart Feature"
/alex *estimate story-cart-001
/alex *estimate story-cart-002
# ... estimate all stories
/alex *plan-sprint --velocity 40
```

**Duration:** 30-60 minutes
**Output:** Sprint plan with 6-10 stories

---

### 5.5 Brownfield Architecture Modernization

**Scenario:** Modernize existing system

```bash
# Interactive workflow
/orchestrator *workflow modernize . "Scale to 50K users + add real-time features"

# OR Step-by-step
/winston *analyze-architecture .
/winston *compare-architectures "Scale to 50K + real-time"
# User selects option B (moderate refactor)
/winston *create-architecture --option moderate
/alex *breakdown-epic "Modernization Implementation Plan"
```

**Duration:** 41-63 minutes (interactive) or 18-25 minutes (quick)
**Output:** Architecture design + implementation plan

---

### 5.6 Architecture Design (Greenfield)

**Scenario:** Design new system architecture

```bash
# Step 1: Requirements
/alex *create-prd "E-commerce Platform Requirements"

# Step 2: Architecture
/winston *create-architecture .claude/requirements/prd.md

# Step 3: Validation
/winston *review-architecture docs/architecture.md

# Step 4: Implementation planning
/alex *breakdown-epic docs/architecture.md
```

**Duration:** 60-90 minutes
**Output:** Complete system architecture + ADRs + diagrams

---

### 5.7 TDD Cycle

**Scenario:** Strict Test-Driven Development

```bash
# Write tests first
/james *implement task-feature-001 --tdd=true

# Verify TDD cycle
# RED: Tests written first (all failing)
# GREEN: Implementation complete (all passing)
# REFACTOR: Code optimized (tests still passing)
```

**Duration:** 30-60 minutes
**Output:** Well-tested feature following TDD principles

---

### 5.8 Quality Assurance Cycle

**Scenario:** Complete QA review and fix cycle

```bash
# Iteration 1
/quinn *review feature/checkout
/james *apply-qa-fixes task-checkout-001

# Iteration 2 (verify fixes)
/quinn *review feature/checkout
/quinn *assess-nfr task-checkout-001

# Final gate
/quinn *validate-quality-gate task-checkout-001 --threshold 80
```

**Duration:** 25-50 minutes
**Output:** Quality-validated feature ready for production

---

## 6. Slash Commands Reference

### 6.1 Architecture Commands

**`/design-architecture <requirements>`**
```bash
/design-architecture requirements.md --type fullstack --depth comprehensive
```
Creates system architecture from requirements with ADRs and diagrams.

**`/analyze-architecture [path]`**
```bash
/analyze-architecture . --depth comprehensive --focus scalability
```
Analyzes existing codebase architecture with production readiness score.

**`/review-architecture <file>`**
```bash
/review-architecture docs/architecture.md --focus security
```
Peer reviews architecture for quality, risks, and opportunities.

**`/winston-consult [question]`**
```bash
/winston-consult "How do I add real-time features to my app?"
```
Interactive architecture consultation with intelligent routing.

### 6.2 Validation Commands

**`/validate-story <story-file>`**
```bash
/validate-story .claude/stories/story-001.md --mode strict
```
Validates user story using INVEST criteria.

### 6.3 Agent Commands

**`/alex <command> <args>`**
Routes planning commands to Alex subagent.

**`/james <command> <args>`**
Routes implementation commands to James subagent.

**`/quinn <command> <args>`**
Routes quality commands to Quinn subagent.

**`/orchestrator <command> <args>`**
Routes workflow commands to Orchestrator.

---

## 7. Configuration & Customization

### 7.1 Configuration File

**Location:** `.claude/config.yaml`

**Complete Configuration Template:**

```yaml
# ============================================================
# BMAD Enhanced Configuration
# ============================================================

# Workspace Configuration
workspaceRoot: "./workspace"
epicTemplate: ".claude/templates/epic-template.md"
storyTemplate: ".claude/templates/story-template.md"
taskTemplate: ".claude/templates/task-template.md"

# Testing Configuration
testing:
  # Auto-detect framework or specify: jest, pytest, junit, gtest, cargo, go
  framework: "auto-detect"

  # Minimum coverage threshold (%)
  coverageThreshold: 80

  # Framework-specific configuration
  frameworks:
    jest:
      command: ["npm", "test", "--", "--coverage", "--json"]
      patterns:
        source: ["src/**/*.ts", "src/**/*.tsx"]
        test: ["**/*.test.ts", "**/*.test.tsx"]

    pytest:
      command: ["pytest", "--json-report", "--cov"]
      patterns:
        source: ["**/*.py"]
        test: ["**/test_*.py", "**/*_test.py"]

    junit:
      build_tool: "maven"  # or "gradle"
      command: ["mvn", "test"]
      patterns:
        source: ["src/main/java/**/*.java"]
        test: ["src/test/java/**/*Test.java"]

    # Add custom framework
    mocha:
      adapter: ".claude.custom_adapters.mocha_adapter.MochaAdapter"
      command: ["npm", "run", "test:mocha", "--", "--reporter", "json"]
      patterns:
        source: ["src/**/*.js"]
        test: ["test/**/*.spec.js"]

# Quality Configuration
quality:
  # Quality standards file
  qualityStandards: ".claude/templates/quality-checklist.md"

  # Minimum coverage (%)
  min_coverage: 80

  # Maximum cyclomatic complexity
  max_complexity: 10

  # Quality gate threshold (0-100)
  gate_threshold: 80

# Development Configuration
development:
  # Require TDD workflow
  tdd_required: true

  # Max files per change (by complexity)
  max_files_simple: 5
  max_files_standard: 7
  max_files_complex: 10

  # Max diff lines per change
  max_diff_lines_simple: 400
  max_diff_lines_standard: 600
  max_diff_lines_complex: 1000

  # Allow refactoring
  allowRefactoring: true

  # Auto-apply QA fixes
  autoApplyQAFixes: false  # Require explicit command

# Guardrails Configuration
guardrails:
  # Block sensitive files (.env, *.key, credentials.json)
  block_sensitive_files: true

  # Require task specification for implementation
  require_task_spec: true

  # Never commit failing tests
  never_commit_failing: true

  # Complexity escalation threshold
  escalation_threshold: 60

  # Sensitive file patterns
  sensitive_patterns:
    - ".env"
    - ".env.*"
    - "*.key"
    - "*.pem"
    - "credentials.json"
    - "secrets.yaml"

# Telemetry Configuration
telemetry:
  # Enable telemetry collection
  enabled: true

  # Telemetry output directory
  output_dir: "./workspace/telemetry"

  # Retention period (days)
  retention_days: 30

  # Async mode (non-blocking)
  async: true

# Orchestration Configuration
orchestration:
  # State directory
  state_dir: ".claude/orchestrator"

  # Resume on failure
  auto_resume: false

  # Max workflow duration (minutes)
  max_workflow_duration: 480  # 8 hours

  # Checkpoint frequency (minutes)
  checkpoint_frequency: 15

# Subagent Configuration
subagents:
  alex:
    enabled: true
    max_epic_size: 20  # Max stories per epic

  james:
    enabled: true
    preferred_framework: "auto-detect"

  quinn:
    enabled: true
    strict_mode: false

  winston:
    enabled: true
    default_depth: "comprehensive"

  orchestrator:
    enabled: true
    default_velocity: 40

# Git Configuration
git:
  # Auto-commit after implementation
  auto_commit: false

  # Auto-create branches
  auto_create_branch: true

  # Branch naming pattern
  branch_pattern: "feature/{task-id}"

  # Commit message template
  commit_template: |
    {type}: {summary}

    {details}

    Task: {task-id}
```

### 7.2 Custom Templates

**Task Template (`.claude/templates/task-template.md`):**

```markdown
# Task: {task-id}

## Objective
{objective}

## Context
{context}

## Acceptance Criteria
{acceptance-criteria}

## Technical Approach
{technical-approach}

## Test Strategy
{test-strategy}

## Estimated Effort
{story-points} story points

## Dependencies
{dependencies}

## Notes
{notes}
```

**Epic Template (`.claude/templates/epic-template.md`):**

```markdown
# Epic: {epic-id}

## Title
{title}

## Description
{description}

## Business Value
{business-value}

## Stories
{stories}

## Acceptance Criteria
{acceptance-criteria}

## Total Estimate
{total-story-points} story points

## Timeline
{timeline}
```

### 7.3 Custom Test Framework

**Add Custom Framework Adapter:**

```python
# .claude/custom_adapters/mocha_adapter.py
from bmad_commands.framework_adapters.base_adapter import TestFrameworkAdapter
from typing import Dict, Any

class MochaAdapter(TestFrameworkAdapter):
    def parse_results(self, output: str) -> Dict[str, Any]:
        # Parse Mocha JSON output
        import json
        data = json.loads(output)

        return {
            "total": data["stats"]["tests"],
            "passed": data["stats"]["passes"],
            "failed": data["stats"]["failures"],
            "skipped": data["stats"]["pending"],
            "duration_ms": data["stats"]["duration"],
            "coverage_percent": self._extract_coverage(data)
        }

    def get_command(self, project_path: str) -> list:
        return ["npm", "run", "test:mocha", "--", "--reporter", "json"]
```

**Register in config:**

```yaml
testing:
  frameworks:
    mocha:
      adapter: ".claude.custom_adapters.mocha_adapter.MochaAdapter"
      command: ["npm", "run", "test:mocha", "--", "--reporter", "json"]
      patterns:
        source: ["src/**/*.js"]
        test: ["test/**/*.spec.js"]
```

---

## 8. Troubleshooting

### 8.1 Common Issues

**Issue: "Task specification required"**

**Cause:** James requires task spec for implementation

**Solution:**
```bash
/alex *create-task-spec "Your feature description"
/james *implement task-generated-id
```

---

**Issue: "Complexity too high - requires approval"**

**Cause:** Complexity score > 60 triggers escalation

**Solution:**
```bash
# Option 1: Proceed with confirmation (James will prompt)

# Option 2: Break down task
/alex *breakdown-epic "Large feature"
/james *implement task-part-1
/james *implement task-part-2
```

---

**Issue: "Tests failing - coverage below 80%"**

**Cause:** Test coverage doesn't meet threshold

**Solution:**
```bash
# Check coverage report
/james *test task-001

# Add missing tests
# (Edit test files to add uncovered cases)

# Re-run tests
/james *test task-001
```

---

**Issue: "Guardrail violation - too many files"**

**Cause:** Change affects more files than allowed for complexity level

**Solution:**
```bash
# Option 1: Reduce scope
# (Review and minimize files touched)

# Option 2: Split into multiple tasks
/alex *breakdown-epic "Large feature"
```

---

**Issue: "Framework not detected"**

**Cause:** Test framework auto-detection failed

**Solution:**
```bash
# Explicitly specify framework
/james *test task-001 --framework pytest

# Or configure in .claude/config.yaml
testing:
  framework: "pytest"
```

---

**Issue: "Quality gate FAIL"**

**Cause:** Code doesn't meet quality standards

**Solution:**
```bash
# Apply QA fixes
/james *apply-qa-fixes task-001

# Refactor if needed
/james *refactor task-001 --scope moderate

# Re-review
/quinn *review task-001
```

---

**Issue: "Workflow stuck/failed"**

**Cause:** Workflow encountered error during execution

**Solution:**
```bash
# Check workflow status
/orchestrator *status workflow-001

# Resume from last checkpoint
/orchestrator *resume workflow-001

# Or abort if unrecoverable
/orchestrator *abort workflow-001
```

### 8.2 Debug Mode

Enable verbose logging:

```yaml
# .claude/config.yaml
debug:
  enabled: true
  log_level: "DEBUG"
  log_file: "./workspace/debug.log"
```

### 8.3 Performance Issues

**Issue:** Commands running slowly

**Diagnosis:**
```bash
# Check telemetry
cat workspace/telemetry/latest.json | jq '.execution.duration_ms'
```

**Common Causes:**
- Large codebase (use `--depth quick` for faster analysis)
- Network issues (check connectivity)
- Test suite too slow (optimize tests)

---

## 9. Best Practices

### 9.1 Planning Best Practices

**✅ Do:**
- Provide context in requirements
- Break large epics into manageable stories
- Estimate stories before sprint planning
- Review dependencies before committing
- Use refinement for vague requirements

**❌ Don't:**
- Start implementation without task spec
- Create epics > 20 stories
- Skip estimation
- Ignore dependencies
- Commit to sprints without capacity buffer

### 9.2 Development Best Practices

**✅ Do:**
- Follow TDD (tests first)
- Run tests frequently
- Keep changes focused (single responsibility)
- Write descriptive commit messages
- Request code reviews

**❌ Don't:**
- Skip tests
- Commit failing tests
- Make changes > 10 files
- Ignore guardrails
- Bypass quality gates

### 9.3 Quality Best Practices

**✅ Do:**
- Review all implementations
- Address quality concerns promptly
- Maintain 80%+ test coverage
- Fix high-severity issues first
- Track quality metrics

**❌ Don't:**
- Skip reviews
- Ignore NFR failures
- Accept poor test coverage
- Defer security fixes
- Lower quality standards

### 9.4 Architecture Best Practices

**✅ Do:**
- Analyze before designing
- Document key decisions (ADRs)
- Consider scalability from start
- Review architecture before implementation
- Compare options for major decisions

**❌ Don't:**
- Design without requirements
- Skip architecture for "simple" projects
- Make technology decisions without justification
- Ignore production readiness scores
- Over-architect simple systems

### 9.5 Workflow Best Practices

**✅ Do:**
- Use orchestrator for multi-step workflows
- Let complexity assessment route appropriately
- Save workflow state frequently
- Resume failed workflows
- Monitor progress

**❌ Don't:**
- Manual coordination for complex workflows
- Override routing without good reason
- Ignore workflow failures
- Run workflows without monitoring
- Skip checkpoints

---

## Appendix A: Keyboard Shortcuts

| Shortcut | Command | Description |
|----------|---------|-------------|
| `@a` | /alex | Alex (Planner) |
| `@j` | /james | James (Developer) |
| `@q` | /quinn | Quinn (Quality) |
| `@w` | /winston | Winston (Architect) |
| `@o` | /orchestrator | Orchestrator |

---

## Appendix B: Quick Reference Cards

### Planning Card (Alex)

```
COMMAND                           PURPOSE
*create-task-spec <req>          Create task from requirement
*breakdown-epic <epic>           Break epic into stories
*estimate <story>                Estimate story points
*refine-story <story>            Clarify vague requirements
*plan-sprint --velocity N        Create sprint plan
```

### Development Card (James)

```
COMMAND                           PURPOSE
*implement <task-id>             Implement with TDD
*fix <bug-id>                    Fix bug systematically
*test <scope>                    Run tests
*refactor <task-id>              Improve code quality
*apply-qa-fixes <task-id>        Apply QA fixes
*debug <issue>                   Debug investigation
*explain <file>                  Explain code
```

### Quality Card (Quinn)

```
COMMAND                           PURPOSE
*review <task-id>                Comprehensive review
*assess-nfr <task-id>            Assess NFRs
*validate-quality-gate <task>   Gate decision
*trace-requirements <task>       Traceability
*assess-risk <task>              Risk assessment
```

### Architecture Card (Winston)

```
COMMAND                           PURPOSE
*analyze-architecture <path>     Analyze codebase
*create-architecture <req>       Design system
*review-architecture <file>      Review architecture
*compare-architectures <goals>   Compare options
/winston-consult <question>      Interactive help
```

### Orchestration Card

```
COMMAND                           PURPOSE
*workflow feature-delivery       Complete feature
*workflow epic-to-sprint         Epic → sprint
*workflow sprint-execution       Execute sprint
*workflow modernize             Modernize system
*coordinate --subagents A,B      Coordinate agents
```

---

## Appendix C: Glossary

**Acceptance Criteria:** Testable conditions that must be met for a feature to be considered complete.

**ADR (Architecture Decision Record):** Document capturing key architectural decisions with context, options, and rationale.

**Complexity Score:** 0-100 numeric value calculated from weighted factors to determine routing strategy.

**Epic:** Large body of work broken down into multiple user stories.

**Guardrails:** Safety constraints that prevent errors and enforce quality standards.

**NFR (Non-Functional Requirement):** Quality attribute like security, performance, or reliability.

**P×I (Probability × Impact):** Risk assessment methodology scoring likelihood and severity.

**Primitives:** Atomic, deterministic operations at Layer 1 of the architecture.

**Quality Gate:** Decision point where code must meet quality standards to proceed.

**Skills:** Reusable workflow capabilities at Layer 2 of the architecture.

**Story Points:** Fibonacci-scale (1,2,3,5,8,13) effort estimation unit.

**Subagents:** Intelligent coordination layer (Layer 3) that routes to appropriate skills.

**TDD (Test-Driven Development):** Development approach where tests are written before implementation.

**Telemetry:** Structured observability data capturing execution metrics.

**User Story:** Short description of a feature from end-user perspective.

**Velocity:** Number of story points a team can complete per sprint.

---

## Appendix D: Further Reading

**Core Documentation:**
- [Quick Start Guide](./QUICK-START.md) - 10-minute getting started
- [Workflow Guide](./WORKFLOW-GUIDE.md) - Detailed scenario examples
- [Agent Reference](./AGENT-REFERENCE.md) - Complete command reference
- [Best Practices](./BEST-PRACTICES.md) - Recommended patterns
- [Troubleshooting Guide](./TROUBLESHOOTING.md) - Common issues

**Technical Documentation** (How the system WORKS):
- [3-Layer Architecture](./3-layer-architecture-for-skills.md) - Technical implementation details
- [V2 Architecture](./V2-ARCHITECTURE.md) - System architecture overview
- [Framework Support](./FRAMEWORK-SUPPORT-MATRIX.md) - Supported frameworks

**Quick Start Guides:**
- [Alex (Planner)](./quickstart-alex.md)
- [James (Developer)](./quickstart-james.md)
- [Quinn (Quality)](./quickstart-quinn.md)
- [Winston (Architect)](./quickstart-winston.md)
- [Orchestrator](./quickstart-orchestrator.md)

**Workflow Guides:**
- [Example Workflows](./EXAMPLE-WORKFLOWS.md) - 11 copy-paste workflows
- [Brownfield Workflow Guide](./brownfield-workflow-guide.md) - Modernization

---

**BMAD Enhanced User Guide**
*Version 2.0 | Production Ready | Last Updated: 2025-11-05*

For questions or support, see the [Documentation Index](./DOCUMENTATION-INDEX.md).
