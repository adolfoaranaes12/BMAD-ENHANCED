# Command Routing Test Cases

**Date:** January 15, 2025
**Status:** Test Documentation Complete
**Purpose:** Verify command routing system works correctly

---

## Test Environment

**Files Required:**
- ✅ `.claude/skills/router.md` - Command router skill
- ✅ `.claude/commands/alex.md` - Alex slash command
- ✅ `.claude/commands/james.md` - James slash command
- ✅ `.claude/commands/quinn.md` - Quinn slash command
- ✅ `.claude/commands/orchestrator.md` - Orchestrator slash command
- ✅ `.claude/subagents/alex-planner.md` - Alex subagent definition
- ✅ `.claude/subagents/james-developer.md` - James subagent definition
- ✅ `.claude/subagents/quinn-quality.md` - Quinn subagent definition
- ✅ `.claude/subagents/orchestrator.md` - Orchestrator definition

**All files verified and in place!**

---

## Test Cases

### Test 1: Valid Command - Alex Breakdown

**Input:**
```
Use .claude/skills/router.md with command "@alex *breakdown 'User Authentication System'"
```

**Alternative (Slash Command):**
```
/alex breakdown "User Authentication System"
```

**Expected Behavior:**
1. ✅ Parse command successfully
   - subagent: "alex"
   - command: "breakdown"
   - args: "User Authentication System"
2. ✅ Map to file: `.claude/subagents/alex-planner.md`
3. ✅ Find command mapping: `*breakdown` → `.claude/skills/planning/breakdown-epic.md`
4. ✅ Invoke skill with args
5. ✅ Return epic breakdown with user stories

**Status:** Should Pass ✅

---

### Test 2: Valid Command - James Implement

**Input:**
```
Use .claude/skills/router.md with command "@james *implement task-auth-002"
```

**Alternative (Slash Command):**
```
/james implement task-auth-002
```

**Expected Behavior:**
1. ✅ Parse command successfully
   - subagent: "james"
   - command: "implement"
   - args: "task-auth-002"
2. ✅ Map to file: `.claude/subagents/james-developer.md`
3. ✅ Find command mapping: `*implement` → `.claude/skills/development/implement-feature.md`
4. ✅ Invoke skill with task ID
5. ✅ Execute TDD workflow and return implementation

**Status:** Should Pass ✅

---

### Test 3: Valid Command - Quinn Review

**Input:**
```
Use .claude/skills/router.md with command "@quinn *review task-auth-002"
```

**Alternative (Slash Command):**
```
/quinn review task-auth-002
```

**Expected Behavior:**
1. ✅ Parse command successfully
   - subagent: "quinn"
   - command: "review"
   - args: "task-auth-002"
2. ✅ Map to file: `.claude/subagents/quinn-quality.md`
3. ✅ Find command mapping: `*review` → `.claude/skills/quality/review-task.md`
4. ✅ Invoke skill with task ID
5. ✅ Execute quality review and return assessment

**Status:** Should Pass ✅

---

### Test 4: Valid Command - Orchestrator Deliver

**Input:**
```
Use .claude/skills/router.md with command "@orchestrator *deliver 'User login feature'"
```

**Alternative (Slash Command):**
```
/orchestrator deliver "User login feature"
```

**Expected Behavior:**
1. ✅ Parse command successfully
   - subagent: "orchestrator"
   - command: "deliver"
   - args: "User login feature"
2. ✅ Map to file: `.claude/subagents/orchestrator.md`
3. ✅ Find command mapping: `*deliver` → `.claude/skills/implementation/deliver-feature.md`
4. ✅ Invoke skill with feature name
5. ✅ Execute full delivery workflow

**Status:** Should Pass ✅

---

### Test 5: Invalid Syntax - Missing Asterisk

**Input:**
```
Use .claude/skills/router.md with command "@alex breakdown 'Epic'"
```

**Expected Error:**
```
❌ Invalid Command Syntax

Input: "@alex breakdown Epic"
Issue: Missing asterisk (*) before command

Expected format: @<subagent> *<command> <args>
Correct syntax: "@alex *breakdown Epic"

Examples:
  @alex *breakdown "User Authentication"
  @james *implement task-001
  @quinn *review task-001
```

**Status:** Should Fail Gracefully ✅

---

### Test 6: Unknown Subagent

**Input:**
```
Use .claude/skills/router.md with command "@bob *test 'something'"
```

**Expected Error:**
```
❌ Unknown Subagent: @bob

Available subagents:
  • @alex - Planning and estimation
  • @james - Development and implementation
  • @quinn - Quality assurance and review
  • @orchestrator - Workflow coordination

Did you mean: @james?
```

**Status:** Should Fail Gracefully ✅

---

### Test 7: Unknown Command

**Input:**
```
Use .claude/skills/router.md with command "@alex *deploy 'something'"
```

