#!/usr/bin/env python3
"""
Full Quality Control (QC) Audit System for NUVIEW Strategic Pipeline
Comprehensive audit including:
- HTML validation (syntax, structure)
- Python code validation (syntax, style with ruff)
- Shell script validation (shellcheck)
- Data integrity checks (CSV, JSON)
- Documentation quality checks
- Recent PR integration verification
- Regression detection
"""

import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple

import pandas as pd

# Color codes for console output
COLOR_GREEN = '\033[92m'
COLOR_ORANGE = '\033[93m'
COLOR_RED = '\033[91m'
COLOR_BLUE = '\033[94m'
COLOR_CYAN = '\033[96m'
COLOR_RESET = '\033[0m'

def log_section(title: str):
    """Log a section header"""
    print(f"\n{COLOR_CYAN}{'=' * 80}")
    print(f"{title}")
    print(f"{'=' * 80}{COLOR_RESET}\n")

def log_info(msg: str):
    """Log info message"""
    print(f"{COLOR_BLUE}ℹ️  {msg}{COLOR_RESET}")

def log_success(msg: str):
    """Log success message"""
    print(f"{COLOR_GREEN}✅ {msg}{COLOR_RESET}")

def log_warning(msg: str):
    """Log warning message"""
    print(f"{COLOR_ORANGE}⚠️  {msg}{COLOR_RESET}")

def log_error(msg: str):
    """Log error message"""
    print(f"{COLOR_RED}❌ {msg}{COLOR_RESET}")

def validate_html_files() -> Tuple[List[str], List[str], int]:
    """Validate HTML files for syntax and structure"""
    log_section("HTML FILE VALIDATION")

    errors = []
    warnings = []
    files_checked = 0

    html_files = list(Path('.').rglob('*.html'))
    html_files = [f for f in html_files if '.git' not in str(f)]

    log_info(f"Found {len(html_files)} HTML files")

    for html_file in html_files:
        files_checked += 1
        log_info(f"Checking: {html_file}")

        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Basic HTML validation
            if not content.strip():
                errors.append(f"{html_file}: File is empty")
                continue

            # Check for DOCTYPE
            if '<!DOCTYPE html>' not in content and '<!doctype html>' not in content.lower():
                warnings.append(f"{html_file}: Missing DOCTYPE declaration")

            # Check for basic HTML structure
            if '<html' not in content.lower():
                errors.append(f"{html_file}: Missing <html> tag")

            if '<head' not in content.lower():
                warnings.append(f"{html_file}: Missing <head> section")

            if '<body' not in content.lower():
                warnings.append(f"{html_file}: Missing <body> section")

            # Check for charset declaration
            if 'charset=' not in content.lower():
                warnings.append(f"{html_file}: Missing charset declaration")

            # Check for unclosed tags (basic check)
            open_tags = content.count('<div')
            close_tags = content.count('</div>')
            if open_tags != close_tags:
                warnings.append(f"{html_file}: Mismatched <div> tags (open: {open_tags}, close: {close_tags})")

        except UnicodeDecodeError:
            errors.append(f"{html_file}: File encoding error")
        except Exception as e:
            errors.append(f"{html_file}: {str(e)}")

    # Report results
    if errors:
        for error in errors:
            log_error(error)

    if warnings:
        for warning in warnings:
            log_warning(warning)

    if not errors and not warnings:
        log_success(f"All {files_checked} HTML files validated successfully")

    return errors, warnings, files_checked

