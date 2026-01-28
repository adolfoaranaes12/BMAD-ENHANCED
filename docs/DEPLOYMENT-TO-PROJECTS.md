# BMAD Enhanced - Deployment to Projects Guide

**Version:** 1.0
**Last Updated:** 2025-11-05
**Critical:** Read this before deploying to your projects!

## Overview

This guide explains **exactly what files you need** from BMAD Enhanced when deploying to your projects. Copying only `.claude/` is **insufficient** and will result in missing features.

---

## Table of Contents

1. [TL;DR - Quick Deployment](#tldr---quick-deployment)
2. [What Happens with Only `.claude/`](#what-happens-with-only-claude)
3. [Complete Deployment Options](#complete-deployment-options)
4. [Minimal Deployment Package](#minimal-deployment-package)
5. [Full Repository Deployment](#full-repository-deployment)
6. [Verification Checklist](#verification-checklist)
7. [Project-Specific Customization](#project-specific-customization)

---

## TL;DR - Quick Deployment

### Option 1: Minimal (Recommended for Most Projects)

Copy these essential files:

```bash
# From BMAD Enhanced repository to your project
cp -r .claude/ /path/to/your-project/
cp -r scripts/ /path/to/your-project/
cp docs/QUICK-START.md /path/to/your-project/.claude/
cp docs/quickstart-*.md /path/to/your-project/.claude/docs/
```

### Option 2: Full (Recommended for Complex Projects)

```bash
# Clone/copy entire BMAD Enhanced repository
git clone <bmad-enhanced-repo> /path/to/your-project/.bmad-enhanced
# Or copy the whole folder
cp -r "BMAD Enhanced" /path/to/your-project/.bmad-enhanced
```

---

## What Happens with Only `.claude/`

### ❌ What You're Missing

If you only copy `.claude/`, you lose:

#### 1. **Python Scripts** (`scripts/` directory)
**Impact:** CRITICAL
- ❌ No UX improvements (wizard, progress, error handler)
- ❌ No skill monitoring
- ❌ No health checks
- ❌ No custom primitives
- ❌ No test framework adapters

**Affected Features:**
- Interactive command wizard
- Progress visualization
- Error handling with remediation
- Skill validation
- Test execution with multiple frameworks
- Architecture diagram generation
- Tech stack analysis

#### 2. **Documentation** (`docs/` directory)
**Impact:** HIGH
- ❌ No quickstart guides visible
- ❌ No troubleshooting reference
- ❌ No architecture documentation
- ❌ No migration guides
- ❌ No performance tuning guides

#### 3. **Configuration Templates**
**Impact:** MEDIUM
- ❌ No `.claude/config.yaml.template`
- ❌ Need to create config from scratch

#### 4. **Test Framework Adapters**
**Impact:** HIGH (if using tests)
- ❌ No adapters for Jest, Pytest, JUnit, etc.
- ❌ Tests won't run properly

---

### ✅ What Still Works

With only `.claude/`:
- ✅ Basic skill definitions
- ✅ Subagent routing (but degraded)
- ✅ Simple workflows
- ✅ Slash commands

---

## Complete Deployment Options

### Option 1: Minimal Deployment (5 MB, Essential Features)

**Best for:** Most projects, clean integration

**What to copy:**
```
Your Project/
├── .claude/              ← Copy entire directory
│   ├── agents/
│   ├── commands/
│   ├── config.yaml       ← Copy template and customize
│   ├── skills/
│   └── templates/
├── scripts/              ← Copy entire directory
│   ├── bmad-wizard.py
│   ├── progress-visualizer.py
│   ├── error-handler.py
│   ├── monitor-skills.py
│   ├── health-check.sh
│   └── ... (all scripts)
└── docs/                 ← Copy essential docs only
    ├── QUICK-START.md
    ├── quickstart-alex.md
    ├── quickstart-james.md
    ├── quickstart-quinn.md
    ├── quickstart-winston.md
    ├── TROUBLESHOOTING.md
    └── ERROR-CODES.md
```

**Copy Command:**
```bash
#!/bin/bash
# Deploy BMAD Enhanced (minimal) to project

SOURCE="/home/adolfo/Documents/BMAD Enhanced"
TARGET="/path/to/your-project"

# Copy .claude directory
cp -r "$SOURCE/.claude" "$TARGET/"

# Copy scripts
cp -r "$SOURCE/scripts" "$TARGET/"

# Copy essential docs
mkdir -p "$TARGET/docs"
cp "$SOURCE/docs/QUICK-START.md" "$TARGET/docs/"
cp "$SOURCE/docs/quickstart-"*.md "$TARGET/docs/"
cp "$SOURCE/docs/TROUBLESHOOTING.md" "$TARGET/docs/"
cp "$SOURCE/docs/ERROR-CODES.md" "$TARGET/docs/"
cp "$SOURCE/docs/COMMAND-REFERENCE-SUMMARY.md" "$TARGET/docs/"

# Copy config template
cp "$SOURCE/.claude/config.yaml.template" "$TARGET/.claude/" 2>/dev/null || true

echo "✅ Minimal deployment complete"
echo ""
echo "Next steps:"
echo "1. cd $TARGET"
echo "2. Configure: cp .claude/config.yaml.template .claude/config.yaml"
echo "3. Edit .claude/config.yaml for your project"
echo "4. Run health check: ./.claude/skills/bmad-commands/scripts/health-check.sh"
```

---

### Option 2: Full Deployment (Complete Repository)

**Best for:** Complex projects, full feature access, development

**What to copy:** Everything

**Method 1: Subdirectory**
```bash
# Copy entire BMAD Enhanced to subdirectory
cp -r "BMAD Enhanced" /path/to/your-project/.bmad-enhanced

# Create symlinks in project root
cd /path/to/your-project
ln -s .bmad-enhanced/.claude .claude
ln -s .bmad-enhanced/scripts scripts
ln -s .bmad-enhanced/docs docs
```

**Method 2: Git Submodule**
```bash
cd /path/to/your-project
git submodule add <bmad-enhanced-repo-url> .bmad-enhanced
git submodule update --init

# Create symlinks
ln -s .bmad-enhanced/.claude .claude
ln -s .bmad-enhanced/scripts scripts
ln -s .bmad-enhanced/docs docs
```

**Method 3: Direct Copy**
```bash
# Copy everything (simplest but no updates)
cp -r "BMAD Enhanced" /path/to/your-project/

# Rename to avoid confusion
mv /path/to/your-project/"BMAD Enhanced" /path/to/your-project/.bmad-enhanced
```

---

### Option 3: Smart Deployment Script

Save as `.claude/skills/bmad-commands/scripts/deploy-to-project.sh`:

```bash
#!/bin/bash
# BMAD Enhanced - Smart Deployment Script
# Deploys BMAD Enhanced to target project with validation

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BMAD_ROOT="$(dirname "$SCRIPT_DIR")"

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Usage
usage() {
    echo "Usage: $0 [OPTIONS] <target-project-directory>"
    echo ""
    echo "Options:"
    echo "  --minimal     Deploy minimal package (default)"
    echo "  --full        Deploy full repository"
    echo "  --dry-run     Show what would be copied without copying"
    echo "  --force       Overwrite existing files"
    echo ""
    echo "Examples:"
    echo "  $0 ~/projects/my-app"
    echo "  $0 --full ~/projects/my-app"
    echo "  $0 --dry-run ~/projects/my-app"
    exit 1
}

# Parse arguments
MODE="minimal"
DRY_RUN=false
FORCE=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --minimal)
            MODE="minimal"
            shift
            ;;
        --full)
            MODE="full"
            shift
            ;;
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --force)
            FORCE=true
            shift
            ;;
        --help|-h)
            usage
            ;;
        *)
            TARGET="$1"
            shift
            ;;
    esac
done

# Validate target
if [ -z "$TARGET" ]; then
    echo -e "${RED}Error: Target directory required${NC}"
    usage
fi

if [ ! -d "$TARGET" ]; then
    echo -e "${YELLOW}Target directory doesn't exist. Create it? (y/n)${NC}"
    read -r response
    if [[ "$response" =~ ^[Yy]$ ]]; then
        mkdir -p "$TARGET"
    else
        exit 1
    fi
fi

echo "🚀 BMAD Enhanced Deployment"
echo "=========================="
echo ""
echo "Source: $BMAD_ROOT"
echo "Target: $TARGET"
echo "Mode:   $MODE"
echo "Dry run: $DRY_RUN"
echo ""

# Check if files exist
if [ -d "$TARGET/.claude" ] && [ "$FORCE" != true ]; then
    echo -e "${YELLOW}Warning: .claude directory already exists in target${NC}"
    echo "Use --force to overwrite"
    exit 1
fi

# Deploy function
deploy_file() {
    local src="$1"
    local dst="$2"

    if [ "$DRY_RUN" = true ]; then
        echo "  [DRY RUN] Would copy: $src -> $dst"
        return
    fi

    mkdir -p "$(dirname "$dst")"

    if [ -d "$src" ]; then
        cp -r "$src" "$dst"
    else
        cp "$src" "$dst"
    fi

    echo -e "${GREEN}✅${NC} Copied: $src"
}

# Minimal deployment
deploy_minimal() {
    echo "📦 Deploying minimal package..."
    echo ""

    # .claude directory
    deploy_file "$BMAD_ROOT/.claude" "$TARGET/.claude"

    # scripts directory
    deploy_file "$BMAD_ROOT/scripts" "$TARGET/scripts"

    # Essential docs
    mkdir -p "$TARGET/docs"
    deploy_file "$BMAD_ROOT/docs/QUICK-START.md" "$TARGET/docs/QUICK-START.md"
    for file in "$BMAD_ROOT/docs/quickstart-"*.md; do
        deploy_file "$file" "$TARGET/docs/$(basename "$file")"
    done
    deploy_file "$BMAD_ROOT/docs/TROUBLESHOOTING.md" "$TARGET/docs/TROUBLESHOOTING.md"
    deploy_file "$BMAD_ROOT/docs/ERROR-CODES.md" "$TARGET/docs/ERROR-CODES.md"
    deploy_file "$BMAD_ROOT/docs/COMMAND-REFERENCE-SUMMARY.md" "$TARGET/docs/COMMAND-REFERENCE-SUMMARY.md"

    # Config template
    if [ -f "$BMAD_ROOT/.claude/config.yaml.template" ]; then
        deploy_file "$BMAD_ROOT/.claude/config.yaml.template" "$TARGET/.claude/config.yaml.template"
    fi
}

# Full deployment
deploy_full() {
    echo "📦 Deploying full repository..."
    echo ""

    deploy_file "$BMAD_ROOT/.claude" "$TARGET/.bmad-enhanced/.claude"
    deploy_file "$BMAD_ROOT/scripts" "$TARGET/.bmad-enhanced/scripts"
    deploy_file "$BMAD_ROOT/docs" "$TARGET/.bmad-enhanced/docs"

    # Create symlinks
    if [ "$DRY_RUN" != true ]; then
        cd "$TARGET"
        ln -sf .bmad-enhanced/.claude .claude
        ln -sf .bmad-enhanced/scripts scripts
        ln -sf .bmad-enhanced/docs docs
        echo -e "${GREEN}✅${NC} Created symlinks"
    fi
}

# Deploy based on mode
if [ "$MODE" = "minimal" ]; then
    deploy_minimal
else
    deploy_full
fi

# Post-deployment
if [ "$DRY_RUN" != true ]; then
    echo ""
    echo "✅ Deployment complete!"
    echo ""
    echo "📋 Next steps:"
    echo "1. cd $TARGET"
    if [ ! -f "$TARGET/.claude/config.yaml" ]; then
        echo "2. Configure: cp .claude/config.yaml.template .claude/config.yaml"
        echo "3. Edit .claude/config.yaml for your project"
    fi
    echo "4. Run health check: ./.claude/skills/bmad-commands/scripts/health-check.sh"
    echo "5. Read quick start: docs/QUICK-START.md"
else
    echo ""
    echo "📋 Dry run complete. Run without --dry-run to deploy."
fi
```

Make it executable:
```bash
chmod +x .claude/skills/bmad-commands/scripts/deploy-to-project.sh
```

**Usage:**
```bash
# Deploy to project (minimal - recommended)
./.claude/skills/bmad-commands/scripts/deploy-to-project.sh ~/projects/my-app

# Deploy full repository
./.claude/skills/bmad-commands/scripts/deploy-to-project.sh --full ~/projects/my-app

# Dry run (see what would be copied)
./.claude/skills/bmad-commands/scripts/deploy-to-project.sh --dry-run ~/projects/my-app
```

---

## Minimal Deployment Package

Create a minimal deployment package:

```bash
#!/bin/bash
# Create minimal deployment package (tar.gz)

PACKAGE_NAME="bmad-enhanced-minimal-$(date +%Y%m%d).tar.gz"

tar czf "$PACKAGE_NAME" \
  .claude/ \
  scripts/ \
  docs/QUICK-START.md \
  docs/quickstart-*.md \
  docs/TROUBLESHOOTING.md \
  docs/ERROR-CODES.md \
  docs/COMMAND-REFERENCE-SUMMARY.md

echo "✅ Package created: $PACKAGE_NAME"
echo "Size: $(du -h "$PACKAGE_NAME" | cut -f1)"
echo ""
echo "To deploy:"
echo "  tar xzf $PACKAGE_NAME -C /path/to/your-project"
```

---

## Full Repository Deployment

### When to Use Full Deployment

Use full deployment when:
- ✅ You need all documentation
- ✅ You want to customize skills
- ✅ You're developing new features
- ✅ You need architecture references
- ✅ Multiple team members working

### Advantages
- ✅ Complete feature set
- ✅ All documentation available
- ✅ Easy updates via git pull
- ✅ Can customize anything

### Disadvantages
- ❌ Larger footprint (~20 MB vs ~5 MB)
- ❌ More files to manage
- ❌ Potential confusion (what's BMAD vs project)

---

## Verification Checklist

After deployment, verify everything works:

### 1. Basic Structure
```bash
cd /path/to/your-project

# Check directories exist
[ -d .claude ] && echo "✅ .claude exists" || echo "❌ .claude missing"
[ -d scripts ] && echo "✅ scripts exists" || echo "❌ scripts missing"
[ -d .claude/skills ] && echo "✅ skills exists" || echo "❌ skills missing"
```

### 2. Scripts Executable
```bash
# Check scripts can run
python3 .claude/skills/bmad-commands/scripts/monitor-skills.py --validate-only
./.claude/skills/bmad-commands/scripts/health-check.sh
```

### 3. Configuration
```bash
# Check config exists
if [ ! -f .claude/config.yaml ]; then
    echo "⚠️  Create config: cp .claude/config.yaml.template .claude/config.yaml"
fi
```

### 4. Skills Loaded
```bash
# Verify skills
python3 .claude/skills/bmad-commands/scripts/monitor-skills.py
```

### 5. Documentation Accessible
```bash
# Check docs
ls docs/QUICK-START.md
ls docs/quickstart-*.md
```

---

## Project-Specific Customization

After deployment, customize for your project:

### 1. Configuration

```bash
# Copy template
cp .claude/config.yaml.template .claude/config.yaml

# Edit for your project
nano .claude/config.yaml
```

**Key settings to customize:**
```yaml
# Project-specific
project:
  name: "Your Project Name"
  type: web|mobile|backend|fullstack

# Testing framework
testing:
  frameworks:
    jest:  # Or pytest, junit, etc.
      enabled: true

# Your team's guardrails
guardrails:
  test_coverage_min: 80  # Your standard
  complexity_max: 70
```

### 2. Custom Skills

Add project-specific skills:
```bash
mkdir -p .claude/skills/custom/
# Create your custom skills here
```

### 3. Team Documentation

Add project-specific docs:
```bash
# Keep BMAD docs separate
mkdir -p docs/team/
mkdir -p docs/bmad/
mv docs/quickstart-*.md docs/bmad/
```

---

## Common Issues

### Issue 1: Scripts Not Found

**Symptom:**
```
bash: .claude/skills/bmad-commands/scripts/monitor-skills.py: No such file or directory
```

**Cause:** Didn't copy `scripts/` directory

**Fix:**
```bash
cp -r /path/to/bmad-enhanced/scripts /path/to/your-project/
```

---

### Issue 2: Import Errors in Python Scripts

**Symptom:**
```
ImportError: No module named 'yaml'
```

**Cause:** Missing Python dependencies

**Fix:**
```bash
pip install pyyaml
```

---

### Issue 3: Skills Not Loading

**Symptom:** Commands don't work

**Cause:** `.claude/skills/` missing or incomplete

**Fix:**
```bash
# Verify skills
python3 .claude/skills/bmad-commands/scripts/monitor-skills.py
# Should show 32 skills
```

---

### Issue 4: No UX Improvements Visible

**Symptom:** No wizard, no progress, no improved errors

**Cause:** Missing `scripts/` directory OR Claude not invoking them

**Fix:**
```bash
# 1. Ensure scripts exist
ls .claude/skills/bmad-commands/scripts/bmad-wizard.py
ls .claude/skills/bmad-commands/scripts/progress-visualizer.py
ls .claude/skills/bmad-commands/scripts/error-handler.py

# 2. Test manually
python3 .claude/skills/bmad-commands/scripts/bmad-wizard.py

# 3. For Claude to use them, they must be referenced in skills
```

**Note:** Claude Code has low verbosity and won't automatically show script outputs unless explicitly configured in skills.

---

## Addressing Low Verbosity Issue

Since you mentioned Claude has low verbosity and scripts aren't showing:

### Solution 1: Make Scripts Output-First

Update skill definitions to explicitly show outputs:

```markdown
### Step 1: Show Progress
**Command:** `python .claude/skills/bmad-commands/scripts/progress-visualizer.py --workflow "Feature Implementation" --steps 5`
**Output to User:** `cat .claude/logs/progress.log`
**Acceptance:** Progress bar visible to user
```

### Solution 2: Create Wrapper Scripts

```bash
# scripts/run-with-output.sh
#!/bin/bash
# Wrapper that forces output visibility

SCRIPT=$1
shift
ARGS=$@

echo "🚀 Running: $SCRIPT"
python3 "$SCRIPT" $ARGS 2>&1 | tee .claude/logs/last-output.log
echo "✅ Complete. Output logged to .claude/logs/last-output.log"
```

### Solution 3: Integrated Output in Skills

Modify skills to include explicit output commands:

```yaml
outputs:
  - name: user_visible_output
    type: string
    description: "Output shown to user"
    display: true  # Force display
```

---

## Recommended Approach

**For your specific case (copying to multiple projects):**

### Option A: Minimal Package Script (Recommended)

1. **Create deployment script:**
```bash
# Save as deploy-bmad.sh in BMAD Enhanced
#!/bin/bash
TARGET=$1

if [ -z "$TARGET" ]; then
    echo "Usage: $0 <target-project>"
    exit 1
fi

echo "Deploying BMAD Enhanced to $TARGET..."

# Essential only
cp -r .claude "$TARGET/"
cp -r scripts "$TARGET/"
mkdir -p "$TARGET/docs"
cp docs/QUICK-START.md "$TARGET/docs/"
cp docs/quickstart-*.md "$TARGET/docs/"
cp docs/TROUBLESHOOTING.md "$TARGET/docs/"
cp docs/ERROR-CODES.md "$TARGET/docs/"

echo "✅ Deployed! Run: cd $TARGET && ./.claude/skills/bmad-commands/scripts/health-check.sh"
```

2. **Use it:**
```bash
chmod +x deploy-bmad.sh
./deploy-bmad.sh /path/to/project1
./deploy-bmad.sh /path/to/project2
```

### Option B: Symlink from Central Location

```bash
# Keep one BMAD Enhanced installation
export BMAD_HOME="/home/adolfo/Documents/BMAD Enhanced"

# In each project, create symlinks
cd /path/to/project
ln -s "$BMAD_HOME/.claude" .claude
ln -s "$BMAD_HOME/scripts" scripts
ln -s "$BMAD_HOME/docs" docs

# Copy only config (project-specific)
cp "$BMAD_HOME/.claude/config.yaml.template" .claude/config.yaml
```

**Advantages:**
- ✅ Always up-to-date
- ✅ Single source of truth
- ✅ Minimal disk usage

**Disadvantages:**
- ❌ All projects update together
- ❌ Project-specific modifications affect all

---

## Summary

### ❌ Don't Do This:
```bash
# INSUFFICIENT!
cp -r .claude /path/to/project/
```

### ✅ Do This (Minimal):
```bash
# SUFFICIENT for most projects
cp -r .claude /path/to/project/
cp -r scripts /path/to/project/
cp docs/QUICK-START.md docs/quickstart-*.md docs/TROUBLESHOOTING.md /path/to/project/docs/
```

### ✅ Or This (Full):
```bash
# COMPLETE - all features
cp -r "BMAD Enhanced" /path/to/project/.bmad-enhanced
cd /path/to/project
ln -s .bmad-enhanced/.claude .claude
ln -s .bmad-enhanced/scripts scripts
```

---

## Quick Reference Card

Print this and keep it handy:

```
┌─────────────────────────────────────────────────────┐
│  BMAD Enhanced Deployment Quick Reference          │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ❌ INSUFFICIENT (only .claude/):                  │
│     • Missing scripts (no UX, no monitoring)        │
│     • Missing docs (no guides)                      │
│     • Missing test adapters                         │
│                                                     │
│  ✅ MINIMAL (recommended):                         │
│     • Copy: .claude/ scripts/ docs/*.md           │
│     • Size: ~5 MB                                   │
│     • Has: All features, essential docs             │
│                                                     │
│  ✅ FULL (for complex projects):                   │
│     • Copy: Entire repository                       │
│     • Size: ~20 MB                                  │
│     • Has: Everything + full docs                   │
│                                                     │
│  📋 After Deployment:                              │
│     1. cp config.yaml.template config.yaml         │
│     2. Edit config.yaml                             │
│     3. ./.claude/skills/bmad-commands/scripts/health-check.sh                   │
│     4. python .claude/skills/bmad-commands/scripts/monitor-skills.py            │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

**Questions? See [TROUBLESHOOTING.md](./TROUBLESHOOTING.md)**

---

**Maintained by:** BMAD Enhanced Development Team
**Last Updated:** 2025-11-05
