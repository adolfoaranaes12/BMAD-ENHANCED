---
name: review-task
description: Orchestrate comprehensive quality assessment by executing 5 specialized quality skills in sequence and synthesizing results into a unified quality gate decision. Use when performing final review of completed implementation.
acceptance:
  - all_assessments_completed: "All 5 quality skills executed successfully (risk-profile, test-design, trace-requirements, nfr-assess, quality-gate)"
  - gate_decision_made: "Quality gate decision generated (PASS/CONCERNS/FAIL/WAIVED) with overall quality score"
  - reports_generated: "Assessment reports created in .claude/quality/ (assessments/*.md, gates/*.yaml, gates/*.md)"
  - task_updated: "Task file Quality Review section updated with summary and report links"
inputs:
  task_file:
    type: string
    required: true
    description: "Path to task file in .claude/tasks/{task-id}.md format"
  execution_mode:
    type: enum
    values: ["full", "individual", "resume"]
    default: "full"
    description: "Execution mode: full (all 5 skills), individual (selected skills), resume (continue partial review)"
  selected_skills:
    type: array
    required: false
    description: "For individual mode: which skills to execute (risk-profile, test-design, trace-requirements, nfr-assess, quality-gate)"
outputs:
  gate_decision:
    type: object
    description: "Quality gate decision with status, score, blockers, action items"
  assessment_reports:
    type: object
    description: "File paths to all generated assessment reports"
  review_summary:
    type: string
    description: "Human-readable summary of quality review results"
telemetry:
  emit: "skill.review-task.completed"
  track:
    - task_id
    - execution_mode
    - duration_ms
    - skills_executed
    - gate_decision
    - overall_score
---

# Quality Review Orchestrator

Orchestrate comprehensive quality assessment by executing 5 specialized quality skills in sequence and synthesizing results into a unified quality gate decision.

## Purpose

This skill coordinates execution of 5 specialized quality skills to provide comprehensive quality assessment:

1. **risk-profile** → Assess implementation risks using P×I methodology
2. **test-design** → Design comprehensive test strategy with P0/P1/P2 priorities
3. **trace-requirements** → Map AC → Implementation → Tests with gap analysis
4. **nfr-assess** → Assess non-functional requirements (security, performance, reliability, etc.)
5. **quality-gate** → Synthesize all assessments into final gate decision

## When to Use

Use this skill when:
- Performing comprehensive quality review of completed task
- Task status is "Review" (implementation complete)
- Preparing for merge/deploy/release decision

For individual assessments, invoke specific skills directly:
- Need only risk assessment? → Use `risk-profile` directly
- Need only test strategy? → Use `test-design` directly
- Need only traceability? → Use `trace-requirements` directly
- Need only NFR assessment? → Use `nfr-assess` directly
- Need only gate decision? → Use `quality-gate` directly (requires other assessments)

Do NOT use when:
- Task still in progress (wait for "Review" status)
- Reviewing draft specifications (use planning skill)
- Performing quick spot checks (use individual skills)

## Architecture

```
Quality Review Orchestration Flow:

Step 0: Configuration & Verification
  ↓
Step 1: risk-profile → .claude/quality/assessments/{task-id}-risk-{date}.md
  ↓
Step 2: test-design → .claude/quality/assessments/{task-id}-test-design-{date}.md
  ↓
Step 3: trace-requirements → .claude/quality/assessments/{task-id}-trace-{date}.md
  ↓
Step 4: nfr-assess → .claude/quality/assessments/{task-id}-nfr-{date}.md
  ↓
Step 5: quality-gate → .claude/quality/gates/{task-id}-gate-{date}.{yaml,md}
  ↓
Step 6: Update Task File
  ↓
Step 7: Present Summary
```

Each skill builds on previous results. Execution order is critical.

## File Modification Permissions

**AUTHORIZED:**
- ✅ Read task specification and implementation files
- ✅ Execute the 5 quality skills in sequence
- ✅ Generate quality assessment reports
- ✅ Update "Quality Review" section of task file with summary
- ✅ Create quality gate files in .claude/quality/gates/

**NOT AUTHORIZED:**
- ❌ Modify any other section of task file (Objective, AC, Context, Tasks, Implementation Record)
- ❌ Modify implementation or test code
- ❌ Change task status to "Done"
- ❌ Bypass individual skills

## Sequential Orchestration Execution

