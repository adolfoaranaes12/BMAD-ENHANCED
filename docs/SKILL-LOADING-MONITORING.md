# BMAD Enhanced - Skill Loading & Monitoring Guide

**Version:** 1.0
**Last Updated:** 2025-11-05
**Status:** Production Ready

## Overview

This guide explains how to monitor skill loading in BMAD Enhanced and diagnose issues. No more treating skill loading as "divine benevolence" – you now have complete visibility and control.

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [Monitoring Tools](#monitoring-tools)
3. [Understanding Skill Loading](#understanding-skill-loading)
4. [Common Issues](#common-issues)
5. [Diagnostics & Troubleshooting](#diagnostics--troubleshooting)
6. [Skill Validation](#skill-validation)
7. [CI/CD Integration](#cicd-integration)

---

## Quick Start

### Check All Skills (30 seconds)

```bash
# Monitor all skills
python .claude/skills/bmad-commands/scripts/monitor-skills.py

# Expected output:
# 🔍 Discovering skills in .claude/skills...
# 📁 Found 32 skill definition files
#
# ======================================================================
# 📊 SKILL LOADING SUMMARY
# ======================================================================
#
# Total Skills Discovered:  32
# Valid Skills:             32 ✅
# Invalid Skills:           0 ✅
# With YAML Frontmatter:    32
# Categories:               6
```

### Quick Validation

```bash
# Validate only (exit 0 if all valid, 1 if any invalid)
python .claude/skills/bmad-commands/scripts/monitor-skills.py --validate-only

# Good for CI/CD
if python .claude/skills/bmad-commands/scripts/monitor-skills.py --validate-only; then
    echo "✅ All skills valid"
else
    echo "❌ Some skills invalid"
    exit 1
fi
```

### Check Specific Skill

```bash
# Get details for a specific skill
python .claude/skills/bmad-commands/scripts/monitor-skills.py --skill implement-feature

# Output:
# 📋 Skill Details: implement-feature
# Category:     development
# Path:         .claude/skills/development/implement-feature/SKILL.md
# Valid:        ✅ Yes
# Frontmatter:  ✅ Yes
# Size:         10.1 KB
# Lines:        369
```

---

## Monitoring Tools

### 1. Skill Monitor Script

**Location:** `.claude/skills/bmad-commands/scripts/monitor-skills.py`

**Features:**
- ✅ Discovers all skills automatically
- ✅ Validates frontmatter and structure
- ✅ Reports errors with specific details
- ✅ Organizes skills by category
- ✅ Provides statistics
- ✅ Exports to JSON for automation

**Usage:**

```bash
# Full monitoring report
python .claude/skills/bmad-commands/scripts/monitor-skills.py

# Filter by category
python .claude/skills/bmad-commands/scripts/monitor-skills.py --category planning

# Export to JSON
python .claude/skills/bmad-commands/scripts/monitor-skills.py --json skills-status.json

# Check specific skill
python .claude/skills/bmad-commands/scripts/monitor-skills.py --skill create-task-spec
```

---

### 2. Manual Verification

Check skills exist and are readable:

```bash
# Count skills
find .claude/skills -name "SKILL.md" | wc -l
# Should show: 32

# List all skills
find .claude/skills -name "SKILL.md" -type f

# Check specific skill
cat .claude/skills/development/implement-feature/SKILL.md | head -20
```

---

### 3. Watch Mode (Continuous Monitoring)

Monitor skills during development:

```bash
# Watch for changes (requires entr or watch)
find .claude/skills -name "SKILL.md" | entr -c python .claude/skills/bmad-commands/scripts/monitor-skills.py

# Or use watch (runs every 2 seconds)
watch -n 2 python .claude/skills/bmad-commands/scripts/monitor-skills.py --validate-only
```

---

## Understanding Skill Loading

### Skill File Structure

Skills are loaded from:
```
.claude/skills/
├── planning/
│   ├── create-task-spec/
│   │   └── SKILL.md          ← Skill definition
│   ├── breakdown-epic/
│   │   └── SKILL.md
│   └── ...
├── development/
│   ├── implement-feature/
│   │   └── SKILL.md
│   └── ...
├── quality/
│   └── ...
└── ...
```

### Required Skill Structure

Each `SKILL.md` must have:

```markdown
---
name: skill-name
description: Brief description
category: planning|development|quality|architecture|brownfield|implementation
version: 1.0
inputs:
  - name: input_name
    type: string|file|boolean
    required: true|false
outputs:
  - name: output_name
    type: string|file|json
---

# Skill: skill-name

## Workflow Steps

### Step 1: [Step Name]
...
```

### Loading Process

1. **Discovery**: System scans `.claude/skills/` for `SKILL.md` files
2. **Parsing**: Each skill file is parsed for YAML frontmatter
3. **Validation**: Frontmatter is validated for required fields
4. **Registration**: Valid skills are registered by category and name
5. **Routing**: Skills become available for subagent routing

---

## Common Issues

### Issue 1: Missing Category Field

**Symptoms:**
```
❌ implement-feature              ( 369 lines,   10.1 KB)
    ⚠️  Missing required field: category
```

**Cause:** Skill frontmatter missing `category` field

**Fix:**
```yaml
---
name: implement-feature
description: Implement feature from task specification
category: development  # ← ADD THIS
version: 1.0
...
---
```

**Required categories:**
- `planning` - For Alex (Planner)
- `development` - For James (Developer)
- `quality` - For Quinn (Quality)
- `architecture` - For Winston (Architect)
- `brownfield` - For brownfield workflows
- `implementation` - For Orchestrator

---

### Issue 2: No Workflow Steps Section

**Symptoms:**
```
❌ document-project               ( 453 lines,   14.6 KB)
    ⚠️  No workflow steps section found
```

**Cause:** Skill missing workflow steps section

**Fix:**
```markdown
# Skill: document-project

## Description
[Description here]

## Workflow Steps  # ← ADD THIS SECTION

### Step 1: [Step Name]
**Command:** `command here`
**Acceptance:** Success criteria

### Step 2: [Next Step]
...
```

---

### Issue 3: Invalid YAML Frontmatter

**Symptoms:**
```
❌ skill-name
    ⚠️  Invalid YAML frontmatter: expected <block end>, but found ','
```

**Cause:** YAML syntax error (indentation, quotes, etc.)

**Fix:**
```yaml
# Bad YAML (comma in wrong place)
---
name: skill-name,
description: desc
---

# Good YAML
---
name: skill-name
description: desc
---
```

**Common YAML issues:**
- Wrong indentation (use 2 spaces, not tabs)
- Missing quotes around strings with colons
- Trailing commas
- Missing closing quotes

---

### Issue 4: Skill File Not Found

**Symptoms:**
```
📁 Found 0 skill definition files
❌ No skills found!
```

**Cause:** Running from wrong directory or skills not installed

**Fix:**
```bash
# Check current directory
pwd
# Should be in project root with .claude/ directory

# Verify .claude/skills exists
ls -la .claude/skills

# If missing, you may need to clone/install properly
```

---

## Diagnostics & Troubleshooting

### Full System Diagnostic

```bash
# Run comprehensive diagnostic
cat > /tmp/diagnostic.sh << 'EOF'
#!/bin/bash

echo "=== BMAD Enhanced Skill Loading Diagnostic ==="
echo ""

echo "1. Current Directory:"
pwd
echo ""

echo "2. Skills Directory Exists:"
[ -d .claude/skills ] && echo "✅ Yes" || echo "❌ No"
echo ""

echo "3. Skill Count:"
find .claude/skills -name "SKILL.md" 2>/dev/null | wc -l
echo ""

echo "4. Skills by Category:"
for cat in planning development quality architecture brownfield implementation; do
    count=$(find .claude/skills/$cat -name "SKILL.md" 2>/dev/null | wc -l)
    echo "  $cat: $count skills"
done
echo ""

echo "5. Skill Validation:"
python .claude/skills/bmad-commands/scripts/monitor-skills.py --validate-only
echo ""

echo "6. Python Environment:"
which python3
python3 --version
echo ""

echo "7. Required Python Packages:"
python3 -c "import yaml; print('✅ yaml')" 2>/dev/null || echo "❌ yaml (install: pip install pyyaml)"
echo ""

echo "8. Disk Space:"
df -h .claude/ | tail -1
echo ""

echo "=== End Diagnostic ==="
EOF

chmod +x /tmp/diagnostic.sh
/tmp/diagnostic.sh
```

---

### Quick Health Check

```bash
# Create quick health check script
cat > .claude/skills/bmad-commands/scripts/health-check.sh << 'EOF'
#!/bin/bash

# Quick health check for BMAD Enhanced skills

echo "🏥 BMAD Enhanced Health Check"
echo ""

# Check skills directory
if [ ! -d .claude/skills ]; then
    echo "❌ CRITICAL: .claude/skills directory not found"
    exit 1
fi

# Count skills
SKILL_COUNT=$(find .claude/skills -name "SKILL.md" 2>/dev/null | wc -l)
echo "📁 Skills found: $SKILL_COUNT"

if [ $SKILL_COUNT -lt 30 ]; then
    echo "⚠️  WARNING: Expected ~32 skills, found $SKILL_COUNT"
fi

# Validate skills
if python .claude/skills/bmad-commands/scripts/monitor-skills.py --validate-only > /dev/null 2>&1; then
    echo "✅ All skills valid"
else
    echo "❌ Some skills invalid - run 'python .claude/skills/bmad-commands/scripts/monitor-skills.py' for details"
    exit 1
fi

echo ""
echo "✅ Health check passed!"
EOF

chmod +x .claude/skills/bmad-commands/scripts/health-check.sh
./.claude/skills/bmad-commands/scripts/health-check.sh
```

---

## Skill Validation

### Validation Checklist

For each skill, validation checks:

- [x] **File exists** - SKILL.md file present
- [x] **Readable** - File can be read
- [x] **YAML frontmatter** - Starts with `---` markers
- [x] **Valid YAML** - Frontmatter parses correctly
- [x] **Required fields** - Has `name`, `description`, `category`
- [x] **Workflow section** - Contains "## Workflow Steps"
- [x] **Reasonable size** - Not empty, not corrupted

### Manual Validation

Validate a single skill manually:

```bash
SKILL_FILE=".claude/skills/development/implement-feature/SKILL.md"

# Check file exists
[ -f "$SKILL_FILE" ] && echo "✅ File exists" || echo "❌ File not found"

# Check frontmatter
if head -1 "$SKILL_FILE" | grep -q "^---"; then
    echo "✅ Has frontmatter"
else
    echo "❌ No frontmatter"
fi

# Extract and validate YAML
python3 << EOF
import yaml
content = open("$SKILL_FILE").read()
if content.startswith("---"):
    fm = content.split("---")[1]
    try:
        data = yaml.safe_load(fm)
        print("✅ Valid YAML")
        print(f"   Name: {data.get('name', 'MISSING')}")
        print(f"   Category: {data.get('category', 'MISSING')}")
    except Exception as e:
        print(f"❌ Invalid YAML: {e}")
EOF

# Check workflow section
if grep -q "## Workflow" "$SKILL_FILE"; then
    echo "✅ Has workflow section"
else
    echo "❌ No workflow section"
fi
```

---

### Automated Validation in Git Hooks

Add validation to pre-commit hook:

```bash
# .git/hooks/pre-commit
#!/bin/bash

# Validate skills before committing
if ! python .claude/skills/bmad-commands/scripts/monitor-skills.py --validate-only; then
    echo ""
    echo "❌ Skill validation failed. Fix errors before committing."
    echo "Run: python .claude/skills/bmad-commands/scripts/monitor-skills.py"
    exit 1
fi

echo "✅ Skill validation passed"
```

Make it executable:
```bash
chmod +x .git/hooks/pre-commit
```

---

## CI/CD Integration

### GitHub Actions

```yaml
# .github/workflows/validate-skills.yml
name: Validate Skills

on:
  push:
    paths:
      - '.claude/skills/**'
  pull_request:
    paths:
      - '.claude/skills/**'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install pyyaml

      - name: Validate skills
        run: |
          python .claude/skills/bmad-commands/scripts/monitor-skills.py --validate-only
          python .claude/skills/bmad-commands/scripts/monitor-skills.py --json skills-status.json

      - name: Upload skill status
        uses: actions/upload-artifact@v3
        with:
          name: skills-status
          path: skills-status.json
```

---

### GitLab CI

```yaml
# .gitlab-ci.yml
validate-skills:
  stage: test
  image: python:3.11
  before_script:
    - pip install pyyaml
  script:
    - python .claude/skills/bmad-commands/scripts/monitor-skills.py --validate-only
    - python .claude/skills/bmad-commands/scripts/monitor-skills.py --json skills-status.json
  artifacts:
    paths:
      - skills-status.json
    expire_in: 1 week
  only:
    changes:
      - .claude/skills/**
```

---

### Jenkins

```groovy
// Jenkinsfile
stage('Validate Skills') {
    steps {
        sh '''
            pip install pyyaml
            python .claude/skills/bmad-commands/scripts/monitor-skills.py --validate-only
            python .claude/skills/bmad-commands/scripts/monitor-skills.py --json skills-status.json
        '''
        archiveArtifacts artifacts: 'skills-status.json', fingerprint: true
    }
}
```

---

## Monitoring Dashboard

### Create Status Dashboard

```bash
# Generate HTML dashboard
cat > scripts/generate-dashboard.py << 'EOF'
#!/usr/bin/env python3
import json
from datetime import datetime

# Run monitor and get JSON
import subprocess
subprocess.run(['python', '.claude/skills/bmad-commands/scripts/monitor-skills.py', '--json', 'skills-status.json'])

# Read JSON
with open('skills-status.json') as f:
    data = json.load(f)

summary = data['summary']
skills = data['skills']

# Generate HTML
html = f"""<!DOCTYPE html>
<html>
<head>
    <title>BMAD Enhanced - Skills Status</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        .summary {{ background: #f0f0f0; padding: 20px; border-radius: 5px; }}
        .valid {{ color: green; }}
        .invalid {{ color: red; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background: #4CAF50; color: white; }}
    </style>
</head>
<body>
    <h1>BMAD Enhanced - Skills Status</h1>
    <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>

    <div class="summary">
        <h2>Summary</h2>
        <p>Total Skills: {summary['total_skills']}</p>
        <p class="valid">Valid Skills: {summary['valid_skills']}</p>
        <p class="invalid">Invalid Skills: {summary['invalid_skills']}</p>
        <p>Categories: {summary['categories']}</p>
    </div>

    <h2>Skills by Category</h2>
    <table>
        <tr>
            <th>Category</th>
            <th>Name</th>
            <th>Status</th>
            <th>Size (KB)</th>
            <th>Lines</th>
        </tr>
"""

for skill in sorted(skills, key=lambda s: (s['category'], s['name'])):
    status = "✅" if skill['valid'] else "❌"
    size_kb = skill['size_bytes'] / 1024
    html += f"""
        <tr>
            <td>{skill['category']}</td>
            <td>{skill['name']}</td>
            <td>{'<span class="valid">' if skill['valid'] else '<span class="invalid">'}{status}</span></td>
            <td>{size_kb:.1f}</td>
            <td>{skill['line_count']}</td>
        </tr>
    """

html += """
    </table>
</body>
</html>
"""

with open('skills-dashboard.html', 'w') as f:
    f.write(html)

print("📊 Dashboard generated: skills-dashboard.html")
EOF

python scripts/generate-dashboard.py
```

Open `skills-dashboard.html` in your browser for a visual dashboard.

---

## Best Practices

### 1. Regular Monitoring

```bash
# Daily check (add to cron)
0 9 * * * cd /path/to/bmad-enhanced && python .claude/skills/bmad-commands/scripts/monitor-skills.py --validate-only
```

### 2. Pre-Deploy Validation

```bash
# Before deploying
./.claude/skills/bmad-commands/scripts/health-check.sh || { echo "Health check failed!"; exit 1; }
```

### 3. Development Workflow

```bash
# After modifying a skill
python .claude/skills/bmad-commands/scripts/monitor-skills.py --skill <skill-name>

# Validate before committing
python .claude/skills/bmad-commands/scripts/monitor-skills.py --validate-only
git add .claude/skills/...
git commit -m "Update skill"
```

### 4. Team Collaboration

```bash
# Share skill status with team
python .claude/skills/bmad-commands/scripts/monitor-skills.py --json skills-status.json
# Commit skills-status.json to repo for visibility
```

---

## FAQ

**Q: How often should I check skill loading?**
A: Daily in development, before each deployment, and in CI/CD pipelines.

**Q: What if a skill shows as invalid but seems to work?**
A: Fix the validation errors anyway - they may cause issues later or in different contexts.

**Q: Can I have custom categories?**
A: Currently, only the predefined categories are supported. Custom categories require code changes.

**Q: How do I know if a skill is being used?**
A: Check telemetry logs (`.claude/logs/telemetry.jsonl`) for skill usage.

**Q: What's the performance impact of many skills?**
A: Minimal - skills are loaded on-demand, not all at once.

---

## Related Documentation

- [V2-ARCHITECTURE.md](/home/adolfo/Documents/BMAD%20Enhanced/docs/V2-ARCHITECTURE.md) - Architecture overview
- [ADVANCED-WORKFLOW-CUSTOMIZATION.md](/home/adolfo/Documents/BMAD%20Enhanced/docs/ADVANCED-WORKFLOW-CUSTOMIZATION.md) - Custom skills
- [TROUBLESHOOTING.md](/home/adolfo/Documents/BMAD%20Enhanced/docs/TROUBLESHOOTING.md) - General troubleshooting
- [PRODUCTION-MONITORING-GUIDE.md](/home/adolfo/Documents/BMAD%20Enhanced/docs/PRODUCTION-MONITORING-GUIDE.md) - Production monitoring

---

**Maintained by:** BMAD Enhanced Development Team
**Last Updated:** 2025-11-05

**No more divine benevolence - you have complete control! 🎯**
