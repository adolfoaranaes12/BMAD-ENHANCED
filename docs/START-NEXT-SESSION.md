# Start Next Coding Session - Quick Handoff

**Copy this entire prompt into your next Claude Code session:**

---

# Skills Refactoring Session - Context & Instructions

## Current Status

**Project:** BMAD Enhanced - Migration from BMAD Method v4 to Claude Code architecture

**Progress:**
- ✅ Week 0: Terminology standardization complete
- ✅ Architecture: 100% Claude Code compliant
- ✅ Skills refactored: 2 of 18 (11% complete)
  - fix-issue: Grade A, 67% token reduction
  - estimate-stories: Grade A, 75% token reduction
- 🎯 **Your mission: Refactor 3 high-priority skills (implement-feature, review-task, create-task-spec)**

**Documentation Version:** ROADMAP v3.2

---

## Your Mission: Refactor 3 Skills to Grade A

**Priority order:**
1. **implement-feature** (development skill) - Core dev workflow
2. **review-task** (quality skill) - Core QA workflow
3. **create-task-spec** (planning skill) - Core planning workflow

**Success criteria per skill:**
- ✅ Grade A compliance (validate with skill-creator)
- ✅ 70%+ token reduction
- ✅ YAML frontmatter with proper structure
- ✅ 300-400 lines in SKILL.md
- ✅ 3-5 reference files (1,500-2,500 total lines)
- ✅ 100% portable (no hardcoded paths)

**Time estimate:** 12-15 hours total (4-5 hours first skill, 3-4 hours each subsequent)

---

## Critical Architecture Context

### The 3-Layer Architecture

**⚠️ KEY CONCEPT:** All skills use the same structure (SKILL.md + references/). The "3 layers" describes the ROLE skills play, not different file types.

```
Layer 3: SUBAGENTS (.claude/agents/)
    ↓ Route to appropriate skills
Layer 2: WORKFLOW SKILLS (.claude/skills/)  ← YOUR TARGETS
    ↓ May use primitives
Layer 1: PRIMITIVES (.claude/skills/bmad-commands/)
    ↓ Atomic operations
```

**All skills:**
- Have SKILL.md with YAML frontmatter
- Use references/ for detailed content (progressive disclosure)
- Are packageable and portable
- Follow official Claude Code skill-creator pattern

