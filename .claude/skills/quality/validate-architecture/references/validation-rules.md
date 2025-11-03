# Validation Rules and Scoring Criteria

Comprehensive validation rules, scoring criteria, and decision matrices for architecture validation.

---

## Overall Scoring

### Weighted Score Calculation

```
Overall Score = (Completeness × 0.25) + (Tech Justification × 0.20) +
                (NFRs × 0.20) + (Security × 0.15) +
                (Scalability × 0.10) + (Documentation × 0.10)
```

### Pass/Fail Thresholds

| Score | Result | Action |
|-------|--------|--------|
| 85-100 | PASS (Excellent) | Proceed to implementation |
| 70-84 | PASS (Good) | Address recommendations, proceed |
| 50-69 | FAIL (Needs Work) | Fix critical + high priority, re-validate |
| 0-49 | FAIL (Inadequate) | Major rework required |

---

## Dimension 1: Completeness (Weight: 25%)

**Scoring:**
```
Score = (Sections Present / Required Sections) × 100
```

### Required Sections (All Project Types)

| Section | Weight | Description |
|---------|--------|-------------|
| System Overview | 15% | Purpose, goals, context |
| Architecture Diagrams | 20% | Visual representation (min 1 diagram) |
| Technology Stack | 20% | Complete list of technologies |
| Data Architecture | 15% | Data model, database selection |
| Deployment Architecture | 10% | Hosting, CI/CD |
| Security Architecture | 10% | Auth, encryption, compliance |
| ADRs | 10% | Minimum 3 decision records |

### Frontend-Specific Sections

| Section | Weight | Description |
|---------|--------|-------------|
| Component Architecture | 20% | Component design, hierarchy |
| State Management | 15% | Client/server state approach |
| Routing Strategy | 10% | Navigation, route design |
| Styling Approach | 10% | CSS strategy |

### Backend-Specific Sections

| Section | Weight | Description |
|---------|--------|-------------|
| API Design | 20% | REST/GraphQL/RPC patterns |
| Service Architecture | 15% | Monolith/microservices |
| Data Layer | 15% | ORM, queries, caching |
| Integration Patterns | 10% | External system connections |

### Full Stack-Specific Sections

| Section | Weight | Description |
|---------|--------|-------------|
| Frontend Architecture | 15% | UI patterns |
| Backend Architecture | 15% | API/service patterns |
| Integration | 15% | Frontend ↔ Backend communication |
| Authentication | 10% | Auth strategy |

---

## Dimension 2: Technology Justification (Weight: 20%)

**Scoring:**
```
Score = (Technologies with Justification / Total Technologies) × 100
```

### Justification Quality Rubric

| Quality | Score | Criteria |
|---------|-------|----------|
| Excellent | 100% | Rationale + alternatives + tradeoffs + data/benchmarks |
| Good | 75% | Rationale + alternatives + tradeoffs |
| Fair | 50% | Rationale only (no alternatives) |
| Poor | 25% | Vague or missing rationale |
| None | 0% | Technology listed without justification |

### Required Justifications

**Must justify for 100% score:**
- Primary framework (React, Next.js, Express, etc.)
- Database selection
- Authentication method
- API design pattern
- Hosting/deployment platform
- Major libraries (>10KB impact)

**Example - Excellent Justification:**
```
Database: PostgreSQL
Rationale: Relational model fits our data (users, teams, projects with joins).
Alternatives: MongoDB (rejected: poor join performance), MySQL (good but less features)
Tradeoffs: Schema migrations vs flexibility (acceptable for data consistency)
Benchmarks: 45ms vs 180ms for complex queries (PostgreSQL vs MongoDB)
Decision: ADR-001
```

**Example - Poor Justification:**
```
Database: MongoDB
Rationale: It's popular and scalable.
```

---

## Dimension 3: NFRs Coverage (Weight: 20%)

**Scoring:**
```
NFRs Addressed = Count of NFRs with concrete architecture decisions
Score = (NFRs Addressed / Required NFRs) × 100
```

### Required NFRs

| NFR | How to Address | Score Impact |
|-----|----------------|--------------|
| Performance | Response time targets, caching strategy, optimization | 25% |
| Scalability | Growth projections, scaling plan, bottlenecks | 25% |
| Security | Auth, encryption, input validation | 25% |
| Reliability | Availability target, redundancy, failover | 15% |
| Maintainability | Code organization, testing, docs | 10% |

### NFR Scoring Rubric

