# BMAD Enhanced - Agent Reference

**Complete command reference for all 5 core agents**

**Version:** 2.0 | **Last Updated:** 2025-11-05

---

## Table of Contents

1. [Overview](#overview)
2. [Alex (Planner)](#alex-planner)
3. [James (Developer)](#james-developer)
4. [Quinn (Quality)](#quinn-quality)
5. [Winston (Architect)](#winston-architect)
6. [Orchestrator (Coordinator)](#orchestrator-coordinator)
7. [Command Comparison Matrix](#command-comparison-matrix)

---

## Overview

BMAD Enhanced provides 5 specialized agents with 24 total commands. Each agent follows the V2 pattern with 7-step workflow, intelligent routing, and comprehensive guardrails.

### Agent Summary

| Agent | Role | Commands | Complexity Range |
|-------|------|----------|------------------|
| **Alex** | Planner | 5 | Simple-Standard (10-60) |
| **James** | Developer | 7 | Variable (15-80) |
| **Quinn** | Quality | 5 | Standard-Complex (30-75) |
| **Winston** | Architect | 5 | Standard-Complex (40-70) |
| **Orchestrator** | Coordinator | 2 | Standard-Complex (30-80) |

### V2 Pattern

Every command follows 7 steps:
1. **LOAD** - Parse input, load context
2. **ASSESS** - Calculate complexity (0-100)
3. **ROUTE** - Select strategy (Simple/Standard/Complex)
4. **GUARD** - Check guardrails
5. **EXECUTE** - Run skill
6. **VERIFY** - Validate acceptance criteria
7. **TELEMETRY** - Emit structured data

---

## Alex (Planner)

**Role:** Planning & Requirements Specialist

**Purpose:** Transform requirements into actionable specifications with estimation and sprint planning.

**Quick Start:** [Alex Guide](./quickstart-alex.md)

---

### Command 1: `*create-task-spec`

**Purpose:** Create detailed task specification from requirement

**Syntax:**
```bash
/alex *create-task-spec "<requirement>"
/alex *create-task-spec "User login with email and password"
```

**Input Contract:**
```yaml
requirement:
  type: string
  required: true
  description: "Feature requirement or user story"
context:
  type: string
  required: false
  description: "Additional context (frameworks, constraints)"
```

**Output Contract:**
```yaml
task_id: string              # Generated task identifier
task_file: string            # Path to specification file
objective: string            # Clear goal statement
acceptance_criteria: array   # 3-7 testable conditions
technical_approach: string   # Implementation strategy
test_strategy: string        # Testing approach
estimated_effort: number     # Story points (1-13)
dependencies: array          # Required prerequisites
```

**Complexity Factors:**
- Requirement clarity (30%)
- Scope size (25%)
- Technical complexity (20%)
- Dependencies (15%)
- Constraints (10%)

**Routing:**
- Simple (≤30): Clear, small scope
- Standard (31-60): Moderate complexity
- Complex (>60): Large scope, many dependencies

**Example:**
```bash
/alex *create-task-spec "Add OAuth Google login"

# Output:
✓ Task specification created: .claude/tasks/task-auth-005.md
  Objective: Implement Google OAuth 2.0 authentication
  Acceptance Criteria: 5
  Story Points: 8
  Dependencies: Google OAuth API credentials
```

**When to Use:**
- Starting new feature
- Need structured planning
- Before implementation

**When NOT to Use:**
- Requirement is vague (use *refine-story first)
- Already have task spec

---

### Command 2: `*breakdown-epic`

**Purpose:** Break large epic into manageable user stories

**Syntax:**
```bash
/alex *breakdown-epic "<epic>"
/alex *breakdown-epic "User Authentication System"
```

**Input Contract:**
```yaml
epic:
  type: string
  required: true
  description: "Epic description or file path"
target_size:
  type: string
  required: false
  default: "3-5"
  description: "Target story size in points"
```

**Output Contract:**
```yaml
stories_created: number      # Count of stories
story_files: array           # Paths to story files
total_story_points: number   # Sum of all stories
dependency_map: object       # Story dependencies
recommended_order: array     # Implementation sequence
sprint_suggestions: array    # Sprint allocation recommendations
```

**Complexity Factors:**
- Epic size (30%)
- Dependencies (25%)
- Technical uncertainty (20%)
- Team capacity (15%)
- Timeline constraints (10%)

**Example:**
```bash
/alex *breakdown-epic "Shopping Cart System"

# Output:
✓ Epic broken down: 9 stories
  Total: 32 story points
  Recommended: 3 sprints at 12-15 velocity
  Files: .claude/stories/story-cart-001.md through story-cart-009.md
```

---

### Command 3: `*estimate`

**Purpose:** Estimate story points using structured formula

**Syntax:**
```bash
/alex *estimate "<story>"
/alex *estimate .claude/stories/story-cart-001.md
```

**Input Contract:**
```yaml
story:
  type: string
  required: true
  description: "Story description or file path"
context:
  type: string
  required: false
  description: "Tech stack, constraints"
```

**Output Contract:**
```yaml
story_points: number         # Fibonacci (1,2,3,5,8,13)
estimation_breakdown: object # Factor scores
confidence: string           # High/Medium/Low
assumptions: array           # Estimation assumptions
risks: array                 # Identified risks
```

**Estimation Formula:**
```
5 Factors (0-100 each):
1. Technical Complexity (30%)
2. Scope & Effort (25%)
3. Dependencies (20%)
4. Uncertainty (15%)
5. Testing Requirements (10%)

Story Points mapping:
0-20: 1 point
21-40: 2 points
41-60: 3 points
61-75: 5 points
76-85: 8 points
86-100: 13 points
```

**Example:**
```bash
/alex *estimate "Add product search with filtering"

# Output:
✓ Estimated: 5 story points
  Complexity: 65 (Moderate-High)
  Factors: Tech(70), Scope(60), Deps(50), Uncertainty(40), Testing(70)
  Confidence: Medium
```

---

### Command 4: `*refine-story`

**Purpose:** Clarify vague requirements through structured questioning

**Syntax:**
```bash
/alex *refine-story "<vague-requirement>"
/alex *refine-story "Users want better security"
```

**Input Contract:**
```yaml
story:
  type: string
  required: true
  description: "Vague or ambiguous requirement"
clarifications:
  type: object
  required: false
  description: "Answers to clarifying questions"
```

**Output Contract:**
```yaml
refined_story: string        # Clear, specific requirement
acceptance_criteria: array   # Concrete conditions
clarifying_questions: array  # Questions answered
assumptions: array           # Documented assumptions
refined_file: string         # Path to refined story
```

**Refinement Process:**
1. Identify ambiguities
2. Ask clarifying questions
3. Generate refined specification
4. Document assumptions

**Example:**
```bash
/alex *refine-story "Improve app performance"

# Output:
✓ Story refined: .claude/stories/story-perf-001-refined.md
  Clarifications: 7 questions answered
  Specific Requirements:
  - Reduce API response time from 450ms to <200ms
  - Implement Redis caching
  - Add database indexes
  Acceptance Criteria: 5 testable conditions
```

---

### Command 5: `*plan-sprint`

**Purpose:** Create detailed sprint plan from backlog

**Syntax:**
```bash
/alex *plan-sprint --velocity <points> [options]
/alex *plan-sprint --velocity 40 --team-size 4
```

**Input Contract:**
```yaml
velocity:
  type: number
  required: true
  description: "Team velocity (story points per sprint)"
sprint_length:
  type: string
  required: false
  default: "2-weeks"
  options: ["1-week", "2-weeks", "3-weeks"]
team_size:
  type: number
  required: false
  default: 3
stories:
  type: array
  required: false
  description: "Story files (default: backlog)"
```

**Output Contract:**
```yaml
sprint_plan_file: string     # Path to sprint plan
committed_points: number     # Points committed (≤95% velocity)
stories_selected: array      # Stories in sprint
daily_breakdown: object      # Day-by-day plan
team_allocation: object      # Developer assignments
dependency_analysis: object  # Critical path
risks: array                 # Identified sprint risks
sprint_goal: string          # Sprint objective
```

**Planning Algorithm:**
1. Load backlog (estimated stories)
2. Prioritize by value + dependencies
3. Allocate to fit velocity (max 95%)
4. Map dependencies
5. Distribute across team
6. Identify risks

**Example:**
```bash
/alex *plan-sprint --velocity 40 --sprint-length 2-weeks

# Output:
✓ Sprint plan created: .claude/sprints/sprint-15-plan.md
  Committed: 38 points (95% capacity)
  Stories: 8
  Team Allocation:
  - Dev A: 15 pts (Stories 1,4,7)
  - Dev B: 8 pts (Stories 2,6,8)
  - Dev C: 8 pts (Story 3)
  - Dev D: 5 pts (Story 5)
  Buffer: 2 points
```

---

## James (Developer)

**Role:** Implementation Specialist with TDD

**Purpose:** Implement features, fix bugs, run tests, refactor code using Test-Driven Development.

**Quick Start:** [James Guide](./quickstart-james.md)

---

### Command 1: `*implement` 🌍

**Purpose:** Implement features with TDD workflow

**Syntax:**
```bash
/james *implement <task-id> [--subtask <subtask-id>] [--framework <framework>]
/james *implement task-auth-001
/james *implement task-auth-001 --framework pytest
/james *implement task-auth-001 --subtask subtask-1
```

**Input Contract:**
```yaml
task_id:
  type: string
  required: true
  description: "Task specification identifier"
subtask_id:
  type: string
  required: false
  description: "Optional subtask identifier (e.g., subtask-1)"
  validation: "Must match pattern: subtask-{number}"
framework:
  type: string
  required: false
  default: "auto-detect"
  options: ["auto-detect", "jest", "pytest", "junit", "gtest", "cargo", "go"]
```

**Output Contract:**
```yaml
success: boolean
files_created: array         # Source + test files
tests_total: number
tests_passed: number
coverage_percent: number     # Must be ≥ 80%
tdd_cycle: object           # RED/GREEN/REFACTOR metrics
duration_ms: number
```

**TDD Workflow:**
1. **RED:** Write failing tests (all fail)
2. **GREEN:** Implement code (all pass)
3. **REFACTOR:** Improve quality (tests still pass)

**Complexity Factors:**
- Files affected (30%)
- Database changes (25%)
- API changes (20%)
- Dependencies (15%)
- Test complexity (10%)

**Guardrails:**
- Max 5-10 files (based on complexity)
- Coverage ≥ 80%
- All tests must pass
- Task spec required

**Framework Support (Auto-Detected):**
- Jest (JavaScript/TypeScript)
- Pytest (Python)
- JUnit (Java/Kotlin)
- Google Test (C/C++)
- Cargo test (Rust)
- Go test (Go)

**Example:**
```bash
# Implement full task
/james *implement task-login-001

# Output:
✓ Implementation complete
  TDD Cycle:
  - RED: 12 tests written (all failing)
  - GREEN: Implementation complete (all passing)
  - REFACTOR: Code optimized
  Files:
  - src/auth/login.ts (120 lines)
  - tests/auth/login.test.ts (180 lines)
  Coverage: 95%
  Duration: 18 minutes

# Implement specific subtask (for incremental development)
/james *implement task-auth-002 --subtask subtask-1

# Output:
✓ Subtask implementation complete
  Subtask: subtask-1 (Implement data model)
  TDD Cycle:
  - RED: 5 tests written (all failing)
  - GREEN: Implementation complete (all passing)
  - REFACTOR: Code optimized
  Files:
  - src/auth/models.ts (60 lines)
  - tests/auth/models.test.ts (90 lines)
  Coverage: 92%
  Duration: 8 minutes
```

---

### Command 2: `*fix`

**Purpose:** Fix bugs with root cause analysis

**Syntax:**
```bash
/james *fix <bug-id>
/james *fix bug-login-timeout --reproduce-steps "..."
```

**Input Contract:**
```yaml
bug_id:
  type: string
  required: true
reproduce_steps:
  type: string
  required: false
  description: "Steps to reproduce"
priority:
  type: string
  required: false
  options: ["low", "medium", "high", "critical"]
```

**Output Contract:**
```yaml
success: boolean
root_cause: string           # Identified cause
fix_description: string      # What was fixed
files_changed: array
regression_tests_added: number
related_issues: array        # Similar patterns found
```

**Fix Process:**
1. Reproduce bug
2. Write failing test
3. Root cause analysis
4. Implement fix
5. Verify fix
6. Add regression tests
7. Check for similar issues

**Complexity Factors:**
- Affected components (30%)
- Reproduction difficulty (25%)
- Root cause clarity (20%)
- Existing test coverage (15%)
- Impact scope (10%)

**Example:**
```bash
/james *fix bug-memory-leak

# Output:
✓ Bug fixed: bug-memory-leak
  Root Cause: Missing cleanup in useEffect
  Fix: Added return cleanup function
  Files Changed: 1 (MetricsWidget.tsx)
  Regression Tests: 3 added
  Related Issues: Found 2 similar patterns
```

---

### Command 3: `*test` 🌍

**Purpose:** Execute tests with coverage analysis

**Syntax:**
```bash
/james *test <scope>
/james *test task-001
/james *test --all
/james *test src/auth/** --framework pytest
```

**Input Contract:**
```yaml
scope:
  type: string
  required: false
  default: "all"
  description: "Task ID, file pattern, or --all"
framework:
  type: string
  required: false
  default: "auto-detect"
coverage_threshold:
  type: number
  required: false
  default: 80
```

**Output Contract:**
```yaml
total: number                # Total tests
passed: number
failed: number
skipped: number
coverage_percent: number
duration_ms: number
failed_tests: array          # Details of failures
coverage_gaps: array         # Uncovered code
performance_metrics: object
```

**Example:**
```bash
/james *test --all

# Output:
✓ Test execution complete
  Total: 189 tests
  Passing: 189 (100%)
  Coverage: 87%
  Duration: 8.2s
  Coverage Gaps:
  - src/utils/validators.py (lines 45-52)
  - src/api/routes/admin.py (lines 120-130)
```

---

### Command 4: `*refactor`

**Purpose:** Improve code quality safely

**Syntax:**
```bash
/james *refactor <task-id> [--scope conservative|moderate|aggressive]
/james *refactor task-001 --scope moderate
```

**Input Contract:**
```yaml
task_id:
  type: string
  required: true
scope:
  type: string
  required: false
  default: "moderate"
  options: ["conservative", "moderate", "aggressive"]
focus:
  type: string
  required: false
  description: "Specific improvements (e.g., 'reduce complexity')"
```

**Output Contract:**
```yaml
success: boolean
files_refactored: array
improvements: object         # Before/after metrics
tests_status: string         # "all passing"
behavior_preserved: boolean  # Must be true
```

**Refactoring Scopes:**
- **Conservative:** Minimal changes, very safe
- **Moderate:** Standard improvements
- **Aggressive:** Extensive refactoring

**Guarantees:**
- All tests pass before and after
- Behavior preserved
- Code metrics improved

**Complexity Factors:**
- Files to refactor (30%)
- Quality issues (25%)
- Technical debt (20%)
- Test coverage (15%)
- Code complexity (10%)

---

### Command 5: `*apply-qa-fixes`

**Purpose:** Apply fixes from Quinn's review

**Syntax:**
```bash
/james *apply-qa-fixes <task-id>
/james *apply-qa-fixes task-001 --scope high_severity
```

**Input Contract:**
```yaml
task_id:
  type: string
  required: true
scope:
  type: string
  required: false
  options: ["all", "high_severity", "critical"]
```

**Output Contract:**
```yaml
fixes_applied: number
issues_resolved: array
files_changed: array
tests_added: number
```

**Priority Order:**
1. Critical issues (blocking)
2. High severity (security, data loss)
3. Medium severity (performance, usability)
4. Low severity (style, documentation)

---

### Command 6: `*debug`

**Purpose:** Hypothesis-driven debugging

**Syntax:**
```bash
/james *debug "<issue>"
/james *debug "Login tests failing intermittently"
```

**Input Contract:**
```yaml
issue:
  type: string
  required: true
error_log:
  type: string
  required: false
  description: "Path to log file"
```

**Output Contract:**
```yaml
root_cause: string
hypothesis_tested: array
fix_implemented: boolean
prevention_recommendations: array
```

---

### Command 7: `*explain`

**Purpose:** Explain code and generate documentation

**Syntax:**
```bash
/james *explain <file-or-pattern>
/james *explain src/auth/oauth.py --audience developer
```

**Input Contract:**
```yaml
target:
  type: string
  required: true
  description: "File path or pattern"
audience:
  type: string
  required: false
  default: "developer"
  options: ["technical-expert", "developer", "non-technical", "beginner"]
```

**Output Contract:**
```yaml
explanation: string
documentation_generated: string
examples: array
related_files: array
```

---

## Quinn (Quality)

**Role:** Quality Assurance & Risk Assessment

**Purpose:** Ensure quality through comprehensive reviews, NFR assessment, and risk analysis.

**Quick Start:** [Quinn Guide](./quickstart-quinn.md)

---

### Command 1: `*review`

**Purpose:** Comprehensive quality review

**Syntax:**
```bash
/quinn *review <task-id>
/quinn *review task-001 --scope comprehensive
```

**Input Contract:**
```yaml
task_id:
  type: string
  required: true
scope:
  type: string
  required: false
  default: "comprehensive"
  options: ["quick", "standard", "comprehensive"]
```

**Output Contract:**
```yaml
quality_score: number        # 0-100
gate_decision: string        # PASS/CONCERNS/FAIL
dimensions: object           # 6 dimension scores
issues: array                # Categorized by severity
recommendations: array
report_file: string
```

**Review Dimensions:**
1. Functionality (acceptance criteria)
2. Code Quality (complexity, maintainability)
3. Test Coverage (percentage, quality)
4. Security (vulnerabilities, best practices)
5. Performance (efficiency, scalability)
6. Documentation (completeness, clarity)

**Quality Score Scale:**
- 90-100: Excellent (Grade A)
- 80-89: Good (Grade B)
- 70-79: Acceptable (Grade C)
- 60-69: Concerns (Grade D)
- 0-59: Fail (Grade F)

**Gate Decisions:**
- **PASS:** Score ≥ 80, ready for production
- **CONCERNS:** Score 60-79, address issues
- **FAIL:** Score < 60, must fix

---

### Command 2: `*assess-nfr`

**Purpose:** Assess non-functional requirements

**Syntax:**
```bash
/quinn *assess-nfr <task-id> --categories "security,performance"
```

**Input Contract:**
```yaml
task_id:
  type: string
  required: true
categories:
  type: array
  required: false
  default: ["all"]
  options: ["security", "performance", "reliability", "scalability", "maintainability", "usability"]
```

**Output Contract:**
```yaml
overall_score: number        # 0-100
category_scores: object      # Score per category
compliance_status: object    # Met/not met per NFR
gaps: array
recommendations: array
```

**NFR Categories:**
- Security (auth, encryption, validation)
- Performance (response time, throughput)
- Reliability (error handling, recovery)
- Scalability (horizontal/vertical)
- Maintainability (code quality, docs)
- Usability (UX, accessibility)

---

### Command 3: `*validate-quality-gate`

**Purpose:** Make final quality gate decision

**Syntax:**
```bash
/quinn *validate-quality-gate <task-id> --threshold 80
```

**Input Contract:**
```yaml
task_id:
  type: string
  required: true
threshold:
  type: number
  required: false
  default: 80
```

**Output Contract:**
```yaml
gate_decision: string        # PASS/FAIL
scorecard: object            # Detailed scores
blockers: array              # Items preventing pass
recommendations: array
```

---

### Command 4: `*trace-requirements`

**Purpose:** Requirements traceability matrix

**Syntax:**
```bash
/quinn *trace-requirements <task-id>
```

**Input Contract:**
```yaml
task_id:
  type: string
  required: true
```

**Output Contract:**
```yaml
traceability_matrix: object  # Requirement → test mapping
coverage_per_requirement: object
gaps: array
completeness: number         # Percentage
```

---

### Command 5: `*assess-risk`

**Purpose:** Risk assessment using P×I methodology

**Syntax:**
```bash
/quinn *assess-risk "<change>" --scope architecture --impact high
```

**Input Contract:**
```yaml
change:
  type: string
  required: true
  description: "Change being assessed"
scope:
  type: string
  required: false
  options: ["architecture", "implementation", "deployment"]
impact:
  type: string
  required: false
  options: ["low", "medium", "high", "critical"]
```

**Output Contract:**
```yaml
overall_risk_score: number   # 0-100
risks: array                 # Identified risks with P×I scores
risk_distribution: object    # High/Medium/Low counts
mitigation_strategies: array
total_mitigation_cost: string
recommendation: string       # Proceed/Proceed with Caution/Don't Proceed
```

**P×I Methodology:**
- Probability (P): 1-5 scale
- Impact (I): 1-5 scale
- Risk Score: P × I (1-25)

**Risk Categories:**
- High: P×I > 12
- Medium: P×I 6-12
- Low: P×I < 6

---

## Winston (Architect)

**Role:** System Architecture & Design

**Purpose:** Design architecture, analyze codebases, compare options, make technology decisions.

**Quick Start:** [Winston Guide](./quickstart-winston.md)

---

### Command 1: `*analyze-architecture`

**Purpose:** Analyze existing codebase architecture

**Syntax:**
```bash
/winston *analyze-architecture <path>
/winston *analyze-architecture . --depth comprehensive --focus scalability
```

**Input Contract:**
```yaml
path:
  type: string
  required: false
  default: "."
  description: "Codebase path"
depth:
  type: string
  required: false
  default: "comprehensive"
  options: ["quick", "standard", "comprehensive"]
focus:
  type: string
  required: false
  options: ["all", "security", "performance", "scalability"]
```

**Output Contract:**
```yaml
production_readiness_score: number  # 0-100
dimension_scores: object            # 8 dimensions
architecture_quality: number
code_quality: number
test_coverage: number
security: number
performance: number
scalability: number
maintainability: number
technical_debt: number
top_priorities: array               # Top 5 improvements
modernization_opportunities: array
report_file: string                 # Detailed report
diagrams: array                     # Architecture diagrams
tech_stack_inventory: string        # All dependencies
adrs: array                         # Discovered ADRs
```

**8 Quality Dimensions (0-100 each):**
1. Architecture Quality
2. Code Quality
3. Test Coverage
4. Security
5. Performance
6. Scalability
7. Maintainability
8. Technical Debt

**Production Readiness Scale:**
- 90-100: ⭐⭐⭐⭐⭐ Excellent
- 75-89: ⭐⭐⭐⭐ Very Good
- 60-74: ⭐⭐⭐ Good
- 45-59: ⭐⭐ Needs Improvement
- 0-44: ⭐ Significant Issues

---

### Command 2: `*create-architecture`

**Purpose:** Design system architecture from requirements

**Syntax:**
```bash
/winston *create-architecture <requirements>
/winston *create-architecture docs/prd.md --type fullstack --depth comprehensive
```

**Input Contract:**
```yaml
requirements:
  type: string
  required: true
  description: "PRD file or requirements description"
type:
  type: string
  required: false
  options: ["frontend", "backend", "fullstack"]
depth:
  type: string
  required: false
  default: "comprehensive"
```

**Output Contract:**
```yaml
architecture_file: string    # Main architecture document
diagrams: array              # C4 diagrams
data_model: string           # ER diagram
api_specification: string    # OpenAPI spec
technology_stack: object     # Selected technologies
adrs: array                  # Architecture Decision Records
nfr_mapping: object          # NFR compliance
deployment_architecture: object
security_architecture: object
estimated_cost: object       # Development + infrastructure
```

---

### Command 3: `*review-architecture`

**Purpose:** Peer review architecture quality

**Syntax:**
```bash
/winston *review-architecture <file>
/winston *review-architecture docs/architecture.md --focus security
```

**Input Contract:**
```yaml
file:
  type: string
  required: true
  description: "Architecture document path"
focus:
  type: string
  required: false
  options: ["all", "completeness", "quality", "risks", "opportunities"]
```

**Output Contract:**
```yaml
completeness_score: number   # 0-100
quality_score: number        # 0-100
risks: array                 # Identified risks
opportunities: array         # Optimization opportunities
compliance: object           # Standards compliance
decision: string             # PASS/CONCERNS/FAIL
recommendations: array
```

---

### Command 4: `*validate-story`

**Purpose:** Validate architecture story quality

**Syntax:**
```bash
/winston *validate-story <story-file> --mode strict
```

---

### Command 5: `*compare-architectures`

**Purpose:** Compare architecture options with trade-offs

**Syntax:**
```bash
/winston *compare-architectures "<goals>"
/winston *compare-architectures "Scale to 50K users + add real-time" --current docs/analysis.md
```

**Input Contract:**
```yaml
goals:
  type: string
  required: true
  description: "Modernization goals"
current:
  type: string
  required: false
  description: "Current architecture analysis"
constraints:
  type: object
  required: false
  properties:
    budget: string
    timeline: string
```

**Output Contract:**
```yaml
options: array               # 3 options (Minimal, Moderate, Full)
comparison_matrix: object    # Cost/timeline/risk comparison
recommendation: object       # Recommended option with confidence
trade_offs_analysis: object  # Detailed trade-offs
next_steps: array
```

**3 Options Generated:**
- **Option A (Minimal):** Quick wins, low cost, limited benefits
- **Option B (Moderate):** Balanced, usually recommended
- **Option C (Full):** Best long-term, highest cost

---

## Orchestrator (Coordinator)

**Role:** Workflow Coordination

**Purpose:** Execute complete workflows and coordinate multiple subagents.

**Quick Start:** [Orchestrator Guide](./quickstart-orchestrator.md)

---

### Command 1: `*workflow`

**Purpose:** Execute complete workflow

**Syntax:**
```bash
/orchestrator *workflow <type> "<input>"
/orchestrator *workflow feature-delivery "User profile page"
/orchestrator *workflow modernize . "Scale to 100K users"
```

**Input Contract:**
```yaml
type:
  type: string
  required: true
  options: ["feature-delivery", "epic-to-sprint", "sprint-execution", "modernize"]
input:
  type: string
  required: true
  description: "Workflow-specific input"
options:
  type: object
  required: false
```

**Workflow Types:**

**1. feature-delivery**
- Phases: Planning → Implementation → Review → PR
- Duration: 30-120 minutes
- Complexity: 47.5 (Standard)

**2. epic-to-sprint**
- Phases: Breakdown → Estimation → Sprint Planning
- Duration: 30-60 minutes
- Complexity: 29.5 (Simple)

**3. sprint-execution**
- Phases: Sprint Start → Story Loop → Review → Retro
- Duration: 1-2 weeks
- Complexity: 60-80 (Complex)

**4. modernize**
- Phases: Analysis → PRD → Comparison → Architecture → Plan
- Duration: 41-63 minutes (full) or 18-25 minutes (quick)
- Complexity: 49 (Standard)

**Output Contract:**
```yaml
workflow_id: string
success: boolean
phases_executed: number
result: object               # Workflow-specific results
state_file: string           # State for resume
telemetry: object
next_steps: array
```

---

### Command 2: `*coordinate`

**Purpose:** Cross-subagent coordination

**Syntax:**
```bash
/orchestrator *coordinate "<task>" --subagents <list>
/orchestrator *coordinate "Validate architecture and plan" --subagents winston,alex
```

**Input Contract:**
```yaml
task:
  type: string
  required: true
subagents:
  type: array
  required: true
  description: "Comma-separated subagent list"
pattern:
  type: string
  required: false
  options: ["sequential", "parallel", "iterative", "collaborative"]
```

**Output Contract:**
```yaml
coordination_id: string
subagents_used: array
pattern_used: string
success: boolean
result: object
```

**Coordination Patterns:**
- **Sequential:** A → B → C (linear)
- **Parallel:** A ∥ B ∥ C (independent)
- **Iterative:** A → B → A (loops)
- **Collaborative:** A ⇄ B (bidirectional)

---

## Command Comparison Matrix

### By Agent

| Agent | Commands | Total | Avg Complexity |
|-------|----------|-------|----------------|
| Alex | 5 | Planning | Simple-Standard (10-60) |
| James | 7 | Development | Variable (15-80) |
| Quinn | 5 | Quality | Standard-Complex (30-75) |
| Winston | 5 | Architecture | Standard-Complex (40-70) |
| Orchestrator | 2 | Coordination | Standard-Complex (30-80) |

### By Complexity

**Simple Commands (≤30):**
- /alex *create-task-spec (clear requirements)
- /alex *estimate (straightforward stories)

**Standard Commands (31-60):**
- /alex *breakdown-epic
- /alex *refine-story
- /alex *plan-sprint
- /james *implement (moderate features)
- /james *fix (reproducible bugs)
- /james *test
- /james *refactor
- /quinn *review
- /winston *analyze-architecture
- /orchestrator *workflow feature-delivery
- /orchestrator *workflow epic-to-sprint

**Complex Commands (>60):**
- /james *implement (large features)
- /quinn *assess-nfr
- /quinn *assess-risk
- /winston *create-architecture
- /winston *compare-architectures
- /orchestrator *workflow sprint-execution
- /orchestrator *workflow modernize

### By Duration

**Quick (< 15 min):**
- /alex *estimate
- /james *test
- /quinn *trace-requirements

**Standard (15-30 min):**
- /alex *create-task-spec
- /alex *breakdown-epic
- /alex *refine-story
- /alex *plan-sprint
- /james *fix
- /winston *analyze-architecture (quick mode)

**Long (30-60 min):**
- /james *implement
- /james *refactor
- /quinn *review
- /quinn *assess-nfr
- /winston *create-architecture
- /winston *compare-architectures
- /orchestrator *workflow feature-delivery

**Very Long (> 60 min):**
- /orchestrator *workflow sprint-execution (1-2 weeks)
- /orchestrator *workflow modernize (full mode)

---

## Usage Tips

### Choosing the Right Agent

**For Planning:**
- Requirements unclear? → /alex *refine-story
- Need task spec? → /alex *create-task-spec
- Large feature? → /alex *breakdown-epic
- Sprint planning? → /alex *plan-sprint

**For Development:**
- Implement feature? → /james *implement
- Bug fix? → /james *fix
- Run tests? → /james *test
- Improve quality? → /james *refactor

**For Quality:**
- Code review? → /quinn *review
- Quality gate? → /quinn *validate-quality-gate
- Security/performance? → /quinn *assess-nfr
- Risk assessment? → /quinn *assess-risk

**For Architecture:**
- Analyze codebase? → /winston *analyze-architecture
- Design system? → /winston *create-architecture
- Compare options? → /winston *compare-architectures
- Review design? → /winston *review-architecture

**For Automation:**
- Complete workflow? → /orchestrator *workflow
- Multi-agent task? → /orchestrator *coordinate

### Command Chaining

**Common Sequences:**

```bash
# Feature development
/alex *create-task-spec "Feature"
/james *implement task-001
/quinn *review task-001

# Sprint planning
/alex *breakdown-epic "Epic"
/alex *estimate story-001
/alex *plan-sprint --velocity 40

# Modernization
/winston *analyze-architecture .
/winston *compare-architectures "Goals"
/winston *create-architecture --option moderate
```

---

## Related Documentation

- **[Quick Start Guide](./QUICK-START.md)** - 10-minute getting started
- **[User Guide](./USER-GUIDE.md)** - Comprehensive 15-20 page guide
- **[Workflow Guide](./WORKFLOW-GUIDE.md)** - 15 detailed scenarios
- **[Troubleshooting Guide](./TROUBLESHOOTING.md)** - Common issues
- **[Best Practices](./BEST-PRACTICES.md)** - Recommended patterns

---

**BMAD Enhanced Agent Reference**
*Version 2.0 | Complete command reference for all 5 agents*
