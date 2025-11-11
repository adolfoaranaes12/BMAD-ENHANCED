#!/usr/bin/env python3
"""
BMAD Enhanced - Interactive Command Wizard
Helps users select the right subagent and command for their task.
"""

import sys
from typing import Dict, List, Tuple

# ANSI color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Command database with metadata
COMMANDS = {
    "orchestrator": {
        "name": "Orchestrator",
        "description": "Coordinates complete workflows across multiple subagents",
        "doc": "docs/quickstart-orchestrator.md",
        "commands": {
            "*workflow": {
                "description": "Execute complete end-to-end workflow",
                "use_when": [
                    "Delivering a complete feature from requirement to PR",
                    "Breaking down an epic into sprint-ready stories",
                    "Executing an entire sprint",
                    "Coordinating multiple phases automatically"
                ],
                "example": "*workflow --type=feature-delivery --requirement='Add user authentication'",
                "complexity": "High",
                "duration": "30-120 minutes"
            },
            "*coordinate": {
                "description": "Coordinate specific cross-subagent tasks",
                "use_when": [
                    "Need sequential execution (Plan → Implement → Review)",
                    "Need parallel execution of independent tasks",
                    "Need iterative refinement between subagents",
                    "Have a custom coordination pattern"
                ],
                "example": "*coordinate --pattern=sequential --tasks='create-task-spec,implement,review'",
                "complexity": "Medium-High",
                "duration": "15-60 minutes"
            }
        }
    },
    "alex": {
        "name": "Alex (Planner)",
        "description": "Planning, estimation, and requirement analysis",
        "doc": "docs/quickstart-alex.md",
        "commands": {
            "*create-task-spec": {
                "description": "Create detailed task specification",
                "use_when": [
                    "Starting a new feature or task",
                    "Need detailed acceptance criteria",
                    "Want implementation guidance",
                    "Creating a task for James to implement"
                ],
                "example": "*create-task-spec --title='User Authentication' --requirement='Users need to log in'",
                "complexity": "Low-Medium",
                "duration": "5-15 minutes"
            },
            "*breakdown-epic": {
                "description": "Break epic into user stories",
                "use_when": [
                    "Have a large feature to decompose",
                    "Need sprint-sized stories",
                    "Want story hierarchy",
                    "Planning a release"
                ],
                "example": "*breakdown-epic --epic='E-commerce checkout system'",
                "complexity": "Medium",
                "duration": "10-20 minutes"
            },
            "*estimate": {
                "description": "Estimate story points and effort",
                "use_when": [
                    "Sprint planning",
                    "Need effort estimates",
                    "Prioritizing work",
                    "Resource allocation"
                ],
                "example": "*estimate --story='Implement payment gateway' --context='Using Stripe API'",
                "complexity": "Low-Medium",
                "duration": "5-10 minutes"
            },
            "*refine-story": {
                "description": "Add detail and acceptance criteria to story",
                "use_when": [
                    "Story is too vague",
                    "Missing acceptance criteria",
                    "Need more technical detail",
                    "Backlog refinement session"
                ],
                "example": "*refine-story --story='User can reset password'",
                "complexity": "Low",
                "duration": "5-10 minutes"
            },
            "*plan-sprint": {
                "description": "Create sprint plan from stories",
                "use_when": [
                    "Starting a new sprint",
                    "Allocating stories to sprint",
                    "Need capacity planning",
                    "Setting sprint goals"
                ],
                "example": "*plan-sprint --stories='story1.md,story2.md' --capacity=40",
                "complexity": "Medium",
                "duration": "10-20 minutes"
            }
        }
    },
    "james": {
        "name": "James (Developer)",
        "description": "Implementation, testing, and debugging",
        "doc": "docs/quickstart-james.md",
        "commands": {
            "*implement": {
                "description": "Implement features from specifications",
                "use_when": [
                    "Have a task spec ready",
                    "Starting feature development",
                    "Following TDD approach",
                    "Need production-ready code"
                ],
                "example": "*implement --spec=.claude/tasks/task-001-spec.md --tdd=true",
                "complexity": "Medium-High",
                "duration": "15-60 minutes"
            },
            "*fix": {
                "description": "Fix bugs with root cause analysis",
                "use_when": [
                    "Bug is reproducible",
                    "Need systematic debugging",
                    "Want root cause analysis",
                    "Regression prevention"
                ],
                "example": "*fix --issue='Login fails with special characters' --reproduce-steps='steps.md'",
                "complexity": "Medium",
                "duration": "10-30 minutes"
            },
            "*test": {
                "description": "Run tests and analyze results",
                "use_when": [
                    "After implementation",
                    "Before committing",
                    "CI/CD pipeline",
                    "Regression testing"
                ],
                "example": "*test --scope=unit --coverage-threshold=80",
                "complexity": "Low-Medium",
                "duration": "5-15 minutes"
            },
            "*refactor": {
                "description": "Improve code structure without changing behavior",
                "use_when": [
                    "Code smells detected",
                    "Reducing technical debt",
                    "Improving maintainability",
                    "Before adding new features"
                ],
                "example": "*refactor --target=src/auth.py --focus='Extract method, reduce complexity'",
                "complexity": "Medium",
                "duration": "10-30 minutes"
            },
            "*apply-qa-fixes": {
                "description": "Apply fixes from QA review",
                "use_when": [
                    "After Quinn's review",
                    "Have quality gate concerns",
                    "Need to address review comments",
                    "Iterating on quality"
                ],
                "example": "*apply-qa-fixes --review=.claude/quality/review-20250104.md",
                "complexity": "Low-Medium",
                "duration": "10-20 minutes"
            },
            "*debug": {
                "description": "Debug complex issues with analysis",
                "use_when": [
                    "Bug is intermittent or complex",
                    "Need deep investigation",
                    "Multiple potential causes",
                    "Performance issues"
                ],
                "example": "*debug --issue='Memory leak in background worker' --logs=worker.log",
                "complexity": "Medium-High",
                "duration": "15-45 minutes"
            },
            "*explain": {
                "description": "Explain code functionality and design",
                "use_when": [
                    "Onboarding new developers",
                    "Understanding legacy code",
                    "Documentation needed",
                    "Code review preparation"
                ],
                "example": "*explain --file=src/payment/processor.py --focus='Payment flow'",
                "complexity": "Low",
                "duration": "5-10 minutes"
            }
        }
    },
    "quinn": {
        "name": "Quinn (Quality)",
        "description": "Quality review, NFR assessment, and risk analysis",
        "doc": "docs/quickstart-quinn.md",
        "commands": {
            "*review": {
                "description": "Comprehensive quality review",
                "use_when": [
                    "After feature implementation",
                    "Before PR submission",
                    "Quality gate checkpoint",
                    "Release readiness check"
                ],
                "example": "*review --target=feature/user-auth --scope=comprehensive",
                "complexity": "Medium-High",
                "duration": "15-30 minutes"
            },
            "*assess-nfr": {
                "description": "Assess non-functional requirements",
                "use_when": [
                    "Security concerns",
                    "Performance requirements",
                    "Scalability assessment",
                    "Reliability/maintainability check"
                ],
                "example": "*assess-nfr --categories='security,performance' --target=src/api",
                "complexity": "Medium",
                "duration": "10-20 minutes"
            },
            "*validate-quality-gate": {
                "description": "Make quality gate decision (PASS/CONCERNS/FAIL)",
                "use_when": [
                    "Before merging to main",
                    "Release go/no-go decision",
                    "Sprint acceptance",
                    "Production deployment approval"
                ],
                "example": "*validate-quality-gate --target=feature/payment --threshold=80",
                "complexity": "Medium",
                "duration": "10-15 minutes"
            },
            "*trace-requirements": {
                "description": "Verify requirement implementation",
                "use_when": [
                    "Acceptance testing",
                    "Compliance verification",
                    "Requirement sign-off",
                    "Feature completeness check"
                ],
                "example": "*trace-requirements --spec=task-spec.md --implementation=src/",
                "complexity": "Low-Medium",
                "duration": "10-15 minutes"
            },
            "*assess-risk": {
                "description": "Identify and score implementation risks",
                "use_when": [
                    "Before major changes",
                    "New technology adoption",
                    "Complex features",
                    "Risk mitigation planning"
                ],
                "example": "*assess-risk --change='Migrate to microservices' --scope=architecture",
                "complexity": "Medium",
                "duration": "10-20 minutes"
            }
        }
    }
}