### Step 0: Configuration and Verification

**Purpose:** Load configuration, verify task readiness, determine execution mode.

**Actions:**

1. Load configuration from `.claude/config.yaml`:
   ```yaml
   quality:
     qualityLocation: .claude/quality
     gateThreshold: CONCERNS
     riskScoreThreshold: 6
     requireAllAssessments: false
   ```

2. Get and verify task file:
   - Prompt user for task file path (e.g., `.claude/tasks/task-007-user-auth.md`)
   - Verify file exists and is readable
   - Check status is "Review"
   - Verify implementation complete (all tasks checked [x])
   - Verify Implementation Record populated

3. Determine execution mode:
   ```
   Quality Review Options:

   A) Full Review (Recommended) - Run all 5 skills
   B) Individual Skills - Run specific skills only
   C) Resume Partial Review - Continue from where previous review left off
   ```

4. Check existing assessments (for resume option):
   ```bash
   ls .claude/quality/assessments/{task-id}-*
   ```

**Halt if:**
- Config file missing or invalid
- Task file not found or unreadable
- Task status not "Review"
- Implementation appears incomplete

**Output:**
```
✓ Configuration loaded
✓ Task: {task-id} - {title}
✓ Task status: Review (ready for quality assessment)
✓ Implementation complete: {tasks_complete}/{total_tasks}
✓ Execution mode: {Full Review | Individual Skills | Resume}
```

**Reference:** See [execution-paths.md](references/execution-paths.md) for detailed flow logic.

---

### Step 1: Execute Risk Profile Skill

**Purpose:** Assess implementation risks using P×I (Probability × Impact) methodology.

**Actions:**

1. Invoke risk-profile.md skill:
   ```
   Executing: .claude/skills/quality/risk-profile.md
   Task: {task-id}
   ```

2. Skill executes 7-step risk assessment process:
   - Identify risk areas (10-20 risks)
   - Score risks (P×I, scale 1-9)
   - Develop mitigation strategies
   - Prioritize test scenarios
   - Generate risk profile report

3. Capture results:
   ```yaml
   riskProfile:
     status: complete
     file: .claude/quality/assessments/{task-id}-risk-{date}.md
     summary:
       totalRisks: 12
       criticalRisks: 1
       highRisks: 3
       highRisksMitigated: 2/4
   ```

**Output:**
```
✓ Risk Profile complete
✓ Total Risks: {total} ({critical} critical, {high} high)
✓ Mitigation Coverage: {mitigated}/{high_risk_items}
✓ Report: {file_path}
```

**Error Handling:** If skill fails, ask user to fix and re-run, or skip and continue (impacts gate confidence).

---

### Step 2: Execute Test Design Skill

**Purpose:** Design comprehensive test strategy with P0/P1/P2 priorities and mock strategies.

**Actions:**

1. Invoke test-design.md skill:
   ```
   Executing: .claude/skills/quality/test-design.md
   Task: {task-id}
   Risk Profile: {risk-file} (for risk-informed test prioritization)
   ```

2. Skill executes 7-step test design process:
   - Analyze test requirements per AC
   - Design test scenarios (Given-When-Then)
   - Develop mock strategies
   - Plan CI/CD integration
   - Generate test design document

3. Capture results:
   ```yaml
   testDesign:
     status: complete
     file: .claude/quality/assessments/{task-id}-test-design-{date}.md
     summary:
       totalTests: 24
       p0Tests: 8
       p1Tests: 12
       p2Tests: 4
   ```

**Output:**
```
✓ Test Design complete
✓ Total Tests: {total} ({p0} P0, {p1} P1, {p2} P2)
✓ Test Levels: {unit} unit, {integration} integration, {e2e} E2E
✓ Report: {file_path}
```

---

### Step 3: Execute Requirements Traceability Skill

**Purpose:** Map acceptance criteria → implementation → tests with gap analysis.

**Actions:**

1. Invoke trace-requirements.md skill:
   ```
   Executing: .claude/skills/quality/trace-requirements.md
   Task: {task-id}
   Risk Profile: {risk-file}
   Test Design: {test-file}
   ```

2. Skill executes 7-step traceability process:
   - Build forward traceability (AC → Implementation)
   - Build backward traceability (Tests → AC)
   - Identify coverage gaps
   - Create traceability matrix
   - Generate recommendations

