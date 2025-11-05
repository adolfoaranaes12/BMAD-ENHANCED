# James (Developer) Quick Start Guide

**Subagent:** james-developer-v2
**Role:** Implementation Specialist with TDD
**Commands:** 7
**Version:** 2.0

---

## Overview

**James** is your intelligent development assistant that transforms requirements into working, tested code using Test-Driven Development with complexity-based routing and comprehensive safety guardrails.

### What James Does

- ✅ Implements features with TDD workflow
- ✅ Fixes bugs systematically with root cause analysis
- ✅ Executes tests with coverage analysis
- ✅ Refactors code safely with test validation
- ✅ Applies QA fixes from quality gates
- ✅ Debugs issues using hypothesis-driven investigation
- ✅ Explains code and generates documentation

### V2 Features

- **Intelligent Routing:** Automatically selects implementation strategy (simple/standard/complex)
- **Complexity Assessment:** 0-100 scale using 5 weighted factors per command
- **Guardrails:** Prevents excessive changes and enforces quality standards
- **Full Telemetry:** Every operation tracked and observable
- **TDD Workflow:** Test-first development enforced

---

## Commands

### 1. `*implement` - Implement Features 🌍 Framework-Agnostic

**Purpose:** Implement features using Test-Driven Development with intelligent routing

**Syntax:**
```bash
@james *implement <task-id>
@james *implement task-auth-002
@james *implement task-payment-001
```

**🌍 NEW: Works with ANY test framework!**
```bash
# Auto-detects your test framework
@james *implement task-login-001      # Jest, Pytest, JUnit, GTest, Cargo, Go
@james *implement task-api-001        # Tests written in your framework
```

**Examples:**
```bash
# TypeScript/Next.js project (auto-detects Jest)
@james *implement task-login-001

# Python/Flask project (auto-detects Pytest)
@james *implement task-api-auth

# Java/Spring project (auto-detects JUnit)
@james *implement task-checkout-flow

# C++ project (auto-detects Google Test)
@james *implement task-sorting-algorithm

# Rust project (auto-detects Cargo test)
@james *implement task-http-server

# Go project (auto-detects Go test)
@james *implement task-grpc-service
```

**What You Get:**
- Working, tested implementation (in YOUR framework)
- Test suite with 80%+ coverage
- Code following TDD (tests written first)
- Acceptance criteria verified
- Telemetry and execution log

**Complexity Factors:**
- Files affected (30%)
- Database changes (25%)
- API changes (20%)
- Dependencies (15%)
- Test complexity (10%)

**When to Use:**
- Implementing features from task specifications
- Building new functionality
- After Alex creates task spec

**Framework Support:**
See [Framework Extension Guide](../.claude/skills/bmad-commands/FRAMEWORK-EXTENSION-GUIDE.md) to add custom frameworks

---

### 2. `*fix` - Fix Bugs

**Purpose:** Fix bugs systematically through reproduction, root cause analysis, and validated fixes

**Syntax:**
```bash
@james *fix <issue-id>
@james *fix bug-login-email
@james *fix issue-42
```

**Examples:**
```bash
@james *fix bug-auth-timeout
@james *fix issue-checkout-error
@james *fix bug-payment-validation
```

**What You Get:**
- Bug fixed with test coverage
- Root cause analysis documented
- Regression test added
- Fix verified against acceptance criteria
- Related code reviewed for similar issues

**Complexity Factors:**
- Affected components (30%)
- Reproduction difficulty (25%)
- Root cause clarity (20%)
- Test coverage exists (15%)
- Impact scope (10%)

**When to Use:**
- Fixing reported bugs
- Addressing test failures
- Resolving production issues

---

### 3. `*test` - Execute Tests 🌍 Framework-Agnostic

**Purpose:** Execute tests with coverage analysis, identify gaps, and suggest missing tests

**Syntax:**
```bash
@james *test <scope>
@james *test task-auth-002
@james *test src/auth/login.ts
@james *test --all
```

**🌍 NEW: Auto-detects test framework!**
```bash
@james *test task-login-001  # Auto-detects: Jest, Pytest, JUnit, GTest, Cargo, Go
```

**Examples:**
```bash
# Auto-detection (recommended)
@james *test task-login-001       # Detects Jest (JS/TS)
@james *test task-api-001         # Detects Pytest (Python)
@james *test task-service-001     # Detects JUnit (Java)
@james *test task-algorithm-001   # Detects GTest (C++)

# Explicit framework
@james *test task-auth-001 --framework pytest
@james *test task-checkout --framework junit
```

