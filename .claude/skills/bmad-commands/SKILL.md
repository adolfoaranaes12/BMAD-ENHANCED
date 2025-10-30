---
name: bmad-commands
description: Atomic command primitives for BMAD operations. Provides type-safe, testable wrappers around file operations and test execution with structured JSON I/O and built-in telemetry. This skill should be used when BMAD workflows need deterministic, reliable primitive operations with observability.
---

# BMAD Commands

## Overview

BMAD Commands provide atomic, testable command primitives that BMAD skills compose into workflows. Each command follows a strict contract with typed inputs/outputs, structured error handling, and built-in telemetry.

**Design Principles:**
- **Deterministic**: Same inputs always produce same outputs
- **Testable**: Pure functions with JSON I/O
- **Observable**: All commands emit telemetry data
- **Composable**: Commands are building blocks for skills

## Available Commands

### read_file

Read file contents with metadata.

**Usage:**
```bash
python scripts/read_file.py --path <file-path> --output json
```

**Inputs:**
- `path` (required): Path to file to read

**Outputs:**
- `content`: File contents as text
- `line_count`: Number of lines
- `size_bytes`: File size in bytes
- `path`: Absolute path to file

**Example:**
```bash
python .claude/skills/bmad-commands/scripts/read_file.py \
  --path workspace/tasks/task-001.md \
  --output json
```

**Returns:**
```json
{
  "success": true,
  "outputs": {
    "content": "# Task Specification\n...",
    "line_count": 45,
    "size_bytes": 1024,
    "path": "/absolute/path/to/task-001.md"
  },
  "telemetry": {
    "command": "read_file",
    "duration_ms": 12,
    "timestamp": "2025-01-15T10:30:00Z",
    "path": "workspace/tasks/task-001.md",
    "line_count": 45
  },
  "errors": []
}
```

---

### run_tests

Execute tests with specified framework and return structured results.

**Usage:**
```bash
python scripts/run_tests.py --path <test-path> --framework <jest|pytest> --timeout <seconds> --output json
```

**Inputs:**
- `path` (required): Directory containing tests
- `framework` (optional): Test framework (default: jest)
- `timeout` (optional): Timeout in seconds (default: 120)

**Outputs:**
- `passed`: Whether all tests passed (boolean)
- `summary`: Human-readable summary
- `total_tests`: Total number of tests
- `passed_tests`: Number passed
- `failed_tests`: Number failed
- `coverage_percent`: Coverage percentage (0-100)
- `junit_path`: Path to JUnit report

**Example:**
```bash
python .claude/skills/bmad-commands/scripts/run_tests.py \
  --path . \
  --framework jest \
  --timeout 120 \
  --output json
```

**Returns:**
```json
{
  "success": true,
  "outputs": {
    "passed": true,
    "summary": "10/10 tests passed",
    "total_tests": 10,
    "passed_tests": 10,
    "failed_tests": 0,
    "coverage_percent": 87,
    "junit_path": "./junit.xml"
  },
  "telemetry": {
    "command": "run_tests",
    "framework": "jest",
    "duration_ms": 4523,
    "timestamp": "2025-01-15T10:30:00Z",
    "total_tests": 10,
    "passed_tests": 10,
    "failed_tests": 0
  },
  "errors": []
}
```

---

## Response Format

All commands return JSON with this structure:

```json
{
  "success": boolean,
  "outputs": {
    // Command-specific outputs
  },
  "telemetry": {
    "command": string,
    "duration_ms": number,
    "timestamp": string,
    // Command-specific telemetry
  },
  "errors": [
    // Array of error strings (empty if success=true)
  ]
}
```

**Exit Codes:**
- `0`: Command succeeded (`success: true`)
- `1`: Command failed (`success: false`)

---

## Using Commands from Skills

To use commands from other skills, execute the script and parse the JSON output.

**Example in a skill's SKILL.md:**

```markdown
### Step 1: Read Task Specification

Execute the read_file command:

python .claude/skills/bmad-commands/scripts/read_file.py \
  --path workspace/tasks/{task_id}.md \
  --output json

Parse the JSON response and extract `outputs.content` for the task specification.

### Step 2: Run Tests

Execute the run_tests command:

python .claude/skills/bmad-commands/scripts/run_tests.py \
  --path . \
  --framework jest \
  --output json

Parse the JSON response and check `outputs.passed` to verify tests passed.
```

---

## Error Handling

All commands handle errors gracefully and return structured error information:

```json
{
  "success": false,
  "outputs": {},
  "telemetry": {
    "command": "read_file",
    "duration_ms": 5,
    "timestamp": "2025-01-15T10:30:00Z"
  },
  "errors": ["file_not_found"]
}
```

**Common Errors:**
- `file_not_found`: File doesn't exist
- `path_is_not_file`: Path is a directory
- `permission_denied`: Insufficient permissions
- `timeout`: Operation exceeded timeout
- `invalid_path`: Path validation failed
- `unexpected_error`: Unexpected error occurred

---

## Telemetry

All commands emit telemetry data for observability:

- `command`: Command name
- `duration_ms`: Execution time in milliseconds
- `timestamp`: ISO 8601 timestamp
- Command-specific metrics (e.g., line_count, test_count)

This telemetry enables:
- Performance monitoring
- Usage analytics
- Debugging workflows
- Production observability

---

## Command Contracts

Full command contracts (inputs, outputs, errors, telemetry) are documented in:
`references/command-contracts.yaml`

Reference this file when:
- Creating new commands
- Updating existing commands
- Integrating commands into skills
- Understanding command behavior

---

## Testing Commands

Test commands independently before using in workflows:

```bash
# Test read_file
python .claude/skills/bmad-commands/scripts/read_file.py \
  --path README.md \
  --output json

# Test run_tests (if you have a test suite)
python .claude/skills/bmad-commands/scripts/run_tests.py \
  --path . \
  --framework jest \
  --output json
```

Verify:
- JSON output is valid
- Exit code is 0 for success, 1 for failure
- Telemetry data is present
- Errors are structured

---

## Extending Commands

To add new commands:

1. Create `scripts/<command_name>.py`
2. Follow the standard response format
3. Add command contract to `references/command-contracts.yaml`
4. Update this SKILL.md with usage documentation
5. Make script executable: `chmod +x scripts/<command_name>.py`
6. Test independently before integrating

---

## Philosophy

Commands are the **foundation layer** of BMAD's 3-layer architecture:

1. **Commands** (this skill): Atomic, testable primitives
2. **Skills**: Compose commands into workflows
3. **Subagents**: Orchestrate skills with routing and guardrails

By keeping commands deterministic and testable, we enable:
- Unit testing of the framework itself
- Reliable skill composition
- Observable workflows
- Production-ready operations
