#!/bin/bash
# BMAD Enhanced - Quick Health Check
# Validates that the system is properly configured and skills are loaded

set -e

echo "🏥 BMAD Enhanced Health Check"
echo "=============================="
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

ERRORS=0
WARNINGS=0

# Function to check and report
check() {
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ $1${NC}"
    else
        echo -e "${RED}❌ $1${NC}"
        ((ERRORS++))
    fi
}

warn() {
    echo -e "${YELLOW}⚠️  $1${NC}"
    ((WARNINGS++))
}

# 1. Check we're in project root
echo "1. Checking project structure..."
if [ ! -d .claude ]; then
    echo -e "${RED}❌ CRITICAL: Not in project root (no .claude/ directory)${NC}"
    echo "   Run this script from the BMAD Enhanced root directory"
    exit 1
fi
check "Project root directory"

# 2. Check skills directory
echo ""
echo "2. Checking skills directory..."
[ -d .claude/skills ]
check "Skills directory exists"

# 3. Count skills
echo ""
echo "3. Counting skills..."
SKILL_COUNT=$(find .claude/skills -name "SKILL.md" 2>/dev/null | wc -l)
echo "   Found: $SKILL_COUNT skills"

if [ $SKILL_COUNT -eq 0 ]; then
    echo -e "${RED}❌ No skills found!${NC}"
    ((ERRORS++))
elif [ $SKILL_COUNT -lt 30 ]; then
    warn "Expected ~32 skills, found $SKILL_COUNT"
else
    echo -e "${GREEN}✅ Skill count reasonable ($SKILL_COUNT skills)${NC}"
fi

# 4. Check skills by category
echo ""
echo "4. Checking skills by category..."
for cat in planning development quality architecture brownfield implementation; do
    count=$(find .claude/skills/$cat -name "SKILL.md" 2>/dev/null | wc -l)
    if [ $count -gt 0 ]; then
        echo -e "   ${GREEN}✅${NC} $cat: $count skills"
    else
        warn "$cat: $count skills (empty category)"
    fi
done

# 5. Check Python
echo ""
echo "5. Checking Python environment..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo "   $PYTHON_VERSION"
    check "Python 3 available"
else
    echo -e "${RED}❌ Python 3 not found${NC}"
    ((ERRORS++))
fi

# 6. Check required Python packages
echo ""
echo "6. Checking Python packages..."
if python3 -c "import yaml" 2>/dev/null; then
    check "PyYAML installed"
else
    echo -e "${RED}❌ PyYAML not installed${NC}"
    echo "   Install: pip install pyyaml"
    ((ERRORS++))
fi

# 7. Validate skills
echo ""
echo "7. Validating skills..."
if [ -f .claude/skills/bmad-commands/scripts/monitor-skills.py ]; then
    # Run validation with timeout
    if timeout 5 python3 .claude/skills/bmad-commands/scripts/monitor-skills.py --validate-only >/dev/null 2>&1; then
        check "All skills valid"
    else
        warn "Some skills may be invalid (run: python3 .claude/skills/bmad-commands/scripts/monitor-skills.py for details)"
    fi
else
    warn "monitor-skills.py not found (skipping validation)"
fi

# 8. Check config file
echo ""
echo "8. Checking configuration..."
if [ -f .claude/config.yaml ]; then
    check "Config file exists"
else
    warn "Config file not found (.claude/config.yaml)"
    echo "   You may need to copy from config.yaml.template"
fi

# 9. Check documentation
echo ""
echo "9. Checking documentation..."
DOC_COUNT=$(find docs -name "*.md" -type f | grep -v archive | wc -l)
echo "   Found: $DOC_COUNT documentation files"
if [ $DOC_COUNT -ge 35 ]; then
    check "Documentation present"
else
    warn "Expected ~40 docs, found $DOC_COUNT"
fi

# 10. Check disk space
echo ""
echo "10. Checking disk space..."
DISK_USAGE=$(df -h .claude/ | tail -1 | awk '{print $5}' | sed 's/%//')
echo "   Disk usage: ${DISK_USAGE}%"
if [ $DISK_USAGE -lt 90 ]; then
    check "Sufficient disk space"
else
    warn "Disk usage high: ${DISK_USAGE}%"
fi

# Summary
echo ""
echo "=============================="
echo "📊 Health Check Summary"
echo "=============================="
if [ $ERRORS -eq 0 ] && [ $WARNINGS -eq 0 ]; then
    echo -e "${GREEN}✅ All checks passed!${NC}"
    echo ""
    echo "System is healthy and ready to use."
    exit 0
elif [ $ERRORS -eq 0 ]; then
    echo -e "${YELLOW}⚠️  $WARNINGS warnings found${NC}"
    echo ""
    echo "System is functional but some warnings need attention."
    exit 0
else
    echo -e "${RED}❌ $ERRORS errors found${NC}"
    if [ $WARNINGS -gt 0 ]; then
        echo -e "${YELLOW}⚠️  $WARNINGS warnings found${NC}"
    fi
    echo ""
    echo "System has issues that need to be fixed."
    exit 1
fi
