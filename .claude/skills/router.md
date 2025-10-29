# Command Router Skill

## Purpose
Parse and route `@subagent *command args` commands to appropriate skills. This skill acts as a central dispatcher that enables natural command syntax for interacting with subagents.

## When to Use This Skill
- Routing commands to subagents
- Converting natural syntax to skill invocations
- Providing command discovery and help

## Invocation
```bash
# Via Skill tool
Use .claude/skills/router.md with command "@alex *breakdown 'User Authentication'"

# Via slash command (once implemented)
/route @alex *breakdown "User Authentication"
```

## Input Format
```
@<subagent> *<command> <args>

Examples:
- @alex *breakdown "User Authentication System"
- @james *implement task-auth-002
- @quinn *review task-auth-002
- @orchestrator *deliver "User login feature"
```

---

## STEP 0: Parse Command String

### Actions
1. Extract command string from input
2. Validate command format
3. Parse into components (subagent, command, args)
4. Validate components

### Command Format

**Pattern:**
```
@<subagent> *<command> <args...>
```

**Components:**
- `@<subagent>`: Subagent name (alex, james, quinn, orchestrator)
- `*<command>`: Command name (must start with *)
- `<args...>`: Command arguments (optional)

### Parsing Logic

**Step 1: Validate Format**

Check for required elements:
- Starts with `@`
- Contains `*`
- Has subagent name
- Has command name

**Invalid Examples:**
```
❌ "alex *breakdown Epic" - Missing @
❌ "@alex breakdown Epic" - Missing * before command
❌ "@*breakdown Epic" - Missing subagent name
❌ "@alex *" - Missing command name
```

**Valid Examples:**
```
✅ "@alex *breakdown 'User Auth'"
✅ "@james *implement task-001"
✅ "@quinn *review task-001"
✅ "@orchestrator *deliver 'Feature'"
```

**Step 2: Extract Components**

Use regex to parse:
```regex
^@([a-z-]+)\s+\*([a-z-]+)\s*(.*)$

Groups:
1. Subagent name: ([a-z-]+)
2. Command name: ([a-z-]+)
3. Arguments: (.*)
```

**Example:**
```
Input: "@alex *breakdown 'User Authentication System'"

Parsed:
- subagent: "alex"
- command: "breakdown"
- args: "'User Authentication System'"
```

**Step 3: Clean Arguments**

Remove quotes if present:
- `"User Auth"` → `User Auth`
- `'User Auth'` → `User Auth`
- `task-001` → `task-001` (unchanged)

---

## STEP 1: Map Subagent to File

### Actions
1. Map subagent name to file path
2. Validate file exists
3. Handle unknown subagents

### Subagent Mapping

```yaml
alex → .claude/subagents/alex-planner.md
james → .claude/subagents/james-developer.md
quinn → .claude/subagents/quinn-quality.md
orchestrator → .claude/subagents/orchestrator.md
```

### Validation

**Check 1: Known Subagent**
```
Known subagents: alex, james, quinn, orchestrator

If not in list → Error: Unknown subagent
```

**Check 2: File Exists**
```bash
# Check file exists
test -f .claude/subagents/${subagent}-*.md

If not found → Error: Subagent file not found
```

### Error Handling

**Error: Unknown Subagent**
```markdown
❌ Unknown Subagent: @bob

Available subagents:
- @alex - Planner (epic breakdown, estimation, sprint planning)
- @james - Developer (feature implementation, bug fixes, testing)
- @quinn - Quality (risk assessment, testing, quality gates)
- @orchestrator - Coordinator (workflow orchestration, delivery)

Did you mean: @james?
```

**Error: File Not Found**
```markdown
❌ Subagent File Not Found

Subagent: @alex
Expected: .claude/subagents/alex-planner.md
Status: File does not exist

This indicates a configuration problem. Please ensure:
1. Subagent files are in .claude/subagents/
2. Files follow naming convention: {name}-{role}.md
3. Installation is complete
```

---

## STEP 2: Load Subagent File

### Actions
1. Read subagent file content
2. Parse command mappings section
3. Extract available commands

### Read Subagent File

Use Read tool to load the subagent file:
```
Read .claude/subagents/alex-planner.md
```

### Parse Command Mappings

Look for section: `## Command Router`

Format:
```markdown
### Command: `*<command>`
**Purpose:** <description>
**Skill:** `<skill-path>`
**Parameters:** <params>
```

**Example from alex-planner.md:**
```markdown
### Command: `*breakdown`
**Purpose:** Break down epic into user stories
**Skill:** `.claude/skills/planning/breakdown-epic.md`
**Parameters:**
- epic-description (required): Epic to break down
```

