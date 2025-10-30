# BMAD Enhanced Skills Refactoring - Session 3 Handoff

**Date:** 2025-10-29
**Previous Session:** Session 2 (3 skills refactored, 44% complete)
**Current Progress:** 8 of 18 skills (44%)
**Target for Session 3:** 11 of 18 skills (61%)
**Estimated Time:** 3-3.5 hours

---

## Executive Summary

You are continuing the **BMAD Enhanced skills refactoring project**. Sessions 1 and 2 successfully refactored **8 skills to Grade A** with an **average 64% token reduction**. This session will refactor **3 more skills** using the proven **templates.md pattern**.

### Session 2 Achievements ✅

**Skills Completed:**
1. **refactor-code** (quality): 659 → 348 lines (47% reduction) - Grade A
2. **breakdown-epic** (planning): 1,066 → 265 lines (75% reduction) - Grade A
3. **quality-gate** (quality): 1,057 → 447 lines (58% reduction) - Grade A

**Total Progress:** 28% → 44% (8/18 skills complete)
**Session Duration:** ~3.2 hours
**Token Usage:** ~127k of 200k budget (63%)
**Packages Created:** refactor-code.zip, breakdown-epic.zip, quality-gate.zip

### What Makes This Session Unique

**Proven Pattern:** The templates.md approach has now been validated across **8 skills** (5 in Session 1, 3 in Session 2) with **100% Grade A success rate**. You can confidently follow the exact same 7-step process.

