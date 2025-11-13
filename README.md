# BMAD Enhanced

**Break My AGILE Down - Enhanced Edition**

Transform hours of AGILE ceremony into minutes of AI-assisted productivity.

---

## 📚 Quick Navigation

**New to BMAD Enhanced?** Start here:

- **[Quick Start](./docs/QUICK-START.md)** ⭐ - Get started fast
- **[Choosing Your Approach](./docs/CHOOSING-YOUR-APPROACH.md)** ⭐ - Direct Skills or Subagents?
- **[User Guide](./docs/USER-GUIDE.md)** - Complete guide
- **[Workflow Guide](./docs/WORKFLOW-GUIDE.md)** - Practical examples
- **[Troubleshooting](./docs/TROUBLESHOOTING.md)** - Fix common issues

**See [Documentation Index](./docs/DOCUMENTATION-INDEX.md) for all guides**

---

## What is BMAD Enhanced?

BMAD Enhanced is a **Claude Code native** AI agent framework that implements the proven BMAD Method v4 workflow. It transforms 10-17 hours of manual AGILE work into 48-63 minutes of AI-assisted productivity.

**Time Savings: 85-90% reduction in AGILE overhead**

---

## Two Ways to Use BMAD Enhanced

BMAD Enhanced gives you **two approaches** for different use cases:

### 1️⃣ Slash Commands (Direct Skills) - For Structured Tasks

**When to use:** You know exactly what you want to do

```bash
/create-task-spec "User authentication"     # Creates task specification
/implement-feature task-001                 # Implements the feature
/quality-gate task-001                      # Runs quality checks
```

**Best for:**
- ✅ Clear, specific tasks with known requirements
- ✅ Repeatable workflows (planning, implementation, testing)
- ✅ Fast, deterministic results
- ✅ When you want direct skill execution

### 2️⃣ Subagents (Conversational) - For Exploration & Guidance

**When to use:** You need help figuring out what to do

```bash
@james "Help me debug this login issue"            # Interactive debugging
@winston "Should I use microservices or monolith?" # Architecture advice
@orchestrator *workflow feature-delivery "Social login"  # Complete workflow
```

**Best for:**
- 💬 Need guidance or don't know where to start
- 🔍 Exploring options or debugging issues
- 🤝 Want conversational interaction
- 🎯 Complex workflows requiring coordination

---

## Quick Decision Guide

```
Do you know EXACTLY what needs to be done?
│
├─ YES → Use /slash-commands (Direct Skills)
│         Fast, deterministic, structured output
│
└─ NO  → Use @subagents (Conversational)
          Get guidance, explore options, interactive help
```

**Examples:**

| What You Want | Use This | Command |
|---------------|----------|---------|
| Create a task spec | Direct Skill | `/create-task-spec "Login feature"` |
| Not sure how to architect something | Subagent | `@winston "Need help with architecture"` |
| Implement a specific task | Direct Skill | `/implement-feature task-001` |
| Debug an unknown issue | Subagent | `@james "Login is broken, help debug"` |
| Run tests | Direct Skill | `/run-tests --coverage` |
| Plan entire epic | Subagent | `@orchestrator *workflow epic-to-sprint` |

---

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/bmad-enhanced.git
cd bmad-enhanced

# Verify structure
ls -la .claude/
```

**See [Installation Guide](./docs/INSTALLATION-GUIDE.md) for detailed setup**

---

## How to Use: Choose Your Approach

### Approach 1: Direct Skills (Slash Commands)

Use `/command` when you know what you need:

```bash
# Complete workflow - structured tasks
/create-task-spec "User authentication feature"
/implement-feature task-auth-001
/run-tests --coverage
/quality-gate task-auth-001
```

**All Available Commands:**
- **Planning:** `/create-task-spec`, `/breakdown-epic`, `/estimate-stories`, `/sprint-plan`
- **Architecture:** `/analyze-architecture`, `/create-architecture`, `/validate-architecture`
- **Development:** `/implement-feature`, `/run-tests`, `/fix-issue`, `/refactor-code`
- **Quality:** `/quality-gate`, `/nfr-assess`, `/trace-requirements`, `/test-design`

### Approach 2: Subagents (Conversational)

Use `@agent` when you need guidance:

```bash
# Get help and interact
@alex "I have a feature request for user login, how should I break this down?"
@winston "Should I use REST or GraphQL for my API?"
@james "The tests are failing but I'm not sure why"
@quinn "Is this code ready for production?"
```

**Available Subagents:**
- **@alex** - Planning & Requirements (creates specs, breaks down work)
- **@james** - Development (implements, debugs, explains code)
- **@quinn** - Quality Assurance (reviews, validates, assesses)
- **@winston** - Architecture (designs, analyzes, advises)
- **@orchestrator** - Workflow Coordination (runs complete workflows)

---

## Common Workflows

### Workflow 1: Simple Feature (Direct Skills Approach)

When you know what to build:

```bash
# 1. Create specification
/create-task-spec "User login endpoint with JWT"

