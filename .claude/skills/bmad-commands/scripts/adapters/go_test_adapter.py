"""Go Test Framework Adapter"""

import json
import subprocess
from pathlib import Path

from .base import TestFrameworkAdapter, TestResult, TestFailure


class GoTestAdapter(TestFrameworkAdapter):
    """Adapter for Go test framework"""

    def detect(self, path: Path) -> bool:
        """Detect if Go project is present"""
        return (path / "go.mod").exists()

    def run_tests(self, path: Path, timeout: int, with_coverage: bool = False) -> TestResult:
        """Execute Go tests"""
        start_time = __import__('time').time()

        try:
            # Build command
            cmd = ["go", "test", "-json", "./..."]
            if with_coverage:
                cmd.extend(["-cover", "-coverprofile=coverage.out"])

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
            test_result.framework = "go"

            # Extract coverage if requested
            if with_coverage:
                coverage = self.get_coverage(path)
                if coverage:
                    test_result.coverage_percent = coverage

            return test_result

        except subprocess.TimeoutExpired:
            return TestResult.timeout_error("go")
        except Exception as e:
            return TestResult.execution_error(str(e), "go")

    def parse_output(self, stdout: str, stderr: str, returncode: int) -> TestResult:
        """Parse Go test JSON output"""
        total = passed = failed = skipped = 0
        failures = []

        # Go test JSON is line-delimited
        for line in stdout.split("\n"):
            if not line.strip():
                continue

            try:
                data = json.loads(line)
                action = data.get("Action")
                test_name = data.get("Test")

                if action == "run" and test_name:
                    total += 1
                elif action == "pass" and test_name:
                    passed += 1
                elif action == "fail" and test_name:
                    failed += 1

                    # Extract failure message
                    output = data.get("Output", "")
                    failures.append(TestFailure(
                        test_name=f"{data.get('Package', '')}.{test_name}",
                        error_message=output.strip()
                    ))
                elif action == "skip" and test_name:
                    skipped += 1

            except json.JSONDecodeError:
                continue

        return TestResult(
            success=True,
            passed=failed == 0,
            total_tests=total,
            passed_tests=passed,
            failed_tests=failed,
            skipped_tests=skipped,
            summary=f"Go: {passed}/{total} tests passed",
            failures=failures,
            framework="go"
        )

    def get_coverage(self, path: Path) -> float:
        """Extract coverage from coverage.out"""
        coverage_file = path / "coverage.out"
        if not coverage_file.exists():
            return 0.0

        try:
            # Run go tool cover to get percentage
            result = subprocess.run(
                ["go", "tool", "cover", "-func=coverage.out"],
                cwd=path,
                capture_output=True,
                text=True
            )

            # Parse output: "total:			(statements)		XX.X%"
            for line in result.stdout.split("\n"):
                if "total:" in line:
                    percent_str = line.split()[-1].rstrip("%")
                    return float(percent_str)

        except:
            pass

        return 0.0
