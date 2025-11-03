Parse command and arguments from user input.

Command format: /validate-story <story-file> [--mode <mode>]

Example: /validate-story .claude/stories/epic-001/story-003.md
Example: /validate-story .claude/stories/epic-001/story-003.md --mode quick

Extract:
- story_file: ${1} (first argument, story file path)
- mode: ${2} (optional: full, quick, critical_only - default: full)

Route to validate-story skill:
Use .claude/skills/planning/validate-story/SKILL.md with:
- Input: story_file = ${1}
- Input: validation_mode = ${2:-full} (default to "full" if not specified)

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
