# Quality Review Skill: Comprehensive Quality Orchestration

<!-- BMAD Enhanced Quality Review Orchestrator -->
<!-- Coordinates execution of 5 specialized quality skills -->
<!-- Version: 2.0 (Refactored to orchestrator pattern) -->

## Purpose

Orchestrate comprehensive quality assessment by executing 5 specialized quality skills in sequence and synthesizing results into a unified quality gate decision.

**Architecture (Skills + Orchestration):**
- **risk-profile.md**: Assess risks using P×I methodology → Identify high-risk areas
- **test-design.md**: Design comprehensive test strategy → Define P0/P1/P2 tests
- **trace-requirements.md**: Map AC → Implementation → Tests → Identify coverage gaps
- **nfr-assess.md**: Assess NFRs (security, performance, reliability, etc.) → NFR scores
- **quality-gate.md**: Synthesize all assessments → Final PASS/CONCERNS/FAIL decision
- **review-task.md** (this file): Orchestrate all 5 skills → Unified quality review

**Key Innovation:**
- Separation of concerns: Each skill focused on one quality dimension
- Reusability: Individual skills can be run standalone or as part of review
- Composability: Easy to add new quality skills
- Maintainability: Smaller, focused skill files instead of monolithic review

## When to Use This Skill

Use this skill when you need to:
- Perform comprehensive quality review of completed task
- Execute full quality assessment (all 5 skills in sequence)
- Generate unified quality gate decision
- Prepare for merge/deploy/release decision

**For individual assessments, use specific skills:**
- Need only risk assessment? → Use `risk-profile.md` directly
- Need only test strategy? → Use `test-design.md` directly
- Need only traceability? → Use `trace-requirements.md` directly
- Need only NFR assessment? → Use `nfr-assess.md` directly
- Need only gate decision? → Use `quality-gate.md` directly (requires other assessments)

**Do NOT use this skill for:**
- Tasks still in progress (wait for "Review" status)
- Draft task specifications (use planning skill)
- Quick spot checks (use individual skills)

## File Modification Permissions

**CRITICAL PERMISSION BOUNDARIES:**

**YOU ARE AUTHORIZED TO:**
- ✅ Read task specification and implementation files
- ✅ Execute the 5 quality skills in sequence
- ✅ Generate quality assessment reports
- ✅ Update "Quality Review" section of task file with summary
- ✅ Create quality gate files in .claude/quality/gates/

**YOU ARE NOT AUTHORIZED TO:**
- ❌ Modify any other section of task file (Objective, AC, Context, Tasks, Implementation Record)
- ❌ Modify implementation or test code
- ❌ Change task status to "Done"
- ❌ Bypass individual skills (must run through orchestration)

---

## SEQUENTIAL Orchestration Execution

**CRITICAL:** Execute skills in dependency order. Each skill builds on previous results.

### Step 0: Load Configuration and Verify Task

**Purpose:** Load configuration, verify task readiness, ask user for execution mode.

**Actions:**

1. **Load Configuration:**
   ```yaml
   # Read .claude/config.yaml
   quality:
     qualityLocation: .claude/quality
     gateThreshold: CONCERNS
     riskScoreThreshold: 6
     requireAllAssessments: false
   ```

2. **Get Task File:**
   - Prompt user for task file path
   - Example: `.claude/tasks/task-007-user-auth.md`
   - Verify file exists and is readable

3. **Verify Task Readiness:**
   - Read task specification
   - Check status is "Review"
   - Verify implementation complete (all tasks checked [x])
   - Verify Implementation Record populated

