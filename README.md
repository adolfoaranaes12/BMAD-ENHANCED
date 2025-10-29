# BMAD Enhanced

**Break My AGILE Down - Enhanced Edition**

Transform hours of AGILE ceremony into minutes of AI-assisted productivity.

---

## What is BMAD Enhanced?

BMAD Enhanced is a comprehensive AI-powered AGILE workflow system that automates the entire software development lifecycle - from epic breakdown to production deployment - using specialized AI subagents.

**Time Savings:**
- Before: 10-17 hours per feature (manual AGILE)
- After: 48-63 minutes per feature (AI-assisted)
- Savings: 85-90% reduction in AGILE overhead

---

## Quick Start

### Basic Usage

Command format: `@<subagent> *<command> <args>`

**Examples:**
```
@alex *breakdown "User Authentication System"
@james *implement task-auth-002
@quinn *review task-auth-002
@orchestrator *deliver "User login feature"
```

### Using Slash Commands

Convenient shortcuts for each subagent:
```
/alex breakdown "Epic Name"
/james implement task-001
/quinn review task-001
/orchestrator deliver "Feature Name"
```

### Using Router Directly

```
Use .claude/skills/router.md with command "@alex *breakdown 'Epic Name'"
```

---

## The Team

BMAD Enhanced consists of 4 specialized AI subagents:

### 🎯 Alex (Planner)
**Role:** Planning & Estimation

**Commands:**
- `*breakdown <epic>` - Break down epic into user stories
- `*estimate <story>` - Estimate story points
- `*sprint <stories>` - Create sprint plan
- `*refine <story>` - Refine story details
- `*plan <story>` - Create detailed task specification

**Example:**
```
/alex breakdown "User Authentication System"
```

---

### 💻 James (Developer)
**Role:** Development & Implementation

**Commands:**
- `*implement <task-id>` - Implement feature using TDD
- `*fix <issue>` - Fix bug with test coverage
- `*test <scope>` - Run tests and analyze coverage
- `*refactor <code>` - Refactor code
- `*debug <issue>` - Debug problem
- `*coverage` - Analyze test coverage

**Example:**
```
/james implement task-auth-002
```

---

### ✅ Quinn (Quality)
**Role:** Quality Assurance & Review

**Commands:**
- `*review <task-id>` - Review implementation quality
- `*audit <code>` - Audit code quality
- `*security <code>` - Security audit
- `*performance <code>` - Performance analysis
- `*accessibility <code>` - Accessibility check
- `*report <task-id>` - Generate quality report

**Example:**
```
/quinn review task-auth-002
```

---

### 🎭 Orchestrator (Coordinator)
**Role:** Workflow Coordination

**Commands:**
- `*deliver <feature>` - Execute full delivery workflow

**Example:**
```
/orchestrator deliver "User login feature"
```

**What it does:**
1. Alex breaks down epic into stories
2. Alex creates task specifications
3. James implements each task with TDD
4. Quinn reviews each implementation
5. Reports completion

---

## Common Workflows

### Workflow 1: Plan a Feature
```
1. /alex breakdown "Feature Name"
   → Returns: story-001, story-002, story-003

2. /alex estimate story-001
   → Returns: 5 story points

3. /alex plan story-001
   → Returns: task-001, task-002, task-003
```

---

### Workflow 2: Implement a Task
```
1. /james implement task-auth-002
   → Implements feature with TDD
   → Runs tests
   → Reports coverage

2. /quinn review task-auth-002
   → Reviews code quality
   → Checks tests
   → Provides recommendations

3. (Fix issues if any)
4. /james fix <issue-description>
```

---

### Workflow 3: Full Feature Delivery
```
/orchestrator deliver "User login with JWT tokens"

→ Automatically:
  1. Breaks down epic
  2. Creates task specs
  3. Implements all tasks
  4. Reviews all tasks
  5. Reports completion
```

---

## Architecture

