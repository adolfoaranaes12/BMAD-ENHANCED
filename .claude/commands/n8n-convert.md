---
args: <workflow-json-path>
---

Convert the n8n workflow JSON file at `{{args}}` to Inngest using the n8n-to-inngest skill.

# Execution Protocol

Follow this structured approach to ensure systematic translation:

## Phase 0: Validation & Setup

1. **Verify the input file exists** at the provided path
2. **Validate it's valid JSON** by attempting to read it
3. **Create a todo list** with the 5 translation phases:
   - Phase 1: Analysis & Decomposition
   - Phase 2: Architecture Design
   - Phase 3: Implementation
   - Phase 4: Testing & Validation
   - Phase 5: Deployment Planning

## Phase 1: Analysis & Decomposition (REQUIRED FIRST)

Before proceeding with any other phase:

1. **Run the parser script** to analyze the workflow structure:
   ```bash
   python .claude/skills/n8n-to-inngest/scripts/parse_n8n_workflow.py {{args}}
   ```

2. **Analyze the parser output** to identify:
   - Trigger type (webhook, schedule, manual, event)
   - Node count and types
   - Complexity indicators (conditionals, loops, sub-workflows)
   - Credentials that need migration
   - Dependencies and execution order

3. **Present findings to the user** including:
   - Workflow name and metadata
   - Trigger mechanism
   - Node breakdown by category
   - Complexity assessment
   - Recommended template(s)

4. **Ask clarifying questions** if needed:
   - Environment variable naming preferences
   - Target Inngest project structure
   - Testing strategy preferences
   - Any business logic that's not obvious from the JSON

## Phase 2-5: Systematic Translation

Once Phase 1 is complete and user has confirmed understanding:

1. **Load the n8n-to-inngest skill** for detailed guidance
2. **Follow the 5-phase workflow** from SKILL.md
3. **Update todo list progress** after completing each phase
4. **Reference appropriate resources**:
   - `references/patterns.md` for implementation examples
   - `references/challenges.md` when encountering issues
   - `assets/templates/` for starting code
   - `scripts/generate_step_id.py` for step naming

## Quality Gates

Ensure these requirements are met:

- [ ] Parser script executed successfully on input JSON
- [ ] All n8n nodes mapped to Inngest equivalents
- [ ] Credentials migrated to environment variables
- [ ] Step IDs are deterministic and kebab-case
- [ ] Error handling configured (retries, onFailure)
- [ ] TypeScript types defined for events and data
- [ ] Each external API call is isolated in its own step
- [ ] Steps are designed to be idempotent
- [ ] Implementation follows patterns from references
- [ ] Code includes proper error context for debugging

## Output Deliverables

Provide the user with:

1. **Inngest function(s)** - Complete TypeScript implementation
2. **Event schemas** - TypeScript type definitions
3. **Environment variables list** - Required config
4. **Webhook handler** (if webhook trigger) - Express/Next.js endpoint
5. **Testing checklist** - Based on Phase 4 guidance
6. **Deployment notes** - Configuration and monitoring setup
7. **Migration comparison** - Key differences from n8n behavior

## Important Notes

- **Always run the parser first** - Never skip Phase 1 analysis
- **Use TodoWrite** - Keep user informed of progress through all phases
- **Load references as needed** - Don't try to keep everything in memory
- **Ask questions** - Better to clarify than to guess business logic
- **Show your work** - Explain mapping decisions and trade-offs

Now proceed with the systematic translation following this protocol.
