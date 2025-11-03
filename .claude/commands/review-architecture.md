Parse command and arguments from user input.

Command format: /review-architecture <architecture-file> [--focus <area>] [--mode <mode>]

Example: /review-architecture docs/architecture.md
Example: /review-architecture docs/architecture.md --focus security
Example: /review-architecture docs/architecture.md --focus scalability --mode strict

Extract:
- architecture_file: ${1} (first argument, architecture document path)
- focus_area: ${2} (optional: security, scalability, performance, cost, all - default: all)
- review_mode: ${3} (optional: quick, standard, strict - default: standard)

Route to architecture-review skill:
Use .claude/skills/quality/architecture-review/SKILL.md with:
- Input: architecture_file = ${1}
- Input: focus_area = ${2:-all} (default to "all" for comprehensive review)
- Input: review_mode = ${3:-standard} (default to "standard")

Execute comprehensive architecture review workflow:
1. Load architecture document and requirements (if available)
2. Completeness check (all required sections present)
3. Technology justification review (alternatives considered, rationale provided)
4. ADR quality assessment (minimum count, quality score per ADR)
5. NFR coverage analysis (performance, scalability, security, reliability, maintainability)
6. Security review (auth, authorization, encryption, compliance)
7. Scalability assessment (growth projections, horizontal scaling, bottlenecks)
8. Performance optimization opportunities (caching, CDN, query optimization)
9. Cost analysis (infrastructure costs, operational overhead)
10. Risk identification and mitigation strategies

Focus area deep-dives:
- Security: Vulnerabilities, attack vectors, compliance gaps, security testing
- Scalability: Bottleneck analysis, scaling triggers, database scaling, cost scaling
- Performance: Response time optimization, caching strategy, CDN, bundle size
- Cost: Infrastructure costs, operational overhead, cost-benefit analysis
- All: Comprehensive review across all dimensions

Output review report:
- Overall architecture quality score (0-100)
- Dimension scores (completeness, tech justification, NFRs, security, scalability, documentation)
- Critical issues (must fix before implementation)
- High priority recommendations (should fix)
- Medium priority recommendations (nice to have)
- Low priority improvements (optional)
- Risk assessment (critical, major, minor risks)
- Action items prioritized by impact

Validation scoring:
- Completeness: 25% weight
- Technology Justification: 20% weight
- NFRs Coverage: 20% weight
- Security & Compliance: 15% weight
- Scalability Planning: 10% weight
- Documentation Quality: 10% weight

Pass/Fail criteria:
- Score ≥85: PASS (Excellent) - Ready for implementation
- Score 70-84: PASS (Good) - Address recommendations, proceed
- Score 50-69: FAIL (Needs Work) - Fix critical + high priority, re-validate
- Score 0-49: FAIL (Inadequate) - Major rework required

Quality gates:
- No critical issues blocking implementation
- Validation score ≥70 to proceed
- All NFRs addressed
- Security risks have mitigation plans
- ADR minimum count met

Emit telemetry:
- skill.architecture-review.completed
- Track: validation_score, critical_issues_count, recommendations_count, focus_area, review_result
