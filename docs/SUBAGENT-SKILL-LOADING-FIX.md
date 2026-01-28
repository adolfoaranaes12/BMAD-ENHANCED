# Subagent Skill Loading Fix

**Date:** 2025-11-06
**Issue:** Subagents were not properly invoking skills when receiving `*` commands
**Status:** ✅ Fixed

---

## The Problem

When users invoked slash commands like `/winston *analyze-architecture .`, the subagents were:

1. Loading correctly via the slash command
2. But then trying to use `Read(.claude/skills/*/SKILL.md)` instead of invoking the skill
3. This caused the skill documentation to load as text instead of the skill actually executing

## Root Cause

Agent prompts instructed subagents to **"Read the skill file"** rather than **"invoke the skill using the Skill tool"**.

Skills are designed to be invoked via the `Skill` tool, NOT read as regular files.

---

## The Fix Pattern

### ❌ WRONG Pattern #1 (Describing Workflow)

```markdown
## Command: `*create-task-spec`

### Workflow

#### Step 1: Load Requirements
Parse user input to extract requirements...

#### Step 2: Assess Complexity
Calculate complexity score...
```

**Problem:** The subagent describes the workflow but never loads the skill.

---

### ❌ WRONG Pattern #2 (Using Read Tool)

```markdown
## Command: `*create-task-spec`

**Skill Path:** `.claude/skills/create-task-spec/SKILL.md`

**Action:**
1. **Load the skill:** Read(.claude/skills/create-task-spec/SKILL.md)
2. **Execute the skill's workflow** exactly as documented
```

**Problem:** Using Read() treats the skill as a text file, not as an executable skill. The skill never actually invokes.

---

### ✅ CORRECT Pattern (Using Skill Tool)

```markdown
## Command: `*create-task-spec`

**Skill Name:** `create-task-spec`

**Action:**
1. **Invoke skill:** `Skill(command="create-task-spec")`
2. The skill will expand with its full prompt
3. **Execute the skill's workflow** exactly as documented in the expanded prompt
4. **Follow all steps** defined in the skill
5. **Generate outputs** as specified in the skill

**Usage:**
```bash
/alex *create-task-spec "User signup with email"
/alex *create-task-spec workspace/stories/story-123.md
```
```

**Solution:** The subagent invokes the skill using the Skill tool, waits for expansion, then executes.

---

## Required Changes for Each Subagent

### 1. Add Command-to-Skill Mapping Table

Add this section at the top of command routing:

```markdown
## Command-to-Skill Mapping

**CRITICAL:** When you receive a command starting with `*`, immediately invoke the corresponding skill using the Skill tool:

| Command | Skill Tool Invocation |
|---------|----------------------|
| `*command-name` | `Skill(command="skill-name")` |

**Execution Flow:**
1. User provides: `/subagent *command-name args`
2. You immediately call: `Skill(command="skill-name")`
3. Wait for skill expansion message
4. The skill's full prompt will be provided
5. Execute the skill's documented workflow with the provided parameters
```

### 2. Update Command Routing Section

Replace Read() instructions with Skill tool invocations:

```markdown
## Command Routing & Skill Execution

**CRITICAL:** [Subagent Name] must **use the Skill tool to load and execute skills**.
When you see a command starting with `*`, invoke the corresponding skill using the Skill tool.

### Command: `*command-name`

**Skill Name:** `skill-name`

**Action:**
1. **Invoke skill:** `Skill(command="skill-name")`
2. The skill will expand with its full prompt
3. **Execute the skill's workflow** exactly as documented in the expanded prompt
4. **Follow all steps** defined in the skill
5. **Generate outputs** as specified in the skill

**Usage:**
```bash
/subagent *command-name [args]
```
```

### 3. Update Execution Pattern

Replace Read() references with Skill tool:

```markdown
## Execution Pattern

**For every command received:**

1. Parse command and arguments
2. Identify corresponding skill name
3. Invoke skill using Skill tool: Skill(command="skill-name")
4. Wait for skill prompt to expand
5. Execute the skill's documented workflow
6. Follow all steps in sequence
7. Generate specified outputs
8. Return results to user

**Example Execution Flow:**

User: /subagent *command-name args

Subagent:
1. Recognizes command: *command-name
2. Invokes skill: Skill(command="skill-name")
3. Skill expands with full prompt
4. Follows skill's documented workflow
5. Generates outputs as specified
6. Returns results to user
```

