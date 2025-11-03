# Next Session Context: Continue Phase 2 with quinn-quality V2

**Date Created:** January 31, 2025
**For:** Next Claude Code session
**Task:** Implement quinn-quality V2 following alex-planner V2 pattern

---

## Session Quick Start

**Copy this to start your next session:**

```
I'm continuing Phase 2 of the BMAD Enhanced project. We just completed alex-planner V2
and now need to implement quinn-quality V2 with the same intelligent routing, guardrails,
and telemetry pattern.

Context documents to read:
1. docs/PHASE-2-AND-3-PLAN.md - Overall roadmap
2. docs/ALEX-PLANNER-V2-COMPLETE.md - Reference implementation
3. docs/PHASE-1-COMPLETION-SUMMARY.md - Background on V2 architecture
4. .claude/agents/james-developer-v2.md - Original V2 pattern template
5. .claude/agents/alex-planner.md - Just completed, use as reference

Current task: Implement quinn-quality V2 with 5 commands following the established pattern.
Estimated effort: 8-10 hours over 2-3 sessions.
```

---

## Project Overview

### What is BMAD Enhanced?

BMAD Enhanced is a **3-layer architecture system** for AI-assisted software development:

**Layer 1: Primitives** (bmad-commands)
- 6 deterministic Python commands with JSON I/O
- Examples: read_file.py, run_tests.py, generate_architecture_diagram.py
- All return structured: `{success, outputs, telemetry, errors}`

**Layer 2: Workflow Skills**
- 25+ specialized skills across 5 categories
- Examples: implement-feature, fix-issue, quality-gate, create-task-spec
- Compose primitives into workflows
- Located in `.claude/skills/`

**Layer 3: Subagents**
- 6 specialized subagents with command routing
- Examples: james-developer, alex-planner, quinn-quality, winston-architect
- Orchestrate skills with intelligent routing and guardrails
- Located in `.claude/agents/`

---

## Current Project Status

### Phase 1: ✅ COMPLETE (100%)

**james-developer-v2 Subagent**
- 5 commands: *implement, *apply-qa-fixes, *fix, *test, *refactor
- Full 7-step workflow pattern
- Intelligent complexity-based routing (0-100 scale)
- Comprehensive guardrails
- Full telemetry
- File: `.claude/agents/james-developer-v2.md` (2,097 lines)

**All development skills have V2 contracts:**
- implement-feature, fix-issue, run-tests, execute-task
- Contracts include: acceptance, inputs, outputs, telemetry

**Documentation:**
- docs/PHASE-1-COMPLETION-SUMMARY.md - Complete Phase 1 summary
- docs/SESSION-SUMMARY-PHASE-1-COMPLETE.md - Session notes

---

### Phase 2: 🚧 IN PROGRESS (20% complete)

**Objective:** Upgrade remaining subagents to V2 architecture

**Completed (1/5):**
1. ✅ **alex-planner V2** (1 hour, 979 lines)
   - 5 commands: *create-task-spec, *breakdown-epic, *estimate, *refine-story, *plan-sprint
   - File: `.claude/agents/alex-planner.md`
   - Backup: `.claude/agents/alex-planner-v1.md`
   - Docs: `docs/ALEX-PLANNER-V2-COMPLETE.md`

**In Progress (0/5):**
2. ⏳ **quinn-quality V2** (8-10 hours) ← **YOU ARE HERE**
3. ⏳ orchestrator V2 (6-8 hours)
4. ⏳ james-developer-v2 additions: *debug, *explain (6-8 hours)
5. ⏳ V2 contracts for 16 skills (8-12 hours)

**Remaining Effort:** 28-38 hours

---

## The V2 Pattern

### What is V2 Architecture?

V2 subagents follow a **standardized 7-step workflow** for every command:

**7-Step Workflow Pattern:**
1. **Load** - Load specification/context using bmad-commands
2. **Assess** - Calculate complexity score (0-100) with weighted factors
3. **Route** - Select appropriate skill based on complexity
4. **Guard** - Check guardrails before execution
5. **Execute** - Invoke skill with context
6. **Verify** - Verify acceptance criteria met
7. **Telemetry** - Emit structured telemetry

### Complexity Assessment Pattern

**Standard Formula:**
- 5 factors with weights (typically 30%, 25%, 20%, 15%, 10%)
- Each factor scored 0-100
- Final score = weighted sum
- 3 categories: Low (≤30), Medium (31-60), High (>60)

