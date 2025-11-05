"""Pytest Test Framework Adapter"""

import json
import subprocess
from pathlib import Path

from .base import TestFrameworkAdapter, TestResult, TestFailure


class PytestAdapter(TestFrameworkAdapter):
    """Adapter for Pytest test framework (Python)"""

    def detect(self, path: Path) -> bool:
        """Detect if Pytest is present in the project"""
        # Check for pytest config files
        pytest_configs = ["pytest.ini", "pyproject.toml", "setup.cfg", "tox.ini"]
        for config in pytest_configs:
            if (path / config).exists():
                return True

        # Check for setup.py with pytest
        setup_py = path / "setup.py"
        if setup_py.exists():
            try:
                content = setup_py.read_text()
                if "pytest" in content:
                    return True
            except:
                pass

        # Check for requirements files
        for req_file in ["requirements.txt", "requirements-dev.txt", "requirements_dev.txt"]:
            req_path = path / req_file
            if req_path.exists():
                try:
                    content = req_path.read_text()
                    if "pytest" in content:
                        return True
                except:
                    pass

        return False

    def run_tests(self, path: Path, timeout: int, with_coverage: bool = False) -> TestResult:
        """Execute Pytest tests"""
        start_time = __import__('time').time()

        try:
            # Build command
            cmd = ["pytest", "--json-report", "--json-report-file=.pytest-report.json", "-v"]
            if with_coverage:
                cmd.extend(["--cov", "--cov-report=json"])

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
            test_result.framework = "pytest"

            # Extract coverage if available
            if with_coverage:
                coverage = self.get_coverage(path)
                if coverage:
                    test_result.coverage_percent = coverage

            return test_result

        except subprocess.TimeoutExpired:
            return TestResult.timeout_error("pytest")
        except Exception as e:
            return TestResult.execution_error(str(e), "pytest")

    def parse_output(self, stdout: str, stderr: str, returncode: int) -> TestResult:
        """Parse Pytest JSON output"""
        # Try to read JSON report
        report_path = Path(".pytest-report.json")

        if report_path.exists():
            try:
                data = json.loads(report_path.read_text())
                summary = data.get("summary", {})

                total = summary.get("total", 0)
                passed = summary.get("passed", 0)
                failed = summary.get("failed", 0)
                skipped = summary.get("skipped", 0)

                # Extract failures
                failures = []
                for test in data.get("tests", []):
                    if test.get("outcome") == "failed":
                        failures.append(TestFailure(
                            test_name=test.get("nodeid", ""),
                            error_message=test.get("call", {}).get("longrepr", ""),
                            file_path=test.get("nodeid", "").split("::")[0] if "::" in test.get("nodeid", "") else None
                        ))

                return TestResult(
                    success=True,
                    passed=failed == 0,
                    total_tests=total,
                    passed_tests=passed,
                    failed_tests=failed,
                    skipped_tests=skipped,
                    summary=f"Pytest: {passed}/{total} tests passed",
                    failures=failures,
                    framework="pytest"
                )

            except (json.JSONDecodeError, FileNotFoundError):
                pass

        # Fallback: parse plain text output
        success = returncode == 0

        # Try to extract test counts from output
        total = passed = failed = 0
        for line in stdout.split("\n"):
            if "passed" in line:
                # Try to parse "X passed, Y failed in Z seconds"
                parts = line.split(",")
                for part in parts:
                    if "passed" in part:
                        try:
                            passed = int(part.split()[0])
                        except:
                            pass
                    if "failed" in part:
                        try:
                            failed = int(part.split()[0])
                        except:
                            pass

        total = passed + failed

        return TestResult(
            success=True,
            passed=success,
            total_tests=total,
            passed_tests=passed,
            failed_tests=failed,
            summary=stdout[:500] if stdout else stderr[:500],
            framework="pytest"
        )

    def get_coverage(self, path: Path) -> float:
        """Extract coverage from coverage.json"""
        coverage_file = path / "coverage.json"
        if not coverage_file.exists():
            return 0.0

        try:
            data = json.loads(coverage_file.read_text())
            totals = data.get("totals", {})
            percent = totals.get("percent_covered", 0.0)
            return float(percent)
        except:
            return 0.0
