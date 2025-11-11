#!/bin/bash
# Verification script for subagent skill loading
# Usage: ./scripts/verify-skill-loading.sh

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Subagent Skill Loading Verification"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Check if subagents reference Read() for skill loading
echo "=== Checking Skill Loading Implementation ==="
echo ""

for agent in .claude/agents/*.md; do
  agent_name=$(basename "$agent" .md)

  # Skip archive files
  if [[ "$agent" == *"archive"* ]]; then
    continue
  fi

  if grep -q "Read(.claude/skills/" "$agent"; then
    echo "✅ $agent_name - Loads skills correctly"
  else
    echo "❌ $agent_name - NOT loading skills (needs fix)"
  fi
done

echo ""
echo "=== Checking for Command Routing Section ==="
echo ""

for agent in .claude/agents/*.md; do
  agent_name=$(basename "$agent" .md)

  # Skip archive files
  if [[ "$agent" == *"archive"* ]]; then
    continue
  fi

  if grep -q "Command Routing" "$agent" || grep -q "explicitly load" "$agent"; then
    echo "✅ $agent_name - Has routing instructions"
  else
    echo "⚠️  $agent_name - Missing routing instructions"
  fi
done

echo ""
echo "=== Checking for Critical Skill Loading Instructions ==="
echo ""

for agent in .claude/agents/*.md; do
  agent_name=$(basename "$agent" .md)

  # Skip archive files
  if [[ "$agent" == *"archive"* ]]; then
    continue
  fi

  if grep -q "CRITICAL.*explicitly.*skill" "$agent" || grep -q "Always.*Load.*Skills" "$agent"; then
    echo "✅ $agent_name - Has critical skill loading instruction"
  else
    echo "⚠️  $agent_name - Missing critical instruction"
  fi
done

echo ""
echo "=== Subagent-Skill Mapping Check ==="
echo ""

# Define expected skills for each subagent
declare -A expected_skills
expected_skills["alex-planner-v2"]="create-task-spec breakdown-epic estimate-stories refine-story sprint-plan"
expected_skills["james-developer-v2"]="implement-feature fix-issue run-tests refactor-code apply-qa-fixes"
expected_skills["quinn-quality-v2"]="review-task nfr-assess quality-gate trace-requirements risk-profile"
expected_skills["winston-architect"]="create-architecture analyze-architecture create-adr validate-architecture architecture-review compare-architectures"
expected_skills["john-pm"]="create-prd create-brownfield-prd"
expected_skills["sarah-po"]="validate-story"

for agent in "${!expected_skills[@]}"; do
  agent_file=".claude/agents/$agent.md"

  if [[ ! -f "$agent_file" ]]; then
    echo "⚠️  $agent - File not found"
    continue
  fi

  skills="${expected_skills[$agent]}"
  missing_count=0

  for skill in $skills; do
    if ! grep -q "$skill/SKILL.md" "$agent_file"; then
      ((missing_count++))
    fi
  done

  skill_count=$(echo "$skills" | wc -w)
  found_count=$((skill_count - missing_count))

  if [[ $missing_count -eq 0 ]]; then
    echo "✅ $agent - All $skill_count skills referenced"
  else
    echo "⚠️  $agent - $found_count/$skill_count skills referenced ($missing_count missing)"
  fi
done

echo ""
echo "=== Skills Directory Check ==="
echo ""

# Check if skill directories exist
for skill_dir in .claude/skills/*/; do
  skill_name=$(basename "$skill_dir")
  skill_file="$skill_dir/SKILL.md"

  if [[ -f "$skill_file" ]]; then
    # Count lines in skill file
    lines=$(wc -l < "$skill_file")
    if [[ $lines -gt 50 ]]; then
      echo "✅ $skill_name - SKILL.md exists ($lines lines)"
    else
      echo "⚠️  $skill_name - SKILL.md too small ($lines lines)"
    fi
  else
    echo "❌ $skill_name - SKILL.md MISSING"
  fi
done

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Summary"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Count status
total_agents=$(find .claude/agents/ -name "*.md" ! -path "*/archive/*" | wc -l)
fixed_agents=$(grep -l "Read(.claude/skills/" .claude/agents/*.md 2>/dev/null | wc -l)
needs_fix=$((total_agents - fixed_agents))

echo "Total Subagents: $total_agents"
echo "✅ Fixed: $fixed_agents"
echo "❌ Needs Fix: $needs_fix"
echo ""

if [[ $needs_fix -eq 0 ]]; then
  echo "🎉 All subagents are correctly configured!"
  exit 0
else
  echo "⚠️  $needs_fix subagent(s) need fixing"
  echo ""
  echo "See docs/SUBAGENT-SKILL-LOADING-FIX.md for fix pattern"
  exit 1
fi