# Goal-based recommendations
GOAL_MAPPING = {
    "plan": {
        "keywords": ["plan", "planning", "requirement", "spec", "story", "epic", "estimate", "sprint"],
        "subagent": "alex",
        "recommended_commands": ["*create-task-spec", "*breakdown-epic", "*plan-sprint"]
    },
    "implement": {
        "keywords": ["implement", "code", "develop", "build", "create", "feature", "tdd"],
        "subagent": "james",
        "recommended_commands": ["*implement", "*test"]
    },
    "fix": {
        "keywords": ["fix", "bug", "issue", "problem", "error", "broken", "debug"],
        "subagent": "james",
        "recommended_commands": ["*fix", "*debug", "*test"]
    },
    "improve": {
        "keywords": ["refactor", "improve", "optimize", "clean", "debt", "technical debt"],
        "subagent": "james",
        "recommended_commands": ["*refactor", "*test"]
    },
    "review": {
        "keywords": ["review", "quality", "check", "assess", "evaluate", "validate"],
        "subagent": "quinn",
        "recommended_commands": ["*review", "*validate-quality-gate"]
    },
    "nfr": {
        "keywords": ["security", "performance", "scalability", "reliability", "nfr", "non-functional"],
        "subagent": "quinn",
        "recommended_commands": ["*assess-nfr", "*assess-risk"]
    },
    "workflow": {
        "keywords": ["workflow", "end-to-end", "complete", "orchestrate", "coordinate", "automate"],
        "subagent": "orchestrator",
        "recommended_commands": ["*workflow", "*coordinate"]
    },
    "understand": {
        "keywords": ["understand", "explain", "documentation", "onboard", "learn"],
        "subagent": "james",
        "recommended_commands": ["*explain"]
    }
}