**Performance (25% of NFR score):**
- ✅ Excellent (100%): Specific targets (p95 <500ms), caching strategy, CDN, optimization plan
- ⚠️ Good (75%): General targets, basic caching
- ❌ Fair (50%): Vague ("should be fast")
- ❌ Poor (0%): Not addressed

**Scalability (25% of NFR score):**
- ✅ Excellent (100%): Growth projections, horizontal scaling plan, database scaling, bottleneck analysis
- ⚠️ Good (75%): General scaling approach, some projections
- ❌ Fair (50%): Vague ("will scale")
- ❌ Poor (0%): Not addressed

**Security (25% of NFR score):**
- ✅ Excellent (100%): Auth method, authorization model, encryption (rest+transit), compliance
- ⚠️ Good (75%): Auth + basic encryption
- ❌ Fair (50%): Auth only
- ❌ Poor (0%): Not addressed

**Reliability (15% of NFR score):**
- ✅ Excellent (100%): Availability target (99.9%), redundancy, failover, DR plan
- ⚠️ Good (75%): Basic redundancy mentioned
- ❌ Fair (50%): Vague ("highly available")
- ❌ Poor (0%): Not addressed

**Maintainability (10% of NFR score):**
- ✅ Excellent (100%): Testing strategy, code org principles, CI/CD, documentation plan
- ⚠️ Good (75%): Testing mentioned
- ❌ Fair (50%): Vague
- ❌ Poor (0%): Not addressed

---

## Dimension 4: Security & Compliance (Weight: 15%)

**Scoring:**
```
Score = (Security Elements Addressed / Required Elements) × 100
```

### Required Security Elements

| Element | Required | Score Weight |
|---------|----------|--------------|
| Authentication | Yes | 30% |
| Authorization | Yes | 25% |
| Data Encryption | Yes | 20% |
| Input Validation | Yes | 10% |
| Security Testing | Recommended | 5% |
| Compliance (if applicable) | Yes | 10% |

### Security Scoring Rubric

**Authentication (30%):**
- ✅ Excellent: Method specified (OAuth/JWT/etc), provider/library, session management
- ⚠️ Good: Method specified
- ❌ Fair: Vague ("users can log in")
- ❌ Poor: Not addressed

**Authorization (25%):**
- ✅ Excellent: Model documented (RBAC/ABAC), roles defined, resource permissions
- ⚠️ Good: Basic model mentioned
- ❌ Fair: Vague
- ❌ Poor: Not addressed

**Data Encryption (20%):**
- ✅ Excellent: At-rest AND in-transit, key management approach
- ⚠️ Good: HTTPS mentioned
- ❌ Fair: Vague
- ❌ Poor: Not addressed

**Compliance (10%):**
- ✅ Excellent: Specific compliance (GDPR/HIPAA/etc), how requirements met
- ⚠️ Good: Compliance mentioned
- ❌ Fair: Vague
- ❌ Poor: Not addressed (when required)

---

## Dimension 5: Scalability Planning (Weight: 10%)

**Scoring:**
```
Score = (Scaling Elements Addressed / Required Elements) × 100
```

### Required Scaling Elements

| Element | Weight | Description |
|---------|--------|-------------|
| Growth Projections | 30% | User/data growth estimates |
| Horizontal Scaling Plan | 30% | How to add capacity |
| Database Scaling | 20% | Reads/writes scaling approach |
| Bottleneck Identification | 20% | Known limits and mitigations |

### Scaling Quality Rubric

**Growth Projections (30%):**
- ✅ Excellent: Specific numbers (10K → 100K users in 12 months), data volume estimates
- ⚠️ Good: General growth expectations
- ❌ Fair: Vague ("expect to grow")
- ❌ Poor: Not addressed

**Horizontal Scaling (30%):**
- ✅ Excellent: Stateless services, load balancer, auto-scaling, specific triggers
- ⚠️ Good: Stateless services mentioned
- ❌ Fair: Vague ("will scale horizontally")
- ❌ Poor: Not addressed

**Database Scaling (20%):**
- ✅ Excellent: Read replicas, sharding plan, connection pooling
- ⚠️ Good: Read replicas mentioned
- ❌ Fair: Vague
- ❌ Poor: Not addressed

**Bottlenecks (20%):**
- ✅ Excellent: Identified bottlenecks, thresholds, mitigation plans
- ⚠️ Good: Some bottlenecks mentioned
- ❌ Fair: Generic concerns
- ❌ Poor: Not addressed

---

## Dimension 6: Documentation Quality (Weight: 10%)

**Scoring:**
```
Score = (Quality Indicators Met / Total Indicators) × 100
```