# 2. Implement
/implement-feature task-login-001

# 3. Quality check
/quality-gate task-login-001
```

**Why this approach:** Clear requirements, structured output, fast execution

### Workflow 2: Feature with Guidance (Subagent Approach)

When you need help figuring it out:

```bash
# 1. Get planning help
@alex "I need to add user authentication, not sure how to break it down"

# 2. Get implementation help
@james "Implement the task we just created, need TDD guidance"

# 3. Get quality feedback
@quinn "Review the authentication code, check for security issues"
```

**Why this approach:** Interactive guidance, exploratory, flexible

### Workflow 3: Complete Automation (Orchestrator)

Let the orchestrator handle everything:

```bash
# One command for entire feature
@orchestrator *workflow feature-delivery "Social login with OAuth"

# Automatically: plan → architect → implement → test → review
```

**Why this approach:** Hands-off automation, end-to-end delivery

**See [Workflow Guide](./docs/WORKFLOW-GUIDE.md) for 15+ detailed examples**

**📖 [Complete Guide: Choosing Your Approach](./docs/CHOOSING-YOUR-APPROACH.md)** - Detailed decision guide with examples

---

## Behind the Scenes

**How it works:** BMAD Enhanced has reusable skills (like building blocks) and conversational agents that help you use them.

Both approaches use the same skills:
- `/create-task-spec` → Runs the skill directly
- `@alex *create-task-spec` → Alex helps you run the skill

**The difference:** Subagents add conversation and guidance.

**Core 5 Subagents (Most Common):**

| Subagent | Specialization | Quick Start Guide |
|----------|----------------|-------------------|
| **@alex** | Planning & Requirements | [Guide](./docs/quickstart-alex.md) |
| **@james** | Development & Debugging | [Guide](./docs/quickstart-james.md) |
| **@quinn** | Quality & Testing | [Guide](./docs/quickstart-quinn.md) |
| **@winston** | Architecture & Design | [Guide](./docs/quickstart-winston.md) |
| **@orchestrator** | Workflow Coordination | [Guide](./docs/quickstart-orchestrator.md) |

**Plus 5 specialized persona agents:** @john (PM), @mary (Analyst), @bob (Scrum Master), @sarah (PO), @sally (UX)

*See [Agent Routing Guide](./docs/AGENT-ROUTING-GUIDE.md) for all 10 agents*

**Bonus:** Framework-agnostic testing (Jest, Pytest, JUnit, GTest, Cargo, Go, etc.)

---

## Documentation

### Getting Started
- **[Quick Start](./docs/QUICK-START.md)** - Get started fast
- **[Choosing Your Approach](./docs/CHOOSING-YOUR-APPROACH.md)** - Which way to work
- **[User Guide](./docs/USER-GUIDE.md)** - Complete guide
- **[Workflow Examples](./docs/WORKFLOW-GUIDE.md)** - Real-world examples
- **[Troubleshooting](./docs/TROUBLESHOOTING.md)** - Fix issues

### For Developers
- **[Best Practices](./docs/BEST-PRACTICES.md)** - How to use effectively
- **[Command Reference](./docs/COMMAND-REFERENCE-SUMMARY.md)** - All commands

### For Teams
- **[Production Deployment](./docs/PRODUCTION-DEPLOYMENT-GUIDE.md)** - Deploy to production
- **[Security Review](./docs/PRODUCTION-SECURITY-REVIEW.md)** - Security checklist

**[Complete Documentation Index](./docs/DOCUMENTATION-INDEX.md)** - All guides

---

## Project Status

**Status:** Production Ready ✅

BMAD Enhanced is ready to use for real projects. It's been thoroughly tested and includes everything you need to start building software faster.

**See [Roadmap](./docs/ROADMAP.md) for what's next**

---

## Real-World Examples

### Example 1: Authentication Feature

**Using Direct Skills (You know what to do):**
```bash
/create-task-spec "JWT authentication with email/password"
/implement-feature task-auth-001
/run-tests --coverage
/quality-gate task-auth-001
```
**Result:** Task spec → Implementation → Tests passing → Quality approved (15 minutes)

**Using Subagents (You need guidance):**
```bash
@alex "I need authentication but not sure about JWT vs sessions"
# Alex helps you decide and creates the spec