4. **Ask User for Execution Mode:**
   ```
   Quality Review Options:

   A) Full Review (Recommended)
      Run all 5 skills in sequence:
      1. Risk Profile → 2. Test Design → 3. Traceability → 4. NFR → 5. Quality Gate
      Duration: ~10-15 minutes
      Result: Comprehensive quality assessment with gate decision

   B) Individual Skills
      Run specific skills only:
      1. Risk Profile only
      2. Test Design only
      3. Traceability only
      4. NFR Assessment only
      5. Quality Gate only (requires other assessments exist)

   C) Resume Partial Review
      Continue from where previous review left off
      (Only available if some assessments already exist)

   Which option would you like?
   ```

5. **Check Existing Assessments** (for resume option):
   ```bash
   ls .claude/quality/assessments/{task-id}-*
   # Check which assessments already exist
   ```

**Halt If:**
- Config file missing or invalid
- Task file not found or unreadable
- Task status not "Review"
- Implementation appears incomplete (unchecked tasks, empty Implementation Record)

**Output:**
```
✓ Configuration loaded
✓ Task: {task-id} - {title}
✓ Task status: Review (ready for quality assessment)
✓ Implementation complete: {tasks_complete}/{total_tasks}
✓ Execution mode: {Full Review | Individual Skills | Resume}
```

---

## Execution Paths

### Path A: Full Review (All 5 Skills)

Execute all skills in sequence: risk-profile → test-design → trace-requirements → nfr-assess → quality-gate

**Proceed to Step 1.**

### Path B: Individual Skills

Execute only requested skill(s). Skip to Step 7 (present results) when done.

**User selects specific skill → Execute that skill → Present results → Done.**

### Path C: Resume Partial Review

Detect which assessments exist, skip those, run remaining skills.

**Example:**
- Existing: risk-profile, test-design
- Missing: trace-requirements, nfr-assess, quality-gate
- Action: Run trace → nfr → gate → Done

**Proceed to Step 1, skipping already-completed skills.**

---

## Step 1: Execute Risk Profile Skill

**Purpose:** Assess implementation risks using P×I (Probability × Impact) methodology.

**Actions:**

1. **Invoke risk-profile.md skill:**
   ```
   Executing: .claude/skills/quality/risk-profile.md
   Task: {task-id}
   ```

2. **Skill executes 7 steps:**
   - Load config and task
   - Identify risk areas (10-20 risks)
   - Score risks (P×I, scale 1-9)
   - Develop mitigation strategies
   - Prioritize test scenarios (P0/P1/P2)
   - Generate risk profile report
   - Present summary

3. **Output:**
   - `.claude/quality/assessments/{task-id}-risk-{YYYYMMDD}.md`
   - Risk summary presented to user

4. **Capture Results:**
   ```yaml
   riskProfile:
     status: complete
     file: .claude/quality/assessments/{task-id}-risk-{date}.md
     summary:
       totalRisks: 12
       criticalRisks: 1
       highRisks: 3
       highRisksMitigated: 2/4
       highRisksTested: 3/4
   ```

**Handle Errors:**
- If skill fails: Report error, ask user to fix and re-run, or skip and continue
- If skill incomplete: Halt or continue without risk data (impacts gate decision)

**Output:**
```
✓ Risk Profile complete
✓ Total Risks: {total} ({critical} critical, {high} high)
✓ Mitigation Coverage: {mitigated}/{high_risk_items}
✓ Report: {file_path}
```

---

## Step 2: Execute Test Design Skill

**Purpose:** Design comprehensive test strategy with P0/P1/P2 priorities and mock strategies.

**Actions:**

1. **Invoke test-design.md skill:**
   ```
   Executing: .claude/skills/quality/test-design.md
   Task: {task-id}
   Risk Profile: {risk-file} (for risk-informed test prioritization)
   ```

2. **Skill executes 7 steps:**
   - Load config and context (includes risk profile if available)
   - Analyze test requirements per AC
   - Design test scenarios (Given-When-Then)
   - Develop mock strategies
   - Plan CI/CD integration
   - Calculate test summary
   - Generate test design document
   - Present summary

3. **Output:**
   - `.claude/quality/assessments/{task-id}-test-design-{YYYYMMDD}.md`
   - Test design summary presented to user

