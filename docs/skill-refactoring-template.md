# Skill Refactoring Template (V2 with 3-Layer Architecture)

**Purpose:** Step-by-step template for refactoring BMAD Enhanced skills to full compliance with both skill-creator standards AND 3-layer architecture (Primitives → Workflows → Subagents).

**Time per skill:** 4-5 hours (with practice, 3-4 hours)

**Validated examples:**
- fix-issue ✅ (skill-creator compliant)
- estimate-stories ✅ (skill-creator compliant)
- implement-v2 ✅ (3-layer architecture prototype)

**Compliance Standards:**
- ✅ skill-creator (packaging, progressive disclosure)
- ✅ 3-layer architecture (contracts, telemetry, primitives)

---

## Quick Start Checklist

For each skill, complete these steps in order:

- [ ] **Step 1:** Analyze current skill (15 min)
- [ ] **Step 2:** Create directory structure (5 min)
- [ ] **Step 3:** Add YAML frontmatter with V2 contracts (20 min) ⭐ NEW
- [ ] **Step 4:** Streamline SKILL.md (60 min)
- [ ] **Step 4.5:** Integrate bmad-commands (15 min) ⭐ NEW
- [ ] **Step 5:** Create reference files (90-120 min)
- [ ] **Step 6:** Remove old file (2 min)
- [ ] **Step 7:** Validate compliance (20 min)
- [ ] **Step 8:** Add routing guidance (10 min) ⭐ NEW

**Total:** ~4.5 hours per skill (includes V2 architecture)

---

## Understanding the 3-Layer Architecture

**⚠️ CRITICAL CONCEPT:** All skills you create follow skill-creator patterns (SKILL.md, references/, etc.). The "3 layers" refers to the **ROLE skills play**, not different file structures.

**Skills remain portable, self-contained packages.** Whether a skill plays a "Layer 1" or "Layer 2" role, it's still a skill that can be packaged (via `package_skill.py`), distributed (.zip), and used anywhere.

### Layer 1: Primitives

**What they are:** Skills that bundle executable scripts for atomic, deterministic operations.

**Example:** `bmad-commands`

**Structure:**
```
bmad-commands/
├── SKILL.md          ← It's a skill!
├── scripts/          ← Python scripts bundled IN the skill
│   ├── read_file.py
│   └── run_tests.py
└── references/
```

**Key point:** bmad-commands IS A SKILL (not a separate layer type). It follows skill-creator pattern and is packageable/portable.

### Layer 2: Workflow Skills

**What they are:** Skills that implement workflows, may call primitive skills.

**Examples:** `implement-v2`, `estimate-stories`, `fix-issue`

**Structure:**
```
implement-v2/
├── SKILL.md          ← It's a skill!
└── references/
    ├── tdd-workflow.md
    └── refactoring-patterns.md
```

**Key point:** These are STILL SKILLS (packageable, portable). They just play a different role (composing workflows instead of providing primitives).

### Layer 3: Subagents (NOT Skills)

**What they are:** Coordination files that route requests to appropriate skills.

**Example:** `james-developer-v2`

**Structure:**
```
.claude/agents/james-developer-v2.md  ← Single file (NOT a directory)
```

**Contains (inline):**
- YAML frontmatter (name, description, tools, model)
- Routing logic
- Guardrails
- Workflow instructions

**Key point:** Subagents are NOT skills. They're single .md coordination files (not packageable via skill-creator).

### The Key Principle: Skills Stay Portable

**Your skills MUST remain:**
- ✅ Packageable (via `package_skill.py`)
- ✅ Distributable (.zip files)
- ✅ Self-contained (all dependencies bundled)
- ✅ Portable (work anywhere)

**The 3-layer architecture is about HOW SKILLS WORK TOGETHER, not about creating different file types.**

When you refactor a skill:
- You're creating a SKILL (follows skill-creator pattern)
- That skill might bundle scripts (Layer 1 role)
- Or that skill might use commands (Layer 2 role)
- Or it might be neither (standalone skill)
- But it's ALWAYS a portable, packageable skill

---

## Detailed Steps

### Step 1: Analyze Current Skill (15 minutes)

**Goal:** Understand what needs to be refactored

**Actions:**

1. **Get line count:**
   ```bash
   wc -l .claude/skills/category/skill-name.md
   ```

2. **Identify non-compliant elements:**
   ```bash
   # Check for frontmatter
   head -10 .claude/skills/category/skill-name.md

   # Check for sections to remove
   grep -n "^## " .claude/skills/category/skill-name.md
   ```

3. **List sections to remove:**
   - ❌ "## Invocation"
   - ❌ "## Skill Configuration"
   - ❌ "## Skill Metadata"
   - ❌ "## When to Use This Skill" (if verbose, > 10 lines)
   - ❌ HTML comments (`<!-- ... -->`)

4. **Identify content for references:**
   - Long examples (>50 lines)
   - Detailed patterns/techniques
   - Comprehensive guides
   - Decision trees
   - Templates

5. **Document findings:**
   ```markdown
   ## [skill-name] Analysis

   Current state:
   - Lines: XXX (X.Xx over limit)
   - Frontmatter: ❌ Missing
   - Sections to remove: [list]

   Content to extract:
   - Lines XXX-XXX: [Topic] → references/[filename].md
   - Lines XXX-XXX: [Topic] → references/[filename].md

   Target: <400 lines
   ```

**Output:** Analysis document or notes

---

### Step 2: Create Directory Structure (5 minutes)

**Goal:** Set up proper skill directory

**Commands:**

```bash
# Navigate to skills directory
cd .claude/skills/category

# Create skill directory
mkdir -p skill-name/references

# Optional: Create other directories if needed
mkdir -p skill-name/scripts    # If skill needs executable scripts
mkdir -p skill-name/assets     # If skill needs templates/files
```

**Example:**
```bash
cd .claude/skills/planning
mkdir -p refine-story/references
```

**Result:**
```
.claude/skills/category/skill-name/
├── references/
└── (SKILL.md will go here)
```

---

### Step 3: Add YAML Frontmatter with V2 Contracts (20 minutes)

