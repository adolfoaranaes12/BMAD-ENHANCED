#!/usr/bin/env python3
"""
BMAD Command: run_tests
Execute tests with specified framework and return structured results
"""

import json
import subprocess
import sys
import time
from pathlib import Path
from datetime import datetime


def run_tests(path: str, framework: str = "jest", timeout_sec: int = 120):
    """Execute tests and return structured results"""
    start_time = time.time()

    try:
        # Validate path
        test_path = Path(path)
        if not test_path.exists():
            return {
                "success": False,
                "outputs": {},
                "telemetry": {
                    "command": "run_tests",
                    "framework": framework,
                    "duration_ms": int((time.time() - start_time) * 1000),
                    "timestamp": datetime.now().isoformat()
                },
                "errors": ["invalid_path"]
            }

        # Execute tests based on framework
        if framework == "jest":
            try:
                # Run jest with JSON output
                result = subprocess.run(
                    ["npm", "test", "--", "--json", "--passWithNoTests"],
                    cwd=test_path,
                    capture_output=True,
                    timeout=timeout_sec,
                    text=True
                )

                # Parse jest JSON output
                try:
                    test_results = json.loads(result.stdout)
                    success = test_results.get("success", False)
                    num_total = test_results.get("numTotalTests", 0)
                    num_passed = test_results.get("numPassedTests", 0)
                    num_failed = test_results.get("numFailedTests", 0)

                    # Extract coverage if available
                    coverage_data = test_results.get("coverageMap", {})
                    coverage_percent = 0
                    if coverage_data:
                        total_coverage = coverage_data.get("total", {})
                        coverage_percent = total_coverage.get("pct", 0)

                    return {
                        "success": True,
                        "outputs": {
                            "passed": success,
                            "summary": f"{num_passed}/{num_total} tests passed",
                            "total_tests": num_total,
                            "passed_tests": num_passed,
                            "failed_tests": num_failed,
                            "coverage_percent": coverage_percent,
                            "junit_path": str(test_path / "junit.xml")
                        },
                        "telemetry": {
                            "command": "run_tests",
                            "framework": framework,
                            "duration_ms": int((time.time() - start_time) * 1000),
                            "timestamp": datetime.now().isoformat(),
                            "total_tests": num_total,
                            "passed_tests": num_passed,
                            "failed_tests": num_failed
                        },
                        "errors": []
                    }
                except json.JSONDecodeError:
                    # Jest output wasn't JSON, try parsing plain text
                    stdout = result.stdout
                    stderr = result.stderr
                    success = result.returncode == 0

                    return {
                        "success": True,
                        "outputs": {
                            "passed": success,
                            "summary": stdout if stdout else stderr,
                            "total_tests": 0,
                            "passed_tests": 0 if not success else 0,
                            "failed_tests": 0 if success else 0,
                            "coverage_percent": 0,
                            "junit_path": ""
                        },
                        "telemetry": {
                            "command": "run_tests",
                            "framework": framework,
                            "duration_ms": int((time.time() - start_time) * 1000),
                            "timestamp": datetime.now().isoformat()
                        },
                        "errors": ["json_parse_failed"]
                    }

            except subprocess.TimeoutExpired:
                return {
                    "success": False,
                    "outputs": {},
                    "telemetry": {
                        "command": "run_tests",
                        "framework": framework,
                        "duration_ms": int((time.time() - start_time) * 1000),
                        "timestamp": datetime.now().isoformat()
                    },
                    "errors": ["timeout"]
                }

        elif framework == "pytest":
            # Pytest support
            try:
                result = subprocess.run(
                    ["pytest", "--json-report", "--json-report-file=report.json"],
                    cwd=test_path,
                    capture_output=True,
                    timeout=timeout_sec,
                    text=True
                )

                # Read JSON report
                report_path = test_path / "report.json"
                if report_path.exists():
                    report_data = json.loads(report_path.read_text())
                    summary = report_data.get("summary", {})

                    return {
                        "success": True,
                        "outputs": {
                            "passed": summary.get("failed", 0) == 0,
                            "summary": f"{summary.get('passed', 0)}/{summary.get('total', 0)} tests passed",
                            "total_tests": summary.get("total", 0),
                            "passed_tests": summary.get("passed", 0),
                            "failed_tests": summary.get("failed", 0),
                            "coverage_percent": 0,  # Pytest coverage requires separate plugin
                            "junit_path": ""
                        },
                        "telemetry": {
                            "command": "run_tests",
                            "framework": framework,
                            "duration_ms": int((time.time() - start_time) * 1000),
                            "timestamp": datetime.now().isoformat()
                        },
                        "errors": []
                    }
                else:
                    return {
                        "success": False,
                        "outputs": {},
                        "telemetry": {
                            "command": "run_tests",
                            "framework": framework,
                            "duration_ms": int((time.time() - start_time) * 1000),
                            "timestamp": datetime.now().isoformat()
                        },
                        "errors": ["report_not_found"]
                    }

            except subprocess.TimeoutExpired:
                return {
                    "success": False,
                    "outputs": {},
                    "telemetry": {
                        "command": "run_tests",
                        "framework": framework,
                        "duration_ms": int((time.time() - start_time) * 1000),
                        "timestamp": datetime.now().isoformat()
                    },
                    "errors": ["timeout"]
                }

        else:
            return {
                "success": False,
                "outputs": {},
                "telemetry": {
                    "command": "run_tests",
                    "framework": framework,
                    "duration_ms": int((time.time() - start_time) * 1000),
                    "timestamp": datetime.now().isoformat()
                },
                "errors": ["unsupported_framework"]
            }

    except Exception as e:
        return {
            "success": False,
            "outputs": {},
            "telemetry": {
                "command": "run_tests",
                "framework": framework,
                "duration_ms": int((time.time() - start_time) * 1000),
                "timestamp": datetime.now().isoformat()
            },
            "errors": [f"unexpected_error: {str(e)}"]
        }


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run tests with structured output")
    parser.add_argument("--path", required=True, help="Path to tests")
    parser.add_argument("--framework", default="jest", choices=["jest", "pytest"], help="Test framework")
    parser.add_argument("--timeout", type=int, default=120, help="Timeout in seconds")
    parser.add_argument("--output", default="json", choices=["json"], help="Output format")

    args = parser.parse_args()

    result = run_tests(args.path, args.framework, args.timeout)
    print(json.dumps(result, indent=2))

    sys.exit(0 if result["success"] else 1)
