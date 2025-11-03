# Skills Books - Integration Guide for Existing Skills and Subagents

**Version:** 1.0
**Date:** 2025-11-03
**Purpose:** Guide for integrating existing skills with subagents from book chapters
**Target Audience:** BMAD Enhanced developers enhancing subagent coordination

---

## Table of Contents

1. [Overview](#overview)
2. [Understanding the Integration Model](#understanding-the-integration-model)
3. [Workflow: Integrating Skills to Subagents](#workflow-integrating-skills-to-subagents)
4. [Book-Based Skill Integration](#book-based-skill-integration)
5. [Subagent Enhancement from Books](#subagent-enhancement-from-books)
6. [Routing Logic Development](#routing-logic-development)
7. [Testing Integration](#testing-integration)
8. [Complete Examples](#complete-examples)
9. [Common Integration Patterns](#common-integration-patterns)
10. [Troubleshooting](#troubleshooting)

---

## Overview

### What This Guide Provides

This guide shows you how to **integrate existing skills with subagents** using knowledge from technical books to enhance routing, decision-making, and coordination.

**Key Activities:**
- ✅ **Add skills to subagent routing** - Connect existing skills to subagents
- ✅ **Enhance routing logic** - Use book frameworks to improve skill selection
- ✅ **Update subagent coordination** - Implement book-based decision-making
- ✅ **Add guardrails** - Apply book principles as safety checks
- ✅ **Test integration** - Verify skills work correctly with subagents

### Difference from "Full Layer Books.md"

**Full Layer Books.md:**
- Creates NEW skills/primitives/subagents from books
- Focus: Building components from scratch
- Time: 2-8 hours per component

**Skills Books.md (this guide):**
- Integrates EXISTING skills with subagents
- Focus: Connection and coordination
- Time: 30 minutes - 2 hours per integration

### When to Use This Guide

**Use this guide when:**
- ✅ You have existing skills that need subagent integration
- ✅ You want to add book-based routing to existing subagents
- ✅ You need to enhance subagent decision-making
- ✅ You want to apply book principles to coordination
- ✅ You have multiple skills that need intelligent routing

**Use "Full Layer Books.md" when:**
- ❌ You need to create NEW skills from book chapters
- ❌ You need to build primitives or workflow skills
- ❌ You're starting from scratch

---

## Understanding the Integration Model

### The Coordination Layer (Layer 3)

**Subagents (Layer 3) coordinate skills (Layer 1 & 2):**

```
┌─────────────────────────────────────────────────────────┐
│  SUBAGENT (Layer 3)                                     │
│  .claude/agents/example-agent.md                        │
│                                                          │
│  Responsibilities:                                       │
│  1. Assess context (using book frameworks)              │
│  2. Route to appropriate skill (book-based logic)       │
│  3. Enforce guardrails (book principles)                │
│  4. Verify success (book criteria)                      │
│                                                          │
│  Routing Map (from book):                               │
│  ┌──────────────────────────────────┐                  │
│  │ Low complexity  → skill-a        │                  │
│  │ Medium complexity → skill-b      │                  │
│  │ High complexity → skill-c        │                  │
│  └──────────────────────────────────┘                  │
└─────────────────────────────────────────────────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ↓                 ↓                 ↓
┌────────────┐    ┌────────────┐    ┌────────────┐
│ SKILL A    │    │ SKILL B    │    │ SKILL C    │
│ (Layer 2)  │    │ (Layer 2)  │    │ (Layer 2)  │
│            │    │            │    │            │
│ Simple     │    │ Standard   │    │ Complex    │
│ workflow   │    │ workflow   │    │ workflow   │
└────────────┘    └────────────┘    └────────────┘
```

### Key Integration Points

**1. Routing Logic** (Primary focus)
- Book provides decision framework
- Maps context → skill selection
- Example: "Refactoring" book → smell type → refactoring skill

**2. Guardrails** (Safety layer)
- Book provides principles and limits
- Prevents incorrect skill usage
- Example: "Never refactor without tests" (Fowler)

**3. Quality Gates** (Verification layer)
- Book provides success criteria
- Verifies skill outputs
- Example: "Tests must pass" (TDD)

**4. Escalation Triggers** (Human-in-loop)
- Book provides guidance on when to escalate
- Identifies scenarios requiring human judgment
- Example: "Architectural changes need review" (Clean Architecture)

---

## Workflow: Integrating Skills to Subagents

### Phase 1: Inventory and Analysis (30 minutes)

**Step 1: List Existing Skills**

```bash
# List all available skills
find .claude/skills -name "SKILL.md" -type f

# Organize by domain
ls -la .claude/skills/development/
ls -la .claude/skills/planning/
ls -la .claude/skills/quality/
```

**Create Skill Inventory:**
```markdown
## Skill Inventory for [Subagent Name]

### Development Skills
1. **implement-feature** (.claude/skills/development/implement-feature/)
   - Purpose: TDD-based feature implementation
   - Complexity: Medium
   - Current usage: James (developer) subagent

2. **fix-issue** (.claude/skills/development/fix-issue/)
   - Purpose: Debug and fix bugs
   - Complexity: Variable
   - Current usage: James (developer) subagent

3. **refactor-code** (.claude/skills/quality/refactor-code/)
   - Purpose: Improve code design
   - Complexity: Medium-High
   - Current usage: Not integrated yet ← INTEGRATION OPPORTUNITY

### Planning Skills
[Continue listing...]

### Quality Skills
[Continue listing...]
```

**Step 2: Identify Subagent(s)**

```bash
# List existing subagents
ls -la .claude/agents/
```

**Subagent Analysis:**
```markdown
## Subagent: [Name]

**Current Responsibilities:**
- [Responsibility 1]
- [Responsibility 2]

**Skills Currently Used:**
1. [skill-a] - [When used]
2. [skill-b] - [When used]

**Skills Missing/Could Use:**
1. [skill-x] - [Why needed]
2. [skill-y] - [Why needed]

**Book Reference Opportunity:**
- Book: [Book Title]
- Chapter: [X]
- Framework: [Framework name for routing]
```

**Step 3: Identify Integration Needs**

**Questions to Answer:**
1. Which skills should this subagent route to?
2. What decision logic determines routing? (Book framework?)
3. What guardrails apply? (Book principles?)
4. What are success criteria? (Book quality gates?)

**Integration Needs Template:**
```markdown
## Integration Needs: [Subagent] + [Skills]

**Routing Decision Framework:**
- Source: [Book Title, Chapter X]
- Decision factors: [List from book]
- Routing map: [Condition → Skill mapping]

**Guardrails Needed:**
- Source: [Book Title, Chapter Y]
- Hard limits: [From book]
- Escalation triggers: [From book]

**Quality Gates:**
- Source: [Book Title, Chapter Z]
- Success criteria: [From book]
- Verification approach: [How to check]
```

---

### Phase 2: Develop Routing Logic from Books (1-2 hours)

**Step 1: Extract Decision Framework from Book**

**Template:**
```markdown
## Routing Framework: [Framework Name]

**Source:** [Book Title], Chapter [X], Pages [Y-Z]

**Decision Factors (from book):**

### Factor 1: [Name]
**Description:** [From book]
**Measurement:** [How to assess]
**Values:**
- Low: [Definition from book]
- Medium: [Definition from book]
- High: [Definition from book]

### Factor 2: [Name]
[Repeat structure]

### Factor 3: [Name]
[Repeat structure]

---

## Routing Rules (from book)

**Rule 1:** [Condition from book]
→ **Action:** Route to [skill-name]
→ **Rationale:** [Why, from book]
→ **Book Reference:** Chapter [X], Page [Y]

**Rule 2:** [Condition from book]
→ **Action:** Route to [skill-name]
→ **Rationale:** [Why, from book]
→ **Book Reference:** Chapter [A], Page [B]

[Continue for all rules...]

---

## Decision Tree

```
[Visual representation of routing logic from book]

Assess Context
    │
    ├─ [Factor 1]
    │   ├─ Low → [skill-a] (Chapter X)
    │   ├─ Medium → [skill-b] (Chapter Y)
    │   └─ High → [skill-c] (Chapter Z)
    │
    └─ [Factor 2]
        ├─ [Condition A] → [skill-d]
        └─ [Condition B] → [skill-e]
```
```

**Example from "Refactoring" book:**
```markdown
## Routing Framework: Smell-Driven Refactoring

**Source:** Refactoring by Martin Fowler, Chapter 3, Pages 75-88

**Decision Factors:**

### Factor 1: Code Smell Severity
**Description:** How serious is the code smell (from Chapter 3)
**Measurement:** Smell type + affected lines + impact
**Values:**
- Critical: Duplicate Code, Long Method (>50 lines), Large Class (>300 lines)
- Major: Feature Envy, Data Clumps, Switch Statements
- Minor: Long Parameter List (4-5 params), Comments

### Factor 2: Refactoring Scope
**Description:** How many files/classes affected
**Values:**
- Single method: 1-2 methods in 1 file
- Single class: Multiple methods, 1 class
- Multiple classes: Architectural impact

---

## Routing Rules

**Rule 1: Critical Smell + Single Method**
→ **Action:** Route to `refactor-code-smell` skill
→ **Rationale:** Direct smell → refactoring mapping (Fowler, Chapter 6)
→ **Book Reference:** Chapter 6, Page 110 (Extract Method)

**Rule 2: Critical Smell + Multiple Classes**
→ **Action:** Route to `refactor-architecture` skill
→ **Rationale:** Needs architectural redesign (Fowler, Chapter 8)
→ **Book Reference:** Chapter 8, Page 167 (Move Method, Extract Class)

**Rule 3: Minor Smell + Good Test Coverage**
→ **Action:** Route to `refactor-code-smell` skill (low priority)
→ **Rationale:** Safe to refactor with tests (Fowler principle)
→ **Book Reference:** Chapter 2, Page 17 (Refactoring requires tests)

**Rule 4: Any Smell + No Tests**
→ **Action:** Escalate to user (write tests first)
→ **Rationale:** Cannot safely refactor without tests (Fowler principle)
→ **Book Reference:** Chapter 2, Page 17
```

**Step 2: Map Skills to Routing Rules**

**Create Skill Mapping:**
```markdown
## Skill Mapping for [Subagent]

**From [Book Framework]:**

### Skill A: [skill-name]
**Path:** .claude/skills/[domain]/[skill-name]/SKILL.md
**When to Use (from book):**
- [Condition 1 from book]
- [Condition 2 from book]
**Book Reference:** Chapter [X], Page [Y]
**Example Scenario:** [From book]

### Skill B: [skill-name]
[Repeat structure]

### Skill C: [skill-name]
[Repeat structure]

---

## Alternative Skills (Fallbacks)

**If [condition], use alternative:**
- Primary blocked → Use [alternative-skill]
- Complexity too high → Escalate to user
- Prerequisites missing → Use [prep-skill] first

**From Book:** [Reference to book's guidance on alternatives]
```

**Step 3: Define Guardrails from Book**

**Guardrails Template:**
```markdown
## Guardrails for [Subagent]

**Source:** [Book Title], Chapter [X]

### Hard Limits (Never Exceed)

**Limit 1: [Name]**
- **Source:** Chapter [X], Page [Y]
- **Rule:** [Specific limit from book]
- **Rationale:** [Why this limit exists, from book]
- **Check:** [How to verify]
- **If violated:** [Action - block/escalate]

**Limit 2: [Name]**
[Repeat structure]

---

### Quality Gates (Must Pass)

**Gate 1: [Name]**
- **Source:** Chapter [A], Page [B]
- **Check:** [What to verify, from book]
- **Pass criteria:** [From book]
- **Fail action:** [What to do if fails]

**Gate 2: [Name]**
[Repeat structure]

---

### Escalation Triggers

**Trigger 1: [Description]**
- **Source:** Chapter [C], Page [D]
- **Condition:** [When to escalate, from book]
- **Reason:** [Why escalation needed, from book]
- **Action:** [Escalate with context]

**Trigger 2: [Description]**
[Repeat structure]
```

**Example from "Refactoring" book:**
```markdown
## Guardrails for Refactoring Specialist

**Source:** Refactoring by Martin Fowler, Chapter 2

### Hard Limits

**Limit 1: No Refactoring Without Tests**
- **Source:** Chapter 2, Page 17
- **Rule:** Tests must exist with >50% coverage before refactoring
- **Rationale:** "Refactoring requires tests" (Fowler's core principle)
- **Check:** Run test suite, verify coverage
- **If violated:** Block refactoring, escalate with recommendation to write tests

**Limit 2: Never Break Tests**
- **Source:** Chapter 2, Page 19
- **Rule:** All tests must pass after each refactoring step
- **Rationale:** Tests verify behavior preservation (Fowler principle)
- **Check:** Run tests after refactoring
- **If violated:** Undo refactoring immediately, try smaller steps

**Limit 3: No Mixed Changes**
- **Source:** Chapter 2, Page 18 ("Two Hats")
- **Rule:** Never refactor and add features simultaneously
- **Rationale:** Keeps changes focused and safe
- **Check:** Review change scope
- **If violated:** Split into separate tasks

---

### Quality Gates

**Gate 1: Test Verification**
- **Source:** Chapter 2, Page 17
- **Check:** All tests pass after refactoring
- **Pass criteria:** 100% test passage rate
- **Fail action:** Undo refactoring, review mechanics, try smaller steps

**Gate 2: Code Quality Improvement**
- **Source:** Implied throughout book
- **Check:** At least one quality metric improved
- **Pass criteria:** Reduced length, complexity, or duplication
- **Fail action:** Reconsider refactoring choice

---

### Escalation Triggers

**Trigger 1: No Tests Exist**
- **Source:** Chapter 2, Page 17
- **Condition:** Code has no test suite or <50% coverage
- **Reason:** Cannot safely refactor without tests
- **Action:** Escalate: "Tests required. Recommend writing tests before refactoring. See Fowler, Chapter 2."

**Trigger 2: Architectural Change Needed**
- **Source:** Chapter 2, implied
- **Condition:** Refactoring requires changing class hierarchies or module boundaries
- **Reason:** Large refactorings need human judgment
- **Action:** Escalate: "Architectural change detected. Recommend human review. See Fowler, Chapter 12 [Large Refactorings]."
```

---

### Phase 3: Update Subagent File (30-60 minutes)

**Step 1: Read Current Subagent**

```bash
# Read current subagent file
cat .claude/agents/[agent-name].md
```

**Step 2: Add Routing Logic**

**Update subagent .md file with routing section:**

**Template:**
```markdown
---
name: [agent-name]
description: [Updated description mentioning book-based routing]
tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
source:
  book: "[Book Title]"
  author: "[Author Name]"
  routing_framework: "[Framework Name]"
---

# [Agent Name] Subagent

## Role

[Existing role description]

**Enhanced with:** [Book Title] by [Author Name]
- Routing framework: [Framework Name] (Chapter [X])
- Decision-making: [Approach from book]
- Guardrails: [Principles from book]

---

## Decision-Making Framework

**From [Book Title], Chapter [X]:**

This subagent uses [Framework Name] to route requests to appropriate skills.

**Assessment Criteria (from book):**

1. **[Criterion 1]** (Chapter [X], Page [Y])
   - [Description from book]
   - Low: [Definition] → [skill-a]
   - Medium: [Definition] → [skill-b]
   - High: [Definition] → [skill-c]

2. **[Criterion 2]** (Chapter [A], Page [B])
   [Repeat structure]

3. **[Criterion 3]** (Chapter [C], Page [D])
   [Repeat structure]

---

## Command: *[command-name]

### Workflow

**Based on:** [Book Title], Chapter [X]

**Step 1: Assess Context**

[Existing or new assessment logic using book framework]

Calculate [score/classification]:
```
[Formula from book]
```

**Step 2: Route to Skill**

**Routing Rules (from book):**

**[Condition A]:**
- **Book reference:** Chapter [X], Page [Y]
- **Condition:** [Detailed condition from book]
- **Skill:** `.claude/skills/[domain]/[skill-a]/SKILL.md`
- **Rationale:** [Why this skill, from book]

**[Condition B]:**
- **Book reference:** Chapter [A], Page [B]
- **Condition:** [Detailed condition from book]
- **Skill:** `.claude/skills/[domain]/[skill-b]/SKILL.md`
- **Rationale:** [Why this skill, from book]

[Continue for all conditions...]

Execute selected skill.

**Step 3: Verify Success**

**Success Criteria (from book):**
- ✅ [Criterion 1] - Chapter [X]
- ✅ [Criterion 2] - Chapter [Y]

[Continue with existing verification or add book-based checks]

**Step 4: Emit Telemetry**

[Existing telemetry or add book reference tracking]

---

## Guardrails

**From [Book Title]:**

### Hard Limits

[Add guardrails from Step 3 of Phase 2]

### Quality Gates

[Add quality gates from Step 3 of Phase 2]

### Escalation Triggers

[Add escalation triggers from Step 3 of Phase 2]

---

## Book References

**Routing Framework:**
- Title: [Book Title]
- Author: [Author Name]
- Key Chapters:
  - Chapter [X]: [Topic] - [Routing framework]
  - Chapter [Y]: [Topic] - [Guardrails]
  - Chapter [Z]: [Topic] - [Quality gates]

---

*Enhanced routing based on [Book Title] by [Author Name]*
```

**Step 3: Test Integration**

```bash
# Test routing with different scenarios

# Scenario 1: Low complexity (from book)
# Expected: Routes to [skill-a]
# @[agent-name] *command "low complexity request"

# Scenario 2: Medium complexity (from book)
# Expected: Routes to [skill-b]
# @[agent-name] *command "medium complexity request"

# Scenario 3: High complexity (from book)
# Expected: Routes to [skill-c] or escalates
# @[agent-name] *command "high complexity request"

# Scenario 4: Guardrail violation (from book)
# Expected: Blocked with warning
# @[agent-name] *command "request that violates hard limit"

# Scenario 5: Quality gate failure
# Expected: Appropriate handling per book
# [After skill execution, verify quality checks applied]
```

---

### Phase 4: Documentation and Validation (30 minutes)

**Step 1: Update Usage Documentation**

```bash
# Create or update usage guide
cat > docs/agents/[agent-name]-usage.md <<EOF
# [Agent Name] Usage Guide

**Enhanced with:** [Book Title] by [Author Name]

## Routing Logic

This subagent uses [Framework Name] from [Book Title] to intelligently route requests.

**Decision Factors:**
1. [Factor 1] - Chapter [X]
2. [Factor 2] - Chapter [Y]
3. [Factor 3] - Chapter [Z]

**Routing Map:**
- [Condition A] → [skill-a] (Chapter [X])
- [Condition B] → [skill-b] (Chapter [Y])
- [Condition C] → [skill-c] (Chapter [Z])

## Available Skills

### [skill-a]
**Used when:** [From book]
**Book reference:** Chapter [X], Page [Y]
**Example:** [Scenario from book]

### [skill-b]
[Repeat structure]

### [skill-c]
[Repeat structure]

## Guardrails

**Hard Limits (from book):**
- [Limit 1] - Chapter [A]
- [Limit 2] - Chapter [B]

**Quality Gates:**
- [Gate 1] - Chapter [C]
- [Gate 2] - Chapter [D]

## Examples

**Example 1:** [From book]
\`\`\`
@[agent-name] *command "scenario from book"
\`\`\`
**Expected routing:** [skill-name] (Chapter [X])
**Rationale:** [Why, from book]

[Continue with more examples]

## Book References

- [Book Title] by [Author Name]
- Framework: [Framework Name]
- Chapters: [List]
EOF
```

**Step 2: Validation Checklist**

```markdown
## Integration Validation: [Subagent] + [Skills]

### Routing Logic
- [ ] Decision framework extracted from book
- [ ] All routing rules reference book chapter/page
- [ ] Decision tree visualized
- [ ] Skill mapping complete

### Guardrails
- [ ] Hard limits from book identified
- [ ] Quality gates from book defined
- [ ] Escalation triggers from book captured
- [ ] All guardrails reference book

### Skills Integration
- [ ] All relevant skills listed
- [ ] Skill paths correct
- [ ] Conditions for each skill clear
- [ ] Fallback/alternative skills identified

### Testing
- [ ] Tested with low complexity scenario
- [ ] Tested with medium complexity scenario
- [ ] Tested with high complexity scenario
- [ ] Tested guardrail violations
- [ ] Tested quality gate checks

### Documentation
- [ ] Subagent file updated
- [ ] Book references inline
- [ ] Usage guide created/updated
- [ ] Examples from book included

### Quality
- [ ] Subagent follows single .md file pattern
- [ ] All routing logic inline (not in separate files)
- [ ] Book attribution complete
- [ ] No hardcoded assumptions
```

---

## Book-Based Skill Integration

### Pattern 1: "Refactoring" Book → Developer Subagent

**Goal:** Integrate refactoring skills using Fowler's smell-driven framework

**Steps:**

1. **Extract Framework** (from Chapter 3: "Bad Smells in Code")
   - Smell catalog
   - Severity assessment
   - Refactoring recommendations

2. **Map Skills:**
   - Low complexity smell → `refactor-code-smell` skill
   - High complexity smell → `refactor-architecture` skill
   - No tests → Escalate

3. **Add Guardrails** (from Chapter 2: "Principles in Refactoring")
   - Hard limit: Never refactor without tests
   - Hard limit: Never break tests
   - Hard limit: Never mix refactoring and features

4. **Update Subagent:**
   ```markdown
   ## Command: *refactor

   ### Step 1: Assess Code Smell
   Use Fowler's catalog (Chapter 3) to identify smell and severity.

   ### Step 2: Route to Skill
   - Critical smell + single method → refactor-code-smell
   - Critical smell + multiple classes → refactor-architecture
   - Any smell + no tests → Escalate

   [Continue with routing logic...]
   ```

**Result:** Developer subagent now routes refactoring requests using Fowler's proven framework.

---

### Pattern 2: "Test-Driven Development" Book → Developer Subagent

**Goal:** Integrate TDD workflow using Beck's Red-Green-Refactor cycle

**Steps:**

1. **Extract Framework** (from Chapter 6: "Red-Green-Refactor")
   - Three-step cycle
   - Test-first principle
   - Continuous refactoring

2. **Map Skills:**
   - New feature with tests → `tdd-workflow` skill
   - New feature without tests → `implement-feature` skill (writes tests first)
   - Bug with tests → `fix-issue` skill (test reproduces bug first)

3. **Add Guardrails** (from Beck's principles)
   - Hard limit: "Never write production code without failing test"
   - Hard limit: "Write only enough code to pass test"
   - Quality gate: All tests must pass

4. **Update Subagent:**
   ```markdown
   ## Command: *implement

   ### Step 1: Check for Tests
   - Tests exist → Use tdd-workflow skill
   - No tests → Start with test creation (Beck principle)

   ### Step 2: Follow Red-Green-Refactor
   Execute skill with Beck's three-step cycle:
   1. RED: Write failing test
   2. GREEN: Make test pass
   3. REFACTOR: Improve design

   [Continue with routing logic...]
   ```

**Result:** Developer subagent enforces TDD methodology per Beck's book.

---

### Pattern 3: "Clean Architecture" Book → Architecture Reviewer

**Goal:** Integrate architecture validation using Martin's principles

**Steps:**

1. **Extract Framework** (from Part IV: "Component Principles")
   - Component cohesion principles
   - Component coupling principles
   - Architecture boundaries

2. **Map Skills:**
   - Architecture document → `validate-architecture` skill
   - Boundary violations → `review-architecture` skill
   - Coupling issues → `refactor-architecture` skill

3. **Add Guardrails** (from Martin's principles)
   - Hard limit: Dependencies must point inward (Dependency Rule)
   - Hard limit: No framework dependencies in business logic
   - Quality gate: All boundaries well-defined

4. **Update Subagent:**
   ```markdown
   ## Command: *review-architecture

   ### Step 1: Validate Boundaries
   Use Clean Architecture principles (Chapter 17):
   - Check Dependency Rule
   - Verify business logic isolation
   - Assess boundary definitions

   ### Step 2: Route to Skill
   - Boundary violations → review-architecture skill
   - Coupling issues → refactor-architecture skill
   - Complete validation → validate-architecture skill

   [Continue with routing logic...]
   ```

**Result:** Architecture reviewer enforces Clean Architecture principles.

---

### Pattern 4: "Design Patterns" Book → Pattern Selector

**Goal:** Integrate pattern application using Gang of Four catalog

**Steps:**

1. **Extract Framework** (from Introduction: "What Is a Design Pattern?")
   - Pattern selection criteria
   - Problem classification
   - Trade-offs

2. **Map Skills:**
   - Creational problem → `apply-creational-pattern` skill
   - Structural problem → `apply-structural-pattern` skill
   - Behavioral problem → `apply-behavioral-pattern` skill

3. **Add Guardrails** (from GoF principles)
   - Hard limit: Pattern must solve actual problem (no over-engineering)
   - Hard limit: Consider simpler solutions first
   - Quality gate: Pattern correctly implements GoF structure

4. **Update Subagent:**
   ```markdown
   ## Command: *apply-pattern

   ### Step 1: Classify Problem
   Use GoF framework to determine pattern type:
   - Object creation issue → Creational pattern
   - Object composition issue → Structural pattern
   - Object interaction issue → Behavioral pattern

   ### Step 2: Select Pattern
   Route based on problem classification (GoF catalog):
   - Creational → apply-creational-pattern
   - Structural → apply-structural-pattern
   - Behavioral → apply-behavioral-pattern

   [Continue with routing logic...]
   ```

**Result:** Pattern selector subagent routes using GoF classification.

---

## Subagent Enhancement from Books

### Enhancement Type 1: Add Book-Based Decision Framework

**Before (simple routing):**
```markdown
## Command: *review

Route to review-task skill.
```

**After (book-enhanced routing):**
```markdown
## Command: *review

**Based on:** Code Complete by Steve McConnell, Chapter 20

### Step 1: Assess Review Type
- [ ] Code review (Chapter 20.1)
- [ ] Design review (Chapter 20.2)
- [ ] Architecture review (Chapter 20.3)

### Step 2: Route to Appropriate Skill
**From McConnell's Review Framework:**

**Code Review (Chapter 20.1):**
- Condition: Code-level changes (methods, functions)
- Skill: `.claude/skills/quality/review-code/SKILL.md`
- Checklist: McConnell's code review checklist (Appendix B)

**Design Review (Chapter 20.2):**
- Condition: Class design, module design
- Skill: `.claude/skills/quality/review-design/SKILL.md`
- Checklist: McConnell's design review checklist

**Architecture Review (Chapter 20.3):**
- Condition: System architecture, component boundaries
- Skill: `.claude/skills/quality/review-architecture/SKILL.md`
- Checklist: McConnell's architecture review checklist

Execute selected skill with appropriate checklist.
```

**Enhancement:** Now routes based on McConnell's review framework with specific checklists.

---

### Enhancement Type 2: Add Book-Based Guardrails

**Before (no guardrails):**
```markdown
## Command: *refactor

Execute refactor-code skill.
```

**After (book-enhanced guardrails):**
```markdown
## Command: *refactor

**Guardrails from Refactoring by Martin Fowler:**

### Pre-Flight Checks
1. **Tests exist?** (Chapter 2, Page 17)
   - [ ] Test suite present
   - [ ] Coverage ≥50%
   - If NO: Block and escalate ("Refactoring requires tests")

2. **Tests passing?** (Chapter 2, Page 19)
   - [ ] All tests green
   - If NO: Block and escalate ("Fix tests before refactoring")

3. **Mixed changes?** (Chapter 2, Page 18 - "Two Hats")
   - [ ] Only refactoring (no features)
   - If YES: Block and split ("Keep refactoring separate from features")

### If All Checks Pass
Execute refactor-code skill.

### Post-Flight Checks
1. **Tests still passing?**
   - If NO: Undo immediately (Fowler principle)
2. **Code quality improved?**
   - If NO: Reconsider refactoring choice
```

**Enhancement:** Now enforces Fowler's refactoring principles as guardrails.

---

### Enhancement Type 3: Add Book-Based Quality Gates

**Before (no quality verification):**
```markdown
## Command: *implement

Execute implement-feature skill.
```

**After (book-enhanced quality gates):**
```markdown
## Command: *implement

Execute implement-feature skill.

### Quality Gates (from Test-Driven Development by Kent Beck)

**Gate 1: Test-First Compliance** (Beck's core principle)
- Check: Tests written before production code?
- Pass criteria: Test file timestamp < implementation file timestamp
- Fail action: Escalate ("TDD requires tests first - Beck principle")

**Gate 2: Red-Green-Refactor Followed** (Beck's cycle)
- Check: Tests failed initially, then passed?
- Pass criteria: Git history shows failing commit → passing commit
- Fail action: Warn ("Verify Red-Green cycle followed")

**Gate 3: All Tests Pass** (Beck requirement)
- Check: Test suite passes
- Pass criteria: 100% passage
- Fail action: Block merge ("All tests must pass - Beck principle")

**Gate 4: Sufficient Test Coverage** (Beck guidance)
- Check: Code coverage ≥80%
- Pass criteria: Coverage meets threshold
- Fail action: Escalate ("Increase test coverage per Beck")
```

**Enhancement:** Now verifies Beck's TDD principles as quality gates.

---

### Enhancement Type 4: Add Book-Based Escalation Triggers

**Before (no escalation logic):**
```markdown
## Command: *design-architecture

Execute design-architecture skill.
```

**After (book-enhanced escalation):**
```markdown
## Command: *design-architecture

### Step 1: Assess Architecture Complexity

**From Clean Architecture by Robert C. Martin:**

Calculate complexity:
- Number of components
- Number of boundaries
- External dependencies
- Business rule complexity

### Step 2: Route or Escalate

**Simple Architecture (≤3 components, 1-2 boundaries):**
- Route to: design-simple-architecture skill
- Rationale: Straightforward, low risk

**Medium Architecture (4-6 components, 3-4 boundaries):**
- Route to: design-standard-architecture skill
- Rationale: Requires careful boundary definition (Martin, Chapter 17)

**Complex Architecture (>6 components, >4 boundaries):**
- **ESCALATE TO USER** (Martin guidance)
- Reason: "Large architectures require collaboration and iteration"
- Recommendation: "Suggest iterative approach, starting with core boundaries"
- Book Reference: Chapter 16 ("Independence"), Chapter 33 ("Case Study")

**High External Dependencies (>5 external systems):**
- **ESCALATE TO USER**
- Reason: "Integration complexity requires human judgment"
- Recommendation: "Define clear anti-corruption layers (Chapter 8)"

**Business Logic Uncertainty:**
- **ESCALATE TO USER**
- Reason: "Architecture must reflect clear business rules (Chapter 20)"
- Recommendation: "Clarify business rules before architecture design"
```

**Enhancement:** Now escalates complex scenarios per Clean Architecture guidance.

---

## Routing Logic Development

### Template 1: Complexity-Based Routing (Most Common)

**Source Pattern:** Many books use complexity as routing factor

**Template:**
```markdown
### Step 1: Calculate Complexity Score

**Formula (derived from [Book]):**
```
Complexity = ([Factor 1] × W1) + ([Factor 2] × W2) + ([Factor 3] × W3)

Where:
- Factor 1: [Description] (Weight: W1)
- Factor 2: [Description] (Weight: W2)
- Factor 3: [Description] (Weight: W3)
```

**From Book:** [Chapter X, Page Y]

### Step 2: Route Based on Score

**Low Complexity (Score ≤ [threshold]):**
- Skill: `.claude/skills/[domain]/[simple-skill]/SKILL.md`
- Rationale: [From book]
- Book Reference: [Chapter A, Page B]

**Medium Complexity (Score [threshold] - [threshold]):**
- Skill: `.claude/skills/[domain]/[standard-skill]/SKILL.md`
- Rationale: [From book]
- Book Reference: [Chapter C, Page D]

**High Complexity (Score > [threshold]):**
- Skill: `.claude/skills/[domain]/[complex-skill]/SKILL.md`
- Rationale: [From book]
- Book Reference: [Chapter E, Page F]

**Very High Complexity (Score > [critical threshold]):**
- Action: Escalate to user
- Rationale: [From book - beyond automation]
- Book Reference: [Chapter G, Page H]
```

**Example (Refactoring):**
```markdown
### Step 1: Calculate Refactoring Complexity

**Formula (derived from Fowler):**
```
Complexity = (Lines Affected × 1) + (Classes Affected × 10) + (Has Tests? 0 : 50)
```

### Step 2: Route Based on Score

**Low Complexity (Score ≤ 30):**
- Skill: `.claude/skills/development/refactor-code-smell/SKILL.md`
- Rationale: Simple, isolated refactoring (Fowler, Chapter 6)
- Book Reference: Chapter 6, Page 106 (Extract Method)

**Medium Complexity (Score 31-60):**
- Skill: `.claude/skills/development/refactor-design/SKILL.md`
- Rationale: Requires careful refactoring (Fowler, Chapter 7)
- Book Reference: Chapter 7, Page 142 (Move Method, Extract Class)

**High Complexity (Score > 60):**
- Skill: `.claude/skills/development/refactor-architecture/SKILL.md`
- Rationale: Architectural refactoring (Fowler, Chapter 8)
- Book Reference: Chapter 8, Page 167 (Large refactorings)

**No Tests (Score includes +50):**
- Action: Escalate to user
- Rationale: "Refactoring requires tests" (Fowler core principle)
- Book Reference: Chapter 2, Page 17
```

---

### Template 2: Category-Based Routing

**Source Pattern:** Design Patterns, Architecture styles

**Template:**
```markdown
### Step 1: Classify Problem

**Classification Framework (from [Book]):**

Analyze problem to determine category:
- [ ] Category A: [Description from book]
- [ ] Category B: [Description from book]
- [ ] Category C: [Description from book]

**Decision Criteria:**
[Criteria from book for classification]

### Step 2: Route Based on Category

**Category A:**
- Skill: `.claude/skills/[domain]/[skill-a]/SKILL.md`
- Rationale: [Why this skill for category A, from book]
- Book Reference: [Chapter X, Page Y]
- Example: [Example from book]

**Category B:**
- Skill: `.claude/skills/[domain]/[skill-b]/SKILL.md`
- Rationale: [Why this skill for category B, from book]
- Book Reference: [Chapter A, Page B]
- Example: [Example from book]

**Category C:**
- Skill: `.claude/skills/[domain]/[skill-c]/SKILL.md`
- Rationale: [Why this skill for category C, from book]
- Book Reference: [Chapter C, Page D]
- Example: [Example from book]

**Unclear Category:**
- Action: Escalate with analysis
- Rationale: [From book - need human classification]
```

**Example (Design Patterns):**
```markdown
### Step 1: Classify Problem

**Classification Framework (from Gang of Four):**

Determine pattern type:
- [ ] Creational: Object creation complexity
- [ ] Structural: Object composition issues
- [ ] Behavioral: Object interaction problems

**Decision Criteria (from GoF Introduction):**
- Creational: "How objects are created" (Chapter 3)
- Structural: "How objects are composed" (Chapter 4)
- Behavioral: "How objects interact" (Chapter 5)

### Step 2: Route Based on Category

**Creational Pattern Needed:**
- Skill: `.claude/skills/development/apply-creational-pattern/SKILL.md`
- Rationale: Addresses object creation complexity (GoF, Part 3)
- Book Reference: Chapter 3, Page 81
- Example: Factory Method, Abstract Factory, Singleton

**Structural Pattern Needed:**
- Skill: `.claude/skills/development/apply-structural-pattern/SKILL.md`
- Rationale: Addresses object composition (GoF, Part 4)
- Book Reference: Chapter 4, Page 139
- Example: Adapter, Decorator, Facade

**Behavioral Pattern Needed:**
- Skill: `.claude/skills/development/apply-behavioral-pattern/SKILL.md`
- Rationale: Addresses object interaction (GoF, Part 5)
- Book Reference: Chapter 5, Page 221
- Example: Strategy, Observer, Command

**No Clear Pattern Fit:**
- Action: Escalate
- Rationale: "Consider if pattern is actually needed" (GoF advice)
```

---

### Template 3: Risk-Based Routing

**Source Pattern:** Testing strategies, Quality assurance

**Template:**
```markdown
### Step 1: Assess Risk Level

**Risk Assessment Framework (from [Book]):**

**Risk Factors (from [Book, Chapter X]):**
1. [Factor 1]: [Description] - [Impact level]
2. [Factor 2]: [Description] - [Impact level]
3. [Factor 3]: [Description] - [Impact level]

**Calculate Risk Score:**
```
Risk = ([Factor 1 score] × [Weight]) + ([Factor 2 score] × [Weight]) + ([Factor 3 score] × [Weight])
```

**Risk Levels (from book):**
- Low Risk: Score ≤ [threshold]
- Medium Risk: Score [threshold] - [threshold]
- High Risk: Score > [threshold]

### Step 2: Route Based on Risk

**Low Risk:**
- Skill: `.claude/skills/[domain]/[quick-skill]/SKILL.md`
- Rationale: [From book - can use faster approach]
- Book Reference: [Chapter A, Page B]

**Medium Risk:**
- Skill: `.claude/skills/[domain]/[standard-skill]/SKILL.md`
- Rationale: [From book - needs careful approach]
- Book Reference: [Chapter C, Page D]

**High Risk:**
- Skill: `.claude/skills/[domain]/[thorough-skill]/SKILL.md`
- Rationale: [From book - needs exhaustive approach]
- Book Reference: [Chapter E, Page F]

**Critical Risk:**
- Action: Escalate to user
- Rationale: [From book - too risky to automate]
- Book Reference: [Chapter G, Page H]
```

---

## Testing Integration

### Integration Test Plan

**Test 1: Routing Accuracy**
```markdown
## Test: Verify Routing Logic

**Book Reference:** [Framework from book]

### Test Case 1: Low Complexity Scenario
**Input:** [Scenario from book or derived]
**Expected Routing:** [skill-name] (per book framework)
**Rationale:** [Why this skill, from book Chapter X]
**Verification:**
- [ ] Correctly classified as low complexity
- [ ] Routed to expected skill
- [ ] Rationale matches book framework

### Test Case 2: Medium Complexity Scenario
[Repeat structure]

### Test Case 3: High Complexity Scenario
[Repeat structure]

### Test Case 4: Edge Case from Book
**Input:** [Edge case scenario from book]
**Expected Routing:** [skill-name or escalation]
**Book Reference:** [Chapter X, Page Y discussing this case]
**Verification:**
- [ ] Edge case detected
- [ ] Appropriate routing or escalation
- [ ] Book guidance followed
```

**Test 2: Guardrails Enforcement**
```markdown
## Test: Verify Guardrails

**Book Reference:** [Principles from book]

### Test Case 1: Hard Limit Violation
**Scenario:** [Violate hard limit from book]
**Expected:** Block with warning referencing book
**Book Reference:** [Chapter X, Page Y]
**Verification:**
- [ ] Violation detected
- [ ] Request blocked
- [ ] Warning message references book principle

### Test Case 2: Quality Gate Failure
**Scenario:** [Fail quality gate from book]
**Expected:** [Action per book guidance]
**Book Reference:** [Chapter A, Page B]
**Verification:**
- [ ] Quality gate checked
- [ ] Failure detected
- [ ] Appropriate action taken per book

### Test Case 3: Escalation Trigger
**Scenario:** [Trigger escalation condition from book]
**Expected:** Escalate with book-based recommendation
**Book Reference:** [Chapter C, Page D]
**Verification:**
- [ ] Escalation trigger detected
- [ ] User notified with context
- [ ] Recommendation includes book reference
```

**Test 3: End-to-End Flow**
```markdown
## Test: Complete Workflow

**Book Methodology:** [Methodology name from book]

### Test Scenario: [Complete scenario from book]

**Context:** [Scenario description from book Chapter X]

**Expected Flow:**
1. **Assessment:** [Expected classification per book]
2. **Routing:** [Expected skill selection per book]
3. **Execution:** [Skill executes per book methodology]
4. **Verification:** [Quality gates checked per book]
5. **Result:** [Expected outcome per book]

**Verification:**
- [ ] Each step follows book guidance
- [ ] Book references visible in logs/telemetry
- [ ] Final result matches book expectations
- [ ] No deviations from book methodology
```

---

## Complete Examples

### Example 1: Integrate "Refactoring" Book with Developer Subagent

**Goal:** Add Fowler's smell-driven refactoring framework to james-developer

**Current State:**
```markdown
# james-developer.md (before)

## Command: *refactor

Execute refactor-code skill.
```

**After Integration:**

```markdown
# james-developer-v2.md (after)

---
name: james-developer-v2
description: Developer subagent enhanced with Fowler's smell-driven refactoring framework
tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
source:
  book: "Refactoring: Improving the Design of Existing Code"
  author: "Martin Fowler"
  routing_framework: "Smell-Driven Refactoring"
---

# James Developer V2 Subagent

## Role

Implementation specialist enhanced with Martin Fowler's refactoring methodology.

**Primary Responsibilities:**
1. Feature implementation (TDD-based)
2. Bug fixing
3. **Code refactoring (Fowler's smell-driven approach)** ← NEW

---

## Command: *refactor

**Based on:** Refactoring by Martin Fowler, Chapter 3

### Step 1: Detect Code Smell

**From Fowler's Catalog (Chapter 3):**

Analyze code for smells:
- Long Method (>15 lines)
- Large Class (>100 lines)
- Duplicate Code
- Long Parameter List (>3 params)
- Feature Envy
- Data Clumps
- Primitive Obsession
- Switch Statements

### Step 2: Assess Severity

**Fowler's Severity Classification:**
```
Critical: Duplicate Code, Long Method (>50 lines), Large Class (>300 lines)
Major: Feature Envy, Data Clumps, Switch Statements
Minor: Long Parameter List (4-5 params), Comments
```

Calculate complexity:
```
Complexity = (Lines Affected × 1) + (Classes Affected × 10) + (No Tests? +50 : 0)
```

### Step 3: Route to Skill

**Routing Rules (from Fowler):**

**Simple Refactoring (Complexity ≤30, single smell):**
- **Book reference:** Chapter 6, Extract Method
- **Condition:** Single smell, isolated location, tests exist
- **Skill:** `.claude/skills/development/refactor-code-smell/SKILL.md`
- **Rationale:** Direct smell → refactoring per Fowler catalog
- **Example:** Extract long method (Chapter 6, Page 106)

**Complex Refactoring (Complexity >60, multiple smells):**
- **Book reference:** Chapters 8-9, larger refactorings
- **Condition:** Multiple smells, affects design, tests exist
- **Skill:** `.claude/skills/development/refactor-architecture/SKILL.md`
- **Rationale:** Architectural redesign needed (Fowler, Chapter 8)
- **Example:** Replace conditional with polymorphism (Chapter 10)

**No Tests (Complexity includes +50):**
- **Book reference:** Chapter 2, Page 17
- **Action:** ESCALATE
- **Message:** "Refactoring requires tests. Fowler: 'Whenever I do refactoring, the first step is always the same. I need to build a solid set of tests for that section of code.' Please add tests before refactoring."

Execute selected skill.

### Step 4: Verify Success

**Success Criteria (from Fowler):**
- ✅ All tests still pass (behavior preserved)
- ✅ Code smell eliminated or significantly reduced
- ✅ Code readability improved ("clear intent")
- ✅ No new smells introduced

**Fowler's Verification:**
> "Any fool can write code that a computer can understand. Good programmers write code that humans can understand." (Chapter 1, Page 15)

---

## Guardrails

**From Fowler's Principles (Chapter 2):**

### Hard Limits

**1. Never Refactor Without Tests**
- Source: Chapter 2, Page 17
- Rule: Tests must exist with ≥50% coverage
- Check: Verify test suite exists
- If violated: BLOCK - "Refactoring requires tests (Fowler principle)"

**2. Never Break Tests**
- Source: Chapter 2, Page 19
- Rule: All tests must pass after refactoring
- Check: Run test suite
- If violated: UNDO - "Undo refactoring immediately (Fowler principle)"

**3. Never Mix Refactoring and Features**
- Source: Chapter 2, Page 18 ("Two Hats")
- Rule: Separate refactoring commits from feature commits
- Check: Review change scope
- If violated: SPLIT - "Keep refactoring separate (Fowler 'Two Hats')"

### Quality Gates

**Gate 1: Test Verification**
- Source: Chapter 2, Page 17
- Check: All tests pass after refactoring
- Pass: 100% test passage
- Fail: Undo, review mechanics, try smaller steps

**Gate 2: Code Quality Improvement**
- Check: At least one metric improved
- Pass: Reduced length, complexity, or duplication
- Fail: Reconsider refactoring choice

### Escalation Triggers

**Trigger 1: No Tests**
- Condition: Code has no tests or <50% coverage
- Reason: Cannot safely refactor (Fowler, Chapter 2)
- Action: Escalate - "Write tests first, then refactor"

**Trigger 2: Tests Fail Repeatedly**
- Condition: 3 refactoring attempts, tests still fail
- Reason: May need manual review
- Action: Escalate with failure analysis

**Trigger 3: Architectural Change Needed**
- Condition: Requires changing class hierarchies
- Reason: Large refactorings need judgment (Fowler, Chapter 12)
- Action: Escalate - "Architectural change detected, recommend review"

---

## Book References

**Refactoring Framework:**
- Title: Refactoring: Improving the Design of Existing Code
- Author: Martin Fowler
- Key Chapters:
  - Chapter 2: Principles in Refactoring (methodology)
  - Chapter 3: Bad Smells in Code (routing framework)
  - Chapters 6-11: Refactoring Catalog (techniques)

---

*Enhanced with Smell-Driven Refactoring from Fowler*
```

**Testing:**
```bash
# Test 1: Low complexity with tests
@james *refactor "Extract method from lines 45-60 in calculator.js"
# Expected: Routes to refactor-code-smell skill

# Test 2: High complexity with tests
@james *refactor "Refactor authentication module (5 classes, 500 lines)"
# Expected: Routes to refactor-architecture skill

# Test 3: No tests (guardrail violation)
@james *refactor "Refactor payment processing"
# Expected: BLOCKED - "Refactoring requires tests (Fowler)"

# Test 4: Tests fail after refactoring
# [Simulate refactoring that breaks tests]
# Expected: UNDO immediately with Fowler reference
```

**Result:** James now routes refactoring requests using Fowler's proven framework, enforces Fowler's principles as guardrails, and provides book-referenced guidance.

---

## Common Integration Patterns

### Pattern 1: Framework-Based Routing

**Books:** Most technical books with methodologies

**Pattern:**
1. Extract decision framework from book
2. Map framework to skill selection
3. Add book references inline
4. Enforce framework as guardrails

**Example Books:**
- Refactoring (smell → refactoring mapping)
- Design Patterns (problem type → pattern category)
- Clean Architecture (boundary detection → architecture skill)

---

### Pattern 2: Principle-Based Guardrails

**Books:** Books emphasizing principles and best practices

**Pattern:**
1. Extract core principles from book
2. Convert principles to hard limits
3. Add quality gates from book's success criteria
4. Reference principles in violation messages

**Example Books:**
- Clean Code (principles → code quality guardrails)
- Pragmatic Programmer (practices → development guardrails)
- Release It! (stability patterns → deployment guardrails)

---

### Pattern 3: Checklist-Based Verification

**Books:** Books with comprehensive checklists

**Pattern:**
1. Extract checklists from book
2. Map checklists to quality gates
3. Verify skill outputs against checklist
4. Report checklist pass/fail with book reference

**Example Books:**
- Code Complete (review checklists)
- The Checklist Manifesto (process checklists)
- Effective Java (item-by-item guidelines)

---

### Pattern 4: Risk-Based Escalation

**Books:** Books discussing risk management

**Pattern:**
1. Extract risk assessment from book
2. Calculate risk score per book
3. Route based on risk level
4. Escalate high-risk scenarios with book guidance

**Example Books:**
- Release It! (stability risks)
- Waltzing with Bears (project risks)
- The Phoenix Project (operational risks)

---

## Troubleshooting

### Issue 1: "Routing Logic Too Complex"

**Symptom:** Decision tree has too many branches, hard to follow

**Solution:**
1. Simplify to 3-4 primary routes
2. Group similar conditions
3. Use nested routing (coarse → fine)
4. Document edge cases separately

**Example:**
```markdown
# Instead of 10 separate conditions:
- If A and B and C → skill-1
- If A and B and D → skill-2
- If A and E and C → skill-3
[...]

# Use nested routing:
- If A → Assess B/C/D/E → Route to appropriate skill
- If NOT A → Different branch
```

---

### Issue 2: "Book Framework Doesn't Map Cleanly to Skills"

**Symptom:** Book describes concepts that don't match skill granularity

**Solution:**
1. Create intermediate classification step
2. Map book concepts to skill combinations
3. Use multi-skill workflows
4. Document conceptual mapping

**Example:**
- Book describes "Refactor to Patterns" (multiple steps)
- Skills provide atomic refactorings
- Subagent chains skills to implement pattern

---

### Issue 3: "Multiple Books Cover Same Domain"

**Symptom:** Refactoring covered in Fowler + Clean Code + others

**Solution:**
1. Choose primary source (most authoritative)
2. Note complementary sources in references
3. Use primary for routing, secondary for enrichment
4. Cross-reference where approaches differ

**Example:**
```markdown
## Routing Framework

**Primary Source:** Refactoring by Martin Fowler

**Complementary Sources:**
- Clean Code by Robert C. Martin (Chapter 3: Functions)
  - Reinforces "small methods" principle
- Working Effectively with Legacy Code (Chapter 22)
  - Additional techniques for code without tests

**Routing uses Fowler's framework, enriched with Martin's principles.**
```

---

### Issue 4: "Book Principles Conflict"

**Symptom:** Two books give different advice for same scenario

**Solution:**
1. Document both approaches
2. Choose one as primary (with rationale)
3. Offer alternative as option
4. Explain trade-offs from both books

**Example:**
```markdown
## Conflict: Test Granularity

**Kent Beck (TDD):** Fine-grained unit tests, one assertion per test
**Martin Fowler (Refactoring):** Coarser integration tests acceptable

**Our Approach (Primary: Beck):**
- Default: Fine-grained unit tests (Beck)
- Option: Integration tests for complex interactions (Fowler)
- Rationale: Beck's approach provides better failure isolation

**User Choice:**
@james *test-strategy unit  # Beck approach (default)
@james *test-strategy integration  # Fowler approach
```

---

### Issue 5: "Guardrails Too Restrictive"

**Symptom:** Book principles block legitimate use cases

**Solution:**
1. Add "override with justification" option
2. Log overrides for review
3. Provide escape hatch with warning
4. Track override patterns

**Example:**
```markdown
## Guardrail: Never Refactor Without Tests

**Hard Limit (Fowler):**
- Tests must exist before refactoring

**Override Option:**
- User can override with `--force` and justification
- Warning: "Refactoring without tests is risky (Fowler, Chapter 2)"
- Logged: Override recorded for review
- Recommendation: "Add tests as soon as possible"

**Usage:**
@james *refactor --force "Legacy code, adding tests first would take 2 weeks"
```

---

## Conclusion

### Key Takeaways

1. **Integration Enhances Existing Skills**
   - Books provide routing frameworks
   - Principles become guardrails
   - Success criteria become quality gates

2. **Subagents Coordinate Using Book Knowledge**
   - Decision-making from book frameworks
   - Routing from book classification
   - Guardrails from book principles

3. **Integration Is Faster Than Creation**
   - 30 minutes - 2 hours per integration
   - Reuses existing skills
   - Adds intelligence to coordination

4. **Book References Add Credibility**
   - Users trust book-based decisions
   - Clear rationale for routing
   - Educational for users

5. **Testing Validates Integration**
   - Test routing accuracy
   - Test guardrails enforcement
   - Test quality gates

### Success Metrics

**After integration:**
- ✅ Subagent routes intelligently using book framework
- ✅ All routing decisions reference book chapter/page
- ✅ Guardrails enforce book principles
- ✅ Quality gates verify book success criteria
- ✅ Users see book references in output

### Next Steps

**Immediate:**
1. Choose subagent to enhance
2. Select book with applicable framework
3. Extract routing logic from book
4. Update subagent .md file
5. Test integration

**Long-term:**
1. Enhance all subagents with book frameworks
2. Build library of routing patterns
3. Document integration recipes
4. Share with community

---

## Resources

### Related Guides

- **Full Layer Books.md** - Creating new skills/primitives/subagents from books
- **3-layer-architecture-for-skills.md** - Architecture deep-dive
- **skill-refactoring-template.md** - Skill creation template

### Example Integrations

**In BMAD Enhanced:**
- james-developer-v2.md (example subagent with routing)
- alex-planner.md (example planner with guardrails)
- quinn-quality.md (example QA with quality gates)

### Books for Integration

**High Integration Value:**
1. Refactoring by Martin Fowler ⭐⭐⭐⭐⭐
2. Test-Driven Development by Kent Beck ⭐⭐⭐⭐⭐
3. Clean Code by Robert C. Martin ⭐⭐⭐⭐
4. Design Patterns by Gang of Four ⭐⭐⭐⭐
5. Clean Architecture by Robert C. Martin ⭐⭐⭐⭐

---

**Version:** 1.0
**Last Updated:** 2025-11-03
**Maintained By:** BMAD Enhanced Core Team

---

*Integrate intelligently. Coordinate effectively. Reference credibly.*