**Expected Error:**
```
❌ Unknown Command: *deploy

Subagent: @alex (Planner)

Available commands:
  • *breakdown - Break down epic into user stories
  • *estimate - Estimate story points for story
  • *sprint - Create sprint plan
  • *refine - Refine and improve story
  • *plan - Create detailed task specification

Did you mean: *plan?
```

**Status:** Should Fail Gracefully ✅

---

### Test 8: Special Command - Help

**Input:**
```
Use .claude/skills/router.md with command "@help"
```

**Expected Output:**
```
# BMAD Enhanced Command Reference

## Available Subagents

### @alex (Planner)
Commands:
  • *breakdown <epic> - Break down epic into user stories
  • *estimate <story> - Estimate story points
  • *sprint <stories> - Create sprint plan
  • *refine <story> - Refine story
  • *plan <story> - Create task specification

### @james (Developer)
Commands:
  • *implement <task-id> - Implement feature using TDD
  • *fix <issue> - Fix bug or issue
  • *test <scope> - Run tests and coverage
  • *refactor <code> - Refactor code
  • *debug <issue> - Debug problem
  • *coverage - Analyze test coverage

### @quinn (Quality)
Commands:
  • *review <task-id> - Review implementation
  • *audit <code> - Audit code quality
  • *security <code> - Security audit
  • *performance <code> - Performance analysis
  • *accessibility <code> - Accessibility check
  • *report <task-id> - Generate quality report

### @orchestrator (Coordinator)
Commands:
  • *deliver <feature> - Full delivery workflow

## Usage Examples

Basic syntax: @<subagent> *<command> <args>

Examples:
  @alex *breakdown "User Authentication System"
  @james *implement task-auth-002
  @quinn *review task-auth-002
  @orchestrator *deliver "User login feature"

## Slash Command Shortcuts

You can also use slash commands:
  /alex breakdown "Epic"
  /james implement task-001
  /quinn review task-001
  /orchestrator deliver "Feature"
```

**Status:** Should Pass ✅

---

### Test 9: Special Command - Subagent Help

**Input:**
```
Use .claude/skills/router.md with command "@alex *help"
```

**Expected Output:**
```
# @alex (Planner) - Command Reference

## Available Commands

### *breakdown <epic>
**Skill:** `.claude/skills/planning/breakdown-epic.md`
**Purpose:** Break down epic into user stories
**Example:** `@alex *breakdown "User Authentication System"`

### *estimate <story>
**Skill:** `.claude/skills/planning/estimate-story.md`
**Purpose:** Estimate story points for story
**Example:** `@alex *estimate story-auth-001`

### *sprint <stories>
**Skill:** `.claude/skills/planning/create-sprint-plan.md`
**Purpose:** Create sprint plan from stories
**Example:** `@alex *sprint story-001 story-002 story-003`

### *refine <story>
**Skill:** `.claude/skills/planning/refine-story.md`
**Purpose:** Refine and improve story details
**Example:** `@alex *refine story-auth-001`

### *plan <story>
**Skill:** `.claude/skills/planning/create-task-spec.md`
**Purpose:** Create detailed task specification
**Example:** `@alex *plan story-auth-001`

## Usage Tips

- Use quotes for multi-word arguments: `"User Authentication"`
- All commands start with asterisk: `*command`
- Get general help: `@help`
- Get version info: `@version`
```

**Status:** Should Pass ✅

---

### Test 10: Special Command - Version

**Input:**
```
Use .claude/skills/router.md with command "@version"
```

**Expected Output:**
```
# BMAD Enhanced - System Information

**Version:** 1.0.0
**Status:** Production Ready
**Date:** January 15, 2025

## Components

**Subagents:** 4
  • Alex (Planner)
  • James (Developer)
  • Quinn (Quality)
  • Orchestrator (Coordinator)

**Skills:** 18
  • Planning: 5 skills
  • Development: 3 skills
  • Quality: 6 skills
  • Implementation: 1 skill
  • Routing: 1 skill
  • Templates: 2 skills

**Total Lines of Code:** 40,300+

## Time Savings
  • Before BMAD: 10-17 hours per feature
  • After BMAD: 48-63 minutes per feature
  • Savings: 85-90%

## Support
  • Documentation: `/home/adolfo/Documents/BMAD Enhanced/docs/`
  • Issue Tracker: GitHub
  • Help Command: `@help`
```

**Status:** Should Pass ✅

---

## Integration Tests

### Integration Test 1: Full Planning Workflow

**Commands:**
```
1. /alex breakdown "User Authentication System"
2. /alex estimate story-auth-001
3. /alex plan story-auth-001
```

**Expected:**
- Epic broken into stories
- Story estimated with points
- Task specification created

**Status:** Should Pass ✅

---

### Integration Test 2: Full Development Workflow

