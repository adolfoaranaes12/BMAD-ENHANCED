# 3-Layer Architecture for BMAD Skills

**Version:** 2.0.0
**Date:** October 28, 2025
**Status:** Production Ready

---

## Critical Understanding

**⚠️ MOST IMPORTANT CONCEPT:**

> **Skills remain skills. The "3 layers" refers to the ROLE skills play in the architecture, NOT different file structures.**

**All skills:**
- ✅ Follow skill-creator patterns (SKILL.md, references/, etc.)
- ✅ Are packageable (package_skill.py)
- ✅ Are portable (.zip distribution)
- ✅ Are self-contained (all dependencies bundled)

**The architecture is about HOW SKILLS WORK TOGETHER, not about creating different types of files.**

---

## Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [Layer 1: Primitives](#layer-1-primitives)
3. [Layer 2: Workflow Skills](#layer-2-workflow-skills)
4. [Layer 3: Subagents](#layer-3-subagents-not-skills)
5. [How They Work Together](#how-they-work-together)
6. [Portability Guarantee](#portability-guarantee)
7. [Examples](#complete-examples)
8. [Migration Guide](#migration-guide)

---

## Architecture Overview

### The Three Layers

```
┌─────────────────────────────────────────────────────────────┐
│  Layer 3: SUBAGENTS (Coordination Files)                    │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ .claude/agents/james-developer-v2.md  (single file)   │   │
│  │                                                        │   │
│  │ Contains (inline):                                     │   │
│  │ - YAML frontmatter (name, description, tools, model)  │   │
│  │ - Routing logic                                       │   │
│  │ - Guardrails                                          │   │
│  │ - Workflow instructions                               │   │
│  └──────────────────────────────────────────────────────┘   │
│                           │                                   │
│                           │ Routes to skills based on context │
│                           ↓                                   │
├─────────────────────────────────────────────────────────────┤
│  Layer 2: WORKFLOW SKILLS (Regular Skills)                   │
│  ┌──────────────────────┐  ┌───────────────────────────┐    │
│  │ implement-v2/        │  │ estimate-stories/         │    │
│  │ ├── SKILL.md  ✅     │  │ ├── SKILL.md  ✅          │    │
│  │ └── references/       │  │ └── references/           │    │
│  └──────────────────────┘  └───────────────────────────┘    │
│           │                           │                       │
│           │ Uses commands             │ No commands needed   │
│           ↓                           ↓                       │
├─────────────────────────────────────────────────────────────┤
│  Layer 1: PRIMITIVES (Skills with Scripts)                     │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ bmad-commands/  (This is a SKILL! ✅)                 │   │
│  │ ├── SKILL.md                                          │   │
│  │ ├── scripts/          (Python scripts bundled here)   │   │
│  │ │   ├── read_file.py                                  │   │
│  │ │   └── run_tests.py                                  │   │
│  │ └── references/                                       │   │
│  │     └── command-contracts.yaml                        │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘

KEY INSIGHT: Layers 1 and 2 are ALL SKILLS (packageable, portable).
            Layer 3 is single .md files (project-specific coordination).
```

---

### Design Principles

1. **Skills Stay Skills**
   - All follow skill-creator pattern
   - All are packageable
   - All are portable
   - All are self-contained

2. **Layers Define Roles, Not Structure**
   - Layer 1 (Primitives): Skills that provide atomic operations
   - Layer 2 (Workflow Skills): Skills that implement workflows
   - Layer 3 (Subagents): Files that coordinate routing

3. **Portability First**
   - Skills work anywhere
   - No external dependencies
   - Distributable as .zip
   - Version-controllable

4. **Composability**
   - Skills can call other skills' scripts
   - Skills can be used by multiple subagents
   - Skills remain independent

---

## How Skills Are Dynamically Loaded and Executed

### The Dynamic Loading Mechanism

**Critical Understanding:** Skills are **markdown files with instructions**, not executable code. The agent acts as an "interpreter" that dynamically loads and follows these instructions.

#### Step-by-Step Loading Process

**1. Agent Receives Command with \*prefix**
```
User: /alex *create-task-spec "Feature description"
        ↓
Agent sees: *create-task-spec
```

**2. Agent's Routing Logic Activates**

The agent file (`.claude/agents/alex-planner-v2.md`) contains routing instructions:
```markdown
## Command Routing

When you receive a command starting with `*`, route to the appropriate skill:

- `*create-task-spec` → .claude/skills/planning/create-task-spec/SKILL.md
- `*breakdown-epic` → .claude/skills/planning/breakdown-epic/SKILL.md
- `*estimate` → .claude/skills/planning/estimate/SKILL.md
```

**3. Agent Uses Read Tool to Load Skill**

The agent dynamically loads the skill file:
```
Read tool: .claude/skills/planning/create-task-spec/SKILL.md
```

**4. Agent Follows Skill Instructions Step-by-Step**

The skill file contains instructions like:
```markdown
## Workflow

1. Analyze the requirement description
2. Use Read tool to check for existing task files
3. Generate unique task ID
4. Create task specification using template
5. Use Write tool to save task file
...
```

**5. Agent Executes Using Available Tools**

As the agent follows the skill instructions, it uses tools:
- **Read tool** - to load files
- **Write tool** - to create/update files
- **Bash tool** - to run commands
- **Edit tool** - to modify files
- etc.

### Key Technical Points

✅ **Skills are NOT pre-compiled** - they load on-demand when needed
✅ **Skills are NOT executable** - they're instructions that the agent interprets
✅ **The \* prefix is our convention** - not a Claude Code feature, but our routing signal
✅ **Agent is the interpreter** - reads skill markdown and executes instructions
✅ **Dynamic = Flexible** - can add new skills without modifying agents

### Analogy: Recipe Execution

Think of it like cooking:
- **Skill File** = Recipe (instructions written in markdown)
- **Agent** = Chef (reads recipe and follows steps)
- **Tools** = Kitchen equipment (Read, Write, Bash tools)
- **\*command** = Menu selection (which recipe to use)

The chef (agent) doesn't "become" the recipe - they **read and follow** it.

### Implications for Developers

**Adding New Skills:**
1. Create new SKILL.md file in appropriate directory
2. Update agent's routing logic to recognize the new \*command
3. No compilation needed - agent will Read and follow it

**Modifying Skills:**
1. Edit the SKILL.md file
2. Changes take effect immediately (next time agent Reads it)
3. No restart or recompilation needed

**Portability:**
- Skills are just markdown files → easy to version control
- No runtime dependencies → works anywhere
- Package as .zip → distribute to others

---

## Layer 1: Primitives

### What They Are

**Primitives are regular skills that bundle executable scripts.**

They follow the exact same skill-creator pattern as any other skill, but they include a `scripts/` directory with executable code.

---

### Structure

```
.claude/skills/bmad-commands/     ← SKILL DIRECTORY
├── SKILL.md                       ← Standard skill file ✅
├── scripts/                       ← Executable scripts (optional dir)
│   ├── read_file.py              ← Python script
│   └── run_tests.py              ← Python script
└── references/                    ← Documentation (optional dir)
    └── command-contracts.yaml     ← Command specifications
```

**This IS a skill!**
- ✅ Has SKILL.md
- ✅ Packageable with package_skill.py
- ✅ Distributable as bmad-commands.zip
- ✅ Portable (works anywhere with Python)

---

### Purpose

Provide **deterministic, testable primitives** for other skills to use.

**Instead of:**
```markdown
## Step 1: Read File
Read the task specification file and extract contents.
```

**Do this:**
```markdown
## Step 1: Read File
Execute bmad-commands script:
python .claude/skills/bmad-commands/scripts/read_file.py \
  --path workspace/tasks/task-001.md \
  --output json

Parse JSON response for file contents.
```

---

### Benefits

- **Deterministic:** Same inputs → same outputs
- **Testable:** Scripts can be unit tested
- **Observable:** Structured JSON output with telemetry
- **Reusable:** Multiple skills can use same commands
- **Versioned:** Command contracts documented

---

### Example: bmad-commands Skill

**SKILL.md:**
```markdown
---
name: bmad-commands
description: Atomic command primitives for BMAD operations with JSON I/O and telemetry
---

# BMAD Commands

## Overview
Provides deterministic, testable command primitives...

## Available Commands

### read_file
Read file contents with metadata.

**Usage:**
```bash
python scripts/read_file.py --path <file> --output json
```

**Returns:**
```json
{
  "success": true,
  "outputs": {"content": "...", "line_count": 45},
  "telemetry": {"duration_ms": 12},
  "errors": []
}
```

[Continue with other commands...]
```

**scripts/read_file.py:**
```python
#!/usr/bin/env python3
"""Command: read_file"""
import json, sys
from pathlib import Path

def read_file(path: str):
    content = Path(path).read_text()
    return {
        "success": True,
        "outputs": {"content": content, "line_count": len(content.splitlines())},
        "telemetry": {"command": "read_file"},
        "errors": []
    }

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True)
    args = parser.parse_args()
    result = read_file(args.path)
    print(json.dumps(result))
    sys.exit(0 if result["success"] else 1)
```

**Package and distribute:**
```bash
cd ~/.claude/plugins/.../skill-creator
python scripts/package_skill.py path/to/bmad-commands
# Creates: bmad-commands.zip (portable, distributable)
```

---

## Layer 2: Workflow Skills

### What They Are

**Workflow skills are regular skills that implement multi-step processes.**

They may call Layer 1 primitive skills, or they may not. They follow the standard skill-creator pattern.

---

### Structure

```
.claude/skills/development/implement-v2/   ← SKILL DIRECTORY
├── SKILL.md                                ← Standard skill file ✅
└── references/                             ← Documentation (optional)
    ├── tdd-workflow.md                     ← Detailed workflow
    └── refactoring-patterns.md             ← Patterns reference
```

**This IS a skill!**
- ✅ Has SKILL.md
- ✅ Packageable with package_skill.py
- ✅ Distributable as implement-v2.zip
- ✅ Portable (works anywhere)

---

### Purpose

Implement **multi-step workflows** that may compose primitive skills.

---

### Types of Workflow Skills

#### Type 1: Implementation Skills (Uses Commands)

**Example:** implement-v2

**Calls primitive skills:**
```markdown
### Step 1: Load Task Spec

Execute bmad-commands:
python .claude/skills/bmad-commands/scripts/read_file.py \
  --path workspace/tasks/{task_id}.md \
  --output json

Parse outputs.content for task specification.
```

**Has contracts (V2 architecture):**
```yaml
---
name: implement
description: Implement features using TDD
acceptance:
  - tests_passing: "All tests must pass"
  - coverage_threshold: "Coverage >= 80%"
inputs:
  task_id:
    type: string
    required: true
outputs:
  implementation_complete:
    type: boolean
telemetry:
  emit: "skill.implement.completed"
  track: ["task_id", "coverage_percent", "duration_ms"]
---
```

---

#### Type 2: Planning Skills (No Commands)

**Example:** estimate-stories

**Doesn't need commands:**
```markdown
### Step 1: Analyze Complexity

Use complexity scale (1-5) to assess story difficulty.

See: references/complexity-scale.md for detailed scale.
```

**May have minimal contracts:**
```yaml
---
name: estimate-stories
description: Estimate story points using structured formula
acceptance:
  - estimates_provided: "All stories have estimates"
telemetry:
  emit: "skill.estimate.completed"
  track: ["story_id", "story_points", "duration_ms"]
---
```

---

### Example: implement-v2 Skill

**SKILL.md:**
```markdown
---
name: implement
description: Implement features using TDD workflow with bmad-commands
acceptance:
  - tests_passing: "All tests must pass"
  - coverage_threshold: "Test coverage >= 80%"
inputs:
  task_id:
    type: string
    required: true
outputs:
  implementation_complete:
    type: boolean
telemetry:
  emit: "skill.implement.completed"
  track: ["task_id", "coverage_percent", "duration_ms"]
---

# Implement Feature with TDD

## Overview
Implements features following Test-Driven Development...

## Workflow

### Step 1: Load Task Specification

**Action:** Use bmad-commands to load task spec

Execute:
```bash
python .claude/skills/bmad-commands/scripts/read_file.py \
  --path workspace/tasks/{task_id}.md \
  --output json
```

Parse response: Check `success == true`, extract `outputs.content`

### Step 2: RED Phase - Write Failing Tests
[Workflow continues...]

### Step 3: GREEN Phase - Implement Code
[Workflow continues...]

### Step 4: Run Tests

Execute:
```bash
python .claude/skills/bmad-commands/scripts/run_tests.py \
  --path . \
  --framework jest \
  --output json
```

Verify: `outputs.passed == true` and `outputs.coverage_percent >= 80`
```

**Package and distribute:**
```bash
python scripts/package_skill.py path/to/implement-v2
# Creates: implement-v2.zip (portable, distributable)
```

---

## Layer 3: Subagents (NOT Skills)

### What They Are

**Subagents are coordination files, NOT skills.**

They don't follow the skill-creator pattern. They're not packageable. They route requests to skills based on context.

---

### Structure

```
.claude/agents/james-developer-v2.md    ← Single file, NOT SKILL.md! ❌
```

**Official Claude Code format:**
- Single .md file (not a directory)
- YAML frontmatter with name, description, tools, model
- All content inline (routing logic, guardrails, etc.)

**This is NOT a skill:**
- ❌ Not named SKILL.md
- ❌ Not packageable with package_skill.py
- ❌ Not distributable as standalone
- ❌ Not portable (tied to subagent system)

---

### Purpose

Provide **intelligent routing and orchestration**:
- Assess complexity/risk
- Select appropriate skill
- Enforce guardrails
- Handle escalation

---

### ⚠️ CRITICAL: How Subagents Must Invoke Skills

**Subagents MUST use the Skill tool to invoke skills, NOT the Read tool.**

This is the most common mistake when creating subagents:

```markdown
✅ CORRECT WAY - Use Skill Tool:
Skill(command="create-task-spec")
Skill(command="implement-v2")
Skill(command="analyze-architecture")

❌ WRONG WAY - Using Read Tool:
Read(.claude/skills/create-task-spec/SKILL.md)      # Loads text, doesn't execute!
Read(.claude/skills/implement-v2/SKILL.md)          # Skill never runs!
Read(.claude/skills/analyze-architecture/SKILL.md)  # Only documentation shown!
```

**Why This Matters:**

| Tool | What It Does | Result |
|------|--------------|--------|
| `Skill(command="skill-name")` | Invokes the skill and expands its full prompt | ✅ Skill executes correctly |
| `Read(.claude/skills/skill-name/SKILL.md)` | Loads the skill file as text | ❌ Only shows documentation, skill never runs |

**Correct Execution Flow:**

```
1. User: /alex *create-task-spec "User login"
2. Subagent recognizes: *create-task-spec
3. Subagent calls: Skill(command="create-task-spec")
4. System shows: <command-message>create-task-spec is running…</command-message>
5. Skill expands with full workflow prompt
6. Subagent executes the expanded workflow
7. Output generated correctly
```

**Required in Agent Files:**

Every subagent file MUST include:
1. **Command-to-Skill Mapping Table** showing which Skill() command to use
2. **Execution instructions** using `Skill(command="...")` syntax
3. **DO/DON'T examples** showing Skill tool (correct) vs Read tool (wrong)

See [Subagent Skill Loading Fix](./SUBAGENT-SKILL-LOADING-FIX.md) for complete implementation details.

---

### Example: james-developer-v2 Subagent

**File:** `.claude/agents/james-developer-v2.md` (single file)

```markdown
---
name: james-developer-v2
description: Developer subagent with intelligent routing, guardrails, and automated verification. Use proactively for implementation tasks.
tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
---

# James Developer V2 Subagent

## Purpose
Routes development commands to appropriate skills based on context.

## Command: *implement

### Step 1: Load Task Specification

Use bmad-commands to read task:
python .claude/skills/bmad-commands/scripts/read_file.py \
  --path workspace/tasks/{task_id}.md

### Step 2: Assess Complexity

Calculate complexity score:
- Files: 1-2=10pts, 3-5=30pts, 6+=60pts
- DB changes: None=0pts, Schema=50pts, Migration=90pts

### Step 3: Route to Skill

**Routing Rules (inline):**
- complexity ≤ 30 → Use `.claude/skills/development/implement-v2/SKILL.md`
- complexity > 60 → Use `.claude/skills/development/implement-with-discovery/SKILL.md`

Execute selected skill.

### Step 4: Verify Acceptance

Check skill outputs match acceptance criteria.

## Guardrails

**Hard Limits:**
- Max 5 files per change
- Max 400 lines per diff
- Never commit failing tests

**Escalation Triggers:**
- Complexity > 80
- Breaking API changes
- Database migrations
```

**Note:** All routing logic and guardrails are inline in the single .md file, not in separate references/ files.

---

## How They Work Together

### Complete Flow Example

**User Request:**
```
@james *implement task-auth-002
```

---

**Layer 3: James Subagent (Orchestration)**

1. **Load task spec** (calls Layer 1):
   ```bash
   python .claude/skills/bmad-commands/scripts/read_file.py \
     --path workspace/tasks/task-auth-002.md
   ```

2. **Assess complexity:**
   - Parse task: 2 files, no DB changes, no API changes
   - Score: 10pts (files) + 0 (DB) + 0 (API) = 10pts (LOW)

3. **Route to skill** (selects Layer 2):
   - Complexity = 10 (LOW)
   - Routing logic (inline) says: Use implement-v2
   - Invoke: `.claude/skills/development/implement-v2/SKILL.md`

---

**Layer 2: implement-v2 Skill (Workflow)**

1. **Load task spec** (calls Layer 1):
   ```bash
   python .claude/skills/bmad-commands/scripts/read_file.py \
     --path workspace/tasks/task-auth-002.md
   ```

2. **Write tests** (TDD RED phase)

3. **Implement code** (TDD GREEN phase)

4. **Run tests** (calls Layer 1):
   ```bash
   python .claude/skills/bmad-commands/scripts/run_tests.py \
     --path . --framework jest
   ```

5. **Return outputs:**
   ```json
   {
     "implementation_complete": true,
     "test_coverage_percent": 87,
     "tests_passed": true
   }
   ```

---

**Layer 3: James Subagent (Verification)**

1. **Check acceptance criteria:**
   - ✅ tests_passing: outputs.tests_passed == true
   - ✅ coverage_threshold: outputs.test_coverage_percent (87) >= 80

2. **Emit telemetry:**
   ```json
   {
     "agent": "james-v2",
     "command": "implement",
     "task_id": "task-auth-002",
     "routing": {"complexity": 10, "skill": "implement-v2"},
     "result": {"success": true, "coverage": 87}
   }
   ```

3. **Report to user:**
   ```
   ✅ Implementation complete!
   Files modified: 2
   Tests: 12/12 passing
   Coverage: 87%

   Ready for review: @quinn *review task-auth-002
   ```

---

### Data Flow Diagram

```
User Request
     │
     ↓
┌────────────────────────────────┐
│ Layer 3: Subagent (James V2)   │
│ ┌────────────────────────────┐ │
│ │ 1. Load task (Layer 1)     │ │ ← Calls bmad-commands
│ │ 2. Assess complexity        │ │
│ │ 3. Select skill (Layer 2)  │ │ ← Routes to implement-v2
│ └────────────────────────────┘ │
└────────────────────────────────┘
     │
     ↓
┌────────────────────────────────┐
│ Layer 2: Skill (implement-v2)  │
│ ┌────────────────────────────┐ │
│ │ 1. Load task (Layer 1)     │ │ ← Calls bmad-commands
│ │ 2. Write tests              │ │
│ │ 3. Implement code           │ │
│ │ 4. Run tests (Layer 1)     │ │ ← Calls bmad-commands
│ │ 5. Return outputs           │ │
│ └────────────────────────────┘ │
└────────────────────────────────┘
     │
     ↓
┌────────────────────────────────┐
│ Layer 1: Primitives (bmad)     │
│ ┌────────────────────────────┐ │
│ │ Execute Python scripts      │ │
│ │ Return JSON with telemetry  │ │
│ └────────────────────────────┘ │
└────────────────────────────────┘
```

---

## Portability Guarantee

### Skills Are Portable

**ALL skills (Layer 1 and 2) are:**

✅ **Packageable**
```bash
python scripts/package_skill.py .claude/skills/bmad-commands
# → bmad-commands.zip

python scripts/package_skill.py .claude/skills/development/implement-v2
# → implement-v2.zip
```

✅ **Distributable**
```bash
# Share via .zip files
scp bmad-commands.zip user@server:/path/
scp implement-v2.zip user@server:/path/

# Install anywhere
unzip bmad-commands.zip -d .claude/skills/
unzip implement-v2.zip -d .claude/skills/development/
```

✅ **Self-Contained**
- All dependencies bundled (Python scripts, references, assets)
- No external file dependencies
- Relative paths only
- Works in any environment

✅ **Version-Controllable**
```bash
git add .claude/skills/bmad-commands/
git add .claude/skills/development/implement-v2/
git commit -m "Add command and workflow skills"
```

---

### Subagents Are NOT Portable

**Subagents (Layer 3) are:**

❌ **Not packageable** (no SKILL.md, different structure)
❌ **Not distributable** as standalone (tied to subagent system)
❌ **Not self-contained** (reference external skills)

**But that's okay!** Subagents are meant to be project-specific coordination logic.

---

### Testing Portability

**For any skill:**

```bash
# 1. Package
cd ~/.claude/plugins/.../skill-creator
python scripts/package_skill.py /path/to/skill

# 2. Validate
python scripts/validate_skill.py /path/to/skill

# 3. Test in different location
unzip skill-name.zip -d /tmp/test
# Verify all references resolve, scripts execute

# 4. Distribute
# Ship .zip file to other users/projects
```

---

## Complete Examples

### Example 1: Command Skill (bmad-commands)

**File:** `.claude/skills/bmad-commands/SKILL.md`

```markdown
---
name: bmad-commands
description: Atomic command primitives for BMAD operations with JSON I/O and telemetry
---

# BMAD Commands

## Overview
Provides deterministic, testable command primitives that other skills compose into workflows.

## Available Commands

### read_file
Read file contents with metadata.

Usage: python scripts/read_file.py --path <file> --output json

Returns JSON with success, outputs {content, line_count}, telemetry, errors.

### run_tests
Execute tests with structured results.

Usage: python scripts/run_tests.py --path <dir> --framework jest --output json

Returns JSON with success, outputs {passed, coverage_percent, tests_total}, telemetry, errors.

## Using from Other Skills

```markdown
### Step 1: Read File

Execute: python .claude/skills/bmad-commands/scripts/read_file.py --path file.md --output json
Parse: Extract outputs.content from JSON response
```

## Command Contracts

See: references/command-contracts.yaml for detailed specifications.
```

**Packaging:**
```bash
python scripts/package_skill.py .claude/skills/bmad-commands
# ✅ Creates bmad-commands.zip (portable!)
```

---

### Example 2: Workflow Skill (implement-v2)

**File:** `.claude/skills/development/implement-v2/SKILL.md`

```markdown
---
name: implement
description: Implement features using TDD workflow with bmad-commands for file operations and testing
acceptance:
  - tests_passing: "All tests must pass"
  - coverage_threshold: "Test coverage >= 80%"
  - no_syntax_errors: "Code must have no syntax errors"
inputs:
  task_id:
    type: string
    required: true
    description: "Task identifier"
outputs:
  implementation_complete:
    type: boolean
    description: "Whether implementation succeeded"
  test_coverage_percent:
    type: number
    description: "Test coverage percentage achieved"
telemetry:
  emit: "skill.implement.completed"
  track:
    - task_id
    - test_coverage_percent
    - duration_ms
    - tests_total
    - tests_passed
---

# Implement Feature with TDD

## Overview
Implement features following Test-Driven Development workflow using bmad-commands for deterministic operations.

## Prerequisites
- Task specification exists at workspace/tasks/{task_id}.md
- bmad-commands skill available
- Test framework installed

## Workflow

### Step 1: Load Task Specification

Execute bmad-commands:
python .claude/skills/bmad-commands/scripts/read_file.py \
  --path workspace/tasks/{task_id}.md \
  --output json

Parse response:
- Check success == true
- Extract outputs.content for task specification
- Parse sections: Objective, Acceptance Criteria

### Step 2: RED Phase - Write Failing Tests

Write tests covering all acceptance criteria.

See: references/tdd-workflow.md for detailed TDD patterns.

### Step 3: GREEN Phase - Implement Code

Write minimum code to make tests pass.

### Step 4: Run Tests

Execute bmad-commands:
python .claude/skills/bmad-commands/scripts/run_tests.py \
  --path . \
  --framework jest \
  --output json

Verify:
- outputs.passed == true
- outputs.coverage_percent >= 80

### Step 5: Verify Acceptance Criteria

Check all criteria from task spec are met.

## Output

Return structured output with telemetry:
{
  "implementation_complete": true,
  "test_coverage_percent": 87,
  "tests_passed": true
}
```

**Packaging:**
```bash
python scripts/package_skill.py .claude/skills/development/implement-v2
# ✅ Creates implement-v2.zip (portable!)
```

---

### Example 3: Subagent (james-developer-v2)

**File:** `.claude/agents/james-developer-v2.md` (single file, not a directory)

**(NOT SKILL.md - this is a subagent file!)**

```markdown
---
name: james-developer-v2
description: Developer subagent with intelligent routing, guardrails, and automated verification. Use proactively for implementation tasks.
tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
---

# James Developer V2 Subagent

## Role
Implementation specialist with intelligent routing

## Command: *implement

### Workflow

**Step 1: Load Task Specification**

Use bmad-commands:
python .claude/skills/bmad-commands/scripts/read_file.py \
  --path workspace/tasks/{task_id}.md

**Step 2: Assess Complexity**

Calculate score using inline formula:
- Files: 1-2=10pts, 3-5=30pts, 6+=60pts
- DB: None=0pts, Schema=50pts, Migration=90pts
- API: None=0pts, Modify=30pts, New=60pts

**Step 3: Route to Skill**

Based on complexity:
- ≤30: Use .claude/skills/development/implement-v2/SKILL.md
- >60: Use .claude/skills/development/implement-with-discovery/SKILL.md

Execute selected skill.

**Step 4: Verify Acceptance**

Check skill outputs against acceptance criteria:
- tests_passing must be true
- coverage_threshold must be >= 80

**Step 5: Emit Telemetry**

{
  "agent": "james-v2",
  "command": "implement",
  "routing": {"complexity": X, "skill": "implement-v2"},
  "result": {"success": true, "coverage": X}
}
```

**NOT packageable** (not a skill, different purpose - project-specific coordination)

---

## Migration Guide

### Starting from Scratch

1. **Create Layer 1 (Primitive Skill):**
   ```bash
   cd ~/.claude/plugins/.../skill-creator
   python scripts/init_skill.py bmad-commands --path /path/to/skills
   # Edit SKILL.md, create scripts/, package
   ```

2. **Create Layer 2 (Workflow Skills):**
   ```bash
   python scripts/init_skill.py implement --path /path/to/skills/development
   # Edit SKILL.md, add contracts, reference Layer 1, package
   ```

3. **Create Layer 3 (Subagent):**
   ```bash
   # Create single .md file in .claude/agents/
   touch .claude/agents/james-developer-v2.md

   # Edit james-developer-v2.md with:
   # - YAML frontmatter (name, description, tools, model)
   # - Routing logic (inline)
   # - Guardrails (inline)
   # - Workflow instructions (inline)
   ```

---

### Migrating Existing Skills

**If you have skills without V2 architecture:**

1. **Keep skill structure** (don't change SKILL.md location)
2. **Add contracts** to YAML frontmatter
3. **Integrate primitives** where appropriate (Layer 1 calls to bmad-commands)
4. **Create routing guidance** if called by subagents
5. **Re-package** and distribute

**Skills remain skills throughout!**

---

## Summary

### Key Takeaways

✅ **Skills remain skills** - All follow skill-creator pattern
✅ **Layers define roles** - How skills work together, not file structure
✅ **Portability guaranteed** - Skills packageable, distributable
✅ **Primitives are skills** - bmad-commands IS A SKILL with scripts/
✅ **Subagents are different** - Single .md coordination files, not skills

### The Three Layers

| Layer | What It Is | File Structure | Packageable? |
|-------|------------|----------------|--------------|
| **1: Primitives** | Skill with scripts | SKILL.md + scripts/ | ✅ Yes |
| **2: Workflows** | Skill with workflow | SKILL.md + references/ | ✅ Yes |
| **3: Subagents** | Coordination file | agent.md (single file) | ❌ No |

### Architecture Benefits

- ✅ **Observable:** Telemetry at every layer
- ✅ **Testable:** Primitives are unit-testable
- ✅ **Composable:** Skills call other skills
- ✅ **Safe:** Guardrails and acceptance checks
- ✅ **Portable:** Skills work anywhere

---

**Version:** 2.0.0
**Status:** Production Ready
**Next:** Use this architecture for all BMAD skills
