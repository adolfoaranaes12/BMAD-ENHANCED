# Framework Support Matrix

## Overview

BMAD Enhanced v2.1 introduces **framework-agnostic testing** through a pluggable adapter pattern. This document provides a comprehensive matrix of supported test frameworks, their capabilities, and setup instructions.

---

## Supported Frameworks

### Built-in Frameworks (Auto-detected)

| Framework | Language | Auto-Detect | Coverage | Status | Notes |
|-----------|----------|-------------|----------|--------|-------|
| **Jest** | JavaScript/TypeScript | ✅ Yes | ✅ Yes | 🟢 Built-in | Default for JS/TS projects |
| **Pytest** | Python | ✅ Yes | ✅ Yes | 🟢 Built-in | Default for Python projects |

### Example Frameworks (Reference Implementations)

| Framework | Language | Auto-Detect | Coverage | Status | Notes |
|-----------|----------|-------------|----------|--------|-------|
| **JUnit** | Java/Kotlin | ✅ Yes | ❌ No* | 🟡 Example | Maven & Gradle support |
| **Google Test** | C/C++ | ✅ Yes | ❌ No* | 🟡 Example | CMake/CTest integration |
| **Cargo** | Rust | ✅ Yes | ⚠️ Partial | 🟡 Example | Native Cargo test |
| **Go Test** | Go | ✅ Yes | ✅ Yes | 🟡 Example | Native Go tooling |

*Coverage support can be added via adapter extension

---

## Framework Details

### Jest (JavaScript/TypeScript)

**Status:** 🟢 Built-in
**File:** `.claude/skills/bmad-commands/scripts/adapters/jest_adapter.py`

**Auto-Detection:**
- `package.json` with Jest in dependencies
- `jest.config.js` or `jest.config.ts` present

**Features:**
- ✅ JSON output parsing
- ✅ Coverage extraction
- ✅ Failure details with stack traces
- ✅ File-level test results

**Usage:**
```bash
# Auto-detect
@james *test task-login-001

# Explicit
@james *test task-auth-001 --framework jest --coverage
```

**Setup:**
```json
// package.json
{
  "devDependencies": {
    "jest": "^29.0.0"
  },
  "scripts": {
    "test": "jest"
  }
}
```

---

### Pytest (Python)

**Status:** 🟢 Built-in
**File:** `.claude/skills/bmad-commands/scripts/adapters/pytest_adapter.py`

**Auto-Detection:**
- `pytest.ini`, `pyproject.toml`, or `setup.cfg` present
- `requirements.txt` contains pytest
- `tests/` directory exists

**Features:**
- ✅ JSON report parsing
- ✅ Coverage via coverage.json
- ✅ Failure details with stack traces
- ✅ Test parameterization support

**Usage:**
```bash
# Auto-detect
@james *test task-api-001

# Explicit with coverage
@james *test task-auth-001 --framework pytest --coverage
```

**Setup:**
```bash
# requirements.txt
pytest>=7.0.0
pytest-json-report>=1.5.0
pytest-cov>=4.0.0
```

```ini
# pytest.ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
```

---

### JUnit (Java/Kotlin)

**Status:** 🟡 Example
**File:** `.claude/skills/bmad-commands/scripts/adapters/junit_adapter.py`

**Auto-Detection:**
- `pom.xml` (Maven) present
- `build.gradle` or `build.gradle.kts` (Gradle) present

**Features:**
- ✅ XML report parsing (Surefire/Gradle)
- ✅ Maven & Gradle support
- ✅ Failure details
- ⚠️ Coverage requires JaCoCo

**Usage:**
```bash
# Auto-detect
@james *test task-service-001

# Explicit
@james *test task-checkout --framework junit
```

**Setup (Maven):**
```xml
<!-- pom.xml -->
<dependencies>
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter</artifactId>
        <version>5.9.0</version>
        <scope>test</scope>
    </dependency>
</dependencies>
```

**Setup (Gradle):**
```gradle
dependencies {
    testImplementation 'org.junit.jupiter:junit-jupiter:5.9.0'
}

test {
    useJUnitPlatform()
}
```

---

### Google Test (C/C++)

**Status:** 🟡 Example
**File:** `.claude/skills/bmad-commands/scripts/adapters/gtest_adapter.py`

**Auto-Detection:**
- `CMakeLists.txt` with GoogleTest references
- Build directory with test executables

