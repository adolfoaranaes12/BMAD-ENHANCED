# Framework Extension Guide

## How to Add Support for Your Test Framework

BMAD Enhanced uses a **Framework Adapter Pattern** that allows you to add support for any test framework without modifying core code. This guide shows you how to create custom framework adapters.

---

## Quick Start

### Step 1: Create Your Adapter

Create a Python file in `.claude/custom_adapters/`:

```python
# .claude/custom_adapters/my_framework_adapter.py

from pathlib import Path
from bmad_commands.adapters.base import TestFrameworkAdapter, TestResult, TestFailure
import subprocess

class MyFrameworkAdapter(TestFrameworkAdapter):
    """Adapter for MyFramework test runner"""

    def detect(self, path: Path) -> bool:
        """Auto-detect if your framework is present"""
        # Check for config files, dependencies, etc.
        return (path / "my-framework.config.json").exists()

    def run_tests(self, path: Path, timeout: int, with_coverage: bool = False) -> TestResult:
        """Execute tests using your framework"""
        start_time = __import__('time').time()

        try:
            # Run your test command
            result = subprocess.run(
                ["my-test-runner", "--json"],  # Your test command
                cwd=path,
                capture_output=True,
                timeout=timeout,
                text=True
            )

            # Parse the output
            test_result = self.parse_output(result.stdout, result.stderr, result.returncode)

            # Add metadata
            test_result.duration_ms = int((__import__('time').time() - start_time) * 1000)
            test_result.framework = "my_framework"

            return test_result

        except subprocess.TimeoutExpired:
            return TestResult.timeout_error("my_framework")
        except Exception as e:
            return TestResult.execution_error(str(e), "my_framework")

    def parse_output(self, stdout: str, stderr: str, returncode: int) -> TestResult:
        """Parse your framework's output into TestResult format"""
        # Parse your framework's output format
        # This example assumes JSON output
        import json

        try:
            data = json.loads(stdout)

            return TestResult(
                success=True,
                passed=data.get("all_passed", False),
                total_tests=data.get("total", 0),
                passed_tests=data.get("passed", 0),
                failed_tests=data.get("failed", 0),
                skipped_tests=data.get("skipped", 0),
                coverage_percent=data.get("coverage", 0.0),
                summary=f"MyFramework: {data.get('passed', 0)}/{data.get('total', 0)} tests passed",
                framework="my_framework"
            )

        except json.JSONDecodeError:
            # Fallback for non-JSON output
            return TestResult(
                success=True,
                passed=returncode == 0,
                summary=stdout[:500],
                framework="my_framework"
            )
```

### Step 2: Register Your Adapter

Add it to `.claude/config.yaml`:

```yaml
testing:
  default_framework: "auto"  # Auto-detect by default

  frameworks:
    # Your custom framework
    my_framework:
      adapter: ".claude.custom_adapters.my_framework_adapter.MyFrameworkAdapter"
      command: ["my-test-runner", "--json"]
      auto_detect:
        - "my-framework.config.json"
```

### Step 3: Use It

```bash
# Auto-detect (if you implemented detect())
python .claude/skills/bmad-commands/scripts/run_tests.py --path . --framework auto

# Explicit
python .claude/skills/bmad-commands/scripts/run_tests.py --path . --framework my_framework

# With coverage
python .claude/skills/bmad-commands/scripts/run_tests.py --path . --framework my_framework --coverage
```

---

## TestResult Schema

Your adapter must return a `TestResult` object with this schema:

```python
from adapters.base import TestResult, TestFailure

TestResult(
    # Required
    success: bool,        # Command executed successfully (not test pass/fail)
    passed: bool,         # All tests passed

    # Test counts
    total_tests: int,
    passed_tests: int,
    failed_tests: int,
    skipped_tests: int,

    # Optional
    coverage_percent: float,    # 0.0-100.0
    duration_ms: int,
    summary: str,               # Human-readable summary
    framework: str,             # Framework name

    # Failures (optional but recommended)
    failures: List[TestFailure] = [
        TestFailure(
            test_name="test_something",
            error_message="Expected 5, got 3",
            stack_trace="...",      # Optional
            file_path="test.py",    # Optional
            line_number=42          # Optional
        )
    ]
)
```

---

## Complete Examples

### Example 1: Mocha (JavaScript)

