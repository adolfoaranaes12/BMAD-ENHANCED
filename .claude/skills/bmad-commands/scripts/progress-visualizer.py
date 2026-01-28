#!/usr/bin/env python3
"""
BMAD Enhanced - Progress Visualization System
Provides real-time progress tracking for workflows and commands.
"""

import sys
import time
import json
from datetime import datetime, timedelta
from typing import Optional, List, Dict
from enum import Enum


class ProgressStyle(Enum):
    """Progress bar styles"""
    BAR = "bar"           # [████████░░] 80%
    SPINNER = "spinner"   # ⠋ Processing...
    DOTS = "dots"         # ... Processing
    MINIMAL = "minimal"   # Step 1/7


class Colors:
    """ANSI color codes"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'


class WorkflowStep(Enum):
    """7-step workflow phases"""
    LOAD = 1
    ASSESS = 2
    ROUTE = 3
    GUARD = 4
    EXECUTE = 5
    VERIFY = 6
    TELEMETRY = 7


STEP_NAMES = {
    WorkflowStep.LOAD: "Load Context",
    WorkflowStep.ASSESS: "Assess Complexity",
    WorkflowStep.ROUTE: "Route Strategy",
    WorkflowStep.GUARD: "Check Guardrails",
    WorkflowStep.EXECUTE: "Execute",
    WorkflowStep.VERIFY: "Verify Results",
    WorkflowStep.TELEMETRY: "Emit Telemetry"
}

STEP_DESCRIPTIONS = {
    WorkflowStep.LOAD: "Loading configuration and context",
    WorkflowStep.ASSESS: "Analyzing complexity factors",
    WorkflowStep.ROUTE: "Selecting execution strategy",
    WorkflowStep.GUARD: "Validating guardrails",
    WorkflowStep.EXECUTE: "Executing primary operation",
    WorkflowStep.VERIFY: "Verifying outcomes",
    WorkflowStep.TELEMETRY: "Recording telemetry"
}

SPINNER_FRAMES = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']


class ProgressTracker:
    """Tracks and displays progress for BMAD operations"""

    def __init__(self,
                 total_steps: int = 7,
                 style: ProgressStyle = ProgressStyle.BAR,
                 show_eta: bool = True,
                 show_elapsed: bool = True):
        self.total_steps = total_steps
        self.current_step = 0
        self.style = style
        self.show_eta = show_eta
        self.show_elapsed = show_elapsed
        self.start_time = None
        self.step_start_time = None
        self.step_times: List[float] = []
        self.spinner_index = 0
        self.completed = False

    def start(self, operation_name: str = "Operation"):
        """Start progress tracking"""
        self.start_time = datetime.now()
        self.operation_name = operation_name
        self._print(f"\n{Colors.BOLD}{Colors.CYAN}Starting: {operation_name}{Colors.ENDC}\n")

    def update_step(self, step: WorkflowStep, status: str = ""):
        """Update to a new workflow step"""
        if self.step_start_time:
            elapsed = (datetime.now() - self.step_start_time).total_seconds()
            self.step_times.append(elapsed)

        self.current_step = step.value
        self.step_start_time = datetime.now()

        step_name = STEP_NAMES[step]
        step_desc = STEP_DESCRIPTIONS[step]

        if status:
            step_desc = status

        self._render_progress(step_name, step_desc)

    def update_substep(self, message: str):
        """Update substep within current step"""
        self._render_progress(STEP_NAMES[WorkflowStep(self.current_step)], message, is_substep=True)

    def complete(self, message: str = "Completed successfully"):
        """Mark operation as complete"""
        self.completed = True
        self.current_step = self.total_steps

        total_elapsed = (datetime.now() - self.start_time).total_seconds()

        self._print(f"\n{Colors.GREEN}✓{Colors.ENDC} {Colors.BOLD}{message}{Colors.ENDC}")
        if self.show_elapsed:
            self._print(f"  {Colors.DIM}Total time: {self._format_duration(total_elapsed)}{Colors.ENDC}\n")

    def error(self, message: str):
        """Mark operation as failed"""
        self.completed = True
        total_elapsed = (datetime.now() - self.start_time).total_seconds() if self.start_time else 0

        self._print(f"\n{Colors.RED}✗{Colors.ENDC} {Colors.BOLD}{message}{Colors.ENDC}")
        if self.show_elapsed and total_elapsed > 0:
            self._print(f"  {Colors.DIM}Time elapsed: {self._format_duration(total_elapsed)}{Colors.ENDC}\n")

    def _render_progress(self, step_name: str, description: str, is_substep: bool = False):
        """Render progress based on style"""
        if self.style == ProgressStyle.BAR:
            self._render_bar(step_name, description, is_substep)
        elif self.style == ProgressStyle.SPINNER:
            self._render_spinner(step_name, description, is_substep)
        elif self.style == ProgressStyle.DOTS:
            self._render_dots(step_name, description, is_substep)
        elif self.style == ProgressStyle.MINIMAL:
            self._render_minimal(step_name, description, is_substep)

    def _render_bar(self, step_name: str, description: str, is_substep: bool):
        """Render progress bar style"""
        progress = self.current_step / self.total_steps
        bar_width = 30
        filled = int(bar_width * progress)
        bar = '█' * filled + '░' * (bar_width - filled)

        percentage = int(progress * 100)

        prefix = "  ↳" if is_substep else "▶"
        color = Colors.CYAN if is_substep else Colors.BLUE

        eta_str = ""
        if self.show_eta and not is_substep and self.step_times:
            eta = self._estimate_remaining()
            if eta:
                eta_str = f" | ETA: {self._format_duration(eta)}"

        elapsed_str = ""
        if self.show_elapsed and self.step_start_time:
            elapsed = (datetime.now() - self.step_start_time).total_seconds()
            elapsed_str = f" | {self._format_duration(elapsed)}"

        line = f"{prefix} {color}[{bar}] {percentage}%{Colors.ENDC} | Step {self.current_step}/{self.total_steps}: {Colors.BOLD}{step_name}{Colors.ENDC}{eta_str}{elapsed_str}"
        self._print(line)

        if description and not is_substep:
            self._print(f"   {Colors.DIM}{description}{Colors.ENDC}")

    def _render_spinner(self, step_name: str, description: str, is_substep: bool):
        """Render spinner style"""
        spinner = SPINNER_FRAMES[self.spinner_index % len(SPINNER_FRAMES)]
        self.spinner_index += 1

        prefix = "  ↳" if is_substep else spinner
        color = Colors.CYAN if is_substep else Colors.BLUE

        line = f"{prefix} {color}Step {self.current_step}/{self.total_steps}: {Colors.BOLD}{step_name}{Colors.ENDC}"
        if description:
            line += f" - {Colors.DIM}{description}{Colors.ENDC}"

        self._print(line)

    def _render_dots(self, step_name: str, description: str, is_substep: bool):
        """Render dots style"""
        dots = "." * (self.spinner_index % 4)
        self.spinner_index += 1

        prefix = "  ↳" if is_substep else "•"
        color = Colors.CYAN if is_substep else Colors.BLUE

        line = f"{prefix} {color}{step_name}{dots}{Colors.ENDC}"
        if description:
            line += f" {Colors.DIM}{description}{Colors.ENDC}"

        self._print(line)

    def _render_minimal(self, step_name: str, description: str, is_substep: bool):
        """Render minimal style"""
        prefix = "  ↳" if is_substep else "▶"
        color = Colors.CYAN if is_substep else Colors.BLUE

        line = f"{prefix} {color}[{self.current_step}/{self.total_steps}] {step_name}{Colors.ENDC}"
        if description:
            line += f" - {Colors.DIM}{description}{Colors.ENDC}"

        self._print(line)

    def _estimate_remaining(self) -> Optional[float]:
        """Estimate remaining time based on average step time"""
        if not self.step_times:
            return None

        avg_step_time = sum(self.step_times) / len(self.step_times)
        remaining_steps = self.total_steps - self.current_step
        return avg_step_time * remaining_steps

    def _format_duration(self, seconds: float) -> str:
        """Format duration in human-readable format"""
        if seconds < 1:
            return f"{int(seconds * 1000)}ms"
        elif seconds < 60:
            return f"{seconds:.1f}s"
        elif seconds < 3600:
            minutes = int(seconds / 60)
            secs = int(seconds % 60)
            return f"{minutes}m {secs}s"
        else:
            hours = int(seconds / 3600)
            minutes = int((seconds % 3600) / 60)
            return f"{hours}h {minutes}m"

    def _print(self, message: str):
        """Print message to stderr (so it doesn't interfere with output)"""
        print(message, file=sys.stderr, flush=True)


class WorkflowProgress:
    """Specialized progress tracker for BMAD workflows"""

    def __init__(self, workflow_type: str, subagent: str, command: str):
        self.workflow_type = workflow_type
        self.subagent = subagent
        self.command = command
        self.tracker = ProgressTracker(
            total_steps=7,
            style=ProgressStyle.BAR,
            show_eta=True,
            show_elapsed=True
        )

    def start(self):
        """Start workflow progress"""
        operation_name = f"{self.subagent} - {self.command}"
        self.tracker.start(operation_name)

    def load_context(self, details: str = ""):
        """Step 1: Load Context"""
        self.tracker.update_step(WorkflowStep.LOAD, details)

    def assess_complexity(self, score: Optional[int] = None):
        """Step 2: Assess Complexity"""
        details = f"Complexity score: {score}" if score else ""
        self.tracker.update_step(WorkflowStep.ASSESS, details)

    def route_strategy(self, strategy: str):
        """Step 3: Route Strategy"""
        self.tracker.update_step(WorkflowStep.ROUTE, f"Strategy: {strategy}")

    def check_guardrails(self, passed: bool = True):
        """Step 4: Check Guardrails"""
        status = "All guardrails passed" if passed else "Guardrail violations detected"
        self.tracker.update_step(WorkflowStep.GUARD, status)

    def execute(self, details: str = ""):
        """Step 5: Execute"""
        self.tracker.update_step(WorkflowStep.EXECUTE, details)

    def execute_substep(self, substep: str):
        """Update substep during execution"""
        self.tracker.update_substep(substep)

    def verify(self, success: bool = True):
        """Step 6: Verify"""
        status = "Verification successful" if success else "Verification issues detected"
        self.tracker.update_step(WorkflowStep.VERIFY, status)

    def emit_telemetry(self):
        """Step 7: Emit Telemetry"""
        self.tracker.update_step(WorkflowStep.TELEMETRY, "Recording metrics")

    def complete(self, message: str = "Workflow completed successfully"):
        """Complete workflow"""
        self.tracker.complete(message)

    def error(self, message: str):
        """Error in workflow"""
        self.tracker.error(message)


def demo_progress():
    """Demo the progress visualization system"""
    import time

    # Demo 1: Workflow progress
    print("\n" + "=" * 70)
    print("DEMO 1: Full Workflow Progress")
    print("=" * 70)

    workflow = WorkflowProgress("feature-delivery", "james", "*implement")
    workflow.start()

    time.sleep(0.5)
    workflow.load_context("Loading task spec and project context")
    time.sleep(0.5)

    workflow.assess_complexity(score=65)
    time.sleep(0.5)

    workflow.route_strategy("complex")
    time.sleep(0.5)

    workflow.check_guardrails(passed=True)
    time.sleep(0.5)

    workflow.execute("Implementing feature with TDD approach")
    time.sleep(0.3)
    workflow.execute_substep("Writing unit tests")
    time.sleep(0.3)
    workflow.execute_substep("Implementing core logic")
    time.sleep(0.3)
    workflow.execute_substep("Running tests")
    time.sleep(0.5)

    workflow.verify(success=True)
    time.sleep(0.5)

    workflow.emit_telemetry()
    time.sleep(0.3)

    workflow.complete("Feature implemented successfully with 95% test coverage")

    # Demo 2: Different styles
    print("\n" + "=" * 70)
    print("DEMO 2: Different Progress Styles")
    print("=" * 70)

    styles = [
        (ProgressStyle.BAR, "Bar Style"),
        (ProgressStyle.SPINNER, "Spinner Style"),
        (ProgressStyle.DOTS, "Dots Style"),
        (ProgressStyle.MINIMAL, "Minimal Style")
    ]

    for style, name in styles:
        print(f"\n{Colors.BOLD}{name}:{Colors.ENDC}")
        tracker = ProgressTracker(total_steps=3, style=style, show_eta=False, show_elapsed=False)
        tracker.start("Quick Demo")

        tracker.current_step = 1
        tracker._render_progress("Step 1", "Processing...", False)
        time.sleep(0.3)

        tracker.current_step = 2
        tracker._render_progress("Step 2", "Analyzing...", False)
        time.sleep(0.3)

        tracker.current_step = 3
        tracker._render_progress("Step 3", "Completing...", False)
        time.sleep(0.3)

        tracker.complete("Done!")


if __name__ == "__main__":
    demo_progress()
