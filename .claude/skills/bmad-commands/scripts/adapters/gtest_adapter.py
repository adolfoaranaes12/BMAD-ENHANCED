"""Google Test (GTest) Framework Adapter (C++)"""

import subprocess
import json
from pathlib import Path

from .base import TestFrameworkAdapter, TestResult, TestFailure


class GTestAdapter(TestFrameworkAdapter):
    """Adapter for Google Test framework (C++)"""

    def detect(self, path: Path) -> bool:
        """Detect if Google Test is present"""
        # Check for CMakeLists.txt with gtest
        cmake_file = path / "CMakeLists.txt"
        if cmake_file.exists():
            try:
                content = cmake_file.read_text()
                if "gtest" in content.lower() or "googletest" in content.lower():
                    return True
            except:
                pass

        # Check for build directory with test executables
        build_dirs = ["build", "cmake-build-debug", "cmake-build-release"]
        for build_dir in build_dirs:
            build_path = path / build_dir
            if build_path.exists():
                # Look for test executables
                for exe in build_path.rglob("*test*"):
                    if exe.is_file() and exe.stat().st_mode & 0o111:  # Executable
                        return True

        return False

    def run_tests(self, path: Path, timeout: int, with_coverage: bool = False) -> TestResult:
        """Execute Google Test tests"""
        start_time = __import__('time').time()

        try:
            # Try CTest first (CMake test runner)
            build_dirs = ["build", "cmake-build-debug", "cmake-build-release"]
            build_dir = None

            for bd in build_dirs:
                if (path / bd).exists():
                    build_dir = path / bd
                    break

            if not build_dir:
                return TestResult.execution_error("No build directory found", "gtest")

            # Run CTest with output on failure
            result = subprocess.run(
                ["ctest", "--output-on-failure", "--verbose"],
                cwd=build_dir,
                capture_output=True,
                timeout=timeout,
                text=True
            )

            # Parse result
            test_result = self.parse_output(result.stdout, result.stderr, result.returncode)

            # Add duration
            test_result.duration_ms = int((__import__('time').time() - start_time) * 1000)
            test_result.framework = "gtest"

            return test_result

        except subprocess.TimeoutExpired:
            return TestResult.timeout_error("gtest")
        except Exception as e:
            return TestResult.execution_error(str(e), "gtest")

    def parse_output(self, stdout: str, stderr: str, returncode: int) -> TestResult:
        """Parse CTest/GTest output"""
        total = passed = failed = 0
        failures = []

        # Parse CTest output
        for line in stdout.split("\n"):
            # Look for test results (e.g., "1/10 Test #1: MyTest ...................   Passed")
            if "Test #" in line:
                total += 1
                if "Passed" in line:
                    passed += 1
                elif "Failed" in line:
                    failed += 1

                    # Extract test name
                    parts = line.split(":")
                    if len(parts) >= 2:
                        test_name = parts[1].split("...")[0].strip()
                        failures.append(TestFailure(
                            test_name=test_name,
                            error_message="Test failed (see output for details)"
                        ))

        # If no tests found in CTest format, try GTest format
        if total == 0:
            # GTest output: "[  PASSED  ] 5 tests."
            for line in stdout.split("\n"):
                if "[  PASSED  ]" in line and "tests" in line:
                    try:
                        passed = int(line.split()[3])
                    except:
                        pass
                elif "[  FAILED  ]" in line and "tests" in line:
                    try:
                        failed = int(line.split()[3])
                    except:
                        pass

            total = passed + failed

        return TestResult(
            success=True,
            passed=failed == 0,
            total_tests=total,
            passed_tests=passed,
            failed_tests=failed,
            summary=f"GTest: {passed}/{total} tests passed",
            failures=failures,
            framework="gtest"
        )