**Supported Frameworks:**
- ✅ **JavaScript/TypeScript:** Jest (auto-detected)
- ✅ **Python:** Pytest (auto-detected)
- ✅ **Java/Kotlin:** JUnit with Maven/Gradle
- ✅ **C/C++:** Google Test with CMake/CTest
- ✅ **Rust:** Cargo test
- ✅ **Go:** Go test
- ✅ **Custom:** Add your own in `.claude/config.yaml`

**What You Get:**
- Test execution results (all frameworks)
- Coverage report with gaps identified
- Missing test suggestions
- Performance metrics
- Failed test details with debugging hints

**Scope Types:**
- **Task-based:** Run tests for specific task
- **File-based:** Run tests for specific file
- **Pattern-based:** Run tests matching pattern
- **All tests:** Run entire test suite

**When to Use:**
- After implementing features
- Before committing code
- During debugging

**Learn More:**
- 📖 [Framework Extension Guide](../.claude/skills/bmad-commands/FRAMEWORK-EXTENSION-GUIDE.md)
- 🏗️ [Adapter Architecture](../.claude/skills/bmad-commands/FRAMEWORK-ADAPTER-ARCHITECTURE.md)
- For coverage analysis

---

### 4. `*refactor` - Refactor Code

**Purpose:** Safely improve code quality through incremental refactoring with test validation

**Syntax:**
```bash
@james *refactor <task-id> [--scope <conservative|moderate|aggressive>]
@james *refactor task-auth-002
@james *refactor task-auth-002 --scope conservative
```

**Examples:**
```bash
@james *refactor task-login-001
@james *refactor task-payment-001 --scope moderate
@james *refactor task-api-endpoints --scope conservative
```

**What You Get:**
- Improved code quality
- Technical debt reduced
- Code smells eliminated
- All tests still passing
- Quality metrics improved

**Complexity Factors:**
- Files to refactor (30%)
- Quality issues (25%)
- Technical debt (20%)
- Test coverage (15%)
- Code complexity (10%)

**Refactoring Scopes:**
- **Conservative:** Minimal changes, very safe
- **Moderate:** Standard improvements (default)
- **Aggressive:** Extensive refactoring, requires approval

**When to Use:**
- After Quinn identifies quality issues
- When technical debt accumulates
- Before major feature work
- During code cleanup sprints

---

### 5. `*apply-qa-fixes` - Apply QA Fixes

**Purpose:** Systematically apply fixes from Quinn's quality gate assessment

**Syntax:**
```bash
@james *apply-qa-fixes <task-id>
@james *apply-qa-fixes task-001 --scope high_severity
```

**Examples:**
```bash
@james *apply-qa-fixes task-login-001
@james *apply-qa-fixes task-payment-001 --scope high_severity
@james *apply-qa-fixes task-api-001
```

**What You Get:**
- Quality issues fixed systematically
- High severity issues addressed first
- NFR failures resolved
- Coverage gaps filled
- Updated quality gate (re-run Quinn)

**Complexity Scoring:**
- High severity issues: 20 points each
- NFR failures: 15 points each
- Coverage gaps (P0): 10 points each
- NFR concerns: 5 points each
- Medium severity: 3 points each

**When to Use:**
- After Quinn's quality gate shows FAIL or CONCERNS
- When Quinn identifies critical issues
- Before final deployment
- As part of quality improvement workflow

---

### 6. `*debug` - Debug Issues

**Purpose:** Systematically debug failing tests or runtime issues using hypothesis-driven investigation

**Syntax:**
```bash
@james *debug <issue-description>
@james *debug "Tests failing in UserService.authenticate()"
@james *debug --error-log logs/error.log
```

**Examples:**
```bash
@james *debug "Login tests failing intermittently"
@james *debug "Payment API returns 500 error"
@james *debug --error-log logs/production-error.log
```

**What You Get:**
- Root cause identified
- Hypothesis-driven investigation documented
- Fix implemented and tested
- Debugging steps logged
- Prevention recommendations

**Complexity Factors:**
- Error clarity (30%)
- Reproduction (25%)
- System complexity (20%)
- Logs available (15%)
- Impact (10%)

**When to Use:**
- Tests failing unexpectedly
- Runtime errors occurring
- Intermittent issues
- Production problems need investigation

---

### 7. `*explain` - Explain Code

**Purpose:** Explain code functionality, generate documentation, and create learning materials

