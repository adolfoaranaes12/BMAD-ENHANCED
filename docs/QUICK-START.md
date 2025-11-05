# BMAD Enhanced - Quick Start Guide

**Get started with BMAD Enhanced in 10 minutes**

Welcome to BMAD Enhanced, the AI-powered system for creating and maintaining software products with massive efficiency gains through intelligent agent coordination.

---

## What is BMAD Enhanced?

BMAD Enhanced is a Claude Code native AI agent system that transforms hours of manual development work into minutes of AI-assisted productivity. It provides:

- **5 Specialized Agents:** Planning, Development, Quality, Architecture, Orchestration
- **31 Skills:** Reusable capabilities across planning, development, quality, and architecture domains
- **10 Primitives:** Atomic, testable operations for deterministic workflows
- **85-90% Time Savings:** From requirement to production in minutes, not hours

---

## Prerequisites

**Required:**
- Claude Code CLI installed
- Git repository (for version control)
- Programming environment (Node.js, Python, Java, C++, Rust, or Go)

**Recommended:**
- Test framework installed (Jest, Pytest, JUnit, GTest, Cargo, Go test)
- IDE or text editor

---

## Installation

### 1. Clone BMAD Enhanced

```bash
git clone <your-bmad-enhanced-repo>
cd bmad-enhanced
```

### 2. Verify Structure

```bash
ls -la .claude/
```

You should see:
```
.claude/
├── agents/         # 5 core + 5 persona subagents
├── commands/       # 9 slash commands
└── skills/         # 31 skills organized by domain
```

### 3. Configuration (Optional)

Create `.claude/config.yaml` if you want custom settings:

```yaml
# Basic Configuration
workspaceRoot: "./workspace"
testFramework: "auto-detect"  # or "jest", "pytest", "junit", etc.
coverageThreshold: 80

# Quality Standards
quality:
  min_coverage: 80
  max_complexity: 10

# Development Settings
development:
  tdd_required: true
  max_files_simple: 5
```

---

## Core Concepts

### The Team: 5 Core Agents

**1. Alex (Planner)** - Planning & Requirements
```bash
@alex *create-task-spec "User login feature"
```

**2. James (Developer)** - Implementation with TDD
```bash
@james *implement task-auth-001
```

**3. Quinn (Quality)** - Quality Assurance & Review
```bash
@quinn *review task-auth-001
```

**4. Winston (Architect)** - System Architecture & Design
```bash
@winston *analyze-architecture .
```

**5. Orchestrator** - Workflow Coordination
```bash
@orchestrator *workflow feature-delivery "User authentication"
```

### The Architecture: 3 Layers

```
Layer 3: Subagents (Coordination) → Routes to appropriate skills
Layer 2: Skills (Workflows) → Implements multi-step processes
Layer 1: Primitives (Commands) → Atomic, testable operations
```

---

## Your First Task: Complete Feature Delivery

Let's build a complete feature from scratch in **10 minutes**.

### Option A: Fully Automated (Fastest)

```bash
# One command for complete feature delivery
@orchestrator *workflow feature-delivery "Add logout button to user dashboard"
```

**What Happens:**
1. Alex creates detailed task specification
2. James implements with Test-Driven Development
3. Quinn performs quality review
4. Orchestrator creates pull request

**Time:** 10-15 minutes
**Output:** Production-ready feature with tests and PR

---

### Option B: Step-by-Step (Learning Mode)

#### Step 1: Plan (2 minutes)

```bash
@alex *create-task-spec "Add logout button to user dashboard"
```

**Output:**
```
✓ Task specification created: .claude/tasks/task-ui-001.md

Includes:
- Detailed requirements
- Acceptance criteria (4 items)
- Technical approach
- Test strategy
```

#### Step 2: Implement (5 minutes)

```bash
@james *implement task-ui-001
```

**Output:**
```
✓ TDD Cycle Complete:
  - Tests written first (RED)
  - Implementation completed (GREEN)
  - Code refactored (REFACTOR)

Files created:
- src/components/LogoutButton.tsx
- src/components/__tests__/LogoutButton.test.tsx

Test coverage: 95%
All tests passing ✓
```

