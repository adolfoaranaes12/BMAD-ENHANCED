#!/usr/bin/env python3
"""
BMAD Command: run_tests
Execute tests with specified framework using adapter pattern

Version: 2.0 - Framework-agnostic with adapter pattern
"""

import json
import sys
from pathlib import Path
from datetime import datetime

# Import framework registry
try:
    from framework_registry import FrameworkRegistry
    USE_ADAPTERS = True
except ImportError:
    USE_ADAPTERS = False
    print("Warning: Framework registry not available, using legacy mode", file=sys.stderr)


def run_tests_v2(path: str, framework: str = "auto", timeout_sec: int = 120, with_coverage: bool = False):
    """Execute tests using framework adapter (v2)"""

    try:
        # Initialize registry
        registry = FrameworkRegistry()

        # Auto-detect framework if needed
        if framework == "auto":
            detected = registry.detect_framework(Path(path))
            if not detected:
                return {
                    "success": False,
                    "outputs": {},
                    "telemetry": {
                        "command": "run_tests",
                        "framework": "auto",
                        "duration_ms": 0,
                        "timestamp": datetime.now().isoformat()
                    },
                    "errors": ["no_framework_detected", "hint: specify framework explicitly with --framework"]
                }
            framework = detected
            print(f"Auto-detected framework: {framework}", file=sys.stderr)

        # Get adapter for framework
        adapter = registry.get_adapter(framework)
        if not adapter:
            available = ", ".join(registry.list_frameworks())
            return {
                "success": False,
                "outputs": {},
                "telemetry": {
                    "command": "run_tests",
                    "framework": framework,
                    "duration_ms": 0,
                    "timestamp": datetime.now().isoformat()
                },
                "errors": [
                    f"unsupported_framework: {framework}",
                    f"available_frameworks: {available}"
                ]
            }

        # Execute tests using adapter
        result = adapter.run_tests(Path(path), timeout_sec, with_coverage)

        # Convert to BMAD format
        return result.to_bmad_format()

    except Exception as e:
        return {
            "success": False,
            "outputs": {},
            "telemetry": {
                "command": "run_tests",
                "framework": framework,
                "duration_ms": 0,
                "timestamp": datetime.now().isoformat()
            },
            "errors": [f"unexpected_error: {str(e)}"]
        }


def run_tests_legacy(path: str, framework: str = "jest", timeout_sec: int = 120):
    """Legacy implementation for backward compatibility"""
    import subprocess
    import time

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
            result = subprocess.run(
                ["npm", "test", "--", "--json", "--passWithNoTests"],
                cwd=test_path,
                capture_output=True,
                timeout=timeout_sec,
                text=True
            )

            try:
                test_results = json.loads(result.stdout)
                success = test_results.get("success", False)
                num_total = test_results.get("numTotalTests", 0)
                num_passed = test_results.get("numPassedTests", 0)
                num_failed = test_results.get("numFailedTests", 0)

                return {
                    "success": True,
                    "outputs": {
                        "passed": success,
                        "summary": f"{num_passed}/{num_total} tests passed",
                        "total_tests": num_total,
                        "passed_tests": num_passed,
                        "failed_tests": num_failed,
                        "coverage_percent": 0,
                        "junit_path": str(test_path / "junit.xml")
                    },
                    "telemetry": {
                        "command": "run_tests",
                        "framework": framework,
                        "duration_ms": int((time.time() - start_time) * 1000),
                        "timestamp": datetime.now().isoformat()
                    },
                    "errors": []
                }
            except json.JSONDecodeError:
                stdout = result.stdout
                return {
                    "success": True,
                    "outputs": {
                        "passed": result.returncode == 0,
                        "summary": stdout if stdout else result.stderr,
                        "total_tests": 0,
                        "passed_tests": 0,
                        "failed_tests": 0,
                        "coverage_percent": 0
                    },
                    "telemetry": {
                        "command": "run_tests",
                        "framework": framework,
                        "duration_ms": int((time.time() - start_time) * 1000),
                        "timestamp": datetime.now().isoformat()
                    },
                    "errors": ["json_parse_failed"]
                }

        elif framework == "pytest":
            result = subprocess.run(
                ["pytest", "--json-report", "--json-report-file=report.json"],
                cwd=test_path,
                capture_output=True,
                timeout=timeout_sec,
                text=True
            )

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
                        "coverage_percent": 0
                    },
                    "telemetry": {
                        "command": "run_tests",
                        "framework": framework,
                        "duration_ms": int((time.time() - start_time) * 1000),
                        "timestamp": datetime.now().isoformat()
                    },
                    "errors": []
                }

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


def run_tests(path: str, framework: str = "auto", timeout_sec: int = 120, with_coverage: bool = False):
    """Main entry point - uses v2 if available, falls back to legacy"""
    if USE_ADAPTERS:
        return run_tests_v2(path, framework, timeout_sec, with_coverage)
    else:
        # Legacy mode: map "auto" to "jest" for backward compatibility
        if framework == "auto":
            framework = "jest"
        return run_tests_legacy(path, framework, timeout_sec)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run tests with structured output")
    parser.add_argument("--path", required=True, help="Path to tests")
    parser.add_argument("--framework", default="auto", help="Test framework (auto, jest, pytest, junit, gtest, cargo, go, etc.)")
    parser.add_argument("--timeout", type=int, default=120, help="Timeout in seconds")
    parser.add_argument("--coverage", action="store_true", help="Collect coverage data")
    parser.add_argument("--output", default="json", choices=["json"], help="Output format")
    parser.add_argument("--list-frameworks", action="store_true", help="List available frameworks")

    args = parser.parse_args()

    # List frameworks if requested
    if args.list_frameworks:
        if USE_ADAPTERS:
            registry = FrameworkRegistry()
            frameworks = registry.list_frameworks_detailed()
            print(json.dumps({"frameworks": frameworks}, indent=2))
        else:
            print(json.dumps({"frameworks": ["jest", "pytest"]}, indent=2))
        sys.exit(0)

    # Run tests
    result = run_tests(args.path, args.framework, args.timeout, args.coverage)
    print(json.dumps(result, indent=2))

    sys.exit(0 if result["success"] and result.get("outputs", {}).get("passed", False) else 1)
