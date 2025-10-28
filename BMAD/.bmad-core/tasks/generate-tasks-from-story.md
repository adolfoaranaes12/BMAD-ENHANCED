# Generate Tasks from Story

**Purpose**: Create detailed, actionable tasks in Task Master based on a completed story's requirements.

**Prerequisites**:
- Story must be in "Ready for Development" status
- Story must have clear acceptance criteria
- Task Master must be configured and accessible

**Workflow**:

1. **Analyze Story Requirements**
   - Extract functional requirements from acceptance criteria
   - Identify technical requirements and dependencies
   - Determine appropriate task breakdown granularity

2. **Generate Task Structure**
   - Create main tasks for major features
   - Break down complex tasks into subtasks
   - Set proper dependencies between tasks
   - Assign appropriate priorities

3. **Create Tasks in Task Master**
   - Use Task Master commands to create tasks
   - Add detailed descriptions and implementation notes
   - Set up proper task relationships

4. **Validate Task Generation**
   - Verify all story requirements are covered
   - Check task dependencies are correct
   - Ensure tasks are actionable and clear

**Task Generation Strategy**:
- **High-level tasks**: Major features or components
- **Subtasks**: Specific implementation steps
- **Dependencies**: Based on technical requirements
- **Priorities**: Based on story priority and dependencies

**Commands to Execute**:
```bash
# Create main tasks
mcp_task-master-ai_add_task --projectRoot="/home/adolfo/Documents/AIFrontDeskTS" --prompt="[task-description]" --priority="[priority]"

# Expand complex tasks
mcp_task-master-ai_expand_task --projectRoot="/home/adolfo/Documents/AIFrontDeskTS" --id="[task-id]" --research

# Set dependencies
mcp_task-master-ai_add_dependency --projectRoot="/home/adolfo/Documents/AIFrontDeskTS" --id="[task-id]" --dependsOn="[dependency-id]"
```

**Success Criteria**:
- All story requirements mapped to tasks
- Tasks are actionable and clear
- Dependencies properly set
- Developer can start implementation immediately

**Quality Checks**:
- Each task has clear acceptance criteria
- Tasks follow existing patterns and standards
- No circular dependencies
- Appropriate level of granularity