def print_header(text: str):
    """Print formatted header"""
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'=' * 70}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}{text.center(70)}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'=' * 70}{Colors.ENDC}\n")


def print_section(text: str):
    """Print section header"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}{text}{Colors.ENDC}")
    print(f"{Colors.BLUE}{'-' * len(text)}{Colors.ENDC}")


def print_command(subagent: str, command: str, details: Dict):
    """Print formatted command details"""
    print(f"\n{Colors.BOLD}{Colors.GREEN}Command: {command}{Colors.ENDC}")
    print(f"{Colors.YELLOW}Description:{Colors.ENDC} {details['description']}")
    print(f"{Colors.YELLOW}Complexity:{Colors.ENDC} {details['complexity']}")
    print(f"{Colors.YELLOW}Duration:{Colors.ENDC} {details['duration']}")

    print(f"\n{Colors.YELLOW}Use when:{Colors.ENDC}")
    for use_case in details['use_when']:
        print(f"  • {use_case}")

    print(f"\n{Colors.YELLOW}Example:{Colors.ENDC}")
    print(f"  {Colors.CYAN}{details['example']}{Colors.ENDC}")


def recommend_by_goal(goal: str) -> Tuple[str, List[str]]:
    """Recommend subagent and commands based on user goal"""
    goal_lower = goal.lower()

    # Check each goal category
    for category, mapping in GOAL_MAPPING.items():
        if any(keyword in goal_lower for keyword in mapping['keywords']):
            return mapping['subagent'], mapping['recommended_commands']

    # Default to showing all options
    return None, []


def interactive_mode():
    """Run interactive wizard"""
    print_header("BMAD Enhanced - Command Wizard")

    print(f"{Colors.BOLD}Welcome to the BMAD Enhanced Command Wizard!{Colors.ENDC}")
    print("This tool helps you find the right command for your task.\n")

    # Step 1: Get user goal
    print(f"{Colors.BOLD}What would you like to do?{Colors.ENDC}")
    print("(Describe your goal in a few words, e.g., 'implement a new feature', 'fix a bug', 'review code')")
    print(f"{Colors.YELLOW}> {Colors.ENDC}", end="")

    try:
        user_goal = input().strip()
    except (EOFError, KeyboardInterrupt):
        print("\n\nExiting wizard.")
        return

    if not user_goal:
        print(f"\n{Colors.RED}No input provided. Exiting.{Colors.ENDC}")
        return

    # Step 2: Get recommendations
    recommended_subagent, recommended_commands = recommend_by_goal(user_goal)

    if recommended_subagent:
        print_section(f"Recommendation for: '{user_goal}'")

        subagent_info = COMMANDS[recommended_subagent]
        print(f"\n{Colors.BOLD}Recommended Subagent:{Colors.ENDC} {Colors.GREEN}{subagent_info['name']}{Colors.ENDC}")
        print(f"{Colors.YELLOW}Description:{Colors.ENDC} {subagent_info['description']}")
        print(f"{Colors.YELLOW}Documentation:{Colors.ENDC} {subagent_info['doc']}")

        print(f"\n{Colors.BOLD}Recommended Commands:{Colors.ENDC}")

        for i, cmd in enumerate(recommended_commands, 1):
            if cmd in subagent_info['commands']:
                cmd_details = subagent_info['commands'][cmd]
                print(f"\n{Colors.BOLD}[{i}] {cmd}{Colors.ENDC}")
                print(f"    {cmd_details['description']}")
                print(f"    {Colors.CYAN}{cmd_details['example']}{Colors.ENDC}")

        # Step 3: Ask if user wants more details
        print(f"\n{Colors.BOLD}Would you like to:{Colors.ENDC}")
        print("  1. See detailed information about a command")
        print("  2. Browse all commands")
        print("  3. Exit")
        print(f"{Colors.YELLOW}Choice (1-3): {Colors.ENDC}", end="")

        try:
            choice = input().strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\nExiting wizard.")
            return

        if choice == "1":
            print(f"{Colors.YELLOW}Enter command number (1-{len(recommended_commands)}): {Colors.ENDC}", end="")
            try:
                cmd_num = int(input().strip())
                if 1 <= cmd_num <= len(recommended_commands):
                    cmd = recommended_commands[cmd_num - 1]
                    print_command(recommended_subagent, cmd, subagent_info['commands'][cmd])
                else:
                    print(f"{Colors.RED}Invalid command number.{Colors.ENDC}")
            except (ValueError, EOFError, KeyboardInterrupt):
                print(f"\n{Colors.RED}Invalid input.{Colors.ENDC}")
        elif choice == "2":
            browse_all_commands()
        else:
            print("\nExiting wizard.")
    else:
        print(f"\n{Colors.YELLOW}No specific recommendation found. Showing all available commands.{Colors.ENDC}")
        browse_all_commands()

    # Final message
    print(f"\n{Colors.BOLD}{Colors.GREEN}For more information, see:{Colors.ENDC}")
    print(f"  • Documentation Index: {Colors.CYAN}docs/DOCUMENTATION-INDEX.md{Colors.ENDC}")
    print(f"  • Quick Start Guides: {Colors.CYAN}docs/quickstart-*.md{Colors.ENDC}")
    print(f"  • V2 Architecture: {Colors.CYAN}docs/V2-ARCHITECTURE.md{Colors.ENDC}\n")


def browse_all_commands():
    """Browse all available commands"""
    print_section("All Available Commands")

    for subagent_key, subagent_info in COMMANDS.items():
        print(f"\n{Colors.BOLD}{Colors.GREEN}► {subagent_info['name']}{Colors.ENDC}")
        print(f"  {subagent_info['description']}")
        print(f"  {Colors.CYAN}{subagent_info['doc']}{Colors.ENDC}")

        for cmd, details in subagent_info['commands'].items():
            print(f"\n  {Colors.BOLD}{cmd}{Colors.ENDC}")
            print(f"    {details['description']}")
            print(f"    {Colors.YELLOW}Complexity:{Colors.ENDC} {details['complexity']} | {Colors.YELLOW}Duration:{Colors.ENDC} {details['duration']}")


def list_by_subagent(subagent: str):
    """List commands for a specific subagent"""
    if subagent not in COMMANDS:
        print(f"{Colors.RED}Error: Unknown subagent '{subagent}'{Colors.ENDC}")
        print(f"Available subagents: {', '.join(COMMANDS.keys())}")
        return

    subagent_info = COMMANDS[subagent]
    print_section(f"{subagent_info['name']} Commands")

    print(f"{Colors.BOLD}Description:{Colors.ENDC} {subagent_info['description']}")
    print(f"{Colors.BOLD}Documentation:{Colors.ENDC} {subagent_info['doc']}\n")

    for cmd, details in subagent_info['commands'].items():
        print_command(subagent, cmd, details)


def show_help():
    """Show help message"""
    print_header("BMAD Enhanced - Command Wizard Help")

    print(f"{Colors.BOLD}Usage:{Colors.ENDC}")
    print(f"  python .claude/skills/bmad-commands/scripts/bmad-wizard.py [options]\n")

    print(f"{Colors.BOLD}Options:{Colors.ENDC}")
    print(f"  {Colors.CYAN}(no arguments){Colors.ENDC}     Run interactive wizard")
    print(f"  {Colors.CYAN}--list-all{Colors.ENDC}         List all commands")
    print(f"  {Colors.CYAN}--subagent <name>{Colors.ENDC}  Show commands for specific subagent")
    print(f"  {Colors.CYAN}--help{Colors.ENDC}             Show this help message\n")

    print(f"{Colors.BOLD}Available Subagents:{Colors.ENDC}")
    for key, info in COMMANDS.items():
        print(f"  {Colors.CYAN}{key:15}{Colors.ENDC} - {info['name']}")

    print(f"\n{Colors.BOLD}Examples:{Colors.ENDC}")
    print(f"  python .claude/skills/bmad-commands/scripts/bmad-wizard.py")
    print(f"  python .claude/skills/bmad-commands/scripts/bmad-wizard.py --list-all")
    print(f"  python .claude/skills/bmad-commands/scripts/bmad-wizard.py --subagent alex")


def main():
    """Main entry point"""
    if len(sys.argv) == 1:
        # No arguments - run interactive mode
        interactive_mode()
    elif "--help" in sys.argv or "-h" in sys.argv:
        show_help()
    elif "--list-all" in sys.argv:
        browse_all_commands()
    elif "--subagent" in sys.argv:
        try:
            idx = sys.argv.index("--subagent")
            subagent = sys.argv[idx + 1]
            list_by_subagent(subagent)
        except IndexError:
            print(f"{Colors.RED}Error: --subagent requires an argument{Colors.ENDC}")
            show_help()
    else:
        print(f"{Colors.RED}Error: Unknown option{Colors.ENDC}")
        show_help()


if __name__ == "__main__":
    main()
