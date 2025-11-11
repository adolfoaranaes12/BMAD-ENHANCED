---
description: Create comprehensive PRD from high-level product idea (greenfield)
argument-hint: "<product-idea>"
allowed-tools: Skill
---

Invoke the create-prd skill:

Use Skill tool with skill="create-prd"

This will execute the PRD creation workflow:
1. Requirements gathering using Five Whys and JTBD framework
2. Market analysis (TAM/SAM/SOM, competitive landscape)
3. Feature definition with MoSCoW prioritization
4. Success metrics (AARRR framework)
5. Generate comprehensive 12-section PRD

The skill will parse $ARGUMENTS for:
- `product-idea` - High-level product concept or description (required)

Output: PRD document at configured location with market analysis and prioritized features
