# BMAD Enhanced - Example Workflows

This guide provides practical, copy-paste ready examples for common BMAD Enhanced workflows. Each workflow includes step-by-step instructions, expected commands, and sample outputs.

## Table of Contents

1. [Feature Development Workflows](#feature-development-workflows)
   - [Complete Feature Delivery (Orchestrated)](#1-complete-feature-delivery-orchestrated)
   - [Manual Feature Development](#2-manual-feature-development)
   - [TDD Feature Development](#3-tdd-feature-development)
2. [Bug Fixing Workflows](#bug-fixing-workflows)
   - [Simple Bug Fix](#4-simple-bug-fix)
   - [Complex Bug Investigation](#5-complex-bug-investigation)
3. [Quality Improvement Workflows](#quality-improvement-workflows)
   - [Code Quality Improvement](#6-code-quality-improvement)
   - [QA Review Cycle](#7-qa-review-cycle)
4. [Sprint Planning Workflows](#sprint-planning-workflows)
   - [Epic to Sprint Plan](#8-epic-to-sprint-plan)
   - [Sprint Execution](#9-sprint-execution)
5. [Architecture & Refactoring Workflows](#architecture--refactoring-workflows)
   - [Refactoring with Safety](#10-refactoring-with-safety)
   - [Risk Assessment for Major Changes](#11-risk-assessment-for-major-changes)

---

## Feature Development Workflows

### 1. Complete Feature Delivery (Orchestrated)

**Use Case:** Deliver a complete feature from requirement to pull request with full automation.

**When to Use:**
- Starting a new feature with a clear requirement
- Want full automation with minimal manual intervention
- Need coordinated planning, implementation, and review

**Duration:** 30-120 minutes

#### Steps:

```bash
# Run the complete feature delivery workflow
*workflow --type=feature-delivery --requirement="Add user authentication with email and password"
```

#### What Happens:
1. **Planning Phase** (Alex)
   - Creates detailed task specification
   - Analyzes requirements and acceptance criteria
   - Estimates complexity and effort

2. **Implementation Phase** (James)
   - Implements feature following TDD approach
   - Writes tests first, then implementation
   - Runs full test suite

3. **Quality Review Phase** (Quinn)
   - Comprehensive code review
   - NFR assessment (security, performance)
   - Quality gate validation

4. **Finalization**
   - Generates PR description
   - Records telemetry
   - Provides summary report

#### Expected Output:
```
✓ Task specification created: .claude/tasks/task-001-spec.md
✓ Feature implemented: src/auth/authentication.py
✓ Tests created: tests/test_authentication.py
✓ All tests passing (Coverage: 95%)
✓ Quality gate: PASS (Score: 85/100)
✓ Ready for PR submission

Deliverables:
- Task Spec: .claude/tasks/task-001-spec.md
- Implementation: src/auth/authentication.py, src/auth/validators.py
- Tests: tests/test_authentication.py (18 tests)
- Review: .claude/quality/review-20250104-001.md
- Telemetry: .claude/telemetry/workflow-20250104-001.json
```

---

### 2. Manual Feature Development

**Use Case:** Step-by-step feature development with full control over each phase.

**When to Use:**
- Want control over each step
- Need to review between phases
- Learning the BMAD workflow

**Duration:** 30-90 minutes

#### Step 1: Create Task Specification
```bash
*create-task-spec \
  --title="User Authentication" \
  --requirement="Users need to log in with email and password" \
  --context="Using Flask framework, PostgreSQL database"
```

**Output:**
```
✓ Task specification created: .claude/tasks/task-002-spec.md

Specification includes:
- Detailed requirements
- Acceptance criteria (5 items)
- Technical approach
- Test strategy
- Estimated effort: 8 story points
```

#### Step 2: Implement Feature
```bash
*implement \
  --spec=.claude/tasks/task-002-spec.md \
  --tdd=true
```

**Output:**
```
✓ TDD Cycle Complete:
  - Red: 12 tests written (all failing)
  - Green: Implementation complete (all tests passing)
  - Refactor: Code optimized

Files created:
- src/auth/authentication.py
- src/auth/validators.py
- tests/test_authentication.py

Test coverage: 95%
```

#### Step 3: Run Tests
```bash
*test --scope=all --coverage-threshold=80
```

**Output:**
```
✓ All tests passing:
  - Unit tests: 25/25 passing
  - Integration tests: 8/8 passing
  - Coverage: 95% (target: 80%)

No issues found.
```

#### Step 4: Quality Review
```bash
*review --target=src/auth --scope=comprehensive
```

**Output:**
```
✓ Review complete: .claude/quality/review-20250104-002.md

Findings:
- Security: PASS (No vulnerabilities)
- Code Quality: PASS (Complexity < 10)
- Test Coverage: PASS (95%)
- Documentation: CONCERNS (Missing docstrings on 2 functions)

Recommendation: Address minor concerns before merging
```

#### Step 5: Apply QA Fixes
```bash
*apply-qa-fixes --review=.claude/quality/review-20250104-002.md
```

**Output:**
```
✓ QA fixes applied:
  - Added docstrings to authenticate() and validate_password()
  - Updated type hints for consistency

Re-run *review to validate fixes.
```

#### Step 6: Validate Quality Gate
```bash
*validate-quality-gate --target=src/auth --threshold=80
```

**Output:**
```
✓ Quality Gate: PASS

Score: 90/100
- Functionality: 95/100
- Code Quality: 90/100
- Test Coverage: 95/100
- Documentation: 85/100

Approved for merge to main branch.
```

---

### 3. TDD Feature Development

**Use Case:** Strict Test-Driven Development with red-green-refactor cycle.

**Duration:** 30-60 minutes

#### Complete TDD Workflow:
```bash
# Step 1: Create spec
*create-task-spec \
  --title="Password Reset" \
  --requirement="Users can reset forgotten password via email"

# Step 2: Implement with TDD
*implement \
  --spec=.claude/tasks/task-003-spec.md \
  --tdd=true \
  --test-first=true

# Step 3: Refactor if needed
*refactor \
  --target=src/auth/password_reset.py \
  --focus="Extract method, simplify conditionals"

# Step 4: Final test run
*test --scope=unit --coverage-threshold=90
```

**Expected Flow:**
```
TDD Cycle:
1. RED:   Write 8 failing tests for password reset
2. GREEN: Implement minimum code to pass tests
3. REFACTOR: Extract email sending to separate function

✓ All 8 tests passing
✓ Coverage: 98%
✓ Code complexity: 6 (excellent)
```

---

## Bug Fixing Workflows

### 4. Simple Bug Fix

**Use Case:** Fix a well-understood, reproducible bug.

**Duration:** 10-30 minutes

#### Workflow:
```bash
# Fix the bug with root cause analysis
*fix \
  --issue="Login fails when email contains + character" \
  --reproduce-steps="1. Enter email test+user@example.com\n2. Click login\n3. Error: Invalid email" \
  --priority=high
```

**Output:**
```
✓ Bug analysis complete:

Root Cause: Email validation regex doesn't allow + character
Location: src/auth/validators.py:15

Fix Applied:
- Updated email regex pattern to RFC 5322 compliant
- Added test case for + character in email
- All tests passing

Regression Prevention:
- Added 5 new test cases for email edge cases
- Updated validation documentation

Files changed:
- src/auth/validators.py
- tests/test_validators.py
```

#### Verification:
```bash
# Run tests to verify fix
*test --scope=unit --focus=auth

# Create regression test
*test --scope=regression --focus=email-validation
```

---

### 5. Complex Bug Investigation

**Use Case:** Intermittent or complex bug requiring deep investigation.

**Duration:** 15-45 minutes

#### Workflow:
```bash
# Step 1: Deep debugging
*debug \
  --issue="Memory leak in background worker" \
  --logs=logs/worker.log \
  --time-range="2025-01-04 10:00 to 2025-01-04 12:00"
```

**Output:**
```
✓ Debugging analysis:

Symptoms:
- Memory usage increases over 4 hours
- Process killed by OOM
- Occurs during high load

Investigation:
- Log analysis: 150 entries reviewed
- Memory profiling: Large dict accumulation
- No cleanup in event handler

Root Cause:
- Event handlers appending to global cache
- No LRU eviction or size limit
- Cache grows unbounded

Location: src/worker/event_handler.py:45-67
```

#### Step 2: Fix Implementation
```bash
*implement \
  --spec="Fix memory leak by adding LRU cache with max size" \
  --context="Based on debug analysis" \
  --tdd=true
```

#### Step 3: Verify Fix
```bash
# Run extended tests
*test --scope=integration --duration=extended

# Monitor memory usage
*debug \
  --verify-fix=true \
  --monitor="memory" \
  --duration=1h
```

---

## Quality Improvement Workflows

### 6. Code Quality Improvement

**Use Case:** Improve existing code quality and reduce technical debt.

**Duration:** 20-45 minutes

#### Workflow:
```bash
# Step 1: Identify issues
*review --target=src/payment --scope=code-quality

# Step 2: Refactor
*refactor \
  --target=src/payment/processor.py \
  --focus="Reduce complexity, extract methods, improve naming"

# Step 3: Verify improvements
*test --scope=all --coverage-threshold=80

# Step 4: Final review
*review --target=src/payment --scope=code-quality
```

**Before:**
```
Code Quality Issues:
- Cyclomatic complexity: 15 (high)
- Function length: 120 lines (too long)
- Duplication: 3 similar blocks
- Missing docstrings

Score: 55/100
```

**After:**
```
✓ Improvements:
- Complexity reduced: 15 → 6
- Functions extracted: 3 new helper functions
- Duplication eliminated
- Full documentation added

Score: 90/100 (+35 points)
```

---

### 7. QA Review Cycle

**Use Case:** Complete quality assurance review and fix cycle.

**Duration:** 25-50 minutes

#### Complete Cycle:
```bash
# Cycle 1: Initial Review
*review --target=feature/checkout --scope=comprehensive

# Apply fixes
*apply-qa-fixes --review=.claude/quality/review-20250104-003.md

# Cycle 2: Verify Fixes
*review --target=feature/checkout --scope=comprehensive

# Assess NFRs
*assess-nfr \
  --categories="security,performance,reliability" \
  --target=src/checkout

# Final quality gate
*validate-quality-gate --target=feature/checkout --threshold=80
```

**Review Iterations:**
```
Iteration 1:
- 8 issues found
- Score: 68/100
- Decision: CONCERNS

Iteration 2:
- 2 minor issues remaining
- Score: 85/100
- Decision: PASS

✓ Ready for production
```

---

## Sprint Planning Workflows

### 8. Epic to Sprint Plan

**Use Case:** Break down epic into sprint-ready stories with estimates.

**Duration:** 30-60 minutes

#### Complete Planning Workflow:
```bash
# Step 1: Break down epic
*breakdown-epic \
  --epic="E-commerce Checkout System" \
  --target-size=3-5 \
  --context="Payment gateway integration, shipping, tax calculation"
```

**Output:**
```
✓ Epic broken down into 8 user stories:

1. Shopping cart management (3 pts)
2. Shipping address collection (2 pts)
3. Payment method selection (3 pts)
4. Tax calculation (5 pts)
5. Order summary display (2 pts)
6. Payment processing (5 pts)
7. Order confirmation (3 pts)
8. Email notifications (3 pts)

Total: 26 story points
```

#### Step 2: Estimate Each Story
```bash
*estimate \
  --story=.claude/planning/stories/story-001-cart.md \
  --context="React frontend, REST API backend"

*estimate \
  --story=.claude/planning/stories/story-002-address.md \
  --context="Address validation, Google Maps API"

# ... repeat for all stories
```

#### Step 3: Create Sprint Plan
```bash
*plan-sprint \
  --stories=.claude/planning/stories/story-*.md \
  --capacity=40 \
  --sprint-length=2-weeks \
  --team-size=3
```

**Output:**
```
✓ Sprint plan created: .claude/planning/sprint-01-plan.md

Sprint 1 (40 points capacity):
- Week 1: Stories 1-4 (15 pts) - Foundation
- Week 2: Stories 5-8 (11 pts) - Integration & Testing
- Buffer: 14 pts for bugs/blockers

Allocation:
- Developer A: Stories 1, 4 (13 pts)
- Developer B: Stories 2, 3, 5 (10 pts)
- Developer C: Stories 6, 7, 8 (17 pts)

Dependencies:
- Story 6 depends on Stories 2, 3
- Story 7 depends on Story 6
```

---

### 9. Sprint Execution

**Use Case:** Execute complete sprint with automated coordination.

**Duration:** 2 weeks (automated checkpoints)

#### Orchestrated Sprint:
```bash
*workflow \
  --type=sprint-execution \
  --plan=.claude/planning/sprint-01-plan.md \
  --team-size=3 \
  --daily-standups=true
```

**Daily Progress:**
```
Day 1:
✓ Story 1: In Progress (Developer A)
✓ Story 2: In Progress (Developer B)
✓ Story 3: Ready (Developer C)

Day 3:
✓ Story 1: Completed (Tests passing, reviewed)
✓ Story 2: Completed
✓ Story 3: In Progress
✓ Story 4: Started

Day 10 (End of Sprint):
✓ All stories completed: 8/8
✓ Total points: 26/40 (65% capacity used)
✓ Quality gate: PASS
✓ 12 bugs fixed
✓ 95% test coverage maintained

Sprint retrospective generated.
```

---

## Architecture & Refactoring Workflows

### 10. Refactoring with Safety

**Use Case:** Refactor code while ensuring behavior preservation.

**Duration:** 20-45 minutes

#### Safe Refactoring Process:
```bash
# Step 1: Establish baseline
*test --scope=all --record-baseline=true

# Step 2: Review code for issues
*review --target=src/legacy --scope=code-quality

# Step 3: Refactor
*refactor \
  --target=src/legacy/processor.py \
  --focus="Extract class, simplify conditionals, remove duplication" \
  --preserve-behavior=true

# Step 4: Verify behavior preservation
*test --scope=all --compare-baseline=true

# Step 5: Final review
*review --target=src/legacy --scope=code-quality
```

**Refactoring Report:**
```
✓ Refactoring complete:

Changes:
- Extracted PaymentProcessor class
- Simplified 15 conditional branches
- Removed 45 lines of duplication
- Improved naming consistency

Behavior Verification:
- All 87 tests passing (same as baseline)
- No performance regression
- API contract unchanged

Code Quality:
- Complexity: 18 → 7
- Maintainability: 45 → 85
- Duplication: 12% → 0%
```

---

### 11. Risk Assessment for Major Changes

**Use Case:** Assess risks before implementing major architectural changes.

**Duration:** 15-30 minutes

#### Risk Assessment Workflow:
```bash
# Step 1: Assess overall risk
*assess-risk \
  --change="Migrate from monolith to microservices" \
  --scope=architecture \
  --impact=high
```

**Risk Assessment Report:**
```
✓ Risk assessment complete:

Identified Risks (8 total):

HIGH RISK (P×I > 12):
1. Data consistency (P:4, I:5) = 20
   - Impact: Multiple services accessing same data
   - Mitigation: Implement distributed transactions, event sourcing

2. Service discovery (P:3, I:4) = 12
   - Impact: Services can't find each other
   - Mitigation: Use service mesh (Istio), health checks

MEDIUM RISK (P×I: 6-12):
3. Deployment complexity (P:4, I:3) = 12
4. Testing complexity (P:3, I:3) = 9
5. Monitoring overhead (P:3, I:3) = 9

LOW RISK (P×I < 6):
6. Team learning curve (P:2, I:2) = 4
7. Tool costs (P:2, I:2) = 4
8. Documentation needs (P:2, I:1) = 2

Overall Risk Score: 72/100 (HIGH)
```

#### Step 2: Create Mitigation Plan
```bash
*create-task-spec \
  --title="Microservices Migration - Phase 1" \
  --requirement="Mitigate high-risk items before starting migration" \
  --context="Based on risk assessment"
```

#### Step 3: Implement with Risk Monitoring
```bash
*coordinate \
  --pattern=sequential \
  --tasks="implement-event-sourcing,setup-service-mesh,test-distributed-transactions" \
  --risk-monitoring=true
```

---

## Tips for Effective Workflow Usage

### 1. Choose the Right Workflow
- **Simple tasks** (< 30 min): Use individual commands (*implement, *fix, *test)
- **Medium tasks** (30-60 min): Use *coordinate for multi-step operations
- **Complex tasks** (> 60 min): Use *workflow for full automation

### 2. Leverage Complexity Assessment
```bash
# Check complexity before starting
*create-task-spec --title="Your Task" --estimate-only=true

# If complexity > 70:
#   → Break down with *breakdown-epic
#   → Plan carefully with *plan-sprint
```

### 3. Always Run Quality Checks
```bash
# After any implementation:
*test --scope=all
*review --target=changed-files
*validate-quality-gate --threshold=80
```

### 4. Monitor Progress
```bash
# For long-running operations, use progress tracking:
*workflow --type=feature-delivery --show-progress=true
```

### 5. Handle Errors Gracefully
```bash
# If errors occur:
*debug --issue="Error description" --logs=path/to/log

# Review error messages for:
# - Remediation steps
# - Documentation links
# - Related issues
```

---

## Cheat Sheet

### Quick Command Reference

**Planning:**
```bash
*create-task-spec --title="..." --requirement="..."
*breakdown-epic --epic="..."
*plan-sprint --stories="..." --capacity=40
```

**Development:**
```bash
*implement --spec=... --tdd=true
*fix --issue="..." --reproduce-steps="..."
*test --scope=all --coverage-threshold=80
*refactor --target=... --focus="..."
```

**Quality:**
```bash
*review --target=... --scope=comprehensive
*assess-nfr --categories="security,performance" --target=...
*validate-quality-gate --target=... --threshold=80
```

**Orchestration:**
```bash
*workflow --type=feature-delivery --requirement="..."
*coordinate --pattern=sequential --tasks="task1,task2,task3"
```

---

## Getting Help

- **Interactive Wizard:** `python .claude/skills/bmad-commands/scripts/bmad-wizard.py`
- **Command Help:** Use `--help` flag with any command
- **Documentation:** `docs/DOCUMENTATION-INDEX.md`
- **Quick Starts:** `docs/quickstart-*.md`

---

## Related Documentation

- [V2 Architecture](./V2-ARCHITECTURE.md) - System architecture and design
- [Quick Start Guides](./DOCUMENTATION-INDEX.md#quick-start-guides) - Subagent-specific guides
- [Production Deployment](./PRODUCTION-DEPLOYMENT-GUIDE.md) - Production setup
- [Documentation Index](./DOCUMENTATION-INDEX.md) - Complete documentation map

---

**Last Updated:** 2025-01-04
**Version:** V2.0
**Status:** Production Ready
