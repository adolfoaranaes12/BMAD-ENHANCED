# /update-taskmaster-status Task

When this command is used, execute the following task:

# Update Task Master Status

**Purpose**: Update Task Master task status and progress based on development work completed.

**Prerequisites**:
- Task Master must be configured and accessible
- Developer must be working on specific tasks
- Progress updates must be available

**Workflow**:

1. **Identify Current Task**
   - Get current task from Task Master
   - Check task status and progress
   - Identify what needs to be updated

2. **Update Task Status**
   - Mark task as "in-progress" when starting
   - Update subtask status as work progresses
   - Mark tasks as "done" when completed

3. **Log Detailed Progress**
   - Add implementation details to task
   - Log findings and decisions made
   - Document any issues or challenges

4. **Update Dependencies**
   - Check if task completion affects other tasks
   - Update dependent task status if appropriate
   - Ensure proper task flow

**Status Update Types**:
- **Task Start**: Set status to "in-progress"
- **Progress Update**: Log detailed progress in task details
- **Subtask Complete**: Mark individual subtasks as "done"
- **Task Complete**: Mark main task as "done"
- **Blocked**: Mark task as "blocked" if issues arise

**Commands to Execute**:
```bash
# Set task status
mcp_task-master-ai_set_task_status --projectRoot="/home/adolfo/Documents/AIFrontDeskTS" --id="[task-id]" --status="[status]"

# Update task details
mcp_task-master-ai_update_task --projectRoot="/home/adolfo/Documents/AIFrontDeskTS" --id="[task-id]" --prompt="[update-details]"

# Update subtask progress
mcp_task-master-ai_update_subtask --projectRoot="/home/adolfo/Documents/AIFrontDeskTS" --id="[subtask-id]" --prompt="[progress-details]"
```

**Success Criteria**:
- Task status accurately reflects current work
- Progress is detailed and useful for future reference
- Dependencies are properly managed
- Next tasks are clearly identified

**Quality Checks**:
- Status updates are timely and accurate
- Progress logs are detailed and informative
- No tasks are left in incorrect status
- Dependencies are properly updated