**Goal:** Create compliant frontmatter with 3-layer architecture support

**V2 Enhanced Template:**
```yaml
---
name: skill-name
description: [One-line description of what skill does and when to use it, <200 chars]
acceptance:
  - criterion_1: "Description of what must be true for completion"
  - criterion_2: "Description of second criterion"
inputs:
  input_name:
    type: string|number|boolean|array|object
    required: true|false
    description: "What this input represents"
outputs:
  output_name:
    type: string|number|boolean|array|object
    description: "What this output represents"
telemetry:
  emit: "skill.skill-name.completed"
  track:
    - metric_1
    - metric_2
    - duration_ms
---
```

---

#### 3.1: Basic Fields (Required)

**name:** Use kebab-case, matches directory name
```yaml
✅ name: fix-issue
✅ name: estimate-stories
✅ name: create-task-spec
❌ name: Fix Issue (not kebab-case)
❌ name: fix_issue (use hyphens, not underscores)
```

**description:** Extract from "## Purpose" section
- One line, <200 characters
- Specific about what skill does
- Explains when to use it
- Imperative/infinitive form

```yaml
✅ description: Debug and fix bugs by reproducing issues, identifying root causes, implementing fixes, and validating without regressions
✅ description: Estimate story points using structured formula based on complexity, effort, and risk for consistent sprint planning
✅ description: Implement features using TDD workflow with bmad-commands for file operations and testing
❌ description: This skill helps you fix bugs (too vague, uses "you")
❌ description: Bug fixing (too short, not descriptive)
```

---

#### 3.2: Acceptance Criteria (Optional but Recommended)

**Purpose:** Define what "done" means for this skill (enables automated verification)

**Guidelines:**

1. **Testable:** Each criterion must be verifiable
   ```yaml
   ✅ acceptance:
     - tests_passing: "All tests must pass"
     - coverage_threshold: "Test coverage >= 80%"
     - no_syntax_errors: "Code must compile without syntax errors"

   ❌ acceptance:
     - code_quality: "Code should be good" (not testable, too vague)
   ```

2. **Specific:** Avoid vague language
   ```yaml
   ✅ stories_created: "All required user stories documented with acceptance criteria"
   ❌ task_done: "Task should be complete" (too vague)
   ```

3. **Minimal:** 2-5 criteria is typical
   - Too few: Under-specified
   - Too many: Over-constrained

**Common Patterns by Skill Type:**

**Development skills (implement, fix, refactor):**
```yaml
acceptance:
  - tests_passing: "All tests must pass"
  - coverage_threshold: "Test coverage >= 80%"
  - no_syntax_errors: "Code must have no syntax errors"
  - requirements_met: "All acceptance criteria from task spec addressed"
```

**Planning skills (estimate, breakdown, refine):**
```yaml
acceptance:
  - stories_created: "Required user stories documented"
  - estimates_provided: "All stories have story point estimates"
  - acceptance_defined: "Each story has clear acceptance criteria"
```

**Quality skills (review, audit, assess):**
```yaml
acceptance:
  - assessment_complete: "All quality dimensions assessed"
  - issues_documented: "All issues logged with severity"
  - recommendations_provided: "Actionable recommendations given"
```

**When to skip:** If skill is purely procedural with no measurable outcomes, acceptance criteria may be omitted.

---

#### 3.3: Inputs and Outputs (Optional)

**Purpose:** Document skill's data contract (enables routing and composition)

**Inputs Example:**
```yaml
inputs:
  task_id:
    type: string
    required: true
    description: "Task identifier (e.g., task-auth-002)"
    validation: "Must match pattern: task-{component}-{number}"

  skip_tests:
    type: boolean
    required: false
    description: "Skip test execution (not recommended)"
    default: false
```

**Outputs Example:**
```yaml
outputs:
  implementation_complete:
    type: boolean
    description: "Whether implementation succeeded"

  files_modified:
    type: array
    description: "List of files created or modified"

  test_coverage_percent:
    type: number
    description: "Achieved test coverage percentage"
```

**Types:**
- `string` - Text
- `number` - Integer or float
- `boolean` - true/false
- `array` - List of items
- `object` - Structured data

**When to define:**
- **Always** if skill accepts parameters
- **Always** if skill produces observable results
- **Skip** if skill is purely procedural (no data in/out)

---

#### 3.4: Telemetry (Recommended for V2)

**Purpose:** Enable observability, debugging, and performance monitoring

**Template:**
```yaml
telemetry:
  emit: "skill.{skill-name}.{event}"
  track:
    - key_metric_1
    - key_metric_2
    - duration_ms
```

**Event Naming:** Use pattern `skill.{name}.{event}`
```yaml
✅ emit: "skill.implement.completed"
✅ emit: "skill.estimate.calculated"
✅ emit: "skill.review.finished"
❌ emit: "done" (not descriptive)
❌ emit: "implementCompleted" (use dots, kebab-case)
```

**Metrics to Track:**

**Always include:**
- `duration_ms` - Execution time

**Common metrics:**
- Counts: `files_modified`, `tests_run`, `issues_found`
- Quality: `coverage_percent`, `complexity_score`
- Outcomes: `success`, `errors_count`

**Examples by Skill Type:**

**Development skills:**
```yaml
telemetry:
  emit: "skill.implement.completed"
  track:
    - task_id
    - files_modified_count
    - tests_total
    - tests_passed
    - coverage_percent
    - duration_ms
```

**Planning skills:**
```yaml
telemetry:
  emit: "skill.estimate.completed"
  track:
    - story_id
    - story_points
    - complexity_score
    - effort_score
    - risk_score
    - duration_ms
```

**Quality skills:**
```yaml
telemetry:
  emit: "skill.review.completed"
  track:
    - task_id
    - issues_found
    - severity_critical
    - severity_major
    - recommendations_count
    - duration_ms
```

---

#### 3.5: Complete Examples

