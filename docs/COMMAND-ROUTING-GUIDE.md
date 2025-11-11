# Command Routing Guide

**BMAD Enhanced V2 - Hybrid Architecture**

This guide helps you choose between **skill-direct commands** and **subagent commands** for optimal quality and efficiency.

---

## Quick Decision Tree

```
Is your task clear and deterministic?
  ├─ YES → Use skill-direct command (/analyze-architecture, /implement-feature, etc.)
  └─ NO  → Is it exploratory or conversational?
      ├─ YES → Use subagent (@winston-architect, @james-developer-v2, etc.)
      └─ NO  → Use skill-direct command (when in doubt, start here)
```

---

## Architecture Overview

### Skill-Direct Commands (Deterministic Path)
```
User → /command → Skill → Primitives
                  (loaded in main context - reliable)
```

**Characteristics:**
- ✅ Reliable (skills always load in main context)
- ✅ Context-efficient (skills loaded on-demand)
- ✅ Fast (no subprocess overhead)
- ✅ Structured outputs (standardized formats)
- ✅ Repeatable (same workflow every time)

### Subagent Commands (Flexible Path)
```
User → /command → Task(subagent) → Skills (when appropriate)
                                  ↓
                              Primitives
```

**Characteristics:**
- 🔀 Flexible (dynamic decision-making)
- 🗣️ Conversational (multi-turn interactions)
- 🔍 Exploratory (discovers as it goes)
- 🎯 Adaptive (adjusts based on findings)
- ⚠️ Variable (skills may not load consistently in subprocess)

---

## When to Use Skill-Direct Commands

### Use Cases
1. **Clear inputs and outputs** - "Analyze this codebase"
2. **Documented workflow** - Known sequence of steps
3. **Repeatable process** - Same task performed multiple times
4. **Structured deliverables** - Formal reports, specifications
5. **Speed critical** - Need results quickly
6. **High reliability required** - Cannot afford skill loading failures

### Examples

**Architecture:**
```bash
/analyze-architecture .  --depth comprehensive
/create-architecture docs/prd.md --type fullstack
/validate-architecture docs/architecture.md
/create-adr "Use PostgreSQL for relational data"
/compare-architectures "Add real-time chat feature"
/review-architecture docs/architecture.md --focus security
```

**Planning:**
```bash
/create-task-spec "User authentication feature"
/breakdown-epic docs/epic-auth.md
/estimate-stories docs/stories/
/sprint-plan docs/stories/ --velocity 40
/refine-story docs/stories/story-001.md
```

**Development:**
```bash
/implement-feature task-006
/fix-issue task-012
/run-tests --coverage
/refactor-code src/auth/login.ts
/apply-qa-fixes docs/quality-gate-report.md
```

**Quality:**
```bash
/quality-gate task-006
/nfr-assess docs/prd.md
/review-task task-006
/test-design docs/requirements.md
/trace-requirements docs/prd.md
/risk-profile docs/architecture.md
```

---

## When to Use Subagent Commands

### Use Cases
1. **Exploratory work** - "Help me figure out what's wrong"
2. **Conversational guidance** - "Should I use X or Y?"
3. **Unknown state** - Need to investigate first
4. **Multi-turn interaction** - Questions and answers
5. **Dynamic workflows** - Path depends on discoveries
6. **Debugging** - Trial-and-error problem solving

### Examples

**Architecture Consultation:**
```bash
/winston-consult "Should I refactor or rewrite this legacy system?"
@winston-architect "Help me modernize this codebase"
/winston *compare-architectures "Current system vs microservices"
```

**Planning Guidance:**
```bash
@alex-planner-v2 "Help me plan this vague feature idea"
/alex consult "How should I break down this complex epic?"
```

**Development & Debugging:**
```bash
/james debug "Login is intermittently failing"
@james-developer-v2 "Tests are broken but I don't know why"
/james fix "Something wrong with authentication"
@james-developer-v2 "Explain how this authentication flow works"
```

**Quality Consultation:**
```bash
@quinn-quality-v2 "Review my architecture for security risks"
/quinn consult "How should I improve test coverage?"
```

