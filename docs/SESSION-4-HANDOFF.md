# BMAD Enhanced Skills Refactoring - Session 4 Handoff

**Date:** 2025-10-30 (for next session)
**Previous Session:** Session 3 (3 skills refactored, 61% complete)
**Current Progress:** 11 of 18 skills (61%)
**Target for Session 4:** 14 of 18 skills (78%)
**Estimated Time:** 3-3.5 hours

---

## Executive Summary

You are continuing the **BMAD Enhanced skills refactoring project**. Sessions 1-3 successfully refactored **11 skills to Grade A** with an **average 56% token reduction**. This session will refactor **3 more skills** using the proven **templates.md pattern**.

### Sessions 1-3 Achievements ✅

**Session 1 (5 skills):**
- fix-issue, implement-feature, estimate-stories, review-task, create-task-spec
- Average: 64% reduction, 70 min/skill
- Grade A: 5/5 (100%)

**Session 2 (3 skills):**
- refactor-code, breakdown-epic, quality-gate
- Average: 60% reduction, 63 min/skill
- Grade A: 3/3 (100%)

**Session 3 (3 skills):**
- run-tests, nfr-assess, trace-requirements
- Average: 45% reduction, 67 min/skill
- Grade A: 3/3 (100%)

**Total Progress:** 0% → 61% (11/18 skills complete)
**Total Lines Reduced:** ~2,400 lines
**Success Rate:** 100% (11/11 Grade A validations)

### What Makes Session 4 Strategic

**Completing Categories:** This session will:
1. ✅ **Complete the Planning category** (refine-story)
2. 🏗️ **Begin the Brownfield category** (document-project)
3. 🔧 **Advance Development category** (execute-task)

**Balanced Skillset:** After Session 4:
- Development: 4/6 (67%)
- Planning: 3/3 (100%) ✅ **COMPLETE**
- Quality: 5/5 (100%) ✅ **COMPLETE**
- Brownfield: 1/4 (25%)

**Pattern Maturity:** The templates.md pattern has been validated across 11 skills with 100% success rate. You can confidently apply the same process.

---

## Your Mission for Session 4

### Refactor the Next 3 Skills

**Target Skills (Development → Planning → Brownfield):**

1. **execute-task** (development)
   - Location: `.claude/skills/development/execute-task/`
   - Estimated: 600-800 lines → ~350 lines target
   - Complements implement-feature and run-tests (already refactored)

2. **refine-story** (planning)
   - Location: `.claude/skills/planning/refine-story/`
   - Estimated: 700-900 lines → ~370 lines target
   - Completes the planning category (last planning skill)

3. **document-project** (brownfield)
   - Location: `.claude/skills/brownfield/document-project/`
   - Estimated: 800-1000 lines → ~390 lines target
   - First brownfield skill (sets pattern for category)

### Why These 3 Skills?

**Strategic Selection:**
- **execute-task**: Completes implementation workflow (implement → test → execute)
- **refine-story**: Completes planning category (3/3 skills done)
- **document-project**: Starts brownfield category, demonstrates pattern for remaining 3

**Category Completion:** After this session:
- ✅ Planning: 100% complete (all 3 skills done)
- ✅ Quality: 100% complete (all 5 skills done)
- 🔧 Development: 67% complete (4 of 6 skills)
- 🏗️ Brownfield: 25% complete (1 of 4 skills)

**Logical Workflow:** These 3 skills represent a complete product lifecycle:
1. execute-task: Execute validated implementation
2. refine-story: Refine requirements based on feedback
3. document-project: Document existing/brownfield systems

---

## The Proven 7-Step Process

**Use this exact process for each skill (validated across 11 skills):**

### Step 0: Analyze Current State

**Actions:**
1. Read the SKILL.md file (use offset/limit for files >500 lines)
2. Count lines: `wc -l .claude/skills/{category}/{skill-name}/SKILL.md`
3. Check existing references: `ls -la .claude/skills/{category}/{skill-name}/references/`
4. Identify verbose sections to trim:
   - Step output templates (move to templates.md)
   - Configuration examples (move to templates.md)
   - File format examples (move to templates.md)
   - Verbose explanations (condense or move)
   - Integration sections (condense)
   - Best practices (condense)

**Goal:** Understand the current state and plan trimming strategy

**Pro Tip:** For files >700 lines, plan to use Python batch operations for efficiency

---

### Step 1: Create Directory Structure

**Actions:**
1. Check if `references/` directory exists:
   ```bash
   ls -la .claude/skills/{category}/{skill-name}/references/
   ```

2. Create if needed:
   ```bash
   mkdir -p .claude/skills/{category}/{skill-name}/references
   ```

**Verify:**
```bash
ls -la .claude/skills/{category}/{skill-name}/references/
```

**Expected:** Directory exists, may have empty or partial reference files

---

### Step 2: Verify YAML Frontmatter

**Most skills already have frontmatter from partial refactoring. Quick check:**