**Example 1: Implementation Skill (Full V2)**
```yaml
---
name: implement
description: Implement features using TDD workflow with bmad-commands for file operations and testing
acceptance:
  - tests_passing: "All tests must pass"
  - coverage_threshold: "Test coverage >= 80%"
  - no_syntax_errors: "Code must have no syntax errors"
  - task_spec_loaded: "Task specification successfully loaded"
inputs:
  task_id:
    type: string
    required: true
    description: "Task identifier (e.g., task-auth-002)"
outputs:
  implementation_complete:
    type: boolean
    description: "Whether implementation is complete"
  test_coverage_percent:
    type: number
    description: "Test coverage percentage achieved"
  files_modified:
    type: array
    description: "List of files created or modified"
telemetry:
  emit: "skill.implement.completed"
  track:
    - task_id
    - test_coverage_percent
    - duration_ms
    - files_modified_count
    - tests_total
    - tests_passed
---
```

**Example 2: Planning Skill (Minimal V2)**
```yaml
---
name: estimate-stories
description: Estimate story points using structured formula based on complexity, effort, and risk for consistent sprint planning
acceptance:
  - estimates_provided: "All stories have story point estimates"
  - formula_applied: "Estimation formula correctly applied"
telemetry:
  emit: "skill.estimate.completed"
  track:
    - story_id
    - story_points
    - duration_ms
---
```

**Example 3: Quality Skill (No Contracts)**
```yaml
---
name: review-task
description: Review task implementation for code quality, test coverage, and adherence to standards
---
```
*(Simple skills without measurable outcomes can skip contracts)*

---

### Step 4: Streamline SKILL.md (60 minutes)

**Goal:** Create lean, focused SKILL.md (<400 lines)

**Structure Template:**

```markdown
---
name: skill-name
description: Brief description
---

# Skill Name

## Purpose

[1-2 paragraphs explaining what this skill does and core principles]

## Prerequisites

- [Prerequisite 1]
- [Prerequisite 2]

---

## Workflow

### 1. First Step

Brief explanation of step purpose.

**Key actions:**
- Action 1
- Action 2

**Example:**
```[language]
// Short example (10-30 lines max)
```

**See:** `references/detailed-file.md` for more examples

---

### 2. Second Step

[Repeat pattern for each step]

---

[Continue for all workflow steps]

---

## Common Scenarios

### Scenario 1: Name

Brief description and approach.

**See:** `references/scenarios.md` for full details

---

## Best Practices

1. **Practice 1** - Brief explanation
2. **Practice 2** - Brief explanation
[...]

---

## Reference Files

- `references/file1.md` - What it contains
- `references/file2.md` - What it contains

---

## When to Escalate

- Situation 1
- Situation 2

---

*Part of BMAD Enhanced [Category] Suite*
```

**Key Principles:**

1. **Keep workflow high-level**
   ```markdown
   ✅ "Analyze complexity using 1-5 scale"
   ❌ "Analyze complexity. Complexity is measured on a 1-5 scale. 1 means trivial where..."  (too verbose)
   ```

2. **Use short examples (10-30 lines)**
   ```markdown
   ✅ Show the pattern in 20 lines
   ❌ Show every variation in 150 lines
   ```

3. **Reference, don't repeat**
   ```markdown
   ✅ "**See:** `references/patterns.md`"
   ❌ Include all 200 lines of patterns inline
   ```

4. **Trust Claude's knowledge**
   ```markdown
   ✅ "Follow TDD approach"
   ❌ "Test-Driven Development (TDD) is a software development process where you write tests before code. It follows Red-Green-Refactor..." (Claude knows this)
   ```

5. **Flexibility over rigidity**
   ```markdown
   ✅ "Validate fix with appropriate tests"
   ❌ "STEP 5.1: Run failing test. STEP 5.2: Run related tests. STEP 5.3: Run full suite." (too prescriptive)
   ```

**Target:** 300-400 lines

---

### Step 4.5: Integrate bmad-commands (15 minutes) ⭐ NEW

**⚠️ IMPORTANT:** bmad-commands IS A SKILL (not a separate layer type).

It's a special skill that:
- Bundles Python scripts in `scripts/` directory
- Follows skill-creator pattern (SKILL.md + scripts/ + references/)
- Is packageable and portable
- Plays "Layer 1" role (provides command primitives)

**Your skill structure stays the same.** You're just CALLING another skill's scripts.

---

**Goal:** Use primitives layer for deterministic operations (applies to implementation/development skills)

**When to Integrate:**
- Skill needs file operations (read/write)
- Skill needs test execution
- Skill needs git operations
- Skill performs other deterministic tasks

**Skip if:**
- Skill is planning-only (estimate, refine, breakdown)
- Skill is quality assessment-only (review, audit)
- Skill has no file/command operations

---

#### 4.5.1: Identify Command Opportunities

Review skill workflow and identify steps that can use bmad-commands:

| Operation | Use Command | Example |
|-----------|-------------|---------|
| Read files | ✅ read_file.py | Reading task specs, config files |
| Write files | ✅ write_file.py | Creating implementation files |
| Run tests | ✅ run_tests.py | Executing test suites |
| Git operations | ✅ (future) | Branch creation, commits |
| API calls | ❌ | Use native tools |
| Planning | ❌ | No commands needed |

---

#### 4.5.2: Update Workflow Steps

**Pattern for calling commands:**

```markdown
### Step X: Read Task Specification

**Action:** Load task specification using bmad-commands

Execute:
```bash
python .claude/skills/bmad-commands/scripts/read_file.py \
  --path workspace/tasks/{task_id}.md \
  --output json
```

**Parse response:**
```json
{
  "success": true,
  "outputs": {
    "content": "...",
    "line_count": 45,
    "size_bytes": 1024
  },
  "telemetry": {...},
  "errors": []
}
```

**Extract:**
- Check `success == true`
- Get task content from `outputs.content`
- Parse task sections (Objective, Acceptance Criteria, etc.)

**If command fails:**
- Review `errors` array
- Common errors: `file_not_found`, `permission_denied`
- Handle gracefully or escalate
```

---

#### 4.5.3: Available Commands

**Currently Available:**

1. **read_file.py**
   - Purpose: Read file contents with metadata
   - Inputs: `--path <file-path>`
   - Outputs: content, line_count, size_bytes
   - Use for: Loading task specs, config files, documentation

