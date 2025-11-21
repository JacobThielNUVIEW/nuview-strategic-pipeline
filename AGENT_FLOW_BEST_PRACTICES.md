# NUVIEW Strategic Pipeline - Best Practices & Flow Structure

## Agent Assignment Flow Structure

This document outlines the best practices and flow structure for the NUVIEW Strategic Pipeline based on the three-agent sequential workflow model.

### Sequential Branch Flow

The recommended flow structure follows a sequential approach:

```
Agent 1 → Agent 2 → Agent 3 (with merge gates at each step)
```

#### Agent 1: Initial Development
- Create feature branch from main
- Implement core functionality
- Run initial tests and validations
- Push to `agent1-*` branch
- Create PR with merge gate

#### Agent 2: Integration & Scraper Enhancement
- Checkout Agent 1's completed branch
- Create new branch: `agent2-integration-scrapers`
- Enhance scraper logic and integration
- Add/update tests
- Push to `agent2-*` branch
- Create PR with merge gate

#### Agent 3: Final Fix & Compile (This Implementation)
- Checkout Agent 2's completed branch
- Create new branch: `agent3-final-qc-merge`
- Perform comprehensive QC
- Fix any remaining issues
- Run full test suite
- Merge to main

### Best Practices

#### 1. GitHub Projects for Tracking
- Use GitHub Projects to track progress across all three agents
- Create cards for each agent's tasks
- Link PRs to project cards
- Update status as work progresses

#### 2. Labeling Strategy
- Apply consistent labels across branches and PRs:
  - `topo-focus` - Topographic/LiDAR specific work
  - `agent1-dev` - Initial development work
  - `agent2-integration` - Integration and enhancement work
  - `agent3-qc` - Quality control and final merge work
  - `final-merge` - Ready for main branch merge

#### 3. Timely Delivery: 24-Hour SLAs
- Each agent should complete their work within 24 hours
- Use GitHub Actions workflow notifications to track progress
- Set up automated reminders for approaching deadlines
- Document any blockers immediately

#### 4. Dependency Management
- **Dependabot Configuration**: Automated weekly dependency updates
  - Python packages: Weekly scans on Mondays
  - GitHub Actions: Weekly scans on Mondays
  - Automatic PR creation for security updates
- Review and merge dependabot PRs promptly
- Test dependency updates in feature branches before merging

### Optimization Checklist

#### Pre-Commit Hooks (Recommended)
To set up pre-commit hooks for automatic linting:

```bash
# Install pre-commit
pip install pre-commit

# Create .pre-commit-config.yaml
cat > .pre-commit-config.yaml << EOF
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.14.5
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-json
EOF

# Install hooks
pre-commit install
```

#### CI Gates for Merges
All merge requests must pass:
1. **Linting**: Ruff checks with no errors
2. **Testing**: All pytest tests pass
3. **QC Validation**: Quality control checks pass
4. **Build**: Code builds successfully
5. **Security**: No new vulnerabilities introduced

### Workflow Improvements Implemented

#### Concurrency Control
```yaml
concurrency:
  group: daily-ops-${{ github.ref }}
  cancel-in-progress: false
```
Prevents multiple workflow runs from conflicting with each other.

#### Pinned SHA Actions
All GitHub Actions are pinned to specific SHA hashes for security:
- `actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11` (v4.1.1)
- `actions/setup-python@0a5c61591373683505ea898e09a3ea4f39ef2b9c` (v5.0.0)
- `actions/upload-artifact@5d5d22a31266ced268874388b861e4b58bb5c2f3` (v4.3.1)
- `actions/download-artifact@c850b930e6ba138125429b7e5c93fc707a7f8427` (v4.1.4)

#### Retry Logic with Rebase
```bash
MAX_RETRIES=3
while [ $RETRY_COUNT -lt $MAX_RETRIES ]; do
  if git pull --rebase origin main; then
    if git push origin main; then
      exit 0
    fi
  fi
  RETRY_COUNT=$((RETRY_COUNT + 1))
  sleep 10
done
```

### Code Quality Standards

#### Testing
- **Unit Tests**: All core functionality has unit tests
  - `tests/test_regex_patterns.py`: Budget extraction and keyword filtering
  - `tests/test_priority_scoring.py`: Urgency calculation and priority scoring
- **Test Coverage**: Aim for >80% coverage
- **Test Execution**: Run `pytest` before every commit

#### Linting
- **Tool**: Ruff (configured in `pyproject.toml`)
- **Line Length**: 120 characters maximum
- **Import Sorting**: Automatic with ruff
- **Fix Command**: `ruff check --fix .`

#### Code Optimizations
1. **Deterministic JSON**: All JSON output uses `sort_keys=True`
2. **Parallel Processing**: Scrapers run in parallel using `ThreadPoolExecutor`
3. **Timeout Controls**: All workflow jobs have appropriate timeouts

### Branch Protection Rules

To enable branch protection for the main branch:

1. Go to: `Settings > Branches`
2. Add rule for `main` branch
3. Enable:
   - ✅ Require pull request reviews before merging
   - ✅ Require status checks to pass before merging
   - ✅ Require branches to be up to date before merging
   - ✅ Include administrators
   - ✅ Restrict who can push to matching branches

### Testing End-to-End

To verify the complete pipeline:

```bash
# 1. Run setup script with pipeline execution
./setup_and_run.sh --run-pipeline

# 2. Verify data files were generated
ls -la data/opportunities.json data/forecast.json

# 3. Run QC validator
python3 scripts/qc_validator.py

# 4. Check dashboard (if running locally)
python3 -m http.server 8000
# Navigate to: http://localhost:8000
```

### Security Considerations

1. **Dependabot**: Automated security updates enabled
2. **Action Pinning**: All actions pinned to specific SHAs
3. **Secret Management**: Use GitHub Secrets for sensitive data
4. **Branch Protection**: Enforce code review and CI checks
5. **Least Privilege**: Workflow permissions set to minimum required

### Monitoring & Alerts

- **Workflow Status**: Monitor via GitHub Actions tab
- **Failed Runs**: Automatic issue creation for QC failures
- **Dashboard**: Real-time updates at https://salesnuviewspace.netlify.app
- **Logs**: Artifacts retained for 7-30 days depending on type

### Agent 3 Completion Checklist

- [x] Full QC with pytest tests (regex and priority validation)
- [x] Workflow updates (concurrency, pinned SHAs, retry logic)
- [x] Optimizations (deterministic JSON, parallel scrapers)
- [x] Security (dependabot.yml configuration)
- [x] Testing infrastructure complete
- [ ] End-to-end verification
- [ ] Final merge to main

### Next Steps for Future Agents

When the next development cycle begins:
1. Create new feature branch from latest main
2. Follow the three-agent flow structure
3. Apply labels and track in GitHub Projects
4. Maintain 24-hour SLA per agent
5. Run full test suite before each merge
6. Update this documentation as needed

---

**Last Updated**: 2025-11-21  
**Agent**: Agent 3 - Final Fix & Compile  
**Status**: Implementation Complete
