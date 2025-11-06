# How to Use BMAD Enhanced Agents Correctly

**Essential guide to ensure skills load properly**

Version: 2.0
Last Updated: 2025-11-05

---

## CRITICAL: The Command Syntax

### Always Use This Pattern

```bash
/agent *task [parameters]
```

**Components:**
- `/` - Slash prefix (routes to agent)
- `agent` - Agent name (alex, james, quinn, etc.)
- `*` - Asterisk prefix (CRITICAL - triggers skill routing)
- `task` - Skill command (implement, review, etc.)
- `[parameters]` - Optional parameters

---

## Why the `*` Prefix is CRITICAL

### With `*` Prefix (Correct ✅)

```bash
/james *implement task-001
```

**What Happens:**
1. ✅ Slash command routes to james-developer-v2 agent
2. ✅ Agent sees `*implement` command
3. ✅ **Routing logic ACTIVATES**
4. ✅ Agent calculates complexity
5. ✅ Agent determines which skill to use
6. ✅ **Agent loads skill file:**
   ```
   Read: .claude/skills/development/implement-v2/SKILL.md
   ```
7. ✅ Agent follows skill's TDD workflow
8. ✅ TodoWrite tracks progress
9. ✅ Guardrails enforced
10. ✅ Acceptance criteria verified

**Result:** Full workflow with quality gates ✅

---

### Without `*` Prefix (Wrong ❌)

```bash
# Example 1: Free-form instruction
"Execute the implementation tasks outlined in..."

# Example 2: Missing * prefix
/james implement task-001

# Example 3: Natural language
"James, can you implement task-001?"
```

**What Happens:**
1. ✅ Agent receives prompt
2. ❌ **Routing logic NEVER ACTIVATES** (no `*` prefix detected)
3. ❌ Agent works directly without loading skill
4. ❌ No TDD workflow
5. ❌ No TodoWrite tracking
6. ❌ No guardrails
7. ❌ No acceptance criteria verification
8. ❌ Agent uses Read, Write, Edit tools directly

**Result:** Agent bypasses skill entirely ❌

---

## Correct Examples for All Agents

### Alex (Planner)

```bash
# Create task specification
/alex *create-task-spec "User login with OAuth"

# Break down epic
/alex *breakdown-epic "User Authentication System"

# Estimate story
/alex *estimate story-auth-001

# Refine vague requirements
/alex *refine-story "Users need better security"

# Plan sprint
/alex *plan-sprint "Sprint 15" --velocity 40
```

---

### James (Developer)

```bash
# Implement feature with TDD
/james *implement task-auth-002

# Fix bug
/james *fix bug-login-timeout

# Run tests
/james *test task-auth-002

# Refactor code
/james *refactor task-auth-002

# Apply QA fixes
/james *apply-qa-fixes task-auth-002

# Debug issue
/james *debug "Login tests failing intermittently"

# Explain code
/james *explain src/auth/login.ts
```

---

### Quinn (Quality)

```bash
# Comprehensive review
/quinn *review task-auth-002

# Assess NFRs
/quinn *assess-nfr task-auth-002

# Quality gate decision
/quinn *validate-quality-gate task-auth-002

# Requirements traceability
/quinn *trace-requirements task-auth-002

# Risk assessment
/quinn *assess-risk task-auth-002
```

---

### Winston (Architect)

```bash
# Analyze existing codebase
/winston *analyze-architecture .

# Design system architecture
/winston *create-architecture requirements.md

# Review architecture quality
/winston *review-architecture docs/architecture.md

# Compare architecture options
/winston *compare-architectures "Scale to 50K users + real-time"

# Create ADR
/winston *create-adr "Use Redis for session storage"
/winston *create-adr "packages/backend/src/schema.prisma"

# Validate architectural patterns
/winston *validate-patterns .
/winston *validate-patterns packages/backend

# Interactive consultation (special case - no * needed)
/winston-consult "How do I add real-time features?"
```

---

### Orchestrator

