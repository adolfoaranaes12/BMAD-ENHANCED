---
description: Trace requirements through implementation with traceability matrix
argument-hint: <requirements-file> [--output-format markdown|json]
allowed-tools: Skill
---

Invoke the trace-requirements skill:

Use Skill tool: `Skill(command="trace-requirements")`

This will execute the requirements tracing workflow:
1. Load requirements document
2. Identify all requirements and acceptance criteria
3. Scan codebase for implementation evidence
4. Map requirements to code/tests/docs
5. Identify coverage gaps
6. Calculate traceability completeness
7. Generate traceability matrix and report

The skill will parse $ARGUMENTS for:
- `requirements-file` - Path to requirements (PRD, epic, or task spec) (required)
- `--output-format` - Output format: markdown (default), json
- `--include-tests` - Include test coverage in trace (default: true)
- `--threshold` - Completeness threshold for quality gate: 70, 80, 90, 100 (default: 80)

Output: Requirements traceability report with matrix, gaps, completeness score