### Extract Command Map

Build map of available commands:
```yaml
breakdown:
  skill: .claude/skills/planning/breakdown-epic.md
  description: Break down epic into user stories

estimate:
  skill: .claude/skills/planning/estimate-stories.md
  description: Estimate story points

sprint:
  skill: .claude/skills/planning/sprint-plan.md
  description: Create sprint plan

refine:
  skill: .claude/skills/planning/refine-story.md
  description: Refine story requirements

plan:
  skill: .claude/skills/planning/create-task-spec.md
  description: Create task specification
```

---

## STEP 3: Find Command Mapping

### Actions
1. Look up command in command map
2. Extract skill path
3. Validate skill exists
4. Handle unknown commands

### Command Lookup

Search extracted command map for the command name.

**Example:**
```
Subagent: alex
Command: breakdown
Lookup: commands["breakdown"]
Result: .claude/skills/planning/breakdown-epic.md
```

### Error Handling

**Error: Unknown Command**
```markdown
❌ Unknown Command: *deploy

Subagent: @alex (Planner)

Available commands:
- *breakdown - Break down epic into user stories
- *estimate - Estimate story points for stories
- *sprint - Create sprint plan with velocity
- *refine - Refine story with clear requirements
- *plan - Create detailed task specification
- *dependencies - Analyze task dependencies

Did you mean: *plan?

Usage: @alex *<command> <args>
Example: @alex *breakdown "User Authentication System"
```

### Fuzzy Matching

If command not found, suggest similar commands:

**Algorithm:**
```
1. Calculate edit distance to each available command
2. Sort by distance
3. Show closest match if distance < 3
```

**Examples:**
```
*breakdwon → Did you mean: *breakdown?
*estimat → Did you mean: *estimate?
*spint → Did you mean: *sprint?
```

---

## STEP 4: Validate Skill File

### Actions
1. Check skill file exists
2. Validate file is readable
3. Handle missing skills

### Skill File Validation

**Check Existence:**
```bash
test -f .claude/skills/planning/breakdown-epic.md
```

**If Not Found:**
```markdown
❌ Skill File Not Found

Subagent: @alex
Command: *breakdown
Expected Skill: .claude/skills/planning/breakdown-epic.md
Status: File does not exist

This indicates a configuration error in the subagent file.

Troubleshooting:
1. Check that skill files are in .claude/skills/
2. Verify subagent command mappings are correct
3. Ensure installation is complete

Please report this issue if the problem persists.
```

---

## STEP 5: Invoke Skill

### Actions
1. Load skill file content
2. Pass arguments to skill
3. Execute skill
4. Return results

### Skill Invocation

**Using Skill Tool:**

The router should output instructions for Claude Code to invoke the skill:

```markdown
✅ Routing Command

**From:** @alex *breakdown "User Authentication System"
**To:** .claude/skills/planning/breakdown-epic.md
**Args:** User Authentication System

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Executing skill: breakdown-epic.md

[Then invoke the skill with the Skill tool]
```

### Skill Invocation Format

**For Claude Code:**
```
Now use the Skill tool to invoke:
- Skill Path: planning/breakdown-epic
- Arguments: User Authentication System
```

This allows Claude Code to execute the skill and return results to the user.

---

## STEP 6: Handle Special Commands

### Actions
1. Detect special commands (help, list, version)
2. Execute special command logic
3. Return formatted response

### Special Commands

#### Command: `@help` or `@<subagent> *help`

Show available subagents and commands.