#### Step 3: Review (2 minutes)

```bash
@quinn *review task-ui-001
```

**Output:**
```
✓ Quality Review Complete

Quality Score: 88/100
- Functionality: ✓ PASS
- Code Quality: ✓ PASS
- Test Coverage: ✓ PASS (95%)
- Security: ✓ PASS

Gate Decision: PASS
Ready for production ✓
```

#### Step 4: Done!

Your feature is complete with:
- Working code
- Comprehensive tests (95% coverage)
- Quality validation
- Documentation

---

## Common Commands Cheat Sheet

### Planning Commands (Alex)

```bash
# Create task specification
@alex *create-task-spec "Feature description"

# Break epic into stories
@alex *breakdown-epic "Epic: User Authentication System"

# Estimate story points
@alex *estimate story-auth-001

# Refine vague requirements
@alex *refine-story "Users need better security"

# Create sprint plan
@alex *plan-sprint --velocity 40
```

### Development Commands (James)

```bash
# Implement feature with TDD
@james *implement task-001

# Fix bug systematically
@james *fix bug-login-error

# Run tests (auto-detects framework)
@james *test task-001

# Refactor code safely
@james *refactor task-001

# Apply QA fixes
@james *apply-qa-fixes task-001

# Debug issues
@james *debug "Login tests failing"

# Explain code
@james *explain src/auth/login.ts
```

### Quality Commands (Quinn)

```bash
# Comprehensive quality review
@quinn *review task-001

# Assess non-functional requirements
@quinn *assess-nfr task-001

# Quality gate decision
@quinn *validate-quality-gate task-001

# Requirements traceability
@quinn *trace-requirements task-001

# Risk assessment (P×I methodology)
@quinn *assess-risk task-001
```

### Architecture Commands (Winston)

```bash
# Analyze existing codebase
@winston *analyze-architecture .

# Design system architecture
@winston *create-architecture requirements.md

# Review architecture quality
@winston *review-architecture docs/architecture.md

# Compare architecture options
@winston *compare-architectures "Scale to 50K users"

# Interactive consultation
/winston-consult "How do I add real-time features?"
```

### Orchestration Commands

```bash
# Complete feature delivery
@orchestrator *workflow feature-delivery "Feature description"

# Epic to sprint planning
@orchestrator *workflow epic-to-sprint "Epic name" --velocity 40

# Sprint execution
@orchestrator *workflow sprint-execution "Sprint 15"

# Brownfield modernization
@orchestrator *workflow modernize . "Your goals"

# Cross-subagent coordination
@orchestrator *coordinate "Task" --subagents alex,james
```

---

## Common Workflows

### Workflow 1: Build New Feature

```bash
# Automated (10-15 min)
@orchestrator *workflow feature-delivery "User profile page"

# OR Manual (15-20 min)
@alex *create-task-spec "User profile page"
@james *implement task-profile-001
@quinn *review task-profile-001
```

### Workflow 2: Fix Bug

```bash
# Simple fix (5-10 min)
@james *fix bug-login-timeout

# Complex investigation (15-30 min)
@james *debug "Memory leak in worker process"
@james *implement task-fix-001
@quinn *review task-fix-001
```

### Workflow 3: Quality Improvement

```bash
# Review and improve (20-30 min)
@quinn *review src/payment/
@james *apply-qa-fixes task-payment-001
@james *refactor task-payment-001
@quinn *review task-payment-001
```

### Workflow 4: Architecture Analysis

```bash
# Analyze existing system (10-15 min)
@winston *analyze-architecture .

# Get recommendations (5-10 min)
/winston-consult "How do I scale to 100K users?"

# Design improvements (20-30 min)
@winston *compare-architectures "Add real-time + scale to 50K"
```

### Workflow 5: Sprint Planning

```bash
# Epic to sprint (30-45 min)
@orchestrator *workflow epic-to-sprint "Shopping Cart" --velocity 40
```

---

## Framework Support 🌍

BMAD Enhanced works with **ANY test framework** through auto-detection:

