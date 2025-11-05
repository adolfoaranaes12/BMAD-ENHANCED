# Framework Adapter Architecture

## Overview

Make bmad-commands truly framework-agnostic by introducing a **Framework Adapter Pattern** that allows users to plug in support for any test framework, build system, or language tooling.

## Design Principles

1. **Adapter Pattern:** Each framework implements a standard interface
2. **Configuration-driven:** Frameworks registered in `.claude/config.yaml`
3. **Extensible:** Users can add new frameworks without modifying core code
4. **Backward Compatible:** Existing Jest/Pytest code continues to work
5. **Type-safe Contracts:** Standard input/output schema for all adapters

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     BMAD Commands Layer                      │
│                  (Framework-agnostic logic)                  │
└───────────────────┬─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────┐
│              Framework Registry & Resolver                   │
│          (Loads adapters from config + plugins)              │
└───────────────────┬─────────────────────────────────────────┘
                    │
        ┌───────────┴───────────┬───────────┬──────────┐
        ▼                       ▼           ▼          ▼
┌──────────────┐      ┌──────────────┐  ┌─────┐  ┌─────────┐
│ Jest Adapter │      │Pytest Adapter│  │JUnit│  │  GTest  │
│   (built-in) │      │  (built-in)  │  │     │  │(example)│
└──────────────┘      └──────────────┘  └─────┘  └─────────┘
        │                       │           │          │
        ▼                       ▼           ▼          ▼
┌──────────────────────────────────────────────────────────────┐
│                    Test Frameworks                            │
│         (npm test, pytest, mvn test, ctest, etc.)            │
└──────────────────────────────────────────────────────────────┘
```

---

## Framework Adapter Interface

Every adapter must implement this interface:

```python
class TestFrameworkAdapter:
    """Abstract base class for test framework adapters"""

    def __init__(self, config: dict):
        """Initialize adapter with framework-specific config"""
        pass

    def detect(self, path: Path) -> bool:
        """Auto-detect if this framework is present in the project"""
        pass

    def run_tests(self, path: Path, timeout: int) -> TestResult:
        """Execute tests and return structured results"""
        pass

    def parse_output(self, stdout: str, stderr: str, returncode: int) -> TestResult:
        """Parse test output into standard format"""
        pass

    def get_coverage(self, path: Path) -> Optional[float]:
        """Extract coverage percentage if available"""
        pass
```

**Standard TestResult Schema:**

```python
{
    "success": bool,              # Command executed successfully
    "outputs": {
        "passed": bool,           # All tests passed
        "summary": str,           # Human-readable summary
        "total_tests": int,       # Total test count
        "passed_tests": int,      # Passed test count
        "failed_tests": int,      # Failed test count
        "skipped_tests": int,     # Skipped test count
        "coverage_percent": float, # Coverage percentage (0-100)
        "duration_ms": int,       # Test execution time
        "failures": [             # List of failures
            {
                "test_name": str,
                "error_message": str,
                "stack_trace": str
            }
        ]
    },
    "telemetry": {
        "command": "run_tests",
        "framework": str,
        "duration_ms": int,
        "timestamp": str
    },
    "errors": [str]              # Error codes if failed
}
```

---

## Configuration System

### `.claude/config.yaml`

```yaml
# Testing Configuration
testing:
  # Default framework (auto-detected if not specified)
  default_framework: "auto"

  # Framework Registry
  frameworks:
    # Built-in frameworks
    jest:
      adapter: "bmad_commands.adapters.jest.JestAdapter"
      auto_detect:
        - "package.json"     # Has jest in dependencies
        - "jest.config.js"
      command: ["npm", "test", "--", "--json"]
      coverage_command: ["npm", "test", "--", "--coverage", "--json"]

    pytest:
      adapter: "bmad_commands.adapters.pytest.PytestAdapter"
      auto_detect:
        - "pytest.ini"
        - "setup.py"         # Has pytest in install_requires
        - "pyproject.toml"   # Has pytest in dependencies
      command: ["pytest", "--json-report"]
      coverage_command: ["pytest", "--cov", "--json-report"]

    # User-defined frameworks (examples)
    junit:
      adapter: "bmad_commands.adapters.junit.JUnitAdapter"
      auto_detect:
        - "pom.xml"
      command: ["mvn", "test"]

    gtest:
      adapter: "bmad_commands.adapters.gtest.GTestAdapter"
      auto_detect:
        - "CMakeLists.txt"   # Has GoogleTest
      command: ["ctest", "--output-on-failure"]

    cargo:
      adapter: "bmad_commands.adapters.cargo.CargoAdapter"
      auto_detect:
        - "Cargo.toml"
      command: ["cargo", "test", "--", "--format", "json"]

    go:
      adapter: "bmad_commands.adapters.go_test.GoTestAdapter"
      auto_detect:
        - "go.mod"
      command: ["go", "test", "-json", "./..."]

    # Custom user adapter
    custom:
      adapter: ".claude/custom_adapters/my_framework.MyAdapter"
      command: ["custom-test-runner", "--json"]
