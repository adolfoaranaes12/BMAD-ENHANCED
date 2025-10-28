# Scrum Master Task generation
@sm.mdc @sm.md please activate 

*story-checklist <story>

*generate-tasks for story <story>

# Scrum Master Task Edits
@sm.mdc @sm.md please activate

I need you to update the tasks.json file by adding the complete complexity field structure to all pending tasks and their subtasks.

**Your Mission:**
As the Scrum Master, you are responsible for ensuring all tasks have complete complexity field structure to enable context-driven development. This is a critical quality gate that prevents premature implementation.

**Your Tasks:**
1. **Analyze all pending tasks** using the `analyze_project_complexity` tool to generate accurate complexity scores
2. **Add complete complexity field structure** to all pending tasks and subtasks following the schema in @`complexity_field_management.mdc`
3. **Populate context_requirements** with comprehensive questions, inputs, dependencies, and risks for each task
4. **Set gathering_strategy** flags appropriately based on task complexity and requirements
5. **Ensure context_complete: false** initially for all tasks to enforce context gathering

**Required Complexity Field Structure:**
```yaml
complexity:
  score: 1-10 # Use analyze_project_complexity tool
  context_requirements:
    questions: [] # 4-6 relevant questions for this specific task
    inputs: [] # Required information and documentation
    dependencies: [] # External dependencies and prerequisites
    risks: [] # Potential risks and blockers
  context_answers: # Initially empty - developer will populate
    questions_answered: []
    inputs_provided: []
    dependencies_resolved: []
    risks_mitigated: []
    research_findings: []
    stakeholder_input: []
    technical_decisions: []
  gathering_strategy:
    research_needed: boolean # Based on task complexity
    stakeholder_input: boolean # Based on task requirements
    technical_validation: boolean # Based on technical complexity
    context_complete: false # Always false initially
  metadata:
    last_analyzed: timestamp # Current timestamp
    context_gathered: null # Initially null
    implementation_ready: false # Always false initially
```

**Process:**
1. **Identify Pending Tasks**: Find all tasks with status "pending" that lack complexity fields
2. **Run Complexity Analysis**: Use `analyze_project_complexity` tool to get accurate scores
3. **Add Complexity Structure**: Use `update_task` or `update_subtask` to add complete complexity fields
4. **Populate Requirements**: Generate task-specific questions, inputs, dependencies, and risks
5. **Set Strategy Flags**: Configure research_needed, stakeholder_input, technical_validation appropriately
6. **Validate Structure**: Ensure all tasks follow the established schema

**Quality Gates:**
- ✅ All pending tasks have complete complexity field structure
- ✅ All subtasks inherit complexity field structure from parent
- ✅ Context requirements are comprehensive and task-specific
- ✅ Gathering strategy flags are appropriately set
- ✅ Context_complete is false for all tasks initially
- ✅ Implementation_ready is false for all tasks initially

**Reference:** Use @`complexity_field_management.mdc` for complete schema and guidelines.

**Expected Outcome:**
All pending tasks and subtasks will have complete complexity field structure, enabling developers to gather proper context before implementation begins.

Please proceed with updating all pending tasks and subtasks with complete complexity field structures.

# Scrum Master Subtasks
@sm.mdc @sm.md please activate

I need you to update the tasks.json file by first creating subtasks for all pending tasks and also adding the complete complexity field structure to all pending subtasks.

**Your Mission:**
As the Scrum Master, you are responsible for ensuring all tasks have complete complexity field structure to enable context-driven development. This is a critical quality gate that prevents premature implementation.

**Your Tasks:**
1. **Analyze all pending tasks** using the `analyze_project_complexity` tool to generate accurate complexity scores
2. **Add complete complexity field structure** to all pending tasks and subtasks following the schema in @`complexity_field_management.mdc`
3. **Populate context_requirements** with comprehensive questions, inputs, dependencies, and risks for each task
4. **Set gathering_strategy** flags appropriately based on task complexity and requirements
5. **Ensure context_complete: false** initially for all tasks to enforce context gathering

