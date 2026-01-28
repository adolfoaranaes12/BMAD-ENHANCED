---
description: Refactor code with safety checks and quality improvements
argument-hint: <target> [--pattern <refactoring-pattern>]
allowed-tools: Skill
---

Invoke the refactor-code skill:

Use Skill tool: `Skill(command="refactor-code")`

This will execute the refactoring workflow:
1. Analyze target code
2. Identify refactoring opportunities
3. Select refactoring pattern (if not specified)
4. Run existing tests (baseline)
5. Apply refactoring incrementally
6. Validate tests still pass
7. Measure quality improvements
8. Generate refactoring report

The skill will parse $ARGUMENTS for:
- `target` - File, function, or module to refactor (required)
- `--pattern` - Refactoring pattern: extract-function, extract-class, inline, rename, etc.
- `--safety` - Safety level: conservative (default), moderate, aggressive
- `--quality-focus` - Focus area: readability, performance, maintainability

Output: Refactored code, quality metrics before/after, refactoring log
