# Agent Workflow & Mutual Review Process

## Overview

This document describes the agent-based workflow for implementing features in the NUVIEW Strategic Pipeline, including cross-checks, integration points, and mutual review requirements.

## Agent Roles & Responsibilities

### Agent 1: Pipeline Operations
**Focus:** Core pipeline functionality, scraping, data processing

**Responsibilities:**
- Implement and maintain scraper modules
- Ensure data collection integrity
- Optimize scraping performance
- Handle multi-language support
- Implement bathymetry exclusion logic

**Deliverables:**
- Functional scrapers (34+ agencies)
- Multi-language regex patterns
- Deterministic JSON output
- Source verification

**Review Tags:** `agent1-pipeline`, `scraper-update`, `data-collection`

### Agent 2: Dashboard & Visualization
**Focus:** User interface, dashboard enhancements, visualizations

**Responsibilities:**
- Implement dashboard features
- Create interactive visualizations (Cytoscape)
- Ensure responsive design
- Implement auto-refresh functionality
- Add priority scoring matrix UI

**Deliverables:**
- Enhanced dashboard pages
- Interactive network diagrams
- Priority scoring matrix table
- Collapsible detail sections

**Review Tags:** `agent2-dashboard`, `ui-update`, `visualization`

### Agent 3: QA, Testing & Final Merge
**Focus:** Quality assurance, testing, integration validation

**Responsibilities:**
- Implement test coverage
- Run integration tests
- Validate end-to-end workflows
- Ensure security standards
- Perform final merge

**Deliverables:**
- Comprehensive test suite
- Integration test framework
- Security validation
- Final merged codebase

**Review Tags:** `agent3-qa`, `testing`, `integration`, `final-merge`

## Branch Strategy

### Sequential Branch Flow
```
main
  ├── agent1-pipeline          # Agent 1 work
  │   └── agent2-dashboard     # Agent 2 builds on Agent 1
  │       └── agent3-final-qc  # Agent 3 validates all
  │           └── merge to main
```

### Alternative: Parallel with Integration Branch
```
main
  ├── agent1-pipeline
  ├── agent2-dashboard
  ├── agent3-qa
  └── integration              # All agents merge here for validation
      └── merge to main
```

## Integration Points & Cross-Checks

### 1. Schema Validation (Agent 1 → Agent 2 → Agent 3)

**Agent 1 Output:**
- `schemas/opportunities.json` - JSON Schema definition
- Validated data structure in `data/opportunities.json`

**Agent 2 Dependency:**
- Dashboard must render data matching schema
- UI fields must align with schema properties

**Agent 3 Validation:**
- Run schema validation tests
- Verify all data files pass schema checks
- Test: `test_schema_validation_works()`

**Integration Test:**
```bash
python -m pytest tests/test_integration.py::TestPipelineIntegration::test_schema_validation_works -v
```

### 2. Priority Scoring (Agent 1 → Agent 2)

**Agent 1 Output:**
- `calculate_priority_score()` function in `generate_programs.py`
- Priority scores calculated for all opportunities
- `data/processed/priority_matrix.csv` generated

**Agent 2 Dependency:**
- Display priority scores in dashboard
- Show scoring methodology
- Render priority matrix table

**Agent 3 Validation:**
- Verify priority scores are within valid range (0-85)
- Test scoring calculation logic
- Tests: `TestPriorityScoring` class

**Integration Test:**
```bash
python -m pytest tests/test_integration.py::TestPriorityScoring -v
```

### 3. Dashboard Data Flow (Agent 1 → Agent 2 → Agent 3)

**Agent 1 Output:**
- `data/processed/programs.json` with categorized opportunities
- Auto-generated via `generate_programs.py`

**Agent 2 Dependency:**
- Dashboard fetches and renders `programs.json`
- Auto-refresh every 5 minutes
- Cytoscape visualization uses programs data

**Agent 3 Validation:**
- Test data file structure
- Verify dashboard can load data
- End-to-end workflow validation
- Tests: `TestPipelineIntegration` class

**Integration Test:**
```bash
python -m pytest tests/test_integration.py::TestPipelineIntegration -v
```

### 4. Workflow Integration (All Agents)

**Agent 1 Output:**
- Updated `.github/workflows/daily_ops.yml` with scrape job

**Agent 2 Input:**
- Workflow must trigger dashboard updates

**Agent 3 Enhancement:**
- Add lint/test job to workflow
- Ensure all jobs have proper dependencies
- Validate workflow syntax

**Integration Test:**
```bash
# Locally validate workflow syntax
yamllint .github/workflows/daily_ops.yml

# Validate dependencies
grep "needs:" .github/workflows/daily_ops.yml
```

## Mutual Review Requirements

### Pull Request Template

Each agent PR must include:

1. **Title Format:** `[AgentX] Feature Description`
   - Example: `[Agent1] Add multi-language regex for topographic keywords`

2. **Description Sections:**
   - **Objective:** What was implemented
   - **Changes:** List of modified files
   - **Testing:** Tests added/run
   - **Integration Points:** Dependencies on other agents
   - **Review Tags:** Appropriate labels