**Efficiency:** Session 2 averaged **~63 minutes per skill** (faster than Session 1's 70 minutes). The pattern is mature and efficient.

**Consistency:** All 8 completed skills achieved:
- ✅ Grade A validation
- ✅ 100% portability (no hardcoded paths)
- ✅ Progressive disclosure via templates.md
- ✅ Distributable .zip packages

---

## Your Mission for Session 3

### Refactor the Next 3 Skills

**Target Skills (Development + Quality focus):**

1. **run-tests** (development)
   - Location: `.claude/skills/development/run-tests/`
   - Estimated: 500-700 lines → ~350 lines target
   - Complements implement-feature (already refactored)

2. **nfr-assess** (quality)
   - Location: `.claude/skills/quality/nfr-assess/`
   - Estimated: 800-1,000 lines → ~370 lines target
   - Integrates with quality-gate (already refactored)

3. **trace-requirements** (quality)
   - Location: `.claude/skills/quality/trace-requirements/`
   - Estimated: 800-1,000 lines → ~370 lines target
   - Also integrates with quality-gate

### Why These 3 Skills?

- **run-tests**: Development skill, complements implement-feature and fix-issue (already refactored)
- **nfr-assess + trace-requirements**: Quality skills that integrate with quality-gate (just refactored in Session 2)
- **Logical grouping**: Complete the development testing workflow + quality assessment workflow

---

## The Proven 7-Step Process

**Use this exact process for each skill:**

### Step 0: Analyze Current State

**Actions:**
1. Read the `.md.old` file (if it exists) or current SKILL.md
2. Count lines: `wc -l`
3. Identify verbose sections:
   - Configuration examples (move to templates.md)
   - Step output templates (move to templates.md)
   - File format examples (move to templates.md)
   - Verbose explanations (condense or move)

**Goal:** Understand what needs to be trimmed

---

### Step 1: Create Directory Structure

**Actions:**
1. Create `references/` directory if it doesn't exist:
   ```bash
   mkdir -p .claude/skills/{category}/{skill-name}/references
   ```

**Verify:**
```bash
ls -la .claude/skills/{category}/{skill-name}/references
```

---

### Step 2: Add YAML Frontmatter (if missing)

**Template:**
```yaml
---
name: skill-name
description: Brief one-line description of what the skill does
acceptance:
  criterion_1: "Description of acceptance criterion"
  criterion_2: "Another acceptance criterion"
inputs:
  input_name:
    type: string|array|object
    required: true|false
    description: "What this input is for"
outputs:
  output_name:
    type: string|array|object|number
    description: "What this output contains"
telemetry:
  emit: "skill.{name}.completed"
  track:
    - metric_1
    - metric_2
---
```

**Note:** Most skills already have frontmatter from partial refactoring. Check first!

---

### Step 3: Create Comprehensive templates.md

**This is the SECRET WEAPON** 🎯

**Location:** `.claude/skills/{category}/{skill-name}/references/templates.md`

**Target Size:** 600-1,000 lines (don't worry about being too long!)

**Structure:**

```markdown
# {Skill Name} Templates and Output Formats

## Configuration Format

[Include complete YAML configuration example]

## Step 0: [Step Name]

### Output Template

[Complete example output for this step]

### Error Cases

[Error message templates]

## Step 1: [Step Name]

[Repeat for ALL workflow steps]

## Complete File Format Examples

### [File Type 1] Format

[Complete file template with realistic data]

### [File Type 2] Format

[Another complete template]

## JSON Output Format

[Complete JSON structure returned by skill]

## Integration Examples

### CI/CD Integration

[Example GitHub Actions, GitLab CI, etc.]

### Command Line Usage

[Example bmad-commands usage]
```

**What to Include:**
- ✅ ALL configuration examples (complete YAML)
- ✅ ALL step output templates (every single step!)
- ✅ ALL file format examples (complete structures)
- ✅ Error message templates
- ✅ Integration examples (CI/CD, commands)
- ✅ JSON output format (complete structure)

**Pro Tips:**
- Be COMPREHENSIVE - it's better to have too much than too little
- Use realistic example data (not placeholders)
- Include complete structures (not "..." truncation)
- Copy verbose sections directly from SKILL.md

---

### Step 4: Systematically Trim SKILL.md

**Goal:** Reduce SKILL.md from 500-1,000 lines to **330-390 lines** (target ~350)

**Trimming Techniques:**

#### 4.1: Replace Verbose Step Outputs

**Before:**
```markdown
### Step 2: Analyze Code

**Action:** Analyze the code for refactoring opportunities.

**Output:**
```json
{
  "status": "success",
  "findings": [
    {
      "type": "duplicate_code",
      "location": "src/utils/validation.ts:45-67",
      "suggestion": "Extract to shared function"
    }
  ]
}
```

Present findings to user...
```

**After:**
```markdown
### Step 2: Analyze Code

**Action:** Analyze the code for refactoring opportunities.

**Output:** Refactoring findings with type, location, suggestion, priority

**See:** `references/templates.md#step-2-analysis-output` for complete format
```

**Savings:** 15-25 lines per step × 5-8 steps = **75-200 lines saved**

---

#### 4.2: Replace Config Examples

**Before:**
```markdown
Configuration loaded from `.claude/config.yaml`:

```yaml
quality:
  gate:
    dimensions:
      risk_management:
        weight: 25
        threshold: 70
      test_coverage:
        weight: 20
        threshold: 80
[... 30 more lines ...]
```
```

**After:**
```markdown
**Load config:** Read `.claude/config.yaml` for quality settings (dimensions, weights, thresholds)

**See:** `references/templates.md#configuration-format` for complete structure
```

**Savings:** 30-50 lines

---

#### 4.3: Replace File Format Examples

**Before:**
```markdown
Story file format:

```markdown
---
id: story-auth-001
title: User can sign up for an account
[... 40 lines of complete example ...]
```
```

**After:**
```markdown
**Generate files:** Use bmad-commands write_file for each story and epic summary

**See:** `references/templates.md#story-file-format-template` for complete structure
```

**Savings:** 40-80 lines

---

#### 4.4: Condense Verbose Sections

**Safety Guarantees - Before:**
```markdown
## Safety Guarantees

This skill provides several important safety guarantees:

1. **Test Execution:** All tests must pass before any refactoring is applied. We run the full test suite to establish a baseline.

2. **Automatic Rollback:** If tests fail after a refactoring, the skill automatically rolls back the changes and logs the failure.

[... 10 more lines ...]
```

**Safety Guarantees - After:**
```markdown
## Safety Guarantees

Tests must pass before/after | Automatic rollback on failure | No behavioral changes | All changes logged | One refactoring at a time
```

**Savings:** 12-15 lines

---

**Integration - Before:**
```markdown
## Integration with BMAD Enhanced

This skill integrates seamlessly with other BMAD Enhanced skills:

- **With review-task:** Use quality findings to guide refactoring
- **With quality-gate:** Improve scores through targeted refactoring
[... 10 more lines ...]
```

**Integration - After:**
```markdown
## Integration

Use with review-task (quality findings → refactoring targets) and quality-gate (improve scores)

**See:** `references/templates.md#integration-examples` for CI/CD setup
```

**Savings:** 10-15 lines

---

#### 4.5: Remove Redundant Sections

**Remove entirely:**
- ❌ **"Using This Skill"** section (obvious from frontmatter and workflow steps)
- ❌ **"Philosophy"** section (too verbose, not essential to workflow)
- ❌ **"Limitations"** section (redundant with "Routing Guidance")

**Savings:** 20-40 lines total

---

#### 4.6: Update Reference Files Section

**Before:**
```markdown
## Reference Files

Additional documentation in `references/`:

- **refactoring-patterns.md**: Common patterns
- **risk-assessment-guide.md**: Risk levels
```

**After:**
```markdown
## Reference Files

Detailed documentation in `references/`:

- **templates.md**: All output formats, config examples, file templates
- **refactoring-patterns.md**: Common refactoring patterns and safety levels
- **risk-assessment-guide.md**: Risk assessment techniques
- **incremental-application-guide.md**: Step-by-step refactoring application
- **refactoring-log-template.md**: Complete log format and examples
```

---

### Step 5: Validate with skill-creator

**Command:**
```bash
python3 /home/adolfo/.claude/plugins/marketplaces/anthropic-agent-skills/skill-creator/scripts/package_skill.py .claude/skills/{category}/{skill-name} . validate
```

**Look for:**
```
✅ Skill is valid!
✅ Successfully packaged skill to: {skill-name}.zip
```

**If validation fails:**
1. Read error message carefully
2. Fix the issue (usually YAML syntax or missing sections)
3. Re-validate

**Target:** Grade A (anything that passes is Grade A)

---

### Step 6: Check Line Count

**Command:**
```bash
wc -l .claude/skills/{category}/{skill-name}/SKILL.md
```

**Target Range:** 300-450 lines (sweet spot: 330-390)

**If too long (>450 lines):**
- Look for more sections to condense
- Check if all step outputs reference templates.md
- Remove any remaining verbose examples

**If too short (<300 lines):**
- Verify workflow steps are complete
- Ensure critical information isn't missing
- Check that references are clear

---

### Step 7: Document Results

**Update Session Summary (at end):**
- Skill name and category
- Original lines → final lines (% reduction)
- Grade A validation ✅
- Package created (.zip file)
- Time spent (~60 minutes per skill)

**Create package:**
The validation command already creates `{skill-name}.zip` - this is your distributable package!

---

## Success Criteria Per Skill

**For each skill, you MUST achieve:**

✅ **Grade A validation** - skill-creator script passes
✅ **60%+ token reduction** - Significant decrease from original
✅ **100% portable** - No hardcoded paths or assumptions
✅ **templates.md created** - Comprehensive reference file (600-1000 lines)
✅ **SKILL.md trimmed** - Target 330-390 lines
✅ **Package created** - Distributable .zip file

---

## Example: Session 2 Results

### Skill 1: refactor-code
- **Original:** 659 lines (.md.old)
- **Final:** 348 lines (SKILL.md)
- **Reduction:** -311 lines (-47%)
- **templates.md:** 694 lines
- **Time:** ~60 minutes
- **Grade:** A ✅
- **Package:** refactor-code.zip

### Skill 2: breakdown-epic
- **Original:** 1,066 lines (.md.old)
- **Final:** 265 lines (SKILL.md)
- **Reduction:** -801 lines (-75%)
- **templates.md:** 1,150 lines
- **Time:** ~75 minutes
- **Grade:** A ✅
- **Package:** breakdown-epic.zip

### Skill 3: quality-gate
- **Original:** 1,057 lines (.md.old)
- **Final:** 447 lines (SKILL.md)
- **Reduction:** -610 lines (-58%)
- **templates.md:** 720 lines
- **Time:** ~55 minutes
- **Grade:** A ✅
- **Package:** quality-gate.zip

**Session 2 Average:** 60% reduction, 63 minutes/skill

---

## Key Learnings from Sessions 1 & 2

### What Worked Extremely Well ⭐

1. **templates.md Pattern is Gold**
   - Moving ALL output formats, examples, and templates to templates.md saved 200-300 lines per skill
   - Progressive disclosure: Templates loaded only when referenced
   - Enables complete information without bloating SKILL.md

2. **Systematic Trimming Process**
   - Following the 7-step process created predictable, repeatable results
   - 100% success rate across 8 skills
   - Validating after each skill (not batching) caught issues early

3. **"See: references/templates.md#section" Pattern**
   - Replacing verbose examples with brief description + reference
   - Saved 40-80 lines per skill
   - Maintains complete information accessibility

4. **Early and Frequent Validation**
   - Validate immediately after trimming each skill
   - Don't wait until all 3 are done
   - Trust Grade A validation (if it passes, it's good)

### Challenges and Solutions

**Challenge 1: String Match Failures**
- **Issue:** Edit tool failed with "String to replace not found"
- **Solution:** Read actual file sections first, then match strings exactly
- **Prevention:** Don't assume file content - read first, then edit

**Challenge 2: Variable Line Counts**
- **Issue:** Final line counts varied (265, 348, 447 all passed Grade A)
- **Solution:** Accept range of 300-450 lines (skill-creator is flexible)
- **Lesson:** Focus on workflow clarity, not exact line count

**Challenge 3: Partial Refactoring State**
- **Issue:** Some skills were already partially refactored (had YAML, some references, but no templates.md)
- **Solution:** Work with existing structure, add templates.md, trim further
- **Lesson:** Adapt to current state rather than starting from scratch

**Challenge 4: Empty Reference Files**
- **Issue:** quality-gate had 3 empty reference files from previous session
- **Solution:** Consolidated everything into templates.md
- **Lesson:** templates.md can be the primary/only reference file if needed

---

## Common Pitfalls to Avoid

❌ **DON'T:**
- Wait to validate all skills at end (validate after each!)
- Over-trim (breaking workflow clarity)
- Use placeholders in templates.md (use realistic data)
- Skip templates.md creation (this is the key to token reduction)
- Guess at file content for Edit operations (read first!)

✅ **DO:**
- Create comprehensive templates.md first (600-1000 lines is fine!)
- Replace verbose sections with "See: references/templates.md#section"
- Validate after each skill immediately
- Accept line count variance (265-447 all passed Grade A)
- Trust the process (it's proven across 8 skills)

---

## File Paths Reference

### Skill Locations
```
/home/adolfo/Documents/BMAD Enhanced/.claude/skills/development/run-tests/
/home/adolfo/Documents/BMAD Enhanced/.claude/skills/quality/nfr-assess/
/home/adolfo/Documents/BMAD Enhanced/.claude/skills/quality/trace-requirements/
```

### Validation Script
```
python3 /home/adolfo/.claude/plugins/marketplaces/anthropic-agent-skills/skill-creator/scripts/package_skill.py <skill-path> . validate
```

### Example Commands
```bash
# Check current line count
wc -l .claude/skills/development/run-tests/SKILL.md

# Validate skill
python3 /home/adolfo/.claude/plugins/marketplaces/anthropic-agent-skills/skill-creator/scripts/package_skill.py .claude/skills/development/run-tests . validate

# List reference files
ls -la .claude/skills/development/run-tests/references/
```

---

## Session 3 Workflow Checklist

### Pre-Session Setup
- [ ] Read this handoff document completely
- [ ] Review Session 2 summary: `docs/refactoring-session-2-summary.md`
- [ ] Understand the 7-step process

### For Each Skill (repeat 3 times)

#### Skill 1: run-tests
- [ ] **Step 0:** Read current SKILL.md, count lines, identify verbose sections
- [ ] **Step 1:** Create `references/` directory if needed
- [ ] **Step 2:** Verify YAML frontmatter (likely already exists)
- [ ] **Step 3:** Create comprehensive `references/templates.md` (600-800 lines)
- [ ] **Step 4:** Systematically trim SKILL.md using Edit tool
  - [ ] Replace Step 0 output with reference
  - [ ] Replace Step 1-N outputs with references
  - [ ] Replace config examples with reference
  - [ ] Replace file format examples with references
  - [ ] Condense Safety Guarantees section
  - [ ] Condense Integration section
  - [ ] Remove "Using This Skill" section
  - [ ] Remove "Philosophy" section
  - [ ] Remove "Limitations" section (if redundant)
  - [ ] Update Reference Files section
- [ ] **Step 5:** Validate with skill-creator (Grade A required)
- [ ] **Step 6:** Check line count (target 330-390, accept 300-450)
- [ ] **Step 7:** Document results (original→final lines, reduction %, time)

#### Skill 2: nfr-assess
- [ ] Repeat Steps 0-7

#### Skill 3: trace-requirements
- [ ] Repeat Steps 0-7

### Post-Session Documentation
- [ ] Create `docs/refactoring-session-3-summary.md`
- [ ] Update `docs/REFACTORING-COMPLETE.md` (44% → 61%)
- [ ] Update `docs/ROADMAP.md` if needed
- [ ] Create Session 4 handoff prompt (if continuing)

---

## Time Budget

**Total Budget:** 200k tokens
**Target Usage:** ~120-130k tokens (~60-65%)

**Per-Skill Breakdown:**
- Skill 1 (run-tests): ~35-40k tokens (~60 min)
- Skill 2 (nfr-assess): ~40-45k tokens (~65 min)
- Skill 3 (trace-requirements): ~35-40k tokens (~60 min)
- Documentation: ~10-15k tokens (~30 min)

**Total Estimated Time:** 3-3.5 hours (similar to Session 2)

---

## Templates.md Size Reference

**From Sessions 1 & 2:**

| Skill | templates.md Lines | Notes |
|-------|-------------------|-------|
| implement-feature | 887 | Complete workflow with examples |
| review-task | 678 | All review dimensions, templates |
| create-task-spec | 623 | Task formats, examples |
| refactor-code | 694 | Refactoring patterns, logs |
| breakdown-epic | 1,150 | Most comprehensive - epic/story templates |
| quality-gate | 720 | All dimension outputs, reports |

**Target for Session 3:** 600-900 lines per skill

**Don't worry about templates.md being "too long"** - that's the whole point! The more comprehensive it is, the more you can trim from SKILL.md.

---

## Success Metrics for Session 3

**Target Outcomes:**
- ✅ 3 skills refactored to Grade A
- ✅ 60%+ average token reduction
- ✅ 100% portable (no hardcoded paths)
- ✅ 3 distributable .zip packages
- ✅ Project progress: 44% → 61% (11/18 skills)
- ✅ Session duration: 3-3.5 hours
- ✅ Token usage: ~60-65% of 200k budget

**Quality Checks:**
- All 3 skills validate as Grade A
- SKILL.md files are 300-450 lines
- templates.md files are 600-900 lines
- All references work correctly
- No hardcoded paths anywhere

---

## After Session 3: What's Next?

**Remaining Skills (7):** 61% → 100%

**Session 4 Targets (3 skills):**
1. execute-task (development)
2. refine-story (planning)
3. risk-profile (quality)

**Session 5 Targets (4 skills):**
1. test-design (quality)
2. document-project (brownfield)
3. index-docs (brownfield)
4. sprint-plan (brownfield)

**Then:** End-to-end workflow validation (Week 6)

---

## Questions & Support

**If you encounter issues:**

1. **Validation fails:** Read error message, fix YAML/structure, re-validate
2. **Edit fails (string not found):** Read actual file content first, match exactly
3. **Unsure what to trim:** Look at Session 1-2 examples in completed skills
4. **Line count too high/low:** Adjust trimming, but accept 300-450 range

**Reference Materials:**
- `docs/refactoring-session-1-summary.md` - First 5 skills
- `docs/refactoring-session-2-summary.md` - Last 3 skills
- `docs/skill-refactoring-template.md` - General template
- Completed skills: fix-issue, estimate-stories, implement-feature, review-task, create-task-spec, refactor-code, breakdown-epic, quality-gate

---

## Final Checklist Before Starting

- [ ] I understand the 7-step process
- [ ] I know the 3 target skills (run-tests, nfr-assess, trace-requirements)
- [ ] I have the validation command ready
- [ ] I know what to include in templates.md
- [ ] I know how to systematically trim SKILL.md
- [ ] I will validate after each skill (not batch at end)
- [ ] I will document results as I go

---

**Let's refactor 3 more skills to Grade A!** 🚀

Use the proven templates.md pattern, follow the 7-step process, and validate early and often. You've got this!

**Session Goal:** 44% → 61% completion (11/18 skills)

---

*Handoff Document Version: 1.0*
*Created: 2025-10-29*
*Based on: Session 1 (5 skills) + Session 2 (3 skills) learnings*
*Next Session After This: Session 4 (3 more skills, 61% → 78%)*
