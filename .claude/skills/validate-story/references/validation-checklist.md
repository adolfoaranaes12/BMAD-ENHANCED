# Validation Checklist

Detailed checklist for all 10 validation steps in validate-story skill.

---

## Step 1: Template Completeness Validation

### Required Sections Checklist

- [ ] **Frontmatter (YAML)**
  - [ ] Has `epic_id` field
  - [ ] Has `story_id` field
  - [ ] Has `title` field
  - [ ] Has `status` field
  - [ ] Has `created` date

- [ ] **Objective**
  - [ ] Section exists
  - [ ] Has content (≥ 1 sentence)
  - [ ] Clear and concise (1-3 sentences)
  - [ ] Answers "What does this story achieve?"

- [ ] **Context**
  - [ ] Section exists
  - [ ] Has meaningful content (≥ 3 sentences)
  - [ ] Explains why story is needed
  - [ ] Describes how it fits into epic/product

- [ ] **Acceptance Criteria**
  - [ ] Section exists
  - [ ] Has ≥ 1 acceptance criterion
  - [ ] Criteria are numbered (AC1, AC2, ...)
  - [ ] Each criterion is measurable
  - [ ] Each criterion is testable

- [ ] **Tasks/Subtasks**
  - [ ] Section exists
  - [ ] Has ≥ 1 task
  - [ ] Tasks are numbered
  - [ ] Hierarchical structure (if subtasks)
  - [ ] Each task is actionable

- [ ] **Dev Notes**
  - [ ] Section exists
  - [ ] Has substantial content (≥ 5 sentences)
  - [ ] Explains technical approach
  - [ ] Identifies key technical decisions
  - [ ] Documents integration points

- [ ] **Testing & Validation**
  - [ ] Section exists
  - [ ] Describes testing strategy
  - [ ] Lists test scenarios
  - [ ] Specifies validation steps
  - [ ] Names testing tools/framework

- [ ] **File List**
  - [ ] Section exists
  - [ ] Lists new files to create
  - [ ] Lists existing files to modify
  - [ ] Uses relative paths

- [ ] **Dependencies**
  - [ ] Section exists
  - [ ] Lists external dependencies (libraries, services)
  - [ ] Lists internal dependencies (other stories, tasks)
  - [ ] Identifies system dependencies

### Placeholder Detection

Search for and flag:

- [ ] `{{` + any text + `}}` (template variables)
- [ ] `_TBD_` or `[TBD]`
- [ ] `TODO` or `FIXME`
- [ ] `...` or `[more details needed]`
- [ ] `[placeholder]` or `{placeholder}`

### Content Quality

- [ ] No empty sections (sections must have > 2 lines)
- [ ] No sections with only placeholder text
- [ ] No copied template instructions
- [ ] Sections are story-specific (not generic)

---

## Step 2: File Structure and Source Tree Validation

### File Path Validation

For each file mentioned:

- [ ] **Path Format**
  - [ ] Uses forward slashes (`/`) not backslashes (`\`)
  - [ ] Relative to project root (not absolute)
  - [ ] No leading slash
  - [ ] No trailing slash (for files)

- [ ] **Path Structure**
  - [ ] Matches project structure (src/, tests/, docs/)
  - [ ] Correct directory depth
  - [ ] Consistent naming (camelCase, kebab-case, snake_case per project)

- [ ] **File Extensions**
  - [ ] Appropriate for file type (.ts, .js, .tsx, .vue, .md, .yaml)
  - [ ] Consistent across project (e.g., all .ts not mixed .ts/.js)

- [ ] **Test File Locations**
  - [ ] Test files in `tests/` directory
  - [ ] Test files mirror source structure
  - [ ] Test file naming convention (*.test.*, *.spec.*)

### Directory Validation

- [ ] **Directory Existence**
  - [ ] Referenced directories exist in project structure
  - [ ] No invented directories not in `docs/unified-project-structure.md`

- [ ] **Directory Consistency**
  - [ ] Same directory referenced consistently (no "src/auth" vs "src/authentication")
  - [ ] Case-sensitive matching

- [ ] **File Organization**
  - [ ] Related files in same directory
  - [ ] No mixing unrelated files
  - [ ] Follows project conventions

### Common Issues to Flag

- ❌ Windows paths: `src\auth\login.ts` → should be `src/auth/login.ts`
- ❌ Absolute paths: `/home/user/project/src/file.ts` → should be `src/file.ts`
- ❌ Invented directories: `src/services/auth/` when project uses `src/auth/`
- ❌ Test files in source: `src/api/user.test.ts` → should be `tests/api/user.test.ts`
- ❌ Wrong extensions: `login.javascript` → should be `login.js`

---

## Step 3: UI/Frontend Completeness (if applicable)

### Detect UI Story

Story is UI-related if it mentions:

- [ ] Keywords: UI, component, page, view, styling, responsive, layout
- [ ] File extensions: .tsx, .jsx, .vue, .html, .css, .scss
- [ ] Tasks mention frontend/UI work

### If UI Story, Validate:

#### Component Specifications

- [ ] **Component Names**
  - [ ] All components named
  - [ ] Component names follow project convention
  - [ ] Component hierarchy clear (parent/child relationships)

- [ ] **Component Props/Inputs**
  - [ ] Props documented for each component
  - [ ] Prop types specified
  - [ ] Required vs optional props clear

- [ ] **Component State**
  - [ ] State requirements identified
  - [ ] State management approach specified (local, global, store)

#### Styling and Design

- [ ] **Design Guidance**
  - [ ] Colors specified (or reference to design system)
  - [ ] Spacing/padding specified
  - [ ] Typography specified
  - [ ] Layout approach (flexbox, grid, etc.)

- [ ] **Responsive Behavior**
  - [ ] Mobile behavior specified
  - [ ] Tablet behavior specified
  - [ ] Desktop behavior specified
  - [ ] Breakpoints defined

- [ ] **Accessibility**
  - [ ] ARIA labels mentioned
  - [ ] Keyboard navigation specified
  - [ ] Screen reader support addressed
  - [ ] Color contrast requirements

#### User Interactions

- [ ] **User Flows**
  - [ ] Click handlers described
  - [ ] Navigation flows documented
  - [ ] Modal/dialog behavior specified

- [ ] **Form Handling**
  - [ ] Form fields identified
  - [ ] Validation rules specified
  - [ ] Submit behavior documented
  - [ ] Error handling specified

- [ ] **Error States**
  - [ ] Loading states defined
  - [ ] Error states defined
  - [ ] Empty states defined

#### Frontend-Backend Integration

- [ ] **API Integration**
  - [ ] API endpoints specified
  - [ ] Request/response formats documented
  - [ ] Error handling for API failures

- [ ] **Data Models**
  - [ ] Frontend data models match backend
  - [ ] Data transformation specified (if needed)

---

## Step 4: Acceptance Criteria Satisfaction

### AC Extraction

- [ ] All ACs extracted from "Acceptance Criteria" section
- [ ] Each AC has unique identifier (AC1, AC2, ...)
- [ ] Each AC is a complete sentence

### AC Testability

For each AC:

- [ ] **Measurable**
  - [ ] Has quantifiable success criteria
  - [ ] Can verify pass/fail objectively

- [ ] **Specific**
  - [ ] Not vague (avoid "should work well", "be good")
  - [ ] Clear behavior specified
  - [ ] Edge cases identified

- [ ] **Achievable**
  - [ ] Reasonable scope for single story
  - [ ] No impossible requirements
  - [ ] Dependencies available

### Task-AC Mapping

For each AC:

- [ ] **Has Implementing Tasks**
  - [ ] ≥ 1 task addresses this AC
  - [ ] Tasks are sufficient (cover happy path + errors + edge cases)

- [ ] **Complete Coverage**
  - [ ] All aspects of AC addressed by tasks
  - [ ] No gaps between AC and tasks

### Common Issues

- ❌ Vague AC: "System should be secure" → Specify: "User passwords hashed with bcrypt, salt rounds ≥10"
- ❌ Unmeasurable AC: "UI should look good" → Specify: "UI matches Figma design XYZ"
- ❌ No tasks for AC: AC3 listed but no tasks implement it
- ❌ Partial coverage: AC covers 3 scenarios but tasks only address 1

---

## Step 5: Validation and Testing Instructions

### Testing Section Validation

- [ ] **Testing Strategy**
  - [ ] Strategy described (unit, integration, e2e)
  - [ ] Test pyramid levels identified
  - [ ] Testing approach appropriate for story

- [ ] **Test Scenarios**
  - [ ] ≥ 1 test scenario per AC
  - [ ] Happy path scenarios
  - [ ] Error/failure scenarios
  - [ ] Edge case scenarios

- [ ] **Validation Steps**
  - [ ] Steps are specific (not "test it manually")
  - [ ] Steps are actionable
  - [ ] Steps verify each AC

- [ ] **Testing Tools**
  - [ ] Testing framework specified (Jest, Pytest, Mocha, etc.)
  - [ ] Testing libraries mentioned (React Testing Library, etc.)
  - [ ] Test runners identified (if applicable)

### Test Coverage

- [ ] **AC Coverage**
  - [ ] Every AC has test scenarios
  - [ ] Test scenarios sufficient to verify AC

- [ ] **Test Types**
  - [ ] Unit tests identified
  - [ ] Integration tests identified (if needed)
  - [ ] E2E tests identified (if needed)

### Test Data Requirements

- [ ] **Test Fixtures**
  - [ ] Test data needs identified
  - [ ] Fixture creation approach specified

- [ ] **Mocks/Stubs**
  - [ ] External dependencies to mock identified
  - [ ] Mocking approach specified

- [ ] **Test Environment**
  - [ ] Test environment specified (local, CI, staging)
  - [ ] Environment setup requirements

### Common Issues

- ❌ Vague testing: "Test manually" → Specify: "Run `npm test`, verify all 12 tests pass"
- ❌ Missing scenarios: No error case tests for API failures
- ❌ No tools: Doesn't specify Jest, Pytest, etc.
- ❌ Incomplete coverage: AC1 has tests, AC2-5 don't

---

## Step 6: Security Considerations (if applicable)

### Detect Security-Critical Story

Story is security-critical if it mentions:

- [ ] Keywords: auth, password, token, encryption, secure, permission, access, role
- [ ] Files: auth*, login*, password*, token*, encryption*, access-control*
- [ ] Tasks involve authentication, authorization, data protection

### If Security-Critical, Validate:

#### Authentication/Authorization

- [ ] **Authentication**
  - [ ] Auth method specified (OAuth, JWT, sessions, etc.)
  - [ ] Credential storage approach (hashing algorithm, salt rounds)
  - [ ] Login flow documented

- [ ] **Authorization**
  - [ ] Permission model specified
  - [ ] Role-based access control (if applicable)
  - [ ] Resource-level permissions

#### Data Protection

- [ ] **Encryption**
  - [ ] Data at rest encryption (if needed)
  - [ ] Data in transit (HTTPS/TLS)
  - [ ] Encryption algorithms specified

- [ ] **Sensitive Data**
  - [ ] Identifies what data is sensitive
  - [ ] Protection approach specified
  - [ ] No plaintext storage of secrets

#### Vulnerability Prevention

- [ ] **Input Validation**
  - [ ] Input validation requirements
  - [ ] Sanitization approach
  - [ ] Validation libraries specified

- [ ] **Common Vulnerabilities**
  - [ ] SQL injection prevention (parameterized queries)
  - [ ] XSS prevention (output encoding)
  - [ ] CSRF prevention (tokens)
  - [ ] Rate limiting (if API endpoints)

#### Compliance

- [ ] **Regulatory Requirements**
  - [ ] GDPR compliance (if EU users)
  - [ ] PCI-DSS compliance (if payment data)
  - [ ] HIPAA compliance (if healthcare data)

- [ ] **Security Best Practices**
  - [ ] Least privilege principle
  - [ ] Defense in depth
  - [ ] Secure defaults

### Common Security Issues

- ❌ No password hashing: Stores passwords plaintext
- ❌ Weak hashing: Uses MD5 or SHA1 instead of bcrypt/Argon2
- ❌ No input validation: Accepts user input without validation
- ❌ No rate limiting: API endpoints can be spammed
- ❌ Hardcoded secrets: JWT secret in code instead of env var

---

## Step 7: Tasks/Subtasks Sequence Validation

### Logical Order

- [ ] **Prerequisites First**
  - [ ] Setup tasks before implementation tasks
  - [ ] Model/schema creation before controller/service
  - [ ] Database migration before using new tables
  - [ ] Dependency installation before using libraries

- [ ] **No Circular Dependencies**
  - [ ] Task A doesn't depend on Task B which depends on Task A
  - [ ] Clear dependency chain (A → B → C, not A → B → C → A)

- [ ] **Implementation Before Testing**
  - [ ] Code implementation tasks before test creation (unless TDD)
  - [ ] Feature complete before integration tests

### Task Granularity

- [ ] **Not Too Broad**
  - [ ] Tasks are single-purpose
  - [ ] No "Implement entire X" (break down)
  - [ ] Each task completable in reasonable time

- [ ] **Not Too Fine**
  - [ ] Not too many micro-tasks
  - [ ] Tasks have meaningful scope
  - [ ] Avoid "Add semicolon" level tasks

- [ ] **Appropriate Size**
  - [ ] Most tasks 1-4 hours of work
  - [ ] Large tasks (>4 hours) broken into subtasks

### Task Completeness

- [ ] **All Steps Present**
  - [ ] No missing steps between tasks
  - [ ] Logical progression from start to finish
  - [ ] No assumed/implicit tasks

- [ ] **AC Coverage**
  - [ ] Every AC has implementing tasks
  - [ ] No orphaned tasks (not tied to any AC)

### Task Actionability

- [ ] **Clear Instructions**
  - [ ] Developer knows exactly what to do
  - [ ] No ambiguous language
  - [ ] Specific files/locations mentioned

- [ ] **Verifiable Completion**
  - [ ] Can determine when task is done
  - [ ] Completion criteria clear

### Common Issues

- ❌ Wrong order: "Create controller" before "Create model"
- ❌ Circular: Task 3 needs Task 5, Task 5 needs Task 3
- ❌ Too broad: "Implement authentication system" (100+ hours)
- ❌ Too fine: "Add import statement", "Add semicolon"
- ❌ Vague: "Implement as needed" → Specify: "Create User model with email, passwordHash, createdAt fields"

---

## Step 8: Anti-Hallucination Verification

### File/Directory Verification

For each file/directory mentioned:

- [ ] **Check Project Structure**
  - [ ] File path exists in `docs/unified-project-structure.md`
  - [ ] Directory exists in project
  - [ ] File naming matches project convention

- [ ] **Flag Invented Paths**
  - [ ] Files not in project structure
  - [ ] Directories not documented
  - [ ] Non-standard locations

### Library/Framework Verification

For each library/framework mentioned:

- [ ] **Check Dependencies**
  - [ ] Library in `package.json` (Node.js)
  - [ ] Library in `requirements.txt` (Python)
  - [ ] Library in `Gemfile` (Ruby)
  - [ ] Library in appropriate dependency file

- [ ] **Flag Hallucinated Libraries**
  - [ ] Libraries not in dependencies
  - [ ] Wrong library names
  - [ ] Deprecated/non-existent libraries

### API Endpoint Verification

For each API endpoint mentioned:

- [ ] **Check API Spec**
  - [ ] Endpoint documented in `docs/architecture/api-spec.md`
  - [ ] HTTP method correct
  - [ ] Path structure matches

- [ ] **Flag Invented Endpoints**
  - [ ] Endpoints not in API spec
  - [ ] Incorrect paths
  - [ ] Wrong HTTP methods

### Database Schema Verification

For each table/column mentioned:

- [ ] **Check Schema Docs**
  - [ ] Table exists in `docs/architecture/database-schema.md`
  - [ ] Columns exist in schema
  - [ ] Data types match

- [ ] **Flag Invented Schema**
  - [ ] Tables not in schema
  - [ ] Columns not documented
  - [ ] Wrong data types

### Architecture Pattern Verification

For each architecture pattern mentioned:

- [ ] **Check Architecture Docs**
  - [ ] Pattern documented in `docs/architecture/`
  - [ ] Pattern usage specified
  - [ ] Pattern matches project style

- [ ] **Flag Invented Patterns**
  - [ ] Patterns not in architecture docs
  - [ ] Contradicts documented architecture
  - [ ] Uses different pattern than specified

### Verification Sources

**Primary Sources (check these first):**
- `docs/unified-project-structure.md` - File/directory structure
- `package.json` / `requirements.txt` - Dependencies
- `docs/architecture/api-spec.md` - API endpoints
- `docs/architecture/database-schema.md` - Database schema
- `docs/architecture/*.md` - Architecture patterns

**Flag if Not Found:**
- ❌ File "src/services/auth.ts" not in project structure
- ❌ Library "stripe-sdk" not in package.json
- ❌ Endpoint "POST /api/users/login" not in API spec
- ❌ Table "user_sessions" not in schema docs
- ❌ Pattern "Event Sourcing" not in architecture docs

---

## Step 9: Dev Agent Implementation Readiness

### Self-Contained Context

- [ ] **All Technical Details in Story**
  - [ ] Developer doesn't need to read epic
  - [ ] Developer doesn't need to read architecture docs (basics)
  - [ ] Developer doesn't need to read other stories
  - [ ] All integration points explained in Dev Notes

- [ ] **Dev Notes Comprehensive**
  - [ ] Technical approach explained
  - [ ] Key implementation details provided
  - [ ] Integration points documented
  - [ ] Potential gotchas mentioned

### Clear Instructions

- [ ] **No Ambiguity**
  - [ ] Tasks use specific language
  - [ ] No "implement as needed" or "use best practices"
  - [ ] Technical choices specified (which library, which pattern)

- [ ] **Specific Choices**
  - [ ] Auth method specified (not "add authentication")
  - [ ] Library specified (not "use a library")
  - [ ] Pattern specified (not "use appropriate pattern")

### Complete Technical Context

- [ ] **Implementation Approach**
  - [ ] High-level approach explained
  - [ ] Key algorithms/logic described
  - [ ] Edge cases identified

- [ ] **Integration Points**
  - [ ] How this connects to existing code
  - [ ] Which modules/services to use
  - [ ] API contracts specified

- [ ] **Error Handling**
  - [ ] Error scenarios identified
  - [ ] Error handling approach specified
  - [ ] User-facing error messages described

### Readiness Scoring

**Score 9-10 (Excellent):**
- [ ] All context in story
- [ ] No ambiguous tasks
- [ ] Complete Dev Notes
- [ ] All integration points clear
- [ ] Developer can start immediately

**Score 7-8 (Good):**
- [ ] Most context in story
- [ ] Minor ambiguities (1-2)
- [ ] Dev Notes mostly complete
- [ ] Most integration points clear
- [ ] Developer may need minimal clarification

**Score 5-6 (Fair):**
- [ ] Some context missing
- [ ] Several ambiguous tasks (3-5)
- [ ] Dev Notes incomplete
- [ ] Some integration points unclear
- [ ] Developer needs clarification before starting

**Score 3-4 (Poor):**
- [ ] Significant context missing
- [ ] Many ambiguous tasks (6+)
- [ ] Dev Notes minimal
- [ ] Most integration points unclear
- [ ] Developer blocked without clarification

**Score 1-2 (Very Poor):**
- [ ] Critical context missing
- [ ] Most/all tasks ambiguous
- [ ] No Dev Notes
- [ ] No integration guidance
- [ ] Story not implementable

### Common Readiness Issues

- ❌ Vague: "Add authentication" → Specify: "Add JWT authentication using jsonwebtoken library, 1-hour expiry, refresh tokens in Redis"
- ❌ Missing approach: No Dev Notes → Add: Technical implementation approach, key files, integration points
- ❌ Ambiguous: "Use best practices" → Specify: "Follow REST best practices: use HTTP status codes 200/201/400/401/500"
- ❌ No integration: Doesn't explain how this connects to existing auth system

---

## Quick Reference

### Critical Issues (Auto NO-GO)

1. Missing required section (Objective, AC, Tasks, Testing, File List)
2. Unfilled placeholders ({{var}}, _TBD_)
3. Uncovered AC (AC with no implementing tasks)
4. Hallucinated file/directory not in project
5. Hallucinated library not in dependencies
6. Circular task dependencies
7. No testing section
8. Readiness score < 5

### Should-Fix Issues

1. Incomplete UI specs (for UI stories)
2. Missing security considerations (for auth stories)
3. Vague testing instructions
4. Poor task granularity
5. Incomplete Dev Notes
6. Missing error handling guidance
7. Inconsistent file structure

### Nice-to-Have

1. Additional test scenarios
2. More detailed Dev Notes
3. Better task descriptions
4. Performance considerations
5. Scalability notes

---