### 4. Update Important Principles

Replace Read() examples with Skill tool:

```markdown
## Important Principles

### 1. Always Use the Skill Tool
**DO:** Invoke skills using the Skill tool
```
Skill(command="skill-name")
Skill(command="another-skill")
```

**DON'T:** Try to execute from memory or use Read()
```
❌ "I'll create [output] based on what I know..."
❌ Read(.claude/skills/skill-name/SKILL.md)  # Wrong approach
```

### 2. Follow Skill Workflows Exactly
After the skill expands, the skill prompt contains the authoritative workflow. Execute each step in sequence as documented.

### 3. Use Skill-Defined Outputs
Generate outputs in the format and location specified by the expanded skill prompt.

### 4. Leverage Skill References
If the expanded skill prompt references additional files in references/ directories, use Read tool to load those as needed during execution.
```

---

## Subagent-to-Skill Mapping

### Alex (alex-planner-v2)
- `*create-task-spec` → `.claude/skills/create-task-spec/SKILL.md`
- `*breakdown-epic` → `.claude/skills/breakdown-epic/SKILL.md`
- `*estimate-stories` → `.claude/skills/estimate-stories/SKILL.md`
- `*refine-story` → `.claude/skills/refine-story/SKILL.md`
- `*sprint-plan` → `.claude/skills/sprint-plan/SKILL.md`

### James (james-developer-v2)
- `*implement` → `.claude/skills/implement-feature/SKILL.md`
- `*fix` → `.claude/skills/fix-issue/SKILL.md`
- `*test` → `.claude/skills/run-tests/SKILL.md`
- `*refactor` → `.claude/skills/refactor-code/SKILL.md`
- `*apply-qa-fixes` → `.claude/skills/apply-qa-fixes/SKILL.md`

### Quinn (quinn-quality-v2)
- `*review` → `.claude/skills/review-task/SKILL.md`
- `*nfr-assess` → `.claude/skills/nfr-assess/SKILL.md`
- `*quality-gate` → `.claude/skills/quality-gate/SKILL.md`
- `*trace-requirements` → `.claude/skills/trace-requirements/SKILL.md`
- `*risk-profile` → `.claude/skills/risk-profile/SKILL.md`

### Winston (winston-architect)
- `*create-architecture` → `.claude/skills/create-architecture/SKILL.md`
- `*analyze-architecture` → `.claude/skills/analyze-architecture/SKILL.md`
- `*create-adr` → `.claude/skills/create-adr/SKILL.md`
- `*validate-architecture` → `.claude/skills/validate-architecture/SKILL.md`
- `*review-architecture` → `.claude/skills/architecture-review/SKILL.md`
- `*compare-architectures` → `.claude/skills/compare-architectures/SKILL.md`

### Orchestrator (orchestrator-v2)
- `*workflow` → Routes to multiple subagents (special case)
- `*coordinate` → Routes to multiple subagents (special case)

### Bob (bob-sm)
- Commands route to Alex/James/Quinn as needed

### John (john-pm)
- `*create-prd` → `.claude/skills/create-prd/SKILL.md`
- `*create-brownfield-prd` → `.claude/skills/create-brownfield-prd/SKILL.md`

### Mary (mary-analyst)
- Business analysis commands (no skills yet - uses conversational approach)

### Sally (sally-ux-expert)
- UX commands (no skills yet - uses conversational approach)

### Sarah (sarah-po)
- `*validate-story` → `.claude/skills/validate-story/SKILL.md`

---

## Verification Script

Use this to check if subagents are correctly loading skills:

```bash
#!/bin/bash
# Check if subagents reference Read() for skill loading

echo "=== Checking Subagent Skill Loading ==="
echo ""

for agent in .claude/agents/*.md; do
  agent_name=$(basename "$agent" .md)

  if grep -q "Read(.claude/skills/" "$agent"; then
    echo "✅ $agent_name - Loads skills correctly"
  else
    echo "❌ $agent_name - NOT loading skills (needs fix)"
  fi
done

echo ""
echo "=== Checking for Command Routing Section ==="
echo ""

for agent in .claude/agents/*.md; do
  agent_name=$(basename "$agent" .md)

  if grep -q "Command Routing & Skill Execution" "$agent"; then
    echo "✅ $agent_name - Has routing section"
  else
    echo "⚠️  $agent_name - Missing routing section"
  fi
done
```