3. **Required Checks:**
   - [ ] All tests pass locally
   - [ ] Code follows style guidelines (ruff)
   - [ ] Integration tests pass
   - [ ] Documentation updated
   - [ ] No security vulnerabilities (CodeQL)

### Review Tags for PRs

| Tag | Purpose | Required Reviewers |
|-----|---------|-------------------|
| `agent1-pipeline` | Agent 1 changes | Agent 2, Agent 3 |
| `agent2-dashboard` | Agent 2 changes | Agent 1, Agent 3 |
| `agent3-qa` | Agent 3 changes | Agent 1, Agent 2 |
| `integration-required` | Cross-agent dependency | All agents |
| `final-merge` | Ready for main | All agents + maintainer |

### Review Checklist

**For Agent 1 (Pipeline) Reviews:**
- [ ] Scrapers collect all required fields
- [ ] Data conforms to schema
- [ ] Multi-language support working
- [ ] Bathymetry exclusion logic correct
- [ ] Source verification implemented
- [ ] Output is deterministic

**For Agent 2 (Dashboard) Reviews:**
- [ ] Dashboard renders all data fields
- [ ] Interactive features work (zoom, pan, click)
- [ ] Auto-refresh functioning
- [ ] Priority matrix displays correctly
- [ ] Collapsible sections toggle properly
- [ ] Responsive design maintained

**For Agent 3 (QA) Reviews:**
- [ ] All integration tests pass
- [ ] No regressions in existing tests
- [ ] Workflow syntax valid
- [ ] Security scans clean
- [ ] Documentation complete
- [ ] End-to-end validation successful

## End-to-End Validation Process

### Step 1: Local Validation

Each agent must run before submitting PR:

```bash
# Run all tests
python -m pytest tests/ -v

# Run linter
python -m ruff check .

# Run QC validator
python scripts/qc_validator.py

# Generate programs
python scripts/generate_programs.py

# Verify output files
ls -la data/processed/
```

### Step 2: Integration Testing

Before merge to main:

```bash
# Run full integration test suite
python -m pytest tests/test_integration.py -v

# Test workflow locally (if possible)
act -j lint-test  # Using nektos/act

# Verify schema validation
python -c "
from jsonschema import validate
import json
with open('schemas/opportunities.json') as f: schema = json.load(f)
with open('data/opportunities.json') as f: data = json.load(f)
validate(instance=data, schema=schema)
print('Schema validation passed')
"
```

### Step 3: Cross-Agent Review

1. **Agent 1 → Agent 2:** Verify data structure matches dashboard needs
2. **Agent 2 → Agent 3:** Provide UI test cases for validation
3. **Agent 3 → Agent 1:** Report any data quality issues found in testing

### Step 4: Final Merge Approval

Required approvals before merge to main:
- ✅ All integration tests pass
- ✅ All agents have reviewed changes
- ✅ Security scan (CodeQL) passes
- ✅ Workflow runs successfully in CI
- ✅ Documentation updated

## Communication Channels

### GitHub Issues
- Use for feature requests and bugs
- Tag with agent labels
- Link related PRs

### Pull Request Comments
- Use for code-specific discussions
- Request changes with clear action items
- Approve when satisfied

### Project Board
- Track progress across agents
- Use columns: To Do, In Progress, Review, Done
- Assign issues to agents

## Troubleshooting Integration Issues

### Data Schema Mismatch
**Symptom:** Dashboard fails to render or shows errors
**Solution:**
1. Check `schemas/opportunities.json`
2. Validate data: `python scripts/qc_validator.py`
3. Verify dashboard code uses correct field names

### Priority Scoring Issues
**Symptom:** Scores out of range or missing
**Solution:**
1. Check `calculate_priority_score()` in `generate_programs.py`
2. Run: `python scripts/generate_programs.py`
3. Verify: `cat data/processed/priority_matrix.csv`

### Workflow Failures
**Symptom:** CI/CD pipeline fails
**Solution:**
1. Check workflow syntax: `yamllint .github/workflows/daily_ops.yml`
2. Verify job dependencies are correct
3. Check logs in GitHub Actions UI

### Test Failures
**Symptom:** Integration tests fail
**Solution:**
1. Run locally: `python -m pytest tests/test_integration.py -v`
2. Check data files exist and are valid
3. Verify all scripts run successfully

## Best Practices

1. **Always run tests before pushing**
2. **Update documentation with code changes**
3. **Use descriptive commit messages**
4. **Tag PRs appropriately for visibility**
5. **Respond to reviews within 24 hours**
6. **Don't merge without all approvals**
7. **Keep branches up-to-date with main**
8. **Use draft PRs for work-in-progress**

## Maintenance Schedule

- **Daily:** Automated scraping and QC validation
- **Weekly:** Manual review of flagged opportunities
- **Monthly:** Security audit and dependency updates
- **Quarterly:** Full system review and optimization

---

**Last Updated:** 2025-11-21  
**Version:** 1.0.0  
**Maintainer:** NUVIEW Team
