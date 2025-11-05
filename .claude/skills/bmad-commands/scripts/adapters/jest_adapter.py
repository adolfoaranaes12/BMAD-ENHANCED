"""Jest Test Framework Adapter"""

import json
import subprocess
from pathlib import Path
from typing import Dict, Any

from .base import TestFrameworkAdapter, TestResult, TestFailure


class JestAdapter(TestFrameworkAdapter):
    """Adapter for Jest test framework (JavaScript/TypeScript)"""

    def detect(self, path: Path) -> bool:
        """Detect if Jest is present in the project"""
        # Check for package.json with jest dependency
        package_json = path / "package.json"
        if package_json.exists():
            try:
                data = json.loads(package_json.read_text())
                deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
                if "jest" in deps:
                    return True
            except:
                pass

        # Check for jest config files
        jest_configs = ["jest.config.js", "jest.config.ts", "jest.config.json"]
        for config in jest_configs:
            if (path / config).exists():
                return True

        return False

    def run_tests(self, path: Path, timeout: int, with_coverage: bool = False) -> TestResult:
        """Execute Jest tests"""
        start_time = __import__('time').time()

        try:
            # Build command
            cmd = ["npm", "test", "--", "--json", "--passWithNoTests"]
            if with_coverage:
                cmd.append("--coverage")

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
            test_result.framework = "jest"

            return test_result

        except subprocess.TimeoutExpired:
            return TestResult.timeout_error("jest")
        except Exception as e:
            return TestResult.execution_error(str(e), "jest")

    def parse_output(self, stdout: str, stderr: str, returncode: int) -> TestResult:
        """Parse Jest JSON output"""
        try:
            # Parse JSON output
            data = json.loads(stdout)

            success = data.get("success", False)
            num_total = data.get("numTotalTests", 0)
            num_passed = data.get("numPassedTests", 0)
            num_failed = data.get("numFailedTests", 0)
            num_pending = data.get("numPendingTests", 0)

            # Extract failures
            failures = []
            for test_result in data.get("testResults", []):
                for assertion in test_result.get("assertionResults", []):
                    if assertion.get("status") == "failed":
                        failures.append(TestFailure(
                            test_name=assertion.get("fullName", ""),
                            error_message=assertion.get("failureMessages", [""])[0] if assertion.get("failureMessages") else "",
                            stack_trace=assertion.get("failureMessages", [""])[0] if assertion.get("failureMessages") else None,
                            file_path=test_result.get("name")
                        ))

            # Extract coverage
            coverage_percent = 0.0
            coverage_data = data.get("coverageMap", {})
            if coverage_data:
                # Jest coverage is complex, approximate from totals
                total_coverage = coverage_data.get("total", {})
                if total_coverage:
                    statements = total_coverage.get("statements", {}).get("pct", 0)
                    branches = total_coverage.get("branches", {}).get("pct", 0)
                    functions = total_coverage.get("functions", {}).get("pct", 0)
                    lines = total_coverage.get("lines", {}).get("pct", 0)
                    coverage_percent = (statements + branches + functions + lines) / 4

            return TestResult(
                success=True,
                passed=success,
                total_tests=num_total,
                passed_tests=num_passed,
                failed_tests=num_failed,
                skipped_tests=num_pending,
                coverage_percent=coverage_percent,
                summary=f"Jest: {num_passed}/{num_total} tests passed",
                failures=failures,
                framework="jest"
            )

        except json.JSONDecodeError:
            # Fallback: parse plain text output
            success = returncode == 0
            return TestResult(
                success=True,
                passed=success,
                summary=stdout if stdout else stderr,
                framework="jest",
                errors=["json_parse_failed"] if not success else []
            )