**Example (from james-developer-v2 *implement command):**
```
Factors:
- Files affected (30%): 1-2=10, 3-5=30, 6-10=60, 11+=90
- Database changes (25%): None=0, Schema=50, Migration=90
- API changes (20%): None=0, Modify=30, New=60, Breaking=90
- Dependencies (15%): None=0, Internal=20, External=50, New=90
- Test complexity (10%): Unit=10, Integration=40, E2E=70, All=90

Final Score = (files × 0.30) + (db × 0.25) + (api × 0.20) + (deps × 0.15) + (tests × 0.10)
```

### Routing Pattern

**Standard Routing:**
- **Route 1:** Simple/Low (complexity ≤30) → Basic skill, minimal guardrails
- **Route 2:** Standard/Medium (31-60) → Standard skill, standard guardrails
- **Route 3:** Complex/High (>60) → Advanced skill, strict guardrails, escalation required
- **Default Route:** Fallback for edge cases

### Guardrails Pattern

**Types:**
- **Global:** Apply to all commands (e.g., max files, require tests)
- **Command-specific:** Apply to one command (e.g., refactor requires passing tests first)
- **Safety:** Critical constraints (e.g., no hardcoded secrets, block .env files)
- **Escalation triggers:** When to ask user for confirmation

### Telemetry Pattern

**Standard Structure:**
```json
{
  "agent": "subagent-name",
  "command": "command-name",
  "routing": {
    "complexity_score": 45,
    "skill_selected": "skill-name",
    "reason": "explanation"
  },
  "guardrails": {
    "checked": true,
    "passed": true,
    "violations": []
  },
  "execution": {
    // Command-specific metrics
    "duration_ms": 120000,
    "files_modified": 3,
    // etc.
  },
  "acceptance": {
    "verified": true,
    "all_criteria_met": true
  },
  "timestamp": "2025-01-31T18:00:00Z"
}
```

---

## YOUR TASK: Implement quinn-quality V2

### Current State

**File:** `.claude/agents/quinn-quality.md` (V1 version exists)
**Backup location:** `.claude/agents/quinn-quality-v1.md` (create this first)

**Current quinn-quality V1:**
- Basic quality agent
- No complexity assessment
- No intelligent routing
- Limited guardrails
- No telemetry

### Target State

**quinn-quality V2 must have:**
- ✅ YAML frontmatter (name, description, tools, model)
- ✅ V2 Enhancements section
- ✅ 5 complete commands with 7-step workflow
- ✅ Intelligent complexity-based routing
- ✅ Comprehensive guardrails
- ✅ Full telemetry structures
- ✅ Philosophy and comparison sections
- ✅ Usage examples
- ✅ Integration guides

---

## The 5 Commands to Implement

### Command 1: `*review` ⭐ HIGH PRIORITY

**Purpose:** Comprehensive quality review (code quality + NFRs + gate decision)

**Syntax:** `@quinn *review <task-id>`

**Complexity Factors:**
- Files to review (30%): 1-2=10, 3-5=40, 6-8=70, 9+=90
- Quality issues (25%): 0-3=10, 4-8=50, 9-15=80, 16+=90
- NFR requirements (20%): None=10, Basic=40, Standard=70, Comprehensive=90
- Test coverage (15%): >90%=10, 70-90%=50, 50-70%=80, <50%=90
- Codebase size (10%): Small=10, Medium=40, Large=70, XLarge=90

**Routes:**
- Simple review (≤30): Few files, good quality, high coverage
- Standard review (31-60): Moderate complexity
- Comprehensive review (>60): Many files, quality issues, complex NFRs

**Skills used:**
- `.claude/skills/quality/review-task/SKILL.md`
- May chain to: nfr-assess, refactor-code, quality-gate

**Guardrails:**
- Min coverage 80%
- Quality score requirements
- NFR compliance checks
- All critical issues addressed

**Telemetry:**
```json
{
  "agent": "quinn-quality-v2",
  "command": "review",
  "task_id": "task-auth-001",
  "routing": {
    "complexity_score": 45,
    "review_depth": "standard"
  },
  "execution": {
    "files_reviewed": 5,
    "issues_found": 12,
    "issues_critical": 0,
    "issues_high": 3,
    "issues_medium": 6,
    "issues_low": 3,
    "nfr_checked": 8,
    "nfr_passed": 7,
    "nfr_failed": 1,
    "coverage_percent": 87,
    "quality_score": 78,
    "gate_decision": "PASS",
    "duration_ms": 300000
  }
}
```