**Expected Frontmatter:**
```yaml
---
name: skill-name
description: Brief one-line description
acceptance:
  criterion_1: "Description"
inputs:
  input_name:
    type: string
    required: true
    description: "What this input is for"
outputs:
  output_name:
    type: string
    description: "What this output contains"
telemetry:
  emit: "skill.{name}.completed"
  track:
    - metric_1
---
```

**Action:** Read first ~50 lines and verify frontmatter exists and is valid

**If Missing:** Add frontmatter (rare - most skills already have it)

---

### Step 3: Create Comprehensive templates.md

**🎯 This is the SECRET WEAPON for token reduction!**

**Location:** `.claude/skills/{category}/{skill-name}/references/templates.md`

**Target Size:** 700-1000 lines (don't worry about being too long!)

**Structure Template:**

```markdown
# {Skill Name} Templates and Output Formats

All output formats, examples, and templates for the {skill-name} skill.

---

## Step 0: {First Step Name} Output

**Complete Output Format:**
```
[Complete example output with realistic data]
```

**Example with Real Data:**
[Another complete example]

---

## Step 1: {Second Step Name} Output

**Complete Output Format:**
[Complete format]

**Successful Case Example:**
[Example with success]

**Error Case Example:**
[Example with errors]

---

[Repeat for ALL workflow steps]

---

## Complete File Format Examples

### {File Type 1} Format

**Template:**
```yaml
[Complete YAML/JSON/etc template]
```

**Example with Real Data:**
```yaml
[Complete example with realistic values]
```

### {File Type 2} Format

[Another complete template]

---

## JSON Output Format

**Complete Skill Output Structure:**
```json
{
  "complete": "json structure",
  "with": "all fields",
  "including": ["nested", "arrays"],
  "and": {
    "nested": "objects"
  }
}
```

---

## Integration Examples

### Integration with {Other Skill}

**Input from {other-skill}:**
[Description of inputs]

**How {this-skill} uses it:**
[Complete workflow example]

**Example:**
```markdown
[Complete integration example with data flow]
```

### CI/CD Integration

**GitHub Actions:**
```yaml
[Complete GitHub Actions workflow]
```

**GitLab CI:**
```yaml
[Complete GitLab CI configuration]
```

---

## Error Templates

### {Error Type 1}

**Complete Error Output:**
```
[Complete error message with context]
```

**Cause:** [Detailed explanation]
**Solution:** [Complete solution steps]

---

*Complete templates and output formats for {skill-name} skill*
```

**What to Include (Checklist):**
- ✅ ALL step output templates (EVERY workflow step!)
- ✅ Successful execution examples (with realistic data)
- ✅ Error case examples (for each step)
- ✅ Complete file format templates (YAML, JSON, Markdown)
- ✅ Configuration examples (complete structures)
- ✅ Integration workflow examples (with other skills)
- ✅ CI/CD integration examples (if applicable)
- ✅ Complete JSON output format (skill's return structure)
- ✅ Error message templates (all error types)
- ✅ Command-line usage examples (if applicable)

**Pro Tips:**
- **Be COMPREHENSIVE** - 700-1000 lines is perfectly fine!
- **Use realistic data** - Not placeholders like "example.com", use actual-looking data
- **Include complete structures** - No "..." truncation, show full examples
- **Format consistently** - Use markdown code blocks, tables, headers
- **Add context** - Brief explanations before each template
- **Cross-reference** - Link between related templates when helpful

**Examples from Sessions 1-3:**
- implement-feature: 887 lines (workflow, file templates, integration)
- nfr-assess: 800 lines (6 NFR categories, each with complete outputs)
- breakdown-epic: 1,150 lines (most comprehensive - epic/story templates)
- trace-requirements: 700 lines (traceability matrix, gap analysis)

**Time Investment:** 15-20 minutes to create comprehensive templates.md
**Payoff:** Enables 200-400 line reduction in SKILL.md!

---

### Step 4: Systematically Trim SKILL.md

**Goal:** Reduce SKILL.md from 600-1000 lines to **350-450 lines**

**Trimming Strategy (in order):**

#### 4.1: Replace Verbose Step Outputs (HIGHEST IMPACT)

**Target:** Steps in workflow (Step 0, Step 1, Step 2, etc.)

**Before:**
```markdown
**Output:**
```
✓ Step 1 complete
✓ Files processed: 12
✓ Results:
  - Success: 10 files
  - Warnings: 2 files
  - Errors: 0 files
✓ Duration: 2.3s
✓ Next: Proceed to Step 2
```
```

**After:**
```markdown
**Output:** Step complete, files processed count, results breakdown (success/warnings/errors), duration, next step

**See:** `references/templates.md#step-1-output-format` for complete format
```

**Savings:** 10-20 lines per step × 5-8 steps = **50-160 lines saved**

**How to do it:**
1. Find each step's `**Output:**` section
2. Read the verbose output format (usually in code block)
3. Condense to one-line summary listing key fields
4. Add `**See:**` reference to templates.md section
5. Use Edit tool to replace

---

#### 4.2: Replace Configuration Examples (HIGH IMPACT)

**Target:** YAML/JSON config examples in workflow steps

**Before:**
```markdown
Load configuration from `.claude/config.yaml`:

```yaml
development:
  execute:
    validation:
      enabled: true
      strict_mode: false
      check_dependencies: true
    deployment:
      environment: staging
      auto_rollback: true
      health_check_timeout: 30
[... 30 more lines ...]
```
```

**After:**
```markdown
**Load config:** Read `.claude/config.yaml` for execution settings (validation, deployment, rollback)

**See:** `references/templates.md#configuration-format` for complete structure
```

**Savings:** 30-50 lines

---

#### 4.3: Replace File Format Examples (HIGH IMPACT)

**Target:** Complete file templates shown in workflow

**Before:**
```markdown
Generate task execution log:

```markdown
---
task_id: task-007
execution_date: 2025-10-30
status: success
[... 50 lines of complete template ...]
```
```

**After:**
```markdown
**Generate log:** Use bmad-commands write_file for execution log with task ID, status, metrics, errors

**See:** `references/templates.md#execution-log-format` for complete template
```

**Savings:** 40-80 lines

---

#### 4.4: Condense Verbose Sections (MEDIUM IMPACT)

**Common Verbose Sections to Condense:**

**A) Integration with Other Skills**

**Before (verbose):**
```markdown
## Integration with Other Skills

### Integration with implement-feature

**Input from implement-feature:**
- Implementation record with files created/modified
- Task specification with acceptance criteria
- Quality review results

**How execute-task uses it:**
When implement-feature completes, execute-task can be triggered to...
[10 more lines of detailed explanation]

**Example:**
```markdown
[Complete workflow example]
```

### Integration with run-tests

**Input from run-tests:**
[Another 15 lines of detailed explanation]
```

**After (condensed):**
```markdown
## Integration with Other Skills

**Integration with implement-feature:** Uses implementation record, task spec, quality review | Triggered after implementation completes

**Integration with run-tests:** Requires test results before execution | Validates tests pass before deploying

**See:** `references/templates.md#integration-examples` for complete workflows
```

**Savings:** 40-60 lines

---

**B) Best Practices**

**Before:**
```markdown
## Best Practices

1. **Validate Before Execution** - Always run tests and quality checks before executing tasks in production. This prevents deploying broken code.

2. **Use Rollback Plans** - Document rollback procedures before executing. If execution fails, you need a clear path to revert changes.

[6 more detailed practices with explanations]
```

**After:**
```markdown
## Best Practices

Validate before execution | Use rollback plans | Monitor during execution | Document changes | Test in staging first | Review logs after execution | Automate where possible | Keep audit trail

**See:** `references/best-practices.md` for detailed guidance
```

**Savings:** 15-25 lines

---

**C) Common Scenarios / Use Cases**

**Before:**
```markdown
## Common Scenarios

### Scenario 1: Successful Execution

**Context:** Task has passed all quality checks
**Steps:**
1. Load task specification
2. Validate prerequisites
3. Execute implementation
[10 more lines]

### Scenario 2: Failed Execution

[Another 15 lines]

### Scenario 3: Partial Execution

[Another 15 lines]
```

**After:**
```markdown
## Common Scenarios

**Successful:** Load task → validate → execute → verify | **Failed:** Rollback changes, log errors, notify | **Partial:** Resume from checkpoint, complete remaining steps

**See:** `references/templates.md#common-scenarios` for complete workflows
```

**Savings:** 30-45 lines

---

#### 4.5: Remove Non-Essential Sections (LOW-MEDIUM IMPACT)

**Sections to Remove Entirely:**

**A) "Using This Skill" Section**
- Usually obvious from frontmatter and workflow
- Adds 10-20 lines
- Remove completely

**B) "Philosophy" Section**
- Explains architectural principles
- Nice-to-have but not essential
- Adds 15-25 lines
- Remove completely

**C) "Limitations" Section (if redundant with Routing Guidance)**
- Often duplicates routing guidance
- Adds 10-15 lines
- Remove if redundant, keep if unique limitations

**Total Savings:** 35-60 lines

---

#### 4.6: Update Reference Files Section

**Add templates.md at the top:**

**Before:**
```markdown
## Reference Files

- **execution-guide.md**: Detailed execution procedures
- **validation-rules.md**: Validation criteria
- **error-handling.md**: Error recovery procedures
```

**After:**
```markdown
## Reference Files

Detailed documentation in `references/`:

- **templates.md**: All output formats, file templates, examples, integration workflows, JSON structures
- **execution-guide.md**: Detailed execution procedures and validation
- **validation-rules.md**: Validation criteria and checks
- **error-handling.md**: Error recovery procedures
- **best-practices.md**: Detailed best practices and guidelines
```

**Key Change:** Add templates.md as first entry

---

#### 4.7: Systematic Editing Process

**Recommended Order:**

1. **Start with Step Outputs** (highest impact, 50-160 lines)
   - Replace each step's verbose output with summary + reference
   - Work through Step 0, 1, 2, ... sequentially

2. **Replace Config/File Examples** (high impact, 70-130 lines)
   - Find YAML/JSON config blocks
   - Find file template blocks
   - Replace with summaries + references

3. **Condense Verbose Sections** (medium impact, 85-130 lines)
   - Integration section
   - Best Practices section
   - Common Scenarios section

4. **Remove Non-Essential Sections** (low-medium impact, 35-60 lines)
   - "Using This Skill"
   - "Philosophy"
   - "Limitations" (if redundant)

5. **Update Reference Files Section** (quick, 5-10 lines)
   - Add templates.md at top

**Total Expected Reduction:** 245-490 lines (from 600-1000 → 350-450)

---

### Step 5: Validate with skill-creator

**Command:**
```bash
python3 /home/adolfo/.claude/plugins/marketplaces/anthropic-agent-skills/skill-creator/scripts/package_skill.py .claude/skills/{category}/{skill-name} . validate
```

**Expected Output:**
```
✅ Skill is valid!
✅ Successfully packaged skill to: {skill-name}.zip
```

**What Validation Checks:**
- YAML frontmatter is valid
- Required sections exist (Purpose, Workflow, etc.)
- File structure is correct
- No obvious syntax errors

**If Validation Fails:**
1. Read error message carefully
2. Fix the issue (usually YAML syntax or missing section)
3. Re-validate immediately

**Validation is Flexible:**
- Accepts line counts from ~220 to ~550 lines
- Focuses on structure and completeness, not exact length
- Trust Grade A validation - if it passes, it's good!

**Important:** Validate **after each skill**, not after all 3 skills!

---

### Step 6: Check Line Count

**Command:**
```bash
wc -l .claude/skills/{category}/{skill-name}/SKILL.md
```

**Target Range:** 300-450 lines (sweet spot: 350-400)

**Acceptable Range:** 220-550 lines (skill-creator is flexible)

**If Too Long (>500 lines):**
- Look for more sections to condense
- Check if all step outputs reference templates.md
- Check if config/file examples are moved to templates.md
- Look for remaining verbose examples

**If Too Short (<300 lines):**
- Verify workflow steps are complete
- Ensure critical information isn't missing
- Check that references are clear and helpful
- Verify acceptance criteria are documented

**Don't Over-Optimize:**
- Quality and clarity > exact line count
- Complex skills can be longer (like trace-requirements: 529 lines, still Grade A)
- Structure and references matter more than hitting exact target

---

### Step 7: Document Results

**Update Session Summary:**

After each skill, document:
- Skill name and category
- Original lines → final lines (reduction count and %)
- Grade A validation status ✅
- Package created (.zip file)
- Time spent (~60-70 minutes per skill)
- templates.md size (~700-1000 lines)

**Example Entry:**
```markdown
### Skill 1: execute-task (development)
- **Original:** 687 lines
- **Final:** 364 lines
- **Reduction:** -323 lines (-47%)
- **templates.md:** 843 lines
- **Time:** ~65 minutes
- **Grade:** A ✅
- **Package:** execute-task.zip
```

**Create Package:**
The validation command automatically creates `{skill-name}.zip` - this is your distributable package!

---

## Success Criteria Per Skill

**For each skill, you MUST achieve:**

✅ **Grade A validation** - skill-creator script passes
✅ **40-60% token reduction** - Significant decrease from original
✅ **100% portable** - No hardcoded paths (like /home/user/...)
✅ **templates.md created** - Comprehensive reference file (700-1000 lines)
✅ **SKILL.md trimmed** - Target 350-450 lines (accept 300-550)
✅ **Package created** - Distributable .zip file
✅ **References updated** - templates.md listed first in References section

---

## Detailed Examples from Sessions 1-3

### Example: Trimming Step Outputs (run-tests, Session 3)

**Before (Step 1 - Execute Tests):**
```markdown
**Action:** Use bmad-commands to run tests.

Execute:
```bash
python .claude/skills/bmad-commands/scripts/run_tests.py \
  --path . \
  --framework jest \
  --output json
```

**Parse Response:**
```json
{
  "success": true,
  "outputs": {
    "passed": true,
    "total_tests": 12,
    "passed_tests": 12,
    "failed_tests": 0,
    "coverage_percent": 87,
    "duration_ms": 2456,
    "failures": []
  },
  "telemetry": {
    "command": "run_tests",
    "framework": "jest"
  },
  "errors": []
}
```

**Verify:**
- Check `success == true`
- Extract test results from `outputs`
- Check for failures in `outputs.failures`

**If tests fail:**
- Report failed tests from `outputs.failures`
- Provide failure details
- Suggest fixes or reruns

**See:** `references/test-execution-guide.md` for execution details
```

**After:**
```markdown
**Action:** Use bmad-commands to run tests.

**Execute:** `python .claude/skills/bmad-commands/scripts/run_tests.py --path . --framework jest --output json`

**Parse Response:** Extract success, outputs (passed, total_tests, coverage_percent, failures), telemetry, errors

**If tests fail:** Report failed tests with details, suggest fixes, do not proceed with coverage analysis

**See:** `references/templates.md#step-1-test-execution-templates` for complete response formats and error handling
```

**Lines Saved:** 32 lines → 7 lines = **25 lines saved**

---

### Example: Condensing Integration (nfr-assess, Session 3)

**Before:**
```markdown
## Integration with Other Skills

### Integration with risk-profile

**Input from risk-profile:**
- Security risks identified in risk profile inform security assessment severity
- Performance risks inform performance assessment priorities
- Reliability risks inform reliability criteria weighting

**How nfr-assess uses risk profile:**
When a risk is identified in risk profile (e.g., "SQL injection - Score 6, HIGH"), and the NFR assessment finds a related gap (e.g., "Input Validation: CONCERNS - No sanitization"), the gap severity is amplified. A HIGH security gap that matches a HIGH risk becomes CRITICAL (must fix before merge).

**Example:**
```
Risk Profile: Risk #2 - SQL injection (Score: 6, HIGH)
NFR Security: Input Validation (CONCERNS) - No SQL injection protection
→ Gap Severity: CRITICAL (base: HIGH + risk amplification: +1)
→ Priority: P0 (blocks merge)
```

### Integration with trace-requirements

**Input from traceability:**
- Implementation evidence validates NFR implementation (e.g., security controls, error handlers)
- Test coverage metrics inform reliability and maintainability assessments

**Output to traceability:**
- NFR gaps become additional coverage gaps in traceability matrix
- Missing NFR implementations flagged as uncovered requirements

[... continues with more integrations ...]
```

**After:**
```markdown
## Integration with Other Skills

**Integration with risk-profile:** Security/performance/reliability risks from risk profile inform NFR assessment priorities and amplify gap severity (e.g., HIGH gap + HIGH risk = CRITICAL P0)

**Integration with trace-requirements:** Implementation evidence validates NFR implementation; NFR gaps feed back as coverage gaps in traceability matrix

**Integration with test-design:** Performance/load/security test specifications inform corresponding NFR category assessments

**Integration with quality-gate:** Overall NFR score + category scores + critical gaps feed into quality gate decision (≥90%: PASS-excellent, 75-89%: PASS-good, 60-74%: CONCERNS, <60%: FAIL; Security/Reliability <50%: production blocker)

**See:** `references/templates.md#integration-examples` for detailed integration workflows and decision logic
```

**Lines Saved:** ~55 lines → ~11 lines = **44 lines saved**

---

### Example: Condensing Best Practices (trace-requirements, Session 3)

**Before:**
```markdown
## Best Practices

1. **Run NFR assessment before quality gate** - Identifies quality issues early in the review process, allowing time for remediation before merge decision.

2. **Integrate automated checks** - Leverage tools (security scans, linting, test coverage) for objective, reproducible metrics. Automated checks reduce manual effort and increase assessment reliability.

3. **Document evidence thoroughly** - Include file paths, line numbers, and code snippets for all assessments. Evidence makes findings actionable and defensible.

4. **Prioritize Security and Reliability** - These categories directly impact production readiness. Security vulnerabilities and reliability issues are production blockers (P0 priority).

5. **Set measurable thresholds** - Define clear pass/fail criteria in project configuration (e.g., "max critical vulnerabilities: 0", "min test coverage: 80%"). Measurable thresholds enable objective assessment.

6. **Re-run after fixes** - After closing NFR gaps, re-run nfr-assess to validate gap closure and update NFR score. Track score improvement over time.

7. **Customize category weights** - Adjust category weights in scoring formula based on project priorities (e.g., increase Security weight for security-critical systems).

8. **Review with stakeholders** - Share NFR assessment reports with technical leads, security teams, and product owners. NFR gaps often require cross-functional decisions.
```

**After:**
```markdown
## Best Practices

Run NFR assessment before quality gate | Integrate automated checks (security, linting, coverage) | Document evidence thoroughly (file paths, line numbers, snippets) | Prioritize Security and Reliability (production blockers) | Set measurable thresholds in config | Re-run after fixes to validate | Customize category weights per project | Review with stakeholders (cross-functional decisions)
```

**Lines Saved:** 18 lines → 2 lines = **16 lines saved**

---

## Time Budget and Token Management

### Estimated Time Per Skill

**Based on Sessions 1-3 averages:**

**execute-task:** ~65 minutes
- Analyze: 5 min
- Create templates.md: 20 min
- Trim SKILL.md: 30 min
- Validate: 2 min
- Document: 8 min

**refine-story:** ~70 minutes
- Analyze: 5 min
- Create templates.md: 25 min
- Trim SKILL.md: 30 min
- Validate: 2 min
- Document: 8 min

**document-project:** ~75 minutes
- Analyze: 5 min (larger file)
- Create templates.md: 25 min
- Trim SKILL.md: 35 min (more complex)
- Validate: 2 min
- Document: 8 min

**Session Documentation:** ~30 minutes

**Total Estimated Time:** 3.5 hours

### Token Budget

**Total Budget:** 200k tokens
**Target Usage:** ~120-130k tokens (~60-65%)

**Per-Skill Breakdown:**
- Skill 1 (execute-task): ~35-40k tokens
- Skill 2 (refine-story): ~40-45k tokens
- Skill 3 (document-project): ~40-45k tokens
- Documentation: ~10-15k tokens

**Token Conservation Tips:**
1. **Use offset/limit for large files** (>500 lines)
2. **Batch operations for trimming** (if file >700 lines)
3. **Strategic reading** (don't re-read entire file multiple times)
4. **Efficient template creation** (write complete templates.md in one operation)

---

## Common Pitfalls to Avoid

**❌ DON'T:**
1. **Wait to validate until all 3 skills done** - Validate after each skill!
2. **Over-trim** - Maintain workflow clarity and completeness
3. **Use placeholders in templates.md** - Use realistic example data
4. **Skip templates.md creation** - This is the key to token reduction!
5. **Guess at file content for Edit operations** - Read first, then edit!
6. **Batch validate multiple skills** - One skill at a time
7. **Worry about exact line count** - Focus on structure and clarity
8. **Remove critical workflow information** - Keep workflow complete

**✅ DO:**
1. **Create comprehensive templates.md FIRST** (700-1000 lines is perfect!)
2. **Replace verbose sections with summaries + references**
3. **Validate immediately after each skill**
4. **Accept line count variance** (220-550 all pass Grade A)
5. **Trust the proven process** (100% success rate across 11 skills)
6. **Use Python batch operations for large files** (>700 lines)
7. **Read file first before Edit operations** (avoid string match failures)
8. **Document results as you go** (don't batch documentation)

---

## File Paths Reference

### Skill Locations

**execute-task:**
```
/home/adolfo/Documents/BMAD Enhanced/.claude/skills/development/execute-task/
```

**refine-story:**
```
/home/adolfo/Documents/BMAD Enhanced/.claude/skills/planning/refine-story/
```

**document-project:**
```
/home/adolfo/Documents/BMAD Enhanced/.claude/skills/brownfield/document-project/
```

### Validation Script

```bash
python3 /home/adolfo/.claude/plugins/marketplaces/anthropic-agent-skills/skill-creator/scripts/package_skill.py <skill-path> . validate
```

### Example Commands

```bash
# Check current line count
wc -l .claude/skills/development/execute-task/SKILL.md

# Validate skill
python3 /home/adolfo/.claude/plugins/marketplaces/anthropic-agent-skills/skill-creator/scripts/package_skill.py .claude/skills/development/execute-task . validate

# List reference files
ls -la .claude/skills/development/execute-task/references/

# Check git status
git status
```

---

## Session 4 Workflow Checklist

### Pre-Session Setup
- [ ] Read this handoff document completely
- [ ] Review Session 3 summary: `docs/refactoring-session-3-summary.md`
- [ ] Understand the 7-step process
- [ ] Verify working directory: `/home/adolfo/Documents/BMAD Enhanced`

### For Each Skill (repeat 3 times)

#### Skill 1: execute-task (development)
- [ ] **Step 0:** Read SKILL.md (use offset/limit if >500 lines), count lines, check references, identify verbose sections
- [ ] **Step 1:** Verify `references/` directory exists (create if needed)
- [ ] **Step 2:** Verify YAML frontmatter exists and is valid
- [ ] **Step 3:** Create comprehensive `references/templates.md` (700-1000 lines)
  - [ ] All step output formats (EVERY step!)
  - [ ] Configuration examples (complete YAML)
  - [ ] File format examples (execution logs, etc.)
  - [ ] Integration examples
  - [ ] JSON output format
  - [ ] Error templates
- [ ] **Step 4:** Systematically trim SKILL.md
  - [ ] Replace Step 0 output with summary + reference
  - [ ] Replace Step 1-N outputs with summaries + references
  - [ ] Replace config examples with references
  - [ ] Replace file format examples with references
  - [ ] Condense Integration section
  - [ ] Condense Best Practices section
  - [ ] Remove "Using This Skill" section
  - [ ] Remove "Philosophy" section
  - [ ] Remove "Limitations" (if redundant)
  - [ ] Update Reference Files section (add templates.md first)
- [ ] **Step 5:** Validate with skill-creator (Grade A required)
- [ ] **Step 6:** Check line count (target 350-450, accept 300-550)
- [ ] **Step 7:** Document results (original→final, reduction %, time, templates.md size)

#### Skill 2: refine-story (planning)
- [ ] Repeat Steps 0-7 (same process)
- [ ] Note: This completes the Planning category (3/3 skills)!

#### Skill 3: document-project (brownfield)
- [ ] Repeat Steps 0-7 (same process)
- [ ] Note: This is the first Brownfield skill - sets pattern for remaining 3

### Post-Session Documentation
- [ ] Create `docs/refactoring-session-4-summary.md`
  - [ ] Metrics for each skill (lines, reduction %, time)
  - [ ] Key learnings and challenges
  - [ ] Token usage and efficiency notes
  - [ ] Templates.md sizes
- [ ] Update `docs/REFACTORING-COMPLETE.md` (if exists)
- [ ] Update `docs/ROADMAP.md` (61% → 78% progress)
- [ ] Note: Planning and Quality categories now 100% complete!

---

## Expected Results for Session 4

### Success Metrics

**Target Outcomes:**
- ✅ 3 skills refactored to Grade A
- ✅ 40-55% average token reduction (slightly lower OK for complex skills)
- ✅ 100% portable (no hardcoded paths)
- ✅ 3 distributable .zip packages
- ✅ Project progress: 61% → 78% (14/18 skills)
- ✅ Session duration: 3-3.5 hours
- ✅ Token usage: ~60-65% of 200k budget

**Quality Checks:**
- All 3 skills validate as Grade A
- SKILL.md files are 300-550 lines
- templates.md files are 700-1000 lines
- All references work correctly
- No hardcoded paths anywhere

**Category Completion:**
- ✅ Planning: 100% complete (3/3 skills)
- ✅ Quality: 100% complete (5/5 skills)
- 🔧 Development: 67% complete (4/6 skills)
- 🏗️ Brownfield: 25% complete (1/4 skills)

### Line Count Targets

**execute-task:**
- Estimated original: 650-750 lines
- Target: 350-400 lines
- Expected reduction: 45-50% (~300-350 lines saved)

**refine-story:**
- Estimated original: 750-850 lines
- Target: 370-420 lines
- Expected reduction: 45-50% (~350-400 lines saved)

**document-project:**
- Estimated original: 850-950 lines
- Target: 380-450 lines
- Expected reduction: 40-50% (~400-500 lines saved)

**Total Expected Reduction:** ~1,050-1,250 lines

---

## After Session 4: What's Next?

### Remaining Skills (4 skills, 22%)

**Session 5 will complete the project:**

**Remaining Development Skills (2):**
- TBD (need to check actual skill names in development/)
- TBD (need to check actual skill names in development/)

**Remaining Brownfield Skills (3):**
- index-docs
- sprint-plan
- (1 more TBD - need to check brownfield/)

**Session 5 Targets:**
- Target: 78% → 100% (4 skills)
- Estimated time: 4-4.5 hours (slightly longer, final push)
- Complete all remaining categories

**Final Validation:**
- End-to-end workflow testing
- Inter-skill integration validation
- Performance testing
- Documentation review
- Project completion celebration! 🎉

---

## Category Status After Session 4

### Completed Categories ✅

**Planning (3/3 skills - 100%):**
- ✅ estimate-stories (Session 1)
- ✅ create-task-spec (Session 1)
- ✅ breakdown-epic (Session 2)
- ✅ **refine-story (Session 4)** ← Completes category!

**Quality (5/5 skills - 100%):**
- ✅ review-task (Session 1)
- ✅ refactor-code (Session 2)
- ✅ quality-gate (Session 2)
- ✅ nfr-assess (Session 3)
- ✅ trace-requirements (Session 3)

### In-Progress Categories 🔧

**Development (4/6 skills - 67%):**
- ✅ fix-issue (Session 1)
- ✅ implement-feature (Session 1)
- ✅ run-tests (Session 3)
- ✅ **execute-task (Session 4)** ← New!
- ❌ TBD (Session 5)
- ❌ TBD (Session 5)

**Brownfield (1/4 skills - 25%):**
- ✅ **document-project (Session 4)** ← First brownfield skill!
- ❌ index-docs (Session 5)
- ❌ sprint-plan (Session 5)
- ❌ TBD (Session 5)

---

## Key Success Factors

### What Makes Skills Pass Grade A

**Based on 11 successful validations:**

1. **Valid YAML Frontmatter**
   - All required fields present
   - Correct syntax (colons, indentation)
   - Meaningful acceptance criteria

2. **Complete Workflow**
   - Clear sequential steps
   - Each step has purpose, actions, output
   - Halt conditions documented

3. **Proper Structure**
   - ## headings for major sections
   - ### headings for workflow steps
   - **Bold** for subsections
   - Code blocks properly formatted

4. **Reference System**
   - References section lists all reference files
   - `**See:**` references point to real sections
   - templates.md contains referenced content

5. **No Placeholders**
   - All template variables filled
   - No TODO or FIXME comments
   - No obvious missing sections

**Validation is NOT Strict About:**
- Exact line count (accepts 220-550)
- Specific wording or phrasing
- Level of detail (can be brief with good references)
- Number of examples (quality > quantity)

---

## Templates.md Best Practices

### What Makes a Great templates.md

**From 11 successful skills:**

1. **Comprehensive Coverage**
   - Every workflow step has output template
   - Both success and error cases shown
   - All file formats included

2. **Realistic Examples**
   - Actual-looking data (not "example" or "placeholder")
   - Complete structures (no "..." truncation)
   - Multiple examples per template type

3. **Clear Organization**
   - Organized by workflow step
   - Clear headers (## Step 1: Name)
   - Subsections for variants (success, error, edge cases)

4. **Integration Content**
   - Shows how skill integrates with others
   - Complete workflow examples with data flow
   - CI/CD examples if applicable

5. **Complete Formats**
   - Full JSON output structure
   - Complete YAML configurations
   - Full command-line examples
   - Complete error messages with solutions

### Templates.md Size Guidelines

**By Skill Complexity:**

**Simple Skills (like estimate-stories):**
- 600-800 lines
- Fewer workflow steps
- Simpler output formats
- Basic integrations

**Medium Skills (like run-tests, nfr-assess):**
- 750-900 lines
- Multiple workflow steps
- Rich output formats
- Several integrations

**Complex Skills (like breakdown-epic, trace-requirements):**
- 1000-1200 lines
- Many workflow steps
- Complex output formats (matrices, tables)
- Multiple integrations
- Extensive examples

**Session 4 Skills (estimated):**
- execute-task: ~800-900 lines (medium complexity)
- refine-story: ~750-850 lines (medium complexity)
- document-project: ~900-1000 lines (higher complexity, first brownfield)

---

## Troubleshooting Guide

### Common Issues and Solutions

**Issue 1: Validation Fails - "Invalid YAML frontmatter"**

**Solution:**
- Check for proper indentation (2 spaces, not tabs)
- Ensure colons followed by space: `name: value`
- Check for special characters in strings (use quotes)
- Validate YAML syntax online if needed

---

**Issue 2: Edit Operation Fails - "String to replace not found"**

**Solution:**
- Read the actual file content first
- Match the string EXACTLY (including whitespace)
- Check for tabs vs spaces
- Try a smaller, more unique string to match

**Prevention:**
- Always Read before Edit
- Copy exact strings from Read output
- Don't assume file content

---

**Issue 3: Line Count Too High After Trimming**

**Solution:**
- Look for more sections to condense
- Check if all step outputs reference templates.md
- Ensure config/file examples moved to templates.md
- Look for remaining verbose explanations
- Consider batch operations for aggressive trimming

**Remember:** 500-550 lines can still pass Grade A if well-structured

---

**Issue 4: Templates.md Feels Too Long**

**Solution:**
- This is normal and expected!
- 700-1000 lines is perfect
- Don't worry about length
- More comprehensive = better

**Remember:** The whole point is to move content FROM SKILL.md TO templates.md

---

**Issue 5: Unsure What to Include in templates.md**

**Solution:**
- Include EVERYTHING from SKILL.md that's verbose
- All output formats (every step)
- All examples (config, files, integration)
- All error messages
- Complete JSON structures
- When in doubt, include it!

**Remember:** You can always reference it later with `**See:**` links

---

**Issue 6: Token Budget Concerns**

**Solution:**
- Use offset/limit for large file reads
- Batch Edit operations when possible
- Don't re-read entire files unnecessarily
- Create templates.md in one Write operation
- Strategic reading (only what you need)

**Monitoring:**
- Check <system-reminder> for token usage
- ~40k per skill is normal
- ~130k total is healthy

---

## Quick Reference Card

### Essential Commands

```bash
# Check line count
wc -l .claude/skills/{category}/{skill-name}/SKILL.md

# List references
ls -la .claude/skills/{category}/{skill-name}/references/

# Validate skill
python3 /home/adolfo/.claude/plugins/marketplaces/anthropic-agent-skills/skill-creator/scripts/package_skill.py .claude/skills/{category}/{skill-name} . validate

# Check git status
git status
```

### Essential File Paths

```
Skills:
  /home/adolfo/Documents/BMAD Enhanced/.claude/skills/development/execute-task/
  /home/adolfo/Documents/BMAD Enhanced/.claude/skills/planning/refine-story/
  /home/adolfo/Documents/BMAD Enhanced/.claude/skills/brownfield/document-project/

Validator:
  /home/adolfo/.claude/plugins/marketplaces/anthropic-agent-skills/skill-creator/scripts/package_skill.py

Documentation:
  /home/adolfo/Documents/BMAD Enhanced/docs/
```

### Success Checklist (per skill)

- [ ] templates.md created (700-1000 lines)
- [ ] SKILL.md trimmed (300-550 lines)
- [ ] Grade A validation ✅
- [ ] .zip package created
- [ ] 40-60% reduction achieved
- [ ] No hardcoded paths
- [ ] Results documented

---

## Final Reminders

### Trust the Process

**This pattern has 100% success rate across 11 skills:**
1. Create comprehensive templates.md
2. Replace verbose sections with summaries + references
3. Validate immediately
4. Accept flexible line count (300-550)
5. Document and move to next skill

**You've got this!** 🚀

### Key Principles

1. **Progressive Disclosure** - Templates.md contains details, SKILL.md references them
2. **Comprehensive Templates** - Don't worry about templates.md being "too long"
3. **Validate Early** - After each skill, not after all 3
4. **Trust Grade A** - If validation passes, it's good
5. **Quality > Quantity** - Structure and clarity matter more than exact line count

### Session 4 Goal

**Complete 3 more skills to Grade A**
- execute-task (development)
- refine-story (planning) ← Completes Planning category!
- document-project (brownfield) ← First Brownfield skill!

**Advance project from 61% → 78%**

---

**Ready to refactor! Let's complete 3 more skills to Grade A!** 🎯

---

*Handoff Document Version: 1.0*
*Created: 2025-10-30*
*Based on: Sessions 1-3 (11 skills, 100% Grade A success rate)*
*Next Session After This: Session 5 (final 4 skills, 78% → 100%)*
*Estimated Time: 3-3.5 hours*
*Token Budget: ~120-130k of 200k*