**Layer 1 (Primitives):** bmad-commands skill with Python scripts
**Layer 2 (Workflows):** implement-feature, review-task, create-task-spec (what you're refactoring)
**Layer 3 (Subagents):** james-developer-v2.md, quinn-quality.md, etc. (NOT skills)

---

## Step-by-Step Process (per skill)

### Step 1: Read & Analyze (15 min)
- Read the current skill file
- Count lines
- Identify sections
- Plan what goes in SKILL.md vs references/

### Step 2: Create Directory Structure (5 min)
```
.claude/skills/[category]/[skill-name]/
├── SKILL.md
└── references/
```

### Step 3: Add YAML Frontmatter (20 min)
```yaml
---
name: skill-name
description: |
  Clear description of what this skill does and when to use it.
version: "2.0.0"
dependencies:
  - bmad-commands  # Only if using Layer 1 primitives
---
```

### Step 4: Streamline SKILL.md (60 min)
**Target: 300-400 lines**

**Keep in SKILL.md:**
- Purpose & overview (2-3 paragraphs)
- Quick start (numbered steps, imperative voice)
- Key sections with links to references/
- Success criteria

**Move to references/:**
- Detailed workflows
- Examples and code
- Patterns and templates
- Checklists
- Troubleshooting

### Step 5: Create Reference Files (90-120 min)
**Create 3-5 files, 400-600 lines each:**
- workflow-guide.md
- patterns-library.md
- examples.md
- checklist.md
- troubleshooting.md

### Step 6: Remove Old File (2 min)
If skill was a single file, delete it after verifying new structure works.

### Step 7: Validate with skill-creator (20 min)
Must achieve **Grade A** before moving on.

### Step 8: Document Metrics (10 min)
Record before/after lines, token reduction %, validation results.

---

## Your Essential Reading List

**Before starting, read these in order:**

1. **docs/skill-refactoring-template.md** - Your complete guide (MUST READ)
2. **.claude/skills/development/fix-issue/SKILL.md** - Grade A example
3. **.claude/skills/planning/estimate-stories/SKILL.md** - Grade A example
4. **docs/3-layer-architecture-for-skills.md** - Architecture context
5. **docs/NEXT-SESSION-PROMPT.md** - Detailed instructions (this file's full version)

---

## Common Pitfalls to Avoid

❌ Making SKILL.md too long (>400 lines)
❌ Missing YAML frontmatter
❌ Using declarative voice ("You should...") instead of imperative ("Review...")
❌ Recreating primitives instead of referencing bmad-commands
❌ Hardcoded paths
❌ Not validating with skill-creator
❌ Insufficient reference content

---

## Your Deliverables

1. **3 refactored skills** (implement-feature, review-task, create-task-spec)
   - Each with SKILL.md (300-400 lines)
   - Each with references/ (3-5 files, 1,500-2,500 total lines)
   - All Grade A validated

2. **Updated docs/REFACTORING-COMPLETE.md**
   - Add 3 new skills to completed list
   - Update progress: 11% → 28% (5/18 skills)
   - Document metrics

3. **Session summary** in docs/refactoring-session-1-summary.md
   - Skills completed
   - Metrics (before/after, token reduction)
   - Challenges and solutions
   - Time taken
   - Next steps

---

## How to Start Right Now

**Step 1: Read the documentation (30 min)**
```
Please read these files in this order and confirm you understand the process:

1. docs/skill-refactoring-template.md
2. .claude/skills/development/fix-issue/SKILL.md
3. .claude/skills/planning/estimate-stories/SKILL.md

After reading, tell me:
- What goes in SKILL.md vs references/?
- What is progressive disclosure?
- What makes a skill Grade A?
```

**Step 2: Start with implement-feature (4 hours)**
```
Now let's refactor implement-feature:

1. Read the current skill file at .claude/skills/development/implement-feature/
2. Analyze its structure and content
3. Create a refactoring plan showing:
   - What will go in SKILL.md (target: 350 lines)
   - What reference files you'll create (list names and purpose)
   - Estimated line counts

Please share your plan before proceeding with the refactoring.
```

**Step 3: Execute and validate**
```
[After plan approval]
Proceed with refactoring following Steps 1-8.
Validate with skill-creator when done.
```

**Step 4: Repeat for review-task and create-task-spec**

---

## Quick Reference: Skills Structure

**Good SKILL.md example (fix-issue, 306 lines):**
```markdown
---
name: fix-issue
description: Fix bugs and issues following TDD
version: "2.0.0"
---

# Fix Issue

## Purpose
[3 paragraphs]

## Quick Start
1. Reproduce the issue
   → See references/debugging-techniques.md
2. Write failing test
   → See references/test-examples.md
...

## Core Workflow
[Brief overview with links to references/]

## Success Criteria
- [ ] Issue reproduced and understood
- [ ] Tests cover the fix
- [ ] Code reviewed
```

**Good references/ structure:**
```
references/
├── debugging-techniques.md (450 lines)
├── test-examples.md (500 lines)
├── common-patterns.md (400 lines)
└── error-scenarios.md (500 lines)
Total: 1,850 lines
```

---

## Success Metrics

**After this session:**
- ✅ 3 skills refactored (implement-feature, review-task, create-task-spec)
- ✅ All Grade A validated
- ✅ Average 70%+ token reduction
- ✅ Progress: 11% → 28% (5 of 18 skills)
- ✅ Ready for next 3 skills in Week 2

---

## Questions? Check These

**Q: How do I decide what goes in SKILL.md vs references/?**
A: SKILL.md = WHAT to do (brief, actionable). references/ = HOW to do it (detailed, comprehensive).

**Q: Should this skill use bmad-commands?**
A: Only if it needs file operations or test execution. Most workflow skills just describe the workflow.

**Q: What if validation isn't Grade A?**
A: Fix the issues (usually frontmatter or length) and re-validate. Don't move on until Grade A.

**Q: How detailed should references be?**
A: Very detailed. 400-600 lines per file. Include examples, code, tables, templates.

---

## Ready? Start Here:

```
I'm ready to refactor 3 high-priority BMAD Enhanced skills to Claude Code Grade A compliance.

First, let me read and understand the process:

1. Please show me: docs/skill-refactoring-template.md
2. Then show me: .claude/skills/development/fix-issue/SKILL.md
3. Then show me: .claude/skills/planning/estimate-stories/SKILL.md

After reviewing these, I'll analyze implement-feature and create a refactoring plan.
```

---

**Document:** START-NEXT-SESSION.md
**Version:** 1.0
**Date:** 2025-10-29
**Expected Duration:** 12-15 hours
**Expected Outcome:** 3 Grade A skills, 28% project completion
