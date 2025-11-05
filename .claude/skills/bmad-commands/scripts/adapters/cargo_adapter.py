"""Cargo Test Framework Adapter (Rust)"""

import json
import subprocess
from pathlib import Path

from .base import TestFrameworkAdapter, TestResult, TestFailure


class CargoAdapter(TestFrameworkAdapter):
    """Adapter for Cargo test framework (Rust)"""

    def detect(self, path: Path) -> bool:
        """Detect if Cargo/Rust project is present"""
        return (path / "Cargo.toml").exists()

    def run_tests(self, path: Path, timeout: int, with_coverage: bool = False) -> TestResult:
        """Execute Cargo tests"""
        start_time = __import__('time').time()

        try:
            # Build command
            cmd = ["cargo", "test", "--", "--format", "json", "-Z", "unstable-options"]

            # Execute tests
            result = subprocess.run(
                cmd,
                cwd=path,
                capture_output=True,
                timeout=timeout,
                text=True
            )

            # Parse result
            test_result = self.parse_output(result.stdout, result.stderr, result.returncode)

            # Add duration
            test_result.duration_ms = int((__import__('time').time() - start_time) * 1000)
            test_result.framework = "cargo"

            return test_result

        except subprocess.TimeoutExpired:
            return TestResult.timeout_error("cargo")
        except Exception as e:
            return TestResult.execution_error(str(e), "cargo")

    def parse_output(self, stdout: str, stderr: str, returncode: int) -> TestResult:
        """Parse Cargo test JSON output"""
        total = passed = failed = 0
        failures = []

        # Cargo JSON output is line-delimited JSON
        for line in stdout.split("\n"):
            if not line.strip():
                continue

            try:
                data = json.loads(line)

                # Look for test events
                if data.get("type") == "test":
                    event = data.get("event")

                    if event == "started":
                        total += 1
                    elif event == "ok":
                        passed += 1
                    elif event == "failed":
                        failed += 1

                        # Extract failure details
                        test_name = data.get("name", "")
                        failures.append(TestFailure(
                            test_name=test_name,
                            error_message="Test failed (see output for details)"
                        ))

            except json.JSONDecodeError:
                continue

        # Fallback: parse plain text if JSON parsing failed
        if total == 0:
            for line in stdout.split("\n"):
                if "test result:" in line:
                    # Parse: "test result: ok. 5 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out"
                    parts = line.split(".")
                    if len(parts) >= 2:
                        stats = parts[1]
                        for stat in stats.split(";"):
                            if "passed" in stat:
                                try:
                                    passed = int(stat.split()[0])
                                except:
                                    pass
                            elif "failed" in stat:
                                try:
                                    failed = int(stat.split()[0])
                                except:
                                    pass

            total = passed + failed

        return TestResult(
            success=True,
            passed=failed == 0,
            total_tests=total,
            passed_tests=passed,
            failed_tests=failed,
            summary=f"Cargo: {passed}/{total} tests passed",
            failures=failures,
            framework="cargo"
        )
