# Command Routing Mechanism Design

**Date:** January 15, 2025
**Status:** Design Complete - Ready for Implementation
**Purpose:** Enable `@subagent *command args` syntax for seamless subagent invocation

---

## Executive Summary

The command routing mechanism is the "glue" that connects user commands to subagents and skills. It parses commands like `@alex *breakdown "Epic"`, identifies the appropriate subagent and skill, and executes the workflow.

**What it does:**
```
User Input: "@alex *breakdown 'User Authentication'"
     ↓
Parse Command → Find Subagent → Find Skill → Execute → Return Output
     ↓              ↓              ↓           ↓           ↓
   alex        alex-planner   breakdown-   (run skill)  (output to user)
               .md            epic.md
```

**Why it's critical:**
- Without it, users must manually invoke skills via Skill tool (verbose)
- With it, natural language commands work seamlessly
- Enables orchestrator workflows
- Makes system feel like a team of AI assistants

---

## Current State

### What We Have

**Subagents (4):**
1. `alex-planner.md` - Planning subagent
2. `quinn-quality.md` - Quality subagent
3. `james-developer.md` - Development subagent
4. `orchestrator.md` - Workflow coordinator

**Skills (15):**
- Planning: 5 skills
- Quality: 6 skills
- Development: 3 skills
- Implementation: 1 skill

**Command Mappings:**
Each subagent file contains command mappings like:
```markdown
### Command: `*breakdown`
**Skill:** `.claude/skills/planning/breakdown-epic.md`
```

### What's Missing

**Command Router:**
- No parser for `@subagent *command args` syntax
- No mechanism to load subagent files
- No automatic skill execution
- No standardized output format

**Current Workaround:**
```
User: "Use the planning skill at .claude/skills/planning/breakdown-epic.md
       to break down the epic 'User Authentication'"
```

**Desired:**
```
User: "@alex *breakdown 'User Authentication'"
```

---

## Design Options

### Option A: Claude Code Native Integration (Ideal)

**How it works:**
- Claude Code natively recognizes `@subagent` syntax
- Parses command internally
- Loads subagent file
- Executes skill automatically
- Returns output

**Pros:**
- ✅ Seamless user experience
- ✅ Fast execution
- ✅ Clean syntax
- ✅ No workarounds needed

**Cons:**
- ❌ Requires Claude Code changes
- ❌ Not available today
- ❌ Outside our control

**Status:** Future possibility, requires Anthropic

---

### Option B: Slash Command Wrapper (Practical)

**How it works:**
- Create slash commands that invoke subagents
- `/alex breakdown "Epic"` → reads alex-planner.md → invokes skill
- Uses existing slash command infrastructure

**Implementation:**
```bash
# .claude/commands/alex.md
Parse command: "$1" (e.g., "breakdown")
Parse args: "${@:2}" (remaining arguments)

Load `.claude/subagents/alex-planner.md`
Find command mapping for "$1"
Extract skill path
Invoke skill via Skill tool

Return output
```

**Pros:**
- ✅ Works today
- ✅ Uses existing Claude Code features
- ✅ Relatively simple
- ✅ No external dependencies

**Cons:**
- ⚠️ Slightly different syntax (`/alex` instead of `@alex`)
- ⚠️ Requires creating slash command per subagent
- ⚠️ Limited error handling

**Status:** Implementable today

---

### Option C: Pre-Processor Script (Workaround)

**How it works:**
- User input intercepted by script
- `@subagent *command args` parsed and transformed
- Transformed into Skill tool invocation
- Passed to Claude Code

**Implementation:**
```bash
#!/bin/bash
# claude-code-wrapper.sh

# Read user input
input="$1"

# Check if input starts with @
if [[ "$input" == @* ]]; then
  # Parse: @alex *breakdown "Epic"
  subagent=$(echo "$input" | sed -n 's/@\([a-z]*\) .*/\1/p')
  command=$(echo "$input" | sed -n 's/@[a-z]* \*\([a-z-]*\).*/\1/p')
  args=$(echo "$input" | sed -n 's/@[a-z]* \*[a-z-]* \(.*\)/\1/p')

  # Load subagent file
  subagent_file=".claude/subagents/${subagent}-*.md"

  # Extract skill path for command
  skill_path=$(grep -A 1 "Command: \`\*${command}\`" "$subagent_file" | \
               grep "Skill:" | \
               sed 's/.*Skill:** `\(.*\)`/\1/')

  # Transform to Skill tool call
  transformed="Use the skill at ${skill_path} with input: ${args}"

  # Pass to Claude Code
  echo "$transformed"
else
  # Pass through unchanged
  echo "$input"
fi

# Invoke Claude Code with transformed input
claude-code "$transformed"
```