4. **Capture Results:**
   ```yaml
   testDesign:
     status: complete
     file: .claude/quality/assessments/{task-id}-test-design-{date}.md
     summary:
       totalTests: 24
       p0Tests: 8
       p1Tests: 12
       p2Tests: 4
       estimatedDuration: "5m 30s"
   ```

**Handle Errors:**
- If skill fails: Report error, ask user to fix and re-run, or skip and continue

**Output:**
```
✓ Test Design complete
✓ Total Tests: {total} ({p0} P0, {p1} P1, {p2} P2)
✓ Test Levels: {unit} unit, {integration} integration, {e2e} E2E
✓ Report: {file_path}
```

---

## Step 3: Execute Requirements Traceability Skill

**Purpose:** Map acceptance criteria → implementation → tests with gap analysis.

**Actions:**

1. **Invoke trace-requirements.md skill:**
   ```
   Executing: .claude/skills/quality/trace-requirements.md
   Task: {task-id}
   Risk Profile: {risk-file} (for gap severity assessment)
   Test Design: {test-file} (for test-to-requirement mapping)
   ```

2. **Skill executes 7 steps:**
   - Load config and context
   - Build forward traceability (AC → Implementation)
   - Build backward traceability (Tests → AC)
   - Identify coverage gaps
   - Create traceability matrix
   - Generate recommendations
   - Generate traceability report
   - Present summary

3. **Output:**
   - `.claude/quality/assessments/{task-id}-trace-{YYYYMMDD}.md`
   - Traceability summary presented to user

4. **Capture Results:**
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
       gaps:
         critical: 0
         high: 2
         medium: 1
   ```

**Handle Errors:**
- If skill fails: Report error - traceability is critical for quality gate

**Output:**
```
✓ Requirements Traceability complete
✓ Traceability Score: {score}%
✓ Implementation Coverage: {impl_coverage}%
✓ Test Coverage: {test_coverage}%
✓ Gaps: {total_gaps} ({critical} critical, {high} high)
✓ Report: {file_path}
```

---

## Step 4: Execute NFR Assessment Skill

**Purpose:** Assess non-functional requirements across 6 categories (security, performance, reliability, maintainability, scalability, usability).

**Actions:**

1. **Invoke nfr-assess.md skill:**
   ```
   Executing: .claude/skills/quality/nfr-assess.md
   Task: {task-id}
   Risk Profile: {risk-file} (for security/performance risk cross-reference)
   Traceability: {trace-file} (for implementation evidence)
   Test Design: {test-file} (for performance test validation)
   ```

2. **Skill executes 8 steps:**
   - Load config and context
   - Security assessment (validation, auth, encryption, vulnerabilities)
   - Performance assessment (response time, queries, caching)
   - Reliability assessment (error handling, logging, monitoring)
   - Maintainability assessment (code quality, docs, coverage)
   - Scalability assessment (stateless, indexing, async processing)
   - Usability assessment (API design, error messages, docs)
   - Generate NFR report
   - Present summary

3. **Output:**
   - `.claude/quality/assessments/{task-id}-nfr-{YYYYMMDD}.md`
   - NFR summary presented to user

4. **Capture Results:**
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
       gaps:
         critical: 2
         high: 4
         medium: 3
   ```

**Handle Errors:**
- If skill fails: Report error, ask user to fix and re-run, or continue without NFR data

**Output:**
```
✓ NFR Assessment complete
✓ Overall NFR Score: {score}%
✓ Security: {security}%, Reliability: {reliability}%
✓ Critical NFR Gaps: {critical_gaps}
✓ Report: {file_path}
```

---

## Step 5: Execute Quality Gate Skill

**Purpose:** Synthesize all assessments and make final PASS/CONCERNS/FAIL/WAIVED decision.

**Actions:**

