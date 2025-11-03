# Full Layer Books - Comprehensive Development Plan from Book Chapters

**Version:** 1.0
**Date:** 2025-11-03
**Purpose:** Guide for developing new skills, subagents, and primitives from book chapters using the 3-layer architecture
**Target Audience:** BMAD Enhanced developers creating new capabilities from technical literature

---

## Table of Contents

1. [Overview](#overview)
2. [Architecture Foundation](#architecture-foundation)
3. [Book Chapter Processing Workflow](#book-chapter-processing-workflow)
4. [Layer 1: Creating Primitives from Books](#layer-1-creating-primitives-from-books)
5. [Layer 2: Creating Workflow Skills from Books](#layer-2-creating-workflow-skills-from-books)
6. [Layer 3: Creating Subagents from Books](#layer-3-creating-subagents-from-books)
7. [Complete Examples](#complete-examples)
8. [Quality Assurance](#quality-assurance)
9. [Common Patterns by Book Type](#common-patterns-by-book-type)
10. [Troubleshooting](#troubleshooting)

---

## Overview

### What This Guide Provides

This guide enables you to **transform technical book chapters into production-ready BMAD Enhanced components** following the 3-layer architecture:

- **Layer 1 (Primitives):** Atomic, testable operations with scripts
- **Layer 2 (Workflow Skills):** Multi-step processes that compose primitives
- **Layer 3 (Subagents):** Intelligent routing and coordination

### Why Use Book Chapters as Source Material?

**Benefits:**
- ✅ **Rich domain knowledge** - Books contain deep expertise and patterns
- ✅ **Battle-tested practices** - Published patterns have been validated
- ✅ **Comprehensive coverage** - Books provide thorough treatment of topics
- ✅ **Contextual learning** - Skills embody proven methodologies
- ✅ **Rapid skill creation** - Transform existing knowledge into skills

**Best Book Types:**
- Design patterns books (Gang of Four, Cloud Patterns)
- Architecture guides (Clean Architecture, DDD)
- Testing methodologies (TDD, BDD)
- Development practices (Refactoring, Pragmatic Programmer)
- Domain-specific guides (React Patterns, Microservices)
- Process frameworks (Agile, Scrum, Kanban)

---

## Architecture Foundation

### Critical Understanding: Skills Remain Skills

**⚠️ MOST IMPORTANT CONCEPT:**

> **All skills follow the skill-creator pattern. The "3 layers" refers to the ROLE skills play, NOT different file structures.**

**All skills you create:**
- ✅ Follow skill-creator patterns (SKILL.md, references/, etc.)
- ✅ Are packageable (package_skill.py)
- ✅ Are portable (.zip distribution)
- ✅ Are self-contained (all dependencies bundled)

**The architecture is about HOW SKILLS WORK TOGETHER, not about creating different types of files.**

### The Three Layers

```
┌─────────────────────────────────────────────────────────────┐
│  Layer 3: SUBAGENTS (Coordination Files)                    │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ .claude/agents/example-agent.md  (single file)       │   │
│  │                                                        │   │
│  │ Contains (inline):                                     │   │
│  │ - YAML frontmatter (name, description, tools, model)  │   │
│  │ - Routing logic                                       │   │
│  │ - Guardrails                                          │   │
│  │ - Workflow instructions                               │   │
│  └──────────────────────────────────────────────────────┘   │
│                           │                                   │
│                           │ Routes to skills based on context │
│                           ↓                                   │
├─────────────────────────────────────────────────────────────┤
│  Layer 2: WORKFLOW SKILLS (Regular Skills)                   │
│  ┌──────────────────────┐  ┌───────────────────────────┐    │
│  │ pattern-skill/       │  │ process-skill/            │    │
│  │ ├── SKILL.md  ✅     │  │ ├── SKILL.md  ✅          │    │
│  │ └── references/       │  │ └── references/           │    │
│  └──────────────────────┘  └───────────────────────────┘    │
│           │                           │                       │
│           │ Uses primitives           │ May use primitives   │
│           ↓                           ↓                       │
├─────────────────────────────────────────────────────────────┤
│  Layer 1: PRIMITIVES (Skills with Scripts)                   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ domain-commands/  (This is a SKILL! ✅)              │   │
│  │ ├── SKILL.md                                          │   │
│  │ ├── scripts/          (Python scripts bundled here)   │   │
│  │ │   ├── validate_pattern.py                          │   │
│  │ │   └── apply_transformation.py                      │   │
│  │ └── references/                                       │   │
│  │     └── command-contracts.yaml                        │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘

KEY INSIGHT: Layers 1 and 2 are ALL SKILLS (packageable, portable).
            Layer 3 is single .md files (project-specific coordination).
```

### Design Principles

1. **Skills Stay Skills**
   - All follow skill-creator pattern
   - All are packageable and portable
   - All are self-contained

2. **Layers Define Roles, Not Structure**
   - Layer 1: Skills that provide atomic operations
   - Layer 2: Skills that implement workflows
   - Layer 3: Files that coordinate routing

3. **Portability First**
   - Skills work anywhere
   - No external dependencies
   - Distributable as .zip

---

## Book Chapter Processing Workflow

### Phase 1: Chapter Analysis (30-60 minutes per chapter)

**Goal:** Extract actionable knowledge from book chapters

**Process:**

1. **Read and Annotate Chapter**
   ```markdown
   Read chapter: [Title]
   Book: [Book Name]
   Author: [Author]

   Key concepts identified:
   - Concept 1: [Description]
   - Concept 2: [Description]
   - Pattern 1: [Description]
   ```

2. **Identify Skill Opportunities**

   **Ask these questions:**
   - What **operations** can be automated? → Layer 1 candidate
   - What **workflows** are described? → Layer 2 candidate
   - What **decision-making** is involved? → Layer 3 candidate

   **Example from "Refactoring" book:**
   - **Operations:** Extract method, rename variable, move class → Layer 1
   - **Workflows:** Code smell detection → fix → verify → Layer 2
   - **Decision-making:** When to refactor, what pattern to apply → Layer 3

3. **Extract Patterns and Techniques**

   **Create a patterns inventory:**
   ```markdown
   ## Patterns from [Chapter Name]

   ### Pattern 1: [Name]
   **Description:** [What it is]
   **When to Use:** [Context]
   **How it Works:** [Steps]
   **Example:** [Code or scenario]

   ### Pattern 2: [Name]
   [Repeat structure]
   ```

4. **Identify Code Examples**

   **Catalog examples:**
   - Short examples (10-30 lines) → Include in SKILL.md
   - Long examples (50+ lines) → Extract to references/
   - Multiple variations → Create references/examples.md

5. **Map to 3-Layer Architecture**

   **Decision Tree:**
   ```
   Is it an atomic operation? (YES/NO)
     ├─ YES → Layer 1 (Primitive)
     │   └─ Can it be a Python script? (YES/NO)
     │       ├─ YES → Create primitive with script
     │       └─ NO → Create primitive skill (no script)
     │
     └─ NO → Is it a multi-step process? (YES/NO)
         ├─ YES → Layer 2 (Workflow Skill)
         │
         └─ NO → Is it about decision-making/routing? (YES/NO)
             ├─ YES → Layer 3 (Subagent enhancement)
             └─ NO → Reference material only
   ```

### Phase 2: Knowledge Distillation (1-2 hours per chapter)

**Goal:** Transform raw knowledge into structured skill components

**Process:**

1. **Create Knowledge Map**

   ```markdown
   # Knowledge Map: [Chapter Title]

   ## Core Concepts
   - Concept A: [1-2 sentence summary]
   - Concept B: [1-2 sentence summary]

   ## Actionable Patterns
   Pattern 1: [Name] → Workflow skill candidate
   Pattern 2: [Name] → Primitive candidate

   ## Decision Frameworks
   Framework 1: [Name] → Subagent routing logic

   ## Examples Catalog
   - Example 1: [Type] - [Length] - [Use case]
   - Example 2: [Type] - [Length] - [Use case]

   ## Skill Recommendations
   - Layer 1: [Primitive skill name] - [Purpose]
   - Layer 2: [Workflow skill name] - [Purpose]
   - Layer 3: [Subagent update] - [Purpose]
   ```

2. **Define Skill Contracts**

   For each skill identified, create contract:

   ```yaml
   ---
   name: skill-name
   description: Brief description from chapter
   acceptance:
     - criterion_1: "What must be true"
     - criterion_2: "What must be true"
   inputs:
     input_name:
       type: string
       required: true
       description: "What this represents"
   outputs:
     output_name:
       type: string
       description: "What this produces"
   telemetry:
     emit: "skill.skill-name.completed"
     track:
       - metric_1
       - duration_ms
   source:
     book: "Book Title"
     chapter: "Chapter Number"
     author: "Author Name"
   ---
   ```

3. **Extract Reference Material**

   Create references that will go in skill's `references/` directory:

   - `patterns.md` - Patterns from chapter
   - `examples.md` - Detailed code examples
   - `techniques.md` - Step-by-step techniques
   - `decision-trees.md` - Decision frameworks
   - `checklists.md` - Validation checklists

### Phase 3: Skill Creation (2-8 hours per skill)

**Goal:** Create production-ready skills following 3-layer architecture

**Process:** See detailed sections below for each layer

---

## Layer 1: Creating Primitives from Books

### What Are Primitives?

**Primitives are skills that bundle executable scripts for atomic operations.**

They follow the exact same skill-creator pattern, but include a `scripts/` directory with executable code.

### When to Create Primitives from Book Content

**Create primitives when book describes:**
- ✅ Algorithmic operations (e.g., sorting, searching)
- ✅ Transformations (e.g., code refactoring, data conversion)
- ✅ Validations (e.g., pattern checking, constraint validation)
- ✅ Analysis operations (e.g., complexity calculation, metric extraction)
- ✅ Generation tasks (e.g., code generation, template expansion)

**Examples from common books:**
- **"Refactoring" book** → extract-method, rename-variable, move-class primitives
- **"Design Patterns" book** → apply-pattern, validate-pattern primitives
- **"Clean Code" book** → measure-complexity, detect-code-smell primitives
- **"Test-Driven Development" book** → generate-test-stub, calculate-coverage primitives

### Primitive Creation Process

**Step 1: Define the Primitive (30 minutes)**

```markdown
## Primitive Definition

**Name:** [kebab-case-name]
**Source:** [Book Title, Chapter X]
**Purpose:** [One-sentence description]

**Operation Type:** [Transformation/Validation/Analysis/Generation]

**Inputs:**
- Input 1: [Type] - [Description]
- Input 2: [Type] - [Description]

**Outputs:**
- Output 1: [Type] - [Description]
- Output 2: [Type] - [Description]

**Algorithm from Book:**
[Summarize the algorithm/technique from the chapter]

**Determinism:** YES/NO (Same inputs always produce same outputs?)
**Testability:** [How can this be unit tested?]
```

**Step 2: Create Directory Structure (5 minutes)**

```bash
# Create primitive skill directory
mkdir -p .claude/skills/[domain]-commands
mkdir -p .claude/skills/[domain]-commands/scripts
mkdir -p .claude/skills/[domain]-commands/references

# Example: Refactoring primitives from "Refactoring" book
mkdir -p .claude/skills/refactoring-commands
mkdir -p .claude/skills/refactoring-commands/scripts
mkdir -p .claude/skills/refactoring-commands/references
```

**Step 3: Write SKILL.md (1-2 hours)**

```markdown
---
name: [domain]-commands
description: Atomic operations for [domain] based on [Book Title] patterns
source:
  book: "[Book Title]"
  author: "[Author Name]"
  chapters: [1, 3, 5]
---

# [Domain] Commands

## Overview

Provides deterministic, testable command primitives for [domain] operations based on patterns and techniques from **[Book Title]** by [Author].

## Available Commands

### command_1

**Purpose:** [From book chapter X]

**Usage:**
```bash
python scripts/command_1.py --input <value> --output json
```

**Algorithm:**
[Brief description of algorithm from book]

**Returns:**
```json
{
  "success": true,
  "outputs": {
    "result": "...",
    "metrics": {...}
  },
  "telemetry": {...},
  "errors": []
}
```

**Example:**
```bash
python scripts/command_1.py --input "example" --output json
```

**See:** `references/command_1_details.md` for complete algorithm description

---

### command_2

[Repeat structure for each command]

---

## Command Contracts

All commands follow this JSON I/O contract:

**Input:** Command-line arguments or JSON file
**Output:** Structured JSON response

**Response Structure:**
```json
{
  "success": boolean,
  "outputs": {
    // Command-specific outputs
  },
  "telemetry": {
    "command": "command_name",
    "duration_ms": number,
    "book_reference": "Chapter X, Page Y"
  },
  "errors": [
    {
      "type": "error_type",
      "message": "Error description",
      "context": {...}
    }
  ]
}
```

## Using from Other Skills

```markdown
### Step X: Apply [Technique from Book]

Execute [domain]-commands:
```bash
python .claude/skills/[domain]-commands/scripts/command_name.py \
  --input <value> \
  --output json
```

Parse response:
- Check `success == true`
- Extract `outputs.result`
- Use in workflow

If command fails:
- Review `errors` array
- Handle gracefully or escalate
```

## Reference Files

- `references/algorithms.md` - Detailed algorithms from book
- `references/patterns.md` - Patterns these commands implement
- `references/command-contracts.yaml` - Formal command specifications

## Book References

This skill implements techniques from:
- [Book Title] by [Author]
- Chapters: [List]
- Patterns: [List]

---

*Derived from [Book Title] - [Author]*
```

**Step 4: Write Python Scripts (2-4 hours per script)**

```python
#!/usr/bin/env python3
"""
Command: [command_name]
Source: [Book Title], Chapter [X], Page [Y]
Pattern: [Pattern Name]

Description:
[Brief description of what this command does, referencing the book]

Algorithm:
[Pseudocode or description of algorithm from book]

Example:
    python command_name.py --input "value" --output json
"""

import json
import sys
import argparse
from typing import Dict, Any, List
from pathlib import Path

# Import any required libraries
# Keep dependencies minimal for portability


def [command_name](input_param: str, **kwargs) -> Dict[str, Any]:
    """
    [Command description from book]

    Algorithm from [Book Title, Chapter X]:
    1. [Step 1 from book]
    2. [Step 2 from book]
    3. [Step 3 from book]

    Args:
        input_param: [Description]
        **kwargs: Additional parameters

    Returns:
        Dict with success, outputs, telemetry, errors
    """
    try:
        # Initialize response
        response = {
            "success": True,
            "outputs": {},
            "telemetry": {
                "command": "[command_name]",
                "book_reference": "[Book Title, Chapter X]",
                "duration_ms": 0
            },
            "errors": []
        }

        # Start timing
        import time
        start_time = time.time()

        # ========================================
        # IMPLEMENT ALGORITHM FROM BOOK HERE
        # ========================================

        # Step 1: [From book]
        # ...

        # Step 2: [From book]
        # ...

        # Step 3: [From book]
        # ...

        # ========================================

        # Calculate duration
        duration_ms = int((time.time() - start_time) * 1000)
        response["telemetry"]["duration_ms"] = duration_ms

        # Set outputs
        response["outputs"] = {
            "result": "...",  # Command-specific output
            "metrics": {}     # Relevant metrics
        }

        return response

    except Exception as e:
        return {
            "success": False,
            "outputs": {},
            "telemetry": {
                "command": "[command_name]",
                "duration_ms": 0
            },
            "errors": [
                {
                    "type": type(e).__name__,
                    "message": str(e),
                    "context": {"input": input_param}
                }
            ]
        }


def main():
    """Command-line interface"""
    parser = argparse.ArgumentParser(
        description="[Command description from book]"
    )
    parser.add_argument(
        "--input",
        required=True,
        help="[Input description]"
    )
    parser.add_argument(
        "--output",
        default="json",
        choices=["json", "pretty"],
        help="Output format"
    )

    args = parser.parse_args()

    # Execute command
    result = [command_name](args.input)

    # Output result
    if args.output == "pretty":
        print(json.dumps(result, indent=2))
    else:
        print(json.dumps(result))

    # Exit with appropriate code
    sys.exit(0 if result["success"] else 1)


if __name__ == "__main__":
    main()
```

**Step 5: Create Reference Files (1-2 hours)**

**`references/algorithms.md`:**
```markdown
# Algorithms from [Book Title]

## Command 1: [Name]

**Source:** [Book Title], Chapter [X], Pages [Y-Z]

**Algorithm Description:**

[Detailed description of algorithm from book]

**Pseudocode:**
```
function algorithm_name(input):
    step 1: [from book]
    step 2: [from book]
    step 3: [from book]
    return result
```

**Complexity:** [Time and space complexity from book]

**Trade-offs:** [Discussed in book]

---

## Command 2: [Name]

[Repeat structure]
```

**`references/patterns.md`:**
```markdown
# Patterns Implemented

These commands implement the following patterns from [Book Title]:

## Pattern 1: [Pattern Name]

**Chapter:** [X]
**Pages:** [Y-Z]

**Intent:** [From book]

**Applicability:** [When to use, from book]

**Structure:** [Diagram or description from book]

**Implementation:** See `scripts/[command_name].py`

---

## Pattern 2: [Pattern Name]

[Repeat structure]
```

**`references/command-contracts.yaml`:**
```yaml
# Command Contracts for [Domain] Commands
# Source: [Book Title] by [Author]

commands:
  command_1:
    name: "command_1"
    description: "[From book]"
    book_reference:
      title: "[Book Title]"
      chapter: X
      pages: [Y, Z]
      pattern: "[Pattern Name]"

    inputs:
      - name: "input_param"
        type: "string"
        required: true
        description: "[Description]"

    outputs:
      - name: "result"
        type: "string"
        description: "[Description]"
      - name: "metrics"
        type: "object"
        description: "[Description]"

    errors:
      - type: "ValidationError"
        when: "Input validation fails"
      - type: "ProcessingError"
        when: "Algorithm execution fails"

  command_2:
    # [Repeat structure]
```

**Step 6: Test Primitives (1-2 hours)**

```python
# tests/test_command_1.py

import pytest
import json
from pathlib import Path
import sys

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from command_1 import command_1


def test_command_1_success():
    """Test successful execution"""
    result = command_1("valid_input")

    assert result["success"] == True
    assert "result" in result["outputs"]
    assert result["telemetry"]["duration_ms"] > 0


def test_command_1_validation_error():
    """Test input validation"""
    result = command_1("invalid_input")

    assert result["success"] == False
    assert len(result["errors"]) > 0
    assert result["errors"][0]["type"] == "ValidationError"


def test_command_1_algorithm_correctness():
    """
    Test algorithm correctness against examples from book

    Example from [Book Title], Chapter X, Page Y
    """
    # Use example from book
    input_value = "example_from_book"
    expected_output = "expected_result_from_book"

    result = command_1(input_value)

    assert result["success"] == True
    assert result["outputs"]["result"] == expected_output


# Run with: pytest tests/
```

**Step 7: Validate and Package (30 minutes)**

```bash
# Test all commands
pytest .claude/skills/[domain]-commands/tests/

# Package skill
cd ~/.claude/plugins/.../skill-creator
python scripts/package_skill.py /path/to/[domain]-commands

# Verify package
ls -lh [domain]-commands.zip

# Extract and test in different location
unzip [domain]-commands.zip -d /tmp/test
# Verify all scripts work from new location
```

### Primitive Creation Checklist

- [ ] Primitive clearly maps to book technique/algorithm
- [ ] SKILL.md created with book references
- [ ] Python scripts implement algorithms from book
- [ ] Scripts follow JSON I/O contract
- [ ] Reference files document algorithms and patterns
- [ ] Unit tests validate correctness against book examples
- [ ] Skill is packageable and portable
- [ ] Book attribution included (title, author, chapter)

---

## Layer 2: Creating Workflow Skills from Books

### What Are Workflow Skills?

**Workflow skills implement multi-step processes that may compose primitive skills.**

They follow the standard skill-creator pattern (SKILL.md + references/).

### When to Create Workflow Skills from Book Content

**Create workflow skills when book describes:**
- ✅ Multi-step methodologies (e.g., TDD cycle, refactoring workflow)
- ✅ Design processes (e.g., pattern selection, architecture design)
- ✅ Analysis frameworks (e.g., code review checklist, quality assessment)
- ✅ Development workflows (e.g., feature implementation, bug fixing)
- ✅ Planning processes (e.g., estimation techniques, story breakdown)

**Examples from common books:**
- **"Test-Driven Development" book** → tdd-workflow skill
- **"Refactoring" book** → refactor-code-smell skill
- **"Clean Architecture" book** → design-clean-architecture skill
- **"Design Patterns" book** → apply-design-pattern skill
- **"Domain-Driven Design" book** → model-domain skill

### Workflow Skill Creation Process

**Step 1: Extract Workflow from Book (1 hour)**

```markdown
## Workflow Extraction: [Workflow Name]

**Source:** [Book Title], Chapter [X]
**Author:** [Author Name]

**Workflow Description:**
[Summarize the workflow in 2-3 paragraphs]

**Steps from Book:**
1. [Step 1 from book] - [Page reference]
2. [Step 2 from book] - [Page reference]
3. [Step 3 from book] - [Page reference]
4. [Step 4 from book] - [Page reference]

**Decision Points:**
- At Step X: [Decision criteria from book]
- At Step Y: [Alternative paths from book]

**Success Criteria from Book:**
- [Criterion 1]
- [Criterion 2]
- [Criterion 3]

**Common Pitfalls (from book):**
- [Pitfall 1] - [How to avoid]
- [Pitfall 2] - [How to avoid]

**Examples from Book:**
- Example 1: [Chapter X, Page Y] - [Brief description]
- Example 2: [Chapter X, Page Y] - [Brief description]
```

**Step 2: Create Skill Directory Structure (5 minutes)**

```bash
# Create workflow skill directory
mkdir -p .claude/skills/[domain]/[skill-name]
mkdir -p .claude/skills/[domain]/[skill-name]/references

# Example: TDD workflow from "Test-Driven Development" book
mkdir -p .claude/skills/development/tdd-workflow
mkdir -p .claude/skills/development/tdd-workflow/references
```

**Step 3: Write SKILL.md (2-3 hours)**

```markdown
---
name: [skill-name]
description: [One-line description from book]
acceptance:
  - criterion_1: "[From book's success criteria]"
  - criterion_2: "[From book's success criteria]"
inputs:
  input_name:
    type: string
    required: true
    description: "[What this represents]"
outputs:
  output_name:
    type: boolean
    description: "[What this produces]"
telemetry:
  emit: "skill.[skill-name].completed"
  track:
    - metric_1
    - metric_2
    - duration_ms
source:
  book: "[Book Title]"
  chapter: [X]
  author: "[Author Name]"
  methodology: "[Methodology name from book]"
---

# [Skill Name]

## Purpose

[2-3 paragraphs explaining the workflow and its context from the book]

**Based on methodology from:**
- **Book:** [Book Title] by [Author Name]
- **Chapter:** [X] - "[Chapter Title]"
- **Methodology:** [Methodology Name]

## Prerequisites

- [Prerequisite 1 from book]
- [Prerequisite 2 from book]
- [Tool/Dependency if needed]

---

## Workflow

[Brief overview of the complete workflow]

**Workflow Origin:** This workflow implements the [Methodology Name] from [Book Title], Chapter [X].

---

### Step 1: [Step Name from Book]

**Purpose:** [What this step achieves, from book]

**From Book ([Chapter X, Page Y]):**
> [Optional: Short quote from book explaining this step]

**Actions:**
1. [Action 1 from book]
2. [Action 2 from book]
3. [Action 3 from book]

**Key Principles (from book):**
- [Principle 1]
- [Principle 2]

**Example:**
```[language]
// Short example (10-30 lines) from book or adapted from book
```

**Common Mistakes (from book):**
- ❌ [Mistake 1] - [Why it's wrong, from book]
- ❌ [Mistake 2] - [Why it's wrong, from book]

**See:** `references/step-1-details.md` for detailed guidance

---

### Step 2: [Step Name from Book]

[Repeat structure for each workflow step]

**Decision Point:** [If book describes branching logic]
```
Should we do X or Y?
├─ Condition A (from book) → Use approach X
└─ Condition B (from book) → Use approach Y
```

---

### Step 3: [Step Name from Book]

[Continue for all steps...]

---

## Common Scenarios

### Scenario 1: [Scenario from Book]

**Context:** [When this scenario occurs, from book]

**Approach from Book:**
[How the book recommends handling this scenario]

**Example:** [Chapter X, Page Y]

**See:** `references/scenarios.md` for complete scenario coverage

---

### Scenario 2: [Another Scenario from Book]

[Repeat structure]

---

## Best Practices from [Book Title]

1. **[Practice 1 Name]** - [Brief description from book]
   - Chapter [X], Page [Y]
   - Key insight: [From book]

2. **[Practice 2 Name]** - [Brief description from book]
   - Chapter [X], Page [Y]
   - Key insight: [From book]

[Continue for key practices from book]

**See:** `references/best-practices.md` for comprehensive best practices

---

## Validation Checklist

Based on success criteria from [Book Title], Chapter [X]:

- [ ] [Criterion 1 from book]
- [ ] [Criterion 2 from book]
- [ ] [Criterion 3 from book]
- [ ] [Criterion 4 from book]

---

## Reference Files

- `references/workflow-details.md` - Complete step-by-step workflow
- `references/scenarios.md` - Detailed scenario handling
- `references/best-practices.md` - Best practices from book
- `references/examples.md` - Extended examples from book
- `references/patterns.md` - Related patterns from book

---

## When to Escalate

- [Escalation trigger 1 from book]
- [Escalation trigger 2 from book]
- [Escalation trigger 3 from book]

---

## Book References

This skill implements the **[Methodology Name]** from:

**Primary Source:**
- Title: [Book Title]
- Author: [Author Name]
- Chapter: [X] - "[Chapter Title]"
- Pages: [Y-Z]

**Related Chapters:**
- Chapter [A]: [Topic]
- Chapter [B]: [Topic]

**Further Reading:**
- [Related book or article]
- [Related book or article]

---

*Derived from [Book Title] by [Author Name] - [Methodology Name]*
```

**Step 4: Create Reference Files (2-4 hours)**

**`references/workflow-details.md`:**
```markdown
# Detailed Workflow: [Workflow Name]

**Source:** [Book Title], Chapter [X], Pages [Y-Z]

## Complete Workflow

This document provides the complete, detailed workflow as described in [Book Title].

---

## Step 1: [Step Name]

**From Book (Page [X]):**
> [Longer quote from book if applicable]

**Detailed Process:**

1. **[Sub-step 1]**
   - [Detailed description]
   - [Example from book]
   - [Tips from book]

2. **[Sub-step 2]**
   - [Detailed description]
   - [Example from book]
   - [Considerations from book]

3. **[Sub-step 3]**
   - [Detailed description]
   - [Example from book]
   - [Common pitfalls from book]

**Decision Tree:**
```
[If book provides decision logic, create tree]
Question from book?
├─ YES → [Action A from book]
│   └─ Sub-question?
│       ├─ YES → [Action A1]
│       └─ NO → [Action A2]
└─ NO → [Action B from book]
```

**Examples from Book:**

**Example 1: [Title] (Chapter [X], Page [Y])**
```[language]
[Complete example from book]
```

**Analysis:**
[What the book says about this example]

**Example 2: [Title] (Chapter [X], Page [Y])**
[Repeat structure]

---

## Step 2: [Step Name]

[Repeat structure for each step with full detail]

---

## Workflow Variations

**Variation 1: [Name]**

**When to Use:** [From book]

**How it Differs:**
- [Difference 1 from book]
- [Difference 2 from book]

**Example:** [Chapter X, Page Y]

---

## Integration with Other Workflows

[If book discusses how this workflow relates to other methodologies]

---

## Historical Context

[If book provides background on how this methodology evolved]

---

## Author's Insights

[Key insights from the author that aren't captured elsewhere]
```

**`references/scenarios.md`:**
```markdown
# Scenarios: [Workflow Name]

**Source:** [Book Title]

This document covers common scenarios and edge cases discussed in the book.

---

## Scenario 1: [Scenario Name]

**Source:** Chapter [X], Page [Y]

**Context:**
[When this scenario occurs]

**Challenge:**
[What makes this scenario difficult]

**Book's Recommendation:**

**Step 1:** [Approach from book]
[Detailed explanation]

**Step 2:** [Next action from book]
[Detailed explanation]

**Step 3:** [Resolution from book]
[Detailed explanation]

**Example from Book:**
```[language]
[Code or detailed example]
```

**Key Takeaways:**
- [Lesson 1 from book]
- [Lesson 2 from book]

---

## Scenario 2: [Another Scenario]

[Repeat structure]

---

## Anti-Patterns to Avoid

**Anti-Pattern 1: [Name]**

**Description:** [From book]

**Why It's Wrong:** [Explanation from book]

**Instead, Do This:** [Correct approach from book]

**Example:**
```[language]
// Anti-pattern (from book)
[Bad code]

// Correct approach (from book)
[Good code]
```

---

## Edge Cases

**Edge Case 1: [Description]**
- **Discussed in:** Chapter [X], Page [Y]
- **Solution:** [From book]

**Edge Case 2: [Description]**
- **Discussed in:** Chapter [X], Page [Y]
- **Solution:** [From book]
```

**`references/best-practices.md`:**
```markdown
# Best Practices from [Book Title]

**Author:** [Author Name]

This document compiles best practices and principles from across the book.

---

## Core Principles

### Principle 1: [Name]

**Source:** Chapter [X], Page [Y]

**Statement:**
> [Quote from book]

**Explanation:**
[Detailed explanation from book]

**Application:**
[How to apply this principle]

**Example:**
```[language]
[Code example demonstrating principle]
```

**Related Principles:**
- [Principle A]
- [Principle B]

---

### Principle 2: [Name]

[Repeat structure]

---

## Guidelines by Context

### Context 1: [When X]

**From Book:** Chapter [Y]

**Do:**
- ✅ [Guideline 1 from book]
- ✅ [Guideline 2 from book]

**Don't:**
- ❌ [Anti-pattern 1 from book]
- ❌ [Anti-pattern 2 from book]

**Example:** [Chapter X, Page Y]

---

### Context 2: [When Y]

[Repeat structure]

---

## Checklist

**Quality Checklist from [Book Title]:**

- [ ] [Check 1 from book]
- [ ] [Check 2 from book]
- [ ] [Check 3 from book]
- [ ] [Check 4 from book]

**Source:** Chapter [X], Page [Y]

---

## Common Mistakes

**Mistake 1: [Description]**
- **Why it happens:** [From book]
- **Impact:** [From book]
- **Prevention:** [From book]
- **Source:** Chapter [X], Page [Y]

**Mistake 2: [Description]**
[Repeat structure]

---

## Advanced Techniques

**Technique 1: [Name]**

**Level:** [Beginner/Intermediate/Advanced]

**Source:** Chapter [X], Page [Y]

**Description:**
[From book]

**When to Use:**
[From book]

**How it Works:**
1. [Step 1 from book]
2. [Step 2 from book]
3. [Step 3 from book]

**Example:**
```[language]
[Code example from book]
```
```

**`references/examples.md`:**
```markdown
# Examples from [Book Title]

This document provides extended examples from the book.

---

## Example 1: [Title]

**Source:** Chapter [X], Pages [Y-Z]

**Context:**
[What problem this example addresses]

**Before:**
```[language]
[Code before applying technique - from book]
```

**Applying [Technique Name]:**

**Step 1:** [From book]
```[language]
[Intermediate code]
```

**Step 2:** [From book]
```[language]
[Intermediate code]
```

**Step 3:** [From book]
```[language]
[Intermediate code]
```

**After:**
```[language]
[Final code - from book]
```

**Analysis from Book:**
[What the author says about this example]

**Key Insights:**
- [Insight 1 from book]
- [Insight 2 from book]

---

## Example 2: [Title]

[Repeat structure]

---

## Real-World Applications

**Application 1: [Domain]**

**From:** Chapter [X], Page [Y]

**Scenario:**
[Real-world scenario from book]

**Solution:**
[How the book's technique applies]

**Code:**
```[language]
[Example code]
```

**Results:**
[Outcomes discussed in book]

---

## Practice Exercises

**Exercise 1: [Title]**

**Source:** Chapter [X], Page [Y]

**Problem:**
[Exercise from book]

**Hints:**
- [Hint 1 from book]
- [Hint 2 from book]

**Solution:**
```[language]
[Solution from book or derived]
```

**Learning Points:**
- [Point 1]
- [Point 2]
```

**Step 5: Validation and Testing (1-2 hours)**

```bash
# Create validation checklist based on book's success criteria
cat > .claude/skills/[domain]/[skill-name]/validation-checklist.md <<EOF
# Validation Checklist for [Skill Name]

Based on [Book Title], Chapter [X]

## Success Criteria from Book

- [ ] [Criterion 1] - Page [Y]
- [ ] [Criterion 2] - Page [Z]
- [ ] [Criterion 3] - Page [A]

## Quality Gates from Book

- [ ] [Gate 1]
- [ ] [Gate 2]

## Common Pitfalls Check

- [ ] Avoided [Pitfall 1] from Page [X]
- [ ] Avoided [Pitfall 2] from Page [Y]

## Book's Best Practices

- [ ] Applied [Practice 1]
- [ ] Applied [Practice 2]

---

**If all checks pass:** Workflow implemented correctly per [Book Title]
**If any fail:** Review corresponding chapter and references
EOF

# Test skill with example from book
# [Manually test the workflow using an example scenario from the book]

# Validate skill structure
ls -la .claude/skills/[domain]/[skill-name]/
# Should show:
# - SKILL.md
# - references/
# - validation-checklist.md

# Package skill
cd ~/.claude/plugins/.../skill-creator
python scripts/package_skill.py /path/to/[skill-name]
```

**Step 6: Package and Distribute (30 minutes)**

```bash
# Final validation
pytest .claude/skills/[domain]/[skill-name]/tests/ # If tests exist

# Package
python scripts/package_skill.py .claude/skills/[domain]/[skill-name]

# Verify
unzip -l [skill-name].zip

# Test in isolation
unzip [skill-name].zip -d /tmp/test-skill
# Verify references work, all paths are relative
```

### Workflow Skill Creation Checklist

- [ ] Workflow maps clearly to book's methodology
- [ ] SKILL.md documents workflow with book references
- [ ] Each step includes page references to book
- [ ] Common scenarios from book covered
- [ ] Best practices from book documented
- [ ] Reference files provide detailed guidance
- [ ] Examples from book included or adapted
- [ ] Book attribution complete (title, author, chapter, pages)
- [ ] Skill is packageable and portable
- [ ] Validation checklist based on book's success criteria

---

## Layer 3: Creating Subagents from Books

### What Are Subagents?

**Subagents are coordination files (single .md) that route requests to appropriate skills based on context.**

They are NOT skills. They don't follow skill-creator pattern.

**File location:** `.claude/agents/[name].md` (single file, not a directory)

### When to Create/Update Subagents from Book Content

**Create or update subagents when book describes:**
- ✅ Decision-making frameworks (when to use which technique)
- ✅ Role-based workflows (different approaches for different roles)
- ✅ Context-aware routing (complexity-based strategy selection)
- ✅ Expertise domains (specialized agent personas)
- ✅ Quality gates and guardrails (safety checks)

**Examples from common books:**
- **"Refactoring" book** → Refactoring specialist subagent (routes to appropriate refactoring skills)
- **"Design Patterns" book** → Pattern architect subagent (selects appropriate pattern)
- **"Clean Architecture" book** → Architecture reviewer subagent (validates architecture decisions)
- **"Pragmatic Programmer" book** → Code reviewer subagent (applies book's principles)
- **"Test-Driven Development" book** → TDD coach subagent (guides TDD workflow)

### Subagent Creation Process

**Step 1: Define Subagent Persona from Book (30-45 minutes)**

```markdown
## Subagent Persona Definition

**Name:** [agent-name]
**Source Book:** [Book Title] by [Author]
**Based On:** [Role/persona from book or implied expertise]

**Expertise Domain:**
[What this subagent specializes in, based on book's scope]

**Responsibilities (from book):**
1. [Responsibility 1 - Chapter X]
2. [Responsibility 2 - Chapter Y]
3. [Responsibility 3 - Chapter Z]

**Decision-Making Framework:**
[How this subagent decides what to do - extract from book]

Example from book (Chapter X):
- When [condition A] → [action A]
- When [condition B] → [action B]
- When [condition C] → [action C]

**Guardrails (from book's principles):**
- Hard limit 1: [From book]
- Hard limit 2: [From book]
- Warning trigger 1: [From book]

**Personality/Style (if book implies):**
[How this subagent communicates, based on book's tone or role]
```

**Step 2: Map Book Content to Skills (30-45 minutes)**

```markdown
## Skills Mapping for [Subagent Name]

**From [Book Title]:**

### Technique 1: [Name] (Chapter X)
→ **Skill:** [skill-name]
→ **When to use:** [Context from book]
→ **Routing condition:** [Criteria]

### Technique 2: [Name] (Chapter Y)
→ **Skill:** [skill-name]
→ **When to use:** [Context from book]
→ **Routing condition:** [Criteria]

### Technique 3: [Name] (Chapter Z)
→ **Skill:** [skill-name]
→ **When to use:** [Context from book]
→ **Routing condition:** [Criteria]

## Routing Decision Tree (from book)

```
User Request
    │
    ↓
Assess Context (from book's framework)
    ├─ Complexity Assessment (from book)
    │   ├─ Low complexity → Use [skill-1]
    │   ├─ Medium complexity → Use [skill-2]
    │   └─ High complexity → Use [skill-3]
    │
    ├─ Risk Assessment (from book)
    │   ├─ Low risk → Fast approach ([skill-a])
    │   └─ High risk → Careful approach ([skill-b])
    │
    └─ Domain Classification (from book)
        ├─ Domain A → Specialist [skill-x]
        └─ Domain B → Specialist [skill-y]
```

## Guardrails (from book's principles)

**Hard Limits:**
- [Limit 1 from book] - Chapter X, Page Y
- [Limit 2 from book] - Chapter A, Page B

**Escalation Triggers:**
- [Trigger 1 from book]
- [Trigger 2 from book]
```

**Step 3: Create Subagent File (1-2 hours)**

**File:** `.claude/agents/[agent-name].md` (single file)

```markdown
---
name: [agent-name]
description: [One-line description of subagent's role and when to use it]
tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
source:
  book: "[Book Title]"
  author: "[Author Name]"
  methodology: "[Methodology/Role from book]"
---

# [Agent Name] Subagent

## Role

**Expertise:** [Domain expertise from book]

**Based on:** [Book Title] by [Author Name]

This subagent implements decision-making and routing based on the [methodology/framework] described in [Book Title].

**Primary Responsibilities:**
1. [Responsibility 1 - from book]
2. [Responsibility 2 - from book]
3. [Responsibility 3 - from book]

---

## Decision-Making Framework

**From [Book Title], Chapter [X]:**

This subagent uses the [Framework Name] from [Book Title] to determine the appropriate approach for each request.

**Assessment Criteria (from book):**

1. **[Criterion 1]** (Chapter [X], Page [Y])
   - Low: [Definition from book] → [Action/Skill]
   - Medium: [Definition from book] → [Action/Skill]
   - High: [Definition from book] → [Action/Skill]

2. **[Criterion 2]** (Chapter [A], Page [B])
   - [Condition A from book] → [Action/Skill]
   - [Condition B from book] → [Action/Skill]

3. **[Criterion 3]** (Chapter [C], Page [D])
   - [Condition A from book] → [Action/Skill]
   - [Condition B from book] → [Action/Skill]

---

## Command: *[command-name]

### Workflow

**Based on:** [Book Title], Chapter [X] - "[Chapter Title]"

**Step 1: Assess Context**

Evaluate the request using [Framework Name] from book:

**Assessment Questions (from book):**
- [Question 1 from book]
- [Question 2 from book]
- [Question 3 from book]

Calculate [score/classification] based on book's framework:
```
[Formula or logic from book]
```

**Step 2: Select Skill**

**Routing Rules (from book):**

**[Condition A] ([Score/Classification from book]):**
- **Book reference:** Chapter [X], Page [Y]
- **Condition:** [Detailed condition from book]
- **Skill:** `.claude/skills/[domain]/[skill-a]/SKILL.md`
- **Rationale:** [Why this skill, from book]
- **Example scenario:** [From book]

**[Condition B] ([Score/Classification from book]):**
- **Book reference:** Chapter [A], Page [B]
- **Condition:** [Detailed condition from book]
- **Skill:** `.claude/skills/[domain]/[skill-b]/SKILL.md`
- **Rationale:** [Why this skill, from book]
- **Example scenario:** [From book]

**[Condition C] ([Score/Classification from book]):**
- **Book reference:** Chapter [C], Page [D]
- **Condition:** [Detailed condition from book]
- **Skill:** `.claude/skills/[domain]/[skill-c]/SKILL.md`
- **Rationale:** [Why this skill, from book]
- **Example scenario:** [From book]

Execute selected skill with appropriate parameters.

**Step 3: Verify Success**

Check skill outputs against acceptance criteria:

**Success Criteria (from book):**
- ✅ [Criterion 1 from book] - Chapter [X]
- ✅ [Criterion 2 from book] - Chapter [Y]
- ✅ [Criterion 3 from book] - Chapter [Z]

**Quality Gates (from book):**
- [Gate 1 from book] must pass
- [Gate 2 from book] must pass

**Step 4: Emit Telemetry**

Record decision-making and outcomes:
```json
{
  "agent": "[agent-name]",
  "command": "[command-name]",
  "book_methodology": "[Methodology from book]",
  "assessment": {
    "[criterion_1]": "value",
    "[criterion_2]": "value",
    "score": "X"
  },
  "routing": {
    "selected_skill": "[skill-name]",
    "rationale": "[Why this skill, from book]",
    "book_reference": "Chapter X, Page Y"
  },
  "result": {
    "success": true,
    "quality_gates": ["passed", "passed"]
  }
}
```

---

## Guardrails

**From [Book Title]:**

### Hard Limits (Never Exceed)

**Based on Chapter [X], Page [Y]:**

1. **[Limit 1 Name]:** [Description from book]
   - Maximum: [Value from book or derived]
   - Rationale: [Why this limit exists, from book]
   - If exceeded: [Action - escalate or abort]

2. **[Limit 2 Name]:** [Description from book]
   - Maximum: [Value from book or derived]
   - Rationale: [Why this limit exists, from book]
   - If exceeded: [Action - escalate or abort]

3. **[Limit 3 Name]:** [Description from book]
   - Never: [Prohibited action from book]
   - Rationale: [Why this is prohibited, from book]
   - If attempted: [Action - warn and block]

### Quality Gates

**Based on [Book's Quality Framework]:**

**Gate 1: [Name]** (Chapter [A], Page [B])
- Check: [What to verify, from book]
- Pass criteria: [From book]
- Fail action: [From book]

**Gate 2: [Name]** (Chapter [C], Page [D])
- Check: [What to verify, from book]
- Pass criteria: [From book]
- Fail action: [From book]

### Escalation Triggers

**When to escalate to user:**

1. **[Trigger 1]** (from book)
   - Condition: [From book]
   - Reason: [Why escalation needed, from book]
   - Example: [Scenario from book]

2. **[Trigger 2]** (from book)
   - Condition: [From book]
   - Reason: [Why escalation needed, from book]
   - Example: [Scenario from book]

3. **[Trigger 3]** (from book)
   - Condition: [From book]
   - Reason: [Why escalation needed, from book]
   - Example: [Scenario from book]

---

## Commands

### *[command-1]

**Purpose:** [From book]

**Book Reference:** Chapter [X], Page [Y]

**Workflow:** [Brief description]

[Follow "Command: *command-name" structure above]

---

### *[command-2]

**Purpose:** [From book]

**Book Reference:** Chapter [X], Page [Y]

**Workflow:** [Brief description]

[Follow "Command: *command-name" structure above]

---

## Best Practices from [Book Title]

**Principle 1: [Name]**
- **Source:** Chapter [X], Page [Y]
- **Application:** [How this subagent applies principle]
- **Example:** [Scenario]

**Principle 2: [Name]**
- **Source:** Chapter [A], Page [B]
- **Application:** [How this subagent applies principle]
- **Example:** [Scenario]

[Continue for key principles from book that guide this subagent]

---

## Book References

This subagent implements the [Methodology/Framework] from:

**Primary Source:**
- **Title:** [Book Title]
- **Author:** [Author Name]
- **Key Chapters:**
  - Chapter [X]: [Topic] - [Decision framework used]
  - Chapter [Y]: [Topic] - [Routing logic used]
  - Chapter [Z]: [Topic] - [Guardrails derived]

**Methodology:**
- [Methodology Name] - [Brief description from book]

**Related Patterns:**
- [Pattern 1 from book] - Chapter [A]
- [Pattern 2 from book] - Chapter [B]

---

**When to Use This Subagent:**
- [Scenario 1 from book's scope]
- [Scenario 2 from book's scope]
- [Scenario 3 from book's scope]

**When to Use Different Subagent:**
- [Outside book's scope 1] → Use [other-agent]
- [Outside book's scope 2] → Use [other-agent]

---

*Routing and decision-making based on [Book Title] by [Author Name]*
```

**Step 4: Test Subagent Routing (30-60 minutes)**

```bash
# Test routing with scenarios from book

# Scenario 1: Low complexity (from book Chapter X)
# @[agent-name] *command "low complexity request"
# Expected: Routes to [skill-a]

# Scenario 2: High complexity (from book Chapter Y)
# @[agent-name] *command "high complexity request"
# Expected: Routes to [skill-b]

# Scenario 3: Edge case (from book Chapter Z)
# @[agent-name] *command "edge case request"
# Expected: Routes to [skill-c] or escalates

# Verify guardrails
# @[agent-name] *command "request exceeding hard limit"
# Expected: Blocked with warning referencing book principle

# Verify quality gates
# (After skill execution)
# Expected: Quality checks from book applied
```

**Step 5: Documentation (30 minutes)**

```bash
# Create usage guide
cat > docs/agents/[agent-name]-usage.md <<EOF
# Using [Agent Name] Subagent

**Based on:** [Book Title] by [Author Name]

## Overview

This subagent implements [Methodology] from [Book Title].

## When to Use

Use @[agent-name] when:
- [Scenario 1 from book]
- [Scenario 2 from book]
- [Scenario 3 from book]

## Available Commands

### @[agent-name] *command-1

**Purpose:** [From book]

**Example:**
\`\`\`
@[agent-name] *command-1 "description of request"
\`\`\`

**Book Reference:** Chapter [X], Page [Y]

---

### @[agent-name] *command-2

[Repeat structure]

---

## Routing Logic

This subagent uses [Framework Name] from [Book Title] to route requests:

**Assessment Factors:**
1. [Factor 1] - Chapter [X]
2. [Factor 2] - Chapter [Y]
3. [Factor 3] - Chapter [Z]

**Routing Map:**
- [Condition A] → [skill-a] (Chapter [X])
- [Condition B] → [skill-b] (Chapter [Y])
- [Condition C] → [skill-c] (Chapter [Z])

## Guardrails

**Hard Limits from Book:**
- [Limit 1] (Chapter [A], Page [B])
- [Limit 2] (Chapter [C], Page [D])

**Quality Gates:**
- [Gate 1] (Chapter [E], Page [F])
- [Gate 2] (Chapter [G], Page [H])

## Examples from Book

**Example 1:** (Chapter [X], Page [Y])

Request:
\`\`\`
@[agent-name] *command-1 "scenario from book"
\`\`\`

Routing:
- Assessment: [Results]
- Selected Skill: [skill-name]
- Rationale: [Why, from book]

**Example 2:** (Chapter [A], Page [B])
[Repeat structure]

## Book References

- [Book Title] by [Author Name]
- Methodology: [Methodology Name]
- Chapters: [List key chapters]
EOF
```

### Subagent Creation Checklist

- [ ] Persona clearly derived from book's methodology/role
- [ ] Routing logic maps to book's decision framework
- [ ] Each routing condition references book chapter/page
- [ ] Guardrails based on book's principles
- [ ] Quality gates from book's success criteria
- [ ] Skills mapped to book's techniques
- [ ] Escalation triggers from book's guidance
- [ ] Book attribution complete (inline in .md file)
- [ ] Usage guide documents book-based routing
- [ ] Tested with scenarios from book

---

## Complete Examples

### Example 1: "Refactoring" Book → Full 3-Layer Implementation

**Book:** *Refactoring: Improving the Design of Existing Code* by Martin Fowler

**Chapter Used:** Chapter 6 - "A First Set of Refactorings"

#### Layer 1: Refactoring Primitives

**Skill:** `refactoring-commands`

**Primitives Created:**
1. `extract_method.py` - Extract Method refactoring
2. `rename_variable.py` - Rename Variable refactoring
3. `inline_function.py` - Inline Function refactoring
4. `move_class.py` - Move Class refactoring

**File Structure:**
```
.claude/skills/refactoring-commands/
├── SKILL.md
├── scripts/
│   ├── extract_method.py
│   ├── rename_variable.py
│   ├── inline_function.py
│   └── move_class.py
├── references/
│   ├── refactoring-catalog.md (from book's catalog)
│   ├── algorithms.md (detailed algorithms from book)
│   └── command-contracts.yaml
└── tests/
    └── test_refactorings.py
```

**SKILL.md Excerpt:**
```markdown
---
name: refactoring-commands
description: Atomic refactoring operations from Martin Fowler's Refactoring book
source:
  book: "Refactoring: Improving the Design of Existing Code"
  author: "Martin Fowler"
  chapters: [6, 7, 8, 9, 10, 11]
---

# Refactoring Commands

## Overview

Provides deterministic, testable refactoring primitives based on Martin Fowler's canonical refactoring catalog.

## Available Commands

### extract_method

**Source:** Refactoring, Chapter 6, Page 106

**Purpose:** Extract a code fragment into a method of its own

**Algorithm from Book:**
1. Create a new method named after the intent of the method
2. Copy extracted code from source to target
3. Scan for references to variables local in scope
4. Pass local-scope variables as parameters
5. Replace extracted code with call to new method

**Usage:**
```bash
python scripts/extract_method.py \
  --file src/example.js \
  --start-line 10 \
  --end-line 20 \
  --method-name calculateTotal \
  --output json
```

**See:** `references/refactoring-catalog.md#extract-method`

---

[Additional commands...]
```

**Script Example (`scripts/extract_method.py`):**
```python
#!/usr/bin/env python3
"""
Command: extract_method
Source: Refactoring by Martin Fowler, Chapter 6, Page 106
Pattern: Extract Method

Mechanics from book:
1. Create a new method, name it after the intent of the method
2. Copy the extracted code from the source method to the new target method
3. Scan the extracted code for references to variables local in scope to source
4. Pass as parameters to target method if used only in extracted code
5. Replace the extracted code in the source method with call to target method

Example:
    python extract_method.py --file src/calc.js --start-line 10 --end-line 15 \
           --method-name calculateDiscount --output json
"""

import json
import sys
import argparse
import re
from typing import Dict, Any, List
from pathlib import Path


def extract_method(
    file_path: str,
    start_line: int,
    end_line: int,
    method_name: str,
    **kwargs
) -> Dict[str, Any]:
    """
    Extract Method refactoring from Fowler's Refactoring book.

    Implements the mechanics from Chapter 6, Page 106-108.

    Args:
        file_path: Path to source file
        start_line: Start line of code to extract (1-indexed)
        end_line: End line of code to extract (1-indexed)
        method_name: Name for new method
        **kwargs: Additional options

    Returns:
        Dict with success, outputs (refactored code), telemetry, errors
    """
    try:
        response = {
            "success": True,
            "outputs": {},
            "telemetry": {
                "command": "extract_method",
                "book_reference": "Refactoring, Chapter 6, Page 106",
                "pattern": "Extract Method",
                "duration_ms": 0
            },
            "errors": []
        }

        import time
        start_time = time.time()

        # Step 1: Read source file
        source_path = Path(file_path)
        if not source_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        lines = source_path.read_text().splitlines()

        # Validate line numbers
        if start_line < 1 or end_line > len(lines) or start_line > end_line:
            raise ValueError(f"Invalid line range: {start_line}-{end_line}")

        # Step 2: Extract code fragment (Fowler Step 2)
        # Note: Lines are 1-indexed in args, 0-indexed in Python
        extracted_lines = lines[start_line-1:end_line]
        extracted_code = "\n".join(extracted_lines)

        # Step 3: Scan for local variables (Fowler Step 3)
        # Simplified: Find variable references in extracted code
        local_vars = find_local_variables(extracted_code, lines[:start_line-1])

        # Step 4: Generate parameters (Fowler Step 4)
        parameters = ", ".join(local_vars)

        # Step 5: Create new method (Fowler Step 1)
        indentation = get_indentation(lines[start_line-1])
        new_method = generate_method(
            method_name,
            parameters,
            extracted_code,
            indentation
        )

        # Step 6: Replace with call (Fowler Step 5)
        method_call = f"{indentation}{method_name}({parameters});"

        # Build refactored code
        refactored_lines = (
            lines[:start_line-1] +
            [method_call] +
            lines[end_line:]
        )

        # Insert new method (at class/module level)
        insertion_point = find_method_insertion_point(lines, start_line)
        refactored_lines.insert(insertion_point, new_method)

        refactored_code = "\n".join(refactored_lines)

        # Calculate metrics
        duration_ms = int((time.time() - start_time) * 1000)
        response["telemetry"]["duration_ms"] = duration_ms

        # Set outputs
        response["outputs"] = {
            "refactored_code": refactored_code,
            "new_method_name": method_name,
            "parameters": local_vars,
            "lines_extracted": len(extracted_lines),
            "method_signature": f"{method_name}({parameters})"
        }

        return response

    except Exception as e:
        return {
            "success": False,
            "outputs": {},
            "telemetry": {
                "command": "extract_method",
                "duration_ms": 0
            },
            "errors": [
                {
                    "type": type(e).__name__,
                    "message": str(e),
                    "context": {
                        "file": file_path,
                        "line_range": f"{start_line}-{end_line}"
                    }
                }
            ]
        }


def find_local_variables(code: str, context_lines: List[str]) -> List[str]:
    """
    Identify local variables used in extracted code.

    Simplified implementation - production version would use AST parsing.
    """
    # Pattern: variable names (simplified)
    var_pattern = r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b'
    variables = set(re.findall(var_pattern, code))

    # Filter to only variables declared in context
    context_code = "\n".join(context_lines)
    declared_vars = set(re.findall(r'\b(?:let|const|var)\s+([a-zA-Z_][a-zA-Z0-9_]*)', context_code))

    # Return variables used in code that were declared in context
    return sorted(variables & declared_vars)


def get_indentation(line: str) -> str:
    """Get leading whitespace from line"""
    return line[:len(line) - len(line.lstrip())]


def generate_method(name: str, params: str, body: str, indent: str) -> str:
    """Generate new method definition"""
    return f"""
{indent}function {name}({params}) {{
{body}
{indent}}}
"""


def find_method_insertion_point(lines: List[str], current_line: int) -> int:
    """
    Find appropriate place to insert new method.

    Simplified: Insert before current method.
    Production version would use AST to find class/module level.
    """
    # Look backwards for function definition
    for i in range(current_line - 1, -1, -1):
        if 'function' in lines[i]:
            return i
    return current_line - 1


def main():
    """Command-line interface"""
    parser = argparse.ArgumentParser(
        description="Extract Method refactoring (Fowler, Chapter 6)"
    )
    parser.add_argument("--file", required=True, help="Source file path")
    parser.add_argument("--start-line", type=int, required=True, help="Start line")
    parser.add_argument("--end-line", type=int, required=True, help="End line")
    parser.add_argument("--method-name", required=True, help="Name for new method")
    parser.add_argument("--output", default="json", choices=["json", "pretty"])

    args = parser.parse_args()

    result = extract_method(
        args.file,
        args.start_line,
        args.end_line,
        args.method_name
    )

    if args.output == "pretty":
        print(json.dumps(result, indent=2))
    else:
        print(json.dumps(result))

    sys.exit(0 if result["success"] else 1)


if __name__ == "__main__":
    main()
```

#### Layer 2: Refactoring Workflow Skill

**Skill:** `refactor-code-smell`

**Purpose:** Detect code smells and apply appropriate refactorings from Fowler's book

**File Structure:**
```
.claude/skills/development/refactor-code-smell/
├── SKILL.md
└── references/
    ├── code-smells-catalog.md (Chapter 3 from book)
    ├── refactoring-selection.md (Decision trees from book)
    ├── examples.md (Examples from book)
    └── best-practices.md (Fowler's principles)
```

**SKILL.md Excerpt:**
```markdown
---
name: refactor-code-smell
description: Detect and fix code smells using Martin Fowler's refactoring catalog
acceptance:
  - code_smell_identified: "Specific smell from Fowler's catalog identified"
  - appropriate_refactoring_selected: "Correct refactoring chosen per book"
  - tests_passing: "All tests pass after refactoring"
  - code_improved: "Code quality metrics improved"
source:
  book: "Refactoring: Improving the Design of Existing Code"
  author: "Martin Fowler"
  chapters: [3, 6, 7, 8]
  methodology: "Code Smell Detection and Refactoring"
---

# Refactor Code Smell

## Purpose

Systematically detect and eliminate code smells using Martin Fowler's refactoring catalog and methodology.

**Based on:**
- **Book:** Refactoring: Improving the Design of Existing Code by Martin Fowler
- **Chapters:** 3 (Bad Smells in Code), 6-11 (Refactoring Catalog)
- **Methodology:** Smell-Driven Refactoring

## Prerequisites

- Code with tests (Fowler: "Refactoring requires tests")
- refactoring-commands skill available
- Understanding of code smells (see references/code-smells-catalog.md)

---

## Workflow

**From Fowler:** "When you feel the need to write a comment, first try to refactor the code so that any comment becomes superfluous." (Chapter 3)

---

### Step 1: Detect Code Smell

**From Book:** Chapter 3, "Bad Smells in Code"

**Action:** Analyze code for common smells

**Code Smells from Fowler (Top 10):**
1. **Long Method** (Chapter 3, Page 76)
2. **Large Class** (Chapter 3, Page 78)
3. **Long Parameter List** (Chapter 3, Page 78)
4. **Divergent Change** (Chapter 3, Page 79)
5. **Shotgun Surgery** (Chapter 3, Page 80)
6. **Feature Envy** (Chapter 3, Page 80)
7. **Data Clumps** (Chapter 3, Page 81)
8. **Primitive Obsession** (Chapter 3, Page 81)
9. **Switch Statements** (Chapter 3, Page 82)
10. **Duplicate Code** (Chapter 3, Page 76)

**Detection Guidelines:**
- Method > 10 lines → Potential Long Method
- Class > 100 lines → Potential Large Class
- Parameters > 3 → Potential Long Parameter List

**See:** `references/code-smells-catalog.md` for complete catalog

---

### Step 2: Select Refactoring

**From Book:** Chapter 3 provides refactoring recommendations for each smell

**Decision Tree (from Fowler):**

```
Code Smell: Long Method
├─ Extract Method (Chapter 6) - Most common
├─ Replace Temp with Query (Chapter 7) - If temps blocking extraction
├─ Introduce Parameter Object (Chapter 6) - If long param list
└─ Replace Method with Method Object (Chapter 6) - If very complex

Code Smell: Duplicate Code
├─ Same class → Extract Method
├─ Sibling subclasses → Extract Method + Pull Up Method
├─ Unrelated classes → Extract Class
└─ Different algorithms → Form Template Method

[Continue for other smells...]
```

**Refactoring Selection Matrix:**

| Code Smell | Primary Refactoring | Chapter | Alternative |
|------------|-------------------|---------|-------------|
| Long Method | Extract Method | 6 | Replace Temp with Query |
| Duplicate Code | Extract Method | 6 | Pull Up Method |
| Long Parameter List | Introduce Parameter Object | 6 | Preserve Whole Object |
| Large Class | Extract Class | 7 | Extract Subclass |
| Feature Envy | Move Method | 7 | Extract Method |

**See:** `references/refactoring-selection.md` for complete decision trees

---

### Step 3: Apply Refactoring

**Action:** Use refactoring-commands to apply selected refactoring

**Example: Extract Method (most common refactoring)**

From Fowler: "Extract Method is one of the most common refactorings I do."

Execute refactoring-commands:
```bash
python .claude/skills/refactoring-commands/scripts/extract_method.py \
  --file src/calculator.js \
  --start-line 45 \
  --end-line 60 \
  --method-name calculateDiscount \
  --output json
```

Parse response:
- Check `success == true`
- Get `outputs.refactored_code`
- Apply to file

**Fowler's Rule:** "Make sure tests pass before starting refactoring"

---

### Step 4: Run Tests

**From Fowler:** "Whenever I do refactoring, the first step is always the same. I need to build a solid set of tests for that section of code." (Chapter 2, Page 17)

**Action:** Run test suite after each refactoring

**Fowler's Testing Cadence:**
- Test after EVERY refactoring step
- "Never skip tests between refactorings"
- "If tests fail, undo last change"

Execute tests:
```bash
npm test  # Or appropriate test command
```

**If tests fail:**
1. Undo refactoring (Fowler: "Undo is your friend")
2. Review refactoring mechanics from book
3. Try smaller refactoring steps
4. Consider different refactoring

---

### Step 5: Verify Improvement

**Action:** Confirm code quality improved

**Metrics from Fowler:**
- Method length reduced
- Cyclomatic complexity decreased
- Duplication eliminated
- Readability improved ("clear intent")

**Fowler's Definition of Clean Code:**
> "Any fool can write code that a computer can understand. Good programmers write code that humans can understand." (Chapter 1, Page 15)

**Verification Checklist:**
- [ ] Tests still pass
- [ ] Code smell eliminated or reduced
- [ ] Code reads more clearly
- [ ] No new smells introduced

---

## Common Scenarios

### Scenario 1: Long Method with Temp Variables

**From Book:** Chapter 7, "Replace Temp with Query"

**Problem:** Temps prevent extracting code

**Fowler's Solution:**
1. Replace Temp with Query first
2. Then Extract Method
3. Remove inline temps

**Example:** Chapter 7, Page 120

**See:** `references/examples.md#long-method-with-temps`

---

### Scenario 2: Duplicate Code in Subclasses

**From Book:** Chapter 11, "Pull Up Method"

**Problem:** Same code in multiple subclasses

**Fowler's Solution:**
1. Extract Method in each subclass
2. Ensure method signatures identical
3. Pull Up Method to superclass

**Example:** Chapter 11, Page 322

**See:** `references/examples.md#duplicate-in-subclasses`

---

## Best Practices from Fowler

1. **Test First** (Chapter 2)
   - Always ensure tests exist before refactoring
   - "Refactoring requires tests"

2. **Small Steps** (Chapter 2)
   - Refactor in tiny increments
   - Test after each step
   - "Baby steps prevent big mistakes"

3. **Clear Intent** (Chapter 1)
   - Method names should express intent
   - "Code should read like narrative"

4. **Preserve Behavior** (Chapter 1)
   - Refactoring must not change behavior
   - Tests verify behavior preservation

**See:** `references/best-practices.md` for complete principles

---

## Reference Files

- `references/code-smells-catalog.md` - Complete catalog from Chapter 3
- `references/refactoring-selection.md` - Decision trees for each smell
- `references/examples.md` - Extended examples from book
- `references/best-practices.md` - Fowler's refactoring principles

---

## When to Escalate

- Refactoring breaks tests (undo and try smaller steps)
- Unsure which refactoring to apply (consult book/expert)
- Large-scale architectural change needed (beyond single refactoring)

---

## Book References

This skill implements **Smell-Driven Refactoring** from:

**Primary Source:**
- Title: Refactoring: Improving the Design of Existing Code
- Author: Martin Fowler (with Kent Beck and others)
- Key Chapters:
  - Chapter 3: Bad Smells in Code (smell catalog)
  - Chapters 6-11: Refactoring Catalog (techniques)
  - Chapter 2: Principles in Refactoring (methodology)

**Related Chapters:**
- Chapter 1: Refactoring, a First Example
- Chapter 4: Building Tests

---

*Derived from Refactoring by Martin Fowler - Smell-Driven Refactoring*
```

#### Layer 3: Refactoring Specialist Subagent

**Subagent:** `refactoring-specialist`

**Purpose:** Route refactoring requests to appropriate skills based on Fowler's framework

**File:** `.claude/agents/refactoring-specialist.md`

```markdown
---
name: refactoring-specialist
description: Refactoring expert based on Martin Fowler's methodology. Routes to appropriate refactoring skills based on code smell assessment.
tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
source:
  book: "Refactoring: Improving the Design of Existing Code"
  author: "Martin Fowler"
  methodology: "Smell-Driven Refactoring"
---

# Refactoring Specialist Subagent

## Role

**Expertise:** Code refactoring and design improvement

**Based on:** *Refactoring: Improving the Design of Existing Code* by Martin Fowler

This subagent implements smell-driven refactoring methodology from Martin Fowler's canonical refactoring book.

**Primary Responsibilities:**
1. Detect code smells using Fowler's catalog (Chapter 3)
2. Select appropriate refactorings from Fowler's catalog (Chapters 6-11)
3. Apply refactorings safely with test verification
4. Ensure behavior preservation (Fowler's core principle)

---

## Decision-Making Framework

**From Refactoring, Chapter 3: "Bad Smells in Code"**

This subagent uses Fowler's smell-driven approach:
1. Detect smell from catalog
2. Assess severity and impact
3. Select refactoring from catalog
4. Apply with test verification

**Fowler's Philosophy:**
> "When you feel the need to write a comment, first try to refactor the code so that any comment becomes superfluous."

---

## Command: *refactor

### Workflow

**Based on:** Refactoring, Chapter 2 - "Principles in Refactoring"

**Step 1: Assess Code Smells**

**From Book:** Chapter 3, "Bad Smells in Code"

Read code and identify smells from Fowler's catalog:

**Assessment Questions:**
1. Are methods longer than 10-15 lines? → Long Method smell
2. Are classes larger than 100-150 lines? → Large Class smell
3. Is code duplicated across methods/classes? → Duplicate Code smell
4. Are there more than 3-4 parameters? → Long Parameter List smell
5. Does code use primitive types excessively? → Primitive Obsession smell

**Smell Severity Classification (derived from Fowler):**
- **Critical:** Duplicate Code, Long Method (> 50 lines), Large Class (> 300 lines)
- **Major:** Feature Envy, Data Clumps, Switch Statements
- **Minor:** Long Parameter List (4-5 params), Comments (indicating unclear code)

**Calculate refactoring priority:**
```
Priority = (Severity × Impact × Frequency) / Test Coverage

Critical smells → Priority 1
Major smells → Priority 2
Minor smells → Priority 3
```

**Step 2: Select Skill**

**Routing Rules (from Fowler's catalog):**

**Simple Refactoring (single smell, < 20 lines affected):**
- **Book reference:** Chapter 6, Extract Method pattern
- **Condition:** Single smell, isolated location, good test coverage
- **Skill:** `.claude/skills/development/refactor-code-smell/SKILL.md`
- **Rationale:** Direct smell → refactoring mapping from book
- **Example:** Extract long method into smaller methods

**Complex Refactoring (multiple smells, architectural impact):**
- **Book reference:** Chapters 8-9, larger refactorings
- **Condition:** Multiple smells, affects class design, requires design patterns
- **Skill:** `.claude/skills/development/refactor-architecture/SKILL.md`
- **Rationale:** Needs architectural redesign per Fowler's advanced patterns
- **Example:** Replace conditional with polymorphism

**Automated Refactoring (IDE-safe refactorings):**
- **Book reference:** Chapter 6, mechanics sections
- **Condition:** Deterministic refactoring with clear mechanics
- **Use:** `.claude/skills/refactoring-commands/` primitives directly
- **Rationale:** Can be safely automated per Fowler's detailed mechanics
- **Example:** Rename Variable, Extract Method with clear boundaries

Execute selected skill.

**Step 3: Verify Behavior Preservation**

**From Fowler:** "Refactoring must not change observable behavior" (Chapter 1)

Check that tests pass after refactoring:

**Success Criteria (from book):**
- ✅ All tests still pass (behavior preserved)
- ✅ Code smell eliminated or significantly reduced
- ✅ Code readability improved ("clear intent")
- ✅ No new smells introduced

**Fowler's Testing Principle:**
> "Whenever I do refactoring, the first step is always the same. I need to build a solid set of tests for that section of code." (Chapter 2, Page 17)

**If tests fail:**
1. Undo refactoring immediately (Fowler: "Undo is your friend")
2. Review mechanics from book chapter
3. Try smaller refactoring steps
4. Escalate if unsure

**Step 4: Emit Telemetry**

Record refactoring decision and outcome:
```json
{
  "agent": "refactoring-specialist",
  "command": "refactor",
  "book_methodology": "Smell-Driven Refactoring (Fowler)",
  "assessment": {
    "smells_detected": ["Long Method", "Duplicate Code"],
    "severity": "Critical",
    "priority": 1
  },
  "routing": {
    "selected_skill": "refactor-code-smell",
    "refactoring_applied": "Extract Method",
    "book_reference": "Chapter 6, Page 106"
  },
  "result": {
    "success": true,
    "tests_passed": true,
    "lines_reduced": 45,
    "smells_eliminated": ["Long Method"]
  }
}
```

---

## Guardrails

**From Fowler's Refactoring Principles:**

### Hard Limits (Never Exceed)

**Based on Chapter 2, "Principles in Refactoring":**

1. **Never Refactor Without Tests**
   - Must have test suite with good coverage
   - Rationale: "Refactoring requires tests" (Fowler)
   - If no tests: Stop and write tests first

2. **Never Break Tests**
   - Tests must pass after each refactoring step
   - Rationale: Tests verify behavior preservation (Fowler's core principle)
   - If tests fail: Undo immediately

3. **Never Refactor and Add Features Simultaneously**
   - Separate refactoring commits from feature commits
   - Rationale: "Two hats" principle (Fowler, Chapter 2, Page 18)
   - If mixing: Split into separate tasks

### Quality Gates

**Based on Fowler's Success Criteria:**

**Gate 1: Test Verification** (Chapter 2, Page 17)
- Check: All tests pass after refactoring
- Pass criteria: 100% test passage rate
- Fail action: Undo refactoring, review mechanics, try smaller steps

**Gate 2: Behavior Preservation** (Chapter 1, Page 15)
- Check: Observable behavior unchanged
- Pass criteria: Manual verification or integration tests pass
- Fail action: Undo refactoring, identify behavior change, fix

**Gate 3: Code Quality Improvement**
- Check: Metrics improved (length, complexity, duplication)
- Pass criteria: At least one metric improved, none degraded
- Fail action: Reconsider refactoring choice

### Escalation Triggers

**When to escalate to user:**

1. **No Tests Exist** (Fowler: "Refactoring requires tests")
   - Condition: Code has no test suite or insufficient coverage (< 50%)
   - Reason: Cannot safely refactor without tests (Fowler, Chapter 2)
   - Action: Recommend writing tests first, or escalate for user decision

2. **Tests Fail After Multiple Attempts**
   - Condition: Tried 3 different refactoring approaches, tests still fail
   - Reason: May indicate misunderstanding of code or need for manual review
   - Action: Escalate with analysis of failure patterns

3. **Architectural Change Needed** (Beyond Fowler's catalog)
   - Condition: Refactoring requires changing class hierarchies or module boundaries
   - Reason: Large refactorings need human judgment (Fowler, Chapter 2)
   - Example: Needs "Replace Inheritance with Delegation" (Chapter 12)
   - Action: Escalate with recommendation and book reference

4. **Performance Impact Uncertain**
   - Condition: Refactoring may affect performance (e.g., replacing code with method calls)
   - Reason: Fowler addresses this in Chapter 2: "First make it right, then make it fast"
   - Action: Escalate if performance is critical, otherwise apply refactoring

---

## Best Practices from Refactoring

**Principle 1: Test First**
- **Source:** Chapter 2, Page 17
- **Application:** Always verify tests exist and pass before refactoring
- **Quote:** "Whenever I do refactoring, the first step is always the same. I need to build a solid set of tests for that section of code."

**Principle 2: Small Steps**
- **Source:** Chapter 2, Page 19
- **Application:** Refactor in tiny increments, test after each
- **Quote:** "The key to effective refactoring is recognizing that you go faster when you take tiny steps."

**Principle 3: Two Hats**
- **Source:** Chapter 2, Page 18
- **Application:** Never refactor and add features simultaneously
- **Quote:** "When I'm refactoring, I'm wearing my 'refactoring hat.' When I'm adding features, I'm wearing my 'adding features hat.'"

**Principle 4: Preserve Behavior**
- **Source:** Chapter 1, Page 15
- **Application:** Refactoring must not change observable behavior
- **Quote:** "Refactoring is a controlled technique for improving the design of an existing code base. Its essence is applying a series of small behavior-preserving transformations."

**Principle 5: Clear Intent**
- **Source:** Chapter 1, Page 15
- **Application:** Method names should clearly express intent
- **Quote:** "Any fool can write code that a computer can understand. Good programmers write code that humans can understand."

---

## Book References

This subagent implements **Smell-Driven Refactoring** from:

**Primary Source:**
- **Title:** Refactoring: Improving the Design of Existing Code
- **Author:** Martin Fowler (with Kent Beck, John Brant, William Opdyke, Don Roberts)
- **Key Chapters:**
  - Chapter 2: Principles in Refactoring (methodology)
  - Chapter 3: Bad Smells in Code (smell catalog and routing)
  - Chapters 6-11: Refactoring Catalog (specific refactorings)

**Methodology:**
- Smell-Driven Refactoring - Detect smell → Select refactoring → Apply safely → Verify

**Related Patterns:**
- Extract Method (Chapter 6) - Most common refactoring
- Replace Temp with Query (Chapter 7) - Remove blocking temps
- Introduce Parameter Object (Chapter 6) - Reduce parameter lists
- Extract Class (Chapter 7) - Split large classes

---

**When to Use This Subagent:**
- Code needs refactoring to improve design
- Code smells detected (long methods, duplicate code, etc.)
- Preparing code for new features (clean up first)
- Technical debt reduction
- Code review identified design issues

**When to Use Different Subagent:**
- Implementing new features → @james (Developer)
- Architectural redesign → @winston (Architect)
- Bug fixing → @james (Developer with fix-issue skill)
- Testing → @quinn (Quality)

---

*Routing and decision-making based on Refactoring by Martin Fowler*
```

### Example 1 Summary

**What We Created from "Refactoring" Book:**

**Layer 1 (Primitives):**
- refactoring-commands skill with 4 Python scripts
- Implements Fowler's refactoring mechanics exactly as described
- Scripts follow JSON I/O contract for composability

**Layer 2 (Workflow Skill):**
- refactor-code-smell skill
- Implements Fowler's smell-driven workflow
- References book chapters throughout
- Decision trees map smells to refactorings per book

**Layer 3 (Subagent):**
- refactoring-specialist subagent
- Routes based on smell severity and complexity (from book)
- Enforces Fowler's principles as guardrails
- Book quotes guide decision-making

**Result:** Complete, production-ready refactoring system derived entirely from one book.

---

### Example 2: "Test-Driven Development" Book → TDD Workflow Skill

**Book:** *Test-Driven Development: By Example* by Kent Beck

**Chapter Used:** Chapter 1 - "Multi-Currency Money"

#### Quick Implementation

**Layer 2 Skill Only** (TDD is workflow-focused, no primitives needed)

**Skill:** `tdd-workflow`

**Key Content from Book:**

**SKILL.md:**
```markdown
---
name: tdd-workflow
description: Test-Driven Development workflow following Kent Beck's Red-Green-Refactor cycle
source:
  book: "Test-Driven Development: By Example"
  author: "Kent Beck"
  chapters: [1, 2, 6]
  methodology: "Red-Green-Refactor"
---

# TDD Workflow

## Purpose

Implement features using Kent Beck's Test-Driven Development methodology.

**Based on:**
- Book: Test-Driven Development: By Example by Kent Beck
- Methodology: Red-Green-Refactor cycle
- Principle: "Test first, code later"

## Workflow

**Kent Beck's TDD Mantra:**
> "Red. Green. Refactor." (Chapter 6, Page 33)

### Step 1: RED - Write Failing Test

**From Book:** Chapter 1, Page 1

Write a test for next bit of functionality you want.

**Beck's Rule:** "Don't write a line of production code until you have a failing unit test."

[Continue with complete workflow...]
```

**references/tdd-principles.md:**
```markdown
# TDD Principles from Kent Beck

## The Three Rules

**Source:** Test-Driven Development by Example, Chapter 6

1. **Write a test for the next bit of functionality you want to add**
2. **Write the functional code until the test passes**
3. **Refactor both new and old code to make it well structured**

[Continue with principles from book...]
```

**Result:** Comprehensive TDD workflow skill derived from Beck's book, ready for use by james-developer subagent.

---

## Quality Assurance

### Validation Checklist for Book-Derived Skills

**General Quality:**
- [ ] Book properly attributed (title, author, chapter, pages)
- [ ] Methodology/technique clearly identified
- [ ] Direct quotes used where appropriate
- [ ] Book references inline (Chapter X, Page Y format)
- [ ] Examples from book included or adapted
- [ ] Book's terminology preserved

**Layer 1 (Primitives):**
- [ ] Algorithm matches book's description
- [ ] Mechanics follow book's steps exactly
- [ ] Book reference in script docstring
- [ ] Example from book in tests
- [ ] Command output includes book reference

**Layer 2 (Workflow Skills):**
- [ ] Workflow maps to book's methodology
- [ ] Each step references book chapter/page
- [ ] Decision trees from book captured
- [ ] Best practices from book documented
- [ ] Scenarios from book covered
- [ ] Validation criteria from book used

**Layer 3 (Subagents):**
- [ ] Routing logic from book's framework
- [ ] Guardrails based on book's principles
- [ ] Decision-making references book
- [ ] Escalation triggers from book guidance
- [ ] Quality gates from book's success criteria

### Legal and Ethical Considerations

**Copyright:**
- ✅ Use ideas and methodologies (not copyrightable)
- ✅ Reference book properly (fair use)
- ✅ Short quotes with attribution (fair use)
- ❌ Don't copy long passages verbatim
- ❌ Don't reproduce diagrams without permission
- ❌ Don't republish book's content

**Attribution Requirements:**
- Always cite: Book title, author, chapter, page
- Include "Based on" or "Derived from" statements
- Use "From Book:" prefix for quotes
- Maintain book references in metadata

**Respectful Use:**
- Preserve author's intent
- Don't misrepresent book's teachings
- Credit author's insights
- Link to book for further reading

---

## Common Patterns by Book Type

### Design Patterns Books

**Examples:** Gang of Four, Cloud Patterns, Enterprise Integration Patterns

**Typical Content:**
- Pattern catalog (each pattern is a skill candidate)
- When to use each pattern (routing logic)
- Implementation mechanics (primitives)
- Trade-offs and consequences (guardrails)

**Extraction Strategy:**
1. **Layer 1:** Pattern implementation primitives
   - apply-pattern, validate-pattern, detect-pattern scripts
2. **Layer 2:** Pattern selection and application workflows
3. **Layer 3:** Pattern architect subagent (routes to appropriate pattern)

**Time Estimate:** 4-6 hours per pattern, 20-30 patterns per book → 80-180 hours

---

### Architecture Books

**Examples:** Clean Architecture, DDD, Building Microservices

**Typical Content:**
- Architectural principles
- Design guidelines
- Component patterns
- Quality attributes

**Extraction Strategy:**
1. **Layer 2:** Architecture design workflow skills
   - design-clean-architecture, model-domain, design-microservices
2. **Layer 3:** Architecture reviewer subagent
   - Routes based on architecture type, enforces principles as guardrails

**Time Estimate:** 8-12 hours per architecture style

---

### Methodology Books

**Examples:** TDD, Refactoring, Agile/Scrum guides

**Typical Content:**
- Step-by-step processes
- Best practices
- Common pitfalls
- Examples and exercises

**Extraction Strategy:**
1. **Layer 2:** Methodology workflow skills
   - tdd-workflow, refactor-code, agile-planning
2. **Layer 3:** Methodology coach subagent
   - Guides user through methodology, enforces principles

**Time Estimate:** 6-10 hours per methodology

---

### Programming Language Books

**Examples:** Effective Java, JavaScript: The Good Parts, Python Cookbook

**Typical Content:**
- Language-specific patterns
- Idioms and best practices
- Common mistakes to avoid
- Code examples

**Extraction Strategy:**
1. **Layer 1:** Language-specific validation primitives
   - detect-antipattern, validate-idiom
2. **Layer 2:** Code review skills for that language
   - review-java-code, review-javascript-code
3. **Layer 3:** Language expert subagent

**Time Estimate:** 4-6 hours per language pattern/idiom

---

### Testing Books

**Examples:** Growing Object-Oriented Software, Guided by Tests; xUnit Test Patterns

**Typical Content:**
- Testing strategies
- Test patterns
- Test organization
- Mocking techniques

**Extraction Strategy:**
1. **Layer 1:** Test generation primitives
   - generate-test-stub, create-mock
2. **Layer 2:** Test design workflow skills
   - design-unit-tests, design-integration-tests
3. **Layer 3:** Test architect subagent

**Time Estimate:** 6-8 hours per testing strategy

---

## Troubleshooting

### Issue 1: "Book Content Too Abstract"

**Problem:** Chapter describes concepts, not concrete steps

**Solution:**
- Extract principles → Subagent guardrails
- Use examples from book → Concrete skill steps
- Combine with other chapters that show implementation
- Create decision frameworks from book's guidance

**Example:**
- Abstract principle: "Favor composition over inheritance"
- Concrete skill: When to use composition (decision tree), how to refactor inheritance to composition (steps)

---

### Issue 2: "Book Examples in Wrong Language"

**Problem:** Book uses Java, project is Python

**Solution:**
- Adapt patterns to target language
- Preserve pattern intent (don't translate literally)
- Note language adaptation in skill documentation
- Use book's pseudocode if available

**Example:**
- Book shows Java: `public void method(String param)`
- Skill shows Python equivalent: `def method(param: str):`
- Note: "Adapted from Java example in Chapter X"

---

### Issue 3: "Multiple Books Cover Same Topic"

**Problem:** Refactoring covered in Fowler and Clean Code books

**Solution:**
- Choose primary source (most authoritative)
- Cross-reference other sources in references/
- Combine complementary insights
- Note multiple sources in metadata

**Example:**
```yaml
source:
  primary:
    book: "Refactoring"
    author: "Martin Fowler"
  additional_references:
    - book: "Clean Code"
      author: "Robert C. Martin"
      chapters: [3, 10]
```

---

### Issue 4: "Book Chapter Is Entire Methodology"

**Problem:** Chapter describes complete, complex methodology (e.g., entire Scrum framework)

**Solution:**
- Break into multiple skills (one per ceremony/artifact)
- Create skill suite (related skills in same directory)
- Subagent coordinates multi-skill workflows
- Progressive implementation (start with core, add advanced skills later)

**Example:**
- Scrum book → 5-6 skills (sprint-planning, daily-standup, sprint-review, sprint-retro, backlog-refinement)
- Scrum Master subagent → Routes to appropriate ceremony skill

---

### Issue 5: "Skills Too Similar to Existing"

**Problem:** Book's technique overlaps with existing skill

**Solution:**
1. Compare approaches (book vs. existing skill)
2. If book's approach better → Update existing skill with book references
3. If approaches complementary → Create alternative skill with clear differentiation
4. If essentially same → Just add book references to existing skill

**Decision Matrix:**
- Book fundamentally different? → New skill
- Book adds valuable details? → Enhance existing skill
- Book same as existing? → Update references only

---

## Next Steps

### Immediate Actions

1. **Select Book Chapter**
   - Choose technical book with actionable content
   - Select 1-3 chapters to start (don't do entire book at once)
   - Prioritize chapters with concrete techniques

2. **Read and Annotate**
   - Read chapter carefully
   - Highlight actionable techniques
   - Note algorithms, workflows, decision frameworks
   - Mark examples to extract

3. **Map to 3-Layer Architecture**
   - Identify primitives (atomic operations)
   - Identify workflows (multi-step processes)
   - Identify decision-making (routing logic)

4. **Create First Skill**
   - Start with Layer 2 (workflow skill) - easiest
   - Use templates from this guide
   - Include book references throughout
   - Test with example from book

5. **Iterate and Refine**
   - Get feedback on first skill
   - Adjust extraction approach
   - Continue with next chapter/technique

### Long-Term Strategy

**Months 1-2: Foundation Books**
- Refactoring (Martin Fowler)
- Test-Driven Development (Kent Beck)
- Clean Code (Robert C. Martin)

**Months 3-4: Domain-Specific Books**
- Design Patterns (Gang of Four)
- Domain-Driven Design (Eric Evans)
- Building Microservices (Sam Newman)

**Months 5-6: Advanced Topics**
- Growing Object-Oriented Software, Guided by Tests
- Release It! (Michael Nygard)
- Pragmatic Programmer (Hunt & Thomas)

**Goal:** Build comprehensive skill library derived from canonical software engineering books.

---

## Resources

### Recommended Books for Skill Creation

**Essential (High Skill Density):**
1. Refactoring by Martin Fowler ⭐⭐⭐⭐⭐
2. Test-Driven Development by Kent Beck ⭐⭐⭐⭐⭐
3. Design Patterns by Gang of Four ⭐⭐⭐⭐⭐
4. Clean Code by Robert C. Martin ⭐⭐⭐⭐
5. Domain-Driven Design by Eric Evans ⭐⭐⭐⭐

**Highly Valuable (Good Skill Content):**
6. Building Microservices by Sam Newman
7. Release It! by Michael Nygard
8. Growing Object-Oriented Software, Guided by Tests
9. Working Effectively with Legacy Code by Michael Feathers
10. The Pragmatic Programmer by Hunt & Thomas

**Specialized (Domain-Specific Skills):**
11. Effective Java by Joshua Bloch (Java skills)
12. JavaScript: The Good Parts by Douglas Crockford (JS skills)
13. Python Cookbook (Python skills)
14. Enterprise Integration Patterns by Hohpe & Woolf
15. Cloud Native Patterns by Cornelia Davis

### Templates and Examples

**Available in this repository:**
- `docs/skill-refactoring-template.md` - General skill refactoring guide
- `.claude/skills/bmad-commands/` - Example Layer 1 (Primitives)
- `.claude/skills/development/implement-v2/` - Example Layer 2 (Workflow)
- `.claude/agents/james-developer-v2.md` - Example Layer 3 (Subagent)

### Community Resources

**Skill Repositories:**
- BMAD Enhanced skills: `.claude/skills/` (21 skills, production-ready examples)
- Community skill marketplace (planned)

**Documentation:**
- 3-layer-architecture-for-skills.md (architecture deep-dive)
- architecture-claude-code-compliance.md (compliance verification)
- ROADMAP.md (project roadmap and future plans)

---

## Conclusion

### Key Takeaways

1. **Books Are Rich Skill Sources**
   - Technical books contain proven patterns and methodologies
   - Direct extraction preserves quality and correctness
   - Attribution respects authors and enables verification

2. **3-Layer Architecture Organizes Book Content**
   - Primitives: Algorithms and atomic operations
   - Workflows: Methodologies and processes
   - Subagents: Decision-making and routing

3. **Skills Remain Portable**
   - All skills follow skill-creator pattern
   - Package and distribute as .zip files
   - Work across projects and teams

4. **Quality Through Attribution**
   - Reference book chapters and pages
   - Include author insights
   - Preserve original terminology

5. **Systematic Extraction Works**
   - Follow proven workflow (analyze → distill → create)
   - Use templates consistently
   - Validate against book examples

### Success Metrics

**After implementing this guide:**
- ✅ 10+ skills derived from books
- ✅ Skills reference source material throughout
- ✅ Skills validated against book examples
- ✅ Portable and packageable
- ✅ Production-ready quality

### Next Guide

**See:** `Skills Books.md` - For integrating existing skills with subagents

---

**Version:** 1.0
**Last Updated:** 2025-11-03
**Maintained By:** BMAD Enhanced Core Team

---

*Transform knowledge into skills. Transform skills into capability.*
