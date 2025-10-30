# Terminology Alignment with Claude Code Documentation

**Date:** October 29, 2025
**Purpose:** Align BMAD Enhanced terminology with official Claude Code terminology
**Based On:** docs.claude.com official documentation

---

## Executive Summary

We need to update our architecture terminology to match Claude Code's official terms exactly. Our current "3-Layer Architecture" uses non-standard terminology that can confuse users.

**Current Issues:**
- ❌ Calling Layer 1 "Primitive Skills Layer" when it's actually a **skill**
- ❌ Not using actual slash commands despite the name
- ⚠️ Mixed terminology confuses the distinction between Claude Code features

**Correct Alignment:**
- ✅ Use official Claude Code terms: **Skills**, **Subagents**, **Slash Commands**
- ✅ Describe our architecture using standard terminology
- ✅ Add actual slash commands if we want that feature

---

## Official Claude Code Terminology

### 1. Skills (Agent Skills)

**Official Definition (from docs.claude.com/skills):**
> "Agent Skills extend Claude's capabilities through modular, discoverable packages. Each Skill consists of a SKILL.md file containing instructions that Claude reads when relevant, plus optional supporting files like scripts and templates."

**Key Points:**
- Skills are stored in `.claude/skills/`
- Have `SKILL.md` with YAML frontmatter
- Can include scripts, templates, references
- Model-invoked (Claude decides when to use)
- Focused on single capability

**Examples from docs:**
- "PDF form filling skill"
- "Data analysis skill"
- "Code review skill"

---

### 2. Subagents

**Official Definition (from docs.claude.com/sub-agents):**
> "Subagents are specialized AI assistants that Claude Code can delegate tasks to. Each operates independently with its own context window, custom system prompt, and configurable tool access."

**Key Points:**
- Subagents are stored in `.claude/agents/`
- Single `.md` file with YAML frontmatter
- Have custom system prompts
- Control which tools they can access
- Separate context windows

**Examples from docs:**
- "Code reviewer subagent"
- "Debugger subagent"
- "Data scientist subagent"

---

### 3. Slash Commands

**Official Definition (from docs.claude.com/slash-commands):**
> "Slash commands are a core feature of Claude Code that allow you to control Claude's behavior during interactive sessions. They enable automation of frequently-used prompts and provide shortcuts to essential functionality."

**Key Points:**
- Commands are stored in `.claude/commands/`
- Markdown files with optional frontmatter
- Invoked manually with `/command-name`
- Support arguments: `$1`, `$2`, `$ARGUMENTS`
- Can execute bash with `!` prefix

**Examples from docs:**
- Built-in: `/clear`, `/review`, `/help`
- Custom: `/review-pr`, `/deploy`, `/analyze-logs`

---

## Our Current Terminology (Incorrect)

### What We Call It

**"3-Layer Architecture: Commands → Skills → Subagents"**

```
Layer 1: Primitive Skills (bmad-commands)
Layer 2: Workflow Skills
Layer 3: Subagents
```

### Problems with This

**Problem 1: "Commands" is misleading**
- We call it "Primitive Skills Layer"
- But it's NOT slash commands (no `/` invocation)
- It's actually just a skill with bundled Python scripts
- This confuses users about what "commands" means

**Problem 2: Not using actual slash commands**
- `.claude/commands/` directory doesn't exist
- Can't use `/read-task` or `/run-tests`
- Missing a useful Claude Code feature

**Problem 3: Mixed terminology**
- "Primitive Skills Layer" + "Skills Layer" sounds like different things
- Actually both are skills (Layer 1 is just a utility skill)
- Creates false distinction

---

## Correct Terminology (Using Claude Code Terms)

### Option A: Rename to Skills-Based Architecture ✅ RECOMMENDED

**"3-Layer Skills & Subagents Architecture"**

```
Layer 1: Primitive Skills
  └─ Skills that provide atomic operations
     Example: bmad-commands skill

Layer 2: Workflow Skills
  └─ Skills that compose primitives into workflows
     Example: implement-v2, estimate-stories

Layer 3: Subagents
  └─ Coordination layer that routes to appropriate skills
     Example: james-developer-v2
```

**Why this is correct:**
- ✅ Uses official Claude Code terms
- ✅ Accurately describes what each layer IS
- ✅ No confusion about "commands"
- ✅ Clear that Layers 1 & 2 are both skills (different roles)

---

### Option B: Add Actual Slash Commands (Full Feature Use)

**"4-Layer Architecture: Commands → Primitive Skills → Workflow Skills → Subagents"**

