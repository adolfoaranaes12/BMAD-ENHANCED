# Phase 3 Integration Test Plan

**Version:** 1.0
**Created:** 2025-02-03
**Status:** In Progress
**Objective:** Validate V2 architecture through end-to-end integration testing

---

## Executive Summary

This test plan validates that the V2 architecture (4 subagents, 17 skills, 14 commands) works seamlessly end-to-end. We'll test complete workflows, cross-subagent coordination, error recovery, and telemetry capture.

**Success Criteria:**
- ✅ All workflows execute without errors
- ✅ Cross-subagent coordination works smoothly
- ✅ State persistence and resume work correctly
- ✅ Error recovery mechanisms function properly
- ✅ Telemetry captured for all operations

---

## Test Environment

**Prerequisites:**
- BMAD Enhanced V2 architecture installed
- Working directory: `/home/adolfo/Documents/BMAD Enhanced`
- Git repository initialized
- All 4 subagents available (alex, james, quinn, orchestrator)
- All 17 skills with V2 contracts

**Verification Commands:**
```bash
# Verify subagents exist
ls -la .claude/agents/

# Verify skills exist
ls -la .claude/skills/planning/
ls -la .claude/skills/quality/
ls -la .claude/skills/development/

# Verify git status
git status
```

---

## Test Workflows

### Test 1: Feature-Delivery Workflow (End-to-End)

**Objective:** Validate complete feature delivery from planning through quality review

**Workflow Steps:**
```
User Request
    ↓
Orchestrator (*workflow feature-delivery)
    ↓
Phase 1: alex-planner (*create-task-spec)
    ↓
Phase 2: james-developer-v2 (*implement)
    ↓
Phase 3: quinn-quality (*review)
    ↓
Phase 4: Orchestrator (create PR)
    ↓
Complete
```

**Test Scenario:**
- Feature: Simple user authentication with login endpoint
- Input: Product requirement for login functionality
- Expected Output: Complete implementation + quality review + PR

**Test Steps:**

1. **Initiate Workflow**
   ```
   @orchestrator *workflow feature-delivery --feature "User login authentication"
   ```

2. **Verify Phase 1 (Planning - Alex)**
   - [ ] Task specification created
   - [ ] Acceptance criteria defined
   - [ ] Technical approach documented
   - [ ] Complexity assessment performed
   - [ ] Routing decision logged
   - [ ] Telemetry emitted

3. **Verify Phase 2 (Implementation - James)**
   - [ ] TDD workflow followed (tests first)
   - [ ] Implementation completed
   - [ ] Tests passing
   - [ ] Code quality acceptable
   - [ ] Telemetry emitted

4. **Verify Phase 3 (Quality Review - Quinn)**
   - [ ] Review conducted
   - [ ] Issues identified (if any)
   - [ ] Quality score calculated
   - [ ] Recommendations provided
   - [ ] Telemetry emitted

5. **Verify Phase 4 (PR Creation - Orchestrator)**
   - [ ] Branch created
   - [ ] Commits made
   - [ ] PR created with description
   - [ ] Workflow state saved

**Success Criteria:**
- ✅ All phases complete without errors
- ✅ Each subagent emits telemetry
- ✅ Workflow state persisted
- ✅ Final PR created successfully

**Test Results:**
- Status: NOT STARTED
- Execution Time: TBD
- Issues Found: TBD

---

### Test 2: Epic-to-Sprint Workflow

**Objective:** Validate planning workflow from epic breakdown to sprint planning

**Workflow Steps:**
```
User Request (Epic)
    ↓
alex-planner (*breakdown-epic)
    ↓
Stories generated
    ↓
alex-planner (*estimate)
    ↓
Story points assigned
    ↓
alex-planner (*plan-sprint)
    ↓
Sprint plan created
```

**Test Scenario:**
- Epic: E-commerce shopping cart
- Expected Output: 5-8 stories with estimates + sprint plan

**Test Steps:**

1. **Create Epic Document**
   ```markdown
   # Epic: Shopping Cart
   As a customer, I want to add products to a cart and checkout

   Acceptance Criteria:
   - Add items to cart
   - Update quantities
   - Remove items
   - Calculate totals
   - Checkout process
   ```

2. **Test Epic Breakdown**
   ```
   @alex *breakdown-epic docs/epic-shopping-cart.md
   ```
   - [ ] Epic analyzed
   - [ ] 5-8 stories generated
   - [ ] Acceptance criteria per story
   - [ ] Dependencies identified
   - [ ] Complexity assessed
   - [ ] Telemetry emitted

3. **Test Story Estimation**
   ```
   @alex *estimate workspace/stories/
   ```
   - [ ] Each story analyzed
   - [ ] Story points assigned
   - [ ] Justification provided
   - [ ] Risk factors identified
   - [ ] Telemetry emitted

4. **Test Sprint Planning**
   ```
   @alex *plan-sprint --velocity 20 --duration 2-weeks
   ```
   - [ ] Sprint plan created
   - [ ] Stories allocated by priority
   - [ ] Capacity considered
   - [ ] Sprint goals defined
   - [ ] Telemetry emitted