**Workflow Orchestration:**
```bash
/orchestrator *workflow feature-delivery "Social login"
/orchestrator *document-codebase . --depth comprehensive
/orchestrator *coordinate "alex,james,quinn" "Deliver user auth feature"
```

---

## Comparison Matrix

| Factor | Skill-Direct | Subagent |
|--------|--------------|----------|
| **Reliability** | ⭐⭐⭐⭐⭐ High | ⭐⭐⭐ Variable |
| **Speed** | ⭐⭐⭐⭐⭐ Fast | ⭐⭐⭐ Slower |
| **Context Efficiency** | ⭐⭐⭐⭐⭐ Optimal | ⭐⭐⭐⭐ Good |
| **Flexibility** | ⭐⭐ Limited | ⭐⭐⭐⭐⭐ High |
| **Conversational** | ⭐ No | ⭐⭐⭐⭐⭐ Yes |
| **Structured Output** | ⭐⭐⭐⭐⭐ Always | ⭐⭐⭐ Sometimes |
| **Exploration** | ⭐ No | ⭐⭐⭐⭐⭐ Excellent |
| **Best For** | Known tasks | Unknown problems |

---

## Special Cases

### Case 1: Debugging

**ALWAYS use subagent (@james-developer-v2) for debugging:**

**Why:**
- Unknown initial state
- Requires exploration and investigation
- May need multiple rounds of trial-and-error
- Dynamic decisions based on findings
- Can invoke skills after diagnosis

**Example:**
```bash
# ❌ Don't use skill-direct for unknown debugging
/fix-issue "something is broken"  # Needs clear issue ID

# ✅ Use subagent for exploratory debugging
/james debug "Login returning 500 errors"
@james-developer-v2 "Users reporting intermittent failures"
```

### Case 2: Architecture Decision-Making

**Use subagent for exploration, skill-direct for execution:**

**Exploration Phase:**
```bash
/winston-consult "Evaluate migration from monolith to microservices"
# Winston: asks questions, explores options, discusses trade-offs
```

**Execution Phase:**
```bash
/compare-architectures "Current monolith vs microservices vs modular monolith"
# Skill: generates 3 options with detailed trade-off analysis
```

### Case 3: Complete Workflows

**Use orchestrator for multi-agent coordination:**

```bash
/orchestrator *workflow feature-delivery "Two-factor authentication"
# Orchestrator coordinates:
#   1. Alex creates task spec
#   2. Winston validates architecture
#   3. James implements feature
#   4. Quinn runs quality gate
#   5. Creates PR
```

---

## Best Practices

### 1. Start with Skill-Direct Commands

When in doubt, start with skill-direct:
```bash
# Start simple
/analyze-architecture .

# Escalate if needed
@winston-architect "I need help understanding these results"
```

### 2. Use Subagents for Guidance

Use subagents when you need help deciding:
```bash
# Get guidance
@winston-architect "Help me choose between REST and GraphQL"

# Then execute
/create-architecture docs/prd.md --type backend
```

### 3. Combine Both Approaches

Use the hybrid model strategically:
```bash
# 1. Explore with subagent
@alex-planner-v2 "Help me plan this complex feature"

# 2. Execute with skill-direct
/create-task-spec "User authentication with OAuth"
/breakdown-epic docs/epic-auth.md
/sprint-plan docs/stories/ --velocity 40
```

### 4. Debugging Workflow

Always start debugging with subagent:
```bash
# 1. Investigate with subagent
/james debug "Payment processing failing"

# 2. Once issue identified, subagent may invoke skill
# Subagent internally: Skill(command="fix-issue")

# 3. Validate fix
/run-tests src/payment/

# 4. Quality gate
/quality-gate task-payment-fix
```

---

## Migration from V1

**Old Pattern (V1):**
```bash
/winston *analyze-architecture .
# Routes to winston subagent → skills may not load
```

**New Pattern (V2 Hybrid):**
```bash
# For deterministic analysis
/analyze-architecture .  # Direct skill invocation ✅

# For conversational guidance
/winston-consult "Help me with architecture"  # Subagent ✅
```

**What Changed:**
- V1: Everything routed through subagents
- V2: Deterministic tasks use skill-direct, flexible tasks use subagents
- V2: Better reliability, clarity, and context efficiency

---

## Command Reference

### Skill-Direct Commands (Alphabetical)

