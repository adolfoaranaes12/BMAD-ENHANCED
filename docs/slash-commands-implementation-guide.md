# Slash Commands Implementation Guide for BMAD Enhanced

**Date:** October 29, 2025
**Purpose:** Complete guide for implementing slash commands (Layer 0)
**Status:** 📋 Planning Document (For Future Implementation)
**Based On:** Official Claude Code documentation at docs.claude.com/slash-commands

---

## Executive Summary

This document provides a complete implementation guide for adding **Slash Commands** (Layer 0) to BMAD Enhanced. Slash commands are manual shortcuts that complement our existing Skills and Subagents architecture.

**Why Add Slash Commands:**
- Quick manual operations without waiting for model invocation
- Complement skills with user-controlled shortcuts
- Leverage full Claude Code feature set
- Provide immediate access to common operations

**When to Implement:**
- After core skills are stable
- When team requests quick manual access to operations
- To provide shortcuts for frequent workflows

**Estimated Time:** 2-3 hours for initial implementation + 1 hour per additional command

---

## Table of Contents

1. [Understanding Slash Commands](#understanding-slash-commands)
2. [When to Use Slash Commands vs Skills](#when-to-use-slash-commands-vs-skills)
3. [BMAD-Specific Slash Commands](#bmad-specific-slash-commands)
4. [Implementation Steps](#implementation-steps)
5. [Command Templates](#command-templates)
6. [Integration with Existing Architecture](#integration-with-existing-architecture)
7. [Testing and Validation](#testing-and-validation)
8. [Best Practices](#best-practices)
9. [Maintenance](#maintenance)

---

## Understanding Slash Commands

### What Are Slash Commands?

**Official Definition:**
> "Slash commands are a core feature of Claude Code that allow you to control Claude's behavior during interactive sessions. They enable automation of frequently-used prompts and provide shortcuts to essential functionality."

### Key Characteristics

**Invocation:**
- User types `/command-name` in chat
- Immediate execution
- No model decision-making required

**Structure:**
- Markdown files with optional YAML frontmatter
- Stored in `.claude/commands/`
- Support arguments: `$1`, `$2`, `$ARGUMENTS`
- Can execute bash commands with `!` prefix

**Use Cases:**
- Quick file operations
- Common task shortcuts
- Frequent queries
- Status checks
- Quick reports

### Official Format

```markdown
# .claude/commands/command-name.md
---
description: Brief description of what this command does
argument-hint: <arg1> <arg2>
allowed-tools: Bash(python:*), Read, Grep
model: sonnet
disable-model-invocation: false
---

Command prompt content here.

Can include:
- File references: @file-path
- Bash execution: !bash command
- Arguments: $1, $2, $ARGUMENTS
```

---

## When to Use Slash Commands vs Skills

### Use Slash Commands For:

✅ **Quick manual operations**
- `/read-task task-001` - Immediate task read
- `/run-tests unit` - Quick test run
- `/status` - Project status check

✅ **Frequently-used shortcuts**
- Operations you invoke multiple times per day
- Simple, single-purpose actions
- Status checks and queries

✅ **User-controlled invocation**
- When you want explicit control
- When timing matters
- When you don't want model to decide

✅ **Simple, deterministic operations**
- No complex decision-making
- Clear input → output
- Predictable results

### Use Skills For:

✅ **Complex workflows**
- TDD implementation
- Story estimation
- Code review process

✅ **Model-invoked capabilities**
- Claude decides when to use
- Based on context and task
- Automatic selection

✅ **Multi-step operations**
- Requires decision-making
- Conditional logic
- Multiple outcomes

✅ **Reusable capabilities**
- Package and distribute
- Share across projects
- Team standardization

### Comparison Table

| Feature | Slash Commands | Skills |
|---------|----------------|--------|
| **Invocation** | Manual (`/command`) | Automatic (model-invoked) |
| **Location** | `.claude/commands/` | `.claude/skills/` |
| **Complexity** | Simple, single-purpose | Complex workflows |
| **Arguments** | `$1`, `$2`, `$ARGUMENTS` | YAML frontmatter inputs |
| **Packaging** | Not packageable | Packageable with `package_skill.py` |
| **Distribution** | Git only | .zip distribution |
| **Best For** | Quick shortcuts | Reusable capabilities |

### They Complement Each Other

**Example:**
- **Skill:** `implement-v2` - Full TDD implementation workflow (model-invoked)
- **Command:** `/implement task-001` - Quick shortcut to start implementation (manual)

The command can invoke the skill, providing quick manual access.

---

## BMAD-Specific Slash Commands

### Recommended Commands for BMAD Enhanced

#### Priority 1 (Essential)

**1. `/read-task <task-id>`**
- **Purpose:** Quickly read and summarize a task specification
- **Uses:** `bmad-commands` skill's `read_file.py`
- **Example:** `/read-task auth-002`

**2. `/run-tests [path]`**
- **Purpose:** Execute tests and show results
- **Uses:** `bmad-commands` skill's `run_tests.py`
- **Example:** `/run-tests src/auth/`

**3. `/implement <task-id>`**
- **Purpose:** Start implementation workflow for a task
- **Uses:** Invokes `implement-v2` skill
- **Example:** `/implement auth-002`

**4. `/status [scope]`**
- **Purpose:** Show current project status
- **Options:** `tasks`, `tests`, `all`
- **Example:** `/status tasks`

#### Priority 2 (Useful)

**5. `/estimate <story-id>`**
- **Purpose:** Quick story estimation
- **Uses:** Invokes `estimate-stories` skill
- **Example:** `/estimate story-042`

**6. `/review <task-id>`**
- **Purpose:** Start code review for a task
- **Uses:** Invokes `review-task` skill
- **Example:** `/review auth-002`

**7. `/task-info <task-id>`**
- **Purpose:** Show detailed task information
- **Example:** `/task-info auth-002`

**8. `/list-tasks [status]`**
- **Purpose:** List tasks by status
- **Options:** `open`, `in-progress`, `done`, `all`
- **Example:** `/list-tasks open`

#### Priority 3 (Nice to Have)

**9. `/create-task <title>`**
- **Purpose:** Create new task specification
- **Example:** `/create-task "Add OAuth support"`

**10. `/git-status`**
- **Purpose:** Show git status with BMAD context
- **Example:** `/git-status`

**11. `/coverage`**
- **Purpose:** Show test coverage report
- **Example:** `/coverage`

**12. `/quality-check`**
- **Purpose:** Run quality checks
- **Example:** `/quality-check`

---

## Implementation Steps

### Phase 1: Setup (15 minutes)

**Step 1: Create Commands Directory**

```bash
mkdir -p .claude/commands
```

**Step 2: Verify Structure**

```bash
ls -la .claude/
# Should see:
# - agents/
# - skills/
# - commands/  ← New!
```

---

### Phase 2: Implement Priority 1 Commands (2 hours)

#### Command 1: `/read-task`

**Create:** `.claude/commands/read-task.md`

```markdown
---
description: Read and summarize a task specification
argument-hint: <task-id>
allowed-tools: Bash(python:*)
---

# Read Task Specification

Reading task: task-$1

!python .claude/skills/bmad-commands/scripts/read_file.py \
  --path workspace/tasks/task-$1.md \
  --output json

Please provide a concise summary of:
1. **Objective:** What needs to be done
2. **Acceptance Criteria:** How we know it's complete
3. **Technical Approach:** Key technical considerations
4. **Complexity:** Estimated complexity (low/medium/high)
5. **Dependencies:** What this depends on
```

**Test:**
```bash
/read-task auth-002
```

**Expected Output:**
- Reads task-auth-002.md
- Shows JSON output from read_file.py
- Provides structured summary

---

#### Command 2: `/run-tests`

**Create:** `.claude/commands/run-tests.md`

```markdown
---
description: Execute tests and display results
argument-hint: [test-path] [framework]
allowed-tools: Bash(python:*)
---

# Run Tests

Executing tests for: ${1:-all}

!python .claude/skills/bmad-commands/scripts/run_tests.py \
  --path ${1:-.} \
  --framework ${2:-jest} \
  --output json

Please analyze the results and highlight:
1. **Pass Rate:** Tests passed/total
2. **Coverage:** Current test coverage percentage
3. **Failures:** Any failing tests with reasons
4. **Recommendations:** What needs attention
```

**Test:**
```bash
/run-tests src/auth
/run-tests
```

**Expected Output:**
- Runs tests in specified path
- Shows structured results
- Provides analysis

---

#### Command 3: `/implement`

**Create:** `.claude/commands/implement.md`

```markdown
---
description: Start implementation workflow for a task
argument-hint: <task-id>
allowed-tools: Task, Read, Bash(python:*)
---

# Implement Task

Starting implementation for task-$1...

First, let me read the task specification:

!python .claude/skills/bmad-commands/scripts/read_file.py \
  --path workspace/tasks/task-$1.md \
  --output json

Now invoking the implement-v2 skill to complete this task using TDD workflow.

The implement-v2 skill will:
1. Write failing tests (RED)
2. Implement code to pass tests (GREEN)
3. Refactor while keeping tests green (REFACTOR)
4. Verify acceptance criteria
5. Emit telemetry

Please use the .claude/skills/development/implement-v2/SKILL.md skill with task_id: task-$1
```

**Test:**
```bash
/implement auth-002
```

**Expected Output:**
- Reads task spec
- Invokes implement-v2 skill
- Completes full TDD workflow

---

#### Command 4: `/status`

**Create:** `.claude/commands/status.md`

```markdown
---
description: Show current project status
argument-hint: [tasks|tests|all]
allowed-tools: Bash, Read, Glob, Grep
---

# Project Status

Showing ${1:-all} status...

## Tasks Status

!find workspace/tasks -name "*.md" -type f | wc -l

Tasks found. Let me analyze them:

!grep -r "Status:" workspace/tasks --include="*.md" | head -20

## Test Status (if requested)

!python .claude/skills/bmad-commands/scripts/run_tests.py \
  --path . \
  --framework jest \
  --output json 2>/dev/null || echo "Tests not configured"

## Git Status

!git status --short

Please summarize:
1. **Tasks:** Total, by status
2. **Tests:** Pass rate, coverage
3. **Git:** Uncommitted changes
4. **Recommendations:** Next actions
```

**Test:**
```bash
/status
/status tasks
/status tests
```

**Expected Output:**
- Summary of tasks
- Test results
- Git status
- Actionable recommendations

---

### Phase 3: Implement Priority 2 Commands (1 hour)

#### Command 5: `/estimate`

**Create:** `.claude/commands/estimate.md`

```markdown
---
description: Quick story estimation
argument-hint: <story-id>
allowed-tools: Task
---

# Estimate Story

Estimating story: $1

Please use the .claude/skills/planning/estimate-stories/SKILL.md skill to estimate this story.

Story ID: $1
```

**Test:**
```bash
/estimate story-042
```

---

#### Command 6: `/review`

**Create:** `.claude/commands/review.md`

```markdown
---
description: Start code review for a task
argument-hint: <task-id>
allowed-tools: Task, Read, Bash(git:*)
---

# Code Review

Reviewing changes for task-$1...

!git diff --stat

Please use the review skill to analyze these changes for:
1. Code quality
2. Test coverage
3. Best practices
4. Security concerns
```

**Test:**
```bash
/review auth-002
```

---

### Phase 4: Testing & Documentation (30 minutes)

**Step 1: Test Each Command**

Create test checklist:
```markdown
## Command Testing Checklist

- [ ] `/read-task auth-002` - Works, shows task content
- [ ] `/run-tests` - Works, shows test results
- [ ] `/implement auth-002` - Invokes skill correctly
- [ ] `/status` - Shows comprehensive status
- [ ] `/estimate story-042` - Invokes estimation
- [ ] `/review auth-002` - Starts review process

**Date Tested:** [YYYY-MM-DD]
**Tested By:** [Name]
```

**Step 2: Document Commands**

Update project README or create `.claude/commands/README.md`:

```markdown
# BMAD Enhanced Slash Commands

## Available Commands

### Task Management
- `/read-task <task-id>` - Read task specification
- `/implement <task-id>` - Start implementation
- `/review <task-id>` - Start code review
- `/estimate <story-id>` - Estimate story points

### Development
- `/run-tests [path]` - Execute tests
- `/status [scope]` - Project status
- `/coverage` - Test coverage report

## Usage Examples

[Provide examples...]
```

**Step 3: Create Command Index**

Optional: Create `/commands` shortcut:

```markdown
# .claude/commands/commands.md
---
description: List all available custom commands
---

# Available BMAD Commands

Here are all custom slash commands available in this project:

## Task Management
- `/read-task <task-id>` - Read and summarize task specification
- `/implement <task-id>` - Start TDD implementation workflow
- `/review <task-id>` - Begin code review process
- `/estimate <story-id>` - Quick story point estimation

## Development & Testing
- `/run-tests [path]` - Execute tests in specified path
- `/status [scope]` - Show project status (tasks/tests/all)
- `/coverage` - Display test coverage report

## Usage

Type any command followed by required arguments:
```
/read-task auth-002
/implement auth-002
/run-tests src/auth
```

Use `/commands` to see this list anytime.
```

---

## Command Templates

### Basic Command Template

```markdown
# .claude/commands/command-name.md
---
description: Brief description (shown in /help)
argument-hint: <required> [optional]
allowed-tools: Bash, Read, Write
---

Command prompt content here.

Arguments available:
- $1 - First argument
- $2 - Second argument
- $ARGUMENTS - All arguments

Can include:
- File references: @file-path
- Bash execution: !command
- Plain instructions
```

### Command with Bash Execution

```markdown
---
description: Execute bash commands
allowed-tools: Bash(ls:*, cat:*)
---

!ls -la $1
!cat $1

Summary of findings...
```

### Command that Invokes Skill

```markdown
---
description: Invoke a skill
allowed-tools: Task
---

Please use the .claude/skills/category/skill-name/SKILL.md skill with:
- input_1: $1
- input_2: $2
```

### Command with Multiple Arguments

```markdown
---
description: Command with multiple args
argument-hint: <arg1> <arg2> [arg3]
---

First argument: $1
Second argument: $2
Third argument (optional): ${3:-default-value}
All arguments: $ARGUMENTS
```

---

## Integration with Existing Architecture

### How Commands Fit with Skills and Subagents

```
┌──────────────────────────────────────────┐
│ User Types: /implement auth-002          │
└──────────────────────────────────────────┘
                   ↓
┌──────────────────────────────────────────┐
│ Layer 0: SLASH COMMAND                   │
│ /implement command executes              │
│ - Reads task spec (uses bmad-commands) │
│ - Invokes implement-v2 skill             │
└──────────────────────────────────────────┘
                   ↓
┌──────────────────────────────────────────┐
│ Layer 2: WORKFLOW SKILL                  │
│ implement-v2 skill executes              │
│ - Uses bmad-commands for operations    │
│ - Follows TDD workflow                   │
│ - Returns results                        │
└──────────────────────────────────────────┘
                   ↓
┌──────────────────────────────────────────┐
│ Layer 1: PRIMITIVES                      │
│ bmad-commands scripts execute          │
│ - read_file.py                           │
│ - run_tests.py                           │
└──────────────────────────────────────────┘
```

### Commands vs Subagents

**When User Types `/implement auth-002`:**
- ✅ Direct, manual invocation
- ✅ Immediate execution
- ✅ User-controlled timing

**When User Asks "Implement auth-002":**
- ✅ James subagent evaluates
- ✅ Assesses complexity
- ✅ Routes to appropriate skill
- ✅ Applies guardrails

**Both are valid approaches for different scenarios.**

---

## Testing and Validation

### Test Plan

**For Each Command:**

1. **Syntax Test**
   ```bash
   /command-name
   # Should show argument hint if args missing
   ```

2. **Basic Execution**
   ```bash
   /command-name arg1
   # Should execute successfully
   ```

3. **Error Handling**
   ```bash
   /command-name invalid-arg
   # Should handle errors gracefully
   ```

4. **Integration Test**
   ```bash
   /command-name valid-arg
   # Verify it integrates with skills/primitives correctly
   ```

### Validation Checklist

```markdown
## Command Validation

**Command:** /command-name

- [ ] Syntax correct (YAML frontmatter valid)
- [ ] Description clear and concise
- [ ] Arguments work as expected
- [ ] Bash execution (if any) works
- [ ] Tool permissions correct
- [ ] Integrates with skills properly
- [ ] Error handling graceful
- [ ] Documentation complete
- [ ] Tested with real data
- [ ] Works in clean environment

**Status:** ✅ / ⚠️ / ❌
**Notes:** [Any observations]
```

---

## Best Practices

### Do's ✅

**1. Keep Commands Simple**
- Single purpose
- Clear, predictable behavior
- Quick execution

**2. Use Clear Names**
- Descriptive (`/read-task` not `/rt`)
- Consistent naming (`/run-tests` not `/test-run`)
- Verb-first (`/create-task` not `/task-create`)

**3. Provide Argument Hints**
```markdown
argument-hint: <required-arg> [optional-arg]
```

**4. Use Appropriate Tools**
```markdown
allowed-tools: Bash(python:*), Read
# Only what's needed
```

**5. Document Well**
```markdown
description: Clear, concise description of what command does
# This appears in /help
```

**6. Handle Arguments Safely**
```markdown
# With default values:
Path: ${1:-.}

# Check if provided:
${1:?Error: task-id required}
```

**7. Provide User Feedback**
```markdown
Starting implementation for task-$1...
# Clear what's happening
```

### Don'ts ❌

**1. Don't Make Commands Too Complex**
❌ Multi-step workflows with branching logic
✅ Use skills for complex workflows

**2. Don't Duplicate Skill Functionality**
❌ Reimplementing skill logic in command
✅ Invoke the skill from command

**3. Don't Skip Documentation**
❌ No description field
✅ Clear description always

**4. Don't Allow All Tools by Default**
❌ `allowed-tools: *`
✅ Only list needed tools

**5. Don't Hard-Code Paths**
❌ `/absolute/path/to/file`
✅ `workspace/tasks/$1.md`

**6. Don't Ignore Errors**
❌ Silent failures
✅ Clear error messages

---

## Maintenance

### Regular Tasks

**Monthly:**
- Review command usage
- Update documentation
- Check for broken commands
- Gather user feedback

**Quarterly:**
- Review all commands
- Remove unused commands
- Add requested commands
- Update best practices

### Version Control

**Commit Commands with Clear Messages:**
```bash
git add .claude/commands/read-task.md
git commit -m "feat: add /read-task command for quick task reading"
```

**Tag Versions:**
```bash
git tag -a commands-v1.0 -m "Initial slash commands implementation"
```

### Documentation Updates

**Keep README Current:**
- Add new commands
- Remove deprecated commands
- Update examples
- Document changes

**Changelog:**
```markdown
## Commands Changelog

### 2025-11-01
- Added `/read-task` command
- Added `/implement` command
- Added `/status` command

### 2025-11-15
- Updated `/status` to include git info
- Fixed `/run-tests` error handling
```

---

## Migration Path

### From No Commands to Commands

**Phase 1: Add 2-3 Essential Commands**
- Start small
- Get team familiar
- Gather feedback

**Phase 2: Add More Based on Usage**
- Monitor which operations are frequent
- Add commands for those operations
- Iterate based on feedback

**Phase 3: Standardize**
- Document all commands
- Create templates
- Train team

### From Commands to Skills (if needed)

**If a command becomes complex:**
1. Extract to skill
2. Keep command as simple invocation wrapper
3. Maintain backward compatibility

**Example:**
```markdown
# Simple command that grew complex → Extract to skill

# Before (complex command):
# .claude/commands/estimate.md with 200 lines of logic

# After (simple command + skill):
# .claude/commands/estimate.md (10 lines, invokes skill)
# .claude/skills/planning/estimate-stories/SKILL.md (full logic)
```

---

## Examples Gallery

### Example 1: Simple Bash Execution

```markdown
# .claude/commands/git-status.md
---
description: Show git status with BMAD context
allowed-tools: Bash(git:*)
---

!git status --short
!git branch --show-current

Current branch and changes shown above.
```

### Example 2: File Reading with Summary

```markdown
# .claude/commands/task-info.md
---
description: Show detailed task information
argument-hint: <task-id>
allowed-tools: Read
---

@workspace/tasks/task-$1.md

Please provide:
1. Task summary
2. Status
3. Acceptance criteria
4. Dependencies
```

### Example 3: Skill Invocation

```markdown
# .claude/commands/estimate.md
---
description: Estimate story points
argument-hint: <story-id>
allowed-tools: Task
---

Please use the estimate-stories skill to estimate story $1.
```

### Example 4: Multi-Step Command

```markdown
# .claude/commands/quick-review.md
---
description: Quick code review
argument-hint: <task-id>
allowed-tools: Bash(git:*), Read, Task
---

# Quick Review for task-$1

!git diff --stat

!git log --oneline -5

Please review these changes focusing on:
1. Code quality
2. Test coverage
3. Breaking changes
```

---

## Troubleshooting

### Common Issues

**Issue 1: Command Not Found**
```
Symptom: /command-name not recognized
Solution: Check file exists in .claude/commands/
         Check filename matches command name
```

**Issue 2: Arguments Not Working**
```
Symptom: $1 shows literal "$1"
Solution: Verify frontmatter has argument-hint
         Check you're using correct syntax
```

**Issue 3: Bash Commands Fail**
```
Symptom: !command doesn't execute
Solution: Check allowed-tools includes Bash
         Check bash command is valid
         Check permissions
```

**Issue 4: Can't Access Files**
```
Symptom: @file-path doesn't work
Solution: Check allowed-tools includes Read
         Check file path is correct
         Check file exists
```

---

## Summary

### When to Implement

✅ **Implement when:**
- Team requests quick manual access
- Common operations need shortcuts
- Skills are stable and working
- Want to leverage full Claude Code features

⏸️ **Wait if:**
- Skills are still in development
- Team hasn't requested it
- Unclear which operations need shortcuts

### Effort Required

**Initial Setup:** 2-3 hours
- Create directory
- Implement 4-5 essential commands
- Document and test

**Additional Commands:** 30-60 minutes each
- Design command
- Implement
- Test
- Document

**Maintenance:** 1-2 hours per month
- Review usage
- Update as needed
- Add requested commands

### Benefits

✅ **Quick access** to common operations
✅ **Complements** skills nicely
✅ **User control** over timing
✅ **Full feature usage** of Claude Code
✅ **Team productivity** boost

---

## Next Steps

When ready to implement:

1. **Review this guide** thoroughly
2. **Identify 3-5 essential commands** for your team
3. **Follow Phase 1-2** of implementation steps
4. **Test thoroughly** with real usage
5. **Gather feedback** and iterate
6. **Expand gradually** based on usage patterns

**Good luck implementing slash commands! 🚀**

---

*Implementation guide for BMAD Enhanced slash commands*
*Based on official Claude Code documentation (docs.claude.com/slash-commands)*
