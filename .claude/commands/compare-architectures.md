---
description: Compare multiple architecture approaches with trade-off analysis
argument-hint: <description> [--current <file>] [--requirements <file>]
allowed-tools: Skill
---

Invoke the compare-architectures skill:

Use Skill tool: `Skill(command="compare-architectures")`

This will execute the architecture comparison workflow:
1. Analyze description/requirements
2. Generate 3 architecture options (minimal, moderate, comprehensive)
3. Evaluate each across dimensions:
   - Cost (infrastructure, development, operations)
   - Timeline (implementation effort)
   - Risk (technical, operational)
   - Performance (latency, throughput)
   - Scalability (growth capacity)
   - Maintainability (long-term costs)
4. Score and rank options
5. Generate recommendation with confidence level
6. Create comparison report

The skill will parse $ARGUMENTS for:
- `description` - Feature/change description (required)
- `--current` - Current architecture file for context (optional)
- `--requirements` - Requirements file for NFR context (optional)

Output: Architecture comparison report with 3 options, trade-off analysis, recommendation