### Quality Indicators

| Indicator | Weight | Criteria |
|-----------|--------|----------|
| Clarity | 30% | Clear, unambiguous language |
| Diagrams | 25% | Visual representations present |
| Examples | 20% | Concrete examples provided |
| Completeness | 15% | All sections filled out |
| Formatting | 10% | Proper markdown, readable |

### Documentation Quality Rubric

**Clarity (30%):**
- ✅ Excellent: Technical but readable, no jargon, well-structured
- ⚠️ Good: Mostly clear, some ambiguity
- ❌ Fair: Confusing sections
- ❌ Poor: Unclear throughout

**Diagrams (25%):**
- ✅ Excellent: 3+ diagrams (context, container, deployment)
- ⚠️ Good: 1-2 diagrams
- ❌ Fair: 1 diagram, poor quality
- ❌ Poor: No diagrams

**Examples (20%):**
- ✅ Excellent: Code snippets, configuration examples, API samples
- ⚠️ Good: Some examples
- ❌ Fair: Few examples
- ❌ Poor: No examples

---

## ADR Quality Validation

### Minimum ADR Count

| Complexity | Minimum ADRs |
|------------|--------------|
| Simple (0-30) | 3 ADRs |
| Medium (31-60) | 5 ADRs |
| Complex (61-100) | 10 ADRs |

### ADR Quality Checklist

**Per ADR:**
- [ ] Has date and status
- [ ] Context explains problem
- [ ] Decision stated clearly
- [ ] 2+ alternatives considered
- [ ] Rationale provided
- [ ] Consequences (positive + negative) documented

**ADR Score:**
```
Score = (Checklist Items Met / 6) × 100 per ADR
Overall ADR Quality = Average of all ADR scores
```

---

## Critical Issues Classification

### What Makes an Issue Critical?

**Critical (Must Fix):**
- Missing required sections (System Overview, Tech Stack, ADRs)
- Zero security considerations
- No deployment plan
- Technologies with no justification
- < 3 ADRs present
- Contradictory decisions

**High Priority (Should Fix):**
- Vague NFR coverage
- Missing scaling strategy
- Incomplete security (e.g., auth but no authorization)
- Poor ADR quality (missing alternatives)
- No cost estimates

**Medium Priority (Nice to Fix):**
- Missing diagrams
- Limited examples
- Unclear documentation
- No monitoring strategy

**Low Priority (Optional):**
- Formatting issues
- Minor clarifications needed

---

## Decision Matrix

### PASS Criteria

**Minimum requirements:**
- Overall score ≥ 70
- Completeness ≥ 70%
- Security ≥ 60%
- Zero critical issues

**Can proceed to implementation with:**
- Score 70-84: Address high priority recommendations during development
- Score 85+: Minor improvements only

### FAIL Criteria

**Must re-validate if:**
- Overall score < 70
- Completeness < 70%
- Security < 60%
- Any critical issues present

**Automatic FAIL (regardless of score):**
- Missing System Overview
- Zero security considerations
- < 3 ADRs (for medium+ complexity)
- No technology justifications

---

## Example Scoring

### Example 1: Well-Documented Architecture

```
Completeness: 90% (all sections present, detailed)
Tech Justification: 85% (most technologies justified with alternatives)
NFRs: 80% (performance, scalability, security covered)
Security: 90% (auth, encryption, compliance addressed)
Scalability: 75% (scaling plan present, some gaps)
Documentation: 85% (clear, diagrams, examples)

Overall: (90×0.25) + (85×0.20) + (80×0.20) + (90×0.15) + (75×0.10) + (85×0.10)
       = 22.5 + 17 + 16 + 13.5 + 7.5 + 8.5 = 85/100

Result: PASS (Excellent) ✅
```

### Example 2: Incomplete Architecture

```
Completeness: 60% (missing deployment, security sections)
Tech Justification: 40% (few justifications, no alternatives)
NFRs: 30% (vague performance mentions, no scalability)
Security: 20% (minimal auth mention, no encryption)
Scalability: 10% (not addressed)
Documentation: 50% (no diagrams, unclear)

Overall: (60×0.25) + (40×0.20) + (30×0.20) + (20×0.15) + (10×0.10) + (50×0.10)
       = 15 + 8 + 6 + 3 + 1 + 5 = 38/100

Result: FAIL (Inadequate) ❌
Critical Issues: 5 (missing sections, no security, no scaling, no ADRs)
```

---

*Reference for validate-architecture skill - Use these rules for consistent, objective architecture validation*