@james "Implement task-auth-001, walk me through TDD"
# James implements with explanations

@quinn "Check if this auth code is secure"
# Quinn reviews for security issues
```
**Result:** Same outcome + guidance and explanations (20 minutes)

### Example 2: Debug Production Issue

**You must use Subagents for this** (unknown problem):
```bash
@james "Users can't login, getting 500 errors, need help debugging"
# James investigates, finds issue, proposes fix

@james "Implement the fix you suggested"
# James implements and tests the fix
```

**Why not Direct Skills?** Debugging unknown issues requires exploration - that's what subagents do!

### Example 3: Sprint Planning

**Using Direct Skills** (structured, repeatable):
```bash
/breakdown-epic docs/epic-shopping-cart.md    # → 8 stories
/estimate-stories docs/stories/ --velocity 40  # → Points assigned
/sprint-plan docs/stories/ --velocity 40       # → Sprint plan created
```

**Using Orchestrator** (fully automated):
```bash
@orchestrator *workflow epic-to-sprint docs/epic-shopping-cart.md --velocity 40
# Does all three steps automatically
```

**See [Example Workflows](./docs/EXAMPLE-WORKFLOWS.md) for more copy-paste examples**

---

## Troubleshooting

**Not sure which approach to use?**
→ Start with Direct Skills (`/commands`) if you know what to do
→ Use Subagents (`@agent`) if you need help or guidance

**Subagent not understanding you?**
→ Try a Direct Skill instead: `/command-name`

**Want faster results?**
→ Use Direct Skills - they're faster and more deterministic

**Need to explore or debug?**
→ Use Subagents - they're conversational and flexible

**See [Troubleshooting Guide](./docs/TROUBLESHOOTING.md) for detailed help**

---

## Contributing

We welcome contributions! Please follow these guidelines:

1. Read [Standards](./docs/standards.md) for coding conventions
2. Review [Architecture](./docs/V2-ARCHITECTURE.md) for design principles
3. Check [Best Practices](./docs/BEST-PRACTICES.md) for patterns
4. Test thoroughly before submitting
5. Update documentation for any changes

---

## Support

- **Documentation:** [Complete Documentation Index](./docs/DOCUMENTATION-INDEX.md)
- **Issues:** [GitHub Issues](https://github.com/yourusername/bmad-enhanced/issues)
- **Quick Help:** See [Troubleshooting](./docs/TROUBLESHOOTING.md)

---

## License

MIT License - see [LICENSE](./LICENSE) file for details

---

## Credits

**Created by:** BMAD Enhanced Team
**Based on:** BMAD Method v4 (Stable)
**Powered by:** Claude Code + Anthropic AI

---

## Next Steps

1. **Start here:** [Quick Start Guide](./docs/QUICK-START.md)
2. **Learn the basics:** [User Guide](./docs/USER-GUIDE.md)
3. **Try examples:** [Example Workflows](./docs/EXAMPLE-WORKFLOWS.md)
4. **Explore agents:** [Agent Reference](./docs/AGENT-REFERENCE.md)

**Welcome to BMAD Enhanced - Where AGILE meets AI!** 🚀