**Auto-Detected Frameworks:**
- ✅ **JavaScript/TypeScript:** Jest
- ✅ **Python:** Pytest
- ✅ **Java/Kotlin:** JUnit (Maven/Gradle)
- ✅ **C/C++:** Google Test (CMake/CTest)
- ✅ **Rust:** Cargo test
- ✅ **Go:** Go test

**Examples:**

```bash
# Auto-detection (recommended)
@james *implement task-001  # Detects your framework

# Explicit framework
@james *test task-001 --framework pytest
@james *implement task-api --framework junit
```

**Add Custom Framework:** See [Framework Extension Guide](../.claude/skills/bmad-commands/FRAMEWORK-EXTENSION-GUIDE.md)

---

## Next Steps

### Learn More About Each Agent

- **[Alex (Planner) Guide](./quickstart-alex.md)** - Planning workflows
- **[James (Developer) Guide](./quickstart-james.md)** - TDD implementation
- **[Quinn (Quality) Guide](./quickstart-quinn.md)** - Quality assurance
- **[Winston (Architect) Guide](./quickstart-winston.md)** - Architecture design
- **[Orchestrator Guide](./quickstart-orchestrator.md)** - Workflow automation

### Explore Advanced Topics

- **[User Guide](./USER-GUIDE.md)** - Comprehensive 15-20 page guide
- **[Workflow Guide](./WORKFLOW-GUIDE.md)** - 10-15 detailed scenarios
- **[Agent Reference](./AGENT-REFERENCE.md)** - Complete command reference
- **[Best Practices](./BEST-PRACTICES.md)** - Recommended patterns

### Understand the Architecture

- **[V2 Architecture](./V2-ARCHITECTURE.md)** - System design
- **[3-Layer Architecture](./3-layer-architecture-for-skills.md)** - How skills work
- **[Documentation Index](./DOCUMENTATION-INDEX.md)** - Complete documentation

---

## Troubleshooting

### "Command not found"

**Solution:** Ensure you're using the correct agent prefix:
```bash
# Correct
@alex *create-task-spec "Feature"
@james *implement task-001

# Incorrect
alex *create-task-spec  # Missing @
@alex create-task-spec  # Missing *
```

### "Task specification required"

**Solution:** Create task spec first:
```bash
@alex *create-task-spec "Your feature description"
@james *implement task-generated-id
```

### "Tests failing"

**Solution:** Use debug command:
```bash
@james *debug "Test failure description"
@james *test task-001  # Re-run tests
```

### "Complexity too high"

**Solution:** Break down the task:
```bash
@alex *breakdown-epic "Large feature"
# Then implement each smaller task
```

---

## Tips for Success

### ✅ Do's

- **Start with orchestrator** for complete workflows
- **Let complexity assessment work** - trust the routing
- **Run tests frequently** - after every significant change
- **Use step-by-step mode** when learning
- **Review quality gates** - address concerns promptly
- **Trust TDD** - tests first, implementation second

### ❌ Don'ts

- **Don't skip planning** - always start with task specs
- **Don't ignore quality gates** - they prevent technical debt
- **Don't bypass tests** - 80% coverage minimum
- **Don't commit failing tests** - always keep tests green
- **Don't over-engineer** - keep scope focused

---

## Get Help

- **Interactive Wizard:** Run `python scripts/bmad-wizard.py`
- **Documentation:** Browse `docs/` directory
- **Examples:** See `docs/WORKFLOW-GUIDE.md` for detailed scenarios
- **Architecture:** Read `docs/V2-ARCHITECTURE.md` for system design

---

## Summary

You've learned:
- ✅ What BMAD Enhanced is and why it's valuable
- ✅ How to install and configure the system
- ✅ The 5 core agents and their roles
- ✅ How to build your first feature (10 minutes)
- ✅ Common commands and workflows
- ✅ Where to find more information

**Ready to go?** Start with:
```bash
@orchestrator *workflow feature-delivery "Your first feature"
```

---

**Welcome to BMAD Enhanced - Where AI meets AGILE!** 🚀

**Version:** 2.0
**Status:** Production Ready
**Time to Value:** 10 minutes
