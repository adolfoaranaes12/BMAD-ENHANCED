#!/bin/bash
# BMAD Enhanced - Smart Deployment Script
# Deploys BMAD Enhanced to target project with validation

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BMAD_ROOT="$(cd "$(dirname "$SCRIPT_DIR")/../../../.." && pwd)"

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

# Usage
usage() {
    cat << EOF
${BLUE}BMAD Enhanced - Deployment Script${NC}

Usage: $0 [OPTIONS] <target-project-directory>

Options:
  --minimal     Deploy minimal package (default)
                Includes: .claude, scripts, essential docs (~5 MB)

  --full        Deploy full repository
                Includes: Everything (~20 MB)

  --dry-run     Show what would be copied without copying

  --force       Overwrite existing files without prompting

  --help        Show this help message

Examples:
  # Deploy minimal package (recommended)
  $0 ~/projects/my-app

  # Deploy full repository
  $0 --full ~/projects/my-app

  # See what would be deployed
  $0 --dry-run ~/projects/my-app

  # Force overwrite
  $0 --force ~/projects/my-app

EOF
    exit 0
}

# Parse arguments
MODE="minimal"
DRY_RUN=false
FORCE=false
TARGET=""

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
            if [ -z "$TARGET" ]; then
                TARGET="$1"
            fi
            shift
            ;;
    esac
done

# Validate target
if [ -z "$TARGET" ]; then
    echo -e "${RED}Error: Target directory required${NC}"
    echo "Run with --help for usage information"
    exit 1
fi

# Create target if doesn't exist
if [ ! -d "$TARGET" ]; then
    if [ "$DRY_RUN" = false ]; then
        echo -e "${YELLOW}Target directory doesn't exist. Create it? (y/n)${NC}"
        read -r response
        if [[ "$response" =~ ^[Yy]$ ]]; then
            mkdir -p "$TARGET"
            echo -e "${GREEN}✅ Created $TARGET${NC}"
        else
            echo "Aborted."
            exit 1
        fi
    else
        echo -e "${YELLOW}[DRY RUN] Would create: $TARGET${NC}"
    fi
fi

# Print header
echo -e "${BLUE}┌────────────────────────────────────────────────────────┐${NC}"
echo -e "${BLUE}│  BMAD Enhanced Deployment                              │${NC}"
echo -e "${BLUE}└────────────────────────────────────────────────────────┘${NC}"
echo ""
echo "Source: $BMAD_ROOT"
echo "Target: $TARGET"
echo "Mode:   $MODE"
if [ "$DRY_RUN" = true ]; then
    echo -e "Status: ${YELLOW}DRY RUN (no files will be copied)${NC}"
fi
echo ""

# Check if files exist
if [ -d "$TARGET/.claude" ] && [ "$FORCE" != true ] && [ "$DRY_RUN" != true ]; then
    echo -e "${YELLOW}⚠️  Warning: .claude directory already exists in target${NC}"
    echo "Options:"
    echo "  1. Use --force to overwrite"
    echo "  2. Manually remove $TARGET/.claude"
    echo "  3. Choose a different target"
    exit 1
fi

# Deploy function
deploy_file() {
    local src="$1"
    local dst="$2"
    local desc="$3"

    if [ ! -e "$src" ]; then
        echo -e "${YELLOW}⚠️  Skipped (not found): $desc${NC}"
        return
    fi

    if [ "$DRY_RUN" = true ]; then
        echo -e "${BLUE}[DRY RUN]${NC} Would copy: $desc"
        return
    fi

    mkdir -p "$(dirname "$dst")"

    if [ -d "$src" ]; then
        cp -r "$src" "$dst"
    else
        cp "$src" "$dst"
    fi

    # Calculate size
    if [ -d "$dst" ]; then
        SIZE=$(du -sh "$dst" 2>/dev/null | cut -f1)
    else
        SIZE=$(du -sh "$dst" 2>/dev/null | cut -f1)
    fi

    echo -e "${GREEN}✅${NC} Copied: $desc ${BLUE}($SIZE)${NC}"
}