3. Capture results:
   ```yaml
   traceability:
     status: complete
     file: .claude/quality/assessments/{task-id}-trace-{date}.md
     summary:
       totalAC: 6
       implemented: 5
       tested: 6
       implementationCoverage: 83%
       testCoverage: 100%
       traceabilityScore: 87.5%
   ```

**Output:**
```
✓ Requirements Traceability complete
✓ Traceability Score: {score}%
✓ Implementation Coverage: {impl_coverage}%
✓ Test Coverage: {test_coverage}%
✓ Gaps: {total_gaps} ({critical} critical, {high} high)
✓ Report: {file_path}
```

**Error Handling:** Traceability is CRITICAL for quality gate. Must fix and re-run if fails - cannot proceed without traceability.

---

### Step 4: Execute NFR Assessment Skill

**Purpose:** Assess non-functional requirements across 6 categories.

**Actions:**

1. Invoke nfr-assess.md skill:
   ```
   Executing: .claude/skills/quality/nfr-assess.md
   Task: {task-id}
   Risk Profile: {risk-file}
   Traceability: {trace-file}
   Test Design: {test-file}
   ```

2. Skill executes 8-step NFR assessment:
   - Security assessment (validation, auth, encryption, vulnerabilities)
   - Performance assessment (response time, queries, caching)
   - Reliability assessment (error handling, logging, monitoring)
   - Maintainability assessment (code quality, docs, coverage)
   - Scalability assessment (stateless, indexing, async processing)
   - Usability assessment (API design, error messages, docs)

3. Capture results:
   ```yaml
   nfr:
     status: complete
     file: .claude/quality/assessments/{task-id}-nfr-{date}.md
     summary:
       overallScore: 72%
       categories:
         security: 70%
         performance: 80%
         reliability: 65%
         maintainability: 75%
         scalability: 70%
         usability: 70%
   ```

**Output:**
```
✓ NFR Assessment complete
✓ Overall NFR Score: {score}%
✓ Security: {security}%, Reliability: {reliability}%
✓ Critical NFR Gaps: {critical_gaps}
✓ Report: {file_path}
```

---

### Step 5: Execute Quality Gate Skill

**Purpose:** Synthesize all assessments and make final PASS/CONCERNS/FAIL/WAIVED decision.

**Actions:**

1. Invoke quality-gate.md skill:
   ```
   Executing: .claude/skills/quality/quality-gate.md
   Task: {task-id}
   Risk Profile: {risk-file}
   Test Design: {test-file}
   Traceability: {trace-file}
   NFR Assessment: {nfr-file}
   ```

2. Skill executes 8-step gate synthesis:
   - Synthesize risk management dimension
   - Synthesize test coverage dimension
   - Synthesize traceability dimension
   - Synthesize NFR dimension
   - Synthesize implementation quality dimension
   - Synthesize compliance dimension
   - Calculate overall quality score
   - Make gate decision (PASS/CONCERNS/FAIL/WAIVED)

3. Capture results:
   ```yaml
   qualityGate:
     status: complete
     yamlFile: .claude/quality/gates/{task-id}-gate-{date}.yaml
     mdFile: .claude/quality/gates/{task-id}-gate-{date}.md
     decision:
       status: CONCERNS
       overallScore: 75.5%
       canProceed: true
       blockers: []
       actionItems: 3
   ```

**Output:**
```
✓ Quality Gate complete
✓ Gate Decision: {PASS/CONCERNS/FAIL/WAIVED}
✓ Overall Quality Score: {score}%
✓ Can Proceed: {YES/NO}
✓ Blockers: {count}
✓ Action Items: {count} ({p0} P0, {p1} P1)
✓ Reports: {yaml-file}, {md-file}
```

**Error Handling:** Gate decision is CRITICAL. Must fix and re-run if fails - this is the required final output.

---

### Step 6: Update Task File with Quality Review Summary

**Purpose:** Update task file Quality Review section with synthesized summary.

**Actions:**