**Features:**
- ✅ CTest integration
- ✅ GTest output parsing
- ✅ Failure details
- ⚠️ Coverage requires gcov/lcov

**Usage:**
```bash
# Auto-detect
@james *test task-algorithm-001

# Explicit
@james *test task-sorting --framework gtest
```

**Setup (CMake):**
```cmake
# CMakeLists.txt
include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/release-1.12.1.zip
)
FetchContent_MakeAvailable(googletest)

enable_testing()

add_executable(my_test test/my_test.cpp)
target_link_libraries(my_test GTest::gtest_main)

include(GoogleTest)
gtest_discover_tests(my_test)
```

---

### Cargo (Rust)

**Status:** 🟡 Example
**File:** `.claude/skills/bmad-commands/scripts/adapters/cargo_adapter.py`

**Auto-Detection:**
- `Cargo.toml` present

**Features:**
- ✅ JSON output parsing
- ✅ Native Cargo test
- ✅ Failure details
- ⚠️ Coverage via tarpaulin (optional)

**Usage:**
```bash
# Auto-detect
@james *test task-http-server

# With coverage (requires tarpaulin)
@james *test task-api --framework cargo --coverage
```

**Setup:**
```toml
# Cargo.toml
[package]
name = "my_project"
version = "0.1.0"

[dev-dependencies]
# Standard library test framework (built-in)
```

**Coverage Setup (Optional):**
```bash
cargo install cargo-tarpaulin
```

---

### Go Test

**Status:** 🟡 Example
**File:** `.claude/skills/bmad-commands/scripts/adapters/go_test_adapter.py`

**Auto-Detection:**
- `go.mod` present

**Features:**
- ✅ JSON output parsing
- ✅ Native Go test
- ✅ Coverage extraction
- ✅ Benchmark support

**Usage:**
```bash
# Auto-detect
@james *test task-grpc-service

# With coverage
@james *test task-api --framework go --coverage
```

**Setup:**
```go
// myproject_test.go
package myproject

import "testing"

func TestSomething(t *testing.T) {
    // Test code
}
```

```bash
# go.mod exists
go test ./...
```

---

## Adding Custom Frameworks

### Quick Start

1. **Create Adapter** (`.claude/custom_adapters/my_framework_adapter.py`)
2. **Register in Config** (`.claude/config.yaml`)
3. **Use It** (`@james *test --framework my_framework`)

### Example: Mocha (JavaScript)

```python
# .claude/custom_adapters/mocha_adapter.py
from bmad_commands.adapters.base import TestFrameworkAdapter, TestResult
import subprocess
import json

class MochaAdapter(TestFrameworkAdapter):
    def detect(self, path):
        package_json = path / "package.json"
        if package_json.exists():
            data = json.loads(package_json.read_text())
            deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
            return "mocha" in deps
        return False

    def run_tests(self, path, timeout, with_coverage=False):
        result = subprocess.run(
            ["npm", "run", "test", "--", "--reporter", "json"],
            cwd=path, capture_output=True, timeout=timeout, text=True
        )
        return self.parse_output(result.stdout, result.stderr, result.returncode)

    def parse_output(self, stdout, stderr, returncode):
        data = json.loads(stdout)
        stats = data.get("stats", {})
        return TestResult(
            success=True,
            passed=stats.get("failures", 0) == 0,
            total_tests=stats.get("tests", 0),
            passed_tests=stats.get("passes", 0),
            failed_tests=stats.get("failures", 0),
            framework="mocha"
        )
```

```yaml
# .claude/config.yaml
testing:
  frameworks:
    mocha:
      adapter: ".claude.custom_adapters.mocha_adapter.MochaAdapter"
      command: ["npm", "run", "test", "--", "--reporter", "json"]
```

**See:** [Framework Extension Guide](.claude/skills/bmad-commands/FRAMEWORK-EXTENSION-GUIDE.md) for more examples (RSpec, PHPUnit, etc.)

---

## Community Frameworks

Want to add support for your framework? See the [Extension Guide](.claude/skills/bmad-commands/FRAMEWORK-EXTENSION-GUIDE.md)!

### Requested Frameworks