```

---

## Implementation Plan

### Phase 1: Refactor Existing Code

**File:** `.claude/skills/bmad-commands/scripts/run_tests.py`

```python
#!/usr/bin/env python3
"""
BMAD Command: run_tests
Execute tests with specified framework using adapter pattern
"""

import json
import sys
from pathlib import Path
from datetime import datetime

# Import framework registry
from framework_registry import FrameworkRegistry


def run_tests(path: str, framework: str = "auto", timeout_sec: int = 120):
    """Execute tests using framework adapter"""

    # Initialize registry
    registry = FrameworkRegistry()

    # Auto-detect framework if needed
    if framework == "auto":
        framework = registry.detect_framework(Path(path))
        if not framework:
            return {
                "success": False,
                "outputs": {},
                "telemetry": {...},
                "errors": ["no_framework_detected"]
            }

    # Get adapter for framework
    adapter = registry.get_adapter(framework)
    if not adapter:
        return {
            "success": False,
            "outputs": {},
            "telemetry": {...},
            "errors": [f"unsupported_framework: {framework}"]
        }

    # Execute tests using adapter
    result = adapter.run_tests(Path(path), timeout_sec)

    return result


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run tests with structured output")
    parser.add_argument("--path", required=True, help="Path to tests")
    parser.add_argument("--framework", default="auto", help="Test framework (auto-detect if not specified)")
    parser.add_argument("--timeout", type=int, default=120, help="Timeout in seconds")
    parser.add_argument("--output", default="json", choices=["json"], help="Output format")

    args = parser.parse_args()

    result = run_tests(args.path, args.framework, args.timeout)
    print(json.dumps(result, indent=2))

    sys.exit(0 if result["success"] else 1)
```

---

### Phase 2: Framework Registry

**File:** `.claude/skills/bmad-commands/scripts/framework_registry.py`

```python
"""Framework Registry - Loads and manages test framework adapters"""

import importlib
import yaml
from pathlib import Path
from typing import Optional, Dict


class FrameworkRegistry:
    """Registry for test framework adapters"""

    def __init__(self, config_path: Optional[Path] = None):
        """Initialize registry and load adapters from config"""
        if config_path is None:
            config_path = Path(".claude/config.yaml")

        self.adapters: Dict[str, any] = {}
        self.config = self._load_config(config_path)
        self._register_adapters()

    def _load_config(self, path: Path) -> dict:
        """Load configuration file"""
        if not path.exists():
            return {"testing": {"frameworks": {}}}

        with open(path) as f:
            return yaml.safe_load(f)

    def _register_adapters(self):
        """Register all adapters from config"""
        frameworks = self.config.get("testing", {}).get("frameworks", {})

        for name, config in frameworks.items():
            adapter_class = config.get("adapter")
            if adapter_class:
                try:
                    # Import adapter class
                    module_path, class_name = adapter_class.rsplit(".", 1)
                    module = importlib.import_module(module_path)
                    adapter_cls = getattr(module, class_name)

                    # Instantiate adapter
                    self.adapters[name] = adapter_cls(config)
                except Exception as e:
                    print(f"Warning: Failed to load adapter {name}: {e}", file=sys.stderr)

    def detect_framework(self, path: Path) -> Optional[str]:
        """Auto-detect test framework in project"""
        for name, adapter in self.adapters.items():
            if adapter.detect(path):
                return name
        return None

    def get_adapter(self, framework: str):
        """Get adapter for specified framework"""
        return self.adapters.get(framework)

    def list_frameworks(self) -> list:
        """List all registered frameworks"""
        return list(self.adapters.keys())
```

---

### Phase 3: Built-in Adapters

**File:** `.claude/skills/bmad-commands/scripts/adapters/jest_adapter.py`

```python
"""Jest Test Framework Adapter"""

import json
import subprocess
from pathlib import Path
from .base import TestFrameworkAdapter, TestResult


class JestAdapter(TestFrameworkAdapter):
    """Adapter for Jest test framework"""

    def detect(self, path: Path) -> bool:
        """Detect if Jest is present"""
        package_json = path / "package.json"
        if package_json.exists():
            data = json.loads(package_json.read_text())
            deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
            return "jest" in deps

        return (path / "jest.config.js").exists()

    def run_tests(self, path: Path, timeout: int) -> TestResult:
        """Run Jest tests"""
        try:
            result = subprocess.run(
                ["npm", "test", "--", "--json", "--passWithNoTests"],
                cwd=path,
                capture_output=True,
                timeout=timeout,
                text=True
            )

            return self.parse_output(result.stdout, result.stderr, result.returncode)

        except subprocess.TimeoutExpired:
            return TestResult.timeout_error()
        except Exception as e:
            return TestResult.execution_error(str(e))

    def parse_output(self, stdout: str, stderr: str, returncode: int) -> TestResult:
        """Parse Jest JSON output"""
        try:
            data = json.loads(stdout)
            return TestResult(
                success=True,
                passed=data.get("success", False),
                total_tests=data.get("numTotalTests", 0),
                passed_tests=data.get("numPassedTests", 0),
                failed_tests=data.get("numFailedTests", 0),
                coverage_percent=self._extract_coverage(data)
            )
        except json.JSONDecodeError:
            return TestResult.parse_error(stdout, stderr)