**Pros:**
- ✅ Implements exact `@subagent` syntax
- ✅ Transparent to user
- ✅ Flexible (can add features)

**Cons:**
- ❌ Requires wrapper script
- ❌ User must use wrapper instead of direct Claude Code
- ❌ May break with Claude Code updates
- ❌ Platform-dependent (bash script)

**Status:** Possible but fragile

---

### Option D: Skill-Based Router (Recommended)

**How it works:**
- Create a special "router" skill
- User invokes: Use `.claude/skills/router.md` with command "@alex *breakdown Epic"
- Router skill parses command, loads subagent, invokes target skill
- Returns output

**Implementation:**

**File:** `.claude/skills/router.md`

```markdown
# Command Router Skill

## Purpose
Route `@subagent *command args` to appropriate skills

## Input
Command string: "@alex *breakdown 'User Authentication'"

## Process

1. Parse command:
   - Subagent: "alex"
   - Command: "breakdown"
   - Args: "User Authentication"

2. Load subagent file:
   - File: `.claude/subagents/alex-planner.md`

3. Find command mapping:
   - Search for: "Command: `*breakdown`"
   - Extract skill path: `.claude/skills/planning/breakdown-epic.md`

4. Invoke skill:
   - Load skill file
   - Execute with args
   - Return output

## Example

Input: "@alex *breakdown 'User Authentication'"

Output:
"Routing to alex-planner → breakdown-epic.md

Executing breakdown-epic.md with input: 'User Authentication'

[skill output here]"
```

**Pros:**
- ✅ Works within Claude Code today
- ✅ No external dependencies
- ✅ Centralized routing logic
- ✅ Easy to extend

**Cons:**
- ⚠️ Still requires explicit Skill tool invocation
- ⚠️ Not as seamless as native `@subagent`
- ⚠️ Extra indirection layer

**Status:** Best option available today

---

## Recommended Approach: Hybrid (B + D)

**Combine Option B (slash commands) + Option D (router skill)**

### Phase 1: Router Skill (Immediate)
Create `.claude/skills/router.md` that handles command routing.

**Usage:**
```
User: Use .claude/skills/router.md with command "@alex *breakdown 'Epic'"
```

### Phase 2: Slash Command Shortcuts (Week 1)
Create slash commands for each subagent.

**Files to create:**
- `.claude/commands/alex.md`
- `.claude/commands/james.md`
- `.claude/commands/quinn.md`
- `.claude/commands/orchestrator.md`

**Usage:**
```
User: /alex breakdown "Epic"
```

### Phase 3: Native Integration (Future)
Work with Anthropic to add native `@subagent` support.

**Usage:**
```
User: @alex *breakdown "Epic"
```

---

## Detailed Design: Router Skill

### Router Skill Structure

**File:** `.claude/skills/router.md`

```markdown
# Command Router

## Inputs
- command: Full command string (e.g., "@alex *breakdown 'Epic'")

## Outputs
- Skill execution results
- Error messages (if routing fails)

## Process

### Step 1: Parse Command
Extract components from command string.

Pattern: `@<subagent> *<command> <args>`

Examples:
- "@alex *breakdown 'User Auth'" → subagent=alex, command=breakdown, args='User Auth'
- "@james *implement task-auth-002" → subagent=james, command=implement, args=task-auth-002
- "@quinn *review task-auth-002" → subagent=quinn, command=review, args=task-auth-002

### Step 2: Load Subagent File
Map subagent name to file:
- alex → .claude/subagents/alex-planner.md
- james → .claude/subagents/james-developer.md
- quinn → .claude/subagents/quinn-quality.md
- orchestrator → .claude/subagents/orchestrator.md

Read subagent file to get command mappings.

### Step 3: Find Command Mapping
Search subagent file for command definition.

Pattern to find:
```
### Command: `*<command>`
**Skill:** `<skill-path>`
```

Example:
```markdown
### Command: `*breakdown`
**Skill:** `.claude/skills/planning/breakdown-epic.md`
```

Extract skill path.

### Step 4: Validate Skill Exists
Check that skill file exists:
```bash
test -f .claude/skills/planning/breakdown-epic.md
```

If not found, return error.

### Step 5: Invoke Skill
Load skill file and execute with provided args.

Use Skill tool:
```
Skill("planning/breakdown-epic", args)
```

### Step 6: Return Output
Return skill execution results to user.

## Error Handling

### Error 1: Invalid Command Syntax
```
❌ Invalid Command Syntax

