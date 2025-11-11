# Choosing Your Approach: Direct Skills vs Subagents

**Quick Reference Guide for BMAD Enhanced**

---

## The Two Approaches

BMAD Enhanced offers two ways to work:

### 1. Direct Skills (`/slash-commands`)

Run skills directly - fast and structured

### 2. Subagents (`@agent-name`)

Talk to agents - conversational and helpful

---

## Quick Decision Guide

```
┌─────────────────────────────────────────────┐
│ Do you know EXACTLY what needs to be done? │
└──────────────┬──────────────────────────────┘
               │
        ┌──────┴──────┐
        │             │
       YES           NO
        │             │
        ▼             ▼
    /commands     @subagents
  (Direct Skills) (Conversational)
        │             │
        ▼             ▼
    Fast & Clear  Guidance & Help
```

---

## When to Use Direct Skills

**Use `/command-name` when:**
- ✅ You know exactly what you need
- ✅ You want fast, structured results
- ✅ You're doing repetitive workflows
- ✅ You need deterministic output

**Examples:**
```bash
/create-task-spec "User authentication"
/implement-feature task-001
/run-tests --coverage
/quality-gate task-001
```

---

## When to Use Subagents

**Use `@agent-name` when:**
- 💬 You need advice or guidance
- 🔍 You're not sure what to do
- 🐛 You're debugging unknown issues
- 🤝 You want to explore options
- 📚 You want explanations

**Examples:**
```bash
@alex "I need to add login, but not sure how to plan it"
@james "Help me debug this 500 error"
@winston "Should I use microservices or monolith?"
@quinn "Is this code production-ready?"
```

---

## Side-by-Side Comparison

| Aspect | Direct Skills | Subagents |
|--------|---------------|-----------|
| **Speed** | ⚡ Faster | 🐢 Slightly slower |
| **Output** | 📋 Structured | 💬 Conversational |
| **Use When** | You know what to do | You need help |
| **Best For** | Clear tasks | Exploration |
| **Syntax** | `/command args` | `@agent "question"` |
| **Reliability** | 🎯 100% deterministic | 🎨 Flexible |

---

## Real-World Decision Making

### Scenario 1: Implement Login Feature

**✅ Use Direct Skills:**
```bash
/create-task-spec "JWT-based login with email"
/implement-feature task-login-001
/run-tests --coverage
/quality-gate task-login-001
```
**Why:** You know exactly what needs to be done

### Scenario 2: Authentication Decision

**✅ Use Subagents:**
```bash
@alex "I need authentication. Should I use JWT, sessions, or OAuth?"
# Alex helps you decide

@winston "What's the best architecture for auth at scale?"
# Winston provides options

@james "Once we decide, implement the chosen approach"
# James implements with guidance
```
**Why:** You're still figuring out the approach

### Scenario 3: Production Bug

**✅ Use Subagents:**
```bash
@james "Users getting 500 errors on login, need help debugging"
# James investigates and finds root cause

@james "Implement the fix you found"
# James creates the fix
```
**Why:** Unknown problem requires exploration

### Scenario 4: Sprint Planning

**✅ Use Direct Skills:**
```bash
/breakdown-epic docs/epic-cart.md
/estimate-stories docs/stories/
/sprint-plan docs/stories/ --velocity 40
```
**Why:** Structured, repeatable process

---

## Common Mistakes

### ❌ Mistake 1: Using Subagents for Simple Tasks

**Wrong:**
```bash
@alex "Create a task spec for login"
```

**Right:**
```bash
/create-task-spec "User login feature"
```

**Why:** You know what you want - use direct skill (faster)

### ❌ Mistake 2: Using Direct Skills for Unknown Problems

**Wrong:**
```bash
/fix-issue "Something is broken but I don't know what"
```

**Right:**
```bash
@james "The app is crashing on startup, need help debugging"
```

**Why:** Unknown problems need exploration - use subagent

### ❌ Mistake 3: Not Switching Approaches

**Scenario:** Started with subagent, now know what to do

**Inefficient:**
```bash
@alex "Now create a task spec"
@alex "Now estimate it"
@alex "Now create sprint plan"
```

**Efficient:**
```bash
# After getting advice from @alex, switch to direct:
/create-task-spec "Feature we discussed"
/estimate-stories docs/stories/
/sprint-plan docs/stories/ --velocity 40
```

---

## Pro Tips

### Tip 1: Start with Subagent, Then Switch

```bash
# Exploration phase
@winston "Help me understand the architecture options"

# Once you decide, switch to direct skills
/create-architecture docs/requirements.md --type microservices
/validate-architecture docs/architecture.md
```

### Tip 2: Use Direct Skills for Batch Operations

```bash
# Process multiple tasks quickly
/implement-feature task-001
/implement-feature task-002
/implement-feature task-003
/run-tests --coverage
```

### Tip 3: Use Subagents for Learning

```bash
@james "Implement task-001 and explain the TDD process as you go"
# Learn while working
```

### Tip 4: Combine Both Approaches

```bash
# Get advice
@winston "Quick architecture review of my design"

# Implement based on feedback
/validate-architecture docs/architecture.md
/create-adr "Use PostgreSQL based on Winston's advice"

# Get final check
@quinn "Review the updated architecture"
```

---

## Summary

**Direct Skills (`/commands`):**
- Fast, structured, deterministic
- Use when you know what to do
- Great for workflows

**Subagents (`@agents`):**
- Conversational, exploratory, helpful
- Use when you need guidance
- Great for unknowns

**Remember:** Both use the same skills underneath! Subagents just add conversation and guidance.

---

## Quick Reference Table

| I want to... | Use This |
|--------------|----------|
| Create a task spec | `/create-task-spec "desc"` |
| Get planning advice | `@alex "need help planning..."` |
| Implement a feature | `/implement-feature task-ID` |
| Debug unknown issue | `@james "help debug..."` |
| Run tests | `/run-tests --coverage` |
| Learn about code | `@james "explain this code..."` |
| Check quality | `/quality-gate task-ID` |
| Get quality advice | `@quinn "is this ready?"` |
| Design architecture | `/create-architecture file.md` |
| Get arch advice | `@winston "should I use..."` |
| Complete workflow | `@orchestrator *workflow type` |

---

**See Also:**
- [README](../README.md) - Project overview
- [Quick Start](./QUICK-START.md) - Getting started
- [User Guide](./USER-GUIDE.md) - Complete manual
- [Command Routing Guide](./COMMAND-ROUTING-GUIDE.md) - Technical details

---

**Last Updated:** 2025-11-10
**Version:** 1.0
