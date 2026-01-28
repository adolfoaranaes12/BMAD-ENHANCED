# BMAD Enhanced - Complete Parameter Documentation

**Version:** 2.0
**Last Updated:** 2025-11-05
**Status:** Production Ready

## Overview

This document provides comprehensive parameter documentation for all utility functions, primitive commands, and APIs in BMAD Enhanced. Each function includes parameter types, defaults, validation rules, and usage examples.

---

## Table of Contents

1. [Primitive Commands](#primitive-commands)
2. [Test Framework Registry](#test-framework-registry)
3. [Architecture Utilities](#architecture-utilities)
4. [Command Parsing](#command-parsing)
5. [Error Handling](#error-handling)
6. [UX Tools](#ux-tools)

---

## Primitive Commands

### run_tests

Execute tests with specified framework using adapter pattern.

**Location:** `.claude/skills/bmad-commands/scripts/run_tests.py`

#### `run_tests_v2(path, framework, timeout_sec, with_coverage)`

**Description:** Execute tests using framework adapter (v2).

**Parameters:**

| Parameter | Type | Default | Required | Description | Validation |
|-----------|------|---------|----------|-------------|------------|
| `path` | `str` | - | Yes | Path to test file or directory | Must be a valid file/directory path |
| `framework` | `str` | `"auto"` | No | Test framework to use | One of: `auto`, `jest`, `pytest`, `cargo`, `go`, `junit`, `gtest` |
| `timeout_sec` | `int` | `120` | No | Maximum test execution time in seconds | Must be positive integer, recommended: 60-300 |
| `with_coverage` | `bool` | `False` | No | Enable code coverage reporting | Boolean flag |

**Returns:** `dict` - Standard BMAD command response

**Return Structure:**
```python
{
    "success": bool,
    "outputs": {
        "total_tests": int,
        "passed_tests": int,
        "failed_tests": int,
        "skipped_tests": int,
        "coverage_pct": float,  # If with_coverage=True
        "test_duration_ms": int
    },
    "telemetry": {
        "command": "run_tests",
        "framework": str,
        "duration_ms": int,
        "timestamp": str
    },
    "errors": List[str]
}
```

**Example Usage:**
```python
# Auto-detect framework
result = run_tests_v2("tests/", framework="auto")

# Explicit framework with coverage
result = run_tests_v2("src/", framework="jest", timeout_sec=180, with_coverage=True)

# Quick unit tests
result = run_tests_v2("tests/unit/", framework="pytest", timeout_sec=60)
```

**Error Codes:**
- `no_framework_detected`: No test framework found (use `--framework` explicitly)
- `unsupported_framework`: Framework not supported
- `timeout_exceeded`: Test execution exceeded timeout
- `test_failure`: One or more tests failed
- `file_not_found`: Test path does not exist

---

### read_file

Read file contents with structured output.

**Location:** `.claude/skills/bmad-commands/scripts/read_file.py`

#### `read_file(file_path, encoding, max_lines)`

**Description:** Read file contents and return structured result.

**Parameters:**

| Parameter | Type | Default | Required | Description | Validation |
|-----------|------|---------|----------|-------------|------------|
| `file_path` | `str` | - | Yes | Path to file to read | Must be existing file with read permissions |
| `encoding` | `str` | `"utf-8"` | No | File encoding | One of: `utf-8`, `ascii`, `latin-1`, `utf-16` |
| `max_lines` | `int` | `None` | No | Maximum number of lines to read | Must be positive integer or None for all lines |

**Returns:** `dict` - Standard BMAD command response

**Return Structure:**
```python
{
    "success": bool,
    "outputs": {
        "content": str,
        "line_count": int,
        "file_size_bytes": int,
        "encoding": str,
        "truncated": bool  # True if max_lines applied
    },
    "telemetry": {
        "command": "read_file",
        "file_path": str,
        "duration_ms": int,
        "timestamp": str
    },
    "errors": List[str]
}
```

**Example Usage:**
```python
# Read entire file
result = read_file("src/main.py")

# Read first 100 lines
result = read_file("logs/app.log", max_lines=100)

# Read with specific encoding
result = read_file("data.txt", encoding="latin-1")
```

---

## Test Framework Registry

### FrameworkRegistry

Manages test framework adapters from configuration.

**Location:** `.claude/skills/bmad-commands/scripts/framework_registry.py`

#### `__init__(config_path)`

**Description:** Initialize registry and load adapters from config.

**Parameters:**

| Parameter | Type | Default | Required | Description | Validation |
|-----------|------|---------|----------|-------------|------------|
| `config_path` | `Optional[Path]` | `None` | No | Path to `.claude/config.yaml` | Must be valid YAML file if provided. Auto-detected if None. |

**Example Usage:**
```python
# Auto-detect config
registry = FrameworkRegistry()

# Explicit config path
registry = FrameworkRegistry(config_path=Path(".claude/config.yaml"))
```

---

#### `detect_framework(path)`

**Description:** Auto-detect test framework in project.

**Parameters:**

| Parameter | Type | Default | Required | Description | Validation |
|-----------|------|---------|----------|-------------|------------|
| `path` | `Path` | - | Yes | Project root path | Must be existing directory |

**Returns:** `Optional[str]` - Framework name if detected, `None` otherwise

**Detection Logic:**
1. Checks for `package.json` with `jest` in dependencies → `jest`
2. Checks for `pytest.ini`, `pyproject.toml`, or `setup.cfg` → `pytest`
3. Checks for `Cargo.toml` → `cargo`
4. Checks for `go.mod` → `go`
5. Checks for `pom.xml` or `build.gradle` → `junit`
6. Checks for `CMakeLists.txt` with gtest → `gtest`

**Example Usage:**
```python
registry = FrameworkRegistry()
framework = registry.detect_framework(Path("."))
if framework:
    print(f"Detected: {framework}")
else:
    print("No framework detected")
```

---

#### `get_adapter(framework)`

**Description:** Get adapter for specified framework.

**Parameters:**

| Parameter | Type | Default | Required | Description | Validation |
|-----------|------|---------|----------|-------------|------------|
| `framework` | `str` | - | Yes | Framework name | Must be registered framework name |

**Returns:** `Optional[FrameworkAdapter]` - Adapter instance or `None`

**Example Usage:**
```python
registry = FrameworkRegistry()
adapter = registry.get_adapter("jest")
if adapter:
    result = adapter.run_tests(Path("tests/"))
```

---

#### `list_frameworks()`

**Description:** List all registered frameworks.

**Parameters:** None

**Returns:** `List[str]` - List of registered framework names

**Example Usage:**
```python
registry = FrameworkRegistry()
frameworks = registry.list_frameworks()
print(f"Available: {', '.join(frameworks)}")
```

---

## Architecture Utilities

### generate_architecture_diagram

Generate architecture diagrams from architecture documents.

**Location:** `.claude/skills/bmad-commands/scripts/generate_architecture_diagram.py`

#### `generate_diagram(architecture_path, diagram_type, output_dir)`

**Description:** Generate architecture diagram from architecture document.

**Parameters:**

| Parameter | Type | Default | Required | Description | Validation |
|-----------|------|---------|----------|-------------|------------|
| `architecture_path` | `str` | - | Yes | Path to architecture document | Must be existing file (`.md` or `.yaml`) |
| `diagram_type` | `str` | - | Yes | Type of diagram to generate | One of: `c4-context`, `c4-container`, `c4-component`, `deployment`, `sequence`, `data-flow` |
| `output_dir` | `str` | - | Yes | Directory to save generated diagrams | Must be writable directory (created if not exists) |

**Returns:** `dict` - Standard BMAD command response

**Return Structure:**
```python
{
    "success": bool,
    "outputs": {
        "diagram_path": str,        # Absolute path to generated SVG
        "diagram_type": str,        # Type of diagram generated
        "diagram_format": str,      # Always "svg"
        "architecture_source": str  # Source architecture file
    },
    "telemetry": {
        "command": "generate_architecture_diagram",
        "diagram_type": str,
        "duration_ms": int,
        "timestamp": str
    },
    "errors": List[str]
}
```

**Supported Diagram Types:**

| Type | Description | Output |
|------|-------------|--------|
| `c4-context` | System context diagram (C4 Level 1) | Shows system boundaries and external actors |
| `c4-container` | Container diagram (C4 Level 2) | Shows major containers (apps, databases, etc.) |
| `c4-component` | Component diagram (C4 Level 3) | Shows internal components within containers |
| `deployment` | Deployment architecture | Shows infrastructure and deployment topology |
| `sequence` | Sequence diagram | Shows interaction flows between components |
| `data-flow` | Data flow diagram | Shows data movement through system |

**Example Usage:**
```python
# Generate C4 context diagram
result = generate_diagram(
    architecture_path="docs/architecture.md",
    diagram_type="c4-context",
    output_dir="docs/diagrams/"
)

# Generate deployment diagram
result = generate_diagram(
    architecture_path=".claude/architecture/system-design.yaml",
    diagram_type="deployment",
    output_dir=".claude/diagrams/"
)
```

---

### analyze_tech_stack

Analyze technology stack choices from architecture document.

**Location:** `.claude/skills/bmad-commands/scripts/analyze_tech_stack.py`

#### `analyze_tech_stack(architecture_path)`

**Description:** Analyze technology stack from architecture document, validate compatibility, identify risks, and suggest alternatives.

**Parameters:**

| Parameter | Type | Default | Required | Description | Validation |
|-----------|------|---------|----------|-------------|------------|
| `architecture_path` | `str` | - | Yes | Path to architecture document | Must be existing file (`.md` or `.yaml`) |

**Returns:** `dict` - Standard BMAD command response with tech stack analysis

**Return Structure:**
```python
{
    "success": bool,
    "outputs": {
        "technologies": List[{
            "name": str,           # Technology name
            "category": str,       # frontend, backend, database, etc.
            "version": str,        # Version or version range
            "maturity": str,       # stable, beta, experimental
            "license": str         # MIT, Apache, proprietary, etc.
        }],
        "tech_count": int,
        "categories": List[str],
        "compatibility": {
            "issues": List[str],          # Critical compatibility issues
            "warnings": List[str],        # Minor warnings
            "recommendations": List[str]  # Suggestions for improvement
        },
        "risks": List[{
            "technology": str,
            "risk_level": str,     # low, medium, high
            "description": str,
            "mitigation": str
        }],
        "alternatives": List[{
            "for_technology": str,
            "alternative": str,
            "reason": str
        }],
        "architecture_source": str
    },
    "telemetry": {
        "command": "analyze_tech_stack",
        "tech_count": int,
        "duration_ms": int,
        "timestamp": str
    },
    "errors": List[str]
}
```

**Technology Categories:**

| Category | Examples | Detection Keywords |
|----------|----------|-------------------|
| `frontend` | React, Vue, Angular, Svelte | React, Vue.js, Angular, Svelte |
| `backend` | Node.js, Python, Java, Go | Node, Express, Django, Spring |
| `database` | PostgreSQL, MongoDB, MySQL | Postgres, Mongo, MySQL, Redis |
| `cache` | Redis, Memcached | Redis, Memcached |
| `messaging` | RabbitMQ, Kafka | RabbitMQ, Kafka, SQS |
| `infrastructure` | Docker, Kubernetes, AWS | Docker, K8s, AWS, Azure, GCP |
| `testing` | Jest, Pytest, JUnit | Jest, Pytest, JUnit |
| `ci_cd` | GitHub Actions, Jenkins | GitHub Actions, CircleCI, Jenkins |

**Example Usage:**
```python
# Analyze tech stack
result = analyze_tech_stack("docs/architecture/system-design.md")

if result["success"]:
    techs = result["outputs"]["technologies"]
    for tech in techs:
        print(f"{tech['name']} ({tech['category']}): {tech['version']}")

    # Check for compatibility issues
    issues = result["outputs"]["compatibility"]["issues"]
    if issues:
        print(f"⚠️  Compatibility issues: {len(issues)}")
```

---

### extract_adrs

Extract Architecture Decision Records (ADRs) from architecture documents.

**Location:** `.claude/skills/bmad-commands/scripts/extract_adrs.py`

#### `extract_adrs(architecture_path, output_dir)`

**Description:** Extract ADRs from architecture document and save as individual files.

**Parameters:**

| Parameter | Type | Default | Required | Description | Validation |
|-----------|------|---------|----------|-------------|------------|
| `architecture_path` | `str` | - | Yes | Path to architecture document | Must be existing file |
| `output_dir` | `str` | `"docs/adrs"` | No | Directory to save extracted ADRs | Created if not exists |

**Returns:** `dict` - Standard BMAD command response

**Return Structure:**
```python
{
    "success": bool,
    "outputs": {
        "adrs_extracted": int,
        "adr_files": List[str],  # Paths to generated ADR files
        "adr_summary": List[{
            "id": str,            # ADR-001, ADR-002, etc.
            "title": str,
            "status": str,        # Proposed, Accepted, Deprecated, Superseded
            "date": str,
            "file_path": str
        }]
    },
    "telemetry": {
        "command": "extract_adrs",
        "adrs_count": int,
        "duration_ms": int,
        "timestamp": str
    },
    "errors": List[str]
}
```

**ADR Format:**
Each extracted ADR follows the standard format:
```markdown
# ADR-XXX: [Title]

**Status:** [Proposed | Accepted | Deprecated | Superseded]
**Date:** YYYY-MM-DD
**Decision Makers:** [Names]

## Context
[Context description]

## Decision
[Decision description]

## Consequences
[Consequences description]

## Alternatives Considered
[Alternatives]
```

**Example Usage:**
```python
# Extract ADRs
result = extract_adrs("docs/architecture/system-design.md")

if result["success"]:
    print(f"Extracted {result['outputs']['adrs_extracted']} ADRs")
    for adr in result["outputs"]["adr_summary"]:
        print(f"  {adr['id']}: {adr['title']} ({adr['status']})")
```

---

### validate_patterns

Validate architecture patterns against best practices.

**Location:** `.claude/skills/bmad-commands/scripts/validate_patterns.py`

#### `validate_patterns(architecture_path, pattern_catalog)`

**Description:** Validate architecture patterns and identify anti-patterns.

**Parameters:**

| Parameter | Type | Default | Required | Description | Validation |
|-----------|------|---------|----------|-------------|------------|
| `architecture_path` | `str` | - | Yes | Path to architecture document | Must be existing file |
| `pattern_catalog` | `str` | `"standard"` | No | Pattern catalog to use | One of: `standard`, `microservices`, `event-driven`, `serverless`, `monolithic` |

**Returns:** `dict` - Standard BMAD command response

**Return Structure:**
```python
{
    "success": bool,
    "outputs": {
        "patterns_found": List[{
            "name": str,
            "category": str,
            "confidence": float,  # 0.0-1.0
            "description": str
        }],
        "anti_patterns": List[{
            "name": str,
            "severity": str,      # low, medium, high, critical
            "description": str,
            "recommendation": str
        }],
        "validation_score": int,  # 0-100
        "recommendations": List[str]
    },
    "telemetry": {
        "command": "validate_patterns",
        "patterns_found": int,
        "anti_patterns_found": int,
        "duration_ms": int,
        "timestamp": str
    },
    "errors": List[str]
}
```

**Pattern Catalogs:**

| Catalog | Description | Patterns |
|---------|-------------|----------|
| `standard` | General software patterns | MVC, Repository, Factory, Strategy, Observer |
| `microservices` | Microservice patterns | API Gateway, Service Discovery, Circuit Breaker |
| `event-driven` | Event-driven patterns | Event Sourcing, CQRS, Saga |
| `serverless` | Serverless patterns | Function Composition, Event-Driven Functions |
| `monolithic` | Monolithic patterns | Layered Architecture, Modular Monolith |

**Example Usage:**
```python
# Validate microservice patterns
result = validate_patterns(
    architecture_path="docs/architecture.md",
    pattern_catalog="microservices"
)

if result["success"]:
    score = result["outputs"]["validation_score"]
    print(f"Validation Score: {score}/100")

    # Check for anti-patterns
    anti_patterns = result["outputs"]["anti_patterns"]
    critical = [ap for ap in anti_patterns if ap["severity"] == "critical"]
    if critical:
        print(f"⚠️  Critical anti-patterns: {len(critical)}")
```

---

### validate_metrics

Validate architecture quality metrics.

**Location:** `.claude/skills/bmad-commands/scripts/validate_metrics.py`

#### `validate_metrics(architecture_path, metrics_config)`

**Description:** Validate architecture against quality metrics and thresholds.

**Parameters:**

| Parameter | Type | Default | Required | Description | Validation |
|-----------|------|---------|----------|-------------|------------|
| `architecture_path` | `str` | - | Yes | Path to architecture document | Must be existing file |
| `metrics_config` | `str` | `"default"` | No | Metrics configuration | One of: `default`, `strict`, `relaxed`, or path to custom YAML config |

**Returns:** `dict` - Standard BMAD command response

**Return Structure:**
```python
{
    "success": bool,
    "outputs": {
        "metrics": {
            "modularity": int,        # 0-100
            "maintainability": int,   # 0-100
            "scalability": int,       # 0-100
            "security": int,          # 0-100
            "performance": int,       # 0-100
            "testability": int,       # 0-100
            "overall": int            # 0-100
        },
        "thresholds": {
            "modularity": int,
            "maintainability": int,
            # ... (same keys as metrics)
        },
        "violations": List[{
            "metric": str,
            "current_value": int,
            "threshold": int,
            "severity": str,
            "recommendation": str
        }],
        "passed": bool  # True if all metrics meet thresholds
    },
    "telemetry": {
        "command": "validate_metrics",
        "overall_score": int,
        "violations_count": int,
        "duration_ms": int,
        "timestamp": str
    },
    "errors": List[str]
}
```

**Metrics Configuration:**

| Config | Thresholds | Use Case |
|--------|-----------|----------|
| `default` | Balanced (60-70) | General purpose |
| `strict` | High (80-90) | Critical systems, high-quality requirements |
| `relaxed` | Low (40-50) | Prototypes, MVPs, legacy systems |

**Example Usage:**
```python
# Validate with default thresholds
result = validate_metrics("docs/architecture.md")

# Validate with strict thresholds
result = validate_metrics("docs/architecture.md", metrics_config="strict")

# Check results
if result["success"]:
    metrics = result["outputs"]["metrics"]
    print(f"Overall Score: {metrics['overall']}/100")

    if not result["outputs"]["passed"]:
        print("⚠️  Metric violations:")
        for violation in result["outputs"]["violations"]:
            print(f"  - {violation['metric']}: {violation['current_value']} (threshold: {violation['threshold']})")
```

---

## Command Parsing

### parse_command

Parse BMAD commands with type safety and validation.

**Location:** `.claude/skills/bmad-commands/scripts/parse_command.py`

All command parsers follow the same pattern and return structured dictionaries with validated parameters.

#### Command Parser Functions

Each command has a dedicated parser function:

1. **`parse_analyze_architecture(args)`**
2. **`parse_design_architecture(args)`**
3. **`parse_review_architecture(args)`**
4. **`parse_validate_story(args)`**
5. **`parse_implement(args)`**
6. **`parse_create_task_spec(args)`**
7. **`parse_review_code(args)`**

**Common Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `args` | `List[str]` | Command-line arguments (excluding command name) |

**Returns:** `Dict[str, Any]` - Parsed command parameters

**Common Return Structure:**
```python
{
    "command": str,        # Command name
    "skill": str,          # Skill to invoke
    "subagent": str,       # Subagent name (if applicable)
    # ... command-specific parameters
}
```

**Example Usage:**
```python
# Parse analyze-architecture command
args = ["--depth", "quick", "--output", "json"]
parsed = parse_analyze_architecture(args)
# Returns: {
#   "command": "analyze-architecture",
#   "codebase_path": ".",
#   "depth": "quick",
#   "output_format": "json",
#   ...
# }

# Parse with help flag
args = ["--help"]
try:
    parsed = parse_design_architecture(args)
except SystemExit:
    # argparse printed help and called sys.exit()
    pass
```

---

## Error Handling

### ErrorHandler

Main error handler for BMAD operations.

**Location:** `.claude/skills/bmad-commands/scripts/error-handler.py`

#### `__init__(log_file)`

**Description:** Initialize error handler with optional log file.

**Parameters:**

| Parameter | Type | Default | Required | Description | Validation |
|-----------|------|---------|----------|-------------|------------|
| `log_file` | `Optional[str]` | `None` | No | Path to error log file | Must be writable file path if provided |

**Example Usage:**
```python
# No logging
handler = ErrorHandler()

# With log file
handler = ErrorHandler(log_file=".claude/logs/errors.log")
```

---

#### `create_error(template_name, context, additional_remediation)`

**Description:** Create error from predefined template.

**Parameters:**

| Parameter | Type | Default | Required | Description | Validation |
|-----------|------|---------|----------|-------------|------------|
| `template_name` | `str` | - | Yes | Error template name | Must be valid template name from `ERROR_TEMPLATES` |
| `context` | `Optional[Dict]` | `None` | No | Context information for error | Dictionary with error-specific context |
| `additional_remediation` | `Optional[List[str]]` | `None` | No | Additional remediation steps | List of strings |

**Returns:** `BMADError` - Structured error object

**Available Templates:**
- `missing_task_spec`
- `complexity_too_high`
- `guardrail_violation`
- `quality_gate_failed`
- `test_failure`
- `missing_dependency`
- `timeout_exceeded`
- `configuration_error`
- `permission_denied`
- `validation_error`

**Example Usage:**
```python
handler = ErrorHandler()

# Create error from template
error = handler.create_error(
    "missing_task_spec",
    context={
        "command": "*implement",
        "spec_file": ".claude/tasks/task-001-spec.md",
        "cwd": "/home/user/project"
    }
)

# With additional remediation
error = handler.create_error(
    "quality_gate_failed",
    context={
        "command": "*validate-quality-gate",
        "score": 45,
        "threshold": 60
    },
    additional_remediation=[
        "Focus on test coverage in payment module",
        "Fix code duplication in auth service"
    ]
)
```

---

#### `handle_error(error, exit_on_error)`

**Description:** Handle and display error with formatting.

**Parameters:**

| Parameter | Type | Default | Required | Description | Validation |
|-----------|------|---------|----------|-------------|------------|
| `error` | `BMADError` | - | Yes | Error object to handle | Must be `BMADError` instance |
| `exit_on_error` | `bool` | `False` | No | Exit process after handling | If `True` or severity is CRITICAL, calls `sys.exit(1)` |

**Side Effects:**
- Prints formatted error to stderr
- Logs error to file if configured
- May exit process

**Example Usage:**
```python
handler = ErrorHandler()
error = handler.create_error("test_failure", context={...})

# Handle without exiting
handler.handle_error(error, exit_on_error=False)

# Handle and exit
handler.handle_error(error, exit_on_error=True)  # Calls sys.exit(1)
```

---

### BMADError

Structured error with remediation guidance.

#### `__init__(category, severity, message, context, remediation_steps, documentation_links, related_errors)`

**Description:** Create custom structured error.

**Parameters:**

| Parameter | Type | Default | Required | Description |
|-----------|------|---------|----------|-------------|
| `category` | `ErrorCategory` | - | Yes | Error category enum |
| `severity` | `ErrorSeverity` | - | Yes | Error severity enum |
| `message` | `str` | - | Yes | Error message |
| `context` | `Optional[Dict]` | `None` | No | Context information |
| `remediation_steps` | `Optional[List[str]]` | `None` | No | Steps to fix error |
| `documentation_links` | `Optional[List[str]]` | `None` | No | Relevant documentation links |
| `related_errors` | `Optional[List[str]]` | `None` | No | Related error messages |

**Example Usage:**
```python
from scripts.error_handler import BMADError, ErrorCategory, ErrorSeverity

error = BMADError(
    category=ErrorCategory.EXECUTION,
    severity=ErrorSeverity.ERROR,
    message="Database connection failed",
    context={
        "host": "localhost",
        "port": 5432,
        "database": "myapp"
    },
    remediation_steps=[
        "Check if database server is running",
        "Verify connection credentials",
        "Check network connectivity"
    ],
    documentation_links=[
        "docs/TROUBLESHOOTING.md#database-connection"
    ]
)

# Display error
print(error.format())

# Convert to JSON for logging
json_str = error.to_json()
```

---

## UX Tools

### bmad_wizard

Interactive command wizard for BMAD Enhanced.

**Location:** `.claude/skills/bmad-commands/scripts/bmad-wizard.py`

#### `run_wizard(goal, subagent_filter)`

**Description:** Launch interactive wizard for command recommendations.

**Parameters:**

| Parameter | Type | Default | Required | Description | Validation |
|-----------|------|---------|----------|-------------|------------|
| `goal` | `Optional[str]` | `None` | No | User goal or task description | Free-form text, max 500 chars |
| `subagent_filter` | `Optional[str]` | `None` | No | Filter by subagent | One of: `alex`, `james`, `quinn`, `winston`, `orchestrator` |

**Returns:** `dict` - Wizard result with recommended commands

**Return Structure:**
```python
{
    "success": bool,
    "recommendations": List[{
        "command": str,
        "subagent": str,
        "confidence": float,  # 0.0-1.0
        "description": str,
        "example": str
    }],
    "goal_category": str,
    "interactive_mode": bool
}
```

**Example Usage:**
```python
# Interactive mode (no goal specified)
result = run_wizard()

# Goal-based recommendations
result = run_wizard(goal="I need to implement a new feature")

# Filter by subagent
result = run_wizard(goal="Review code quality", subagent_filter="quinn")
```

**Goal Categories:**
1. Implementation (Feature Development)
2. Planning (Requirements Analysis)
3. Quality (Code Review & Testing)
4. Architecture (System Design)
5. Bug Fixing
6. Documentation
7. Workflow Orchestration
8. General Questions

---

### progress_visualizer

Real-time progress visualization for workflows.

**Location:** `.claude/skills/bmad-commands/scripts/progress-visualizer.py`

#### `create_tracker(workflow_name, total_steps, style)`

**Description:** Create progress tracker for workflow.

**Parameters:**

| Parameter | Type | Default | Required | Description | Validation |
|-----------|------|---------|----------|-------------|------------|
| `workflow_name` | `str` | - | Yes | Name of workflow | Max 50 chars |
| `total_steps` | `int` | `7` | No | Total number of steps | Must be 1-20 |
| `style` | `str` | `"bar"` | No | Visualization style | One of: `bar`, `spinner`, `dots`, `minimal` |

**Returns:** `ProgressTracker` - Progress tracker instance

**Visualization Styles:**

| Style | Description | Example |
|-------|-------------|---------|
| `bar` | Horizontal progress bar | `[████████░░] 80% (4/5 steps)` |
| `spinner` | Animated spinner | `⠋ Step 3/5: Building...` |
| `dots` | Dot indicator | `●●●○○ (3/5)` |
| `minimal` | Text only | `Step 3 of 5` |

**Example Usage:**
```python
from scripts.progress_visualizer import create_tracker

# Create tracker
tracker = create_tracker(
    workflow_name="Feature Implementation",
    total_steps=5,
    style="bar"
)

# Update progress
tracker.start_step(1, "Analyzing requirements")
# ... do work ...
tracker.complete_step(1)

tracker.start_step(2, "Writing code")
# ... do work ...
tracker.complete_step(2)

# Get summary
summary = tracker.get_summary()
print(f"Completed in {summary['duration_sec']}s")
```

---

## Best Practices

### Parameter Validation

1. **Always validate input parameters** before processing
2. **Use type hints** for all function parameters
3. **Document validation rules** in docstrings
4. **Return structured errors** for invalid inputs
5. **Provide helpful error messages** with remediation steps

### Default Values

1. **Use sensible defaults** for optional parameters
2. **Document default behavior** clearly
3. **Consider different use cases** when choosing defaults
4. **Make defaults configurable** via config file when appropriate

### Return Values

1. **Use consistent return structures** across all functions
2. **Always include telemetry data** for monitoring
3. **Return actionable error information** on failure
4. **Document all possible return values** and their meanings

### Documentation

1. **Document all parameters** with type, default, and description
2. **Include usage examples** for each function
3. **Explain validation rules** and constraints
4. **Link to related documentation** for context

---

## Related Documentation

- [ERROR-CODES.md](/home/adolfo/Documents/BMAD%20Enhanced/docs/ERROR-CODES.md) - Complete error codes reference
- [V2-ARCHITECTURE.md](/home/adolfo/Documents/BMAD%20Enhanced/docs/V2-ARCHITECTURE.md) - System architecture
- [BEST-PRACTICES.md](/home/adolfo/Documents/BMAD%20Enhanced/docs/BEST-PRACTICES.md) - Development best practices
- [FRAMEWORK-SUPPORT-MATRIX.md](/home/adolfo/Documents/BMAD%20Enhanced/docs/FRAMEWORK-SUPPORT-MATRIX.md) - Test framework support

---

**Maintained by:** BMAD Enhanced Development Team
**Last Review:** 2025-11-05