Input: "@alex breakdown Epic" (missing *)
Expected: "@alex *breakdown Epic"

Syntax: @<subagent> *<command> <args>
```

### Error 2: Unknown Subagent
```
❌ Unknown Subagent: @bob

Available subagents:
- @alex (Planner)
- @james (Developer)
- @quinn (Quality)
- @orchestrator (Coordinator)

Did you mean: @james?
```

### Error 3: Unknown Command
```
❌ Unknown Command: *deploy

Subagent: @alex (Planner)
Available commands:
- *breakdown - Break down epic into stories
- *estimate - Estimate story points
- *sprint - Create sprint plan
- *refine - Refine story
- *plan - Create task spec

Did you mean: *plan?
```

### Error 4: Skill File Not Found
```
❌ Skill File Not Found

Subagent: @alex
Command: *breakdown
Expected skill: .claude/skills/planning/breakdown-epic.md
Status: File does not exist

This is likely a configuration error.
Please check subagent command mappings.
```

## Examples

### Example 1: Successful Routing
```
Input: "@alex *breakdown 'User Authentication System'"

Processing:
1. ✅ Parsed: subagent=alex, command=breakdown, args='User Authentication System'
2. ✅ Loaded: .claude/subagents/alex-planner.md
3. ✅ Found mapping: breakdown → .claude/skills/planning/breakdown-epic.md
4. ✅ Skill exists: Yes
5. ✅ Executing: breakdown-epic.md with input 'User Authentication System'

Output:
[skill output]
```

### Example 2: Error - Unknown Command
```
Input: "@alex *deploy 'User Auth'"

Processing:
1. ✅ Parsed: subagent=alex, command=deploy, args='User Auth'
2. ✅ Loaded: .claude/subagents/alex-planner.md
3. ❌ Command not found: deploy

Error: Unknown command *deploy for subagent @alex

Available commands:
- *breakdown
- *estimate
- *sprint
- *refine
- *plan
```
```

---

## Detailed Design: Slash Commands

### Slash Command per Subagent

Create one slash command per subagent that wraps the router.

#### File: `.claude/commands/alex.md`

```markdown
Parse command and arguments from user input.

Command format: /alex <command> <args>

Example: /alex breakdown "User Authentication System"

Extract:
- command: ${1} (first argument, e.g., "breakdown")
- args: ${@:2} (remaining arguments)

Route to router skill:
Use .claude/skills/router.md with command "@alex *${1} ${@:2}"
```

#### File: `.claude/commands/james.md`

```markdown
Parse command and arguments from user input.

Command format: /james <command> <args>

Example: /james implement task-auth-002

Extract:
- command: ${1}
- args: ${@:2}

Route to router skill:
Use .claude/skills/router.md with command "@james *${1} ${@:2}"
```

#### File: `.claude/commands/quinn.md`

```markdown
Parse command and arguments from user input.

Command format: /quinn <command> <args>

Example: /quinn review task-auth-002

Extract:
- command: ${1}
- args: ${@:2}

Route to router skill:
Use .claude/skills/router.md with command "@quinn *${1} ${@:2}"
```

#### File: `.claude/commands/orchestrator.md`

```markdown
Parse command and arguments from user input.

Command format: /orchestrator <command> <args>

Example: /orchestrator deliver "User login feature"

Extract:
- command: ${1}
- args: ${@:2}

Route to router skill:
Use .claude/skills/router.md with command "@orchestrator *${1} ${@:2}"
```

### Usage Examples

**Before (verbose):**
```
User: Use the skill at .claude/skills/planning/breakdown-epic.md
      to break down the epic "User Authentication System"
```

**After (with slash commands):**
```
User: /alex breakdown "User Authentication System"
```

**Alternative (with router skill directly):**
```
User: Use .claude/skills/router.md with command
      "@alex *breakdown 'User Authentication System'"
```