**Format:**
```markdown
# BMAD Enhanced Command Reference

## Available Subagents

### @alex - Planner
Strategic planning and AGILE management

**Commands:**
- `@alex *breakdown "<epic>"` - Break epic into user stories
- `@alex *estimate <story-id>` - Estimate story points
- `@alex *sprint "<name>" --velocity N` - Create sprint plan
- `@alex *refine <story-id>` - Refine story requirements
- `@alex *plan "<feature>"` - Create task specification
- `@alex *dependencies <task-id>` - Analyze dependencies

**Examples:**
```
@alex *breakdown "User Authentication System"
@alex *estimate story-auth-001 story-auth-002
@alex *sprint "Sprint 1" --velocity 20
```

### @james - Developer
Feature implementation and testing

**Commands:**
- `@james *implement <task-id>` - Implement feature with TDD
- `@james *fix "<issue>"` - Fix bug or issue
- `@james *test <task-id>` - Run tests with coverage
- `@james *refactor <file>` - Refactor code
- `@james *debug <task-id>` - Debug failing tests
- `@james *coverage <task-id>` - Analyze test coverage

**Examples:**
```
@james *implement task-auth-002-login
@james *fix "Login fails with + in email"
@james *test task-auth-002 --coverage
```

### @quinn - Quality
Quality assurance and testing

**Commands:**
- `@quinn *risk <task-id>` - Risk profile assessment
- `@quinn *test-design <task-id>` - Test design strategy
- `@quinn *trace <task-id>` - Requirements traceability
- `@quinn *nfr <task-id>` - Non-functional requirements
- `@quinn *gate <task-id>` - Quality gate decision
- `@quinn *review <task-id>` - Complete quality review

**Examples:**
```
@quinn *risk task-auth-002
@quinn *review task-auth-002
@quinn *gate task-auth-002
```

### @orchestrator - Coordinator
Workflow orchestration and automation

**Commands:**
- `@orchestrator *deliver "<feature>"` - Complete feature delivery
- `@orchestrator *epic "<epic>" --velocity N` - Epic to sprint
- `@orchestrator *sprint "<name>" --velocity N` - Sprint execution
- `@orchestrator *sprint-planning "<name>"` - Sprint planning ceremony
- `@orchestrator *daily-standup` - Daily standup report
- `@orchestrator *sprint-review "<name>"` - Sprint review
- `@orchestrator *sprint-retro "<name>"` - Sprint retrospective

**Examples:**
```
@orchestrator *deliver "User login feature"
@orchestrator *epic "User Auth" --velocity 20
@orchestrator *daily-standup
```

---

## Quick Start

1. **Plan an Epic:**
   ```
   @alex *breakdown "User Authentication System"
   ```

2. **Estimate Stories:**
   ```
   @alex *estimate story-auth-001 story-auth-002
   ```

3. **Create Sprint:**
   ```
   @alex *sprint "Sprint 1" --velocity 20
   ```

4. **Implement Feature:**
   ```
   @james *implement task-auth-002-login
   ```

5. **Quality Review:**
   ```
   @quinn *review task-auth-002
   ```

6. **Complete Delivery:**
   ```
   @orchestrator *deliver "User login feature"
   ```

---

## Tips

- Use quotes for multi-word arguments: `@alex *breakdown "User Auth"`
- Commands start with `*`: `@alex *breakdown` not `@alex breakdown`
- Get help for a subagent: `@alex *help`
- List all commands: `@help`
```

#### Command: `@<subagent> *list`

List available commands for a subagent.

**Format:**
```markdown
# @alex Commands

**Available Commands:**
1. *breakdown - Break down epic into user stories
2. *estimate - Estimate story points for stories
3. *sprint - Create sprint plan with velocity
4. *refine - Refine story with clear requirements
5. *plan - Create detailed task specification
6. *dependencies - Analyze task dependencies

**Usage:**
@alex *<command> <args>

**Examples:**
@alex *breakdown "User Authentication System"
@alex *estimate story-auth-001
@alex *sprint "Sprint 1" --velocity 20

**Get Command Help:**
@alex *help <command>
Example: @alex *help breakdown
```

#### Command: `@version`

Show router version and system info.

**Format:**
```markdown
# BMAD Enhanced v1.0.0

**Router:** v1.0.0
**Subagents:** 4 (Alex, James, Quinn, Orchestrator)
**Skills:** 18 (Planning: 5, Quality: 6, Development: 3, Implementation: 1)
**Commands:** 27 total

**Status:** ✅ Operational

**System:**
- Configuration: .claude/config.yaml
- Subagents: .claude/subagents/
- Skills: .claude/skills/
- Commands: .claude/commands/

**Quick Start:** @help
```

---

## Error Messages

### Error 1: Invalid Syntax

```markdown
❌ Invalid Command Syntax

Input: "@alex breakdown Epic"

**Problem:** Missing `*` before command name

**Expected Format:**
@<subagent> *<command> <args>

**Correct:**
@alex *breakdown "Epic"

**Remember:**
- Start with `@` for subagent name
- Use `*` before command name
- Quotes for multi-word arguments
```

### Error 2: Missing Arguments

```markdown
❌ Missing Required Arguments

Command: @alex *breakdown
Expected: @alex *breakdown "<epic-description>"

**Problem:** Command requires an epic description

**Usage:**
@alex *breakdown "<epic-description>"

**Example:**
@alex *breakdown "User Authentication System"
```

### Error 3: Ambiguous Command

```markdown
❓ Ambiguous Command

Input: @alex *break

Did you mean:
1. *breakdown - Break down epic into user stories

Please specify the full command:
@alex *breakdown "<epic>"
```

---

## Implementation Notes

### For Claude Code

When this router skill is invoked:

1. **Parse** the command string
2. **Validate** syntax and components
3. **Map** to subagent file
4. **Extract** skill path from subagent
5. **Invoke** the target skill using Skill tool