---

### Command 2: `*assess-nfr` ⭐ MEDIUM PRIORITY

**Purpose:** Assess non-functional requirements (performance, security, scalability)

**Syntax:** `@quinn *assess-nfr <task-id>`

**Complexity Factors:**
- NFR count (30%): 1-3=10, 4-6=40, 7-10=70, 11+=90
- System complexity (25%): Simple=10, Moderate=50, Complex=90
- Impact (20%): Low=10, Medium=50, High=90
- Test requirements (15%): Unit only=10, Integration=50, Load/Performance=90
- Documentation (10%): Minimal=10, Standard=50, Comprehensive=90

**Routes:**
- Simple assessment (≤30): Few NFRs, low impact
- Standard assessment (31-60): Moderate NFRs
- Comprehensive assessment (>60): Many NFRs, high impact

**Skills used:**
- `.claude/skills/quality/nfr-assess/SKILL.md`

**Guardrails:**
- All NFRs addressed
- Test plans for P0/P1 NFRs
- Risk identification
- Performance targets defined

**Telemetry:**
```json
{
  "agent": "quinn-quality-v2",
  "command": "assess-nfr",
  "task_id": "task-auth-001",
  "routing": {
    "complexity_score": 35
  },
  "execution": {
    "nfrs_total": 8,
    "nfrs_passed": 7,
    "nfrs_failed": 1,
    "nfrs_concerns": 0,
    "categories": {
      "performance": "PASS",
      "security": "CONCERNS",
      "scalability": "PASS",
      "reliability": "PASS"
    },
    "duration_ms": 180000
  }
}
```

---

### Command 3: `*validate-quality-gate` ⭐ HIGH PRIORITY

**Purpose:** Make quality gate decision (PASS/CONCERNS/FAIL/WAIVED)

**Syntax:** `@quinn *validate-quality-gate <task-id>`

**Complexity Factors:**
- Issue severity (30%): None=10, Low=30, High=70, Critical=90
- NFR failures (25%): None=10, 1-2=50, 3+=90
- Coverage gaps (20%): None=10, Minor=40, Significant=70, Critical=90
- Technical debt (15%): Low=10, Medium=50, High=90
- Risk (10%): Low=10, Medium=50, High=90

**Routes:**
- Clear pass/fail (≤30): Obvious decision
- Borderline (31-60): Needs judgment
- Complex decision (>60): Requires detailed analysis

**Skills used:**
- `.claude/skills/quality/quality-gate/SKILL.md`

**Guardrails:**
- Objective criteria used
- Waiver requires justification
- Escalate for FAIL decisions
- Document rationale

**Decisions:**
- **PASS:** Quality score ≥80, no critical issues, coverage ≥80%
- **CONCERNS:** Score 60-79, some issues, may waive
- **FAIL:** Score <60, critical issues, coverage <60%
- **WAIVED:** User overrides CONCERNS/FAIL with justification

**Telemetry:**
```json
{
  "agent": "quinn-quality-v2",
  "command": "validate-quality-gate",
  "task_id": "task-auth-001",
  "routing": {
    "complexity_score": 40
  },
  "execution": {
    "quality_score": 78,
    "gate_decision": "PASS",
    "issues_critical": 0,
    "issues_high": 2,
    "coverage_percent": 87,
    "nfr_failures": 0,
    "waiver_applied": false,
    "duration_ms": 60000
  }
}
```

---

### Command 4: `*trace-requirements` ⭐ LOW PRIORITY

**Purpose:** Trace requirements to implementation and tests

**Syntax:** `@quinn *trace-requirements <task-id>`

**Complexity Factors:**
- Requirement count (30%): 1-5=10, 6-10=40, 11-20=70, 21+=90
- Implementation complexity (25%): Simple=10, Moderate=50, Complex=90
- Test coverage (20%): Complete=10, Partial=50, Minimal=90
- Documentation (15%): Complete=10, Partial=50, Missing=90
- Traceability gaps (10%): None=10, Minor=50, Significant=90

**Routes:**
- Simple tracing (≤30): Few requirements, clear traceability
- Standard tracing (31-60): Moderate complexity
- Complex tracing (>60): Many requirements, gaps