---

## Implementation Plan

### Phase 1: Router Skill (2 hours)

**Tasks:**
1. Create `.claude/skills/router.md`
2. Implement command parsing logic
3. Implement subagent file loading
4. Implement command mapping extraction
5. Implement skill invocation
6. Add error handling
7. Test with all subagents

**Deliverable:**
- Working router skill
- Can route any `@subagent *command` to correct skill

---

### Phase 2: Slash Commands (1 hour)

**Tasks:**
1. Create `.claude/commands/alex.md`
2. Create `.claude/commands/james.md`
3. Create `.claude/commands/quinn.md`
4. Create `.claude/commands/orchestrator.md`
5. Test each command
6. Document usage

**Deliverable:**
- 4 slash commands
- Shortcut syntax for users

---

### Phase 3: Documentation & Testing (1 hour)

**Tasks:**
1. Update main README with command syntax
2. Create command reference guide
3. Add examples to each subagent file
4. Test end-to-end workflows
5. Create troubleshooting guide

**Deliverable:**
- Complete documentation
- Working examples
- Troubleshooting guide

---

## Testing Plan

### Test Cases

**Test 1: Valid Command - Alex Breakdown**
```
Input: "@alex *breakdown 'User Authentication'"
Expected: Executes breakdown-epic.md with input
Status: Should pass
```

**Test 2: Valid Command - James Implement**
```
Input: "@james *implement task-auth-002"
Expected: Executes implement-feature.md with task-auth-002
Status: Should pass
```

**Test 3: Valid Command - Quinn Review**
```
Input: "@quinn *review task-auth-002"
Expected: Executes review-task.md with task-auth-002
Status: Should pass
```

**Test 4: Invalid Syntax - Missing Asterisk**
```
Input: "@alex breakdown 'Epic'"
Expected: Error: Invalid syntax (missing *)
Status: Should fail gracefully
```

**Test 5: Unknown Subagent**
```
Input: "@bob *test"
Expected: Error: Unknown subagent @bob
Status: Should fail gracefully
```

**Test 6: Unknown Command**
```
Input: "@alex *invalid"
Expected: Error: Unknown command *invalid for @alex
Status: Should fail gracefully
```

**Test 7: Slash Command - Alex**
```
Input: "/alex breakdown 'Epic'"
Expected: Routes to router skill, executes breakdown-epic.md
Status: Should pass
```

**Test 8: Orchestrator Workflow**
```
Input: "@orchestrator *deliver 'User login'"
Expected: Executes complete delivery workflow
Status: Should pass
```

---

## Success Criteria

✅ **Functionality:**
- Router skill can parse all command formats
- All subagent commands route correctly
- All skills execute successfully
- Error handling works for invalid commands

✅ **Usability:**
- Slash commands work for all subagents
- Syntax is intuitive and documented
- Error messages are helpful
- Examples are clear

✅ **Performance:**
- Routing adds <1 second overhead
- Skill execution is same as direct invocation
- No noticeable delay

✅ **Reliability:**
- Handles edge cases gracefully
- No crashes on invalid input
- Clear error messages
- Degrades gracefully

---

## Future Enhancements

### Enhancement 1: Command Auto-Complete
Show available commands when user types `@alex *`

### Enhancement 2: Command Help
`@alex *help` shows all available commands with descriptions

### Enhancement 3: Command History
Track which commands were used, for analytics and improvement

### Enhancement 4: Command Aliases
Allow shorter aliases: `@alex *bd` → `*breakdown`

### Enhancement 5: Command Chaining
Allow multiple commands: `@alex *breakdown Epic && @james *implement story-001`

---

## Conclusion

**Recommendation:** Implement Hybrid Approach (Router Skill + Slash Commands)

**Timeline:**
- Phase 1 (Router): 2 hours
- Phase 2 (Slash Commands): 1 hour
- Phase 3 (Testing & Docs): 1 hour
- **Total: 4 hours**

**Impact:**
- Transforms verbose skill invocations into natural commands
- Makes system feel like team of AI assistants
- Enables complex orchestrated workflows
- Improves user experience dramatically

**Next Step:** Implement router skill (`.claude/skills/router.md`)

---

*Design by: BMAD Enhanced Team*
*Date: January 15, 2025*
*Status: Ready for Implementation*
