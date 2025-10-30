# Coverage Analysis Guide

## Purpose

Parse coverage data, generate reports, and check against thresholds.

---

## Coverage Metrics

### Four Key Metrics

**1. Statement Coverage**
- Percentage of code statements executed
- Target: ≥80%

**2. Branch Coverage**
- Percentage of conditional branches tested
- Target: ≥80%

**3. Function Coverage**
- Percentage of functions called
- Target: ≥80%

**4. Line Coverage**
- Percentage of code lines executed
- Target: ≥80%

---

## Parsing Coverage from bmad-commands

### Coverage Response

```json
{
  "outputs": {
    "coverage_percent": 91.25,
    "coverage_details": {
      "statements": { "covered": 210, "total": 230, "percent": 91.3 },
      "branches": { "covered": 45, "total": 52, "percent": 86.5 },
      "functions": { "covered": 28, "total": 28, "percent": 100 },
      "lines": { "covered": 208, "total": 228, "percent": 91.2 }
    },
    "files": [
      {
        "file": "src/controllers/auth.controller.ts",
        "statements": 92.31,
        "branches": 87.50,
        "functions": 100,
        "lines": 92.31,
        "uncovered_lines": [45, 46, 47, 48, 67]
      }
    ]
  }
}
```

### Extract Coverage

```typescript
const { coverage_percent, coverage_details, files } = outputs;

console.log(`Overall Coverage: ${coverage_percent}%`);
console.log(`Statements: ${coverage_details.statements.percent}%`);
console.log(`Branches: ${coverage_details.branches.percent}%`);
```

---

## Generating Coverage Reports

### Text Report

```
File                  | % Stmts | % Branch | % Funcs | % Lines | Uncovered Lines
----------------------|---------|----------|---------|---------|----------------
auth.controller.ts    |   92.31 |    87.50 |     100 |   92.31 | 45-48,67
auth.service.ts       |   90.48 |    83.33 |     100 |   90.48 | 78,112-115
rate-limit.ts         |   88.89 |      100 |     100 |   88.89 | 23-25
jwt.ts                |     100 |      100 |     100 |     100 |
audit.ts              |   90.00 |    80.00 |     100 |   90.00 | 34-36,55
----------------------|---------|----------|---------|---------|----------------
Overall               |   91.25 |    88.42 |     100 |   91.25 |
```

### Summary Report

```markdown
## Coverage Summary

**Overall Coverage:** 91.25%

| Metric     | Coverage | Target | Status |
|------------|----------|--------|--------|
| Statements | 91.25%   | ≥80%   | ✅ Pass |
| Branches   | 88.42%   | ≥80%   | ✅ Pass |
| Functions  | 100%     | ≥80%   | ✅ Pass |
| Lines      | 91.25%   | ≥80%   | ✅ Pass |

**Status:** ✅ ALL THRESHOLDS MET
```

---

## Checking Thresholds

### Threshold Configuration

```yaml
thresholds:
  statements: 80
  branches: 80
  functions: 80
  lines: 80
```

### Validation Logic

```typescript
function checkThresholds(coverage, thresholds) {
  const results = {
    statements: coverage.statements.percent >= thresholds.statements,
    branches: coverage.branches.percent >= thresholds.branches,
    functions: coverage.functions.percent >= thresholds.functions,
    lines: coverage.lines.percent >= thresholds.lines
  };

  const allPass = Object.values(results).every(r => r === true);

  return { results, allPass };
}
```

### Report Threshold Status

```markdown
**Threshold Check:**
- ✅ Statements: 91.25% (≥80% required)
- ✅ Branches: 88.42% (≥80% required)
- ✅ Functions: 100% (≥80% required)
- ✅ Lines: 91.25% (≥80% required)

**Overall:** ✅ PASS
```

---

## Identifying Uncovered Lines

### Per-File Uncovered Lines

```json
{
  "file": "src/controllers/auth.controller.ts",
  "uncovered_lines": [45, 46, 47, 48, 67],
  "uncovered_ranges": ["45-48", "67"]
}
```

### Visual Representation

```typescript
40: export const login = async (req, res) => {
41:   try {
42:     const validationResult = loginSchema.safeParse(req.body);
43:     if (!validationResult.success) {
44:       return res.status(400).json({ error: 'Validation error' });
45:     }                                                              // ✅ Covered
46:
47:     // Database connection check
48:     if (!isDatabaseConnected()) {                                  // ❌ Line 48 uncovered
49:       return res.status(503).json({ error: 'Service unavailable' }); // ❌ Line 49 uncovered
50:     }                                                              // ❌ Line 50 uncovered
```

---

## Coverage Report Files

### Generated Files

```
coverage/
├── coverage-final.json      # Raw coverage data
├── lcov.info                # LCOV format (for CI/CD)
├── lcov-report/
│   ├── index.html           # HTML overview
│   ├── auth.controller.ts.html
│   └── auth.service.ts.html
└── coverage-summary.json    # Summary data
```

### HTML Report Usage

```markdown
📊 Coverage Report Generated

**HTML Report:** file:///path/to/coverage/lcov-report/index.html

**Visual indicators in HTML:**
- 🟢 Green lines: Covered
- 🔴 Red lines: Uncovered
- 🟡 Yellow lines: Partially covered (branches)

Open in browser for interactive line-by-line coverage view.
```

---

## Quick Reference

**Coverage Thresholds:**
- Minimum: 80% for all metrics
- Target: 85-90% for production code
- Excellent: 95%+ for critical code

**Interpreting Coverage:**
- <80%: Insufficient, add more tests
- 80-85%: Acceptable, look for critical gaps
- 85-95%: Good, minor gaps acceptable
- >95%: Excellent, very thorough

---

*Part of run-tests skill - Development Suite*
