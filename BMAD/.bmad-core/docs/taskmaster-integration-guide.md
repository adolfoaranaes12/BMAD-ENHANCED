# Task Master & BMAD Agents Integration Guide

## Overview

This guide explains how the Task Master system integrates with BMAD agents (Scrum Master and Developer) to provide seamless task management and development workflow.

## Integration Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Scrum Master  │    │   Task Master    │    │    Developer    │
│      (Bob)      │◄──►│   (MCP Server)   │◄──►│     (James)     │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│  Story Files    │    │  Task Database   │    │  Code Files     │
│ docs/stories/   │    │ .taskmaster/     │    │ packages/       │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## Workflow Integration

### 1. Story Creation & Task Generation

**Scrum Master (Bob) Workflow:**
1. **Create Story**: Use `*draft` command to create new story
2. **Generate Tasks**: Use `*sync-taskmaster` to generate tasks in Task Master
3. **Validate Tasks**: Use `*generate-tasks` to ensure proper task breakdown

**Commands:**
```bash
*draft                    # Create new story
*sync-taskmaster         # Generate tasks from story
*generate-tasks          # Create detailed task breakdown
```

### 2. Development & Progress Tracking

**Developer (James) Workflow:**
1. **Get Next Task**: Use Task Master to get next task to work on
2. **Implement**: Follow story requirements and implement code
3. **Update Progress**: Use `*sync-progress` to update both systems
4. **Mark Complete**: Use `*update-status` to mark tasks complete

**Commands:**
```bash
*develop-story           # Implement story following tasks
*sync-progress          # Sync progress between systems
*update-status          # Update Task Master status
```

## Task Master Commands Integration

### Scrum Master Commands

| Command | Purpose | Task Master Integration |
|---------|---------|------------------------|
| `*draft` | Create story | None (story creation only) |
| `*sync-taskmaster` | Generate tasks | `parse_prd`, `add_task`, `expand_task` |
| `*generate-tasks` | Create task breakdown | `add_task`, `add_dependency`, `expand_task` |

### Developer Commands

| Command | Purpose | Task Master Integration |
|---------|---------|------------------------|
| `*develop-story` | Implement story | `get_tasks`, `next_task`, `get_task` |
| `*sync-progress` | Sync progress | `set_task_status`, `update_subtask` |
| `*update-status` | Update status | `set_task_status`, `update_task` |

## Integration Points

### 1. Story to Task Mapping

**Story File Structure:**
```markdown
## Dev Agent Record
- Task Master Task IDs: [1, 2, 3]
- Current Task: 1
- Progress: In Progress
```

**Task Master Integration:**
- Tasks linked to story via metadata
- Progress synchronized between systems
- Status updates reflected in both

### 2. Progress Synchronization

**Bidirectional Updates:**
- Story progress → Task Master status
- Task Master progress → Story updates
- Real-time synchronization

### 3. Dependency Management

**Task Dependencies:**
- Story dependencies → Task Master dependencies
- Task completion → Dependent task activation
- Proper workflow sequencing

## Configuration

### Task Master Configuration

**Required Settings:**
```json
{
  "models": {
    "main": {
      "provider": "openrouter",
      "modelId": "qwen/qwen3-coder:free"
    }
  },
  "global": {
    "projectName": "AIFrontDeskTS",
    "defaultTag": "master"
  }
}
```

### BMAD Agent Configuration

**Scrum Master (sm.md):**
```yaml
commands:
  - sync-taskmaster: Execute task sync-with-taskmaster.md
  - generate-tasks: Execute task generate-tasks-from-story.md

dependencies:
  tasks:
    - sync-with-taskmaster.md
    - generate-tasks-from-story.md
```

**Developer (dev.md):**
```yaml
commands:
  - sync-progress: Execute task sync-taskmaster-progress.md
  - update-status: Execute task update-taskmaster-status.md

dependencies:
  tasks:
    - sync-taskmaster-progress.md
    - update-taskmaster-status.md
```

## Usage Examples

### Example 1: Complete Story Development Workflow

1. **Scrum Master creates story:**
   ```bash
   *draft
   # Creates story-2-5-new-feature.md
   ```

2. **Generate tasks in Task Master:**
   ```bash
   *sync-taskmaster
   # Generates tasks 19, 20, 21 in Task Master
   ```

3. **Developer implements:**
   ```bash
   *develop-story
   # Gets task 19 from Task Master
   # Implements feature
   # Updates progress
   ```

4. **Sync progress:**
   ```bash
   *sync-progress
   # Updates both story and Task Master
   ```

### Example 2: Task Status Updates

**Developer workflow:**
```bash
# Get next task
mcp_task-master-ai_next_task --projectRoot="/home/adolfo/Documents/AIFrontDeskTS"

# Start task
mcp_task-master-ai_set_task_status --projectRoot="/home/adolfo/Documents/AIFrontDeskTS" --id="19" --status="in-progress"

# Update progress
mcp_task-master-ai_update_subtask --projectRoot="/home/adolfo/Documents/AIFrontDeskTS" --id="19.1" --prompt="Implementation complete"

# Mark complete
mcp_task-master-ai_set_task_status --projectRoot="/home/adolfo/Documents/AIFrontDeskTS" --id="19" --status="done"
```

## Benefits

### For Scrum Master (Bob)
- **Automated Task Generation**: Stories automatically generate tasks
- **Progress Visibility**: Real-time view of development progress
- **Better Planning**: Clear task breakdown and dependencies

### For Developer (James)
- **Clear Task Priorities**: Always know what to work on next
- **Progress Tracking**: Detailed logging of implementation progress
- **Seamless Workflow**: No manual task management overhead

### For Project Management
- **Single Source of Truth**: Task Master as central task database
- **Automated Reporting**: Progress tracking across all stories
- **Better Coordination**: Clear handoffs between agents

## Troubleshooting

### Common Issues

1. **Task Master Not Responding**
   - Check MCP server configuration
   - Verify API keys are set
   - Test with simple commands

2. **Story-Task Sync Issues**
   - Verify story file exists
   - Check Task Master task IDs
   - Manually sync if needed

3. **Progress Not Updating**
   - Check both systems for consistency
   - Verify command execution
   - Review error logs

### Error Recovery

**If Integration Fails:**
1. Continue with manual workflow
2. Log issues for later resolution
3. Provide manual sync instructions
4. Escalate to system administrator

## Future Enhancements

### Planned Features
- **Automatic Sync**: Real-time bidirectional synchronization
- **Conflict Resolution**: Handle simultaneous updates
- **Advanced Reporting**: Comprehensive progress analytics
- **Integration Testing**: Automated integration validation

### Extension Points
- **Custom Commands**: Add project-specific commands
- **Workflow Customization**: Adapt to specific project needs
- **Integration APIs**: Programmatic access to integration features

## Support

For issues or questions:
1. Check this integration guide
2. Review Task Master documentation
3. Check BMAD agent documentation
4. Contact system administrator

---

**Last Updated**: 2025-01-12  
**Version**: 1.0  
**Maintained by**: System Integration Team