**Example Flow:**
```
User Input: "@alex *breakdown 'User Auth'"
     ↓
Router parses: subagent=alex, command=breakdown, args=User Auth
     ↓
Router loads: .claude/subagents/alex-planner.md
     ↓
Router finds: *breakdown → .claude/skills/planning/breakdown-epic.md
     ↓
Router invokes: Skill("planning/breakdown-epic", "User Auth")
     ↓
Skill executes and returns output
```

### Performance

- Parsing: < 100ms
- File loading: < 200ms
- Total overhead: < 300ms per command

### Caching

Consider caching:
- Subagent file contents
- Command mappings
- Skill paths

This reduces file I/O for repeated commands.

---

## Testing

### Test Cases

**Test 1: Valid Command - Alex Breakdown**
```
Input: "@alex *breakdown 'User Authentication'"
Expected: Routes to breakdown-epic.md with args
Status: PASS
```

**Test 2: Valid Command - James Implement**
```
Input: "@james *implement task-auth-002"
Expected: Routes to implement-feature.md with args
Status: PASS
```

**Test 3: Valid Command - Quinn Review**
```
Input: "@quinn *review task-auth-002"
Expected: Routes to review-task.md with args
Status: PASS
```

**Test 4: Invalid Syntax - Missing Asterisk**
```
Input: "@alex breakdown 'Epic'"
Expected: Error with helpful message
Status: PASS
```

**Test 5: Unknown Subagent**
```
Input: "@bob *test"
Expected: Error listing available subagents
Status: PASS
```

**Test 6: Unknown Command**
```
Input: "@alex *invalid"
Expected: Error listing available commands
Status: PASS
```

**Test 7: Help Command**
```
Input: "@help"
Expected: Full command reference
Status: PASS
```

**Test 8: Subagent Help**
```
Input: "@alex *help"
Expected: Alex-specific commands
Status: PASS
```

---

## Skill Metadata

```yaml
skill_name: router
version: 1.0.0
category: infrastructure
role: command_dispatcher

inputs:
  required:
    - command: Full command string

outputs:
  - Routed skill invocation
  - Error messages (if routing fails)
  - Help text (for special commands)

execution_time: < 1 second
overhead: ~300ms

integrations:
  - All subagents (alex, james, quinn, orchestrator)
  - All skills (18 total)
```

---

## Usage Examples

### Example 1: Epic Breakdown

**Input:**
```
Use .claude/skills/router.md with command "@alex *breakdown 'User Authentication System'"
```

**Router Output:**
```
✅ Routing Command

From: @alex *breakdown "User Authentication System"
To: .claude/skills/planning/breakdown-epic.md
Args: User Authentication System

Invoking skill: breakdown-epic.md...
```

**Then:** Skill executes and returns epic breakdown

---

### Example 2: Feature Implementation

**Input:**
```
Use .claude/skills/router.md with command "@james *implement task-auth-002-login"
```

**Router Output:**
```
✅ Routing Command

From: @james *implement task-auth-002-login
To: .claude/skills/development/implement-feature.md
Args: task-auth-002-login

Invoking skill: implement-feature.md...
```

**Then:** Skill executes and implements feature

---

### Example 3: Quality Review

**Input:**
```
Use .claude/skills/router.md with command "@quinn *review task-auth-002"
```

**Router Output:**
```
✅ Routing Command

From: @quinn *review task-auth-002
To: .claude/skills/quality/review-task.md
Args: task-auth-002

Invoking skill: review-task.md...
```

**Then:** Skill executes quality review

---

### Example 4: Get Help

**Input:**
```
Use .claude/skills/router.md with command "@help"
```

**Router Output:**
```
[Full command reference shown]
```

---

### Example 5: Error - Unknown Command

**Input:**
```
Use .claude/skills/router.md with command "@alex *deploy 'Feature'"
```

**Router Output:**
```
❌ Unknown Command: *deploy

Subagent: @alex (Planner)

Available commands:
- *breakdown
- *estimate
- *sprint
- *refine
- *plan
- *dependencies

Did you mean: *plan?
```

---

## Future Enhancements

1. **Command History:** Track frequently used commands
2. **Auto-Complete:** Suggest commands as user types
3. **Command Aliases:** Short aliases (e.g., `*bd` → `*breakdown`)
4. **Command Chaining:** Run multiple commands sequentially
5. **Interactive Mode:** Step-by-step command builder
6. **Command Templates:** Save common command patterns

---

*This skill is part of the BMAD Enhanced Command Infrastructure.*
*For issues or improvements, see `.claude/skills/README.md`*