```
Layer 0: Slash Commands
  └─ Quick manual invocations
     Location: .claude/commands/
     Example: /read-task, /run-tests

Layer 1: Primitive Skills
  └─ Atomic operations (scripts, utilities)
     Location: .claude/skills/bmad-commands/
     Example: bmad-commands skill

Layer 2: Workflow Skills
  └─ Composed workflows
     Location: .claude/skills/development/, .claude/skills/planning/
     Example: implement-v2, estimate-stories

Layer 3: Subagents
  └─ Intelligent routing & orchestration
     Location: .claude/agents/
     Example: james-developer-v2
```

**Why this is correct:**
- ✅ Uses ALL Claude Code features
- ✅ Slash commands are actual commands
- ✅ Skills are clearly identified as skills
- ✅ Subagents are clearly coordination layer
- ✅ No terminology confusion

---

## Recommended Changes

### Change 1: Rename Layer 1 ✅ REQUIRED

**Current:**
- "Primitive Skills Layer"
- "Primitive Skills"
- "bmad-commands provides primitive operations"

**Correct:**
- "Primitive Skills Layer" or "Utility Skills Layer"
- "Primitive Skills"
- "bmad-commands provides primitive operations"

**Rationale:**
- Accurately describes what it is (a skill)
- Doesn't claim to be slash commands
- Uses standard Claude Code terminology

---

### Change 2: Update Architecture Description ✅ REQUIRED

**Current Description:**
> "3-Layer Architecture: Commands → Skills → Subagents"

**Correct Description:**
> "3-Layer Architecture: Primitive Skills → Workflow Skills → Subagents"

Or more descriptive:
> "Layered Skills Architecture with Subagent Orchestration"

**Rationale:**
- Makes clear both Layer 1 and 2 are skills
- Uses official Claude Code terminology
- Describes the actual pattern

---

### Change 3: Add Actual Slash Commands (Optional) ⚠️

**Create:**
```
.claude/commands/
├── read-task.md          # /read-task <task-id>
├── run-tests.md          # /run-tests <test-path>
├── implement.md          # /implement <task-id>
└── review.md             # /review <task-id>
```

**Example Command:**
```markdown
# .claude/commands/read-task.md
---
description: Read and summarize a task specification
argument-hint: <task-id>
allowed-tools: Bash(python:*)
---

Read task specification for task-$1:

!python .claude/skills/bmad-commands/scripts/read_file.py \
  --path workspace/tasks/task-$1.md \
  --output json

Summarize the task objective, acceptance criteria, and technical requirements.
```

**Usage:** `/read-task auth-002`

**Benefits:**
- Quick manual operations
- Complements skills nicely
- Uses actual Claude Code slash commands feature
- Provides true "commands" layer

**Rationale:**
- If we want "commands", these are the official way
- Skills are for model-invoked capabilities
- Commands are for user-invoked shortcuts

---

## Updated Architecture Diagram

### Using Correct Claude Code Terminology

```
┌─────────────────────────────────────────────────────────────┐
│ BMAD Enhanced Architecture (Using Claude Code Terms)        │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ Layer 3: SUBAGENTS (Coordination & Routing)                 │
│ Location: .claude/agents/                                   │
│                                                              │
│ • james-developer-v2.md    ← Subagent (official term)       │
│ • alex-planner.md          ← Subagent                       │
│ • quinn-quality.md         ← Subagent                       │
│                                                              │
│ Routes to appropriate skills based on context               │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│ Layer 2: WORKFLOW SKILLS (Composed Operations)              │
│ Location: .claude/skills/development/, .claude/skills/...   │
│                                                              │
│ • implement-v2/SKILL.md    ← Skill (official term)          │
│ • estimate-stories/SKILL.md ← Skill                         │
│ • fix-issue/SKILL.md       ← Skill                          │
│                                                              │
│ Compose primitive operations into workflows                 │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│ Layer 1: PRIMITIVES (Atomic Operations)                     │
│ Location: .claude/skills/bmad-commands/                     │
│                                                              │
│ • bmad-commands/SKILL.md   ← Skill (official term)          │
│   └─ scripts/              ← Bundled Python scripts         │
│      ├─ read_file.py       ← Atomic operation               │
│      └─ run_tests.py       ← Atomic operation               │
│                                                              │
│ Provides testable, deterministic primitives                 │
└─────────────────────────────────────────────────────────────┘

Optional Layer 0 (if we add it):
┌─────────────────────────────────────────────────────────────┐
│ Layer 0: SLASH COMMANDS (Manual Quick Actions)              │
│ Location: .claude/commands/                                 │
│                                                              │
│ • /read-task <id>          ← Slash command (official term)  │
│ • /run-tests <path>        ← Slash command                  │
│ • /implement <id>          ← Slash command                  │
│                                                              │
│ Quick manual invocations, complements skills                │
└─────────────────────────────────────────────────────────────┘
```

---

## Terminology Glossary (Official Claude Code)

