# Session 7 Handoff: QA Workflow Enhancement & Story Validation

**Date:** 2025-10-31
**Priority:** HIGH - Complete pending migrations from BMAD
**Estimated Effort:** 4-6 hours
**Dependencies:** None (Task Master integration deferred post-MVP)

---

## Mission Objective

Implement two critical missing pieces from BMAD migration:

1. **apply-qa-fixes skill** - Enable James to consume QA outputs and systematically fix issues
2. **validate-story skill** - Enable pre-implementation story validation (planning layer)

These complete the Quality ↔ Development feedback loop and ensure implementation readiness.

---

## Context: Where We Are

### ✅ What's Already Complete

**Developer Agent (James) - COMPLETE:**
- ✅ james-developer-v2.md with intelligent routing, guardrails, verification
- ✅ implement-feature skill (TDD workflow)
- ✅ fix-issue skill (bug fixing)
- ✅ bmad-commands primitives layer
- ✅ /james slash command routing

**Quality Agent (Quinn) - COMPLETE:**
- ✅ quinn-quality.md subagent
- ✅ review-task skill (orchestrates 5 quality assessments)
- ✅ risk-profile skill
- ✅ test-design skill
- ✅ trace-requirements skill
- ✅ nfr-assess skill
- ✅ quality-gate skill
- ✅ /quinn slash command routing

**Integration Points:**
- ✅ Tasks flow: James implements → Quinn reviews → Quality gate decision
- ✅ Quality reports: Structured YAML gates + Markdown assessments in `.claude/quality/`

---

### 🔄 What's Missing (Your Mission)

#### Gap 1: apply-qa-fixes Skill

**Problem:** After Quinn reviews and creates quality gate with issues, James has no structured way to consume and fix them.

**BMAD Original:**
- File: `BMAD/.bmad-core/tasks/apply-qa-fixes.md` (151 lines)
- Agent: dev.md (James)
- Command: `*review-qa`

**What it does:**
1. Reads QA gate YAML and assessment markdowns
2. Builds prioritized fix plan (high severity → NFR failures → coverage gaps)
3. Applies code fixes and adds missing tests
4. Validates with lint/tests
5. Updates story Dev Agent Record sections only

**Current State:** We have `fix-issue` skill, but it's generic bug fixing, NOT QA-specific.

**Your Task:** Create `apply-qa-fixes` skill that integrates James ↔ Quinn workflows.

---

#### Gap 2: validate-story Skill

**Problem:** No pre-implementation validation to catch story issues before James starts work.

**BMAD Original:**
- File: `BMAD/.bmad-core/tasks/validate-next-story.md` (137 lines)
- Agent: pm.md / po.md / sm.md
- Command: `*validate` (run before handing story to dev)

**What it does:**
1. Template completeness validation (all sections present, no placeholders)
2. File structure validation (paths, source tree, directory structure)
3. UI/Frontend completeness (if applicable)
4. Acceptance criteria satisfaction assessment
5. Testing instructions review
6. Security considerations
7. Task sequence validation
8. Anti-hallucination verification (source references, architecture alignment)
9. Dev agent implementation readiness
10. Generate GO/NO-GO report

**Current State:** Nothing. Stories go directly to James without validation.

**Your Task:** Create `validate-story` skill in planning layer with pre-implementation validation.

---

## Technical Architecture

### Apply QA Fixes Skill Architecture

**Location:** `.claude/skills/development/apply-qa-fixes/`

**Layer:** Workflow Skills (Layer 2)

**Integration Points:**

