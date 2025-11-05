---
description: Validate user story specifications for completeness, implementation readiness, and anti-hallucination verification before development begins
argument-hint: <story-file> [--mode <mode>]
allowed-tools: Read, Skill
---

# Validate Story Command

Validate user story specifications for completeness and implementation readiness.

## Usage

```bash
/validate-story <story-file> [--mode <mode>]
```

## Parameters

- `story-file` - Path to story file (e.g., `.claude/stories/epic-001/story-003.md`)
- `--mode` - Validation mode: `full` (default), `quick`, `critical_only`

## Examples

```bash
/validate-story .claude/stories/epic-001/story-003.md
/validate-story .claude/stories/epic-001/story-003.md --mode quick
/validate-story .claude/stories/epic-001/story-003.md --mode critical_only
```

## Validation Process

Execute 10-step validation workflow:
1. Template completeness
2. File structure validation
3. UI/Frontend completeness (if applicable)
4. Acceptance criteria satisfaction
5. Testing instructions
6. Security considerations (if applicable)
7. Tasks sequence validation
8. Anti-hallucination verification
9. Implementation readiness assessment
10. Generate validation report

## Output

Validation report with:
- **GO/NO-GO decision**
- Readiness score (1-10)
- Confidence level (High/Medium/Low)
- Critical issues (must fix)
- Should-fix issues (recommended)
- Nice-to-have improvements
- Anti-hallucination findings

## Implementation

Parse command and arguments from user input.

Command format: /validate-story <story-file> [--mode <mode>]

Extract:
- story_file: $1 (first argument, story file path)
- mode: $2 (optional: full, quick, critical_only - default: full)

Route to validate-story skill:
Use .claude/skills/planning/validate-story/SKILL.md with:
- Input: story_file = $1
- Input: validation_mode = $2 (default to "full" if not specified)

Execute 10-step validation workflow:
1. Template completeness
2. File structure validation
3. UI/Frontend completeness (if applicable)
4. Acceptance criteria satisfaction
5. Testing instructions
6. Security considerations (if applicable)
7. Tasks sequence validation
8. Anti-hallucination verification
9. Implementation readiness assessment
10. Generate validation report

Output validation report with:
- GO/NO-GO decision
- Readiness score (1-10)
- Confidence level (High/Medium/Low)
- Critical issues (must fix)
- Should-fix issues (recommended)
- Nice-to-have improvements
- Anti-hallucination findings

Emit telemetry:
- skill.validate-story.completed
- Track: story_id, validation_passed, readiness_score, critical_issues_count