---

## Testing After Fix

After applying fixes, test each subagent:

```bash
# Test Winston
/winston *analyze-architecture .

# Test Alex
/alex *create-task-spec "Test feature"

# Test James
/james *implement workspace/tasks/task-001.md

# Test Quinn
/quinn *review workspace/tasks/task-001.md
```

Verify that:
1. Subagent loads the skill file (watch for Read() calls)
2. Subagent follows the skill's documented workflow
3. Subagent generates outputs as specified in the skill
4. No improvisation or "based on what I know" behavior

---

## Status

### ✅ Fixed (Using Skill Tool)
- ✅ Winston (winston-architect) - Fixed 2025-11-06
- ✅ Alex (alex-planner-v2) - Fixed 2025-11-06
- ✅ James (james-developer-v2) - Already correct
- ✅ Quinn (quinn-quality-v2) - Already correct
- ✅ Orchestrator (orchestrator-v2) - Already correct

### ⚠️  No Skills (Conversational Agents)
- ⚠️  Bob (bob-sm) - Routes to other agents
- ⚠️  Mary (mary-analyst) - No skills (conversational)
- ⚠️  Sally (sally-ux-expert) - No skills (conversational)

### 🔍 To Be Checked
- 🔍 John (john-pm) - Needs verification
- 🔍 Sarah (sarah-po) - Needs verification

---

## Verification Script

Use this to check if subagents are correctly using the Skill tool:

```bash
#!/bin/bash
# Check if subagents use Skill tool instead of Read() for skill loading

echo "=== Checking Subagent Skill Loading Pattern ==="
echo ""

for agent in .claude/agents/*-v2.md .claude/agents/winston-architect.md; do
  if [ -f "$agent" ]; then
    agent_name=$(basename "$agent" .md)

    # Check for WRONG pattern (Read for skills)
    if grep -q "Read(.claude/skills/" "$agent"; then
      echo "❌ $agent_name - Uses Read() (WRONG - needs Skill tool)"
    # Check for CORRECT pattern (Skill tool)
    elif grep -q 'Skill(command=' "$agent"; then
      echo "✅ $agent_name - Uses Skill tool (CORRECT)"
    else
      echo "⚠️  $agent_name - No skill loading found"
    fi
  fi
done
```

---

## Testing After Fix

After applying fixes, test each subagent:

```bash
# Test Winston
/winston *analyze-architecture .

# Test Alex
/alex *create-task-spec "Test feature"

# Test James
/james *implement workspace/tasks/task-001.md

# Test Quinn
/quinn *review workspace/tasks/task-001.md
```

Verify that:
1. ✅ Subagent invokes the Skill tool (not Read)
2. ✅ System shows: `<command-message>skill-name is running…</command-message>`
3. ✅ Skill expands with full prompt
4. ✅ Subagent follows the skill's documented workflow
5. ✅ Subagent generates outputs as specified in the skill
6. ✅ No improvisation or "based on what I know" behavior

---

## Key Takeaways

1. **Always use Skill tool for skill invocation** - Skills are designed to be invoked via the Skill tool, NOT read as files
2. **Read() loads text, Skill() executes skills** - There's a fundamental difference
3. **Command-to-skill mapping is critical** - Explicit mapping tables prevent confusion
4. **Execution flow must include expansion step** - Agents need to "wait for skill expansion"
5. **Examples matter** - DO/DON'T examples help reinforce correct behavior

---

## Next Steps

1. ✅ Winston fixed
2. ✅ Alex fixed
3. 🔍 Check John and Sarah
4. ✅ James, Quinn, Orchestrator already correct
5. ✅ Document the fix pattern

---

**Last Updated:** 2025-11-06
**Fixed By:** Corrected winston-architect and alex-planner-v2 to use Skill tool instead of Read()