1. **Invoke quality-gate.md skill:**
   ```
   Executing: .claude/skills/quality/quality-gate.md
   Task: {task-id}
   Risk Profile: {risk-file}
   Test Design: {test-file}
   Traceability: {trace-file}
   NFR Assessment: {nfr-file}
   ```

2. **Skill executes 8 steps:**
   - Load config and all assessments
   - Synthesize risk management dimension
   - Synthesize test coverage dimension
   - Synthesize traceability dimension
   - Synthesize NFR dimension
   - Synthesize implementation quality dimension
   - Synthesize compliance dimension
   - Calculate overall quality score
   - Make gate decision (PASS/CONCERNS/FAIL/WAIVED)
   - Generate reports (YAML + Markdown)
   - Present summary

3. **Output:**
   - `.claude/quality/gates/{task-id}-gate-{YYYYMMDD}.yaml` (for CI/CD)
   - `.claude/quality/gates/{task-id}-gate-{YYYYMMDD}.md` (human-readable)
   - Gate summary presented to user

4. **Capture Results:**
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
       waivers: 1
   ```

**Handle Errors:**
- If skill fails: Report error - gate decision is required output of review

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

---

## Step 6: Update Task File with Quality Review Summary

**Purpose:** Update task file Quality Review section with synthesized summary.

**Actions:**

1. **Read task file Quality Review section:**
   ```markdown
   ## Quality Review
   <!-- This section updated by quality-review skill -->
   ```

2. **Generate summary from gate decision:**
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

   ---

   For complete details, see quality gate report: `.claude/quality/gates/{task-id}-gate-{date}.md`
   ```

3. **Update task file:**
   - Use Edit tool to replace Quality Review section
   - Preserve all other sections unchanged

**Output:**
```
✓ Task file Quality Review section updated
✓ Task file: {task-file-path}
```

---

## Step 7: Present Unified Quality Review Summary

**Purpose:** Present comprehensive summary synthesizing all 5 skill results.

**Actions:**

