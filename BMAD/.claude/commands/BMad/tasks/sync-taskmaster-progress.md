# /sync-taskmaster-progress Task

When this command is used, execute the following task:

# Sync Task Master Progress

**Purpose**: Synchronize development progress between Task Master and story files, ensuring both systems stay updated.

**Prerequisites**:
- Task Master must be configured and accessible
- Story file must exist and be linked to Task Master tasks
- Developer must be actively working on tasks

**Workflow**:

1. **Get Current Task Status**
   - Retrieve current task from Task Master
   - Check task progress and status
   - Identify any updates needed

2. **Update Story Progress**
   - Update story file Dev Agent Record section
   - Log implementation progress and findings
   - Update task checkboxes and completion status

3. **Sync Task Master Updates**
   - Update task status in Task Master
   - Log detailed progress in task details
   - Mark subtasks as completed when appropriate

4. **Validate Synchronization**
   - Verify both systems show consistent status
   - Check for any discrepancies
   - Ensure progress is accurately reflected

**Sync Points**:
- **Task Start**: Mark task as "in-progress" in both systems
- **Progress Updates**: Log findings and progress in both systems
- **Subtask Completion**: Mark subtasks complete in both systems
- **Task Completion**: Mark task complete and update story status

**Commands to Execute**:
```bash
# Get current task
mcp_task-master-ai_next_task --projectRoot="/home/adolfo/Documents/AIFrontDeskTS"

# Update task status
mcp_task-master-ai_set_task_status --projectRoot="/home/adolfo/Documents/AIFrontDeskTS" --id="[task-id]" --status="[status]"

# Log progress
mcp_task-master-ai_update_subtask --projectRoot="/home/adolfo/Documents/AIFrontDeskTS" --id="[subtask-id]" --prompt="[progress-details]"
```

**Success Criteria**:
- Both systems show consistent task status
- Progress is accurately logged in both systems
- No information is lost between systems
- Developer can continue work seamlessly

**Error Handling**:
- If Task Master is unavailable, continue with story updates
- If story file is locked, retry with backup
- If sync fails, provide manual sync instructions
