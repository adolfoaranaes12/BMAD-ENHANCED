"""
Base Test Framework Adapter

Abstract base class and data structures for test framework adapters.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Optional, List, Dict, Any
from datetime import datetime
import time


@dataclass
class TestFailure:
    """Represents a single test failure"""
    test_name: str
    error_message: str
    stack_trace: Optional[str] = None
    file_path: Optional[str] = None
    line_number: Optional[int] = None


@dataclass
class TestResult:
    """Standard test result format returned by all adapters"""

    # Execution status
    success: bool  # Command executed successfully (not test success)

    # Test results
    passed: bool  # All tests passed
    total_tests: int = 0
    passed_tests: int = 0
    failed_tests: int = 0
    skipped_tests: int = 0

    # Additional data
    coverage_percent: float = 0.0
    duration_ms: int = 0
    summary: str = ""
    failures: List[TestFailure] = field(default_factory=list)

    # Metadata
    framework: str = "unknown"
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    errors: List[str] = field(default_factory=list)

    def to_bmad_format(self) -> Dict[str, Any]:
        """Convert to BMAD standard output format"""
        return {
            "success": self.success,
            "outputs": {
                "passed": self.passed,
                "summary": self.summary or f"{self.passed_tests}/{self.total_tests} tests passed",
                "total_tests": self.total_tests,
                "passed_tests": self.passed_tests,
                "failed_tests": self.failed_tests,
                "skipped_tests": self.skipped_tests,
                "coverage_percent": self.coverage_percent,
                "duration_ms": self.duration_ms,
                "failures": [
                    {
                        "test_name": f.test_name,
                        "error_message": f.error_message,
                        "stack_trace": f.stack_trace,
                        "file_path": f.file_path,
                        "line_number": f.line_number
                    }
                    for f in self.failures
                ]
            },
            "telemetry": {
                "command": "run_tests",
                "framework": self.framework,
                "duration_ms": self.duration_ms,
                "timestamp": self.timestamp,
                "total_tests": self.total_tests,
                "passed_tests": self.passed_tests,
                "failed_tests": self.failed_tests
            },
            "errors": self.errors
        }

    @classmethod
    def timeout_error(cls, framework: str = "unknown") -> "TestResult":
        """Create result for timeout error"""
        return cls(
            success=False,
            passed=False,
            framework=framework,
            errors=["timeout"]
        )

    @classmethod
    def execution_error(cls, error_message: str, framework: str = "unknown") -> "TestResult":
        """Create result for execution error"""
        return cls(
            success=False,
            passed=False,
            framework=framework,
            errors=[f"execution_error: {error_message}"]
        )

    @classmethod
    def parse_error(cls, stdout: str, stderr: str, framework: str = "unknown") -> "TestResult":
        """Create result for parse error"""
        return cls(
            success=True,
            passed=False,
            summary=f"Parse error. Stdout: {stdout[:200]}... Stderr: {stderr[:200]}...",
            framework=framework,
            errors=["parse_error"]
        )


class TestFrameworkAdapter(ABC):
    """
    Abstract base class for test framework adapters.

    Each test framework (Jest, Pytest, JUnit, etc.) implements this interface
    to provide standardized test execution and result parsing.
    """

    def __init__(self, config: Dict[str, Any]):
        """
        Initialize adapter with framework-specific configuration.

        Args:
            config: Framework configuration from .claude/config.yaml
        """
        self.config = config
        self.name = config.get("name", "unknown")
        self.command = config.get("command", [])
        self.coverage_command = config.get("coverage_command", [])

    @abstractmethod
    def detect(self, path: Path) -> bool:
        """
        Auto-detect if this framework is present in the project.

        Args:
            path: Project root path

        Returns:
            True if framework detected, False otherwise
        """
        pass

    @abstractmethod
    def run_tests(self, path: Path, timeout: int, with_coverage: bool = False) -> TestResult:
        """
        Execute tests and return structured results.

        Args:
            path: Path to test directory
            timeout: Timeout in seconds
            with_coverage: Whether to collect coverage

        Returns:
            TestResult with execution results
        """
        pass

    @abstractmethod
    def parse_output(self, stdout: str, stderr: str, returncode: int) -> TestResult:
        """
        Parse test framework output into standard format.

        Args:
            stdout: Standard output from test command
            stderr: Standard error from test command
            returncode: Process return code

        Returns:
            Parsed TestResult
        """
        pass

    def get_coverage(self, path: Path) -> Optional[float]:
        """
        Extract coverage percentage if available.

        Override this if framework has separate coverage extraction.

        Args:
            path: Project root path

        Returns:
            Coverage percentage (0-100) or None
        """
        return None

    def _measure_duration(self, func):
        """Utility to measure execution duration"""
        start = time.time()
        result = func()
        duration_ms = int((time.time() - start) * 1000)
        return result, duration_ms