**Success Criteria:**
- ✅ Epic broken into logical stories
- ✅ All stories estimated
- ✅ Sprint plan created within velocity
- ✅ Workflow state persisted
- ✅ All telemetry captured

**Test Results:**
- Status: NOT STARTED
- Execution Time: TBD
- Issues Found: TBD

---

### Test 3: Cross-Subagent Coordination

**Objective:** Validate coordination between Quinn (review) and James (fixes)

**Workflow Steps:**
```
User Request
    ↓
Orchestrator (*coordinate --subagents quinn,james)
    ↓
Iteration 1:
  quinn (*review) → CONCERNS
  james (*apply-qa-fixes) → Fixed
    ↓
Iteration 2:
  quinn (*review) → PASS
    ↓
Complete
```

**Test Scenario:**
- Code with deliberate quality issues
- Expected: Quinn identifies issues, James fixes, Quinn approves

**Test Steps:**

1. **Create Code with Issues**
   ```javascript
   // Deliberately add issues:
   // - Missing error handling
   // - No input validation
   // - Hardcoded values
   // - No tests
   ```

2. **Initiate Coordination**
   ```
   @orchestrator *coordinate --subagents quinn,james --task "Fix quality issues in login.js"
   ```

3. **Verify Iteration 1 (Quinn Review)**
   - [ ] Quinn identifies issues
   - [ ] Severity assigned
   - [ ] Recommendations provided
   - [ ] Status: CONCERNS
   - [ ] Telemetry emitted

4. **Verify Iteration 1 (James Fixes)**
   - [ ] James receives Quinn's feedback
   - [ ] Fixes applied systematically
   - [ ] Tests added
   - [ ] Status: FIXED
   - [ ] Telemetry emitted

5. **Verify Iteration 2 (Quinn Re-Review)**
   - [ ] Quinn re-reviews code
   - [ ] All issues resolved
   - [ ] Status: PASS
   - [ ] Telemetry emitted

6. **Verify Coordination Complete**
   - [ ] Orchestrator confirms completion
   - [ ] Workflow state saved
   - [ ] Final report generated

**Success Criteria:**
- ✅ Quinn identifies quality issues correctly
- ✅ James fixes issues based on feedback
- ✅ Quinn approves after fixes
- ✅ Coordination state persisted
- ✅ All telemetry captured

**Test Results:**
- Status: NOT STARTED
- Execution Time: TBD
- Issues Found: TBD

---

### Test 4: Error Recovery and Resume

**Objective:** Validate error handling and workflow resume capabilities

**Test Scenarios:**

#### Scenario 4A: Workflow Interruption

**Steps:**
1. Start feature-delivery workflow
2. Abort during Phase 2 (implementation)
3. Resume from checkpoint
4. Verify workflow continues from last state

**Test Steps:**
- [ ] Start workflow
- [ ] Abort mid-execution (Ctrl+C)
- [ ] Verify workflow state saved
- [ ] Resume workflow
- [ ] Verify continuation from checkpoint
- [ ] Verify no duplicate operations

**Expected Behavior:**
- Workflow saves state periodically
- Resume picks up from last checkpoint
- No loss of progress

#### Scenario 4B: Command Failure

**Steps:**
1. Trigger a failing command (e.g., tests fail)
2. Verify error captured
3. Test retry mechanism
4. Test skip capability

**Test Steps:**
- [ ] Create failing test
- [ ] Run james *test
- [ ] Verify error captured
- [ ] Verify retry option offered
- [ ] Test retry mechanism
- [ ] Test skip mechanism

**Expected Behavior:**
- Errors logged with context
- Retry option available
- Skip option available
- Telemetry includes error info

#### Scenario 4C: Guardrail Trigger

**Steps:**
1. Trigger a guardrail condition (e.g., high complexity)
2. Verify escalation occurs
3. Verify routing to complex strategy

**Test Steps:**
- [ ] Create high-complexity scenario
- [ ] Verify guardrail triggered
- [ ] Verify escalation logged
- [ ] Verify strategy switched to complex
- [ ] Verify telemetry includes guardrail info

**Success Criteria:**
- ✅ Workflows can be interrupted and resumed
- ✅ Errors handled gracefully
- ✅ Retry mechanism works
- ✅ Skip mechanism works
- ✅ Guardrails trigger correctly
- ✅ All errors logged

**Test Results:**
- Status: NOT STARTED
- Execution Time: TBD
- Issues Found: TBD

---

### Test 5: Workflow State Persistence

**Objective:** Validate workflow state is saved and can be restored

**Test Steps:**

1. **Create Workflow State**
   ```yaml
   workflow_id: test-workflow-001
   workflow_type: feature-delivery
   status: in_progress
   phases:
     - id: planning
       subagent: alex-planner
       status: completed
       output: workspace/tasks/task-001.md
     - id: implementation
       subagent: james-developer-v2
       status: in_progress
       output: src/login.js
   ```

