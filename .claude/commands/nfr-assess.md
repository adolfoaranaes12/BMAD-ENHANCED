---
description: Assess Non-Functional Requirements across 8 dimensions with gap analysis
argument-hint: <requirements-file> [--focus <dimension>]
allowed-tools: Skill
---

Invoke the nfr-assess skill:

Use Skill tool: `Skill(command="nfr-assess")`

This will execute the NFR assessment workflow:
1. Load requirements document (PRD, epic, or architecture)
2. Identify NFR statements across 8 dimensions:
   - Performance (latency, throughput)
   - Scalability (users, data volume)
   - Security (auth, encryption, compliance)
   - Reliability (uptime, fault tolerance)
   - Maintainability (code quality, documentation)
   - Usability (UX, accessibility)
   - Observability (logging, monitoring)
   - Compliance (regulations, standards)
3. Assess completeness and specificity
4. Identify gaps and missing NFRs
5. Calculate NFR quality score
6. Generate recommendations

The skill will parse $ARGUMENTS for:
- `requirements-file` - Path to requirements document (required)
- `--focus` - Focus on specific dimension (optional)

Output: NFR assessment report with scores, gaps, and recommendations
