# BMAD Enhanced - Installation Guide

**How to install and use BMAD Enhanced in your projects**

Version: 2.0
Last Updated: 2025-11-05

---

## Table of Contents

1. [Quick Installation](#quick-installation)
2. [What Gets Installed](#what-gets-installed)
3. [How It Works](#how-it-works)
4. [Verification Steps](#verification-steps)
5. [Troubleshooting](#troubleshooting)
6. [Advanced Configuration](#advanced-configuration)

---

## Quick Installation

### Option 1: Copy Entire .claude Folder (Recommended)

**Step 1: Copy the folder**
```bash
# From BMAD Enhanced project
cp -r .claude /path/to/your/new/project/

# Or if you're in your new project
cp -r /path/to/bmad-enhanced/.claude .
```

**Step 2: Verify structure**
```bash
cd /path/to/your/new/project
ls -la .claude/
```

You should see:
```
.claude/
├── agents/         # 10 subagent files
├── commands/       # 15 slash commands
├── skills/         # 31 skills organized by domain
├── config.yaml     # Optional configuration
└── settings.local.json  # Optional local settings
```

**Step 3: Test it works**
```bash
# Open Claude Code in your project
cd /path/to/your/new/project

# Test a simple command
/alex *create-task-spec "Test feature"
```

**That's it!** ✅ No plugin installation needed, no additional setup required.

---

## What Gets Installed

### Directory Structure

```
your-project/
├── .claude/
│   ├── agents/                    # Layer 3: Subagents (10 files)
│   │   ├── alex-planner-v2.md
│   │   ├── james-developer-v2.md
│   │   ├── quinn-quality-v2.md
│   │   ├── winston-architect.md
│   │   ├── orchestrator-v2.md
│   │   ├── john-pm.md
│   │   ├── mary-analyst.md
│   │   ├── sarah-po.md
│   │   ├── bob-sm.md
│   │   └── sally-ux-expert.md
│   │
│   ├── commands/                  # Slash commands (15 files)
│   │   ├── alex.md
│   │   ├── james.md
│   │   ├── quinn.md
│   │   ├── winston.md
│   │   ├── orchestrator.md
│   │   ├── john.md
│   │   ├── mary.md
│   │   ├── sarah.md
│   │   ├── bob.md
│   │   ├── sally.md
│   │   ├── design-architecture.md
│   │   ├── analyze-architecture.md
│   │   ├── review-architecture.md
│   │   ├── winston-consult.md
│   │   └── validate-story.md
│   │
│   └── skills/                    # Layer 1 & 2: Skills (31 total)
│       ├── bmad-commands/         # Layer 1: Primitives
│       │   ├── SKILL.md
│       │   ├── scripts/           # Python scripts
│       │   └── references/
│       │
│       ├── planning/              # Layer 2: Planning skills (13)
│       │   ├── create-task-spec/
│       │   ├── breakdown-epic/
│       │   ├── estimate-stories/
│       │   ├── refine-story/
│       │   ├── sprint-plan/
│       │   ├── create-prd/
│       │   ├── create-brownfield-prd/
│       │   └── ...
│       │
│       ├── development/           # Layer 2: Development skills (3)
│       │   ├── implement-v2/
│       │   ├── fix-issue/
│       │   └── test-runner/
│       │
│       ├── quality/               # Layer 2: Quality skills (9)
│       │   ├── review-task/
│       │   ├── refactor-code/
│       │   ├── quality-gate/
│       │   ├── nfr-assess/
│       │   └── ...
│       │
│       ├── brownfield/            # Layer 2: Brownfield skills (4)
│       │   ├── analyze-architecture/
│       │   ├── compare-architectures/
│       │   └── ...
│       │
│       └── implementation/        # Layer 2: Implementation (1)
│           └── execute-task/
│
├── src/                          # Your project code
├── tests/                        # Your project tests
└── ...
```

---

## How It Works

### No Plugin Installation Required

**BMAD Enhanced skills are NOT plugins** - they're part of your project structure.

**How skills load:**

1. **You type a command:**
   ```bash
   /alex *create-task-spec "User login feature"
   ```

2. **Slash command routes to agent:**
   - `/alex.md` tells Claude to invoke the `alex-planner-v2` agent
   - Uses the Task tool to load `.claude/agents/alex-planner-v2.md`

3. **Agent sees \*task command:**
   - Agent's routing logic recognizes `*create-task-spec`
   - Routes to skill: `.claude/skills/planning/create-task-spec/SKILL.md`

4. **Agent dynamically loads skill:**
   - Agent uses **Read tool** to load the skill file
   - Skill file is markdown with step-by-step instructions
   - Agent follows instructions like a recipe

5. **Agent executes skill:**
   - Follows skill's workflow instructions
   - Uses tools (Read, Write, Bash, etc.) as directed
   - Returns result to you

**Key Point:** Skills load automatically when agents need them. No `/plugin` command needed!

---

## Verification Steps

### Step 1: Verify Directory Structure

```bash
# Check .claude folder exists
ls -la .claude/

# Check agents (should see 10 .md files)
ls .claude/agents/

# Check skills (should see 8 directories)
ls .claude/skills/

# Check commands (should see 15 .md files)
ls .claude/commands/*.md
```

**Expected Output:**
```
✓ .claude/ exists
✓ .claude/agents/ contains 10+ files
✓ .claude/skills/ contains 8 directories
✓ .claude/commands/ contains 15 files
```

### Step 2: Test Slash Commands

```bash
# Test help (should show command expanded)
/alex

# Test actual command
/alex *create-task-spec "Simple test feature"
```

**Expected Behavior:**
- `/alex` alone should show the alex subagent loading
- `/alex *create-task-spec "..."` should create a task specification

### Step 3: Verify Skills Load

When you run a command, you should see output like:
```
✓ Loading alex-planner-v2 agent
✓ Routing to create-task-spec skill
✓ Reading .claude/skills/planning/create-task-spec/SKILL.md
✓ Executing workflow...
```

### Step 4: Check Configuration (Optional)

```bash
# Check if config exists
cat .claude/config.yaml

# Check if settings exist
cat .claude/settings.local.json
```

These are optional - skills work without them.

---

## Troubleshooting

### Problem: "Command not found" or "/alex not recognized"

**Cause:** Slash commands not loading

**Solution:**
```bash
# Verify commands directory exists
ls .claude/commands/alex.md

# Check file is readable
cat .claude/commands/alex.md | head -10
```

If file doesn't exist, copy it from BMAD Enhanced:
```bash
cp /path/to/bmad-enhanced/.claude/commands/alex.md .claude/commands/
```

---

### Problem: "Skill file not found"

**Cause:** Agent can't find skill file

**Solution:**
```bash
# Verify skills directory structure
ls .claude/skills/planning/create-task-spec/SKILL.md

# Check skill file is readable
cat .claude/skills/planning/create-task-spec/SKILL.md | head -20
```

If skill doesn't exist, copy entire skills directory:
```bash
cp -r /path/to/bmad-enhanced/.claude/skills .claude/
```

---

### Problem: "Agent not loading"

**Cause:** Agent file missing or corrupted

**Solution:**
```bash
# Verify agent exists
ls .claude/agents/alex-planner-v2.md

# Check YAML frontmatter
head -10 .claude/agents/alex-planner-v2.md
```

Should start with:
```yaml
---
name: alex-planner-v2
description: Planning subagent...
tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
---
```

If missing, copy from BMAD Enhanced:
```bash
cp /path/to/bmad-enhanced/.claude/agents/alex-planner-v2.md .claude/agents/
```

---

### Problem: "Python scripts not found"

**Cause:** bmad-commands scripts missing

**Solution:**
```bash
# Verify scripts exist
ls .claude/skills/bmad-commands/scripts/

# Should contain .py files
ls .claude/skills/bmad-commands/scripts/*.py
```

If missing, copy entire bmad-commands skill:
```bash
cp -r /path/to/bmad-enhanced/.claude/skills/bmad-commands .claude/skills/
```

---

## Advanced Configuration

### Custom Configuration (Optional)

Create `.claude/config.yaml`:

```yaml
# Basic Configuration
workspaceRoot: "./workspace"
testFramework: "auto-detect"  # or "jest", "pytest", "junit", etc.
coverageThreshold: 80

# Quality Standards
quality:
  min_coverage: 80
  max_complexity: 10

# Development Settings
development:
  tdd_required: true
  max_files_simple: 5

# Telemetry (optional)
telemetry:
  enabled: true
  output_dir: ".claude/telemetry"
```

### Local Settings (Optional)

Create `.claude/settings.local.json` for machine-specific settings:

```json
{
  "workspaceRoot": "/absolute/path/to/workspace",
  "pythonPath": "/usr/bin/python3",
  "testCommand": "npm test"
}
```

**Note:** Both files are optional. Skills use sensible defaults if not present.

---

## Minimal Installation

If you only want core functionality, you can install a subset:

### Core Only (5 agents, 15 skills)

```bash
# Create structure
mkdir -p .claude/{agents,commands,skills}

# Copy core agents (5)
cp bmad-enhanced/.claude/agents/alex-planner-v2.md .claude/agents/
cp bmad-enhanced/.claude/agents/james-developer-v2.md .claude/agents/
cp bmad-enhanced/.claude/agents/quinn-quality-v2.md .claude/agents/
cp bmad-enhanced/.claude/agents/winston-architect.md .claude/agents/
cp bmad-enhanced/.claude/agents/orchestrator-v2.md .claude/agents/

# Copy core commands (5)
cp bmad-enhanced/.claude/commands/alex.md .claude/commands/
cp bmad-enhanced/.claude/commands/james.md .claude/commands/
cp bmad-enhanced/.claude/commands/quinn.md .claude/commands/
cp bmad-enhanced/.claude/commands/winston.md .claude/commands/
cp bmad-enhanced/.claude/commands/orchestrator.md .claude/commands/

# Copy essential skills
cp -r bmad-enhanced/.claude/skills/bmad-commands .claude/skills/
cp -r bmad-enhanced/.claude/skills/planning .claude/skills/
cp -r bmad-enhanced/.claude/skills/development .claude/skills/
cp -r bmad-enhanced/.claude/skills/quality .claude/skills/
```

This gives you the essential workflow: plan → develop → review.

---

## Updating BMAD Enhanced

### Update Existing Installation

```bash
# Backup current installation
cp -r .claude .claude.backup

# Copy updated files from BMAD Enhanced
cp -r /path/to/bmad-enhanced/.claude .

# If you had custom config, restore it
cp .claude.backup/config.yaml .claude/
cp .claude.backup/settings.local.json .claude/
```

### Verify Update

```bash
# Check agent versions
grep "version\|Version" .claude/agents/alex-planner-v2.md

# Test command
/alex *create-task-spec "Test after update"
```

---

## FAQ

### Q: Do I need to run `/plugin` command?

**A: No.** Skills are part of your project structure, not plugins. They load automatically when agents need them.

### Q: Can I modify skills for my project?

**A: Yes!** Skills are just markdown files. Edit them to fit your workflow. Just maintain the YAML frontmatter and workflow structure.

### Q: Do skills work offline?

**A: Yes.** Skills are local files. No internet connection needed (except for Claude Code itself).

### Q: Can I share skills across projects?

**A: Yes.** Just copy the `.claude/` folder to any project. Skills are portable.

### Q: What if I only want some skills?

**A: Fine!** Just copy the skills you need. Remove unused ones from `.claude/skills/` directory.

### Q: Do I need Python installed?

**A: Only for bmad-commands primitives.** If you use primitives that run Python scripts (like `read_file.py`, `run_tests.py`), you need Python 3.7+. Otherwise, no.

---

## Summary

**Installation Steps:**

1. ✅ Copy `.claude/` folder to your project
2. ✅ Verify structure with `ls .claude/`
3. ✅ Test with `/alex *create-task-spec "Test"`
4. ✅ Start using BMAD Enhanced!

**No plugin installation, no configuration required, works immediately!**

---

**See Also:**
- [QUICK-START.md](./QUICK-START.md) - Get started in 10 minutes
- [USER-GUIDE.md](./USER-GUIDE.md) - Complete usage guide
- [TROUBLESHOOTING.md](./TROUBLESHOOTING.md) - Common issues
- [3-layer-architecture-for-skills.md](./3-layer-architecture-for-skills.md) - How skills work

---

**Version:** 2.0
**Status:** Production Ready
**Installation Time:** < 5 minutes
