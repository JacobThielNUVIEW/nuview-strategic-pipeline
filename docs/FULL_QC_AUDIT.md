# Full Quality Control (QC) Audit System

## Overview

The Full QC Audit System is a comprehensive automated tool that validates the integrity, quality, and correctness of all files and components within the NUVIEW Strategic Pipeline repository.

## Features

### 1. **HTML Validation**
- Syntax checking
- Structure validation (DOCTYPE, html, head, body tags)
- Charset declaration verification
- Tag matching (div tags)
- File encoding validation

### 2. **Python Code Validation**
- Syntax checking for all Python files
- Style checking using Ruff linter
- PEP 8 compliance verification
- Import statement validation

### 3. **Shell Script Validation**
- Shellcheck integration for bash scripts
- Syntax error detection
- Best practices verification
- Common pitfall identification

### 4. **JSON File Validation**
- JSON syntax validation
- Structure integrity checks
- Empty file detection
- Encoding validation

### 5. **CSV File Validation**
- CSV parsing validation
- Duplicate header detection
- Null value identification
- Row and column count verification

### 6. **Documentation Quality Checks**
- Markdown file validation
- Header presence verification
- Content length checks
- File encoding validation

### 7. **Data Integrity Checks**
- Integration with existing qc_validator.py
- Integration with comprehensive_qc_check.py
- Calculation verification
- Cross-reference validation

### 8. **Recent Updates & Regression Detection**
- Git status checking
- Recent commit analysis
- Merge conflict detection
- Whitespace error detection

## Usage

### Running the Full QC Audit

```bash
# Run the complete QC audit
python scripts/full_qc_audit.py
```

### Output

The audit generates:
1. **Console Output**: Real-time progress and results with color-coded messages
2. **JSON Report**: Detailed findings saved to `data/processed/full_qc_audit_report.json`

### Exit Codes

- `0`: QC Audit PASSED - All checks successful or minor warnings only
- `1`: QC Audit FAILED - Critical issues detected that need resolution

## Report Structure

The generated JSON report includes:

```json
{
  "timestamp": "ISO 8601 timestamp",
  "audit_type": "Full QC Audit",
  "results": {
    "HTML Files": {
      "errors": [],
      "warnings": [],
      "files_checked": 0
    },
    "Python Files": {...},
    "Shell Scripts": {...},
    "JSON Files": {...},
    "CSV Files": {...},
    "Documentation": {...},
    "Data Integrity": {...},
    "Recent Updates": {...}
  },
  "summary": {
    "total_errors": 0,
    "total_warnings": 0,
    "total_files_checked": 0,
    "status": "PASS|PASS_WITH_WARNINGS|FAIL",
    "recommendation": "Action recommendation"
  }
}
```

## Status Levels

### PASS ✅
- Total errors: 0
- All checks successful
- System ready for production

### PASS_WITH_WARNINGS ⚠️
- Total errors: 0
- Minor warnings present (1-3 warnings)
- Review and address warnings recommended
- System functional but could be improved

### FAIL ❌
- Total errors: > 0
- Critical issues detected
- Address errors before deployment
- System not production-ready

## Integration with CI/CD

The QC audit can be integrated into GitHub Actions workflows:

```yaml
name: Full QC Audit

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  qc-audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          sudo apt-get install -y shellcheck
      
      - name: Run Full QC Audit
        run: python scripts/full_qc_audit.py
      
      - name: Upload QC Report
        uses: actions/upload-artifact@v3
        if: always()
        with:
          name: qc-audit-report
          path: data/processed/full_qc_audit_report.json
```

## Examples

### Successful Audit

```
================================================================================
NUVIEW STRATEGIC PIPELINE - FULL QC AUDIT
================================================================================
Timestamp: 2025-11-21T16:21:38.511761

...

================================================================================
QC AUDIT SUMMARY
================================================================================

ℹ️  Files Checked: 60
ℹ️  Total Errors: 0
ℹ️  Total Warnings: 4
ℹ️  Detailed Report: data/processed/full_qc_audit_report.json

✅ HTML Files: ✓ PASSED (7 files)
✅ Python Files: ✓ PASSED (21 files)
⚠️  Shell Scripts: ⚠ 3 warnings (1 files)
✅ JSON Files: ✓ PASSED (8 files)
✅ CSV Files: ✓ PASSED (2 files)
✅ Documentation: ✓ PASSED (21 files)
⚠️  Data Integrity: ⚠ 1 warnings (0 files)
✅ Recent Updates: ✓ PASSED (0 files)

================================================================================
✅ QC AUDIT PASSED - All checks successful!
Recommendation: System is ready for production
```

## Testing

The QC audit system includes comprehensive unit tests:

```bash
# Run all tests
python -m pytest tests/ -v

# Run only QC audit tests
python -m pytest tests/test_qc_audit.py -v
```

Tests cover:
- Report generation and structure
- File validation logic
- Category coverage
- Error and warning counting
- Status determination

## Dependencies

Required packages:
- `pandas>=2.2.0` - CSV processing
- `ruff>=0.1.0` - Python linting
- System packages:
  - `shellcheck` - Shell script validation

## Maintenance

### Adding New Validation Types

To add a new validation category:

1. Create a validation function:
```python
def validate_new_type() -> Tuple[List[str], List[str], int]:
    """Validate new file type"""
    errors = []
    warnings = []
    files_checked = 0
    
    # Validation logic here
    
    return errors, warnings, files_checked
```

2. Add to main() function:
```python
new_errors, new_warnings, new_files = validate_new_type()
all_results['New Type'] = {
    'errors': new_errors,
    'warnings': new_warnings,
    'files_checked': new_files
}
```

3. Add corresponding tests in `tests/test_qc_audit.py`

## Best Practices

1. **Run before commits**: Always run the QC audit before committing major changes
2. **Review warnings**: Even if the audit passes, review and address warnings
3. **Keep updated**: Ensure dependencies (ruff, shellcheck) are up to date
4. **CI integration**: Run in CI/CD pipelines to catch issues early
5. **Regular audits**: Schedule periodic full audits (e.g., weekly)

## Troubleshooting

### Common Issues

**Issue**: Shellcheck not found
```bash
# Solution: Install shellcheck
sudo apt-get install shellcheck  # Ubuntu/Debian
brew install shellcheck          # macOS
```

**Issue**: Ruff not found
```bash
# Solution: Install ruff
pip install ruff
```

**Issue**: Permission denied on shell scripts
```bash
# Solution: Make scripts executable
chmod +x setup_and_run.sh
```

## Related Tools

- **qc_validator.py**: Data-specific quality control (opportunities.json, forecast.json)
- **comprehensive_qc_check.py**: Deep data integrity verification
- **pytest**: Unit test framework for validation tests

## Support

For issues or questions:
1. Check the generated report at `data/processed/full_qc_audit_report.json`
2. Review console output for specific error messages
3. Consult individual validation tool documentation (ruff, shellcheck)
4. Contact the development team

## Version History

- **v1.0.0** (2025-11-21): Initial release
  - HTML, Python, Shell, JSON, CSV, Documentation validation
  - Data integrity checks
  - Recent updates and regression detection
  - Comprehensive reporting
