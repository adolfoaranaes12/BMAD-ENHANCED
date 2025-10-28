# Sync Story with Task Master

**Purpose**: Generate tasks in Task Master from a completed story and sync progress back to the story file.

**Prerequisites**: 
- Story must be completed and ready for development
- Task Master must be initialized and configured
- Story file must exist in `docs/stories/`

**Workflow**:

1. **Parse Story Requirements**
   - Read the story file from `docs/stories/`
   - Extract acceptance criteria and technical requirements
   - Identify dependencies and integration points

2. **Generate Tasks in Task Master**
   - Use Task Master `parse_prd` command to generate tasks from story
   - Configure appropriate number of tasks based on story complexity
   - Set proper dependencies and priorities

3. **Update Story File**
   - Add Task Master task IDs to story file
   - Update Dev Agent Record section with Task Master integration
   - Mark story as "Ready for Development"

4. **Verify Integration**
   - Confirm tasks were created in Task Master
   - Verify story file was updated correctly
   - Test Task Master commands work with new tasks

**Commands to Execute**:
```bash
# Generate tasks from story
mcp_task-master-ai_parse_prd --projectRoot="/home/adolfo/Documents/AIFrontDeskTS" --input="docs/stories/[story-file].md" --numTasks="[appropriate-number]"

# Verify tasks were created
mcp_task-master-ai_get_tasks --projectRoot="/home/adolfo/Documents/AIFrontDeskTS"
```

**Success Criteria**:
- Tasks generated in Task Master match story requirements
- Story file updated with Task Master integration
- Developer can access tasks via Task Master commands
- No conflicts with existing tasks

**Error Handling**:
- If Task Master fails, log error and continue with story creation
- If story file update fails, retry with backup
- If integration fails, provide manual instructions to user