| Framework | Language | Interest | Status |
|-----------|----------|----------|--------|
| **Mocha** | JavaScript | High | 📝 Example in guide |
| **RSpec** | Ruby | High | 📝 Example in guide |
| **PHPUnit** | PHP | Medium | 📝 Example in guide |
| **Vitest** | JavaScript/TypeScript | High | 🔜 Planned |
| **TestNG** | Java | Medium | 🔜 Planned |
| **Catch2** | C++ | Medium | 🔜 Planned |
| **Your Framework** | Any | - | [Contribute!](.claude/skills/bmad-commands/FRAMEWORK-EXTENSION-GUIDE.md) |

---

## Configuration Reference

### Full Config Example

```yaml
# .claude/config.yaml

testing:
  # Default framework (auto-detect if not specified)
  default_framework: "auto"

  # Framework Registry
  frameworks:
    # Built-in frameworks (Jest, Pytest) auto-registered

    # Custom frameworks
    mocha:
      adapter: ".claude.custom_adapters.mocha_adapter.MochaAdapter"
      command: ["npm", "run", "test", "--", "--reporter", "json"]
      coverage_command: ["npm", "run", "test", "--", "--coverage"]
      auto_detect:
        - "package.json"

    junit:
      adapter: "adapters.junit_adapter.JUnitAdapter"
      command: ["mvn", "test"]
      auto_detect:
        - "pom.xml"
        - "build.gradle"
```

---

## Usage Examples

### Auto-Detection (Recommended)

```bash
# Detects framework from project structure
@james *test task-auth-001
@james *implement task-api-001
```

### Explicit Framework

```bash
# Specify framework explicitly
@james *test task-auth-001 --framework pytest
@james *test task-service-001 --framework junit
@james *implement task-algo-001 --framework gtest
```

### With Coverage

```bash
# Auto-detect with coverage
@james *test task-api-001 --coverage

# Explicit with coverage
@james *test task-auth-001 --framework pytest --coverage
```

### List Available Frameworks

```bash
python .claude/skills/bmad-commands/scripts/run_tests.py --list-frameworks
```

---

## Troubleshooting

### Framework Not Auto-Detected

**Problem:** `@james *test` reports "no_framework_detected"

**Solutions:**
1. Check if framework config files exist (package.json, pytest.ini, etc.)
2. Verify dependencies are installed
3. Use explicit framework: `@james *test task-001 --framework jest`
4. Check detection logic in adapter's `detect()` method

### Tests Not Running

**Problem:** Tests don't execute

**Solutions:**
1. Verify test framework is installed
2. Check command in adapter config
3. Run manually first: `npm test`, `pytest`, etc.
4. Review error output for missing dependencies

### Coverage Not Working

**Problem:** Coverage always shows 0%

**Solutions:**
1. Install coverage tools (coverage.py, nyc, etc.)
2. Check `coverage_command` in adapter config
3. Use `--coverage` flag explicitly
4. Verify coverage report format matches adapter parser

---

## Performance Benchmarks

| Framework | Setup Time | Test Execution | Parsing | Total Overhead |
|-----------|------------|----------------|---------|----------------|
| Jest | ~50ms | Test-dependent | ~20ms | ~70ms |
| Pytest | ~100ms | Test-dependent | ~30ms | ~130ms |
| JUnit | ~200ms | Test-dependent | ~50ms | ~250ms |
| GTest | ~150ms | Test-dependent | ~40ms | ~190ms |
| Cargo | ~300ms | Test-dependent | ~30ms | ~330ms |
| Go | ~80ms | Test-dependent | ~20ms | ~100ms |

*Overhead = Framework startup + parsing (excludes actual test execution time)*

---

## Support & Contributing

### Getting Help

- 📖 [Framework Extension Guide](.claude/skills/bmad-commands/FRAMEWORK-EXTENSION-GUIDE.md)
- 🏗️ [Adapter Architecture](.claude/skills/bmad-commands/FRAMEWORK-ADAPTER-ARCHITECTURE.md)
- 📝 [Implementation Summary](.claude/skills/bmad-commands/FRAMEWORK-AGNOSTIC-SUMMARY.md)

### Contributing

Want to add support for your framework?

1. Create adapter following [Extension Guide](.claude/skills/bmad-commands/FRAMEWORK-EXTENSION-GUIDE.md)
2. Test thoroughly on multiple projects
3. Submit pull request with adapter + documentation
4. Update this matrix with your framework

---

**Last Updated:** 2025-11-05
**Version:** v2.1 - Framework-Agnostic Release
