# BMAD Enhanced - UX Improvements Guide

This guide explains the new UX improvements in BMAD Enhanced V2, including how to use the interactive command wizard, progress visualization, improved error handling, and example workflows.

## Table of Contents

1. [Overview](#overview)
2. [Interactive Command Wizard](#interactive-command-wizard)
3. [Progress Visualization](#progress-visualization)
4. [Improved Error Messages](#improved-error-messages)
5. [Example Workflows](#example-workflows)
6. [Integration Examples](#integration-examples)
7. [Best Practices](#best-practices)

---

## Overview

BMAD Enhanced V2 includes four major UX improvements to make the system more accessible and easier to use:

| Component | Purpose | Location |
|-----------|---------|----------|
| **Command Wizard** | Interactive tool to find the right command | `.claude/skills/bmad-commands/scripts/bmad-wizard.py` |
| **Progress Visualization** | Real-time progress tracking for operations | `.claude/skills/bmad-commands/scripts/progress-visualizer.py` |
| **Error Handler** | Helpful error messages with remediation | `.claude/skills/bmad-commands/scripts/error-handler.py` |
| **Example Workflows** | Practical, copy-paste ready examples | `docs/EXAMPLE-WORKFLOWS.md` |

---

## Interactive Command Wizard

### What It Does

The command wizard helps you navigate BMAD's 19 commands across 4 subagents by:
- Asking about your goal
- Recommending appropriate commands
- Providing usage examples
- Linking to relevant documentation

### Basic Usage

```bash
# Run interactive wizard
python .claude/skills/bmad-commands/scripts/bmad-wizard.py

# List all commands
python .claude/skills/bmad-commands/scripts/bmad-wizard.py --list-all

# Show commands for specific subagent
python .claude/skills/bmad-commands/scripts/bmad-wizard.py --subagent alex
python .claude/skills/bmad-commands/scripts/bmad-wizard.py --subagent james
python .claude/skills/bmad-commands/scripts/bmad-wizard.py --subagent quinn
python .claude/skills/bmad-commands/scripts/bmad-wizard.py --subagent orchestrator

# Show help
python .claude/skills/bmad-commands/scripts/bmad-wizard.py --help
```

### Interactive Mode Example

```
$ python .claude/skills/bmad-commands/scripts/bmad-wizard.py

======================================================================
                  BMAD Enhanced - Command Wizard
======================================================================

Welcome to the BMAD Enhanced Command Wizard!
This tool helps you find the right command for your task.

What would you like to do?
(Describe your goal in a few words, e.g., 'implement a new feature', 'fix a bug', 'review code')
> implement a new authentication feature

Recommendation for: 'implement a new authentication feature'
────────────────────────────────────────────────────────────────────

Recommended Subagent: James (Developer)
Description: Implementation, testing, and debugging
Documentation: docs/quickstart-james.md

Recommended Commands:

[1] *implement
    Implement features from specifications
    *implement --spec=.claude/tasks/task-001-spec.md --tdd=true

[2] *test
    Run tests and analyze results
    *test --scope=unit --coverage-threshold=80

Would you like to:
  1. See detailed information about a command
  2. Browse all commands
  3. Exit
Choice (1-3): 1

Enter command number (1-2): 1

Command: *implement
Description: Implement features from specifications
Complexity: Medium-High
Duration: 15-60 minutes

Use when:
  • Have a task spec ready
  • Starting feature development
  • Following TDD approach
  • Need production-ready code

Example:
  *implement --spec=.claude/tasks/task-001-spec.md --tdd=true
```

### Goal-Based Recommendations

The wizard understands these goal categories:

| Goal Keywords | Recommended Subagent | Commands |
|---------------|---------------------|----------|
| plan, requirement, spec, story, epic | Alex (Planner) | *create-task-spec, *breakdown-epic, *plan-sprint |
| implement, code, develop, build, feature | James (Developer) | *implement, *test |
| fix, bug, issue, problem, debug | James (Developer) | *fix, *debug, *test |
| refactor, improve, optimize, clean | James (Developer) | *refactor, *test |
| review, quality, check, assess | Quinn (Quality) | *review, *validate-quality-gate |
| security, performance, nfr | Quinn (Quality) | *assess-nfr, *assess-risk |
| workflow, orchestrate, coordinate | Orchestrator | *workflow, *coordinate |
| understand, explain, documentation | James (Developer) | *explain |

---

## Progress Visualization

### What It Does

The progress visualization system provides real-time feedback during operations:
- Shows current step in 7-step workflow
- Displays progress percentage and ETA
- Tracks elapsed time
- Provides substep updates

### Usage in Skills

```python
from scripts.progress_visualizer import WorkflowProgress, WorkflowStep

# Create progress tracker
progress = WorkflowProgress("feature-delivery", "james", "*implement")
progress.start()

# Step 1: Load Context
progress.load_context("Loading task spec and project context")

# Step 2: Assess Complexity
complexity_score = 65
progress.assess_complexity(score=complexity_score)

# Step 3: Route Strategy
strategy = "complex" if complexity_score > 60 else "standard"
progress.route_strategy(strategy)

# Step 4: Check Guardrails
guardrails_passed = check_guardrails()
progress.check_guardrails(passed=guardrails_passed)

# Step 5: Execute
progress.execute("Implementing feature with TDD approach")

# Substeps during execution
progress.execute_substep("Writing unit tests")
progress.execute_substep("Implementing core logic")
progress.execute_substep("Running tests")

# Step 6: Verify
verification_passed = run_verification()
progress.verify(success=verification_passed)

# Step 7: Telemetry
progress.emit_telemetry()

# Complete
progress.complete("Feature implemented successfully with 95% test coverage")
```

### Progress Styles

The system supports multiple visualization styles:

```python
from scripts.progress_visualizer import ProgressTracker, ProgressStyle

# Bar style (default)
tracker = ProgressTracker(style=ProgressStyle.BAR)
# Output: ▶ [████████░░] 80% | Step 5/7: Execute

# Spinner style
tracker = ProgressTracker(style=ProgressStyle.SPINNER)
# Output: ⠋ Step 5/7: Execute - Implementing feature

# Dots style
tracker = ProgressTracker(style=ProgressStyle.DOTS)
# Output: • Execute... Implementing feature

# Minimal style
tracker = ProgressTracker(style=ProgressStyle.MINIMAL)
# Output: ▶ [5/7] Execute - Implementing feature
```

### Example Output

```
Starting: james - *implement

▶ [█████░░░░░░░░░] 14% | Step 1/7: Load Context | 0.5s
   Loading configuration and context

▶ [███████████░░░] 28% | Step 2/7: Assess Complexity | ETA: 45s | 1.2s
   Analyzing complexity factors

▶ [█████████████░░] 42% | Step 3/7: Route Strategy | ETA: 38s | 0.8s
   Strategy: complex

▶ [███████████████░] 57% | Step 4/7: Check Guardrails | ETA: 30s | 1.0s
   All guardrails passed

▶ [█████████████████] 71% | Step 5/7: Execute | ETA: 20s | 15.3s
   Executing primary operation
  ↳ Writing unit tests
  ↳ Implementing core logic
  ↳ Running tests

▶ [███████████████████] 85% | Step 6/7: Verify Results | ETA: 8s | 3.2s
   Verification successful

▶ [█████████████████████] 100% | Step 7/7: Emit Telemetry | 0.5s
   Recording telemetry

✓ Feature implemented successfully with 95% test coverage
  Total time: 22.5s
```

---

## Improved Error Messages

### What It Does

The error handler provides:
- Clear, structured error messages
- Root cause analysis
- Step-by-step remediation guidance
- Links to relevant documentation
- Context-specific information

### Error Categories

| Category | Description | Examples |
|----------|-------------|----------|
| `validation` | Input validation failures | Invalid parameters, missing required fields |
| `configuration` | Configuration issues | Invalid YAML, missing config |
| `guardrail` | Guardrail violations | Sensitive file access, quality thresholds |
| `execution` | Runtime errors | Test failures, build errors |
| `dependency` | Missing dependencies | Package not installed |
| `timeout` | Operation timeouts | Long-running operation exceeded limit |
| `quality_gate` | Quality gate failures | Coverage too low, tests failing |
| `complexity` | High complexity warnings | Task too complex |
| `file_not_found` | Missing files | Task spec not found |
| `permission` | Permission issues | File access denied |

### Usage in Skills

```python
from scripts.error_handler import ErrorHandler, BMADError, ErrorCategory, ErrorSeverity

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

# Display error
handler.handle_error(error)

# Create custom error
custom_error = BMADError(
    category=ErrorCategory.EXECUTION,
    severity=ErrorSeverity.ERROR,
    message="Custom error message",
    context={"key": "value"},
    remediation_steps=[
        "Step 1 to fix",
        "Step 2 to fix"
    ],
    documentation_links=[
        "docs/relevant-doc.md"
    ]
)

handler.handle_error(custom_error)
```

### Example Error Messages

#### Missing Task Spec
```
======================================================================
✗ ERROR: File Not Found
======================================================================

Message:
  Task specification file not found

Context:
  • command: *implement
  • spec_file: .claude/tasks/task-001-spec.md
  • cwd: /home/user/project

How to Fix:
  1. Create a task specification using: *create-task-spec --title='Your Task'
  2. Ensure the file path is correct and the file exists
  3. Check that the file is in the .claude/tasks/ directory
  4. Verify file permissions allow reading

Related Documentation:
  • docs/quickstart-alex.md#1-create-task-spec
  • docs/V2-ARCHITECTURE.md#task-specifications

Timestamp: 2025-01-04T10:30:45
======================================================================
```

#### Quality Gate Failure
```
======================================================================
✗ ERROR: Quality Gate
======================================================================

Message:
  Quality gate validation failed

Context:
  • command: *validate-quality-gate
  • decision: FAIL
  • score: 45
  • threshold: 60
  • issues: 3 failing tests, 55% coverage (target: 80%)

How to Fix:
  1. Review the quality gate report for specific issues
  2. Address failing tests or low test coverage
  3. Fix code quality issues (complexity, duplication, style)
  4. Use *apply-qa-fixes to address review comments
  5. Re-run *validate-quality-gate after fixes
  6. Focus on increasing test coverage in src/payment/ module
  7. Fix failing integration tests in tests/test_checkout.py

Related Documentation:
  • docs/quickstart-quinn.md#3-validate-quality-gate
  • docs/V2-ARCHITECTURE.md#quality-gates

Timestamp: 2025-01-04T10:45:12
======================================================================
```

#### Guardrail Violation
```
======================================================================
🚨 CRITICAL: Guardrail
======================================================================

Message:
  Guardrail violation detected - operation blocked

Context:
  • command: *implement
  • violation: Attempting to access sensitive file
  • file: .env
  • guardrail: block_sensitive_files

How to Fix:
  1. Review the specific guardrail that was violated
  2. Check if sensitive files are being accessed
  3. Verify test coverage meets minimum threshold
  4. Ensure code meets quality standards
  5. Review .claude/config.yaml for guardrail configuration

Related Documentation:
  • docs/V2-ARCHITECTURE.md#guardrails-framework
  • docs/PRODUCTION-SECURITY-REVIEW.md

Timestamp: 2025-01-04T11:00:00
======================================================================
```

### Available Error Templates

- `missing_task_spec` - Task specification not found
- `complexity_too_high` - Task complexity exceeds threshold
- `guardrail_violation` - Guardrail check failed
- `quality_gate_failed` - Quality gate validation failed
- `test_failure` - Tests failed during execution
- `missing_dependency` - Required dependency not installed
- `timeout_exceeded` - Operation exceeded time limit
- `configuration_error` - Configuration file issue
- `permission_denied` - File/directory access denied
- `validation_error` - Input validation failed

---

## Example Workflows

### What It Provides

The example workflows documentation (`docs/EXAMPLE-WORKFLOWS.md`) includes:
- 11 complete, practical workflows
- Step-by-step instructions
- Copy-paste ready commands
- Expected outputs and durations
- Tips and best practices

### Workflow Categories

1. **Feature Development** (3 workflows)
   - Complete feature delivery (orchestrated)
   - Manual feature development
   - TDD feature development

2. **Bug Fixing** (2 workflows)
   - Simple bug fix
   - Complex bug investigation

3. **Quality Improvement** (2 workflows)
   - Code quality improvement
   - QA review cycle

4. **Sprint Planning** (2 workflows)
   - Epic to sprint plan
   - Sprint execution

5. **Architecture & Refactoring** (2 workflows)
   - Refactoring with safety
   - Risk assessment for major changes

### Quick Access

```bash
# View example workflows
cat docs/EXAMPLE-WORKFLOWS.md

# Or open in your preferred editor
code docs/EXAMPLE-WORKFLOWS.md
vim docs/EXAMPLE-WORKFLOWS.md
```

---

## Integration Examples

### Example 1: Complete Feature with All UX Components

```python
#!/usr/bin/env python3
"""Complete feature implementation with full UX integration"""

import sys
from scripts.progress_visualizer import WorkflowProgress
from scripts.error_handler import ErrorHandler, ErrorCategory, ErrorSeverity
from pathlib import Path

def implement_feature(spec_file: str):
    """Implement feature with progress tracking and error handling"""

    # Initialize components
    progress = WorkflowProgress("feature-delivery", "james", "*implement")
    error_handler = ErrorHandler(log_file=".claude/logs/errors.log")

    try:
        # Start progress tracking
        progress.start()

        # Step 1: Load Context
        progress.load_context("Loading task spec and project context")

        if not Path(spec_file).exists():
            error = error_handler.create_error(
                "missing_task_spec",
                context={
                    "command": "*implement",
                    "spec_file": spec_file,
                    "cwd": str(Path.cwd())
                }
            )
            error_handler.handle_error(error, exit_on_error=True)

        spec = load_spec(spec_file)

        # Step 2: Assess Complexity
        progress.assess_complexity()
        complexity_score = assess_complexity(spec)

        if complexity_score > 80:
            error = error_handler.create_error(
                "complexity_too_high",
                context={
                    "command": "*implement",
                    "complexity_score": complexity_score,
                    "threshold": 70
                }
            )
            error_handler.handle_error(error)  # Warning only

        # Step 3: Route Strategy
        strategy = "complex" if complexity_score > 60 else "standard"
        progress.route_strategy(strategy)

        # Step 4: Check Guardrails
        progress.check_guardrails()
        guardrails_passed, violations = check_guardrails(spec)

        if not guardrails_passed:
            error = error_handler.create_error(
                "guardrail_violation",
                context={
                    "command": "*implement",
                    "violations": violations
                }
            )
            error_handler.handle_error(error, exit_on_error=True)

        progress.check_guardrails(passed=True)

        # Step 5: Execute
        progress.execute("Implementing feature with TDD approach")

        progress.execute_substep("Writing unit tests")
        write_tests(spec)

        progress.execute_substep("Implementing core logic")
        implement_code(spec)

        progress.execute_substep("Running tests")
        test_result = run_tests()

        if not test_result.success:
            error = error_handler.create_error(
                "test_failure",
                context={
                    "command": "*test",
                    "failures": test_result.failures,
                    "coverage": test_result.coverage
                }
            )
            error_handler.handle_error(error, exit_on_error=True)

        # Step 6: Verify
        progress.verify()
        verification_result = verify_implementation(spec)
        progress.verify(success=verification_result.success)

        # Step 7: Telemetry
        progress.emit_telemetry()
        emit_telemetry({
            "command": "*implement",
            "complexity": complexity_score,
            "strategy": strategy,
            "test_coverage": test_result.coverage,
            "duration": progress.tracker.total_elapsed()
        })

        # Complete
        progress.complete(
            f"Feature implemented successfully with {test_result.coverage}% test coverage"
        )

    except Exception as e:
        progress.error(f"Implementation failed: {str(e)}")
        raise

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: implement_feature.py <spec-file>")
        sys.exit(1)

    implement_feature(sys.argv[1])
```

### Example 2: User-Friendly Command Interface

```python
#!/usr/bin/env python3
"""User-friendly wrapper for BMAD commands"""

import sys
import argparse
from scripts.progress_visualizer import WorkflowProgress
from scripts.error_handler import ErrorHandler

def main():
    parser = argparse.ArgumentParser(
        description="BMAD Enhanced - User-Friendly Interface",
        epilog="For help choosing a command, run: python .claude/skills/bmad-commands/scripts/bmad-wizard.py"
    )

    parser.add_argument("goal", help="What you want to do (e.g., 'implement feature')")
    parser.add_argument("--show-progress", action="store_true", help="Show progress bar")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")

    args = parser.parse_args()

    # Initialize error handler
    error_handler = ErrorHandler()

    # Suggest using wizard for first-time users
    if not args.goal:
        print("💡 Not sure which command to use?")
        print("   Run: python .claude/skills/bmad-commands/scripts/bmad-wizard.py")
        print()
        parser.print_help()
        sys.exit(0)

    # Execute command with progress tracking
    if args.show_progress:
        progress = WorkflowProgress("operation", "bmad", args.goal)
        progress.start()
        # ... execute command ...
        progress.complete()
    else:
        # Execute without progress tracking
        pass

if __name__ == "__main__":
    main()
```

---

## Best Practices

### 1. Always Use the Wizard for New Users

```bash
# First time using BMAD? Start here:
python .claude/skills/bmad-commands/scripts/bmad-wizard.py
```

### 2. Enable Progress Tracking for Long Operations

```python
# For operations > 30 seconds, always show progress
if estimated_duration > 30:
    progress = WorkflowProgress(...)
    progress.start()
```

### 3. Provide Context in Error Messages

```python
# Always include relevant context
error = handler.create_error(
    "error_template",
    context={
        "command": command_name,
        "file": file_path,
        "cwd": current_directory,
        "user_input": user_provided_values
    }
)
```

### 4. Reference Example Workflows

```bash
# Before implementing a complex workflow:
# 1. Check docs/EXAMPLE-WORKFLOWS.md for similar examples
# 2. Copy and adapt the example
# 3. Customize for your specific needs
```

### 5. Log Errors for Debugging

```python
# Always log errors to file for later analysis
handler = ErrorHandler(log_file=".claude/logs/errors.log")
```

### 6. Use Appropriate Progress Styles

```python
# Simple operations: MINIMAL
# Standard operations: BAR (default)
# Background operations: SPINNER
# Batch operations: DOTS
```

---

## Testing the UX Improvements

### Test Command Wizard

```bash
# Test interactive mode
python .claude/skills/bmad-commands/scripts/bmad-wizard.py

# Test list mode
python .claude/skills/bmad-commands/scripts/bmad-wizard.py --list-all

# Test subagent filtering
python .claude/skills/bmad-commands/scripts/bmad-wizard.py --subagent james
```

### Test Progress Visualization

```bash
# Run demo
python .claude/skills/bmad-commands/scripts/progress-visualizer.py

# Expected output: Multiple demos showing different progress styles
```

### Test Error Handling

```bash
# Run demo
python .claude/skills/bmad-commands/scripts/error-handler.py

# Expected output: 4 different error examples with full formatting
```

### Verify Example Workflows

```bash
# Ensure file exists and is readable
cat docs/EXAMPLE-WORKFLOWS.md | wc -l
# Expected: ~800+ lines

# Check table of contents
head -50 docs/EXAMPLE-WORKFLOWS.md
```

---

## Troubleshooting

### Command Wizard Not Working

```bash
# Ensure script is executable
chmod +x .claude/skills/bmad-commands/scripts/bmad-wizard.py

# Test Python version
python --version  # Should be 3.8+

# Run directly
python3 .claude/skills/bmad-commands/scripts/bmad-wizard.py
```

### Progress Not Displaying

```python
# Check that output is not being redirected
# Progress writes to stderr by default

# Explicitly flush output
import sys
sys.stderr.flush()
```

### Errors Not Formatted

```bash
# Ensure terminal supports ANSI colors
echo $TERM  # Should show color terminal (xterm-256color, etc.)

# Test color support
python -c "from scripts.error_handler import Colors; print(f'{Colors.RED}Red{Colors.ENDC}')"
```

---

## Related Documentation

- [V2 Architecture](./V2-ARCHITECTURE.md) - System architecture
- [Example Workflows](./EXAMPLE-WORKFLOWS.md) - Practical examples
- [Quick Start Guides](./DOCUMENTATION-INDEX.md#quick-start-guides) - Subagent guides
- [Production Deployment](./PRODUCTION-DEPLOYMENT-GUIDE.md) - Production setup

---

**Last Updated:** 2025-01-04
**Version:** V2.0
**Status:** Production Ready