1. **Input Sources (Quinn's Outputs):**
   - Quality gate YAML: `.claude/quality/gates/{task-id}-gate-{date}.yaml`
   - Risk assessment: `.claude/quality/assessments/{task-id}-risk-{date}.md`
   - Test design: `.claude/quality/assessments/{task-id}-test-design-{date}.md`
   - Trace report: `.claude/quality/assessments/{task-id}-trace-{date}.md`
   - NFR assessment: `.claude/quality/assessments/{task-id}-nfr-{date}.md`

2. **Routing (from James):**
   ```
   User: @james *apply-qa-fixes task-007

   James (james-developer-v2):
   - Load task file
   - Load latest quality gate for task
   - Assess fix complexity (scoring)
   - Route to apply-qa-fixes skill
   - Enforce guardrails
   - Verify acceptance criteria after fixes
   - Emit telemetry
   ```

3. **Skill Workflow:**
   ```
   Step 0: Load Configuration
   - Load .claude/config.yaml
   - Locate task file
   - Find latest quality gate

   Step 1: Parse QA Findings
   - Parse gate.yaml: top_issues[], nfr_validation, trace.ac_gaps
   - Extract high/medium/low severity items
   - Extract NFR failures/concerns
   - Identify test coverage gaps

   Step 2: Build Fix Plan (Priority Order)
   Priority 1: High severity top_issues (security/perf/reliability)
   Priority 2: NFR status FAIL → then CONCERNS
   Priority 3: Test coverage gaps (P0 scenarios from test-design)
   Priority 4: Trace uncovered requirements (AC gaps)
   Priority 5: Medium severity issues
   Priority 6: Low severity issues

   Step 3: Apply Fixes (using bmad-commands)
   - Use primitives for file operations (read_file, write_file, edit_file)
   - Add missing tests to close coverage gaps
   - Fix code issues per plan
   - Follow project architecture

   Step 4: Validate
   - Run tests (use bmad-commands run_tests.py)
   - Run lint
   - Iterate until clean

   Step 5: Update Task File
   AUTHORIZED to update ONLY:
   - Implementation Record section (what fixed, why, how)
   - File List (add/modified/deleted files)
   - Status (InProgress → Review if fixes need re-review)

   NOT AUTHORIZED to update:
   - Objective, Acceptance Criteria, Context, Tasks
   - Quality Review section (that's Quinn's territory)

   Step 6: Emit Telemetry
   - Fixes applied count
   - Test results
   - Coverage improvement
   - Files modified
   ```

4. **Outputs:**
   ```yaml
   outputs:
     fixes_applied:
       type: array
       description: "List of fixes applied with issue IDs"
     tests_added:
       type: number
       description: "Number of tests added"
     coverage_improvement:
       type: number
       description: "Coverage improvement percentage"
     validation_passed:
       type: boolean
       description: "Whether lint and tests pass after fixes"

   telemetry:
     emit: "skill.apply-qa-fixes.completed"
     track:
       - task_id
       - fixes_count
       - tests_added
       - coverage_before
       - coverage_after
       - duration_ms
   ```

5. **Example Usage:**
   ```bash
   # After Quinn review creates gate with CONCERNS/FAIL
   @james *apply-qa-fixes task-007

   # James:
   # ✅ Quality gate loaded: CONCERNS (3 high, 2 medium issues)
   # ✅ Fix plan created (5 fixes prioritized)
   # ⏳ Applying fixes...
   # ✅ Fix 1/5: Added rate limiting middleware (SEC-001)
   # ✅ Fix 2/5: Added SQL parameterization (SEC-002)
   # ✅ Fix 3/5: Added integration tests for auth flow (TEST-001)
   # ...
   # ✅ All fixes applied
   # ✅ Lint: 0 problems
   # ✅ Tests: 45/45 passed (coverage: 82% → 89%)
   # ✅ Task updated
   #
   # Ready for re-review: @quinn *review task-007
   ```

---

### Validate Story Skill Architecture

**Location:** `.claude/skills/planning/validate-story/`

**Layer:** Workflow Skills (Layer 2)

**Who Uses It:**
- Product Owner (PO) before handing story to James
- Scrum Master (SM) during sprint planning
- James (auto-validate before implementation if configured)

**Integration Points:**

1. **Input Sources:**
   - Story file: `.claude/stories/{epic-id}/{story-id}.md`
   - Story template: `.claude/skills/planning/create-story/references/templates.md`
   - Epic file: `.claude/epics/{epic-id}.md`
   - Architecture docs: `docs/architecture/` (if referenced in story)
   - Project structure: `docs/unified-project-structure.md`

2. **Routing:**
   ```
   Direct invocation (no subagent):
   Use .claude/skills/planning/validate-story/SKILL.md

   Or via slash command:
   /validate-story {story-file-path}
   ```

3. **Skill Workflow (10 Validation Steps):**
   ```
   Step 0: Load Core Configuration
   - Load .claude/config.yaml
   - Load story file
   - Load story template
   - Load parent epic (if referenced)

   Step 1: Template Completeness Validation
   - Extract template sections from story-tmpl.md
   - Compare story sections vs. template
   - Check for unfilled placeholders ({{var}}, _TBD_)
   - Verify all required sections present

   Step 2: File Structure and Source Tree Validation
   - File paths clarity (are new/modified files specified?)
   - Source tree relevance (is project structure referenced?)
   - Directory structure (consistent with project?)
   - File creation sequence (logical order?)
   - Path accuracy (match architecture docs?)

   Step 3: UI/Frontend Completeness (if applicable)
   - Component specifications sufficient?
   - Styling/design guidance clear?
   - User interaction flows specified?
   - Responsive/accessibility addressed?
   - Frontend-backend integration clear?

   Step 4: Acceptance Criteria Satisfaction
   - AC coverage (will tasks satisfy all ACs?)
   - AC testability (measurable and verifiable?)
   - Edge cases covered?
   - Success definition clear?
   - Task-AC mapping correct?

   Step 5: Validation and Testing Instructions
   - Test approach clarity
   - Test scenarios identified
   - Validation steps clear
   - Testing tools specified
   - Test data requirements identified

   Step 6: Security Considerations (if applicable)
   - Security requirements identified
   - Authentication/authorization specified
   - Data protection clear
   - Vulnerability prevention addressed
   - Compliance requirements addressed

   Step 7: Tasks/Subtasks Sequence Validation
   - Logical order
   - Dependencies clear
   - Granularity appropriate
   - Completeness (cover all ACs?)
   - Blocking issues

   Step 8: Anti-Hallucination Verification
   - Source verification (claims traceable to docs?)
   - Architecture alignment (matches specs?)
   - No invented details (all backed by sources?)
   - Reference accuracy (sources correct and accessible?)
   - Fact checking (cross-reference epic/architecture)

   Step 9: Dev Agent Implementation Readiness
   - Self-contained context (no need to read external docs?)
   - Clear instructions (unambiguous steps?)
   - Complete technical context (all details in Dev Notes?)
   - Missing information identified
   - All tasks actionable

   Step 10: Generate Validation Report
   Report structure:
   - Template compliance issues
   - Critical issues (must fix - story blocked)
   - Should-fix issues (important quality improvements)
   - Nice-to-have improvements
   - Anti-hallucination findings
   - Final assessment: GO / NO-GO
   - Implementation readiness score (1-10)
   - Confidence level (High/Medium/Low)
   ```

4. **Outputs:**
   ```yaml
   outputs:
     validation_passed:
       type: boolean
       description: "GO (true) or NO-GO (false) decision"
     readiness_score:
       type: number
       description: "Implementation readiness score 1-10"
     confidence_level:
       type: enum
       values: ["High", "Medium", "Low"]
       description: "Confidence in successful implementation"
     critical_issues:
       type: array
       description: "Must-fix issues blocking implementation"
     should_fix_issues:
       type: array
       description: "Important quality improvements"
     nice_to_have:
       type: array
       description: "Optional enhancements"
     anti_hallucination_findings:
       type: array
       description: "Unverifiable claims or invented details"

   telemetry:
     emit: "skill.validate-story.completed"
     track:
       - story_id
       - validation_passed
       - readiness_score
       - critical_issues_count
       - duration_ms
   ```

5. **Example Usage:**
   ```bash
   # Before implementation
   /validate-story .claude/stories/epic-001/story-003.md

   # Output:
   # ===== Story Validation Report =====
   # Story: 1.3 - User Authentication System
   #
   # Template Compliance: ✅ PASS
   # - All required sections present
   # - No unfilled placeholders
   #
   # Critical Issues: ❌ 2 FOUND (MUST FIX)
   # 1. [ARCH] Dev Notes reference non-existent "auth-service.ts" not in architecture
   # 2. [AC] AC4 "Secure password storage" has no corresponding task
   #
   # Should-Fix Issues: ⚠️ 3 FOUND
   # 1. [TEST] Testing section lacks integration test scenarios
   # 2. [SEC] Security considerations don't mention rate limiting
   # 3. [FILE] File paths reference "src/services/" but project uses "app/services/"
   #
   # Anti-Hallucination Findings: ❌ 1 FOUND
   # 1. Claims "bcrypt library" but not specified in architecture or dependencies
   #
   # === FINAL ASSESSMENT ===
   # Decision: NO-GO
   # Readiness Score: 6/10
   # Confidence: Medium
   #
   # Recommendation: Fix 2 critical issues and 1 anti-hallucination finding before
   # handing to James. Should-fix issues can be addressed during implementation.
   ```

---

## File Structure to Create

```
.claude/skills/development/apply-qa-fixes/
├── SKILL.md (main skill definition)
├── references/
│   ├── templates.md (input/output formats, gate schema)
│   ├── priority-rules.md (fix prioritization logic)
│   └── examples.md (usage examples)
└── assets/ (optional: test fixtures)

.claude/skills/planning/validate-story/
├── SKILL.md (main skill definition)
├── references/
│   ├── templates.md (validation report format, story template)
│   ├── validation-checklist.md (10 validation steps detailed)
│   └── examples.md (GO and NO-GO examples)
└── assets/ (optional: test fixtures)
```

---

## YAML Frontmatter Requirements

Both skills MUST follow 3-layer architecture compliance:

```yaml
---
name: apply-qa-fixes  # or validate-story
description: >
  [Concise description]. Use when [specific condition].
acceptance:
  - [criterion_1]: "Description"
  - [criterion_2]: "Description"
  - [criterion_3]: "Description"
inputs:
  param_name:
    type: string|number|boolean|enum|array|object
    required: true|false
    description: "What this input is for"
    validation: "Constraints or pattern" (optional)
outputs:
  output_name:
    type: string|number|boolean|array|object
    description: "What this output represents"
telemetry:
  emit: "skill.[skill-name].completed"
  track:
    - metric_1
    - metric_2
    - duration_ms
---
```

**See:** `docs/3-layer-architecture-for-skills.md` and `docs/skill-refactoring-template.md`

---

## Key Design Principles

### For apply-qa-fixes:

1. **Deterministic Prioritization:** Always same priority order (high severity → NFR failures → coverage gaps)
2. **Minimal Changes:** Fix exactly what's in the gate, don't over-engineer
3. **Validation Loop:** Always run tests after fixes, iterate until clean
4. **Strict Permissions:** Only update Implementation Record and File List in task file
5. **Observability:** Emit telemetry for all fixes applied, tests added, coverage improvement

### For validate-story:

1. **Comprehensive but Fast:** 10 steps should complete in < 3 minutes
2. **Anti-Hallucination Focus:** Verify all technical claims against source docs
3. **Actionable Findings:** Every issue must have clear fix guidance
4. **GO/NO-GO Clarity:** Binary decision with clear rationale
5. **Educational:** Report should teach story creators what to improve

---

## Integration with Existing Components

### apply-qa-fixes Integration:

**With James (james-developer-v2.md):**
- Add new command: `*apply-qa-fixes <task-id>`
- Complexity assessment: Based on number of issues and severity
- Routing logic:
  ```
  If high_severity_count > 5 OR nfr_failures > 2:
    Route to: apply-qa-fixes (with user confirmation)
    Guardrails: Max 10 files, max 800 diff lines
  Else if high_severity_count > 0 OR nfr_failures > 0:
    Route to: apply-qa-fixes
    Guardrails: Max 7 files, max 600 diff lines
  Else:
    Route to: apply-qa-fixes
    Guardrails: Max 5 files, max 400 diff lines
  ```

**With Quinn (quinn-quality.md):**
- Quinn creates quality gate → triggers James apply-qa-fixes
- After fixes, James updates task → triggers Quinn re-review
- Feedback loop: Review → Fix → Re-review → Done

**With bmad-commands:**
- Use `read_file.py` to load gate and assessments
- Use `run_tests.py` to validate after fixes
- Use `write_file.py` / `edit_file.py` for code fixes (when implemented)

**Slash Command:**
Add to `.claude/commands/james.md`:
```bash
/james apply-qa-fixes task-007
```

---

### validate-story Integration:

**With Planning Layer:**
- Part of planning workflow (after story creation, before implementation)
- Can be invoked by:
  - PM (project manager) before sprint planning
  - PO (product owner) before accepting story
  - SM (scrum master) during backlog refinement
  - James (auto-validate before implementation - optional)

**With Story Creation Skills:**
- `create-story` skill can auto-invoke `validate-story` after creation
- Validation report appended to story as "Pre-Implementation Validation" section

**Slash Command:**
Create `.claude/commands/validate-story.md`:
```bash
/validate-story .claude/stories/epic-001/story-003.md
```

---

## Testing Requirements

### For apply-qa-fixes:

**Test Scenarios:**

1. **High Severity Issues:**
   - Gate with 3 high severity security issues
   - Verify fixes applied in priority order
   - Verify tests pass after fixes

2. **NFR Failures:**
   - Gate with NFR security=FAIL, performance=CONCERNS
   - Verify NFR failures fixed before concerns
   - Verify validation passes

3. **Coverage Gaps:**
   - Gate with test_design.coverage_gaps = [AC2, AC4]
   - Verify tests added for missing ACs
   - Verify coverage improvement tracked

4. **Mixed Issues:**
   - Gate with 2 high, 3 medium, 5 low severity + 1 NFR FAIL + 2 coverage gaps
   - Verify correct priority order applied
   - Verify all issues addressed

5. **Guardrail Violations:**
   - Gate with 15 high severity issues requiring 12 file changes
   - Verify James escalates to user for confirmation
   - Verify guardrails enforced

**Test Fixtures:**
Create sample quality gates in `assets/`:
- `sample-gate-high-severity.yaml`
- `sample-gate-nfr-failures.yaml`
- `sample-gate-coverage-gaps.yaml`
- `sample-gate-mixed-issues.yaml`

---

### For validate-story:

**Test Scenarios:**

1. **Perfect Story (GO):**
   - All sections complete
   - No placeholders
   - All ACs covered by tasks
   - Clear implementation guidance
   - Verify: validation_passed=true, score≥9

2. **Missing Sections (NO-GO):**
   - Story missing "Testing" section
   - Story missing "Dev Notes" section
   - Verify: critical_issues include missing sections
   - Verify: validation_passed=false

3. **Unfilled Placeholders (NO-GO):**
   - Story has `{{EpicNum}}` not replaced
   - Story has `_TBD_` in tasks
   - Verify: critical_issues include placeholder locations

4. **Anti-Hallucination (NO-GO):**
   - Story references "auth-service.ts" not in architecture
   - Story claims library not in dependencies
   - Verify: anti_hallucination_findings populated
   - Verify: validation_passed=false

5. **Should-Fix Issues (GO with warnings):**
   - Story missing integration test scenarios
   - Story file paths inconsistent with project structure
   - Verify: validation_passed=true, score 6-8
   - Verify: should_fix_issues populated

**Test Fixtures:**
Create sample stories in `assets/`:
- `sample-story-perfect.md`
- `sample-story-missing-sections.md`
- `sample-story-placeholders.md`
- `sample-story-hallucinations.md`
- `sample-story-should-fix.md`

---

## Success Criteria

### You'll know you're done when:

**For apply-qa-fixes:**

1. ✅ Skill file created with compliant YAML frontmatter
2. ✅ All 6 workflow steps implemented
3. ✅ Priority rules deterministic and documented
4. ✅ Integration with James tested (routing, guardrails, telemetry)
5. ✅ Integration with Quinn tested (gate parsing, assessment loading)
6. ✅ Integration with bmad-commands tested (read_file, run_tests)
7. ✅ At least 3 test scenarios validated with sample fixtures
8. ✅ Documentation complete (references/templates.md, priority-rules.md, examples.md)
9. ✅ Telemetry emits on completion
10. ✅ `/james apply-qa-fixes task-007` works end-to-end

**For validate-story:**

1. ✅ Skill file created with compliant YAML frontmatter
2. ✅ All 10 validation steps implemented
3. ✅ GO/NO-GO decision logic clear and tested
4. ✅ Validation report format structured and actionable
5. ✅ Anti-hallucination verification robust
6. ✅ Integration with story creation workflow tested
7. ✅ At least 3 test scenarios validated (GO, NO-GO, warnings)
8. ✅ Documentation complete (references/validation-checklist.md, examples.md)
9. ✅ Telemetry emits on completion
10. ✅ `/validate-story {path}` works end-to-end

---

## Reference Materials

### Essential Reading (in this order):

1. **Architecture Foundations:**
   - `docs/3-layer-architecture-for-skills.md` - Understand 3-layer architecture
   - `docs/skill-refactoring-template.md` - Follow skill structure template
   - `docs/architecture-claude-code-compliance.md` - Compliance requirements

2. **BMAD Originals (what we're migrating):**
   - `BMAD/.bmad-core/tasks/apply-qa-fixes.md` - Original apply-qa-fixes workflow
   - `BMAD/.bmad-core/tasks/validate-next-story.md` - Original validation workflow
   - `BMAD/.bmad-core/agents/qa.md` - Original Quinn persona
   - `BMAD/.bmad-core/agents/dev.md` - Original James persona

3. **Current Implementations (what exists now):**
   - `.claude/agents/james-developer-v2.md` - James subagent (your integration point)
   - `.claude/agents/quinn-quality.md` - Quinn subagent (your integration point)
   - `.claude/skills/quality/review-task/SKILL.md` - Quinn's review orchestrator
   - `.claude/skills/development/fix-issue/SKILL.md` - Generic bug fixing (similar but different)
   - `.claude/skills/bmad-commands/SKILL.md` - Primitives you'll use

4. **Quality Layer Examples:**
   - `.claude/skills/quality/risk-profile/SKILL.md` - Example quality skill
   - `.claude/skills/quality/quality-gate/SKILL.md` - Gate decision logic
   - `.claude/quality/gates/` - Sample gate files (if any exist)
   - `.claude/quality/assessments/` - Sample assessment reports (if any exist)

5. **Migration Analysis:**
   - `docs/developer-agent-migration-analysis.md` - Completed migration analysis (just created)

---

## Suggested Implementation Order

### Session Flow (4-6 hours):

**Phase 1: Setup & Understanding (30 min)**
1. Read this handoff document thoroughly
2. Review 3-layer architecture docs
3. Scan BMAD originals to understand workflows
4. Review current James and Quinn implementations

**Phase 2: Create apply-qa-fixes skill (2-3 hours)**
1. Create directory structure
2. Write SKILL.md with YAML frontmatter and 6-step workflow
3. Create references/templates.md (gate schema, input/output formats)
4. Create references/priority-rules.md (deterministic priority logic)
5. Create references/examples.md (usage examples)
6. Create test fixtures in assets/
7. Test integration with James (routing, guardrails)
8. Test integration with Quinn (gate parsing)
9. Test with bmad-commands (read_file, run_tests)
10. Validate with at least 3 test scenarios

**Phase 3: Create validate-story skill (1.5-2 hours)**
1. Create directory structure
2. Write SKILL.md with YAML frontmatter and 10-step workflow
3. Create references/templates.md (validation report format)
4. Create references/validation-checklist.md (10 steps detailed)
5. Create references/examples.md (GO/NO-GO examples)
6. Create test fixtures in assets/
7. Test validation logic with sample stories
8. Validate with at least 3 test scenarios (GO, NO-GO, warnings)

**Phase 4: Integration & Slash Commands (30 min)**
1. Update `.claude/commands/james.md` to support `apply-qa-fixes`
2. Create `.claude/commands/validate-story.md`
3. Test end-to-end workflows:
   - Story creation → Validation → Implementation → QA Review → Apply Fixes → Re-review
4. Document any issues or edge cases

**Phase 5: Documentation & Handoff (30 min)**
1. Update `docs/developer-agent-migration-analysis.md` to mark apply-qa-fixes and validate-story as ✅
2. Create usage guide for both skills
3. Document any deviations from BMAD originals (with rationale)
4. Create handoff summary for Session 8

---

## Potential Challenges & Solutions

### Challenge 1: Quality Gate Schema Compatibility
**Problem:** BMAD gates might have different schema than our current .claude/quality/ format
**Solution:**
- Normalize during parsing in apply-qa-fixes
- Document schema differences in references/templates.md
- Ensure backward compatibility

### Challenge 2: Anti-Hallucination Verification Complexity
**Problem:** Verifying claims against architecture docs can be complex
**Solution:**
- Start simple: Check if referenced files exist
- Check if claimed libraries are in package.json/dependencies
- Check if architectural patterns mentioned are in architecture docs
- Flag unverifiable claims for manual review
- Don't block on low-confidence findings

### Challenge 3: Fix Priority Conflicts
**Problem:** Multiple high-severity issues might conflict
**Solution:**
- Follow deterministic priority rules strictly
- Security > Performance > Reliability > Maintainability
- Within same category, use issue ID alphabetical order
- Document all priority decisions in telemetry

### Challenge 4: Guardrail Violations During Fixes
**Problem:** Applying all QA fixes might exceed guardrails (max files, diff lines)
**Solution:**
- Pre-calculate impact before starting fixes
- If would exceed guardrails, escalate to user:
  "This gate has 12 high-severity issues requiring 15 file changes (guardrail: 10 files).
   Recommend: Break into multiple fix sessions or override guardrail?"
- Allow user to prioritize subset of fixes

### Challenge 5: Story Template Evolution
**Problem:** Story template might change over time
**Solution:**
- Store template version in story frontmatter
- validate-story should load template version used for story creation
- Warn if validating against newer template version
- Don't fail validation on template version mismatch

---

## Questions to Consider

As you implement, think about:

1. **apply-qa-fixes:**
   - Should James auto-invoke apply-qa-fixes after a FAIL/CONCERNS gate, or wait for user?
   - Should fixes be applied as single commit or multiple commits per issue?
   - How to handle fixes that require architectural changes (exceed complexity)?
   - Should re-review be automatic or manual after fixes?

2. **validate-story:**
   - Should validation be mandatory before implementation, or optional?
   - Should James refuse to implement NO-GO stories, or just warn?
   - How strict should anti-hallucination checks be (block vs. warn)?
   - Should validation reports be versioned (re-validation after fixes)?

**Document your decisions** in the skill references/ files.

---

## Expected Outputs

At the end of this session, you should have:

### Files Created:
```
.claude/skills/development/apply-qa-fixes/
  ├── SKILL.md (200-300 lines)
  ├── references/
  │   ├── templates.md (gate schema, I/O formats)
  │   ├── priority-rules.md (deterministic logic)
  │   └── examples.md (3-5 usage examples)
  └── assets/
      ├── sample-gate-high-severity.yaml
      ├── sample-gate-nfr-failures.yaml
      └── sample-gate-coverage-gaps.yaml

.claude/skills/planning/validate-story/
  ├── SKILL.md (300-400 lines)
  ├── references/
  │   ├── templates.md (validation report format)
  │   ├── validation-checklist.md (10 steps detailed)
  │   └── examples.md (GO/NO-GO examples)
  └── assets/
      ├── sample-story-perfect.md
      ├── sample-story-missing-sections.md
      └── sample-story-hallucinations.md

.claude/commands/validate-story.md (routing command)

Updated:
  .claude/commands/james.md (add apply-qa-fixes command)
  docs/developer-agent-migration-analysis.md (mark complete)
```

### Documentation:
- Usage guide for both skills
- Integration examples
- Test results summary
- Deviations from BMAD (if any) with rationale
- Session 8 handoff summary

---

## Success Metrics

You'll know the migration is complete when:

1. ✅ **Quality ↔ Development feedback loop works:**
   - Quinn reviews → Creates gate with issues → James applies fixes → Quinn re-reviews → PASS

2. ✅ **Story validation prevents bad implementations:**
   - NO-GO stories blocked with clear issues → Fixed → Re-validated → GO → Implementation

3. ✅ **3-layer architecture maintained:**
   - Both skills have compliant YAML frontmatter
   - Telemetry emitted on completion
   - Integration with James/Quinn subagents tested
   - Primitives used for file operations

4. ✅ **BMAD functionality preserved:**
   - apply-qa-fixes: All priority rules from BMAD original
   - validate-story: All 10 validation steps from BMAD original
   - No regressions in quality workflows

5. ✅ **End-to-end validation:**
   - Create story → Validate (GO) → Implement → Review (CONCERNS) → Apply fixes → Re-review (PASS)
   - Create story → Validate (NO-GO) → Fix story → Re-validate (GO) → Implement

---

## Final Notes

**Philosophy:**
These skills complete the Quality-Development integration. They embody BMAD's core principle: **systematic quality assessment with actionable feedback loops**.

**Quality Gates = Advisory, Not Blocking:**
Remember Quinn's philosophy from BMAD: Quality gates are advisory. Teams choose their quality bar. These skills provide data for informed decisions, not arbitrary blocks.

**Telemetry = Learning:**
Emit detailed telemetry for both skills. Over time, we'll learn:
- Which issues are most common in QA gates?
- Which validation checks catch the most problems?
- What's the average time to fix QA issues?
- How does validation score correlate with implementation success?

**Iterate and Improve:**
These are V1 implementations. After real-world usage:
- Refine priority rules based on feedback
- Add validation checks based on common story problems
- Optimize workflows for speed
- Enhance error handling

---

## Ready to Start?

**Your mission:** Implement apply-qa-fixes and validate-story skills following BMAD workflows, 3-layer architecture, and integration with James/Quinn.

**Remember:**
- Follow the architecture (YAML frontmatter, inputs/outputs, telemetry)
- Use bmad-commands primitives
- Test with sample fixtures
- Document decisions and deviations
- Keep Quinn's advisory philosophy

**Good luck! 🚀**

---

## Quick Start Command

To begin Session 7, use this prompt:

```
I'm ready to implement the apply-qa-fixes and validate-story skills for BMAD
Enhanced. I've read the SESSION-7-HANDOFF-QA-WORKFLOW-ENHANCEMENT.md document.

Let's start with apply-qa-fixes skill. Please:

1. Create the directory structure for .claude/skills/development/apply-qa-fixes/
2. Help me write the SKILL.md with proper YAML frontmatter
3. Implement the 6-step workflow from the handoff doc
4. Create the references/ files (templates.md, priority-rules.md, examples.md)
5. Create sample fixtures for testing

I understand this integrates with:
- James (james-developer-v2.md) for routing and guardrails
- Quinn (quinn-quality.md) for gate parsing
- bmad-commands for primitives (read_file, run_tests)

Let's build this following 3-layer architecture principles.
```