### Skills
- **What:** Modular capabilities packages
- **File:** `SKILL.md` with YAML frontmatter
- **Location:** `.claude/skills/`
- **Invoked:** Automatically by Claude (model-invoked)
- **Purpose:** Extend Claude's capabilities
- **Example:** `implement-v2` skill, `bmad-commands` skill

### Subagents
- **What:** Specialized AI assistants
- **File:** Single `.md` with YAML frontmatter
- **Location:** `.claude/agents/`
- **Invoked:** By delegation or explicit mention
- **Purpose:** Task-specific problem solving with separate context
- **Example:** `james-developer-v2` subagent

### Slash Commands
- **What:** Manual prompt shortcuts
- **File:** `.md` with optional frontmatter
- **Location:** `.claude/commands/`
- **Invoked:** Explicitly by user with `/command-name`
- **Purpose:** Quick, frequently-used operations
- **Example:** `/review-pr 123`

---

## Documentation Updates Required

### Files to Update

1. **Architecture Documents:**
   - `docs/3-layer-architecture-for-skills.md`
   - `docs/3-layer-architecture-prototype.md`
   - `docs/architecture-claude-code-compliance.md`

2. **Template:**
   - `docs/skill-refactoring-template.md`

3. **Reviews and Summaries:**
   - `docs/template-compliance-review.md`
   - `docs/template-v2-update-summary.md`
   - `docs/compliance-fixes-summary.md`

4. **README (if exists):**
   - Main project README

### Changes Needed

**Global find/replace:**
```bash
# Update terminology
"Primitive Skills Layer" → "Primitive Skills Layer"
"Primitive Skills" → "Primitive Skills"
"bmad-commands provides primitive operations" → "bmad-commands skill provides primitives"
"Layer 1: Primitive Skills" → "Layer 1: Primitive Skills"

# Keep correct terms
"Workflow Skills" → (already correct)
"Subagents" → (already correct)
```

**Manual updates:**
- Architecture diagrams
- Explanatory text
- Examples and descriptions

---

## Implementation Plan

### Phase 1: Terminology Updates (Required) ✅

**Step 1: Update Layer 1 Name**
- Find all: "Primitive Skills Layer", "Primitive Skills", "Layer 1: Primitive Skills"
- Replace with: "Primitive Skills Layer", "Primitive Skills", "Layer 1: Primitive Skills"

**Step 2: Update Descriptions**
- Update architecture diagrams
- Update explanatory text
- Clarify bmad-commands is a skill

**Step 3: Update Documentation**
- All markdown files in docs/
- All examples
- All diagrams

**Estimated Time:** 1-2 hours

---

### Phase 2: Add Slash Commands (Optional) ⚠️

**Step 1: Create Commands Directory**
```bash
mkdir -p .claude/commands
```

**Step 2: Create Initial Commands**
- `read-task.md` - Read task specification
- `run-tests.md` - Execute test suite
- `implement.md` - Start implementation
- `review.md` - Start code review

**Step 3: Document Commands**
- Add commands section to README
- Update architecture docs to show 4 layers
- Provide usage examples

**Estimated Time:** 2-3 hours

---

## Recommendation

### Immediate Action (Required) ✅

**Rename Layer 1 to use correct terminology:**

**FROM:**
```
Layer 1: Primitive Skills Layer
- bmad-commands provides primitive operations
- Primitive Skills pattern
```

**TO:**
```
Layer 1: Primitive Skills Layer
- bmad-commands skill provides primitive operations
- Utility skills with bundled scripts
```

**Why:**
- Aligns with official Claude Code terminology
- Accurately describes what it is (a skill)
- Removes confusion about "commands"
- No breaking changes (just terminology)

---

### Optional Addition (Nice to Have) ⚠️

**Add actual slash commands:**
- Create `.claude/commands/` directory
- Add 4-5 useful commands
- Update docs to show this feature
- Demonstrate full Claude Code feature usage

**Why:**
- Uses more of Claude Code's capabilities
- Provides quick manual operations
- Complements skills nicely
- Shows complete feature integration

---

## Summary

**Problem:** Using non-standard "Commands" terminology when we should use "Skills"

**Solution:** Rename to "Primitive Skills" to match official Claude Code terminology

**Impact:**
- ✅ Aligns with Claude Code documentation
- ✅ Removes terminology confusion
- ✅ Accurately describes architecture
- ✅ No breaking changes (terminology only)

**Next Step:** Update all documentation to use correct terminology

---

**Correct Architecture Name:**
> "**3-Layer Skills & Subagents Architecture:**
> Primitive Skills → Workflow Skills → Subagents"

Or:
> "**Layered Skills Architecture with Subagent Orchestration**"

---

*Terminology aligned with official Claude Code documentation (docs.claude.com)*