**Commands:**
```
1. /james implement task-auth-002
2. /james test
3. /quinn review task-auth-002
```

**Expected:**
- Feature implemented with TDD
- Tests run with coverage report
- Quality review completed

**Status:** Should Pass ✅

---

### Integration Test 3: Full Delivery Workflow

**Commands:**
```
1. /orchestrator deliver "User login feature"
```

**Expected:**
- Alex breaks down epic
- Alex creates task specs
- James implements each task
- Quinn reviews each task
- System reports completion

**Status:** Should Pass ✅

---

## Performance Tests

### Performance Test 1: Router Overhead

**Measurement:** Time difference between direct skill invocation vs router

**Baseline (Direct):**
```
Use .claude/skills/planning/breakdown-epic.md with input "Epic"
```

**Router:**
```
Use .claude/skills/router.md with command "@alex *breakdown 'Epic'"
```

**Expected Overhead:** < 1 second
**Status:** Should be negligible

---

### Performance Test 2: Slash Command Overhead

**Baseline (Router):**
```
Use .claude/skills/router.md with command "@alex *breakdown 'Epic'"
```

**Slash Command:**
```
/alex breakdown "Epic"
```

**Expected Overhead:** < 0.5 seconds (just command parsing)
**Status:** Should be negligible

---

## Error Recovery Tests

### Error Recovery Test 1: Typo Correction

**Input:**
```
@alex *breakdwon "Epic"
```

**Expected:**
```
❌ Unknown Command: *breakdwon

Did you mean: *breakdown?
```

**Status:** Should suggest correction ✅

---

### Error Recovery Test 2: Case Sensitivity

**Input:**
```
@ALEX *BREAKDOWN "Epic"
```

**Expected:**
Either:
- Accept (case-insensitive parsing)
- OR suggest: "Did you mean: @alex *breakdown?"

**Status:** Should handle gracefully ✅

---

## Test Summary

**Total Test Cases:** 10 basic + 3 integration + 2 performance + 2 error recovery = 17

**Expected Results:**
- Valid commands: 4 should pass ✅
- Invalid commands: 3 should fail gracefully ✅
- Special commands: 3 should pass ✅
- Integration tests: 3 should pass ✅
- Performance tests: 2 should pass ✅
- Error recovery: 2 should pass ✅

**Overall Status:** All tests should pass! ✅

---

## Manual Testing Instructions

### Step 1: Test Basic Routing
```
Use .claude/skills/router.md with command "@alex *breakdown 'Test Epic'"
```

Expected: Should invoke breakdown-epic.md skill

---

### Step 2: Test Slash Command
```
/alex breakdown "Test Epic"
```

Expected: Should route through alex.md → router.md → breakdown-epic.md

---

### Step 3: Test Error Handling
```
Use .claude/skills/router.md with command "@invalid *test"
```

Expected: Should show helpful error message with available subagents

---

### Step 4: Test Help System
```
Use .claude/skills/router.md with command "@help"
```

Expected: Should display complete command reference

---

### Step 5: Test Integration
```
/orchestrator deliver "Test Feature"
```

Expected: Should execute full workflow across all subagents

---

## Automated Testing (Future)

**When available, create automated tests for:**

1. **Unit Tests** (router.test.ts)
   - Test command parsing
   - Test subagent mapping
   - Test error handling
   - Test special commands

2. **Integration Tests** (router-integration.test.ts)
   - Test full workflows
   - Test subagent coordination
   - Test skill execution

3. **Performance Tests** (router-performance.test.ts)
   - Measure routing overhead
   - Measure memory usage
   - Stress test with many commands

---

## Troubleshooting

### Problem: "Subagent file not found"

**Solution:**
- Verify `.claude/subagents/` contains all 4 subagent files
- Check file names match exactly (alex-planner.md, james-developer.md, etc.)

---

### Problem: "Skill file not found"

**Solution:**
- Verify skill path in subagent file is correct
- Check skill file exists at specified path
- Ensure path starts with `.claude/skills/`

---

### Problem: "Command not found"

**Solution:**
- Verify command name matches exactly (case-sensitive)
- Check subagent file has command mapping
- Ensure asterisk (*) is present in input

---

### Problem: "Slash command not working"

**Solution:**
- Verify `.claude/commands/` contains slash command files
- Check Claude Code recognizes slash commands
- Try using router.md directly as fallback

---

## Conclusion

**Command routing system is ready for testing!**

**Files Created:**
- ✅ router.md skill (command routing logic)
- ✅ alex.md, james.md, quinn.md, orchestrator.md (slash commands)

**Next Steps:**
1. Perform manual testing with test cases above
2. Fix any issues discovered
3. Document actual test results
4. Update documentation with lessons learned

---

*Test documentation created: January 15, 2025*
*Status: Ready for Testing*
*Estimated Testing Time: 30 minutes*
