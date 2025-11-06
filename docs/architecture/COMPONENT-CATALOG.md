# BMAD Enhanced Component Catalog

**Version:** 2.2
**Last Updated:** 2025-11-05
**Status:** Complete Component Reference

---

## Table of Contents

1. [Subagents (10 Total)](#subagents-10-total)
2. [Skills (32 Total)](#skills-32-total)
3. [Primitive Commands (12 Total)](#primitive-commands-12-total)
4. [Templates (5 Total)](#templates-5-total)
5. [UX Tools (3 Total)](#ux-tools-3-total)
6. [Component Relationships](#component-relationships)

---

## Subagents (10 Total)

### Core V2 Subagents (4)

#### 1. Orchestrator V2

**File:** `.claude/agents/orchestrator-v2.md`
**Lines:** 56,661
**Role:** Workflow Coordinator & Cross-Subagent Router
**Model:** Sonnet 4.5

**Commands (2):**
1. `*workflow <type> <input>` - Execute complete workflows
2. `*coordinate <task> --subagents <list>` - Cross-subagent coordination

**Workflow Types:**
- `feature-delivery` - Requirement to PR (Planning → Implementation → Review → PR)
- `epic-to-sprint` - Epic breakdown to sprint plan
- `sprint-execution` - Execute complete sprint
- `modernize` - Complete brownfield modernization (5 phases)
- `document-codebase` - Generate complete documentation (5 phases)

**Key Features:**
- State persistence (`.claude/orchestrator/workflow-*.yaml`)
- Resume capability for failed workflows
- Error recovery with checkpoints
- Interactive user input at decision points

**Performance:**
- Average overhead: 51ms
- State checkpoint: ~5ms per phase
- Full workflow: 45-75 minutes (depending on type)

**Dependencies:**
- Alex (planning)
- James (development)
- Quinn (quality)
- Winston (architecture)

---

#### 2. Alex Planner V2

**File:** `.claude/agents/alex-planner-v2.md`
**Lines:** 27,034
**Role:** Planning & Requirements Management
**Model:** Sonnet 4.5

**Commands (5):**
1. `*create-task-spec "<requirement>"` - Create detailed task specifications
2. `*breakdown-epic "<epic>"` - Break epics into user stories
3. `*estimate "<story>"` - Estimate story points (Fibonacci)
4. `*refine-story "<story>"` - Refine vague requirements
5. `*plan-sprint --velocity <num>` - Create sprint plans

**Complexity Assessment:**
- **Factors:** Scope (30%), Dependencies (25%), Risk (20%), Unknowns (15%), Timeline (10%)
- **Categories:** Simple (≤30), Standard (31-60), Complex (>60)

**Routing Strategies:**
- **Simple:** Quick task spec, basic epic breakdown
- **Standard:** Detailed analysis, comprehensive planning
- **Complex:** Discovery phase, risk assessment, escalation

**Guardrails:**
- Max 20 stories per epic
- Sprint capacity ≤95% of velocity
- Velocity validation against historical data
- Clear acceptance criteria required

**Skills Used:**
- `create-task-spec`
- `breakdown-epic`
- `estimate-stories`
- `refine-story`
- `sprint-plan`

---

#### 3. James Developer V2

**File:** `.claude/agents/james-developer-v2.md`
**Lines:** 83,045
**Role:** Implementation with Test-Driven Development
**Model:** Sonnet 4.5

**Commands (7):**
1. `*implement <task-id>` - TDD-driven feature implementation
2. `*fix <issue-id>` - Bug fixing with test coverage
3. `*test <scope>` - Run tests with framework detection
4. `*refactor <code>` - Safe refactoring with tests
5. `*apply-qa-fixes <task-id>` - Apply fixes from quality reviews
6. `*debug <issue>` - Hypothesis-driven debugging
7. `*explain <code>` - Code explanation (audience-aware)

**TDD Workflow:**
1. **Red Phase:** Write failing tests first
2. **Green Phase:** Implement code to pass tests
3. **Refactor Phase:** Improve while keeping tests green

**Framework Support (6 built-in):**
- **JavaScript/TypeScript:** Jest (auto-detected)
- **Python:** Pytest (auto-detected)
- **Java/Kotlin:** JUnit with Maven/Gradle
- **C/C++:** Google Test with CMake/CTest
- **Rust:** Cargo test
- **Go:** Go test
- **Custom:** Extensible via adapter pattern

**Complexity Assessment:**
- **Factors:** Files (25%), LOC (20%), DB Changes (20%), External APIs (15%), Dependencies (10%), Risk (10%)
- **Categories:** Simple (≤30), Standard (31-60), Complex (>60)

**Guardrails:**
- Min 80% test coverage
- Max 10 files per task
- All tests must pass
- No commented code in implementation
- Clear documentation required

**Skills Used:**
- `implement-feature`
- `implement-v2`
- `fix-issue`
- `apply-qa-fixes`
- `run-tests`

---

#### 4. Quinn Quality V2

**File:** `.claude/agents/quinn-quality-v2.md`
**Lines:** 33,349
**Role:** Quality Assurance & Risk Assessment
**Model:** Sonnet 4.5

**Commands (5):**
1. `*review <task-id>` - Comprehensive quality review
2. `*assess-nfr <task-id>` - Non-functional requirements assessment
3. `*validate-quality-gate <task-id>` - Make quality gate decisions
4. `*trace-requirements <task-id>` - Requirements traceability
5. `*assess-risk <task-id>` - Risk profiling (P×I methodology)

**Quality Dimensions (100 points total):**
- Code Quality (35%): Maintainability, readability, patterns
- Test Quality (30%): Coverage, assertions, edge cases
- Security (15%): Input validation, injection prevention
- Performance (10%): Response time, memory, queries
- Documentation (10%): Comments, README, API docs

**Quality Gates:**
- **PASS:** Score ≥ 80 (deploy to production)
- **CONCERNS:** Score 60-79 (implement with monitoring)
- **FAIL:** Score < 60 (block deployment)

**Risk Assessment (P×I Matrix):**
- **Probability:** Likelihood of risk (1-5 scale)
- **Impact:** Severity if risk occurs (1-5 scale)
- **Risk Score:** P × I (1-25 scale)
- **Categories:** Critical (20-25), High (12-19), Medium (6-11), Low (1-5)

**Complexity Assessment:**
- **Factors:** Files (25%), Complexity (20%), Test Coverage (20%), Security (15%), Performance (10%), Dependencies (10%)
- **Categories:** Simple (≤30), Standard (31-60), Complex (>60)

**Skills Used:**
- `review-task`
- `refactor-code`
- `quality-gate`
- `nfr-assess`
- `trace-requirements`
- `risk-profile`
- `test-design`

---

### Extended Subagents (6)

#### 5. Winston (Architect)

**File:** `.claude/agents/winston-architect.md`
**Lines:** 43,842
**Role:** System Architecture Design & Analysis
**Model:** Sonnet 4.5

**Commands (5):**
1. `*analyze-architecture [path]` - Analyze existing codebase architecture
2. `*create-architecture <requirements>` - Generate system architecture from requirements
3. `*validate-architecture <arch-doc>` - Validate architecture completeness
4. `*review-architecture <arch-doc>` - Peer review architecture for risks
5. `*compare-architectures <requirements>` - Generate 3 architecture options with trade-offs

**Slash Command:**
- `/winston-consult` - Conversational architecture advisor

**Analysis Dimensions (100 points total):**
- Architecture Quality (25%): Patterns, modularity, cohesion
- Code Quality (20%): Maintainability, readability
- Performance (15%): Response time, scalability
- Scalability (15%): Horizontal/vertical scaling
- Security (10%): Authentication, authorization, encryption
- Maintainability (10%): Documentation, testability
- Documentation (5%): Completeness, clarity

**Production Readiness Tiers:**
- **90-100:** Excellent (Production ready, minor polish)
- **80-89:** Very Good (Minor improvements needed)
- **70-79:** Good (Moderate improvements needed)
- **60-69:** Acceptable (Significant improvements needed)
- **Below 60:** Needs Work (Major refactoring required)

**Skills Used:**
- `analyze-architecture`
- `create-architecture`
- `validate-architecture`
- `architecture-review`
- `compare-architectures`
- `create-adr`

---

#### 6. John (PM)

**File:** `.claude/agents/john-pm.md`
**Lines:** 23,617
**Role:** Project Management & Coordination
**Model:** Sonnet 4.5

**Primary Focus:**
- Project planning and tracking
- Resource allocation
- Risk management
- Stakeholder communication
- Timeline management
- Budget oversight

**Key Capabilities:**
- Project charter creation
- Work breakdown structure
- Gantt chart generation
- Resource leveling
- Risk register maintenance

---

#### 7. Sarah (PO)

**File:** `.claude/agents/sarah-po.md`
**Lines:** 28,400
**Role:** Product Ownership & Vision
**Model:** Sonnet 4.5

**Primary Focus:**
- Product vision and strategy
- Backlog prioritization
- User story refinement
- Stakeholder management
- Release planning
- ROI analysis

**Key Capabilities:**
- User story mapping
- Feature prioritization (MoSCoW, RICE)
- Roadmap creation
- KPI tracking
- Acceptance criteria definition

---

#### 8. Bob (SM)

**File:** `.claude/agents/bob-sm.md`
**Lines:** 19,780
**Role:** Scrum Master & Facilitator
**Model:** Sonnet 4.5

**Primary Focus:**
- Sprint facilitation
- Impediment removal
- Ceremony facilitation
- Team coaching
- Process improvement
- Velocity tracking

**Key Capabilities:**
- Sprint planning facilitation
- Daily standup coordination
- Sprint review orchestration
- Retrospective facilitation
- Burndown chart tracking

---

#### 9. Mary (Analyst)

**File:** `.claude/agents/mary-analyst.md`
**Lines:** 33,503
**Role:** Business Analysis & Requirements
**Model:** Sonnet 4.5

**Primary Focus:**
- Requirements elicitation
- Business process modeling
- Gap analysis
- Stakeholder interviews
- Use case documentation
- Acceptance criteria

**Key Capabilities:**
- Business process diagrams
- Use case creation
- Requirements traceability matrix
- Gap analysis reports
- Stakeholder analysis

---

#### 10. Sally (UX Expert)

**File:** `.claude/agents/sally-ux-expert.md`
**Lines:** 27,974
**Role:** UX/UI Design & Usability
**Model:** Sonnet 4.5

**Primary Focus:**
- User experience design
- UI/UX prototyping
- Usability testing
- Accessibility compliance
- Design system creation
- User research

**Key Capabilities:**
- Wireframe creation
- Prototype design
- User journey mapping
- WCAG 2.1 AA compliance validation
- Design system documentation

---

## Skills (32 Total)

### Planning Skills (13)

#### 1. estimate-stories
**Location:** `.claude/skills/planning/estimate-stories/`
**Purpose:** Estimate story points using Fibonacci scale
**Inputs:** Story description or file path
**Outputs:** Story points (1, 2, 3, 5, 8, 13, 21)
**Complexity Factors:** Scope, technical complexity, unknowns, dependencies, risk

#### 2. create-task-spec
**Location:** `.claude/skills/planning/create-task-spec/`
**Purpose:** Create detailed task specifications from requirements
**Inputs:** Requirement description
**Outputs:** Task specification file (`.claude/tasks/task-{id}.md`)
**Sections:** Overview, acceptance criteria, technical approach, testing strategy, dependencies

#### 3. breakdown-epic
**Location:** `.claude/skills/planning/breakdown-epic/`
**Purpose:** Break epics into user stories
**Inputs:** Epic description or file path
**Outputs:** Multiple user story files (`.claude/stories/story-{id}.md`)
**Max Stories:** 20 per epic

#### 4. refine-story
**Location:** `.claude/skills/planning/refine-story/`
**Purpose:** Refine vague requirements into clear user stories
**Inputs:** Vague requirement or incomplete story
**Outputs:** Refined user story with acceptance criteria
**Techniques:** 5W1H, INVEST criteria, Given-When-Then

#### 5. sprint-plan
**Location:** `.claude/skills/planning/sprint-plan/`
**Purpose:** Create sprint plans from backlog
**Inputs:** Velocity (story points per sprint), backlog
**Outputs:** Sprint plan file (`.claude/sprints/sprint-{number}.md`)
**Capacity:** ≤95% of velocity

#### 6. create-architecture
**Location:** `.claude/skills/planning/create-architecture/`
**Purpose:** Generate system architecture from requirements
**Inputs:** PRD or requirements document
**Outputs:** Architecture document (`docs/architecture.md`) with C4 diagrams, ADRs
**Sections:** Context, containers, components, deployment, technology decisions

#### 7. analyze-architecture
**Location:** `.claude/skills/planning/analyze-architecture/`
**Purpose:** Analyze existing codebase architecture
**Inputs:** Codebase path
**Outputs:** Architecture analysis report (`docs/architecture-analysis-{date}.md`)
**Dimensions:** 7 quality dimensions (100-point scale)

#### 8. create-prd
**Location:** `.claude/skills/planning/create-prd/`
**Purpose:** Generate Product Requirements Document
**Inputs:** Product vision, goals, user needs
**Outputs:** PRD file (`docs/prd.md`)
**Sections:** Vision, goals, features, success metrics, constraints

#### 9. create-brownfield-prd
**Location:** `.claude/skills/planning/create-brownfield-prd/`
**Purpose:** Document brownfield system as PRD
**Inputs:** Codebase path
**Outputs:** Brownfield PRD (`docs/brownfield-prd.md`)
**Features:** Feature extraction from code, confidence scores, gaps identification

#### 10. validate-story
**Location:** `.claude/skills/planning/validate-story/`
**Purpose:** Validate user story completeness
**Inputs:** User story file or description
**Outputs:** Validation report (PASS/FAIL with issues)
**Criteria:** INVEST checklist, acceptance criteria presence, clarity

#### 11. shard-document
**Location:** `.claude/skills/planning/shard-document/`
**Purpose:** Break large documents into manageable sections
**Inputs:** Large document path
**Outputs:** Multiple section files
**Max Size:** 500 lines per section

#### 12. interactive-checklist
**Location:** `.claude/skills/planning/interactive-checklist/`
**Purpose:** Interactive task completion tracking
**Inputs:** Task ID or checklist
**Outputs:** Completion status with progress tracking
**Features:** Real-time progress, dependency tracking

#### 13. compare-architectures
**Location:** `.claude/skills/planning/compare-architectures/`
**Purpose:** Generate 3 architecture options with trade-offs
**Inputs:** Requirements, goals, constraints
**Outputs:** Architecture comparison document
**Options:** Minimal changes, moderate refactor, full modernization
**Trade-offs:** Cost, timeline, risk, performance, maintainability

---

### Development Skills (5)

#### 14. implement-feature
**Location:** `.claude/skills/development/implement-feature/`
**Purpose:** TDD-driven feature implementation
**Inputs:** Task ID
**Outputs:** Implementation files, test files, coverage report
**Workflow:** Red → Green → Refactor
**Min Coverage:** 80%

#### 15. implement-v2
**Location:** `.claude/skills/development/implement-v2/`
**Purpose:** V2 implementation with intelligent routing
**Inputs:** Task ID
**Outputs:** Implementation files with V2 telemetry
**Features:** Complexity-based routing, guardrails, state management

#### 16. fix-issue
**Location:** `.claude/skills/development/fix-issue/`
**Purpose:** Bug fixing with test coverage
**Inputs:** Issue description or ID
**Outputs:** Fix implementation, regression tests
**Requirements:** Failing test first, then fix, then verify

#### 17. apply-qa-fixes
**Location:** `.claude/skills/development/apply-qa-fixes/`
**Purpose:** Apply fixes from quality reviews
**Inputs:** Task ID, quality review file
**Outputs:** Fixed code, updated tests
**Process:** Parse findings → Apply fixes → Verify → Update

#### 18. run-tests
**Location:** `.claude/skills/development/run-tests/`
**Purpose:** Execute tests with framework detection
**Inputs:** Scope (all, file, test name)
**Outputs:** Structured test results (JSON)
**Frameworks:** Jest, Pytest, JUnit, GTest, Cargo, Go
**Features:** Auto-detection, consistent output format

---

### Quality Skills (9)

#### 19. review-task
**Location:** `.claude/skills/quality/review-task/`
**Purpose:** Comprehensive code quality review
**Inputs:** Task ID
**Outputs:** Quality report (`.claude/quality/reviews/review-{task-id}.md`)
**Dimensions:** Code quality, test quality, security, performance, documentation
**Scale:** 0-100 points

#### 20. refactor-code
**Location:** `.claude/skills/quality/refactor-code/`
**Purpose:** Safe refactoring with test preservation
**Inputs:** Code file or module
**Outputs:** Refactored code, test validation
**Requirements:** All tests pass before and after

#### 21. quality-gate
**Location:** `.claude/skills/quality/quality-gate/`
**Purpose:** Make quality gate decisions
**Inputs:** Task ID, quality score
**Outputs:** Gate decision (PASS/CONCERNS/FAIL)
**Thresholds:** PASS ≥80, CONCERNS 60-79, FAIL <60

#### 22. nfr-assess
**Location:** `.claude/skills/quality/nfr-assess/`
**Purpose:** Assess non-functional requirements
**Inputs:** Task ID
**Outputs:** NFR assessment report
**Dimensions:** Performance, scalability, security, reliability, usability, maintainability

#### 23. trace-requirements
**Location:** `.claude/skills/quality/trace-requirements/`
**Purpose:** Requirements traceability analysis
**Inputs:** Task ID
**Outputs:** Traceability matrix
**Links:** Requirement → Story → Task → Test → Code

#### 24. risk-profile
**Location:** `.claude/skills/quality/risk-profile/`
**Purpose:** Risk assessment using P×I methodology
**Inputs:** Task ID or component
**Outputs:** Risk profile document
**Scale:** P (1-5) × I (1-5) = Risk Score (1-25)
**Categories:** Critical (20-25), High (12-19), Medium (6-11), Low (1-5)

#### 25. test-design
**Location:** `.claude/skills/quality/test-design/`
**Purpose:** Design comprehensive test strategy
**Inputs:** Task ID or feature description
**Outputs:** Test design document
**Levels:** Unit, integration, system, acceptance

#### 26. validate-architecture
**Location:** `.claude/skills/quality/validate-architecture/`
**Purpose:** Validate architecture completeness
**Inputs:** Architecture document
**Outputs:** Validation report
**Checks:** Required sections, C4 diagrams, ADRs, technology decisions

#### 27. architecture-review
**Location:** `.claude/skills/quality/architecture-review/`
**Purpose:** Peer review architecture for risks
**Inputs:** Architecture document
**Outputs:** Review report with recommendations
**Focus:** Scalability, performance, security, maintainability

---

### Brownfield Skills (1)

#### 28. index-docs
**Location:** `.claude/skills/brownfield/index-docs/`
**Purpose:** Index existing documentation
**Inputs:** Documentation directory
**Outputs:** Documentation index
**Features:** Link validation, completeness check

---

### Implementation Skills (1)

#### 29. execute-task
**Location:** `.claude/skills/implementation/execute-task/`
**Purpose:** Generic task execution
**Inputs:** Task ID
**Outputs:** Execution results
**Use Case:** Custom task workflows

---

### Architecture Skills (New - 3)

#### 30. create-adr
**Location:** `.claude/skills/planning/create-adr/`
**Purpose:** Create Architecture Decision Records
**Inputs:** Decision context, options, chosen solution
**Outputs:** ADR file (`docs/adr/ADR-{number}.md`)
**Format:** Title, status, context, decision, consequences

---

## Primitive Commands (12 Total)

**Location:** `.claude/skills/bmad-commands/scripts/`

### 1. read_file.py
**Purpose:** Read file contents with metadata
**Inputs:** `--path <file-path>`, `--output <json|text>`
**Outputs:** File content, line count, size
**Features:** JSON or text output, error handling

### 2. run_tests.py
**Purpose:** Execute tests with framework detection
**Inputs:** `--framework <name>`, `--scope <all|file|test>`
**Outputs:** Structured test results (JSON)
**Frameworks:** Jest, Pytest, JUnit, GTest, Cargo, Go
**Features:** Auto-detection, adapter pattern, consistent output

### 3. parse_command.py
**Purpose:** Parse and validate commands
**Inputs:** Command string
**Outputs:** Parsed command structure
**Validation:** Syntax, required parameters, types

### 4. framework_registry.py
**Purpose:** Manage test framework adapters
**Inputs:** Framework name
**Outputs:** Adapter instance
**Features:** Registration, lookup, validation

### 5. generate_architecture_diagram.py
**Purpose:** Generate C4 architecture diagrams
**Inputs:** Architecture data (JSON)
**Outputs:** Mermaid diagram code
**Diagram Types:** Context, container, component, deployment

### 6. analyze_tech_stack.py
**Purpose:** Analyze technology choices
**Inputs:** Codebase path
**Outputs:** Technology stack analysis
**Dimensions:** Language, framework, database, tools

### 7. extract_tech_stack.py
**Purpose:** Extract tech stack from codebase
**Inputs:** Codebase path
**Outputs:** Tech stack list (JSON)
**Detection:** package.json, requirements.txt, pom.xml, etc.

### 8. extract_adrs.py
**Purpose:** Extract Architecture Decision Records
**Inputs:** Documentation path
**Outputs:** ADR list (JSON)
**Format:** ADR number, title, status, date

### 9. validate_patterns.py
**Purpose:** Validate architectural patterns
**Inputs:** Codebase path, pattern name
**Outputs:** Pattern validation report
**Patterns:** MVC, MVVM, Layered, Microservices, Event-Driven

### 10. validate_metrics.py
**Purpose:** Validate quality metrics
**Inputs:** Metrics data (JSON)
**Outputs:** Validation report
**Metrics:** Coverage, complexity, duplication, maintainability

### 11-16. Test Framework Adapters
**Location:** `.claude/skills/bmad-commands/scripts/adapters/`

- **jest_adapter.py** - Jest test framework adapter
- **pytest_adapter.py** - Pytest test framework adapter
- **junit_adapter.py** - JUnit test framework adapter
- **gtest_adapter.py** - Google Test adapter
- **cargo_adapter.py** - Rust Cargo test adapter
- **go_adapter.py** - Go test adapter

**Common Interface:**
- `detect()` - Auto-detect framework
- `run_tests(scope)` - Execute tests
- `parse_results()` - Parse output to standard format

---

## Templates (5 Total)

**Location:** `.claude/templates/`

### 1. task-spec.md
**Purpose:** Task specification template
**Sections:** Overview, acceptance criteria, technical approach, testing, dependencies

### 2. quality-gate.md
**Purpose:** Quality gate report template
**Sections:** Summary, quality dimensions, findings, gate decision

### 3. nfr-assessment.md
**Purpose:** Non-functional requirements assessment template
**Sections:** Performance, scalability, security, reliability, usability, maintainability

### 4. risk-profile.md
**Purpose:** Risk assessment template
**Sections:** Risk identification, P×I matrix, mitigation strategies

### 5. trace-requirements.md
**Purpose:** Requirements traceability template
**Sections:** Traceability matrix, coverage analysis, gaps

---

## UX Tools (3 Total)

**Location:** `scripts/`

### 1. bmad-wizard.py
**Purpose:** Interactive command selector
**Lines:** 650
**Features:**
- Menu-driven command selection
- Subagent routing
- Parameter collection
- Command generation

**Usage:**
```bash
python scripts/bmad-wizard.py
```

### 2. progress-visualizer.py
**Purpose:** Real-time progress tracking
**Lines:** 402
**Features:**
- Workflow progress visualization
- Phase completion tracking
- ETA calculation
- Live updates

**Usage:**
```bash
python scripts/progress-visualizer.py --workflow-id workflow-001
```

### 3. error-handler.py
**Purpose:** Improved error messages with remediation
**Lines:** 498
**Features:**
- Error classification
- Root cause analysis
- Remediation suggestions
- User-friendly messages

**Usage:**
```bash
python scripts/error-handler.py --error-log <log-file>
```

---

## Component Relationships

### Dependency Graph

```
Orchestrator V2
    ├── Alex Planner V2
    │   ├── estimate-stories
    │   ├── create-task-spec
    │   ├── breakdown-epic
    │   ├── refine-story
    │   └── sprint-plan
    │       └── bmad-commands (read_file, parse_command)
    │
    ├── James Developer V2
    │   ├── implement-feature
    │   ├── implement-v2
    │   ├── fix-issue
    │   ├── apply-qa-fixes
    │   └── run-tests
    │       └── bmad-commands (read_file, run_tests, framework_registry, adapters)
    │
    ├── Quinn Quality V2
    │   ├── review-task
    │   ├── quality-gate
    │   ├── nfr-assess
    │   ├── trace-requirements
    │   └── risk-profile
    │       └── bmad-commands (read_file, validate_metrics)
    │
    └── Winston Architect
        ├── analyze-architecture
        ├── create-architecture
        ├── validate-architecture
        ├── architecture-review
        └── compare-architectures
            └── bmad-commands (analyze_tech_stack, extract_tech_stack,
                              extract_adrs, validate_patterns,
                              generate_architecture_diagram)
```

### Workflow Composition

```
Feature Delivery Workflow (Orchestrator)
    │
    ├── Phase 1: Planning (Alex)
    │   └── create-task-spec skill
    │       └── read_file, parse_command primitives
    │
    ├── Phase 2: Implementation (James)
    │   └── implement-feature skill
    │       └── read_file, run_tests primitives
    │
    ├── Phase 3: Review (Quinn)
    │   └── review-task skill
    │       └── read_file, validate_metrics primitives
    │
    └── Phase 4: PR Creation (Orchestrator)
        └── Git integration
```

### Skill Reusability Matrix

| Skill | Used By Subagents | Primary | Secondary |
|-------|------------------|---------|-----------|
| estimate-stories | Alex | ✓ | |
| create-task-spec | Alex, Orchestrator | ✓ | ✓ |
| breakdown-epic | Alex | ✓ | |
| implement-feature | James | ✓ | |
| run-tests | James, Quinn | ✓ | ✓ |
| review-task | Quinn | ✓ | |
| analyze-architecture | Winston | ✓ | |
| create-architecture | Winston, Orchestrator | ✓ | ✓ |
| quality-gate | Quinn, Orchestrator | ✓ | ✓ |
| compare-architectures | Winston | ✓ | |

---

## Statistics

### Component Count Summary

| Category | Count |
|----------|-------|
| **Subagents** | 10 (4 core V2, 6 extended) |
| **Skills** | 32 total |
| - Planning Skills | 13 |
| - Development Skills | 5 |
| - Quality Skills | 9 |
| - Brownfield Skills | 1 |
| - Implementation Skills | 1 |
| - Architecture Skills | 3 |
| **Primitive Commands** | 12 |
| **Test Framework Adapters** | 6 |
| **Templates** | 5 |
| **UX Tools** | 3 |
| **Total Components** | 65 |

### Lines of Code

| Component Type | Total Lines |
|---------------|------------|
| Subagent Definitions | 378,965 |
| Skill Workflows | ~10,000 (avg 300 per skill) |
| Primitive Scripts | ~4,000 |
| UX Tools | 1,550 |
| **Total** | **~394,515 lines** |

---

**Document Version:** 2.2
**Last Updated:** 2025-11-05
**Status:** Complete Component Catalog
