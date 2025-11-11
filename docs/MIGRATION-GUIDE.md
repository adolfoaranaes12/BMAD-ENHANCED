# Migration Guide: BMAD v4 to BMAD Enhanced

**Version:** 2.0
**Last Updated:** 2025-11-05
**Estimated Migration Time:** 2-4 hours
**Status:** Production Ready

## Overview

This guide helps you migrate from BMAD v4 to BMAD Enhanced. BMAD Enhanced introduces significant architectural improvements, enhanced capabilities, and a more robust framework while maintaining backward compatibility for most common use cases.

---

## Table of Contents

1. [What's New in BMAD Enhanced](#whats-new-in-bmad-enhanced)
2. [Breaking Changes](#breaking-changes)
3. [Migration Checklist](#migration-checklist)
4. [Step-by-Step Migration](#step-by-step-migration)
5. [Command Mapping](#command-mapping)
6. [Configuration Migration](#configuration-migration)
7. [Skill Migration](#skill-migration)
8. [Testing Your Migration](#testing-your-migration)
9. [Rollback Plan](#rollback-plan)
10. [FAQ](#faq)

---

## What's New in BMAD Enhanced

### Major Improvements

#### 1. **V2 Architecture** 🏗️
- **3-Layer Architecture**: Primitives → Skills → Subagents
- **Intelligent Routing**: Automatic complexity assessment and skill selection
- **Comprehensive Guardrails**: Security, quality, and safety checks
- **Real-time Telemetry**: Enhanced monitoring and observability

#### 2. **Enhanced Subagents** 🤖
- **10 Specialized Subagents** (up from 4 in v4):
  - Alex (Planner v2)
  - James (Developer v2)
  - Quinn (Quality v2)
  - Winston (Architect)
  - Orchestrator v2
  - Sarah (Product Owner)
  - Bob (Scrum Master)
  - Sally (UX Expert)
  - John (Product Manager)
  - Mary (Business Analyst)

#### 3. **New Capabilities** ✨
- **Architecture Design & Analysis**: Greenfield and brownfield workflows
- **Quality Gates**: Automated quality validation
- **Workflow Orchestration**: Multi-step workflow coordination
- **UX Tools Suite**: Interactive wizard, progress visualization, error handling
- **Test Framework Support**: 7 frameworks with adapter pattern

#### 4. **Better Developer Experience** 🎯
- **Comprehensive Documentation**: 60+ guides and references
- **Quickstart Guides**: Per-subagent getting started guides
- **Error Codes Reference**: Structured error handling with remediation
- **Example Workflows**: 11 copy-paste ready workflows
- **Interactive Command Wizard**: Goal-based command recommendations

---

## Breaking Changes

### ⚠️ Critical Breaking Changes

#### 1. Configuration File Structure

**BMAD v4:**
```yaml
# .bmad/config.yml
version: 4.0
agents:
  - name: alex
    type: planner
```

**BMAD Enhanced:**
```yaml
# .claude/config.yaml (new location and name)
version: 2.0
subagents:
  alex:
    enabled: true
    skills:
      - create-task-spec
      - breakdown-epic
```

**Action Required:** Migrate configuration to new format and location.

---

#### 2. Command Syntax Changes

**BMAD v4:**
```bash
bmad plan --task "Add feature"
bmad implement --spec task-001.md
```

**BMAD Enhanced:**
```bash
/alex *create-task-spec --title "Add feature"
/james *implement task-001-spec.md
```

**Action Required:** Update all command invocations to new syntax.

---

#### 3. Directory Structure

**BMAD v4:**
```
.bmad/
├── config.yml
├── tasks/
└── agents/
```

**BMAD Enhanced:**
```
.claude/
├── config.yaml
├── tasks/
├── skills/
├── agents/
├── templates/
└── logs/
```

**Action Required:** Migrate directory structure and update paths.

---

### ⚡ Non-Breaking Changes (Backward Compatible)

1. **Task Specification Format**: Enhanced but v4 format still supported
2. **Output Formats**: New JSON format available, Markdown still supported
3. **Test Commands**: Old syntax works but new syntax recommended

---

## Migration Checklist

Use this checklist to track your migration progress:

### Pre-Migration
- [ ] Backup current BMAD v4 installation and data
- [ ] Review current configuration and customizations
- [ ] Document custom skills and workflows
- [ ] Identify dependencies on BMAD v4 features
- [ ] Read this entire migration guide

### Installation
- [ ] Install BMAD Enhanced alongside BMAD v4 (parallel installation)
- [ ] Verify system prerequisites
- [ ] Clone repository to new location
- [ ] Install Python dependencies
- [ ] Verify installation with `python .claude/skills/bmad-commands/scripts/bmad-wizard.py --version`

### Configuration
- [ ] Migrate `.bmad/config.yml` to `.claude/config.yaml`
- [ ] Update subagent configurations
- [ ] Configure guardrails and quality gates
- [ ] Set up test framework adapters
- [ ] Configure telemetry and logging

### Content Migration
- [ ] Migrate task specifications from `.bmad/tasks/` to `.claude/tasks/`
- [ ] Update custom skills to new format
- [ ] Migrate templates to `.claude/templates/`
- [ ] Update documentation references

### Testing
- [ ] Run migration validation script
- [ ] Test each subagent with sample tasks
- [ ] Verify custom skills work correctly
- [ ] Check CI/CD integration
- [ ] Validate error handling and logging

### Cutover
- [ ] Update team documentation
- [ ] Train team on new commands and workflows
- [ ] Update CI/CD pipelines
- [ ] Monitor for issues in first 24 hours
- [ ] Decommission BMAD v4 after successful migration

---

## Step-by-Step Migration

### Step 1: Install BMAD Enhanced (15 minutes)

#### 1.1 Clone Repository
```bash
# Clone to new directory (keep BMAD v4 intact)
cd ~/Documents/
git clone https://github.com/your-org/bmad-enhanced.git "BMAD Enhanced"
cd "BMAD Enhanced"
```

#### 1.2 Install Dependencies
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Verify installation
python .claude/skills/bmad-commands/scripts/bmad-wizard.py --version
```

Expected output:
```
BMAD Enhanced v2.0
All systems operational ✓
```

---

### Step 2: Migrate Configuration (20 minutes)

#### 2.1 Backup Current Config
```bash
# Backup BMAD v4 config
cp ~/.bmad/config.yml ~/.bmad/config.yml.backup
```

#### 2.2 Create New Configuration
```bash
# Copy template
cp .claude/config.yaml.template .claude/config.yaml
```

#### 2.3 Migrate Settings

**BMAD v4 Config:**
```yaml
# ~/.bmad/config.yml
version: 4.0
default_agent: alex
timeout: 120
testing:
  framework: jest
  coverage_threshold: 80
```

**BMAD Enhanced Config:**
```yaml
# .claude/config.yaml
version: 2.0
defaults:
  subagent: alex
  timeout_sec: 120
  depth: comprehensive

testing:
  frameworks:
    jest:
      enabled: true
      adapter: adapters.jest_adapter.JestAdapter
      command: ["npm", "test"]
  coverage_threshold: 80

guardrails:
  test_coverage_min: 80
  complexity_max: 70
  block_sensitive_files: true

quality_gates:
  enabled: true
  thresholds:
    overall: 60
    critical: 80
```

**Migration Script:**
```bash
# Run automated migration (if available)
python scripts/migrate-config.py --from ~/.bmad/config.yml --to .claude/config.yaml
```

---

### Step 3: Migrate Task Specifications (30 minutes)

#### 3.1 Copy Task Files
```bash
# Copy all tasks
cp -r ~/.bmad/tasks/* .claude/tasks/
```

#### 3.2 Update Task Format

**BMAD v4 Task Format:**
```markdown
# Task: Add User Authentication

## Description
Add JWT-based authentication to the API.

## Requirements
- User login endpoint
- Token validation middleware
- Password hashing

## Acceptance Criteria
- Users can log in with email/password
- Tokens expire after 24 hours
```

**BMAD Enhanced Task Format (Enhanced):**
```markdown
---
task_id: task-001
title: Add User Authentication
status: ready
priority: high
complexity: medium
estimated_hours: 8
---

# Task: Add User Authentication

## Description
Add JWT-based authentication to the API.

## Requirements
- User login endpoint
- Token validation middleware
- Password hashing with bcrypt

## Acceptance Criteria
- [ ] Users can log in with email/password
- [ ] Tokens expire after 24 hours
- [ ] Password reset functionality
- [ ] Test coverage ≥ 80%

## Technical Approach
### Implementation Plan
1. Set up JWT library
2. Create user model with password field
3. Implement login endpoint
4. Add authentication middleware
5. Write comprehensive tests

### Files to Modify
- `src/api/auth.js`
- `src/middleware/auth.js`
- `src/models/User.js`
- `tests/auth.test.js`

## Dependencies
- jsonwebtoken@9.0.0
- bcrypt@5.1.0

## Testing Strategy
- Unit tests for auth functions
- Integration tests for login flow
- Security testing for token validation
```

#### 3.3 Batch Update Script
```python
# scripts/migrate-tasks.py
import os
import yaml
from pathlib import Path

def migrate_task(v4_task_path, enhanced_task_path):
    """Migrate single task from v4 to Enhanced format"""
    with open(v4_task_path) as f:
        content = f.read()

    # Extract title
    title = content.split('\n')[0].replace('# Task: ', '')

    # Add YAML frontmatter
    frontmatter = f"""---
task_id: {Path(enhanced_task_path).stem}
title: {title}
status: ready
priority: medium
complexity: medium
---

"""

    # Write migrated task
    with open(enhanced_task_path, 'w') as f:
        f.write(frontmatter + content)

# Migrate all tasks
for v4_task in Path('~/.bmad/tasks').expanduser().glob('*.md'):
    enhanced_task = Path('.claude/tasks') / v4_task.name
    migrate_task(v4_task, enhanced_task)
    print(f"Migrated: {v4_task.name}")
```

---

### Step 4: Migrate Custom Skills (45 minutes)

#### 4.1 Identify Custom Skills
```bash
# List BMAD v4 custom skills
ls ~/.bmad/skills/
```

#### 4.2 Update Skill Format

**BMAD v4 Skill:**
```markdown
# Skill: custom-deploy

## Description
Deploy application to staging

## Commands
bmad deploy --env staging
```

**BMAD Enhanced Skill:**
```markdown
---
name: custom-deploy
description: Deploy application to staging environment
version: 2.0
category: deployment
inputs:
  - name: environment
    type: string
    required: true
outputs:
  - name: deployment_url
    type: string
---

# Skill: custom-deploy

## Workflow Steps

### 1. Pre-deployment Validation
**Command:** `./scripts/validate-deployment.sh`
**Acceptance:** Exit code 0, all checks pass

### 2. Build Application
**Command:** `npm run build`
**Acceptance:** Build succeeds, dist/ directory created

### 3. Deploy to Environment
**Command:** `./scripts/deploy.sh --env ${environment}`
**Acceptance:** Deployment succeeds, health check passes

### 4. Post-deployment Verification
**Command:** `./scripts/verify-deployment.sh --url ${deployment_url}`
**Acceptance:** All smoke tests pass

## Error Handling
- Build failure → Abort deployment
- Deployment failure → Rollback to previous version
- Verification failure → Alert on-call engineer

## Telemetry
```json
{
  "command": "custom-deploy",
  "environment": "${environment}",
  "duration_ms": 0,
  "success": true
}
```
```

#### 4.3 Place in Correct Location
```bash
# Custom skills go in appropriate category
mkdir -p .claude/skills/deployment/custom-deploy/
cp custom-deploy.md .claude/skills/deployment/custom-deploy/SKILL.md
```

---

### Step 5: Update Command Invocations (30 minutes)

#### 5.1 Command Mapping Reference

| BMAD v4 | BMAD Enhanced | Notes |
|---------|---------------|-------|
| `bmad plan <task>` | `/alex *create-task-spec <file>` | New format with YAML frontmatter |
| `bmad implement <spec>` | `/james *implement <spec>` | Enhanced with guardrails |
| `bmad test` | `/james *test --scope=unit` | Multiple test scopes available |
| `bmad review <file>` | `/quinn *review-code <file>` | Enhanced quality metrics |
| `bmad deploy <env>` | Custom skill or orchestrator | Use workflow orchestration |

#### 5.2 Update Scripts

**Before (BMAD v4):**
```bash
#!/bin/bash
# deploy.sh
bmad plan --task "Deploy to staging"
bmad implement --spec deploy-plan.md
bmad test
bmad deploy --env staging
```

**After (BMAD Enhanced):**
```bash
#!/bin/bash
# deploy.sh
/alex *create-task-spec docs/deploy-requirements.md
/james *implement .claude/tasks/task-001-spec.md
/james *test --scope=all
/orchestrator *workflow deploy-staging --env staging
```

#### 5.3 Update CI/CD Pipelines

**Before (GitHub Actions with BMAD v4):**
```yaml
# .github/workflows/ci.yml
- name: Run BMAD Tests
  run: bmad test
```

**After (GitHub Actions with BMAD Enhanced):**
```yaml
# .github/workflows/ci.yml
- name: Run BMAD Enhanced Tests
  run: |
    source venv/bin/activate
    /james *test --scope=all --coverage
    /quinn *validate-quality-gate
```

---

### Step 6: Migrate Team Workflows (30 minutes)

#### 6.1 Update Documentation

**Before:**
```markdown
# Team Workflow

1. Create task: `bmad plan --task "Feature name"`
2. Implement: `bmad implement task.md`
3. Test: `bmad test`
4. Review: `bmad review`
```

**After:**
```markdown
# Team Workflow

1. **Planning**: `/alex *create-task-spec requirements.md`
2. **Implementation**: `/james *implement task-spec.md`
3. **Testing**: `/james *test --scope=all --coverage`
4. **Quality Review**: `/quinn *review-code --focus=all`
5. **Architecture Review**: `/winston *review-architecture docs/architecture.md`

See [WORKFLOW-GUIDE.md](docs/WORKFLOW-GUIDE.md) for details.
```

#### 6.2 Create Quick Reference

```bash
# Create quick reference card
cat > .claude/QUICK-REFERENCE.md << 'EOF'
# BMAD Enhanced Quick Reference

## Common Commands

### Planning (Alex)
- Create task spec: `/alex *create-task-spec <requirements-file>`
- Break down epic: `/alex *breakdown-epic <epic-file>`
- Estimate story: `/alex *estimate <story-file>`

### Development (James)
- Implement feature: `/james *implement <task-spec>`
- Run tests: `/james *test --scope=all`
- Debug issue: `/james *debug <issue-description>`
- Refactor code: `/james *refactor <file> --focus=<area>`

### Quality (Quinn)
- Review code: `/quinn *review-code <path>`
- Validate quality gate: `/quinn *validate-quality-gate`
- Assess NFRs: `/quinn *assess-nfrs <requirements-file>`

### Architecture (Winston)
- Design architecture: `/winston *design-architecture <requirements>`
- Analyze codebase: `/winston *analyze-architecture .`
- Review architecture: `/winston *review-architecture <arch-file>`

## Interactive Tools

- Command wizard: `python .claude/skills/bmad-commands/scripts/bmad-wizard.py`
- Progress tracker: Automatic in workflows
- Error help: Built into all commands

EOF
```

---

### Step 7: Test Migration (30 minutes)

#### 7.1 Run Validation Script
```bash
# Validate migration
python scripts/validate-migration.py

# Expected output:
# ✓ Configuration valid
# ✓ All tasks migrated
# ✓ Custom skills accessible
# ✓ Commands working
# ✓ Subagents operational
```

#### 7.2 Test Each Subagent
```bash
# Test Alex (Planner)
/alex *create-task-spec docs/sample-requirement.md

# Test James (Developer)
/james *test --scope=unit

# Test Quinn (Quality)
/quinn *review-code src/

# Test Winston (Architect)
/winston *analyze-architecture .

# Test Orchestrator
/orchestrator *workflow document-codebase .
```

#### 7.3 Verify Custom Skills
```bash
# List skills
ls .claude/skills/deployment/

# Test custom skill
/orchestrator *execute-skill deployment/custom-deploy --environment=staging
```

---

## Command Mapping

Complete mapping of BMAD v4 to BMAD Enhanced commands:

### Planning Commands

| BMAD v4 | BMAD Enhanced | Changes |
|---------|---------------|---------|
| `bmad plan --task "..."` | `/alex *create-task-spec <file>` | Requires requirements file |
| `bmad estimate <task>` | `/alex *estimate <story-file>` | Enhanced estimation with complexity |
| `bmad breakdown <epic>` | `/alex *breakdown-epic <epic-file>` | Automatic subtask generation |
| N/A | `/alex *refine-story <story-file>` | New: Story refinement |
| N/A | `/alex *plan-sprint <backlog-file>` | New: Sprint planning |

### Implementation Commands

| BMAD v4 | BMAD Enhanced | Changes |
|---------|---------------|---------|
| `bmad implement <spec>` | `/james *implement <task-spec>` | Enhanced with guardrails |
| `bmad fix <issue>` | `/james *fix <issue-description>` | Intelligent routing |
| `bmad refactor <file>` | `/james *refactor <file>` | Focus areas available |
| `bmad test` | `/james *test --scope=all` | Multiple scopes: unit, integration, e2e |
| N/A | `/james *debug <issue>` | New: Debugging workflow |
| N/A | `/james *apply-qa-fixes <review-file>` | New: Apply QA feedback |
| N/A | `/james *explain <file>` | New: Code explanation |

### Quality Commands

| BMAD v4 | BMAD Enhanced | Changes |
|---------|---------------|---------|
| `bmad review <file>` | `/quinn *review-code <path>` | Comprehensive quality review |
| N/A | `/quinn *validate-quality-gate` | New: Quality gate validation |
| N/A | `/quinn *assess-nfrs <requirements>` | New: NFR assessment |
| N/A | `/quinn *trace-requirements <spec>` | New: Requirements tracing |
| N/A | `/quinn *assess-risk <component>` | New: Risk assessment |

### Architecture Commands (New in Enhanced)

| BMAD v4 | BMAD Enhanced | Description |
|---------|---------------|-------------|
| N/A | `/winston *design-architecture <requirements>` | Design system architecture |
| N/A | `/winston *analyze-architecture <path>` | Analyze existing codebase |
| N/A | `/winston *review-architecture <arch-file>` | Peer review architecture |
| N/A | `/winston *create-adr <decision>` | Create Architecture Decision Record |

### Workflow Orchestration (New in Enhanced)

| BMAD v4 | BMAD Enhanced | Description |
|---------|---------------|-------------|
| N/A | `/orchestrator *workflow document-codebase .` | Complete documentation workflow |
| N/A | `/orchestrator *workflow implement-feature <spec>` | End-to-end feature implementation |
| N/A | `/orchestrator *coordinate <multi-step-task>` | Coordinate across subagents |

---

## Configuration Migration

### Environment Variables

**BMAD v4:**
```bash
export BMAD_HOME=~/.bmad
export BMAD_AGENT=alex
export BMAD_TIMEOUT=120
```

**BMAD Enhanced:**
```bash
export CLAUDE_HOME="$HOME/Documents/BMAD Enhanced"
export BMAD_DEFAULT_SUBAGENT=alex
export BMAD_TIMEOUT_SEC=120
export BMAD_LOG_LEVEL=INFO
```

### Configuration File Sections

#### Testing Configuration
```yaml
# BMAD Enhanced: .claude/config.yaml
testing:
  frameworks:
    jest:
      enabled: true
      adapter: adapters.jest_adapter.JestAdapter
      command: ["npm", "test", "--", "--json"]
    pytest:
      enabled: true
      adapter: adapters.pytest_adapter.PytestAdapter
      command: ["pytest", "--json-report"]
  coverage_threshold: 80
  auto_detect: true
```

#### Guardrails Configuration (New)
```yaml
guardrails:
  enabled: true
  test_coverage_min: 60
  complexity_max: 70
  block_sensitive_files: true
  sensitive_patterns:
    - "*.env"
    - "credentials.json"
    - "*.key"
    - "*.pem"
```

#### Quality Gates Configuration (New)
```yaml
quality_gates:
  enabled: true
  thresholds:
    overall: 60
    critical: 80
  dimensions:
    functionality: 70
    reliability: 80
    performance: 60
    security: 90
    maintainability: 70
    testability: 75
```

---

## Skill Migration

### Converting BMAD v4 Skills to Enhanced Format

#### Step 1: Add YAML Frontmatter
```yaml
---
name: skill-name
description: Brief description
version: 2.0
category: development|planning|quality|architecture
complexity: simple|standard|complex
inputs:
  - name: input_name
    type: string|file|boolean|integer
    required: true|false
    description: Input description
outputs:
  - name: output_name
    type: string|json|file
    description: Output description
telemetry:
  command: skill-name
  track_duration: true
  track_success: true
---
```

#### Step 2: Structure Workflow Steps
```markdown
## Workflow Steps

### Step 1: [Step Name]
**Command:** `command to execute`
**Acceptance:** Success criteria
**Error Handling:** What to do on failure

### Step 2: [Next Step]
...
```

#### Step 3: Add References Directory
```bash
.claude/skills/category/skill-name/
├── SKILL.md              # Main skill definition
└── references/
    ├── examples.md       # Usage examples
    ├── patterns.md       # Common patterns
    └── troubleshooting.md # Known issues
```

---

## Testing Your Migration

### Automated Testing

```bash
# Run migration test suite
python scripts/test-migration.py --comprehensive

# Test specific areas
python scripts/test-migration.py --area=config
python scripts/test-migration.py --area=tasks
python scripts/test-migration.py --area=skills
```

### Manual Testing Checklist

#### Configuration
- [ ] Config file loads without errors
- [ ] All subagents are enabled
- [ ] Test frameworks detected correctly
- [ ] Guardrails configured properly
- [ ] Logging works as expected

#### Commands
- [ ] `/alex *create-task-spec` works
- [ ] `/james *implement` executes
- [ ] `/james *test` runs tests
- [ ] `/quinn *review-code` generates report
- [ ] `/winston *analyze-architecture` completes

#### Custom Skills
- [ ] Custom skills listed correctly
- [ ] Custom skills execute without errors
- [ ] Custom skill outputs match expectations

#### Workflows
- [ ] Complete feature implementation workflow
- [ ] Quality review workflow
- [ ] Documentation workflow
- [ ] Custom workflows execute correctly

### Performance Testing

```bash
# Benchmark commands
time /alex *create-task-spec sample-requirement.md
# Target: < 5 seconds

time /james *test --scope=unit
# Target: Depends on test suite size

time /winston *analyze-architecture .
# Target: < 2 minutes for typical codebase
```

---

## Rollback Plan

If you encounter issues during migration:

### Immediate Rollback (< 1 hour)

1. **Revert to BMAD v4**
```bash
# BMAD v4 is still intact in original location
cd ~/.bmad
bmad --version  # Verify v4 still works
```

2. **Restore Configuration**
```bash
cp ~/.bmad/config.yml.backup ~/.bmad/config.yml
```

3. **Notify Team**
```bash
# Send notification
echo "Rolled back to BMAD v4 due to [reason]" | mail -s "BMAD Rollback" team@example.com
```

### Gradual Rollback (Hybrid Mode)

Run both systems in parallel:

```bash
# Use BMAD v4 for critical operations
alias bmad='/path/to/bmad-v4/bmad'

# Use BMAD Enhanced for new features
alias bmad-enhanced='cd ~/Documents/BMAD\ Enhanced && /alex'
```

### Data Recovery

```bash
# Restore tasks from backup
cp ~/.bmad/tasks/*.md.backup ~/.bmad/tasks/

# Restore custom skills
cp -r ~/.bmad/skills.backup/* ~/.bmad/skills/
```

---

## FAQ

### General Questions

**Q: Can I run BMAD v4 and BMAD Enhanced side by side?**
A: Yes! They use different directories (`.bmad/` vs `.claude/`), so they don't interfere with each other.

**Q: How long does migration take?**
A: 2-4 hours for typical setups. Complex custom configurations may take longer.

**Q: Will my BMAD v4 tasks work in Enhanced?**
A: Basic tasks work, but you'll get better results by migrating to the enhanced format with YAML frontmatter.

**Q: Do I need to rewrite all my custom skills?**
A: No, but converting them to the new format enables advanced features like intelligent routing and guardrails.

### Configuration Questions

**Q: Where is the configuration file now?**
A: `.claude/config.yaml` (was `.bmad/config.yml` in v4)

**Q: Can I import my v4 config automatically?**
A: Yes, use: `python scripts/migrate-config.py --from ~/.bmad/config.yml --to .claude/config.yaml`

**Q: What if I have custom configuration sections?**
A: Place them under a `custom:` section in `.claude/config.yaml`.

### Command Questions

**Q: Why did command syntax change?**
A: The new syntax (`/subagent *skill`) makes routing explicit and enables better error messages and documentation.

**Q: Are there aliases for old commands?**
A: Not built-in, but you can create shell aliases:
```bash
# ~/.bashrc
alias bmad-plan='/alex *create-task-spec'
alias bmad-implement='/james *implement'
```

**Q: Can I use old command syntax?**
A: Limited backward compatibility exists, but we recommend migrating to new syntax.

### Feature Questions

**Q: What happened to the `bmad deploy` command?**
A: Use workflow orchestration: `/orchestrator *workflow deploy-staging` or create a custom deployment skill.

**Q: Are all BMAD v4 features available?**
A: Yes, plus many new ones. See [V2-ARCHITECTURE.md](V2-ARCHITECTURE.md) for the complete feature list.

**Q: How do I use the new UX tools?**
A: Run `python .claude/skills/bmad-commands/scripts/bmad-wizard.py` for the interactive wizard, or see [docs/UX-IMPROVEMENTS-GUIDE.md](UX-IMPROVEMENTS-GUIDE.md).

---

## Migration Support

### Resources

- **Documentation**: [docs/](/home/adolfo/Documents/BMAD%20Enhanced/docs/)
- **Quick Start**: [docs/QUICK-START.md](/home/adolfo/Documents/BMAD%20Enhanced/docs/QUICK-START.md)
- **Architecture**: [docs/V2-ARCHITECTURE.md](/home/adolfo/Documents/BMAD%20Enhanced/docs/V2-ARCHITECTURE.md)
- **Troubleshooting**: [docs/TROUBLESHOOTING.md](/home/adolfo/Documents/BMAD%20Enhanced/docs/TROUBLESHOOTING.md)
- **Examples**: [docs/EXAMPLE-WORKFLOWS.md](/home/adolfo/Documents/BMAD%20Enhanced/docs/EXAMPLE-WORKFLOWS.md)

### Getting Help

1. **Check Documentation**: Start with [TROUBLESHOOTING.md](/home/adolfo/Documents/BMAD%20Enhanced/docs/TROUBLESHOOTING.md)
2. **Run Diagnostics**: `python scripts/diagnose.py`
3. **Check Logs**: `.claude/logs/errors.log`
4. **Community Support**: GitHub Issues
5. **Professional Support**: Contact your BMAD representative

---

## Post-Migration Checklist

After successful migration:

- [ ] Update team documentation with new commands
- [ ] Conduct team training session on BMAD Enhanced
- [ ] Update CI/CD pipelines
- [ ] Archive BMAD v4 backup
- [ ] Monitor system for 1 week
- [ ] Collect team feedback
- [ ] Document any custom workflows
- [ ] Share migration experience with community

---

## Success Metrics

Track these metrics to measure migration success:

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Command Execution Time | < 10% increase | Compare before/after benchmarks |
| Error Rate | < 5% | Monitor `.claude/logs/errors.log` |
| Team Adoption | > 80% in 2 weeks | Survey team usage |
| Quality Score | > v4 baseline | Use `/quinn *validate-quality-gate` |
| Developer Satisfaction | > 4/5 | Post-migration survey |

---

## Conclusion

Congratulations on migrating to BMAD Enhanced! You now have access to:

- 🏗️ **Better Architecture**: 3-layer design with intelligent routing
- 🤖 **More Subagents**: 10 specialized subagents vs 4 in v4
- ✨ **New Capabilities**: Architecture design, quality gates, workflow orchestration
- 🎯 **Better DX**: Comprehensive docs, interactive tools, structured errors
- 🚀 **Production Ready**: Battle-tested with 100% test coverage

**Next Steps:**
1. Read [QUICK-START.md](/home/adolfo/Documents/BMAD%20Enhanced/docs/QUICK-START.md)
2. Try [EXAMPLE-WORKFLOWS.md](/home/adolfo/Documents/BMAD%20Enhanced/docs/EXAMPLE-WORKFLOWS.md)
3. Explore [V2-ARCHITECTURE.md](/home/adolfo/Documents/BMAD%20Enhanced/docs/V2-ARCHITECTURE.md)
4. Join the community and share your experience!

---

**Version History:**

| Version | Date | Changes |
|---------|------|---------|
| 2.0 | 2025-11-05 | Initial migration guide for BMAD Enhanced v2 |

**Maintained by:** BMAD Enhanced Development Team
