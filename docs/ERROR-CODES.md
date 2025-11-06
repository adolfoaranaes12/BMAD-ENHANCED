# BMAD Enhanced - Error Codes Reference

**Version:** 2.0
**Last Updated:** 2025-11-05
**Status:** Production Ready

## Overview

This document provides a comprehensive reference for all error codes in BMAD Enhanced. Each error includes its code, category, severity, description, context information, remediation steps, and related documentation.

## Error Categories

BMAD Enhanced classifies errors into the following categories:

| Category | Description | Typical Severity |
|----------|-------------|------------------|
| **VALIDATION** | Input validation failures | ERROR |
| **CONFIGURATION** | Configuration and setup issues | ERROR |
| **GUARDRAIL** | Security and safety violations | ERROR/CRITICAL |
| **EXECUTION** | Runtime execution failures | ERROR |
| **DEPENDENCY** | Missing or incompatible dependencies | ERROR |
| **TIMEOUT** | Operation timeout exceeded | ERROR |
| **QUALITY_GATE** | Quality threshold violations | ERROR/WARNING |
| **COMPLEXITY** | Complexity threshold warnings | WARNING |
| **FILE_NOT_FOUND** | File or resource not found | ERROR |
| **PERMISSION** | Access permission denied | ERROR |

## Severity Levels

| Severity | Icon | Description | Behavior |
|----------|------|-------------|----------|
| **CRITICAL** | 🚨 | Blocks all operations | System exits immediately |
| **ERROR** | ✗ | Blocks current operation | Operation fails, workflow halts |
| **WARNING** | ⚠ | Allows continuation with caution | Operation continues with user acknowledgment |
| **INFO** | ℹ | Informational only | No blocking, informational message |

---

## Error Code Reference

### VALIDATION Errors

#### `ERR-VAL-001`: Input Validation Failed

**Category:** VALIDATION
**Severity:** ERROR
**Template:** `validation_error`

**Description:**
Input parameters or arguments failed validation checks.

**Common Causes:**
- Invalid command syntax
- Missing required parameters
- Parameter values out of valid range
- Invalid file paths or formats

**Context Fields:**
- `command`: The command that failed
- `parameter`: Parameter that failed validation
- `value`: Invalid value provided
- `expected`: Expected value format or range

**Remediation Steps:**
1. Check command syntax and required parameters
2. Verify input files exist and are readable
3. Ensure parameter values are within valid ranges
4. Review command documentation for correct usage

**Related Documentation:**
- [docs/quickstart-alex.md](/home/adolfo/Documents/BMAD%20Enhanced/docs/quickstart-alex.md)
- [docs/quickstart-james.md](/home/adolfo/Documents/BMAD%20Enhanced/docs/quickstart-james.md)
- [docs/COMMAND-REFERENCE-SUMMARY.md](/home/adolfo/Documents/BMAD%20Enhanced/docs/COMMAND-REFERENCE-SUMMARY.md)

**Example:**
```bash
# Error: Missing required parameter
/alex *create-task-spec
# ERR-VAL-001: Input validation failed
# Context: command='*create-task-spec', missing_parameter='--title'
```

---

#### `ERR-VAL-002`: Invalid File Format

**Category:** VALIDATION
**Severity:** ERROR

**Description:**
File format does not match expected structure (e.g., invalid YAML, JSON, or Markdown).

**Common Causes:**
- Malformed YAML in task specs or config files
- Invalid JSON in telemetry or output files
- Incorrect Markdown structure in documentation

**Context Fields:**
- `file_path`: Path to invalid file
- `expected_format`: Expected file format (YAML, JSON, MD)
- `parse_error`: Specific parsing error message
- `line_number`: Line number where error occurred (if available)

**Remediation Steps:**
1. Validate file syntax using appropriate linter (yamllint, jsonlint)
2. Check for common issues: unmatched quotes, incorrect indentation, missing colons
3. Compare file structure with templates in `.claude/templates/`
4. Use IDE with format validation enabled