**Skills used:**
- `.claude/skills/quality/trace-requirements/SKILL.md`

**Guardrails:**
- All requirements traced
- Gaps identified
- Coverage verified
- Traceability matrix complete

**Telemetry:**
```json
{
  "agent": "quinn-quality-v2",
  "command": "trace-requirements",
  "task_id": "task-auth-001",
  "routing": {
    "complexity_score": 30
  },
  "execution": {
    "requirements_total": 8,
    "requirements_traced": 8,
    "gaps_found": 0,
    "coverage_percent": 100,
    "duration_ms": 120000
  }
}
```

---

### Command 5: `*assess-risk` ⭐ LOW PRIORITY

**Purpose:** Assess technical and business risks

**Syntax:** `@quinn *assess-risk <task-id>`

**Complexity Factors:**
- Risk count (30%): 1-3=10, 4-6=40, 7-10=70, 11+=90
- Impact (25%): Low=10, Medium=50, High=80, Critical=90
- Likelihood (20%): Rare=10, Possible=50, Likely=80, Certain=90
- Mitigation complexity (15%): Simple=10, Moderate=50, Complex=90
- Dependencies (10%): None=10, Few=40, Many=70, External=90

**Routes:**
- Low risk (≤30): Few risks, low impact
- Medium risk (31-60): Moderate risks
- High risk (>60): Many/severe risks, escalation

**Skills used:**
- `.claude/skills/quality/risk-profile/SKILL.md`

**Guardrails:**
- All risks identified
- Mitigation plans documented
- Escalation for high risks
- Risk matrix complete

**Telemetry:**
```json
{
  "agent": "quinn-quality-v2",
  "command": "assess-risk",
  "task_id": "task-auth-001",
  "routing": {
    "complexity_score": 45
  },
  "execution": {
    "risks_identified": 5,
    "risks_high": 1,
    "risks_medium": 2,
    "risks_low": 2,
    "mitigation_plans": 5,
    "escalation_required": false,
    "duration_ms": 90000
  }
}
```

---

## Implementation Steps

### Step 1: Backup and Setup (5 minutes)

```bash
# Backup current quinn-quality
cp .claude/agents/quinn-quality.md .claude/agents/quinn-quality-v1.md

# Create new quinn-quality V2 file
# You'll write to .claude/agents/quinn-quality-v2.md first
# Then replace the original after completion
```

### Step 2: Create File Structure (10 minutes)

**File structure:**
```markdown
---
name: quinn-quality-v2
description: Quality subagent with intelligent routing, guardrails, and automated verification...
tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
---

# Quinn (Quality) Subagent V2

## Role & Purpose
[Similar to alex-planner V2]

## V2 Enhancements
[List improvements]

## When to Invoke
[When to use Quinn]

## Command: `*review`
[Full 7-step workflow - ~250-300 lines]

## Command: `*assess-nfr`
[Full 7-step workflow - ~150-200 lines]

## Command: `*validate-quality-gate`
[Full 7-step workflow - ~150-200 lines]

## Command: `*trace-requirements`
[Full 7-step workflow - ~100-150 lines]

## Command: `*assess-risk`
[Full 7-step workflow - ~100-150 lines]

## Philosophy
[3-layer architecture benefits]

## Comparison: V1 vs V2
[Table showing improvements]

## Available Commands
[List of 5 commands with checkmarks]

## Usage Examples
[Complete workflow example]

## Integration with Other Subagents
[Handoff points]

## Best Practices
[Guidelines]
```