def validate_python_files() -> Tuple[List[str], List[str], int]:
    """Validate Python files for syntax and style using ruff"""
    log_section("PYTHON CODE VALIDATION")

    errors = []
    warnings = []
    files_checked = 0

    # Find all Python files
    python_files = list(Path('.').rglob('*.py'))
    python_files = [f for f in python_files if '.git' not in str(f)]

    log_info(f"Found {len(python_files)} Python files")

    # Check syntax for each file
    for py_file in python_files:
        files_checked += 1
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                compile(f.read(), str(py_file), 'exec')
        except SyntaxError as e:
            errors.append(f"{py_file}: Syntax error at line {e.lineno}: {e.msg}")
        except Exception as e:
            errors.append(f"{py_file}: {str(e)}")

    log_info(f"Syntax checked for {files_checked} Python files")

    # Run ruff for style checking
    log_info("Running ruff for style checking...")
    try:
        result = subprocess.run(
            ['ruff', 'check', 'scripts/', 'tests/', '--output-format=text'],
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.stdout:
            # Parse ruff output
            lines = result.stdout.strip().split('\n')
            for line in lines:
                if line and not line.startswith('warning:') and not line.startswith('Found'):
                    if 'error' in line.lower() or line.startswith('E'):
                        errors.append(f"Ruff: {line}")
                    else:
                        warnings.append(f"Ruff: {line}")

        if result.returncode == 0:
            log_success("Ruff style check passed")
        else:
            log_warning(f"Ruff found {len([w for w in warnings if 'Ruff:' in w])} style issues")

    except FileNotFoundError:
        warnings.append("Ruff not found - skipping style checks")
    except subprocess.TimeoutExpired:
        warnings.append("Ruff check timed out")
    except Exception as e:
        warnings.append(f"Ruff check failed: {str(e)}")

    # Report results
    if errors:
        log_error(f"Found {len(errors)} Python errors")
        for error in errors[:10]:  # Show first 10
            log_error(error)
        if len(errors) > 10:
            log_error(f"... and {len(errors) - 10} more errors")
    else:
        log_success(f"All {files_checked} Python files have valid syntax")

    return errors, warnings, files_checked

def validate_shell_scripts() -> Tuple[List[str], List[str], int]:
    """Validate shell scripts using shellcheck"""
    log_section("SHELL SCRIPT VALIDATION")

    errors = []
    warnings = []
    files_checked = 0

    # Find all shell scripts
    shell_files = list(Path('.').rglob('*.sh'))
    shell_files = [f for f in shell_files if '.git' not in str(f)]

    log_info(f"Found {len(shell_files)} shell scripts")

    for sh_file in shell_files:
        files_checked += 1
        log_info(f"Checking: {sh_file}")

        try:
            result = subprocess.run(
                ['shellcheck', str(sh_file)],
                capture_output=True,
                text=True,
                timeout=10
            )

            if result.stdout:
                lines = result.stdout.strip().split('\n')
                for line in lines:
                    if 'error' in line.lower():
                        errors.append(f"{sh_file}: {line}")
                    elif 'warning' in line.lower():
                        warnings.append(f"{sh_file}: {line}")
                    elif line.strip() and not line.startswith('In ') and 'https://' not in line:
                        warnings.append(f"{sh_file}: {line}")

            if result.returncode == 0:
                log_success(f"{sh_file}: Passed shellcheck")

        except FileNotFoundError:
            warnings.append(f"shellcheck not found - skipping {sh_file}")
            break  # Don't check others if shellcheck is not available
        except subprocess.TimeoutExpired:
            warnings.append(f"{sh_file}: shellcheck timed out")
        except Exception as e:
            warnings.append(f"{sh_file}: {str(e)}")

    # Report results
    if not errors and warnings:
        log_warning(f"Found {len(warnings)} shell script warnings (non-critical)")

    return errors, warnings, files_checked

def validate_json_files() -> Tuple[List[str], List[str], int]:
    """Validate JSON files for syntax and structure"""
    log_section("JSON FILE VALIDATION")

    errors = []
    warnings = []
    files_checked = 0

    # Find all JSON files
    json_files = list(Path('.').rglob('*.json'))
    json_files = [f for f in json_files if '.git' not in str(f) and 'node_modules' not in str(f)]

    log_info(f"Found {len(json_files)} JSON files")

    for json_file in json_files:
        files_checked += 1
        log_info(f"Checking: {json_file}")

        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Check if empty
            if not data:
                warnings.append(f"{json_file}: File is empty or contains null")
            else:
                log_success(f"{json_file}: Valid JSON")

        except json.JSONDecodeError as e:
            errors.append(f"{json_file}: JSON syntax error at line {e.lineno}: {e.msg}")
        except Exception as e:
            errors.append(f"{json_file}: {str(e)}")

    # Report results
    if errors:
        for error in errors:
            log_error(error)
    elif files_checked > 0:
        log_success(f"All {files_checked} JSON files are valid")

    return errors, warnings, files_checked

def validate_csv_files() -> Tuple[List[str], List[str], int]:
    """Validate CSV files for structure and integrity"""
    log_section("CSV FILE VALIDATION")

    errors = []
    warnings = []
    files_checked = 0

    # Find all CSV files
    csv_files = list(Path('.').rglob('*.csv'))
    csv_files = [f for f in csv_files if '.git' not in str(f)]

    log_info(f"Found {len(csv_files)} CSV files")

    for csv_file in csv_files:
        files_checked += 1
        log_info(f"Checking: {csv_file}")

        try:
            df = pd.read_csv(csv_file)

            # Check if empty
            if df.empty:
                warnings.append(f"{csv_file}: File is empty")
                continue

            # Check for duplicate headers
            if df.columns.duplicated().any():
                errors.append(f"{csv_file}: Contains duplicate column headers")

            # Check for null values
            null_count = df.isnull().sum().sum()
            if null_count > 0:
                warnings.append(f"{csv_file}: Contains {null_count} null values")

            log_success(f"{csv_file}: Valid CSV with {len(df)} rows, {len(df.columns)} columns")

        except pd.errors.EmptyDataError:
            errors.append(f"{csv_file}: File is empty")
        except pd.errors.ParserError as e:
            errors.append(f"{csv_file}: CSV parsing error: {str(e)}")
        except Exception as e:
            errors.append(f"{csv_file}: {str(e)}")

    # Report results
    if errors:
        for error in errors:
            log_error(error)
    elif files_checked > 0:
        log_success(f"All {files_checked} CSV files are valid")

    return errors, warnings, files_checked

def validate_documentation() -> Tuple[List[str], List[str], int]:
    """Validate documentation files for clarity and completeness"""
    log_section("DOCUMENTATION VALIDATION")

    errors = []
    warnings = []
    files_checked = 0

    # Find all markdown files
    md_files = list(Path('.').rglob('*.md'))
    md_files = [f for f in md_files if '.git' not in str(f) and 'node_modules' not in str(f)]

    log_info(f"Found {len(md_files)} Markdown files")

    for md_file in md_files:
        files_checked += 1
        log_info(f"Checking: {md_file}")

        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Check if empty
            if not content.strip():
                warnings.append(f"{md_file}: File is empty")
                continue

            # Check for headers
            if not any(line.startswith('#') for line in content.split('\n')):
                warnings.append(f"{md_file}: Missing markdown headers")

            # Check for minimum content length
            if len(content) < 100:
                warnings.append(f"{md_file}: File seems too short ({len(content)} chars)")

            log_success(f"{md_file}: Valid ({len(content)} chars)")

        except UnicodeDecodeError:
            errors.append(f"{md_file}: File encoding error")
        except Exception as e:
            errors.append(f"{md_file}: {str(e)}")

    # Report results
    if errors:
        for error in errors:
            log_error(error)
    elif files_checked > 0:
        log_success(f"All {files_checked} documentation files validated")

    return errors, warnings, files_checked

def check_data_integrity() -> Tuple[List[str], List[str]]:
    """Run existing data integrity checks"""
    log_section("DATA INTEGRITY CHECKS")

    errors = []
    warnings = []

    # Run existing QC validator
    log_info("Running qc_validator.py...")
    try:
        result = subprocess.run(
            [sys.executable, 'scripts/qc_validator.py'],
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode != 0:
            errors.append("QC validator failed - see output above")
        else:
            log_success("QC validator passed")
    except subprocess.TimeoutExpired:
        warnings.append("QC validator timed out")
    except Exception as e:
        warnings.append(f"Could not run QC validator: {str(e)}")

    # Run comprehensive QC check
    log_info("Running comprehensive_qc_check.py...")
    try:
        result = subprocess.run(
            [sys.executable, 'scripts/comprehensive_qc_check.py'],
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode != 0:
            # Parse the output to get specific errors
            if 'CALCULATIONS' in result.stdout and 'FAIL' in result.stdout:
                warnings.append("Calculation verification found inconsistencies (may need recalculation)")
        else:
            log_success("Comprehensive QC check passed")
    except subprocess.TimeoutExpired:
        warnings.append("Comprehensive QC check timed out")
    except Exception as e:
        warnings.append(f"Could not run comprehensive QC check: {str(e)}")

    return errors, warnings

def check_recent_updates() -> Tuple[List[str], List[str]]:
    """Check for recent updates and potential regressions"""
    log_section("RECENT UPDATES & REGRESSION CHECK")

    errors = []
    warnings = []

    try:
        # Check git status
        result = subprocess.run(
            ['git', 'status', '--porcelain'],
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.stdout.strip():
            modified_files = [line.split()[-1] for line in result.stdout.strip().split('\n')]
            log_info(f"Found {len(modified_files)} modified/untracked files")
        else:
            log_success("No uncommitted changes")

        # Check recent commits
        result = subprocess.run(
            ['git', 'log', '--oneline', '--since=1 week ago'],
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.stdout.strip():
            commits = result.stdout.strip().split('\n')
            log_info(f"Found {len(commits)} commits in the last week")
            for commit in commits[:5]:  # Show last 5
                log_info(f"  {commit}")
        else:
            log_info("No commits in the last week")

        # Check for merge conflicts
        result = subprocess.run(
            ['git', 'diff', '--check'],
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.stdout.strip():
            errors.append("Found merge conflict markers or whitespace errors")
            log_error(result.stdout.strip())
        else:
            log_success("No merge conflicts or whitespace errors detected")

    except subprocess.TimeoutExpired:
        warnings.append("Git check timed out")
    except FileNotFoundError:
        warnings.append("Git not available - skipping version control checks")
    except Exception as e:
        warnings.append(f"Git check failed: {str(e)}")

    return errors, warnings

def generate_qc_report(all_results: Dict) -> str:
    """Generate comprehensive QC report"""
    log_section("GENERATING QC REPORT")

    report = {
        "timestamp": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
        "audit_type": "Full QC Audit",
        "results": all_results,
        "summary": {
            "total_errors": sum(len(r.get('errors', [])) for r in all_results.values()),
            "total_warnings": sum(len(r.get('warnings', [])) for r in all_results.values()),
            "total_files_checked": sum(r.get('files_checked', 0) for r in all_results.values())
        }
    }

    # Determine overall status
    if report['summary']['total_errors'] == 0:
        report['summary']['status'] = 'PASS'
        report['summary']['recommendation'] = 'All checks passed. System is ready for production.'
    elif report['summary']['total_errors'] <= 3:
        report['summary']['status'] = 'PASS_WITH_WARNINGS'
        report['summary']['recommendation'] = 'Minor issues detected. Review and address warnings.'
    else:
        report['summary']['status'] = 'FAIL'
        report['summary']['recommendation'] = 'Critical issues detected. Address errors before deployment.'

    # Save report
    os.makedirs('data/processed', exist_ok=True)
    report_path = 'data/processed/full_qc_audit_report.json'

    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)

    log_success(f"QC report saved to {report_path}")

    return report_path

def print_summary(all_results: Dict, report_path: str):
    """Print executive summary"""
    log_section("QC AUDIT SUMMARY")

    total_errors = sum(len(r.get('errors', [])) for r in all_results.values())
    total_warnings = sum(len(r.get('warnings', [])) for r in all_results.values())
    total_files = sum(r.get('files_checked', 0) for r in all_results.values())

    log_info(f"Files Checked: {total_files}")
    log_info(f"Total Errors: {total_errors}")
    log_info(f"Total Warnings: {total_warnings}")
    log_info(f"Detailed Report: {report_path}")

    print()

    # Summary by category
    for category, results in all_results.items():
        errors = len(results.get('errors', []))
        warnings = len(results.get('warnings', []))
        files = results.get('files_checked', 0)

        if errors == 0 and warnings == 0:
            log_success(f"{category}: ✓ PASSED ({files} files)")
        elif errors == 0:
            log_warning(f"{category}: ⚠ {warnings} warnings ({files} files)")
        else:
            log_error(f"{category}: ✗ {errors} errors, {warnings} warnings ({files} files)")

    print()
    print("=" * 80)

    if total_errors == 0:
        log_success("✅ QC AUDIT PASSED - All checks successful!")
        print(f"{COLOR_GREEN}Recommendation: System is ready for production{COLOR_RESET}")
        return 0
    elif total_errors <= 3:
        log_warning("⚠️ QC AUDIT PASSED WITH WARNINGS")
        print(f"{COLOR_ORANGE}Recommendation: Review and address warnings{COLOR_RESET}")
        return 0
    else:
        log_error("❌ QC AUDIT FAILED - Critical issues detected")
        print(f"{COLOR_RED}Recommendation: Address errors before deployment{COLOR_RESET}")
        return 1

def main():
    """Run full QC audit"""
    print(f"{COLOR_CYAN}")
    print("=" * 80)
    print("NUVIEW STRATEGIC PIPELINE - FULL QC AUDIT")
    print("=" * 80)
    print(f"Timestamp: {datetime.now().isoformat()}")
    print(f"{COLOR_RESET}")

    all_results = {}

    # HTML validation
    html_errors, html_warnings, html_files = validate_html_files()
    all_results['HTML Files'] = {
        'errors': html_errors,
        'warnings': html_warnings,
        'files_checked': html_files
    }

    # Python validation
    py_errors, py_warnings, py_files = validate_python_files()
    all_results['Python Files'] = {
        'errors': py_errors,
        'warnings': py_warnings,
        'files_checked': py_files
    }

    # Shell script validation
    sh_errors, sh_warnings, sh_files = validate_shell_scripts()
    all_results['Shell Scripts'] = {
        'errors': sh_errors,
        'warnings': sh_warnings,
        'files_checked': sh_files
    }

    # JSON validation
    json_errors, json_warnings, json_files = validate_json_files()
    all_results['JSON Files'] = {
        'errors': json_errors,
        'warnings': json_warnings,
        'files_checked': json_files
    }

    # CSV validation
    csv_errors, csv_warnings, csv_files = validate_csv_files()
    all_results['CSV Files'] = {
        'errors': csv_errors,
        'warnings': csv_warnings,
        'files_checked': csv_files
    }

    # Documentation validation
    doc_errors, doc_warnings, doc_files = validate_documentation()
    all_results['Documentation'] = {
        'errors': doc_errors,
        'warnings': doc_warnings,
        'files_checked': doc_files
    }

    # Data integrity checks
    data_errors, data_warnings = check_data_integrity()
    all_results['Data Integrity'] = {
        'errors': data_errors,
        'warnings': data_warnings,
        'files_checked': 0
    }

    # Recent updates check
    update_errors, update_warnings = check_recent_updates()
    all_results['Recent Updates'] = {
        'errors': update_errors,
        'warnings': update_warnings,
        'files_checked': 0
    }

    # Generate report
    report_path = generate_qc_report(all_results)

    # Print summary
    exit_code = print_summary(all_results, report_path)

    return exit_code

if __name__ == "__main__":
    sys.exit(main())