**Syntax:**
```bash
@james *explain <file-or-pattern>
@james *explain src/authentication/oauth.py
@james *explain "How does the caching system work?"
@james *explain src/api/** --audience technical --format markdown
```

**Examples:**
```bash
@james *explain src/auth/login.ts
@james *explain "How does authentication work?"
@james *explain src/payment/** --audience non-technical
```

**What You Get:**
- Clear code explanation
- Documentation generated
- Architecture context
- Usage examples
- Learning materials tailored to audience

**Complexity Factors:**
- Code complexity (30%)
- Documentation needs (25%)
- Audience (20%)
- Scope (15%)
- Examples needed (10%)

**Audiences:**
- **Technical expert:** Brief, assumes deep knowledge
- **Developer:** Standard detail with examples
- **Non-technical:** Plain language, concepts explained
- **Beginner:** Tutorial style with interactive examples

**When to Use:**
- Onboarding new developers
- Documenting complex systems
- Creating learning materials
- Understanding unfamiliar code

---

## Common Workflows

### Workflow 1: Implement a New Feature

**Goal:** From task spec to working, tested code

```bash
# Step 1: Implement feature with TDD
@james *implement task-login-001
# Output: Working implementation with tests

# Step 2: Run full test suite
@james *test --all
# Output: All tests passing, 85% coverage

# Step 3: Ready for Quinn to review
@quinn *review task-login-001
```

**Duration:** 20-60 minutes depending on complexity
**Output:** Production-ready feature with tests

---

### Workflow 2: Fix a Bug

**Goal:** From bug report to verified fix

```bash
# Step 1: Fix bug systematically
@james *fix bug-checkout-error
# Output: Bug fixed with regression test

# Step 2: Run tests to verify
@james *test src/checkout/**
# Output: All tests passing, bug verified fixed

# Step 3: Review for quality
@quinn *review bug-checkout-error
```

**Duration:** 15-45 minutes depending on complexity
**Output:** Bug fixed with test coverage

---

### Workflow 3: Quality Improvement Cycle

**Goal:** From quality concerns to improved code

```bash
# Step 1: Quinn identifies issues
@quinn *review task-payment-001
# Output: Quality gate CONCERNS - 5 issues found

# Step 2: Apply QA fixes
@james *apply-qa-fixes task-payment-001
# Output: Issues resolved

# Step 3: Refactor if needed
@james *refactor task-payment-001 --scope moderate
# Output: Code quality improved

# Step 4: Re-review
@quinn *review task-payment-001
# Output: Quality gate PASS
```

**Duration:** 30-90 minutes depending on issues
**Output:** High-quality, well-tested code

---

### Workflow 4: TDD Red-Green-Refactor

**Goal:** Full TDD cycle for new feature

```bash
# Step 1: Implement with TDD (Red → Green)
@james *implement task-new-feature
# Output: Tests written first, implementation follows

# Step 2: Verify tests pass
@james *test task-new-feature
# Output: All tests green

# Step 3: Refactor (if quality issues)
@james *refactor task-new-feature --scope conservative
# Output: Clean, maintainable code

# Step 4: Final verification
@james *test --all
# Output: Full suite passing
```

**Duration:** 30-90 minutes
**Output:** Clean, well-tested feature

---

## TDD Workflow Explained

James enforces **Test-Driven Development** in the *implement command:

### TDD Steps

1. **Red:** Write failing test first
   - Test describes expected behavior
   - Run test → it fails (no implementation yet)

2. **Green:** Write minimal code to pass
   - Implement just enough to make test pass
   - Run test → it passes

3. **Refactor:** Improve code quality
   - Clean up implementation
   - Run test → still passes

4. **Repeat:** For each feature/requirement

### Benefits

- ✅ Tests serve as specification
- ✅ Code coverage guaranteed
- ✅ Prevents over-engineering
- ✅ Refactoring is safe
- ✅ Documentation through tests

---

## Guardrails & Safety

James enforces safety guardrails to prevent issues:

### Global Guardrails (All Commands)

- **Max files per change:** 5 (simple), 7 (standard), 10 (complex)
- **Max diff lines:** 400 (simple), 600 (standard), 1000 (complex)
- **Test coverage:** Minimum 80% required
- **Always run tests:** Before any commit
- **Never commit failing tests:** Tests must pass
- **Block sensitive files:** .env, *.key, credentials.json
- **Require task spec:** No implementation without spec

### Escalation Triggers