### Directory Structure
```
.claude/
├── commands/               # Slash commands
│   ├── alex.md
│   ├── james.md
│   ├── quinn.md
│   └── orchestrator.md
├── skills/                 # Executable skills
│   ├── router.md          # Command router (NEW!)
│   ├── planning/          # Alex's skills (5)
│   ├── development/       # James's skills (3)
│   ├── quality/           # Quinn's skills (6)
│   ├── implementation/    # Orchestrator skills (1)
│   └── templates/         # Templates (2)
├── subagents/             # Subagent definitions
│   ├── alex-planner.md
│   ├── james-developer.md
│   ├── quinn-quality.md
│   └── orchestrator.md
└── templates/             # Task/Story templates
    ├── task-template.md
    └── story-template.md

docs/                      # Documentation
├── command-routing-design.md
├── command-routing-tests.md
├── architecture.md
├── standards.md
└── ... (more docs)

workspace/                 # Generated artifacts
├── epics/
├── stories/
└── tasks/
```

### Components

**18 Skills Total:**
- Planning: 5 skills (breakdown, estimate, sprint, refine, plan)
- Development: 3 skills (implement, fix, test)
- Quality: 6 skills (review, audit, security, performance, accessibility, report)
- Implementation: 1 skill (deliver)
- Routing: 1 skill (router)
- Templates: 2 skills (task, story)

**4 Subagents:**
- Alex (Planner)
- James (Developer)
- Quinn (Quality)
- Orchestrator (Coordinator)

**4 Slash Commands:**
- /alex
- /james
- /quinn
- /orchestrator

**Total Lines of Code:** 40,300+

---

## Command Reference

### Help Commands

```
# General help
@help

# Subagent-specific help
@alex *help
@james *help
@quinn *help
@orchestrator *help

# Version info
@version
```

---

## Development Principles

### Test-Driven Development (TDD)

James follows strict TDD workflow:

1. **Red Phase:** Write failing tests first
2. **Green Phase:** Implement code to make tests pass
3. **Refactor Phase:** Improve code while keeping tests green

**Example:**
```typescript
// Step 1: Write failing test (RED)
describe('AuthService.login', () => {
  it('should return user when credentials valid', async () => {
    const user = await authService.login('user@example.com', 'password');
    expect(user).toBeDefined();
  });
});

// Step 2: Implement (GREEN)
export class AuthService {
  async login(email: string, password: string): Promise<User | null> {
    const user = await User.findByEmail(email);
    if (!user) return null;
    const valid = await bcrypt.compare(password, user.password_hash);
    return valid ? user : null;
  }
}

// Step 3: Refactor (while keeping tests green)
```

---

### Quality Standards

Quinn enforces comprehensive quality checks:

- **Code Quality:** Linting, formatting, type checking
- **Test Coverage:** Minimum 80% coverage
- **Security:** Input validation, SQL injection, XSS prevention
- **Performance:** Response time, memory usage, database queries
- **Accessibility:** WCAG 2.1 AA compliance
- **Documentation:** Clear comments, README, API docs

---

## Integration with GitHub

BMAD Enhanced integrates with GitHub MCP for:

- Branch management
- Commits with standardized messages
- Pull request creation
- Code review workflows
- Issue tracking

**Example workflow:**
```
/james implement task-auth-002
→ Creates branch: feature/task-auth-002
→ Implements code with tests
→ Commits changes
→ Creates pull request
→ Requests review
```

---

## Configuration

### Settings File
`.claude/config.yaml`

```yaml
workspaceRoot: "./workspace"
epicTemplate: ".claude/templates/epic-template.md"
storyTemplate: ".claude/templates/story-template.md"
taskTemplate: ".claude/templates/task-template.md"
qualityStandards: ".claude/templates/quality-checklist.md"
testFramework: "jest"
coverageThreshold: 80
```

---

## Documentation

Comprehensive documentation available in `docs/`:

- **command-routing-design.md** - Router architecture
- **command-routing-tests.md** - Test cases and examples
- **architecture.md** - System architecture
- **standards.md** - Code and quality standards
- **BROWNFIELD-GETTING-STARTED.md** - Using with existing projects
- **ROADMAP.md** - Future enhancements
- **AB-TEST-COMPARISON.md** - Before/after comparison

---

## Examples

### Example 1: Simple Feature

**Goal:** Implement user login endpoint