2. **Save State**
   - [ ] Verify state saved to workspace/workflows/
   - [ ] Verify YAML format
   - [ ] Verify all fields present

3. **Load State**
   - [ ] Load saved workflow
   - [ ] Verify all data restored
   - [ ] Verify can continue from checkpoint

4. **Update State**
   - [ ] Progress to next phase
   - [ ] Verify state updated
   - [ ] Verify timestamps correct

**Success Criteria:**
- ✅ State saved in YAML format
- ✅ State can be loaded
- ✅ State accurately reflects progress
- ✅ Timestamps tracked

**Test Results:**
- Status: NOT STARTED
- Execution Time: TBD
- Issues Found: TBD

---

### Test 6: Telemetry Validation

**Objective:** Validate telemetry captured for all operations

**Telemetry Structure:**
```json
{
  "agent": "subagent-name",
  "command": "*command-name",
  "timestamp": "2025-02-03T10:30:00Z",
  "routing": {
    "complexity_score": 45,
    "factors": {
      "factor_1": 50,
      "factor_2": 40,
      "factor_3": 60,
      "factor_4": 30,
      "factor_5": 20
    },
    "strategy_selected": "standard",
    "reason": "..."
  },
  "guardrails": {
    "checked": true,
    "passed": true,
    "triggered": [],
    "escalations": []
  },
  "execution": {
    "duration_ms": 1250,
    "status": "success"
  },
  "acceptance": {
    "criteria_checked": 6,
    "criteria_passed": 6,
    "pass": true
  }
}
```

**Test Steps:**

1. **Run Each Subagent Command**
   - [ ] alex: *create-task-spec
   - [ ] alex: *breakdown-epic
   - [ ] alex: *estimate
   - [ ] alex: *refine-story
   - [ ] alex: *plan-sprint
   - [ ] james: *implement
   - [ ] james: *fix
   - [ ] james: *test
   - [ ] james: *refactor
   - [ ] james: *debug
   - [ ] james: *explain
   - [ ] james: *apply-qa-fixes
   - [ ] quinn: *review
   - [ ] quinn: *assess-nfr
   - [ ] quinn: *validate-quality-gate
   - [ ] quinn: *trace-requirements
   - [ ] quinn: *assess-risk
   - [ ] orchestrator: *workflow
   - [ ] orchestrator: *coordinate

2. **Verify Telemetry Structure**
   - [ ] All required fields present
   - [ ] Routing section complete
   - [ ] Guardrails section complete
   - [ ] Execution metrics captured
   - [ ] Acceptance criteria tracked
   - [ ] Timestamps accurate

3. **Verify Telemetry Storage**
   - [ ] Telemetry saved to workspace/telemetry/
   - [ ] JSON format valid
   - [ ] Can be parsed and analyzed

**Success Criteria:**
- ✅ All 18 commands emit telemetry
- ✅ Telemetry structure consistent
- ✅ All required fields present
- ✅ Telemetry stored persistently

**Test Results:**
- Status: NOT STARTED
- Execution Time: TBD
- Issues Found: TBD

---

## Test Execution Log

### Test Session 1: [DATE]
- **Tester:** TBD
- **Environment:** BMAD Enhanced V2
- **Tests Executed:** TBD
- **Tests Passed:** TBD
- **Tests Failed:** TBD
- **Issues Found:** TBD

### Test Session 2: [DATE]
- TBD

---

## Issues Tracking

### Issue Log

| ID | Test | Severity | Description | Status | Resolution |
|----|------|----------|-------------|--------|------------|
| TBD | TBD | TBD | TBD | TBD | TBD |

**Severity Levels:**
- **Critical:** Blocks testing, workflow cannot complete
- **High:** Major functionality broken, workaround exists
- **Medium:** Functionality impaired, minor impact
- **Low:** Minor issue, cosmetic or edge case

---

## Test Results Summary

### Overall Status
- **Total Tests:** 6
- **Passed:** 0
- **Failed:** 0
- **Blocked:** 0
- **Not Started:** 6

### Test Coverage
- ✅ End-to-end workflows: NOT STARTED
- ✅ Cross-subagent coordination: NOT STARTED
- ✅ Error recovery: NOT STARTED
- ✅ State persistence: NOT STARTED
- ✅ Telemetry: NOT STARTED

### Critical Findings
- TBD

### Recommendations
- TBD

---

## Next Steps

After completing integration testing:

1. **Document All Findings**
   - Create issue for each bug found
   - Prioritize fixes (critical → high → medium → low)
   - Update test plan based on learnings

2. **Create Integration Test Report**
   - Summary of all test results
   - Workflow execution logs
   - Issues found and resolved
   - Recommendations for Phase 3 Task 2

3. **Proceed to Phase 3 Task 2**
   - Performance Optimization (2-3 hours)
   - Use learnings from integration tests
   - Profile bottlenecks identified during testing

---

**Test Plan Created By:** Session 11
**Last Updated:** 2025-02-03
**Status:** In Progress
**Next Review:** After Test 1 completion