```bash
# Complete feature delivery
/orchestrator *workflow feature-delivery "User authentication"

# Epic to sprint planning
/orchestrator *workflow epic-to-sprint "Shopping Cart" --velocity 40

# Sprint execution
/orchestrator *workflow sprint-execution "Sprint 15"

# Brownfield modernization
/orchestrator *workflow modernize . "Scale to 100K users"

# Cross-subagent coordination
/orchestrator *coordinate "Quality improvement" --subagents quinn,james

# Resume workflow
/orchestrator *resume workflow-abc-123

# Check workflow status
/orchestrator *status workflow-abc-123
```

---

### John (Product Manager)

```bash
# Create greenfield PRD
/john *create-prd "E-commerce platform for artisans"

# Create brownfield PRD
/john *create-brownfield-prd "src/"

# Shard large PRD
/john *shard-prd "docs/prd-large.md"

# Create brownfield epic
/john *create-brownfield-epic "Payment Processing" --codebase "src/"

# Create brownfield story
/john *create-brownfield-story "Stripe integration" --epic "epic-payment-001"
```

---

### Mary (Business Analyst)

```bash
# Brainstorm ideas
/mary *brainstorm "Mobile app monetization strategies"

# Competitive analysis
/mary *create-competitor-analysis "Project management tools"

# Create project brief
/mary *create-project-brief "Customer Portal Redesign"

# Market research
/mary *perform-market-research "AI-powered chatbots"

# Research prompt
/mary *research-prompt "Enterprise SaaS pricing models"

# Requirements elicitation
/mary *elicit "Users want better notifications"
```

---

### Sarah (Product Owner)

```bash
# Create epic
/sarah *create-epic "User Authentication System" --source "prd.md"

# Create story
/sarah *create-story "OAuth login integration"

# Validate story draft
/sarah *validate-story-draft "stories/story-auth-001.md"

# Shard large document
/sarah *shard-doc "docs/requirements-mega.md"

# Execute PO checklist
/sarah *execute-checklist-po "sprint-planning"
```

---

### Bob (Scrum Master)

```bash
# Create developer-ready story
/bob *create-dev-story "Add logout button with confirmation"

# Prepare handoff
/bob *prepare-handoff "stories/story-ui-042.md"
```

---

### Sally (UX Expert)

```bash
# Create frontend specification
/sally *create-front-end-spec "User profile page with avatar upload"

# Generate UI prompt for AI tools
/sally *generate-ui-prompt "Shopping cart checkout flow" --tool v0
/sally *generate-ui-prompt "Dashboard with charts" --tool lovable
/sally *generate-ui-prompt "Login page" --tool artifacts
```

---

## Common Mistakes

### Mistake 1: Missing Slash

```bash
# ❌ WRONG
james *implement task-001
alex *create-task-spec "Feature"

# ✅ CORRECT
/james *implement task-001
/alex *create-task-spec "Feature"
```

---

### Mistake 2: Missing Asterisk

```bash
# ❌ WRONG
/james implement task-001
/alex create-task-spec "Feature"

# ✅ CORRECT
/james *implement task-001
/alex *create-task-spec "Feature"
```

---

### Mistake 3: Free-Form Instructions

```bash
# ❌ WRONG
"James, can you implement the login feature?"
"Execute the implementation tasks in the document"
"Please create a task spec for user authentication"

# ✅ CORRECT
/james *implement task-login-001
/alex *create-task-spec "User authentication with OAuth"
```

---

### Mistake 4: Using @ Instead of /

```bash
# ❌ WRONG
@james *implement task-001
@alex *create-task-spec "Feature"

# ✅ CORRECT
/james *implement task-001
/alex *create-task-spec "Feature"
```

---

## How to Verify Skills Are Loading

### Check the Logs

When skills load correctly, you should see output like:

```
james-developer-v2(*implement task-001)
  ⎿  Prompt: Execute planning command: *implement task-001

  > Loading task specification...
  Read(.claude/tasks/task-001.md)

  > Calculating complexity...
  Complexity score: 35 (Medium)

  > Routing to skill...
  Skill selected: implement-v2
  Reason: "Medium complexity with standard TDD workflow"

  > Loading skill...
  Read(.claude/skills/development/implement-v2/SKILL.md)

  > Executing TDD workflow...
  TodoWrite - Added 7 tasks to todo list

  > RED: Writing tests first...
  Write(tests/auth/login.test.ts)

  > GREEN: Implementing feature...
  Write(src/auth/login.ts)

  > REFACTOR: Improving code quality...
  Edit(src/auth/login.ts)

  > Running tests...
  Bash(npm test)

  ✓ All tests passing (87% coverage)
  ✓ Acceptance criteria verified
  ✓ Implementation complete
```

**Key Indicators:**
- ✅ Command shows `*implement` (with asterisk)
- ✅ "Loading skill..." message
- ✅ `Read(.claude/skills/...SKILL.md)`
- ✅ TodoWrite tracking
- ✅ Structured workflow (RED → GREEN → REFACTOR)

---

### What Wrong Usage Looks Like

```
james-developer-v2(Implement the login feature)
  ⎿  Prompt: Implement the login feature

  Read(src/auth/login.ts)
  Write(src/auth/login.ts)
  Write(tests/auth/login.test.ts)
  Bash(npm test)

  Tests passing ✓
```

**Warning Signs:**
- ❌ No `*` prefix in command name
- ❌ No "Loading skill..." message
- ❌ No `Read(.claude/skills/...SKILL.md)`
- ❌ No TodoWrite tracking
- ❌ Direct tool usage without workflow structure

---

## Troubleshooting

### Problem: "Agent didn't load skill"

**Symptoms:**
- Agent works directly with Read, Write, Edit
- No TodoWrite tracking
- No "Loading skill..." message

**Solution:**
Check your command syntax:
```bash
# Did you use this? ❌
"Implement task-001"
/james implement task-001

# Use this instead: ✅
/james *implement task-001
```

---

### Problem: "Slash command not recognized"

**Symptoms:**
- `/james` command not found
- Agent doesn't respond

**Solution:**
1. Verify `.claude/commands/james.md` exists
2. Check file permissions
3. Restart Claude Code

---

### Problem: "Skill file not found"

**Symptoms:**
- Agent tries to load skill but fails
- Error: "File does not exist"

**Solution:**
1. Verify skill exists:
   ```bash
   ls .claude/skills/development/implement-v2/SKILL.md
   ```
2. Copy skill if missing:
   ```bash
   cp -r /path/to/bmad-enhanced/.claude/skills .claude/
   ```

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────┐
│              BMAD ENHANCED COMMAND SYNTAX                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  CORRECT FORMAT:                                            │
│  /agent *task [parameters]                                  │
│                                                             │
│  EXAMPLE:                                                   │
│  /james *implement task-auth-002                            │
│                                                             │
│  BREAKDOWN:                                                 │
│  / ────────── Slash prefix (routes to agent)                │
│  james ────── Agent name                                    │
│  * ────────── Asterisk (CRITICAL - triggers routing)        │
│  implement ── Skill command                                 │
│  task-auth-002 ─ Parameter                                  │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  WITHOUT * PREFIX → Skills DON'T load!                      │
└─────────────────────────────────────────────────────────────┘
```

---

## Summary

✅ **Always use:** `/agent *task [parameters]`
✅ **The `*` prefix is CRITICAL** - it triggers skill routing
✅ **Without `*`:** Agent bypasses skills and works directly
✅ **With `*`:** Full workflow with TDD, guardrails, tracking

**Key Takeaway:** If you don't see skill loading in logs, check your command syntax!

---

**See Also:**
- [CRITICAL-SKILL-LOADING-ISSUE.md](./CRITICAL-SKILL-LOADING-ISSUE.md) - Detailed problem analysis
- [QUICK-START.md](./QUICK-START.md) - Command flow explained
- [COMMAND-REFERENCE-SUMMARY.md](./COMMAND-REFERENCE-SUMMARY.md) - All 50+ commands
- [INSTALLATION-GUIDE.md](./INSTALLATION-GUIDE.md) - How skills load

---

**Version:** 2.0
**Status:** Essential Reading
**Updated:** 2025-11-05