```bash
# Step 1: Plan
/alex breakdown "User Login Feature"
# Returns: story-login-001

/alex plan story-login-001
# Returns: task-login-001, task-login-002, task-login-003

# Step 2: Implement
/james implement task-login-001
# Implements POST /api/auth/login with tests

# Step 3: Review
/quinn review task-login-001
# Reviews code quality, security, tests
```

---

### Example 2: Complete Epic

**Goal:** Full authentication system

```bash
# Single command for entire epic
/orchestrator deliver "User Authentication System with JWT"

# Orchestrator automatically:
# 1. Alex breaks down into stories
# 2. Alex creates task specs for each story
# 3. James implements each task with TDD
# 4. Quinn reviews each implementation
# 5. Reports completion with stats
```

---

## Troubleshooting

### Command Not Found

**Problem:** `❌ Unknown Command: *xyz`

**Solution:**
- Check command name spelling
- Use `@<subagent> *help` to see available commands
- Verify asterisk (*) is present

---

### Subagent Not Found

**Problem:** `❌ Unknown Subagent: @xyz`

**Solution:**
- Available subagents: @alex, @james, @quinn, @orchestrator
- Check spelling and use lowercase
- Use `@help` to see all subagents

---

### Skill File Not Found

**Problem:** `❌ Skill File Not Found`

**Solution:**
- Verify `.claude/skills/` directory exists
- Check all skill files are present
- Verify subagent command mappings are correct

---

## Statistics

### Code Volume
- **Total:** 40,300+ lines
- **Subagents:** 5,550 lines
- **Skills:** 28,580 lines
- **Documentation:** 4,900 lines
- **Templates:** 1,150 lines
- **Configuration:** 120 lines

### Time Savings
- **Planning:** 2-4 hours → 8-12 minutes (83% savings)
- **Implementation:** 4-8 hours → 20-30 minutes (87% savings)
- **Review:** 2-3 hours → 10-15 minutes (83% savings)
- **Coordination:** 2-3 hours → 10-15 minutes (83% savings)
- **Total:** 10-17 hours → 48-63 minutes (85-90% savings)

---

## Advanced Features

### Custom Skills

Create custom skills in `.claude/skills/`:

```markdown
# My Custom Skill

## Purpose
What this skill does

## Inputs
- input1: Description
- input2: Description

## Process

### Step 0: Load Context
...

### Step 1: Do Something
...

## Outputs
- What this skill returns
```

Add to subagent:
```markdown
### Command: `*custom`
**Skill:** `.claude/skills/custom/my-skill.md`
**Purpose:** Custom functionality
```

---

### Workflow Customization

Modify orchestrator.md to create custom workflows:

```markdown
### Command: `*custom-workflow`
**Skill:** `.claude/skills/implementation/custom-workflow.md`
**Purpose:** Execute custom workflow
**Steps:**
1. Alex: Do planning thing
2. James: Do development thing
3. Quinn: Do quality thing
4. Report results
```

---

## Contributing

### Adding New Commands

1. Create skill in `.claude/skills/`
2. Add command mapping to subagent file
3. Test with router
4. Document in README
5. Add test cases

---

## Support

### Getting Help

- **General Help:** `@help`
- **Subagent Help:** `@alex *help` (or @james, @quinn, @orchestrator)
- **Version Info:** `@version`
- **Documentation:** `docs/` directory
- **Test Cases:** `docs/command-routing-tests.md`

---

## License

MIT License

---

## Version

**Version:** 1.0.0
**Status:** Production Ready
**Date:** January 15, 2025

---

## Credits

**Created by:** BMAD Enhanced Team
**Powered by:** Claude Code + Anthropic AI

---

## Next Steps

1. **Try it out:**
   ```
   /alex breakdown "Your First Epic"
   ```

2. **Read the docs:**
   - Start with: `docs/BROWNFIELD-GETTING-STARTED.md`
   - Architecture: `docs/architecture.md`
   - Standards: `docs/standards.md`

3. **Explore workflows:**
   - Simple: Plan → Implement → Review
   - Advanced: Use orchestrator for full automation

4. **Customize:**
   - Add custom skills
   - Create custom workflows
   - Adjust quality standards

---

**Welcome to BMAD Enhanced - Where AGILE meets AI!**