| Command | Description | Usage |
|---------|-------------|-------|
| `/analyze-architecture` | Brownfield codebase analysis | `/analyze-architecture . --depth quick` |
| `/apply-qa-fixes` | Apply quality gate fixes | `/apply-qa-fixes quality-gate-report.md` |
| `/breakdown-epic` | Epic → user stories | `/breakdown-epic docs/epic-auth.md` |
| `/compare-architectures` | Compare architecture options | `/compare-architectures "Add real-time chat"` |
| `/create-adr` | Create Architecture Decision Record | `/create-adr "Use PostgreSQL"` |
| `/create-architecture` | Design architecture from PRD | `/create-architecture docs/prd.md` |
| `/create-task-spec` | Requirements → task spec | `/create-task-spec "User login"` |
| `/estimate-stories` | Fibonacci story estimation | `/estimate-stories docs/stories/` |
| `/fix-issue` | Fix known issue | `/fix-issue task-012` |
| `/implement-feature` | Implement from spec | `/implement-feature task-006` |
| `/nfr-assess` | Assess non-functional requirements | `/nfr-assess docs/prd.md` |
| `/quality-gate` | Run quality assessment | `/quality-gate task-006` |
| `/refactor-code` | Safe code refactoring | `/refactor-code src/auth/` |
| `/refine-story` | Improve story quality | `/refine-story docs/story-001.md` |
| `/review-architecture` | Peer review architecture | `/review-architecture docs/architecture.md` |
| `/review-task` | Review completed task | `/review-task task-006` |
| `/risk-profile` | Risk assessment | `/risk-profile docs/architecture.md` |
| `/run-tests` | Execute test suite | `/run-tests --coverage` |
| `/sprint-plan` | Generate sprint plan | `/sprint-plan docs/stories/ --velocity 40` |
| `/test-design` | Design test strategy | `/test-design docs/prd.md` |
| `/trace-requirements` | Requirements traceability | `/trace-requirements docs/prd.md` |
| `/validate-architecture` | Validate architecture doc | `/validate-architecture docs/architecture.md` |

### Subagent Commands

| Command | Description | Usage |
|---------|-------------|-------|
| `@alex-planner-v2` | Planning guidance | `@alex-planner-v2 "Help me plan this"` |
| `@james-developer-v2` | Development & debugging | `@james-developer-v2 "Debug login issue"` |
| `@winston-architect` | Architecture consultation | `@winston-architect "Modernize my app"` |
| `@quinn-quality-v2` | Quality consultation | `@quinn-quality-v2 "Review security"` |
| `@orchestrator-v2` | Workflow coordination | `@orchestrator-v2 "Deliver feature"` |
| `/winston-consult` | Architecture consultation | `/winston-consult "Microservices vs monolith"` |
| `/james debug` | Debug unknown issue | `/james debug "Tests failing"` |
| `/orchestrator *workflow` | Execute complete workflow | `/orchestrator *workflow feature-delivery "Login"` |

---

## Troubleshooting

### Issue: Skill didn't load in subagent

**Symptom:**
Subagent says "Skill didn't load, proceeding with expertise"

**Solution:**
Use skill-direct command instead:
```bash
# Instead of
/winston *analyze-architecture .

# Use
/analyze-architecture .
```

### Issue: Need conversational help

**Symptom:**
Skill-direct command doesn't answer your questions

**Solution:**
Use subagent for guidance:
```bash
# Instead of
/create-architecture docs/vague-requirements.md

# Use
@winston-architect "Help me design architecture for these requirements"
```

### Issue: Debugging not working

**Symptom:**
Can't figure out what's broken

**Solution:**
Always use subagent for debugging:
```bash
/james debug "Describe the problem"
@james-developer-v2 "Explain what's happening"
```

---

## Summary

**Golden Rules:**
1. **Clear task** → Skill-direct command
2. **Unclear problem** → Subagent
3. **Debugging** → Always subagent
4. **Speed/reliability** → Skill-direct
5. **Exploration/guidance** → Subagent
6. **When in doubt** → Start with skill-direct

**Objective:**
**Maximize quality while minimizing context** through intelligent routing between skill-direct (deterministic) and subagent (flexible) execution paths.