2. **run_tests.py**
   - Purpose: Execute tests with structured results
   - Inputs: `--path <test-path> --framework <jest|pytest>`
   - Outputs: passed, total_tests, coverage_percent
   - Use for: Running test suites, verifying implementation

**Reference:** `.claude/skills/bmad-commands/SKILL.md` for complete documentation

---

#### 4.5.4: Benefits of Using Commands

- ✅ **Deterministic:** Same inputs = same outputs
- ✅ **Testable:** Commands can be tested independently
- ✅ **Observable:** Built-in telemetry for all operations
- ✅ **Error handling:** Structured error responses
- ✅ **Composable:** Commands can be chained
- ✅ **Versioned:** Command contracts are documented

---

#### 4.5.5: Example Integration

**Before (ad-hoc):**
```markdown
### Step 1: Load Task Spec

Read the task specification file at workspace/tasks/{task_id}.md
and extract the objective and acceptance criteria.
```

**After (with commands):**
```markdown
### Step 1: Load Task Specification

**Action:** Use bmad-commands to read task spec

Execute:
```bash
python .claude/skills/bmad-commands/scripts/read_file.py \
  --path workspace/tasks/{task_id}.md \
  --output json
```

**Parse response:**
- Verify `success == true`
- Extract `outputs.content` for task specification
- Parse sections: Objective, Acceptance Criteria, Technical Specs

**If file not found:**
- Error: `file_not_found` in `errors` array
- Action: Verify task ID is correct
- Suggest: Create task spec first using create-task-spec skill

Reference: `.claude/skills/bmad-commands/SKILL.md` for detailed usage
```

---

### Step 5: Create Reference Files (90-120 minutes)

**Goal:** Extract detailed content to reference files

**Common Reference File Types:**

#### Type 1: Patterns/Examples

**Filename:** `references/[topic]-patterns.md` or `references/examples.md`

**Purpose:** Catalog common patterns with symptoms, approaches, and examples

**Structure:**
```markdown
# [Topic] Patterns

Introduction

---

## Pattern 1: Name

**Symptoms:**
- Symptom 1
- Symptom 2

**Approach:**
1. Step 1
2. Step 2

**Example:**
```[language]
// Code example
```

---

## Pattern 2: Name

[Repeat structure]
```

**Examples:**
- `references/common-patterns.md` (fix-issue)
- `references/test-examples.md` (fix-issue)

#### Type 2: Techniques/Approaches

**Filename:** `references/[topic]-techniques.md` or `references/approaches.md`

**Purpose:** Systematic techniques for accomplishing tasks

**Structure:**
```markdown
# [Topic] Techniques

Introduction

---

## Technique 1: Name

**When to Use:**
- Situation 1
- Situation 2

**How it Works:**
1. Step 1
2. Step 2

**Example:**
```[language]
code
```

**Tips:**
- Tip 1
- Tip 2
```

**Examples:**
- `references/debugging-techniques.md` (fix-issue)

#### Type 3: Scales/Frameworks

**Filename:** `references/[scale-name]-scale.md`

**Purpose:** Detailed rating scales or frameworks

**Structure:**
```markdown
# [Scale Name] (X-Y Scale)

[Scale description]

---

## Level 1: Label

**Description:** [Description]

**Characteristics:**
- Characteristic 1
- Characteristic 2

**Examples:**
- Example 1
- Example 2

---

## Level 2: Label

[Repeat for each level]

---

## Decision Tree

[Decision tree for applying scale]

---

## Common Mistakes

[Common mistakes when using this scale]
```

**Examples:**
- `references/complexity-scale.md` (estimate-stories)
- `references/effort-scale.md` (estimate-stories)
- `references/risk-factors.md` (estimate-stories)

#### Type 4: Complex Scenarios

**Filename:** `references/scenarios.md` or `references/error-scenarios.md`

**Purpose:** Handle edge cases and complex situations

**Structure:**
```markdown
# Complex Scenarios

Introduction

---

## Scenario 1: Name

**Situation:** Description

**Why This Happens:**
- Reason 1
- Reason 2

**How to Handle:**

**Step 1:** [Action]
[Details]

**Step 2:** [Action]
[Details]

---

## Scenario 2: Name

[Repeat structure]

---

## Decision Trees

### Should I [X]?

```
Question?
  ├─ YES → Action A
  └─ NO → Action B
```
```

**Examples:**
- `references/error-scenarios.md` (fix-issue)

#### Type 5: Guides/Calculations

**Filename:** `references/[topic]-guide.md`

**Purpose:** Detailed guides or calculation methods

**Structure:**
```markdown
# [Topic] Guide

Introduction

---

## Section 1

Detailed explanation

**Examples:**
[Multiple detailed examples]

---

## Section 2

[Continue]

---

## Quick Reference

[Summary card or cheat sheet]
```

**Examples:**
- `references/calculation-guide.md` (estimate-stories)

#### Type 6: Templates

**Filename:** `references/templates.md` or `references/report-templates.md`

**Purpose:** Output templates and formats

**Structure:**
```markdown
# Templates

Introduction

---

## Template 1: Name

**Use for:** [When to use]

```markdown
# Template content
[...]
```

---

## Template 2: Name

[Repeat structure]
```

**Examples:**
- `references/report-templates.md` (estimate-stories)

**How Many Reference Files?**