**Related Documentation:**
- [docs/V2-ARCHITECTURE.md#file-formats](/home/adolfo/Documents/BMAD%20Enhanced/docs/V2-ARCHITECTURE.md)
- [.claude/templates/](/home/adolfo/Documents/BMAD%20Enhanced/.claude/templates/)

---

#### `ERR-VAL-003`: Parameter Out of Range

**Category:** VALIDATION
**Severity:** ERROR

**Description:**
Numeric parameter value exceeds acceptable range.

**Common Causes:**
- Complexity score out of 0-100 range
- Timeout value too large or negative
- Test coverage percentage invalid

**Context Fields:**
- `parameter`: Parameter name
- `value`: Provided value
- `min`: Minimum allowed value
- `max`: Maximum allowed value

**Remediation Steps:**
1. Check parameter value against valid range
2. Adjust value to fall within acceptable bounds
3. Review documentation for parameter constraints

**Related Documentation:**
- [docs/V2-ARCHITECTURE.md#complexity-assessment](/home/adolfo/Documents/BMAD%20Enhanced/docs/V2-ARCHITECTURE.md)

---

### CONFIGURATION Errors

#### `ERR-CFG-001`: Configuration Error

**Category:** CONFIGURATION
**Severity:** ERROR
**Template:** `configuration_error`

**Description:**
Configuration file is missing, invalid, or contains errors.

**Common Causes:**
- Missing `.claude/config.yaml`
- Invalid YAML syntax in config file
- Missing required configuration fields
- Incorrect configuration values

**Context Fields:**
- `config_file`: Path to configuration file
- `error_type`: Type of configuration error
- `missing_fields`: List of missing required fields (if applicable)

**Remediation Steps:**
1. Verify `.claude/config.yaml` exists and is valid YAML
2. Check for required configuration fields
3. Compare with `config.yaml.template`
4. Validate configuration: `python scripts/validate-config.py`

**Related Documentation:**
- [docs/PRODUCTION-DEPLOYMENT-GUIDE.md#configuration](/home/adolfo/Documents/BMAD%20Enhanced/docs/PRODUCTION-DEPLOYMENT-GUIDE.md)
- [.claude/config.yaml.template](/home/adolfo/Documents/BMAD%20Enhanced/.claude/config.yaml.template)

---

#### `ERR-CFG-002`: Invalid Guardrail Configuration

**Category:** CONFIGURATION
**Severity:** ERROR

**Description:**
Guardrail configuration is invalid or conflicts with other settings.

**Common Causes:**
- Conflicting guardrail rules
- Invalid guardrail threshold values
- Missing guardrail definitions

**Context Fields:**
- `guardrail`: Name of invalid guardrail
- `config_value`: Current configuration value
- `conflict`: Conflicting setting (if applicable)

**Remediation Steps:**
1. Review `.claude/config.yaml` guardrail section
2. Ensure threshold values are within 0-100 range
3. Check for conflicting guardrail rules
4. Validate against guardrail schema

**Related Documentation:**
- [docs/V2-ARCHITECTURE.md#guardrails-framework](/home/adolfo/Documents/BMAD%20Enhanced/docs/V2-ARCHITECTURE.md)
- [docs/PRODUCTION-SECURITY-REVIEW.md](/home/adolfo/Documents/BMAD%20Enhanced/docs/PRODUCTION-SECURITY-REVIEW.md)

---

### GUARDRAIL Errors

#### `ERR-GRD-001`: Guardrail Violation

**Category:** GUARDRAIL
**Severity:** ERROR
**Template:** `guardrail_violation`

**Description:**
Operation blocked by security or safety guardrail.

**Common Causes:**
- Attempting to access sensitive files (.env, credentials)
- Modifying protected system files
- Test coverage below minimum threshold
- Code quality below acceptable standards

**Context Fields:**
- `command`: Command that triggered violation
- `violation`: Description of guardrail violation
- `file`: File that triggered violation (if applicable)
- `guardrail`: Name of violated guardrail

**Remediation Steps:**
1. Review the specific guardrail that was violated
2. Check if sensitive files are being accessed
3. Verify test coverage meets minimum threshold
4. Ensure code meets quality standards
5. Review `.claude/config.yaml` for guardrail configuration

**Related Documentation:**
- [docs/V2-ARCHITECTURE.md#guardrails-framework](/home/adolfo/Documents/BMAD%20Enhanced/docs/V2-ARCHITECTURE.md)
- [docs/PRODUCTION-SECURITY-REVIEW.md](/home/adolfo/Documents/BMAD%20Enhanced/docs/PRODUCTION-SECURITY-REVIEW.md)

---

#### `ERR-GRD-002`: Test Coverage Below Threshold

**Category:** GUARDRAIL
**Severity:** ERROR

**Description:**
Code coverage is below the minimum required threshold.

**Common Causes:**
- New code added without corresponding tests
- Existing tests not covering edge cases
- Configuration threshold too strict

**Context Fields:**
- `current_coverage`: Current test coverage percentage
- `required_coverage`: Required minimum coverage
- `uncovered_files`: List of files with low coverage
- `missing_lines`: Number of uncovered lines

**Remediation Steps:**
1. Run coverage report: `*test --scope=unit --coverage`
2. Identify uncovered lines and add tests
3. Use `*test-design` to create comprehensive test plan
4. Adjust threshold in `.claude/config.yaml` if appropriate

**Related Documentation:**
- [docs/quickstart-james.md#3-test](/home/adolfo/Documents/BMAD%20Enhanced/docs/quickstart-james.md)
- [docs/V2-ARCHITECTURE.md#quality-gates](/home/adolfo/Documents/BMAD%20Enhanced/docs/V2-ARCHITECTURE.md)

---

#### `ERR-GRD-003`: Sensitive File Access Blocked

**Category:** GUARDRAIL
**Severity:** CRITICAL

**Description:**
Attempt to access or modify sensitive files blocked by security guardrail.

**Common Causes:**
- Trying to read `.env` files
- Accessing credential files
- Modifying system configuration files
- Reading private keys or certificates

**Context Fields:**
- `file_path`: Path to sensitive file
- `operation`: Operation attempted (read, write, delete)
- `guardrail`: Name of security guardrail triggered

**Remediation Steps:**
1. Review why sensitive file access is needed
2. Use environment variables or secure credential storage instead
3. Verify file path is correct and not pointing to sensitive location
4. If legitimate access needed, adjust guardrail configuration

**Related Documentation:**
- [docs/PRODUCTION-SECURITY-REVIEW.md#sensitive-files](/home/adolfo/Documents/BMAD%20Enhanced/docs/PRODUCTION-SECURITY-REVIEW.md)

---

### EXECUTION Errors

#### `ERR-EXC-001`: Test Failure

**Category:** EXECUTION
**Severity:** ERROR
**Template:** `test_failure`

**Description:**
Tests failed during execution.

**Common Causes:**
- Logic errors in implementation
- Broken test assertions
- Flaky tests with race conditions
- Environment setup issues

**Context Fields:**
- `command`: Test command executed
- `failed_tests`: Number of failed tests
- `total_tests`: Total number of tests
- `test_output`: Snippet of test failure output
- `framework`: Test framework used

**Remediation Steps:**
1. Review test output for specific failures
2. Use `*debug` to investigate failing tests
3. Check if tests are flaky or have dependencies
4. Verify test environment is set up correctly
5. Run tests locally: `*test --scope=unit`

**Related Documentation:**
- [docs/quickstart-james.md#3-test](/home/adolfo/Documents/BMAD%20Enhanced/docs/quickstart-james.md)
- [docs/quickstart-james.md#6-debug](/home/adolfo/Documents/BMAD%20Enhanced/docs/quickstart-james.md)

---

#### `ERR-EXC-002`: Build Failure

**Category:** EXECUTION
**Severity:** ERROR

**Description:**
Build process failed during compilation or bundling.

**Common Causes:**
- Syntax errors in code
- Missing dependencies
- Type errors (TypeScript, Python type hints)
- Configuration issues

**Context Fields:**
- `build_command`: Command that failed
- `error_message`: Build error message
- `affected_files`: Files with build errors
- `exit_code`: Build process exit code

**Remediation Steps:**
1. Review build output for specific errors
2. Check syntax errors in affected files
3. Verify all dependencies are installed
4. Run type checker: `tsc --noEmit` or `mypy .`
5. Clear build cache and retry

**Related Documentation:**
- [docs/quickstart-james.md#4-refactor](/home/adolfo/Documents/BMAD%20Enhanced/docs/quickstart-james.md)

---

#### `ERR-EXC-003`: Command Execution Failed

**Category:** EXECUTION
**Severity:** ERROR

**Description:**
Primitive command or script execution failed.

**Common Causes:**
- Script not found or not executable
- Python/Node runtime errors
- Invalid arguments passed to script
- System resource limits exceeded

**Context Fields:**
- `command`: Command that failed
- `exit_code`: Process exit code
- `stdout`: Standard output (truncated)
- `stderr`: Standard error output (truncated)

**Remediation Steps:**
1. Check if script exists and has execute permissions
2. Review stderr output for error details
3. Verify Python/Node environment is correctly set up
4. Test command manually with same arguments

**Related Documentation:**
- [docs/V2-ARCHITECTURE.md#primitives-layer](/home/adolfo/Documents/BMAD%20Enhanced/docs/V2-ARCHITECTURE.md)

---

### DEPENDENCY Errors

#### `ERR-DEP-001`: Missing Dependency

**Category:** DEPENDENCY
**Severity:** ERROR
**Template:** `missing_dependency`

**Description:**
Required dependency not found or not installed.

**Common Causes:**
- Package not installed via pip/npm
- Virtual environment not activated
- Incorrect Python/Node version
- Dependency version mismatch

**Context Fields:**
- `dependency`: Name of missing dependency
- `command`: Command that requires dependency
- `package_manager`: Package manager to use (pip, npm, cargo)
- `required_version`: Required version (if specified)

**Remediation Steps:**
1. Install required dependencies: `pip install -r requirements.txt`
2. Check `package.json` or `requirements.txt` for dependencies
3. Verify virtual environment is activated
4. Run dependency installation for your package manager

**Related Documentation:**
- [docs/PRODUCTION-DEPLOYMENT-GUIDE.md#prerequisites](/home/adolfo/Documents/BMAD%20Enhanced/docs/PRODUCTION-DEPLOYMENT-GUIDE.md)
- [README.md#installation](/home/adolfo/Documents/BMAD%20Enhanced/README.md)

---

#### `ERR-DEP-002`: Test Framework Not Found

**Category:** DEPENDENCY
**Severity:** ERROR

**Description:**
Test framework executable not found in PATH.

**Common Causes:**
- Framework not installed (jest, pytest, cargo)
- Framework not in system PATH
- Incorrect framework name specified

**Context Fields:**
- `framework`: Test framework name
- `command`: Framework command attempted
- `available_frameworks`: List of detected frameworks

**Remediation Steps:**
1. Install test framework: `npm install -D jest` or `pip install pytest`
2. Verify framework is in PATH: `which jest` or `which pytest`
3. Use `--framework=auto` to auto-detect available framework
4. Check framework installation documentation

**Related Documentation:**
- [docs/FRAMEWORK-SUPPORT-MATRIX.md](/home/adolfo/Documents/BMAD%20Enhanced/docs/FRAMEWORK-SUPPORT-MATRIX.md)

---

#### `ERR-DEP-003`: Incompatible Dependency Version

**Category:** DEPENDENCY
**Severity:** ERROR

**Description:**
Installed dependency version incompatible with requirements.

**Common Causes:**
- Outdated dependency version
- Breaking changes in newer versions
- Conflicting version requirements

**Context Fields:**
- `dependency`: Dependency name
- `installed_version`: Currently installed version
- `required_version`: Required version or range
- `constraint`: Version constraint specification

**Remediation Steps:**
1. Check installed version: `pip show <package>` or `npm list <package>`
2. Update to compatible version: `pip install <package>==<version>`
3. Review dependency compatibility in documentation
4. Consider upgrading code to work with newer version

---

### TIMEOUT Errors

#### `ERR-TMO-001`: Operation Timeout

**Category:** TIMEOUT
**Severity:** ERROR
**Template:** `timeout_exceeded`

**Description:**
Operation exceeded maximum allowed time and was terminated.

**Common Causes:**
- Slow tests or builds
- Network operations timing out
- Infinite loops or deadlocks
- System resource constraints

**Context Fields:**
- `command`: Command that timed out
- `timeout_sec`: Configured timeout in seconds
- `elapsed_sec`: Time elapsed before timeout
- `operation`: Specific operation that timed out

**Remediation Steps:**
1. Check if operation is stuck or slow
2. Increase timeout in `.claude/config.yaml` if needed
3. Break down operation into smaller steps
4. Review logs for performance bottlenecks

**Related Documentation:**
- [docs/V2-ARCHITECTURE.md#timeouts](/home/adolfo/Documents/BMAD%20Enhanced/docs/V2-ARCHITECTURE.md)
- [docs/PRODUCTION-MONITORING-GUIDE.md#performance-metrics](/home/adolfo/Documents/BMAD%20Enhanced/docs/PRODUCTION-MONITORING-GUIDE.md)

---

### QUALITY_GATE Errors

#### `ERR-QG-001`: Quality Gate Failed

**Category:** QUALITY_GATE
**Severity:** ERROR
**Template:** `quality_gate_failed`

**Description:**
Quality gate validation failed due to quality threshold violations.

**Common Causes:**
- Test failures or low test coverage
- High code complexity
- Code duplication issues
- Style or lint violations
- Missing documentation

**Context Fields:**
- `command`: Quality gate command
- `decision`: Gate decision (FAIL)
- `score`: Overall quality score (0-100)
- `threshold`: Required threshold score
- `issues`: Summary of quality issues

**Remediation Steps:**
1. Review the quality gate report for specific issues
2. Address failing tests or low test coverage
3. Fix code quality issues (complexity, duplication, style)
4. Use `*apply-qa-fixes` to address review comments
5. Re-run `*validate-quality-gate` after fixes

**Related Documentation:**
- [docs/quickstart-quinn.md#3-validate-quality-gate](/home/adolfo/Documents/BMAD%20Enhanced/docs/quickstart-quinn.md)
- [docs/V2-ARCHITECTURE.md#quality-gates](/home/adolfo/Documents/BMAD%20Enhanced/docs/V2-ARCHITECTURE.md)

---

#### `ERR-QG-002`: Test Coverage Insufficient

**Category:** QUALITY_GATE
**Severity:** WARNING

**Description:**
Test coverage is below recommended threshold but above critical minimum.

**Common Causes:**
- Missing edge case tests
- Untested error handling paths
- New code without tests

**Context Fields:**
- `current_coverage`: Current coverage percentage
- `recommended_coverage`: Recommended threshold (usually 80%)
- `critical_coverage`: Critical minimum (usually 60%)
- `gaps`: List of uncovered areas

**Remediation Steps:**
1. Generate coverage report: `*test --coverage`
2. Focus on uncovered critical paths
3. Add edge case and error handling tests
4. Consider if some uncovered code needs tests

**Related Documentation:**
- [docs/V2-ARCHITECTURE.md#test-coverage](/home/adolfo/Documents/BMAD%20Enhanced/docs/V2-ARCHITECTURE.md)

---

#### `ERR-QG-003`: Code Complexity Too High

**Category:** QUALITY_GATE
**Severity:** WARNING

**Description:**
Code complexity exceeds recommended threshold.

**Common Causes:**
- Long functions with many branches
- Deeply nested conditionals
- Large classes with too many responsibilities
- Complex boolean expressions

**Context Fields:**
- `file`: File with high complexity
- `function`: Function/method name
- `complexity_score`: Cyclomatic complexity
- `threshold`: Recommended threshold (usually 10-15)

**Remediation Steps:**
1. Use `*refactor` to simplify complex code
2. Extract helper functions
3. Reduce nesting with early returns
4. Apply SOLID principles
5. Consider design patterns to reduce complexity

**Related Documentation:**
- [docs/quickstart-james.md#4-refactor](/home/adolfo/Documents/BMAD%20Enhanced/docs/quickstart-james.md)
- [docs/BEST-PRACTICES.md#code-quality](/home/adolfo/Documents/BMAD%20Enhanced/docs/BEST-PRACTICES.md)

---

### COMPLEXITY Errors

#### `ERR-CMP-001`: Complexity Too High

**Category:** COMPLEXITY
**Severity:** WARNING
**Template:** `complexity_too_high`

**Description:**
Task complexity score exceeds recommended threshold, suggesting task may be too complex.

**Common Causes:**
- Large scope with many files/changes
- Unknown or unfamiliar domain
- Missing or unclear requirements
- Multiple cross-cutting concerns

**Context Fields:**
- `command`: Command being executed
- `complexity_score`: Calculated complexity (0-100)
- `threshold`: Recommended threshold (usually 70)
- `factors`: Breakdown of complexity contributors

**Remediation Steps:**
1. Review the complexity factors contributing to the high score
2. Consider breaking down the task into smaller subtasks
3. Use `*breakdown-epic` to decompose large features
4. Confirm you want to proceed with this complex task

**Related Documentation:**
- [docs/V2-ARCHITECTURE.md#complexity-assessment](/home/adolfo/Documents/BMAD%20Enhanced/docs/V2-ARCHITECTURE.md)
- [docs/quickstart-alex.md#2-breakdown-epic](/home/adolfo/Documents/BMAD%20Enhanced/docs/quickstart-alex.md)

---

### FILE_NOT_FOUND Errors

#### `ERR-FNF-001`: Task Specification Not Found

**Category:** FILE_NOT_FOUND
**Severity:** ERROR
**Template:** `missing_task_spec`

**Description:**
Required task specification file not found.

**Common Causes:**
- Task spec file not created
- Incorrect file path specified
- File in wrong directory
- File permission issues

**Context Fields:**
- `command`: Command requiring task spec
- `spec_file`: Expected task spec file path
- `cwd`: Current working directory

**Remediation Steps:**
1. Create a task specification using: `*create-task-spec --title='Your Task'`
2. Ensure the file path is correct and the file exists
3. Check that the file is in the `.claude/tasks/` directory
4. Verify file permissions allow reading

**Related Documentation:**
- [docs/quickstart-alex.md#1-create-task-spec](/home/adolfo/Documents/BMAD%20Enhanced/docs/quickstart-alex.md)
- [docs/V2-ARCHITECTURE.md#task-specifications](/home/adolfo/Documents/BMAD%20Enhanced/docs/V2-ARCHITECTURE.md)

---

#### `ERR-FNF-002`: Configuration File Not Found

**Category:** FILE_NOT_FOUND
**Severity:** ERROR

**Description:**
Required configuration file not found.

**Common Causes:**
- `.claude/config.yaml` not created
- Running from wrong directory
- Configuration file deleted or moved

**Context Fields:**
- `config_file`: Expected configuration file path
- `cwd`: Current working directory

**Remediation Steps:**
1. Copy template: `cp .claude/config.yaml.template .claude/config.yaml`
2. Navigate to project root directory
3. Verify `.claude/` directory structure exists
4. Check file permissions

**Related Documentation:**
- [docs/PRODUCTION-DEPLOYMENT-GUIDE.md#configuration](/home/adolfo/Documents/BMAD%20Enhanced/docs/PRODUCTION-DEPLOYMENT-GUIDE.md)

---

#### `ERR-FNF-003`: Test File Not Found

**Category:** FILE_NOT_FOUND
**Severity:** ERROR

**Description:**
Specified test file or test directory not found.

**Common Causes:**
- Incorrect test path specified
- Tests not yet created
- Test directory structure different than expected

**Context Fields:**
- `test_path`: Specified test path
- `expected_locations`: List of common test locations checked

**Remediation Steps:**
1. Verify test file path is correct
2. Create tests if they don't exist
3. Check common test directories: `tests/`, `test/`, `__tests__/`, `spec/`
4. Use `*test --scope=unit` to discover existing tests

**Related Documentation:**
- [docs/FRAMEWORK-SUPPORT-MATRIX.md](/home/adolfo/Documents/BMAD%20Enhanced/docs/FRAMEWORK-SUPPORT-MATRIX.md)

---

### PERMISSION Errors

#### `ERR-PRM-001`: Permission Denied

**Category:** PERMISSION
**Severity:** ERROR
**Template:** `permission_denied`

**Description:**
Permission denied when accessing file or directory.

**Common Causes:**
- Insufficient file permissions
- Directory not writable
- File locked by another process
- Running without required privileges

**Context Fields:**
- `path`: File or directory path
- `operation`: Operation attempted (read, write, execute)
- `current_permissions`: Current file permissions

**Remediation Steps:**
1. Check file/directory permissions: `ls -la`
2. Ensure you have read/write access to the path
3. Verify workspace directory is writable
4. Check if files are locked by another process

**Related Documentation:**
- [docs/PRODUCTION-SECURITY-REVIEW.md#file-permissions](/home/adolfo/Documents/BMAD%20Enhanced/docs/PRODUCTION-SECURITY-REVIEW.md)
- [docs/PRODUCTION-DEPLOYMENT-GUIDE.md#system-requirements](/home/adolfo/Documents/BMAD%20Enhanced/docs/PRODUCTION-DEPLOYMENT-GUIDE.md)

---

## Primitive Command Exit Codes

Primitive commands in `.claude/skills/bmad-commands/scripts/` use standard exit codes:

| Exit Code | Meaning | Action |
|-----------|---------|--------|
| **0** | Success | Operation completed successfully |
| **1** | General error | Check stderr for error message |
| **2** | Invalid arguments | Review command usage and parameters |
| **3** | File not found | Verify file paths are correct |
| **4** | Permission denied | Check file permissions |
| **5** | Timeout | Operation took too long, increase timeout |
| **6** | Dependency missing | Install required dependencies |
| **7** | Configuration error | Fix configuration issues |
| **8** | Test failure | Review and fix failing tests |

### Test Framework Exit Codes

Test framework adapters return framework-specific exit codes:

**Jest:**
- `0`: All tests passed
- `1`: Tests failed
- `2`: Configuration error

**Pytest:**
- `0`: All tests passed
- `1`: Tests failed
- `2`: Tests interrupted
- `3`: Internal error
- `4`: Command line usage error
- `5`: No tests collected

**Cargo (Rust):**
- `0`: All tests passed
- `101`: Tests failed

**Go Test:**
- `0`: All tests passed
- `1`: Tests failed

---

## Error Response Format

All BMAD Enhanced errors follow a structured JSON format:

```json
{
  "success": false,
  "outputs": {},
  "telemetry": {
    "command": "command_name",
    "duration_ms": 0,
    "timestamp": "2025-11-05T10:00:00Z"
  },
  "errors": [
    "error_code: description",
    "hint: additional_guidance"
  ]
}
```

### Error Response Fields

- **success**: Boolean indicating operation success (false for errors)
- **outputs**: Empty object for error responses
- **telemetry**: Metadata about the operation
  - `command`: Command that was executed
  - `duration_ms`: Time taken before error
  - `timestamp`: ISO 8601 timestamp
- **errors**: Array of error messages
  - First element: Primary error code and description
  - Subsequent elements: Additional context, hints, or related errors

---

## Using the Error Handler

### Python Scripts

```python
from scripts.error_handler import ErrorHandler, ErrorCategory, ErrorSeverity

handler = ErrorHandler(log_file=".claude/logs/errors.log")

# Create error from template
error = handler.create_error(
    "missing_task_spec",
    context={
        "command": "*implement",
        "spec_file": ".claude/tasks/task-001-spec.md",
        "cwd": "/home/user/project"
    }
)

# Handle and display error
handler.handle_error(error, exit_on_error=True)
```

### Custom Errors

```python
from scripts.error_handler import BMADError, ErrorCategory, ErrorSeverity

error = BMADError(
    category=ErrorCategory.EXECUTION,
    severity=ErrorSeverity.ERROR,
    message="Custom error message",
    context={
        "key1": "value1",
        "key2": "value2"
    },
    remediation_steps=[
        "Step 1 to fix the issue",
        "Step 2 if step 1 doesn't work"
    ],
    documentation_links=[
        "docs/relevant-guide.md"
    ]
)

print(error.format())
```

---

## Error Logging

All errors are logged to `.claude/logs/errors.log` in JSON format for analysis and debugging:

```json
{
  "category": "quality_gate",
  "severity": "error",
  "message": "Quality gate validation failed",
  "context": {
    "command": "*validate-quality-gate",
    "decision": "FAIL",
    "score": 45,
    "threshold": 60
  },
  "remediation_steps": [...],
  "documentation_links": [...],
  "related_errors": [],
  "timestamp": "2025-11-05T10:00:00.123Z"
}
```

### Log Analysis

View recent errors:
```bash
tail -f .claude/logs/errors.log | jq '.'
```

Count errors by category:
```bash
cat .claude/logs/errors.log | jq -r '.category' | sort | uniq -c
```

Find errors by severity:
```bash
cat .claude/logs/errors.log | jq 'select(.severity == "critical")'
```

---

## Best Practices

### 1. Error Handling in Skills

All skills should:
- Use standardized error templates when possible
- Provide actionable remediation steps
- Include relevant context information
- Link to appropriate documentation
- Log errors for debugging

### 2. Error Recovery

When an error occurs:
1. **Read the error message carefully** - provides specific issue details
2. **Check context fields** - understand what triggered the error
3. **Follow remediation steps** - in order, don't skip steps
4. **Consult documentation links** - for detailed guidance
5. **Check related errors** - may indicate root cause

### 3. Debugging Errors

For persistent errors:
1. Check error log: `.claude/logs/errors.log`
2. Review telemetry data for patterns
3. Verify system prerequisites are met
4. Test with minimal reproduction case
5. Enable debug logging in configuration

---

## Related Documentation

- [V2-ARCHITECTURE.md](/home/adolfo/Documents/BMAD%20Enhanced/docs/V2-ARCHITECTURE.md) - Architecture and error handling framework
- [TROUBLESHOOTING.md](/home/adolfo/Documents/BMAD%20Enhanced/docs/TROUBLESHOOTING.md) - Common issues and solutions
- [PRODUCTION-MONITORING-GUIDE.md](/home/adolfo/Documents/BMAD%20Enhanced/docs/PRODUCTION-MONITORING-GUIDE.md) - Error monitoring and alerting
- [BEST-PRACTICES.md](/home/adolfo/Documents/BMAD%20Enhanced/docs/BEST-PRACTICES.md) - Error handling best practices

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0 | 2025-11-05 | Initial comprehensive error codes documentation |

---

**Maintained by:** BMAD Enhanced Development Team
**Contact:** See [README.md](/home/adolfo/Documents/BMAD%20Enhanced/README.md) for support information