```python
# .claude/custom_adapters/mocha_adapter.py

from pathlib import Path
from bmad_commands.adapters.base import TestFrameworkAdapter, TestResult
import subprocess
import json

class MochaAdapter(TestFrameworkAdapter):
    """Adapter for Mocha test framework"""

    def detect(self, path: Path) -> bool:
        package_json = path / "package.json"
        if package_json.exists():
            data = json.loads(package_json.read_text())
            deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
            return "mocha" in deps
        return False

    def run_tests(self, path: Path, timeout: int, with_coverage: bool = False) -> TestResult:
        start_time = __import__('time').time()

        try:
            cmd = ["npm", "run", "test", "--", "--reporter", "json"]
            result = subprocess.run(cmd, cwd=path, capture_output=True, timeout=timeout, text=True)

            test_result = self.parse_output(result.stdout, result.stderr, result.returncode)
            test_result.duration_ms = int((__import__('time').time() - start_time) * 1000)
            test_result.framework = "mocha"

            return test_result

        except subprocess.TimeoutExpired:
            return TestResult.timeout_error("mocha")
        except Exception as e:
            return TestResult.execution_error(str(e), "mocha")

    def parse_output(self, stdout: str, stderr: str, returncode: int) -> TestResult:
        try:
            data = json.loads(stdout)
            stats = data.get("stats", {})

            return TestResult(
                success=True,
                passed=stats.get("failures", 0) == 0,
                total_tests=stats.get("tests", 0),
                passed_tests=stats.get("passes", 0),
                failed_tests=stats.get("failures", 0),
                skipped_tests=stats.get("pending", 0),
                summary=f"Mocha: {stats.get('passes', 0)}/{stats.get('tests', 0)} tests passed"
            )
        except:
            return TestResult(success=True, passed=returncode == 0, summary=stdout[:500])
```

**Register in .claude/config.yaml:**

```yaml
testing:
  frameworks:
    mocha:
      adapter: ".claude.custom_adapters.mocha_adapter.MochaAdapter"
      command: ["npm", "run", "test", "--", "--reporter", "json"]
      auto_detect:
        - "package.json"
```

---

### Example 2: RSpec (Ruby)

```python
# .claude/custom_adapters/rspec_adapter.py

from pathlib import Path
from bmad_commands.adapters.base import TestFrameworkAdapter, TestResult
import subprocess
import json

class RSpecAdapter(TestFrameworkAdapter):
    """Adapter for RSpec test framework"""

    def detect(self, path: Path) -> bool:
        return (path / "spec").exists() and (path / ".rspec").exists()

    def run_tests(self, path: Path, timeout: int, with_coverage: bool = False) -> TestResult:
        start_time = __import__('time').time()

        try:
            cmd = ["rspec", "--format", "json"]
            result = subprocess.run(cmd, cwd=path, capture_output=True, timeout=timeout, text=True)

            test_result = self.parse_output(result.stdout, result.stderr, result.returncode)
            test_result.duration_ms = int((__import__('time').time() - start_time) * 1000)
            test_result.framework = "rspec"

            return test_result

        except subprocess.TimeoutExpired:
            return TestResult.timeout_error("rspec")
        except Exception as e:
            return TestResult.execution_error(str(e), "rspec")

    def parse_output(self, stdout: str, stderr: str, returncode: int) -> TestResult:
        try:
            data = json.loads(stdout)
            summary = data.get("summary", {})

            return TestResult(
                success=True,
                passed=summary.get("failure_count", 0) == 0,
                total_tests=summary.get("example_count", 0),
                passed_tests=summary.get("example_count", 0) - summary.get("failure_count", 0),
                failed_tests=summary.get("failure_count", 0),
                skipped_tests=summary.get("pending_count", 0)
            )
        except:
            return TestResult(success=True, passed=returncode == 0, summary=stdout[:500])
```

---

### Example 3: PHPUnit (PHP)

```python
# .claude/custom_adapters/phpunit_adapter.py

from pathlib import Path
from bmad_commands.adapters.base import TestFrameworkAdapter, TestResult
import subprocess
import json

class PHPUnitAdapter(TestFrameworkAdapter):
    """Adapter for PHPUnit test framework"""

    def detect(self, path: Path) -> bool:
        return (path / "phpunit.xml").exists() or (path / "phpunit.xml.dist").exists()

    def run_tests(self, path: Path, timeout: int, with_coverage: bool = False) -> TestResult:
        start_time = __import__('time').time()

        try:
            cmd = ["phpunit", "--log-json", ".phpunit-result.json"]
            result = subprocess.run(cmd, cwd=path, capture_output=True, timeout=timeout, text=True)

            test_result = self.parse_output(result.stdout, result.stderr, result.returncode)
            test_result.duration_ms = int((__import__('time').time() - start_time) * 1000)
            test_result.framework = "phpunit"

            return test_result

        except subprocess.TimeoutExpired:
            return TestResult.timeout_error("phpunit")
        except Exception as e:
            return TestResult.execution_error(str(e), "phpunit")

    def parse_output(self, stdout: str, stderr: str, returncode: int) -> TestResult:
        # PHPUnit JSON log is line-delimited
        total = passed = failed = skipped = 0

        try:
            for line in stdout.split("\n"):
                if not line.strip():
                    continue
                data = json.loads(line)

                if data.get("event") == "test":
                    status = data.get("status")
                    total += 1

                    if status == "pass":
                        passed += 1
                    elif status in ["fail", "error"]:
                        failed += 1
                    elif status == "skipped":
                        skipped += 1

            return TestResult(
                success=True,
                passed=failed == 0,
                total_tests=total,
                passed_tests=passed,
                failed_tests=failed,
                skipped_tests=skipped
            )
        except:
            return TestResult(success=True, passed=returncode == 0, summary=stdout[:500])
```