- Minimum: 2-3 files (don't over-split)
- Typical: 3-5 files
- Maximum: Depends on content (estimate-stories has 5)

**Naming Conventions:**

```
✅ references/common-patterns.md
✅ references/debugging-techniques.md
✅ references/complexity-scale.md
✅ references/error-scenarios.md

❌ references/ref1.md (not descriptive)
❌ references/CommonPatterns.md (use kebab-case)
❌ references/common_patterns.md (use hyphens)
```

---

### Step 6: Remove Old File (2 minutes)

**Goal:** Clean up old non-compliant file

**Commands:**

```bash
# Back up old file
mv .claude/skills/category/skill-name.md .claude/skills/category/skill-name.md.old

# Or delete if confident
rm .claude/skills/category/skill-name.md
```

**Verify:**
```bash
# Check new structure exists
ls -la .claude/skills/category/skill-name/

# Should see:
# SKILL.md
# references/
```

---

### Step 7: Validate Compliance (20 minutes)

**Goal:** Ensure skill meets both skill-creator and 3-layer architecture requirements

**V2 Validation Checklist:**

```markdown
## Skill: [name]

**Date Refactored:** [YYYY-MM-DD]

### Pre-Refactoring
- Lines: ___
- Frontmatter: ❌
- V2 Contracts: ❌
- Over limit: ❌ (by ___ lines)

### Post-Refactoring
- Lines: ___
- Frontmatter: ✅
- V2 Contracts: ✅ / ⚠️ Partial / ❌
- Under limit: ✅

### Structure Compliance (skill-creator)
- [ ] YAML frontmatter with name + description
- [ ] No HTML comments
- [ ] No "Invocation" section
- [ ] No "Configuration" section
- [ ] No "Metadata" section
- [ ] Under 450 lines (ideally <400)

### V2 Architecture Compliance (3-Layer) ⭐ NEW
- [ ] **Contracts defined (if applicable):**
  - [ ] Acceptance criteria (2-5 criteria)
  - [ ] Inputs documented (if skill accepts parameters)
  - [ ] Outputs documented (if skill produces results)
  - [ ] Telemetry configured (emit + track)
- [ ] **Commands integration (for implementation skills):**
  - [ ] bmad-commands used where appropriate
  - [ ] Command calls properly documented
  - [ ] Error handling for command failures
- [ ] **Routing guidance (if called by subagents):**
  - [ ] Routing factors identified
  - [ ] Alternative skills documented

### Content Quality
- [ ] Workflow clear and focused
- [ ] Examples short (10-30 lines)
- [ ] References detailed content
- [ ] Trusts Claude's knowledge
- [ ] Imperative form throughout

### Progressive Disclosure
- [ ] references/ directory exists
- [ ] Detailed content extracted
- [ ] References indexed in SKILL.md

### Testing
- [ ] Old file backed up/removed
- [ ] Directory structure correct
- [ ] All reference files created
- [ ] Read through for clarity
- [ ] Commands tested (if integrated)

**Grade:** [A/B/C/D/F]
**Status:**
- skill-creator: [✅ Compliant / ❌ Non-Compliant]
- V2 Architecture: [✅ Full / ⚠️ Partial / ❌ None]
**Notes:** [Any observations]
```

**Quick Validation Commands:**

```bash
# Check line count
wc -l .claude/skills/category/skill-name/SKILL.md

# Check frontmatter
head -5 .claude/skills/category/skill-name/SKILL.md

# List references
ls .claude/skills/category/skill-name/references/

# Check for removed sections
grep -i "invocation\|configuration\|metadata" .claude/skills/category/skill-name/SKILL.md
```

**Target Metrics:**
- ✅ SKILL.md: 250-450 lines
- ✅ References: 2-5 files
- ✅ Total reduction: 50-75%
- ✅ Token efficiency: 60-75% reduction

---

### Step 8: Add Routing Guidance (10 minutes) ⭐ NEW

**⚠️ NOTE:** Routing is for SUBAGENTS, not skills.

- **Skills:** Remain portable, self-contained
- **Subagents:** Coordination files that route to skills
- **Routing guidance:** Helps subagents know when to use your skill

**Your skill stays a skill.** Routing guidance is just documentation.

---

**Goal:** Document how subagents should route to this skill

**When to Add:**
- Skill is invoked by a subagent (James, Alex, Quinn, Orchestrator)
- Multiple variants of skill exist
- Skill complexity varies by context

**When to Skip:**
- Skill is standalone (not called by subagents)
- Only one variant exists
- No routing logic needed

---

#### 8.1: Identify Routing Factors

Document factors that influence routing to this skill:

**Common Factors:**
- **Complexity:** simple, medium, complex
- **Scope:** single-file, multi-file, large-scale
- **Risk:** low, medium, high
- **Type:** bug-fix, feature, refactor
- **Prerequisites:** tests-exist, no-tests, schema-changes

---

#### 8.2: Create Routing Guidance File

**For skills with routing needs, create:**
`references/routing-guidance.yaml`

**Template:**
```yaml
# Routing Guidance for [skill-name]

routing_factors:
  complexity:
    low: "Simple, straightforward implementation"
    medium: "Standard complexity requiring careful implementation"
    high: "Complex, requires discovery phase"

  scope:
    single_file: "Changes affect 1-2 files"
    multi_file: "Changes affect 3-5 files"
    large_scale: "Changes affect 6+ files"

  risk:
    low: "No breaking changes"
    medium: "Minor schema/API changes"
    high: "Breaking changes or migrations"

recommended_routing:
  - condition: "complexity == low AND scope == single_file"
    use_this_skill: true
    reason: "Simple implementation, standard workflow sufficient"

  - condition: "complexity == high OR risk == high"
    use_this_skill: false
    use_instead: "skill-name-with-discovery"
    reason: "High complexity requires discovery phase first"

  - condition: "scope == large_scale"
    escalate_to_user: true
    reason: "Large scope changes require user approval"
```

---

#### 8.3: Add Routing Section to SKILL.md

Add routing guidance to SKILL.md:

```markdown
## Routing Guidance

**When to use this skill:**
- Simple to medium complexity implementations
- Changes affect ≤5 files
- No breaking changes or migrations

**When to use alternative:**
- High complexity (>60 complexity score)
- Large scale changes (>5 files)
- Breaking changes requiring discovery
- Route to: `implement-with-discovery`

**Complexity Assessment:**
- **Low (0-30):** 1-2 files, no database/API changes → Use this skill
- **Medium (31-60):** 3-5 files, minor schema changes → Use this skill with caution
- **High (61-100):** 6+ files, migrations, breaking changes → Use alternative skill

**See:** `references/routing-guidance.yaml` for detailed routing rules
```

---

#### 8.4: Update Subagent Routing Rules

If skill is called by a subagent, document routing inline in the subagent's .md file:

**Example: James Developer V2**

Edit `.claude/agents/james-developer-v2.md` to add/update routing section:

```markdown
## Command: *implement

### Step 3: Route to Skill

**Routing Rules:**

**Simple Implementation (complexity ≤ 30):**
- Condition: complexity_max: 30, files_affected_max: 3
- Skill: `.claude/skills/development/implement-v2/SKILL.md`
- Reason: Simple implementation with standard TDD

**Complex Implementation (complexity ≥ 61):**
- Condition: complexity_min: 61
- Skill: `.claude/skills/development/implement-with-discovery/SKILL.md`
- Reason: High complexity requires discovery

Execute selected skill based on complexity score.
```

**Note:** All routing logic is inline in the subagent .md file, not in separate YAML files.

---

#### 8.5: Example: Routing-Enabled Skill

**Skill with routing guidance:**

```markdown
---
name: implement
description: Implement features using TDD workflow
---

# Implement Feature

## Purpose
...

## Routing Guidance

**Use this skill when:**
- Complexity ≤ 30 (simple implementation)
- Files affected ≤ 3
- No database migrations
- No breaking API changes

**Use alternative when:**
- Complexity > 60 → Use `implement-with-discovery`
- Files > 5 → Break into smaller tasks
- Migrations required → Use `implement-with-migration`

**Complexity factors:**
- Files: 1-2=10pts, 3-5=30pts, 6+=60pts
- DB changes: None=0pts, Schema=50pts, Migration=90pts
- API: None=0pts, Modify=30pts, New=60pts

**See:** `references/routing-guidance.yaml`

## Workflow
...
```

---

#### 8.6: When Routing Guidance is Optional

**Skip routing guidance if:**
- Skill is standalone (not invoked by subagents)
- Only one version exists (no alternatives)
- Skill always appropriate (no complexity branching)
- Examples: estimate-stories, refine-story, review-task

---

## Ensuring Skill Portability

**⚠️ CRITICAL:** Skills must remain portable, self-contained packages.

This is the **foundation** of the skill-creator pattern. Skills that aren't portable can't be packaged, distributed, or shared across projects.

### Portability Requirements

**✅ DO:**
- Keep all resources in skill directory
- Bundle scripts in `scripts/` directory (if needed)
- Bundle templates/assets in `assets/` directory (if needed)
- Document dependencies in SKILL.md
- Use relative paths within skill
- Package with `package_skill.py`
- Test skill works in different locations

**❌ DON'T:**
- Reference files outside skill directory
- Require external dependencies not bundled
- Hard-code absolute paths
- Assume specific environment (except workspace/)
- Create skills that only work locally
- Depend on system-specific tools not documented

### Portable vs Non-Portable Examples

**✅ Portable (CORRECT):**
```markdown
Execute:
```bash
python .claude/skills/bmad-commands/scripts/read_file.py \
  --path workspace/tasks/{task_id}.md
```
```

**Why it's portable:**
- Uses relative path from Claude Code root
- References another skill by relative path
- Assumes only standard workspace/ structure

**❌ Non-Portable (WRONG):**
```markdown
Execute:
```bash
python /home/user/projects/bmad/scripts/helper.py \
  --path /home/user/tasks/task.md
```
```

**Why it's NOT portable:**
- Hard-coded absolute path
- References files outside skill
- Assumes specific user/environment

### Testing Portability

**Step 1: Package your skill**
```bash
python scripts/package_skill.py .claude/skills/category/skill-name
```

This should create: `skill-name.zip`

**Step 2: Extract to different location**
```bash
# Extract to temp directory
unzip skill-name.zip -d /tmp/test-skill

# Or extract to different project
unzip skill-name.zip -d ~/other-project/.claude/skills/category/
```

**Step 3: Verify it works**
```bash
# Check structure
ls -la /tmp/test-skill/skill-name/

# Should see:
# SKILL.md
# references/
# scripts/ (if applicable)
# assets/ (if applicable)

# Verify references resolve
grep "references/" /tmp/test-skill/skill-name/SKILL.md

# All paths should be relative
```

**Step 4: Test in different environment**
- Open skill in different Claude Code project
- Verify skill loads correctly
- Check references are accessible
- Test scripts execute (if applicable)

### Why Portability Matters

**✅ Skills can be shared across projects**
- Same skill works in multiple repos
- No environment-specific configuration
- Consistent behavior everywhere

**✅ Skills can be distributed to teams**
- Package once, share with team
- Everyone gets same version
- No setup required

**✅ Skills work in any environment**
- No assumptions about file system
- No hard-coded paths
- No external dependencies (or bundled)

**✅ Skills can be version-controlled separately**
- Git submodules
- Separate repositories
- Independent versioning

### Common Portability Violations

**Violation 1: Hard-coded paths**
```markdown
❌ Read config from /home/user/.config/app.yaml
✅ Read config from workspace/.config/app.yaml
```

**Violation 2: External scripts**
```markdown
❌ python ~/scripts/helper.py
✅ python .claude/skills/bmad-commands/scripts/helper.py
```

**Violation 3: System tools without docs**
```markdown
❌ Run custom-tool (not documented, not bundled)
✅ Run python3 (standard, documented in prerequisites)
```

**Violation 4: Absolute references**
```markdown
❌ **See:** /home/user/docs/guide.md
✅ **See:** references/guide.md
```

### Bundling Dependencies

**If skill needs external tools:**

1. **Bundle scripts in skill**
   ```
   skill-name/
   ├── SKILL.md
   ├── scripts/
   │   ├── helper.py
   │   └── validator.py
   └── references/
   ```

2. **Bundle templates/assets**
   ```
   skill-name/
   ├── SKILL.md
   ├── assets/
   │   ├── template.md
   │   └── config.yaml
   └── references/
   ```

3. **Document requirements**
   ```markdown
   ## Prerequisites

   - Python 3.8+ (standard)
   - pytest (install: `pip install pytest`)
   - Node.js 16+ (for test execution)
   ```

**Never assume tools are available without documenting them.**

### The Package Test

**The ultimate portability test:**

1. Package skill: `package_skill.py`
2. Email .zip to someone else
3. They extract and use it
4. It works without modifications

**If this fails, your skill is not portable.**

### Portability Checklist

Before marking skill complete:

- [ ] All file references are relative (not absolute)
- [ ] No references outside skill directory
- [ ] Scripts bundled in `scripts/` (if needed)
- [ ] Templates bundled in `assets/` (if needed)
- [ ] External dependencies documented in SKILL.md
- [ ] Skill packages successfully (`package_skill.py`)
- [ ] Skill extracts correctly (tested in /tmp)
- [ ] Skill works in different location (tested)
- [ ] No hard-coded paths or assumptions
- [ ] README or SKILL.md explains prerequisites

**If all checkboxes are ✅, your skill is portable.**

---

## Common Patterns by Skill Type

### Pattern 1: Development Skills (fix-issue, implement-feature, run-tests)

**Typical Structure:**
- Workflow: Test → Implement → Validate
- References: patterns, techniques, test-examples, scenarios

**Common extractions:**
- TDD examples → `references/test-examples.md`
- Debugging approaches → `references/debugging-techniques.md`
- Common bugs → `references/common-patterns.md`
- Error scenarios → `references/error-scenarios.md`

**Target SKILL.md:** 300-350 lines

### Pattern 2: Planning Skills (estimate-stories, refine-story, breakdown-epic)

**Typical Structure:**
- Workflow: Analyze → Apply framework → Document
- References: scales, frameworks, templates, scenarios

**Common extractions:**
- Rating scales → `references/[scale-name]-scale.md`
- Calculation methods → `references/calculation-guide.md`
- Report templates → `references/templates.md`
- Edge cases → `references/scenarios.md`

**Target SKILL.md:** 350-400 lines

### Pattern 3: Quality Skills (review-task, quality-gate, nfr-assess)

**Typical Structure:**
- Workflow: Assess → Analyze → Report
- References: criteria, scoring, templates, checklists

**Common extractions:**
- Assessment criteria → `references/criteria.md`
- Scoring matrices → `references/scoring.md`
- Report templates → `references/templates.md`
- Decision trees → `references/decision-trees.md`

**Target SKILL.md:** 300-400 lines

---

## Time-Saving Tips

### Tip 1: Batch Similar Skills

Refactor skills in same category together—they share patterns:

**Development skills batch:**
- fix-issue ✅ (done)
- implement-feature
- run-tests

**Planning skills batch:**
- estimate-stories ✅ (done)
- refine-story
- breakdown-epic
- create-task-spec

**Quality skills batch:**
- review-task
- quality-gate
- nfr-assess
- trace-requirements

### Tip 2: Reuse Reference Patterns

Don't recreate from scratch—adapt from examples:

- Use fix-issue references as template for other development skills
- Use estimate-stories references as template for other planning skills
- Create shared references in `.claude/skills/references/common/`

### Tip 3: Automate Repetitive Tasks

**Remove sections script:**
```bash
#!/bin/bash
# remove-sections.sh
skill_file=$1

# Remove common sections
sed -i '/^## Invocation/,/^## /d' "$skill_file"
sed -i '/^## Skill Configuration/,/^## /d' "$skill_file"
sed -i '/^## Skill Metadata/,/^## /d' "$skill_file"
sed -i '/<!--.*-->/d' "$skill_file"

echo "Removed extraneous sections from $skill_file"
```

### Tip 4: Work in 90-Minute Blocks

- **Block 1:** Steps 1-3 (Analysis, structure, frontmatter) - 25 min
- **Break:** 10 min
- **Block 2:** Step 4 (Streamline SKILL.md) - 60 min
- **Break:** 15 min
- **Block 3:** Step 5 (Create references) - 90 min
- **Break:** 15 min
- **Block 4:** Steps 6-7 (Remove old, validate) - 17 min

Total: ~3.7 hours with breaks

### Tip 5: Track Progress

Create a tracking sheet:

| Skill | Lines Before | Lines After | Reduction | Status | Date |
|-------|--------------|-------------|-----------|--------|------|
| fix-issue | 949 | 306 | 67% | ✅ Done | 2025-10-28 |
| estimate-stories | 1,477 | 374 | 75% | ✅ Done | 2025-10-28 |
| refine-story | 1,375 | ___ | ___ | ⏳ In Progress | |
| [Next skill] | ___ | ___ | ___ | 📋 Todo | |

---

## Troubleshooting

### Issue 1: "I can't get under 500 lines"

**Solution:** Extract more content to references

1. Look for long examples (>30 lines) → Extract
2. Look for detailed explanations → Extract
3. Look for comprehensive lists → Extract
4. Check if explaining basic concepts Claude knows → Remove

**Target:** Most skills can reach 300-400 lines

### Issue 2: "Too many small reference files"

**Solution:** Consolidate related content

Instead of:
```
references/pattern1.md
references/pattern2.md
references/pattern3.md
```

Consolidate to:
```
references/common-patterns.md  (includes all 3)
```

**Balance:** 3-5 reference files is typical

### Issue 3: "Workflow seems too rigid"

**Solution:** Add flexibility language

```markdown
❌ STEP 1: Do X
   STEP 2: Do Y
   STEP 3: Do Z

✅ ## Workflow

   Typical flow: X → Y → Z

   Adapt based on project context.
```

### Issue 4: "Can't find natural split points"

**Solution:** Split by granularity

- **SKILL.md:** High-level workflow, quick references
- **references/:** Detailed steps, comprehensive examples

**Rule:** If it's longer than 50 lines and not core workflow, extract it.

---

## Quality Checks

Before marking skill complete, verify:

**Structure:**
```bash
# Check structure
tree .claude/skills/category/skill-name/

# Should see:
# skill-name/
# ├── SKILL.md
# └── references/
#     ├── file1.md
#     ├── file2.md
#     └── file3.md
```

**Frontmatter:**
```bash
head -5 .claude/skills/category/skill-name/SKILL.md

# Should see:
# ---
# name: skill-name
# description: [description]
# ---
```

**Length:**
```bash
wc -l .claude/skills/category/skill-name/SKILL.md

# Should be: <450 lines (ideally 300-400)
```

**Writing Style:**
```bash
# Check for second person (should find nothing)
grep -i "you should\|you can\|you need" .claude/skills/category/skill-name/SKILL.md
```

**References:**
```bash
# Check references are mentioned
grep "references/" .claude/skills/category/skill-name/SKILL.md
```

---

## Success Criteria

A successfully refactored skill has:

- ✅ Proper YAML frontmatter (name + description)
- ✅ Under 450 lines (ideally 300-400)
- ✅ Clear, flexible workflow
- ✅ Short examples (10-30 lines)
- ✅ Detailed content in references/
- ✅ Imperative writing style
- ✅ Trusts Claude's knowledge
- ✅ 2-5 reference files
- ✅ References indexed clearly
- ✅ No extraneous documentation
- ✅ Reads naturally and clearly

---

## V2 Architecture Benefits

**Why add 3-layer architecture compliance:**

### Observability
- **Telemetry:** Track skill performance, identify bottlenecks
- **Metrics:** Coverage, duration, success rates
- **Debugging:** Clear visibility into what went wrong

### Testability
- **Contracts:** Formal inputs/outputs enable testing
- **Acceptance Criteria:** Automated verification of success
- **Primitives:** Unit-testable atomic operations

### Composability
- **Routing:** Subagents can intelligently select skills
- **Primitives:** Reusable across multiple skills
- **Contracts:** Skills can call other skills reliably

### Safety
- **Guardrails:** Prevent excessive changes
- **Validation:** Automated acceptance checks
- **Escalation:** Clear paths when things go wrong

### Production-Ready
- **Deterministic:** Predictable behavior
- **Documented:** Clear contracts and expectations
- **Maintainable:** Easy to update and extend

**Trade-offs:**
- ⏱️ +1 hour per skill (20% longer)
- 📝 More upfront work (contracts, telemetry)
- ✅ But: Better quality, easier to maintain long-term

---

## Next Steps

### Immediate Actions

1. **Choose next skill** - Start with development skills (they benefit most from commands)
   - **Best first:** implement-feature (uses bmad-commands)
   - **Then:** fix-issue variants, refactor skills
   - **Last:** Planning/quality skills (fewer V2 benefits)

2. **Follow template** - Use this V2 template step-by-step
   - Don't skip V2 steps (contracts, telemetry, routing)
   - Refer to implement-v2 as example

3. **Track progress** - Mark skills complete with V2 status
   ```
   | Skill | skill-creator | V2 Architecture | Date |
   |-------|---------------|-----------------|------|
   | implement | ✅ | ✅ Full | 2025-10-28 |
   | fix-issue | ✅ | ❌ None | 2025-10-28 |
   ```

4. **Learn and adapt** - Each refactoring gets faster
   - First few skills: 4-5 hours (learning V2 patterns)
   - Later skills: 3-4 hours (experienced)

5. **Validate frequently** - Check both compliances after each skill
   - skill-creator validation
   - V2 architecture validation

### V2 Timeline Estimates

**With V2 Architecture Integration:**

- **Skills 3-5:** 4-5 hours each (learning V2 patterns)
- **Skills 6-10:** 3.5-4 hours each (getting comfortable)
- **Skills 11-18:** 3-4 hours each (experienced with V2)

**Total for 16 remaining skills:** ~55-65 hours

**Spread over 3-4 weeks:** 4-5 hours per day

**Or phased approach:**
- **Phase 1 (Week 1-2):** skill-creator compliance only (~40 hours)
- **Phase 2 (Week 3-4):** Add V2 architecture to all (~20 hours)
- **Total:** ~60 hours, more flexible

### Priority Order

**Tier 1: High V2 Value (Do First)**
- implement-feature (uses commands heavily)
- fix-bug variants
- run-tests
- refactor-code

**Tier 2: Medium V2 Value**
- create-task-spec (some commands)
- breakdown-epic
- review-task (telemetry valuable)

**Tier 3: Low V2 Value (Do Last)**
- estimate-stories (already done ✅)
- refine-story
- quality assessments

---

## Resources

### Validated Examples

**skill-creator Compliant:**
- `.claude/skills/development/fix-issue/` ✅
- `.claude/skills/planning/estimate-stories/` ✅

**V2 Architecture (Full):**
- `.claude/skills/development/implement-v2/` ✅
- `.claude/skills/bmad-commands/` ✅
- `.claude/agents/james-developer-v2/` ✅

### Documentation

**General:**
- `docs/skills-refactoring-guide.md` - Detailed refactoring guide
- `docs/skills-compliance-analysis.md` - Initial compliance analysis
- `docs/skills-validation-report.md` - Validation results

**V2 Architecture:**
- `docs/3-layer-architecture-prototype.md` - Architecture overview ⭐
- `docs/command-routing-design.md` - Routing patterns
- `.claude/skills/bmad-commands/SKILL.md` - Commands reference

**This Template:**
- `docs/skill-refactoring-template.md` - This V2-enhanced template

---

## Quick Reference

### V2 Checklist Per Skill

**Minimum (all skills):**
- [ ] YAML frontmatter with name + description
- [ ] Under 450 lines
- [ ] Progressive disclosure (references/)

**V2 Enhanced (recommended):**
- [ ] Acceptance criteria (2-5 criteria)
- [ ] Telemetry (emit + track)

**V2 Full (development skills):**
- [ ] Acceptance criteria ✅
- [ ] Inputs/outputs ✅
- [ ] Telemetry ✅
- [ ] bmad-commands integration ✅
- [ ] Routing guidance (if called by subagent) ✅

---

**Remember:**

> **The goal is not just compliance, but creating production-ready, observable, testable skills that leverage the full power of the 3-layer architecture.**

If V2 features don't make sense for a particular skill, that's okay! Apply pragmatically:
- **Development/implementation skills:** Full V2
- **Planning skills:** Minimal V2 (telemetry)
- **Quality skills:** Selective V2 (acceptance criteria, telemetry)

**Good luck building the future of BMAD! 🚀**