**Required Complexity Field Structure:**
```yaml
complexity:
  score: 1-10 # Use analyze_project_complexity tool
  context_requirements:
    questions: [] # 4-6 relevant questions for this specific task
    inputs: [] # Required information and documentation
    dependencies: [] # External dependencies and prerequisites
    risks: [] # Potential risks and blockers
  context_answers: # Initially empty - developer will populate
    questions_answered: []
    inputs_provided: []
    dependencies_resolved: []
    risks_mitigated: []
    research_findings: []
    stakeholder_input: []
    technical_decisions: []
  gathering_strategy:
    research_needed: boolean # Based on task complexity
    stakeholder_input: boolean # Based on task requirements
    technical_validation: boolean # Based on technical complexity
    context_complete: false # Always false initially
  metadata:
    last_analyzed: timestamp # Current timestamp
    context_gathered: null # Initially null
    implementation_ready: false # Always false initially
```

**Process:**
1. **Identify Pending Tasks**: Find all tasks with status "pending" that lack complexity fields
2. **Run Complexity Analysis**: Use `analyze_project_complexity` tool to get accurate scores
3. **Add Complexity Structure**: Use `update_task` or `update_subtask` to add complete complexity fields
4. **Populate Requirements**: Generate task-specific questions, inputs, dependencies, and risks
5. **Set Strategy Flags**: Configure research_needed, stakeholder_input, technical_validation appropriately
6. **Validate Structure**: Ensure all tasks follow the established schema

**Quality Gates:**
- ✅ All pending tasks have complete complexity field structure
- ✅ All subtasks inherit complexity field structure from parent
- ✅ Context requirements are comprehensive and task-specific
- ✅ Gathering strategy flags are appropriately set
- ✅ Context_complete is false for all tasks initially
- ✅ Implementation_ready is false for all tasks initially

**Reference:** Use @`complexity_field_management.mdc` for complete schema and guidelines.

**Expected Outcome:**
All pending tasks and subtasks will have complete complexity field structure, enabling developers to gather proper context before implementation begins.

Please proceed with updating all pending tasks and subtasks with complete complexity field structures.

# Developer Populate Complexity Fields
@dev.mdc @dev.md please activate

The Scrum Master has completed adding complexity fields to all pending tasks. Now I need you to begin the context gathering phase for the next available task.

**Current Status:**
- All pending tasks now have complete complexity field structures
- [X] tasks already have complete context (context_complete: true, implementation_ready: true)
- [X] tasks need context gathering

**Your Mission:**
1. **Find the next task** that needs context gathering (context_complete: false)
2. **Review context_requirements** to understand what needs to be gathered
3. **Use research tool** to gather current best practices and information
4. **Populate context_answers** with your findings and decisions
5. **Mark context_complete: true** when all requirements are met

**Context Gathering Workflow:**
1. **Check Task Status**: Use `get_task` to view task details and complexity field
2. **Review Requirements**: Examine `context_requirements` (questions, inputs, dependencies, risks)
3. **Research Phase**: Use `research` tool if `research_needed: true`
4. **Document Findings**: Use `update_subtask` to populate `context_answers`
5. **Mark Complete**: Set `context_complete: true` when ready

**Critical Rules:**
- **NEVER start coding** without `context_complete: true` and `implementation_ready: true`
- **Always document** research findings, technical decisions, and rationale
- **Use research tool** for current best practices and implementation guidance
- **Maintain audit trail** with timestamps for all decisions

**Context Answers Structure:**
```yaml
context_answers:
  questions_answered: [] # Your answers to questions with timestamps
  inputs_provided: [] # Information you've gathered with status
  dependencies_resolved: [] # Status of dependencies and blockers
  risks_mitigated: [] # How you'll handle identified risks
  research_findings: [] # What you've researched with sources
  stakeholder_input: [] # Input from stakeholders (if needed)
  technical_decisions: [] # Technical choices made with rationale
```

**Commands to Use:**
- `get_task` - View task details and complexity field
- `research` - Gather current best practices and information
- `update_subtask` - Populate context answers with findings
- `set_task_status` - Update task status when context complete

**Reference:** Use @`complexity_field_quick_reference.mdc` for detailed workflow guidance.

**Start with:** Find the next task that needs context gathering and begin the process. Focus on one task at a time until context_complete: true.

Please proceed with context gathering for the next available task.

# Developer Execute
@dev.mdc @dev.md please activate and execute the pending tasks in order from @tasks.json