- **Complexity > 60:** User confirmation required
- **Breaking changes:** User approval needed
- **Failed tests:** Stop and report
- **Coverage below 80%:** Warning + block commit
- **Guardrail violations:** Stop and report

---

## Tips & Best Practices

### ✅ Do's

- **Always have task spec:** James requires task specifications
- **Trust TDD:** Write tests first, implementation second
- **Start simple:** Let complexity assessment route appropriately
- **Run tests frequently:** After every significant change
- **Apply QA fixes:** Address Quinn's concerns promptly
- **Use debug for investigation:** Hypothesis-driven debugging works

### ❌ Don'ts

- **Don't skip tests:** 80% coverage is minimum
- **Don't commit failing tests:** Always ensure green
- **Don't ignore guardrails:** They prevent technical debt
- **Don't over-engineer:** Keep scope focused
- **Don't bypass QA:** Quality gates exist for good reasons

---

## Complexity Assessment

James calculates complexity differently per command. Here's the *implement assessment:

### 5 Weighted Factors

1. **Files Affected** (30%): 1-2=10, 3-5=30, 6-10=60, 11+=90
2. **Database Changes** (25%): None=0, Existing=20, Schema=50, Migration=90
3. **API Changes** (20%): None=0, Modify=30, New=60, Breaking=90
4. **Dependencies** (15%): None=0, Internal=20, External=50, New services=90
5. **Test Complexity** (10%): Unit only=10, Integration=40, E2E=70, Multiple=90

**Formula:** (files × 0.30) + (db × 0.25) + (api × 0.20) + (deps × 0.15) + (tests × 0.10)

**Routing:**
- **Simple (≤30):** Quick TDD workflow
- **Standard (31-60):** Detailed TDD with planning
- **Complex (>60):** Discovery phase + TDD, user approval required

*Other commands (*fix, *test, *refactor, etc.) use different complexity factors appropriate to their context.*

---

## Configuration

### James Settings

Configure in `.claude/config.yaml`:

```yaml
development:
  tdd_required: true              # Enforce TDD workflow
  min_coverage: 80                # Minimum test coverage %
  max_files_simple: 5             # Max files for simple changes
  max_files_standard: 7           # Max files for standard changes
  max_files_complex: 10           # Max files for complex changes

quality:
  allowRefactoring: true          # Enable *refactor command
  autoApplyQAFixes: false         # Require explicit *apply-qa-fixes

guardrails:
  block_sensitive_files: true     # Block .env, *.key, credentials.json
  require_task_spec: true         # Require task spec for *implement
  never_commit_failing: true      # Block commits with failing tests
```

---

## Troubleshooting

### Issue: "Task Specification Required"

**Solution:** Create task spec first
```bash
# Use Alex to create task spec
@alex *create-task-spec "Your feature description"

# Then implement
@james *implement task-generated-id
```

### Issue: "Complexity Too High - Requires Approval"

**Solution:** Review and confirm, or break down task
```bash
# Option 1: Confirm you want to proceed
# James will prompt for confirmation

# Option 2: Break down into smaller tasks
@alex *breakdown-epic "Your large feature"
# Then implement each smaller task individually
```

### Issue: "Tests Failing - Coverage Below 80%"

**Solution:** Add missing tests
```bash
# Run tests to see gaps
@james *test task-id

# Review coverage report
# Add tests for uncovered code paths

# Re-run tests
@james *test task-id
```

### Issue: "Guardrail Violation - Too Many Files"

**Solution:** Reduce scope or split into multiple tasks
```bash
# Option 1: Review and reduce implementation scope
# Option 2: Split into multiple related tasks
@alex *breakdown-epic "Your large feature"

# Implement each task separately
@james *implement task-part-1
@james *implement task-part-2
```

---

## Next Steps

**After Implementation:**
1. **Quality Review:** Use Quinn to review implemented features
2. **Integration:** Use Orchestrator for cross-team coordination
3. **Architecture Review:** Use Winston for system design validation

**Related Guides:**
- [Alex (Planner) Quick Start](./quickstart-alex.md)
- [Quinn (Quality) Quick Start](./quickstart-quinn.md)
- [Orchestrator Quick Start](./quickstart-orchestrator.md)
- [V2 Architecture](./V2-ARCHITECTURE.md)

---

**Questions?** See [V2 Architecture Documentation](./V2-ARCHITECTURE.md)

**James (Developer) Quick Start Guide**
*Part of BMAD Enhanced V2 Architecture*
