# AI Agent Handoff Prompt - BMAD Enhanced Development

**Date:** October 29, 2025
**Purpose:** Complete context and next steps for AI agent to continue BMAD Enhanced development
**Current Status:** Architecture complete, 2 skills refactored, 16 skills remaining

---

## Your Mission

You are continuing development of **BMAD Enhanced**, a sophisticated AI-powered software development methodology that leverages Claude Code's Skills, Subagents, and (future) Slash Commands to provide a structured, observable, and production-ready development workflow.

Your immediate task is to **refactor the remaining 16 BMAD skills** to be fully compliant with both:
1. **skill-creator** standards (packaging, portability, progressive disclosure)
2. **3-layer architecture** standards (contracts, telemetry, routing)

---

## 📋 Complete Project Context

### What is BMAD Enhanced?

**BMAD (Brownfield Methodical Agile Development)** is a methodology for AI-assisted software development. The "Enhanced" version adds:
- Layered architecture (Primitive Skills → Workflow Skills → Subagents)
- Formal contracts (acceptance criteria, inputs/outputs, telemetry)
- Intelligent routing (subagents select appropriate skills based on complexity)
- Safety guardrails (prevent excessive changes, enforce quality standards)
- Full observability (telemetry at every layer)

### Current Architecture

```
3-Layer Skills & Subagents Architecture

┌─────────────────────────────────────────────────────────┐
│ Layer 3: SUBAGENTS (Intelligent Routing)                │
│ Location: .claude/agents/                               │
│                                                          │
│ • james-developer-v2.md    ← Developer subagent         │
│ • alex-planner.md          ← Planning subagent          │
│ • quinn-quality.md         ← Quality subagent           │
│ • orchestrator.md          ← Master orchestrator        │
│                                                          │
│ Routes to appropriate skills based on context           │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│ Layer 2: WORKFLOW SKILLS (Composed Operations)          │
│ Location: .claude/skills/development/, planning/, etc.  │
│                                                          │
│ • implement-v2/SKILL.md    ← TDD implementation ✅      │
│ • estimate-stories/SKILL.md ← Story estimation ✅       │
│ • fix-issue/SKILL.md       ← Bug fixing (needs update)  │
│ • [13 more skills]         ← Need refactoring           │
│                                                          │
│ Compose primitive operations into workflows             │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│ Layer 1: PRIMITIVES (Atomic Operations)                 │
│ Location: .claude/skills/bmad-commands/                 │
│                                                          │
│ • bmad-commands/SKILL.md   ← Skill with bundled scripts │
│   └─ scripts/              ← Python scripts             │
│      ├─ read_file.py       ← Atomic file operations     │
│      └─ run_tests.py       ← Atomic test execution      │
│                                                          │
│ Provides testable, deterministic primitives             │
└─────────────────────────────────────────────────────────┘
```