---

## Testing Your Adapter

### 1. Test Auto-Detection

```bash
cd your-project
python -c "
from pathlib import Path
from .claude.custom_adapters.my_framework_adapter import MyFrameworkAdapter

adapter = MyFrameworkAdapter({})
detected = adapter.detect(Path('.'))
print(f'Detected: {detected}')
"
```

### 2. Test Execution

```bash
python .claude/skills/bmad-commands/scripts/run_tests.py \
  --path . \
  --framework my_framework \
  --output json
```

### 3. Verify Output Format

The output should follow BMAD format:

```json
{
  "success": true,
  "outputs": {
    "passed": true,
    "summary": "10/10 tests passed",
    "total_tests": 10,
    "passed_tests": 10,
    "failed_tests": 0,
    "skipped_tests": 0,
    "coverage_percent": 85.5,
    "duration_ms": 2500
  },
  "telemetry": {...},
  "errors": []
}
```

---

## Tips & Best Practices

### 1. Robust Detection

```python
def detect(self, path: Path) -> bool:
    """Use multiple signals for detection"""
    # Check config files
    if (path / "framework.config").exists():
        return True

    # Check dependencies
    deps_file = path / "package.json"  # or requirements.txt, etc.
    if deps_file.exists():
        try:
            content = deps_file.read_text()
            if "my-framework" in content:
                return True
        except:
            pass

    # Check for test files
    if list(path.glob("test/**/*.spec.js")):
        return True

    return False
```

### 2. Error Handling

```python
def run_tests(self, path: Path, timeout: int, with_coverage: bool = False) -> TestResult:
    try:
        result = subprocess.run(...)
        return self.parse_output(...)
    except subprocess.TimeoutExpired:
        return TestResult.timeout_error(self.name)
    except FileNotFoundError:
        return TestResult.execution_error("Test runner not found", self.name)
    except Exception as e:
        return TestResult.execution_error(str(e), self.name)
```

### 3. Flexible Parsing

```python
def parse_output(self, stdout: str, stderr: str, returncode: int) -> TestResult:
    # Try JSON first
    try:
        data = json.loads(stdout)
        return self._parse_json(data)
    except json.JSONDecodeError:
        pass

    # Try XML
    try:
        tree = ET.fromstring(stdout)
        return self._parse_xml(tree)
    except:
        pass

    # Fallback: text parsing
    return self._parse_text(stdout, returncode)
```

### 4. Coverage Support

```python
def run_tests(self, path: Path, timeout: int, with_coverage: bool = False) -> TestResult:
    # Adjust command based on coverage flag
    if with_coverage:
        cmd = self.coverage_command or self.command + ["--coverage"]
    else:
        cmd = self.command

    # ... execute and parse ...

    # Extract coverage if available
    if with_coverage:
        coverage = self.get_coverage(path)
        if coverage:
            test_result.coverage_percent = coverage

    return test_result

def get_coverage(self, path: Path) -> float:
    """Extract coverage from framework-specific file"""
    coverage_file = path / "coverage" / "coverage.json"
    if coverage_file.exists():
        data = json.loads(coverage_file.read_text())
        return data.get("total", {}).get("percent", 0.0)
    return 0.0
```

---

## Troubleshooting

### Adapter Not Loading

**Error:** `Warning: Failed to load adapter my_framework: ...`

**Solutions:**
1. Check Python import path in config
2. Verify adapter class name matches config
3. Ensure `__init__` method accepts `config: dict`
4. Check for syntax errors in adapter file

### Auto-Detection Not Working

**Solutions:**
1. Add debug prints to `detect()` method
2. Verify detection logic matches your project structure
3. Test detection independently (see Testing section)

### Parsing Failures

**Solutions:**
1. Print stdout/stderr to see actual format
2. Add fallback parsing for non-standard output
3. Use regex for text parsing if JSON unavailable

---

## Sharing Your Adapter

Consider contributing your adapter to BMAD Enhanced!

1. Test thoroughly on multiple projects
2. Add documentation
3. Submit as pull request to `.claude/skills/bmad-commands/scripts/adapters/`
4. Update this guide with your example

---

## Supported Frameworks (Built-in)

- ✅ **Jest** (JavaScript/TypeScript)
- ✅ **Pytest** (Python)

## Example Adapters (Reference)

- ✅ **JUnit** (Java/Kotlin)
- ✅ **Google Test** (C++)
- ✅ **Cargo** (Rust)
- ✅ **Go Test** (Go)

## Community Adapters

Add yours here!

---

**Need help?** Check the existing adapters in `.claude/skills/bmad-commands/scripts/adapters/` for more examples.
