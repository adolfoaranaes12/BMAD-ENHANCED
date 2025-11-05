---
description: Route architecture commands to Winston for system design, architecture review, codebase analysis, and ADR creation
argument-hint: <command> <args>
allowed-tools: Task
---

Route the command "$ARGUMENTS" to the winston-architect subagent for architecture operations.

Use the Task tool with:
- subagent_type: winston-architect
- description: Winston architecture command
- prompt: Execute architecture command: $ARGUMENTS

## Available Commands

- `*create-architecture` - Design system architecture from requirements
- `*review-architecture` - Review architecture for quality and risks
- `*analyze-architecture` - Analyze existing codebase architecture
- `*create-adr` - Create Architecture Decision Record
- `*validate-patterns` - Validate architectural patterns

## Usage Examples

```bash
# Design architecture from PRD
/winston *create-architecture docs/prd.md --type fullstack

# Review existing architecture
/winston *review-architecture docs/architecture.md --focus security

# Analyze brownfield codebase
/winston *analyze-architecture src/ --depth comprehensive

# Create ADR for technology decision
/winston *create-adr "Use PostgreSQL for relational data"
```

## When to Use

Use `/winston` for:
- Technical architecture design
- Architecture reviews and validation
- Codebase analysis
- ADR creation
- Pattern validation

Use `/winston-consult` for:
- Conversational architecture exploration
- Multi-option comparison
- Brainstorming with other agents
- "Help me figure out what I need"
