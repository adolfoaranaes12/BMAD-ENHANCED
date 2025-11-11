---
description: Generate PRD from existing codebase through systematic analysis
argument-hint: "<codebase-path>"
allowed-tools: Skill
---

Invoke the create-brownfield-prd skill:

Use Skill tool with skill="create-brownfield-prd"

This will execute the brownfield PRD creation workflow:
1. Codebase analysis (5-phase discovery: structure, code, data, behavior, integration)
2. Feature extraction and user flow reconstruction
3. Gap analysis (missing features, technical debt)
4. Generate comprehensive PRD with confidence scoring
5. Highlight areas requiring human validation

The skill will parse $ARGUMENTS for:
- `codebase-path` - Path to existing codebase to analyze (required)

Output: Brownfield PRD document with feature extraction, gap analysis, and confidence scores