# Minimal deployment
deploy_minimal() {
    echo -e "${GREEN}📦 Deploying Minimal Package${NC}"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""

    # .claude directory
    echo "1. Core Configuration & Skills"
    deploy_file "$BMAD_ROOT/.claude" "$TARGET/.claude" ".claude directory"
    echo ""

    # .claude/skills/bmad-commands/scripts directory
    echo "2. Scripts & Tools"
    deploy_file "$BMAD_ROOT/.claude/skills/bmad-commands/scripts" "$TARGET/scripts" "scripts directory"
    echo ""

    # Essential docs
    echo "3. Essential Documentation"
    mkdir -p "$TARGET/docs" 2>/dev/null || true
    deploy_file "$BMAD_ROOT/docs/QUICK-START.md" "$TARGET/docs/QUICK-START.md" "Quick Start"
    deploy_file "$BMAD_ROOT/docs/TROUBLESHOOTING.md" "$TARGET/docs/TROUBLESHOOTING.md" "Troubleshooting"
    deploy_file "$BMAD_ROOT/docs/ERROR-CODES.md" "$TARGET/docs/ERROR-CODES.md" "Error Codes"
    deploy_file "$BMAD_ROOT/docs/COMMAND-REFERENCE-SUMMARY.md" "$TARGET/docs/COMMAND-REFERENCE-SUMMARY.md" "Command Reference"

    # Quickstart guides
    for file in "$BMAD_ROOT/docs/quickstart-"*.md; do
        if [ -f "$file" ]; then
            deploy_file "$file" "$TARGET/docs/$(basename "$file")" "$(basename "$file")"
        fi
    done

    # Config template
    if [ -f "$BMAD_ROOT/.claude/config.yaml.template" ]; then
        deploy_file "$BMAD_ROOT/.claude/config.yaml.template" "$TARGET/.claude/config.yaml.template" "Config template"
    fi
    echo ""
}

# Full deployment
deploy_full() {
    echo -e "${GREEN}📦 Deploying Full Repository${NC}"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""

    if [ "$DRY_RUN" = false ]; then
        mkdir -p "$TARGET/.bmad-enhanced" 2>/dev/null || true
    fi

    echo "1. Complete BMAD Enhanced Repository"
    deploy_file "$BMAD_ROOT/.claude" "$TARGET/.bmad-enhanced/.claude" ".claude"
    deploy_file "$BMAD_ROOT/.claude/skills/bmad-commands/scripts" "$TARGET/.bmad-enhanced/scripts" "scripts"
    deploy_file "$BMAD_ROOT/docs" "$TARGET/.bmad-enhanced/docs" "docs"
    echo ""

    # Create symlinks
    echo "2. Creating Symlinks"
    if [ "$DRY_RUN" != true ]; then
        cd "$TARGET"

        # Remove existing symlinks/dirs
        [ -L .claude ] && rm .claude
        [ -L docs ] && rm docs

        ln -sf .bmad-enhanced/.claude .claude
        ln -sf .bmad-enhanced/docs docs

        echo -e "${GREEN}✅${NC} Created symlink: .claude -> .bmad-enhanced/.claude"
        echo -e "${GREEN}✅${NC} Created symlink: docs -> .bmad-enhanced/docs"
    else
        echo -e "${BLUE}[DRY RUN]${NC} Would create symlinks"
    fi
    echo ""
}

# Deploy based on mode
if [ "$MODE" = "minimal" ]; then
    deploy_minimal
else
    deploy_full
fi

# Post-deployment
if [ "$DRY_RUN" != true ]; then
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo -e "${GREEN}✅ Deployment Complete!${NC}"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo -e "${BLUE}📋 Next Steps:${NC}"
    echo ""
    echo "1. Navigate to project:"
    echo "   ${YELLOW}cd $TARGET${NC}"
    echo ""

    if [ ! -f "$TARGET/.claude/config.yaml" ]; then
        echo "2. Create configuration:"
        echo "   ${YELLOW}cp .claude/config.yaml.template .claude/config.yaml${NC}"
        echo ""
        echo "3. Edit configuration for your project:"
        echo "   ${YELLOW}nano .claude/config.yaml${NC}"
        echo ""
        NEXT_STEP=4
    else
        echo "2. Configuration already exists (skipping)"
        echo ""
        NEXT_STEP=3
    fi

    echo "$NEXT_STEP. Run health check:"
    echo "   ${YELLOW}./.claude/skills/bmad-commands/scripts/health-check.sh${NC}"
    echo ""

    ((NEXT_STEP++))
    echo "$NEXT_STEP. Validate skills:"
    echo "   ${YELLOW}python3 .claude/skills/bmad-commands/scripts/monitor-skills.py${NC}"
    echo ""

    ((NEXT_STEP++))
    echo "$NEXT_STEP. Read quick start:"
    echo "   ${YELLOW}cat docs/QUICK-START.md${NC}"
    echo ""

    # Calculate total size
    if [ "$MODE" = "minimal" ]; then
        TOTAL_SIZE=$(du -sh "$TARGET/.claude" "$TARGET/scripts" "$TARGET/docs" 2>/dev/null | awk '{sum+=$1} END {print sum}')
        echo -e "${BLUE}📊 Total deployed: ~5 MB${NC}"
    else
        TOTAL_SIZE=$(du -sh "$TARGET/.bmad-enhanced" 2>/dev/null | cut -f1)
        echo -e "${BLUE}📊 Total deployed: $TOTAL_SIZE${NC}"
    fi
else
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo -e "${YELLOW}📋 Dry Run Complete${NC}"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "No files were copied. Run without --dry-run to deploy."
    echo ""
    echo "To deploy for real:"
    if [ "$MODE" = "minimal" ]; then
        echo "  ${YELLOW}$0 $TARGET${NC}"
    else
        echo "  ${YELLOW}$0 --full $TARGET${NC}"
    fi
fi

echo ""