```

**Similar adapters for:** `pytest_adapter.py`, `junit_adapter.py`, `gtest_adapter.py`, `cargo_adapter.py`, `go_test_adapter.py`

---

### Phase 4: Example Adapters for Other Frameworks

**File:** `.claude/skills/bmad-commands/scripts/adapters/junit_adapter.py`

```python
"""JUnit Test Framework Adapter (Java/Kotlin)"""

import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path
from .base import TestFrameworkAdapter, TestResult


class JUnitAdapter(TestFrameworkAdapter):
    """Adapter for JUnit (Maven/Gradle)"""

    def detect(self, path: Path) -> bool:
        """Detect if JUnit is present"""
        return (path / "pom.xml").exists() or (path / "build.gradle").exists()

    def run_tests(self, path: Path, timeout: int) -> TestResult:
        """Run Maven/Gradle tests"""
        # Detect build tool
        if (path / "pom.xml").exists():
            cmd = ["mvn", "test"]
        else:
            cmd = ["./gradlew", "test"]

        try:
            result = subprocess.run(cmd, cwd=path, capture_output=True, timeout=timeout, text=True)
            return self.parse_output(result.stdout, result.stderr, result.returncode)
        except subprocess.TimeoutExpired:
            return TestResult.timeout_error()

    def parse_output(self, stdout: str, stderr: str, returncode: int) -> TestResult:
        """Parse JUnit XML reports"""
        # Find test reports
        report_dirs = [Path("target/surefire-reports"), Path("build/test-results/test")]

        total = passed = failed = 0

        for report_dir in report_dirs:
            if report_dir.exists():
                for xml_file in report_dir.glob("TEST-*.xml"):
                    tree = ET.parse(xml_file)
                    root = tree.getroot()
                    total += int(root.get("tests", 0))
                    failed += int(root.get("failures", 0))
                    passed = total - failed

        return TestResult(
            success=True,
            passed=failed == 0,
            total_tests=total,
            passed_tests=passed,
            failed_tests=failed
        )
```

---

## Usage Examples

### Auto-detection (Recommended)

```bash
# Auto-detect framework from project structure
python .claude/skills/bmad-commands/scripts/run_tests.py --path . --framework auto
```

### Explicit Framework

```bash
# Use specific framework
python .claude/skills/bmad-commands/scripts/run_tests.py --path . --framework auto
python .claude/skills/bmad-commands/scripts/run_tests.py --path . --framework junit
python .claude/skills/bmad-commands/scripts/run_tests.py --path . --framework gtest
```

### In Skills

```markdown
## Step 2: Run Tests

Execute tests using configured framework:

```bash
python .claude/skills/bmad-commands/scripts/run_tests.py \
  --path . \
  --framework auto \  # Auto-detect, or specify: jest, pytest, junit, gtest, cargo, go
  --output json
```
```

---

## Benefits

1. **True Framework Agnosticism:** Users can add ANY test framework
2. **Zero Breaking Changes:** Existing Jest/Pytest usage continues to work
3. **Extensible:** New frameworks added via config, not code changes
4. **Auto-detection:** Smart framework detection reduces configuration burden
5. **Consistent Interface:** All frameworks return same data structure
6. **Language Support:** JavaScript, Python, Java, C++, Rust, Go, and more

---

## Migration Path

**Phase 1: Backward Compatibility (v2.1)**
- Keep existing hardcoded Jest/Pytest support
- Add framework registry alongside
- Both systems work in parallel

**Phase 2: Deprecation (v2.2)**
- Mark hardcoded framework code as deprecated
- Guide users to use `--framework` parameter

**Phase 3: Removal (v3.0)**
- Remove hardcoded Jest/Pytest logic
- Full adapter-based system

---

## Custom Framework Example

Users can create custom adapters:

**File:** `.claude/custom_adapters/my_framework.py`

```python
from bmad_commands.adapters.base import TestFrameworkAdapter, TestResult

class MyAdapter(TestFrameworkAdapter):
    def detect(self, path):
        return (path / "my-test-config.yaml").exists()

    def run_tests(self, path, timeout):
        # Your custom test execution logic
        result = subprocess.run(["my-test-runner"], ...)
        return self.parse_output(...)

    def parse_output(self, stdout, stderr, returncode):
        # Your custom parsing logic
        return TestResult(...)
```

**Register in `.claude/config.yaml`:**

```yaml
testing:
  frameworks:
    my_framework:
      adapter: ".claude.custom_adapters.my_framework.MyAdapter"
      command: ["my-test-runner", "--json"]
```

---

## Next Steps

1. Implement `framework_registry.py`
2. Refactor `run_tests.py` to use registry
3. Create adapter base class (`base.py`)
4. Implement built-in adapters (Jest, Pytest)
5. Create example adapters (JUnit, GTest, Cargo, Go)
6. Update skill documentation
7. Create framework extension guide for users

---

**Status:** Design Complete - Ready for Implementation