**Key Concepts:**
- All three layers use **Skills** (Layer 1 & 2 are both skills with different roles)
- Subagents are **NOT skills** (they're coordination files in `.claude/agents/`)
- Everything is **100% compliant** with official Claude Code documentation (docs.claude.com)

---

## ✅ What's Been Completed

### 1. Architecture Designed & Validated ✅

**Created:**
- 3-layer architecture pattern
- Prototype implementation (james-developer-v2, implement-v2, bmad-commands)
- Full validation proving the pattern works

**Documentation:**
- `docs/3-layer-architecture-for-skills.md` - Complete architecture reference
- `docs/3-layer-architecture-prototype.md` - Prototype validation results
- `docs/architecture-claude-code-compliance.md` - Official compliance verification

### 2. Compliance Verified ✅

**Achieved:**
- ✅ 100% compliant with skill-creator standards
- ✅ 100% compliant with official Claude Code docs (subagents, skills)
- ✅ Terminology aligned with docs.claude.com
- ✅ All subagents in correct location (`.claude/agents/`)
- ✅ All subagents in correct format (single .md files)

**Documentation:**
- `docs/compliance-fixes-summary.md` - Compliance fixes applied
- `docs/terminology-update-summary.md` - Terminology alignment

### 3. Refactoring Template Created ✅

**Created:**
- Comprehensive V2 refactoring template
- Includes both skill-creator AND 3-layer architecture compliance
- Step-by-step guide (4-5 hours per skill)

**Documentation:**
- `docs/skill-refactoring-template.md` - **YOUR PRIMARY GUIDE**
- `docs/template-compliance-updates.md` - Template improvements made

### 4. Skills Refactored (2 of 18) ✅

**Completed:**
1. ✅ **implement-v2** - Full V2 implementation (contracts, telemetry, commands integration)
2. ✅ **estimate-stories** - Skill-creator compliant (needs V2 upgrade later)

**Remaining:** 16 skills need refactoring

### 5. Primitives Built ✅

**Created:**
- `bmad-commands` skill with Python scripts
- Provides atomic, testable operations
- Used by workflow skills

**Documentation:**
- `.claude/skills/bmad-commands/SKILL.md` - Command primitives reference

### 6. Subagents Configured ✅

**Created:**
- james-developer-v2 (with full routing and guardrails)
- alex-planner, quinn-quality, orchestrator (basic versions)

**Location:** `.claude/agents/`

### 7. Documentation Cleaned ✅

**Status:**
- 16 outdated files deleted
- 15 current files kept
- Clean, organized documentation structure

---

## 📚 Critical Documentation You Need

### Must-Read Documents (Priority Order)

**1. REFACTORING TEMPLATE (Your Primary Guide)**
```
docs/skill-refactoring-template.md
```
- **USE THIS for every skill refactoring**
- Step-by-step instructions
- Examples for every step
- Validation checklists
- V2 architecture integration

**2. ARCHITECTURE REFERENCE**
```
docs/3-layer-architecture-for-skills.md
```
- Complete architecture explanation
- Layer definitions
- How skills work together
- Portability requirements

**3. COMPLIANCE GUIDE**
```
docs/architecture-claude-code-compliance.md
```
- Official Claude Code alignment
- What to do and not do
- Verification checklists

**4. EXAMPLE SKILLS (Reference Implementations)**
```
.claude/skills/development/implement-v2/SKILL.md
.claude/skills/planning/estimate-stories/SKILL.md
```
- See these for examples of correct structure

**5. BMAD COMMANDS REFERENCE**
```
.claude/skills/bmad-commands/SKILL.md
```
- Available primitive operations
- How to call commands from skills
- Command contracts

### Supporting Documents

**Completed Work:**
- `docs/REFACTORING-COMPLETE.md` - What's been done
- `docs/compliance-fixes-summary.md` - Fixes applied
- `docs/terminology-update-summary.md` - Terminology updates

**Standards:**
- `docs/standards.md` - Coding/documentation standards
- `docs/terminology-alignment-claude-code.md` - Official terminology

**Future Plans:**
- `docs/slash-commands-implementation-guide.md` - For later (optional)
- `docs/ROADMAP.md` - Project roadmap

---

## 🎯 Your Immediate Next Steps

### Phase 1: Understand the Context (30 minutes)

**Step 1: Read the Refactoring Template**
```bash
Read: docs/skill-refactoring-template.md
```
- Understand the 8-step process
- Review validation criteria
- Study the examples

**Step 2: Review Example Skills**
```bash
Read: .claude/skills/development/implement-v2/SKILL.md
Read: .claude/skills/planning/estimate-stories/SKILL.md
```
- See correct structure
- Understand progressive disclosure
- Review contracts (implement-v2 has full V2)

**Step 3: Check Architecture**
```bash
Read: docs/3-layer-architecture-for-skills.md (sections: Overview, Layer Definitions, Key Concepts)
```
- Understand how layers work together
- Grasp portability requirements
- Learn skill vs subagent distinction

---

### Phase 2: Identify Next Skills to Refactor (15 minutes)

**Recommended Priority Order (from template):**

**Tier 1: High V2 Value (Do First - 5 skills)**
These benefit most from V2 architecture:
1. **implement-feature** - Medium complexity implementation
2. **fix-bug** - Bug fixing workflow
3. **run-tests** - Test execution
4. **refactor-code** - Safe refactoring
5. **implement-with-discovery** - High complexity implementation

**Tier 2: Medium V2 Value (Do Second - 4 skills)**
Mixed planning/implementation:
6. **create-task-spec** - Task creation
7. **breakdown-epic** - Epic breakdown
8. **review-task** - Code review
9. **refine-story** - Story refinement

**Tier 3: Lower V2 Value (Do Last - 7 skills)**
Planning/quality focused:
10. **estimate-complexity** - Complexity estimation
11. **quality-gate** - Quality assessment
12. **nfr-assess** - Non-functional requirements
13. **trace-requirements** - Requirements tracing
14. **generate-test-cases** - Test case generation
15. **risk-assessment** - Risk analysis
16. **technical-spike** - Spike planning

**Note:** Exact skill names may vary. Use `ls .claude/skills/` to see actual skills.

---

### Phase 3: Refactor Skills (Main Work)

**For Each Skill:**

**Use the Template Process (4-5 hours per skill):**

```bash
# Reference the template:
docs/skill-refactoring-template.md
```

**Step-by-Step:**

1. **Step 1: Analyze Current Skill (15 min)**
   - Read existing skill file
   - Count lines
   - Identify sections to extract
   - Document findings

2. **Step 2: Create Directory Structure (5 min)**
   ```bash
   mkdir -p .claude/skills/category/skill-name/references
   ```

3. **Step 3: Add YAML Frontmatter with V2 Contracts (20 min)**
   - Add name, description
   - Define acceptance criteria (2-5 criteria)
   - Add inputs/outputs (if applicable)
   - Add telemetry (emit event, track metrics)

   **Example:**
   ```yaml
   ---
   name: skill-name
   description: Brief description with when to use
   acceptance:
     - criterion_1: "What must be true"
     - criterion_2: "What must be true"
   inputs:
     task_id:
       type: string
       required: true
   outputs:
     success:
       type: boolean
   telemetry:
     emit: "skill.skill-name.completed"
     track: ["task_id", "duration_ms"]
   ---
   ```

4. **Step 4: Streamline SKILL.md (60 min)**
   - Keep high-level workflow (<400 lines)
   - Short examples (10-30 lines)
   - Reference details in references/
   - Use imperative form
   - Trust Claude's knowledge

5. **Step 4.5: Integrate bmad-commands (15 min)**
   - **For implementation skills only**
   - Replace ad-hoc operations with bmad-commands
   - Example:
   ```markdown
   Execute:
   ```bash
   python .claude/skills/bmad-commands/scripts/read_file.py \
     --path workspace/tasks/{task_id}.md \
     --output json
   ```
   ```

6. **Step 5: Create Reference Files (90-120 min)**
   - Extract detailed content
   - Create 2-5 reference files
   - Types: patterns, techniques, scales, scenarios, templates
   - Use progressive disclosure

7. **Step 6: Remove Old File (2 min)**
   ```bash
   mv .claude/skills/category/skill-name.md \
      .claude/skills/category/skill-name.md.old
   ```

8. **Step 7: Validate Compliance (20 min)**
   - Check line count (<450 lines)
   - Verify frontmatter
   - Test V2 compliance
   - Use validation checklist from template

9. **Step 8: Add Routing Guidance (10 min)**
   - **For skills called by subagents**
   - Document when to use this skill
   - Add routing section to SKILL.md

**After Each Skill:**
- Mark as complete in tracking
- Test the skill works
- Move to next skill

---

### Phase 4: Tracking Progress

**Create a Progress Tracker:**

```markdown
# BMAD Skills Refactoring Progress

**Started:** [Date]
**Target Completion:** [Date]

## Progress Summary

- Total Skills: 18
- Completed: 2 (11%)
- Remaining: 16 (89%)

## Tier 1 (High V2 Value) - 5 skills
- [ ] implement-feature
- [ ] fix-bug
- [ ] run-tests
- [ ] refactor-code
- [ ] implement-with-discovery

## Tier 2 (Medium V2 Value) - 4 skills
- [ ] create-task-spec
- [ ] breakdown-epic
- [ ] review-task
- [ ] refine-story

## Tier 3 (Lower V2 Value) - 7 skills
- [ ] estimate-complexity
- [ ] quality-gate
- [ ] nfr-assess
- [ ] trace-requirements
- [ ] generate-test-cases
- [ ] risk-assessment
- [ ] technical-spike

## Completed
- [x] implement-v2 (2025-10-28) - Full V2
- [x] estimate-stories (2025-10-28) - skill-creator only

## Notes
[Track issues, learnings, improvements]
```

---

## 🔍 Key Concepts You Must Understand

### 1. Skills vs Subagents

**Skills:**
- Location: `.claude/skills/category/skill-name/`
- File: `SKILL.md` (with YAML frontmatter)
- Structure: SKILL.md + references/ + scripts/ (optional)
- Purpose: Modular capabilities
- Invocation: Model-invoked (Claude decides when to use)
- **Important:** Layers 1 and 2 are BOTH skills (different roles)

**Subagents:**
- Location: `.claude/agents/subagent-name.md`
- File: Single .md file (NOT a directory)
- Structure: Markdown with YAML frontmatter, all content inline
- Purpose: Specialized AI assistants with routing logic
- Invocation: By delegation or explicit mention
- **Important:** Subagents are NOT skills

### 2. Portability is Critical

**Skills MUST be:**
- ✅ Packageable with `package_skill.py`
- ✅ Distributable as .zip files
- ✅ Self-contained (no external dependencies)
- ✅ Portable (work anywhere)

**Never:**
- ❌ Hard-code absolute paths
- ❌ Reference files outside skill directory
- ❌ Require external dependencies not bundled
- ❌ Assume specific environment

### 3. Progressive Disclosure

**Pattern:**
- **SKILL.md:** High-level workflow, quick reference (<400 lines)
- **references/:** Detailed explanations, examples, patterns

**Why:**
- Reduces context window usage
- Keeps main skill file readable
- Claude loads references only when needed

### 4. V2 Architecture Features

**Contracts (YAML frontmatter):**
- Acceptance criteria (what "done" means)
- Inputs (what skill needs)
- Outputs (what skill produces)
- Telemetry (what to track)

**Benefits:**
- Testable (can verify acceptance)
- Observable (telemetry at every layer)
- Composable (clear interfaces)
- Production-ready

**When to Apply:**
- **Full V2:** Development/implementation skills (Tier 1)
- **Partial V2:** Mixed skills (Tier 2) - add acceptance + telemetry
- **Minimal V2:** Planning skills (Tier 3) - optional

### 5. Bmad-Commands Integration

**What it is:**
- Primitive skills layer (Layer 1)
- Skill with bundled Python scripts
- Provides atomic, testable operations

**Available Commands:**
- `read_file.py` - Read files with metadata
- `run_tests.py` - Execute tests with structured output

**When to use:**
- Implementation/development skills
- Skills that need file operations
- Skills that run tests

**When to skip:**
- Planning-only skills
- Quality assessment skills
- No file operations needed

---

## 🚨 Critical Dos and Don'ts

### DO ✅

**✅ Follow the Template**
- Use `docs/skill-refactoring-template.md` for every skill
- Don't skip steps
- Complete validation checklist

**✅ Maintain Portability**
- Keep all resources in skill directory
- Use relative paths
- Bundle dependencies
- Test packaging works

**✅ Use Progressive Disclosure**
- Main SKILL.md: <400 lines
- Details in references/
- 2-5 reference files typical

**✅ Add V2 Features Appropriately**
- Full V2 for Tier 1 (implementation skills)
- Partial V2 for Tier 2 (mixed skills)
- Minimal V2 for Tier 3 (planning skills)

**✅ Reference Examples**
- Study implement-v2 (full V2 example)
- Study estimate-stories (skill-creator example)
- Copy patterns from working skills

**✅ Use Imperative Form**
- "Execute the tests" not "You should execute the tests"
- "Analyze complexity" not "You analyze complexity"
- Action-oriented language

**✅ Trust Claude's Knowledge**
- Don't explain basic concepts (Claude knows TDD, Git, etc.)
- Focus on BMAD-specific workflows
- Provide context, not education

### DON'T ❌

**❌ Don't Create New Architecture Patterns**
- Use the established 3-layer architecture
- Don't invent new layer types
- Follow official Claude Code patterns

**❌ Don't Break Portability**
- No hard-coded paths
- No external file references
- No undealt dependencies

**❌ Don't Make Skills Too Verbose**
- Not over 450 lines for SKILL.md
- Extract details to references/
- Keep examples short (10-30 lines)

**❌ Don't Skip Validation**
- Always complete Step 7 validation
- Check both skill-creator and V2 compliance
- Test that skill works

**❌ Don't Modify Skill Names**
- Keep existing skill names unchanged
- Only update structure and content
- Maintain backward compatibility

**❌ Don't Create Non-Portable Skills**
- Test with package_skill.py
- Verify works in different location
- Check all paths are relative

**❌ Don't Mix Subagents and Skills**
- Subagents go in `.claude/agents/` (single .md files)
- Skills go in `.claude/skills/` (SKILL.md + directories)
- Never confuse the two

---

## 📊 Success Criteria

### Per-Skill Success

**For each refactored skill, verify:**

**skill-creator Compliance:**
- [ ] YAML frontmatter with name + description
- [ ] SKILL.md file in skill directory
- [ ] references/ directory with detailed content
- [ ] Under 450 lines (ideally 300-400)
- [ ] No HTML comments
- [ ] No "Invocation" or "Configuration" sections
- [ ] Progressive disclosure used
- [ ] Packageable with package_skill.py

**V2 Architecture Compliance (if applicable):**
- [ ] Acceptance criteria defined (2-5 criteria)
- [ ] Inputs documented (if skill accepts parameters)
- [ ] Outputs documented (if skill produces results)
- [ ] Telemetry configured (emit + track)
- [ ] Bmad-commands integrated (if implementation skill)
- [ ] Routing guidance (if called by subagents)

**Quality:**
- [ ] Imperative writing style
- [ ] Trusts Claude's knowledge
- [ ] Short examples (10-30 lines)
- [ ] References indexed clearly
- [ ] Reads naturally and clearly

### Overall Success

**When all 16 skills refactored:**
- [ ] 18/18 skills are skill-creator compliant
- [ ] Tier 1 skills (5) have full V2 architecture
- [ ] Tier 2 skills (4) have partial V2 (acceptance + telemetry)
- [ ] Tier 3 skills (7) have minimal V2 (as applicable)
- [ ] All skills packageable
- [ ] All skills portable
- [ ] Documentation updated
- [ ] Progress tracked

---

## 🛠️ Useful Commands

### Check Current Skills

```bash
# List all skills
ls -la .claude/skills/

# Find skills by category
ls -la .claude/skills/development/
ls -la .claude/skills/planning/
ls -la .claude/skills/quality/

# Check skill structure
tree .claude/skills/development/implement-v2/
```

### Validation Commands

```bash
# Check line count
wc -l .claude/skills/category/skill-name/SKILL.md

# Check frontmatter
head -10 .claude/skills/category/skill-name/SKILL.md

# Test packaging
python scripts/package_skill.py .claude/skills/category/skill-name
```

### Progress Tracking

```bash
# Count refactored skills (with SKILL.md in subdirectory)
find .claude/skills -name "SKILL.md" | wc -l

# List old-style skills (need refactoring)
find .claude/skills -maxdepth 2 -name "*.md" ! -name "SKILL.md"
```

---

## 🔄 Workflow Pattern

**For Each Skill, Follow This Pattern:**

```
1. READ: Current skill file
   └─ Analyze structure, content, length

2. PLAN: What to extract to references/
   └─ Identify patterns, examples, detailed guides

3. CREATE: Directory structure
   └─ mkdir -p .claude/skills/category/skill-name/references

4. WRITE: SKILL.md with V2 contracts
   └─ YAML frontmatter + streamlined workflow

5. EXTRACT: Detailed content to references/
   └─ 2-5 reference files with progressive disclosure

6. INTEGRATE: Bmad-commands (if applicable)
   └─ Replace ad-hoc operations with command calls

7. VALIDATE: Against checklist
   └─ skill-creator + V2 compliance

8. TEST: Verify it works
   └─ Package, read, verify paths

9. CLEANUP: Remove old file
   └─ mv old.md old.md.bak

10. DOCUMENT: Progress
    └─ Mark complete, note any issues
```

---

## 💡 Tips for Efficiency

### Batch Similar Skills

Refactor skills in same category together (they share patterns):

**Development Skills Batch (5):**
- implement-feature, fix-bug, run-tests, refactor-code, implement-with-discovery
- Share: TDD patterns, test examples, refactoring techniques

**Planning Skills Batch (4):**
- create-task-spec, breakdown-epic, review-task, refine-story
- Share: Estimation scales, templates, workflows

**Quality Skills Batch (7):**
- estimate-complexity, quality-gate, nfr-assess, etc.
- Share: Assessment criteria, scoring matrices, templates

### Reuse Reference Patterns

Don't recreate from scratch:
- Adapt references from implement-v2 for other dev skills
- Adapt references from estimate-stories for other planning skills
- Create shared references if truly common

### Work in Focused Blocks

**Recommended Schedule:**
- **Block 1 (90 min):** Steps 1-4 (Analyze, structure, frontmatter, streamline)
- **Break (15 min)**
- **Block 2 (120 min):** Step 5 (Create all reference files)
- **Break (15 min)**
- **Block 3 (30 min):** Steps 6-8 (Cleanup, validate, test)

**Result:** 1 skill per 4-5 hour session

### Track Learnings

**Keep notes on:**
- Common patterns across skills
- Shortcuts discovered
- Issues encountered
- Time spent per skill
- Template improvements needed

---

## 🚀 Getting Started Command

**Here's exactly what to do first:**

```bash
# 1. Read the template (your primary guide)
Read: docs/skill-refactoring-template.md

# 2. Review the example skills
Read: .claude/skills/development/implement-v2/SKILL.md
Read: .claude/skills/planning/estimate-stories/SKILL.md

# 3. Check available skills
ls -la .claude/skills/development/
ls -la .claude/skills/planning/

# 4. Pick your first skill (recommend from Tier 1)
# Example: implement-feature or fix-bug

# 5. Start refactoring using the template process
# Follow steps 1-8 from docs/skill-refactoring-template.md

# 6. Track your progress
# Create progress.md to track completed skills
```

---

## 🎯 Expected Timeline

**Estimated Effort:**

**Initial Skills (Learning Phase):**
- Skills 3-5: ~5 hours each = 15 hours
- Learning V2 patterns, getting familiar with template

**Middle Skills (Proficiency):**
- Skills 6-10: ~4 hours each = 20 hours
- Comfortable with process, reusing patterns

**Later Skills (Efficiency):**
- Skills 11-18: ~3.5 hours each = 28 hours
- Fast execution, established patterns

**Total Estimated Time:** 55-65 hours for all 16 skills

**Spread Over:**
- 2 weeks at 5-6 hours/day
- 3 weeks at 3-4 hours/day
- 4 weeks at 2-3 hours/day

---

## 📞 If You Get Stuck

**Check These Resources:**

1. **Template is unclear?**
   - Review examples in implement-v2
   - Check template examples section
   - Look at estimate-stories for simpler case

2. **Validation failing?**
   - Review validation checklist in template
   - Check example skills for correct format
   - Verify against compliance docs

3. **Portability issues?**
   - Read portability section in architecture doc
   - Test with package_skill.py
   - Check for absolute paths

4. **Architecture questions?**
   - Read: docs/3-layer-architecture-for-skills.md
   - Review: Layer definitions, key concepts

5. **Compliance concerns?**
   - Read: docs/architecture-claude-code-compliance.md
   - Verify: Following official Claude Code patterns

---

## 🎉 Final Notes

### You Have Everything You Need

- ✅ Complete architecture designed and validated
- ✅ Comprehensive refactoring template
- ✅ Working example skills
- ✅ Full compliance with Claude Code
- ✅ Clean, organized documentation

### This is Well-Defined Work

- Clear process (8 steps per skill)
- Concrete success criteria
- Example implementations
- Detailed guidance

### You Will Succeed If You

1. **Follow the template** - Don't freelance, use the proven process
2. **Reference examples** - Learn from implement-v2 and estimate-stories
3. **Maintain portability** - Keep skills self-contained
4. **Track progress** - Know what's done, what's next
5. **Stay focused** - One skill at a time, validate each one

---

## 🚀 Ready to Start

**Your First Action:**

```bash
Read this file completely, then read:
docs/skill-refactoring-template.md

Then pick your first skill and begin!
```

**Recommended First Skill:** implement-feature or fix-bug (Tier 1, high V2 value)

---

## 📋 Quick Reference Card

```
PRIMARY GUIDE: docs/skill-refactoring-template.md
ARCHITECTURE: docs/3-layer-architecture-for-skills.md
EXAMPLES:
  - .claude/skills/development/implement-v2/SKILL.md (full V2)
  - .claude/skills/planning/estimate-stories/SKILL.md (skill-creator)
COMMANDS: .claude/skills/bmad-commands/SKILL.md

PROCESS: 8 steps, 4-5 hours per skill
TARGET: <400 lines SKILL.md, 2-5 references/
SKILLS REMAINING: 16 (after implement-v2, estimate-stories)

KEY CONCEPT: Skills stay portable, packageable
             Layers define ROLES not structures

VALIDATION: skill-creator + V2 architecture
TRACKING: Create progress.md to track work
```

---

**Status:** ✅ Ready for AI agent handoff
**Next Step:** Read template, pick first skill, start refactoring

---

*Handoff prepared October 29, 2025*
*All context provided for seamless continuation*