1. Generate summary from gate decision:
   ```markdown
   ## Quality Review

   ### Review Date
   {YYYYMMDD}

   ### Reviewer
   review-task-v2.0 (claude-sonnet-4-5)

   ### Quality Gate Decision
   {PASS | CONCERNS | FAIL | WAIVED}

   ### Overall Quality Score
   {score}%

   ### Assessment Reports
   - Risk Profile: `.claude/quality/assessments/{task-id}-risk-{date}.md`
   - Test Design: `.claude/quality/assessments/{task-id}-test-design-{date}.md`
   - Traceability: `.claude/quality/assessments/{task-id}-trace-{date}.md`
   - NFR Assessment: `.claude/quality/assessments/{task-id}-nfr-{date}.md`
   - Quality Gate: `.claude/quality/gates/{task-id}-gate-{date}.md` (⭐ Start here)

   ### Summary
   {Brief 2-3 sentence summary from gate decision}

   ### Key Findings
   {Top 3-5 findings from gate report}

   ### Action Items
   {P0 action items, if any}

   ### Recommendation
   {Recommendation from gate decision: approve/fix/waive}
   ```

2. Update task file using Edit tool (preserve all other sections unchanged)

**Output:**
```
✓ Task file Quality Review section updated
✓ Task file: {task-file-path}
```

---

### Step 7: Present Unified Quality Review Summary

**Purpose:** Present comprehensive summary synthesizing all 5 skill results.

**Actions:**

Present unified summary:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Comprehensive Quality Review Complete
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Task: {task-id} - {title}
Date: {YYYYMMDD}
Duration: {duration}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🎯 Quality Gate Decision: {STATUS}

**Overall Quality Score:** {score}%
**Can Proceed:** {YES/NO/CONDITIONAL}
**Blockers:** {count}
**Action Items:** {count} ({p0} P0, {p1} P1, {p2} P2)

{Brief rationale from gate decision}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 📊 Quality Dimension Scores

1. Risk Management: {risk_score}%
2. Test Coverage: {test_score}%
3. Requirements Traceability: {trace_score}%
4. Non-Functional Requirements: {nfr_score}%
5. Implementation Quality: {impl_score}%
6. Compliance: {compliance_score}%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🚨 Critical Findings

{List of critical/high findings from all assessments}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## ✅ Action Items

### P0 (Must Complete Before Merge):
{P0 action items from gate}

### P1 (Should Complete Before Release):
{P1 action items from gate}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 📄 Generated Reports

1. ⭐ Quality Gate (START HERE): {gate-md-file}
2. Risk Profile: {risk-file}
3. Test Design: {test-file}
4. Traceability: {trace-file}
5. NFR Assessment: {nfr-file}
6. Gate YAML (CI/CD): {gate-yaml-file}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 💡 Next Steps

What would you like to do?

A) Accept decision and proceed with merge
B) Review detailed reports first
C) Address action items now
D) Request waiver for specific gaps
E) Re-run specific assessment
```

**Reference:** See [summary-templates.md](references/summary-templates.md) for complete output templates.

**User Decision Handling:**

- **A) Accept and proceed:** Confirm decision recorded, remind to mark task "Done" after merge, create tickets for action items
- **B) Review reports:** Provide guidance on which report to start with (gate report), explain interconnections
- **C) Address action items:** Hand to implementation skill with action items as subtasks, schedule re-review
- **D) Request waiver:** Collect details (gap, justification, approver, timeline), update gate file with waiver
- **E) Re-run assessment:** Execute selected skill(s), re-run quality-gate, present updated summary

---

## Execution Complete

Quality review orchestration complete when:

- [x] All 5 skills executed successfully (or skipped intentionally)
- [x] Quality gate decision made
- [x] Gate reports generated (YAML + Markdown)
- [x] Task file Quality Review section updated
- [x] Unified summary presented to user
- [x] User decision collected and actioned

## Best Practices

1. **Run full review when possible** - Most comprehensive assessment
2. **Use individual skills during development** - Faster feedback loops
3. **Re-run specific skills when data changes** - Don't redo entire review
4. **Always start with gate report** - Best overview, links to all details
5. **Track action items in issue system** - Don't lose follow-up work
6. **Document waivers properly** - Include justification, timeline, owner
7. **Automate in CI/CD** - Use gate YAML for automated checks

## References

- [execution-paths.md](references/execution-paths.md) - Detailed execution flow for full/individual/resume modes
- [error-handling.md](references/error-handling.md) - Error scenarios, graceful degradation, fallback strategies
- [summary-templates.md](references/summary-templates.md) - Output templates and formatting examples
- [integration-guide.md](references/integration-guide.md) - CI/CD integration, subagent coordination, automation patterns