**Target size:** 900-1,100 lines (similar to alex-planner's 979 lines)

### Step 3: Implement Commands (6-8 hours)

**Priority order:**
1. `*review` (HIGH) - Most complex, most used (~250-300 lines)
2. `*validate-quality-gate` (HIGH) - Critical for workflow (~150-200 lines)
3. `*assess-nfr` (MEDIUM) - Important for quality (~150-200 lines)
4. `*trace-requirements` (LOW) - Less frequently used (~100-150 lines)
5. `*assess-risk` (LOW) - Specialized use case (~100-150 lines)

**For each command:**
1. Write purpose and syntax (5 lines)
2. Define 5 complexity factors with weights (30 lines)
3. Define 3 routes (simple/standard/complex) (30 lines)
4. Define guardrails (20 lines)
5. Write 7-step workflow summary (40 lines)
6. Write telemetry structure (20 lines)
7. Write 1-2 usage examples (30 lines)

**Total per command:** ~175 lines average

### Step 4: Add Supporting Sections (1-2 hours)

1. **Philosophy** (20 lines) - Copy from alex-planner, adapt
2. **Comparison V1 vs V2** (15 lines) - Table format
3. **Available Commands** (20 lines) - List with checkmarks
4. **Usage Examples** (80-100 lines) - Complete workflow
5. **Integration** (60 lines) - Handoff to/from other subagents
6. **Best Practices** (30 lines) - Guidelines

### Step 5: Finalize and Replace (15 minutes)

```bash
# Verify line count
wc -l .claude/agents/quinn-quality-v2.md

# Replace original
mv .claude/agents/quinn-quality.md .claude/agents/quinn-quality-v1.md
mv .claude/agents/quinn-quality-v2.md .claude/agents/quinn-quality.md

# Create completion summary
# Write to docs/QUINN-QUALITY-V2-COMPLETE.md
```

---

## Reference Files

**Templates to follow:**
1. `.claude/agents/james-developer-v2.md` - Original V2 pattern (2,097 lines)
2. `.claude/agents/alex-planner.md` - Just completed V2 (979 lines)

**Copy these patterns exactly:**
- YAML frontmatter format
- 7-step workflow structure
- Complexity factor tables
- Routing logic format
- Guardrails format
- Telemetry JSON structure
- Philosophy section
- Comparison table
- Usage examples format

**Existing quality skills to route to:**
- `.claude/skills/quality/review-task/SKILL.md`
- `.claude/skills/quality/nfr-assess/SKILL.md`
- `.claude/skills/quality/quality-gate/SKILL.md`
- `.claude/skills/quality/trace-requirements/SKILL.md`
- `.claude/skills/quality/risk-profile/SKILL.md`

---

## Quality Gate Decision Logic

**IMPORTANT:** Include this logic in `*validate-quality-gate` command:

```
Quality Score Calculation:
- Base score: 100 points
- Critical issue: -20 points each
- High severity issue: -10 points each
- Medium severity issue: -5 points each
- Low severity issue: -2 points each
- NFR failure: -15 points each
- NFR concern: -5 points each
- Coverage gap (P0): -10 points each
- Coverage gap (P1): -5 points each

Gate Decision:
- PASS: Score ≥80 AND no critical issues AND coverage ≥80%
- CONCERNS: Score 60-79 OR coverage 60-79% OR 1-2 NFR failures
- FAIL: Score <60 OR critical issues exist OR coverage <60% OR 3+ NFR failures
- WAIVED: User explicitly overrides CONCERNS/FAIL with justification

Escalation:
- FAIL decisions → Always escalate to user
- CONCERNS with critical issues → Escalate
- PASS with warnings → Document but don't escalate
```

---

## Expected Output

### Files to Create

1. **`.claude/agents/quinn-quality.md`** (900-1,100 lines)
   - Complete quinn-quality V2 implementation
   - 5 commands with 7-step workflow
   - All sections (philosophy, comparison, examples, etc.)

2. **`.claude/agents/quinn-quality-v1.md`** (backup)
   - Original V1 version preserved

3. **`docs/QUINN-QUALITY-V2-COMPLETE.md`**
   - Completion summary similar to ALEX-PLANNER-V2-COMPLETE.md
   - Statistics, metrics, next steps

### Success Criteria

- ✅ 5 commands implemented
- ✅ All commands have 7-step workflow
- ✅ All commands have complexity assessment (5 factors)
- ✅ All commands have 3 routing options
- ✅ All commands have guardrails
- ✅ All commands have telemetry structure
- ✅ Philosophy and comparison sections complete
- ✅ Usage examples provided
- ✅ Integration points documented
- ✅ File size 900-1,100 lines
- ✅ Follows alex-planner V2 pattern exactly

---

## Common Pitfalls to Avoid

1. **Don't skip complexity factors** - Must have exactly 5 factors per command
2. **Don't skip guardrails** - Each command needs specific guardrails
3. **Don't skip telemetry** - Must include full JSON structure
4. **Don't deviate from 7-step pattern** - Keep consistency
5. **Don't make it too long** - Target 900-1,100 lines (alex-planner is 979)
6. **Don't forget quality gate logic** - Include decision criteria
7. **Don't skip verification section** - Important for quality checks
8. **Don't forget comparison table** - Shows V1 vs V2 improvements

---

## Time Estimates

**By Section:**
- Setup and structure: 15 minutes
- Command 1 (*review): 2-2.5 hours (most complex)
- Command 2 (*validate-quality-gate): 1.5-2 hours
- Command 3 (*assess-nfr): 1.5-2 hours
- Command 4 (*trace-requirements): 1-1.5 hours
- Command 5 (*assess-risk): 1-1.5 hours
- Supporting sections: 1-2 hours
- Finalization and docs: 30 minutes

**Total:** 8-10 hours (2-3 sessions at 3-4 hours each)

**Session breakdown suggestion:**
- **Session 1 (3-4 hours):** Commands 1-2 (*review, *validate-quality-gate)
- **Session 2 (3-4 hours):** Commands 3-5 + supporting sections
- **Session 3 (1-2 hours):** Finalize, test, document

---

## Questions to Ask If Stuck

1. "How did alex-planner implement this section?"
2. "What does the james-developer-v2 version look like?"
3. "Is my complexity assessment using 5 factors with correct weights?"
4. "Do I have all 3 routes defined?"
5. "Is my telemetry structure complete?"
6. "Have I included escalation logic?"
7. "Am I following the 7-step pattern exactly?"

---

## After Completion

### Next in Phase 2

1. ✅ alex-planner V2 (Complete)
2. ✅ quinn-quality V2 (You just finished!)
3. ⏳ orchestrator V2 (6-8 hours) - NEXT
4. ⏳ james-developer-v2 additions (6-8 hours)
5. ⏳ V2 contracts for skills (8-12 hours)

### Create Completion Summary

Document in `docs/QUINN-QUALITY-V2-COMPLETE.md`:
- What was completed
- Statistics (line count, commands, etc.)
- Comparison V1 vs V2
- Next steps
- Phase 2 progress update

---

## Helpful Commands

```bash
# Check current line count
wc -l .claude/agents/quinn-quality-v2.md

# Compare with reference
wc -l .claude/agents/alex-planner.md

# View specific sections
head -50 .claude/agents/alex-planner.md  # YAML + intro
tail -100 .claude/agents/alex-planner.md  # Examples + practices

# Search for patterns
grep -n "Command:" .claude/agents/alex-planner.md
grep -n "Complexity Factors:" .claude/agents/alex-planner.md
grep -n "Routes:" .claude/agents/alex-planner.md

# Backup before major changes
cp .claude/agents/quinn-quality-v2.md .claude/agents/quinn-quality-v2.md.backup
```

---

## Key Success Factors

1. **Follow the pattern exactly** - Don't invent new structures
2. **Use alex-planner as your template** - It's the most recent
3. **Keep it concise** - Don't over-explain, match the style
4. **Include all sections** - Philosophy, comparison, examples, integration
5. **Test as you go** - Verify each command before moving to next
6. **Document thoroughly** - Create completion summary when done
7. **Stay focused** - 8-10 hours total, pace yourself

---

## Final Checklist Before Completion

- [ ] YAML frontmatter complete (name, description, tools, model)
- [ ] V2 Enhancements section present
- [ ] All 5 commands implemented
- [ ] Each command has 7-step workflow
- [ ] Each command has 5 complexity factors with weights
- [ ] Each command has 3 routes
- [ ] Each command has guardrails
- [ ] Each command has telemetry JSON
- [ ] Quality gate decision logic included
- [ ] Philosophy section complete
- [ ] Comparison table present
- [ ] Available Commands section with checkmarks
- [ ] Usage examples provided (at least 1 complete workflow)
- [ ] Integration points documented (james, alex, orchestrator)
- [ ] Best practices listed
- [ ] File size 900-1,100 lines
- [ ] quinn-quality-v1.md backup created
- [ ] Completion summary written

---

## Good Luck!

You have all the context, templates, and patterns needed. Follow alex-planner V2
closely, adapt for quality concerns, and you'll have quinn-quality V2 complete
in 8-10 hours.

**Remember:** Quality over speed. Better to take 10 hours and get it right than
rush in 6 hours and need to redo it.

**You got this!** 🚀

---

**Document Version:** 1.0
**Last Updated:** January 31, 2025
**Next Session Task:** Implement quinn-quality V2
