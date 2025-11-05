"""JUnit Test Framework Adapter (Java/Kotlin)"""

import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path

from .base import TestFrameworkAdapter, TestResult, TestFailure


class JUnitAdapter(TestFrameworkAdapter):
    """Adapter for JUnit test framework (Java/Kotlin with Maven/Gradle)"""

    def detect(self, path: Path) -> bool:
        """Detect if JUnit/Maven/Gradle is present"""
        return (path / "pom.xml").exists() or \
               (path / "build.gradle").exists() or \
               (path / "build.gradle.kts").exists()

    def run_tests(self, path: Path, timeout: int, with_coverage: bool = False) -> TestResult:
        """Execute JUnit tests via Maven or Gradle"""
        start_time = __import__('time').time()

        try:
            # Detect build tool
            if (path / "pom.xml").exists():
                cmd = ["mvn", "test"]
            elif (path / "build.gradle.kts").exists() or (path / "build.gradle").exists():
                cmd = ["./gradlew", "test"] if (path / "gradlew").exists() else ["gradle", "test"]
            else:
                return TestResult.execution_error("No build tool found", "junit")

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
            test_result.framework = "junit"

            return test_result

        except subprocess.TimeoutExpired:
            return TestResult.timeout_error("junit")
        except Exception as e:
            return TestResult.execution_error(str(e), "junit")

    def parse_output(self, stdout: str, stderr: str, returncode: int) -> TestResult:
        """Parse JUnit XML reports"""
        # Find test report directories
        report_dirs = [
            Path("target/surefire-reports"),  # Maven
            Path("build/test-results/test")   # Gradle
        ]

        total = passed = failed = skipped = 0
        failures = []

        for report_dir in report_dirs:
            if not report_dir.exists():
                continue

            # Parse all TEST-*.xml files
            for xml_file in report_dir.glob("TEST-*.xml"):
                try:
                    tree = ET.parse(xml_file)
                    root = tree.getroot()

                    total += int(root.get("tests", 0))
                    failed += int(root.get("failures", 0)) + int(root.get("errors", 0))
                    skipped += int(root.get("skipped", 0))

                    # Extract failure details
                    for testcase in root.findall(".//testcase"):
                        failure = testcase.find("failure")
                        error = testcase.find("error")

                        if failure is not None or error is not None:
                            elem = failure if failure is not None else error
                            failures.append(TestFailure(
                                test_name=f"{testcase.get('classname', '')}.{testcase.get('name', '')}",
                                error_message=elem.get("message", ""),
                                stack_trace=elem.text,
                                file_path=testcase.get('classname', '').replace('.', '/') + '.java'
                            ))

                except Exception as e:
                    print(f"Warning: Failed to parse {xml_file}: {e}")

        passed = total - failed - skipped

        if total == 0:
            # No XML reports found, try to parse stdout
            return TestResult(
                success=True,
                passed=returncode == 0,
                summary=stdout[:500] if stdout else stderr[:500],
                framework="junit",
                errors=["no_test_reports_found"] if returncode != 0 else []
            )

        return TestResult(
            success=True,
            passed=failed == 0,
            total_tests=total,
            passed_tests=passed,
            failed_tests=failed,
            skipped_tests=skipped,
            summary=f"JUnit: {passed}/{total} tests passed",
            failures=failures,
            framework="junit"
        )