1. **Generate unified summary:**
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
   **Waivers:** {count}

   {Brief rationale from gate decision}

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   ## 📊 Quality Dimension Scores

   1. Risk Management: {risk_score}% ({risk_status})
      - Total Risks: {total} ({critical} critical, {high} high)
      - Mitigation: {mitigated}/{high_risk_items}
      - Report: {risk-file}

   2. Test Coverage: {test_score}% ({test_status})
      - Total Tests: {total} ({p0} P0, {p1} P1, {p2} P2)
      - P0 Passing: {passing}/{p0_total}
      - Coverage: {coverage}%
      - Report: {test-file}

   3. Requirements Traceability: {trace_score}% ({trace_status})
      - Total AC: {total}
      - Implementation: {impl_coverage}%
      - Test Coverage: {test_coverage}%
      - Report: {trace-file}

   4. Non-Functional Requirements: {nfr_score}% ({nfr_status})
      - Security: {security}%
      - Performance: {performance}%
      - Reliability: {reliability}%
      - Report: {nfr-file}

   5. Implementation Quality: {impl_score}% ({impl_status})
      - Task Completion: {completion}%
      - Documentation: {docs}%

   6. Compliance: {compliance_score}% ({compliance_status})
      - Standards: {standards_met}/{standards_total}

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

   All reports available at:

   1. ⭐ Quality Gate (START HERE): {gate-md-file}
   2. Risk Profile: {risk-file}
   3. Test Design: {test-file}
   4. Traceability: {trace-file}
   5. NFR Assessment: {nfr-file}
   6. Gate YAML (CI/CD): {gate-yaml-file}

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   ## 💡 Next Steps

   {Recommendations based on gate status}

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   What would you like to do?

   A) Accept decision and proceed with merge
   B) Review detailed reports first
   C) Address action items now (estimated: {effort})
   D) Request waiver for specific gaps
   E) Re-run specific assessment (if data changed)
   ```

2. **Wait for user decision**

3. **Handle user choice:**
   - **A) Accept and proceed:**
     - Confirm decision recorded in gate file
     - Remind user to mark task as "Done" after merge
     - Remind user to create tickets for action items

   - **B) Review reports:**
     - Provide guidance on which report to start with (gate report)
     - Explain how reports interconnect
     - Return to decision prompt after review

   - **C) Address action items:**
     - Hand back to implementation skill with action items as new subtasks
     - Schedule re-review after fixes complete

   - **D) Request waiver:**
     - Collect waiver details (gap, justification, approver, timeline)
     - Update gate file with waiver
     - Update gate status to WAIVED
     - Confirm waiver tracking in issue system

   - **E) Re-run specific assessment:**
     - Ask which assessment(s) to re-run
     - Execute selected skill(s)
     - Re-run quality-gate skill
     - Present updated summary

**Output:**
- Unified summary presented
- User decision collected
- Next steps clear

---

## Execution Complete

Quality review orchestration complete when:

- [x] All 5 skills executed successfully (or skipped intentionally)
- [x] Quality gate decision made
- [x] Gate reports generated (YAML + Markdown)
- [x] Task file Quality Review section updated
- [x] Unified summary presented to user
- [x] User decision collected and actioned

---

## Error Handling

### Skill Execution Failures

**If risk-profile fails:**
- Impact: Gate decision lacks risk data, may be less accurate
- Action: Ask user to fix issue and re-run, or continue without risk data
- Gate: Proceeds but notes missing risk assessment

**If test-design fails:**
- Impact: Gate decision lacks test strategy data
- Action: Ask user to fix issue and re-run, or use traceability test data as fallback
- Gate: Proceeds with fallback data or notes missing assessment

**If trace-requirements fails:**
- Impact: CRITICAL - gate needs traceability for coverage assessment
- Action: Must fix and re-run, cannot proceed without traceability
- Gate: Cannot proceed, HALT

**If nfr-assess fails:**
- Impact: Gate decision lacks NFR scores (security, performance, etc.)
- Action: Ask user to fix issue and re-run, or use implementation quality as proxy
- Gate: Proceeds with fallback but notes missing NFR data

**If quality-gate fails:**
- Impact: CRITICAL - cannot make gate decision
- Action: Must fix and re-run, this is the final output
- Gate: Cannot proceed, HALT

### Graceful Degradation

When skills fail, provide fallbacks when possible:

```yaml
# Minimum viable gate (traceability only)
qualityGate:
  dimensions:
    riskManagement: N/A (assessment missing)
    testCoverage: from traceability
    traceability: from trace-requirements
    nfr: N/A (assessment missing)
    implementationQuality: from task file
    compliance: basic checks

  decision:
    status: CONCERNS
    confidence: MEDIUM (limited data)
    reasoning: |
      Gate decision made with limited assessment data.
      Risk profile and NFR assessment not performed.
      Decision based primarily on traceability and implementation record.
```

---

## Best Practices

1. **Run full review when possible** - Most comprehensive assessment
2. **Use individual skills during development** - Faster feedback loops
3. **Re-run specific skills when data changes** - Don't redo entire review
4. **Always start with gate report** - Best overview, links to all details
5. **Track action items in issue system** - Don't lose follow-up work
6. **Document waivers properly** - Include justification, timeline, owner
7. **Automate in CI/CD** - Use gate YAML for automated checks

---

## Integration with Subagents

When Quinn (quality subagent) is built, this orchestration will be invoked via:

```
@quinn *review task-007
```

Quinn will:
1. Route to review-task.md skill (this file)
2. Orchestrate execution of 5 quality skills
3. Present results in Quinn's persona voice
4. Provide advisory guidance on gate decision

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-10-28 | Initial monolithic quality review (2000+ lines) |
| 2.0 | 2025-10-28 | Refactored to orchestrator pattern (5 focused skills) |

---

**End of Quality Review Orchestrator**
