Parse command and arguments from user input.

Command format: /design-architecture <requirements-file> [--type <type>] [--complexity <complexity>]

Example: /design-architecture docs/prd.md
Example: /design-architecture docs/epic-user-auth.md --type fullstack
Example: /design-architecture docs/requirements.md --type backend --complexity medium

Extract:
- requirements_file: ${1} (first argument, requirements/PRD file path)
- project_type: ${2} (optional: frontend, backend, fullstack - default: auto-detect)
- complexity: ${3} (optional: simple, medium, complex - default: auto-calculate)

Route to create-architecture skill:
Use .claude/skills/planning/create-architecture/SKILL.md with:
- Input: requirements_file = ${1}
- Input: project_type = ${2:-auto} (default to "auto" for auto-detection)
- Input: complexity = ${3:-auto} (default to "auto" for auto-calculation)

Execute 10-step architecture creation workflow:
1. Requirements analysis (functional, NFRs, constraints)
2. Project type detection (frontend/backend/fullstack)
3. Complexity assessment (0-100 scoring)
4. Technology stack selection with justification
5. Architecture pattern selection
6. ADR generation (minimum 3-10 based on complexity)
7. NFR architecture mapping (performance, scalability, security)
8. Diagram generation (C4 model: context, container, deployment)
9. Security architecture design
10. Validation and completeness check

Output architecture artifacts:
- docs/architecture.md (comprehensive architecture document)
- docs/adrs/ADR-00X-*.md (Architecture Decision Records)
- docs/diagrams/*.mmd (Mermaid architecture diagrams)
- Architecture summary with key decisions

Quality gates:
- All required sections present (based on project type)
- Technology stack justified with alternatives
- Minimum ADR count met (simple: 3, medium: 5, complex: 10)
- NFRs addressed (performance, scalability, security, reliability)
- Security considerations documented
- Scalability approach defined

Emit telemetry:
- skill.create-architecture.completed
- Track: project_type, complexity_score, adrs_count, technologies_count, validation_score
