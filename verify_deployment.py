#!/usr/bin/env python3
"""
Deployment Verification Script for NUVIEW Strategic Pipeline
Validates that all components are ready for production deployment
"""

import json
import os
import sys
from pathlib import Path

# ANSI color codes
GREEN = '\033[92m'
ORANGE = '\033[93m'
RED = '\033[91m'
BLUE = '\033[94m'
RESET = '\033[0m'

def log_info(msg):
    print(f"{BLUE}ℹ️  {msg}{RESET}")

def log_success(msg):
    print(f"{GREEN}✅ {msg}{RESET}")

def log_warning(msg):
    print(f"{ORANGE}⚠️  {msg}{RESET}")

def log_error(msg):
    print(f"{RED}❌ {msg}{RESET}")

def check_file_exists(filepath, required=True):
    """Check if a file exists"""
    if os.path.exists(filepath):
        log_success(f"File exists: {filepath}")
        return True
    else:
        if required:
            log_error(f"Required file missing: {filepath}")
            return False
        else:
            log_warning(f"Optional file missing: {filepath}")
            return True

def validate_json_file(filepath):
    """Validate JSON file syntax"""
    try:
        with open(filepath, 'r') as f:
            json.load(f)
        log_success(f"Valid JSON: {filepath}")
        return True
    except json.JSONDecodeError as e:
        log_error(f"Invalid JSON in {filepath}: {e}")
        return False
    except FileNotFoundError:
        log_error(f"File not found: {filepath}")
        return False

def validate_html_structure(filepath):
    """Basic HTML structure validation"""
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        
        # Use more flexible checks that handle attributes
        required_checks = [
            ('<!DOCTYPE html>' in content, 'DOCTYPE'),
            ('<html' in content and '</html>' in content, 'html tags'),
            ('<head' in content and '</head>' in content, 'head tags'),
            ('<body' in content and '</body>' in content, 'body tags'),
            ('<title>' in content, 'title tag')
        ]
        
        failed = [name for passed, name in required_checks if not passed]
        
        if failed:
            log_error(f"HTML structure issues in {filepath}: Missing {failed}")
            return False
        
        log_success(f"Valid HTML structure: {filepath}")
        return True
    except Exception as e:
        log_error(f"Error validating {filepath}: {e}")
        return False

def check_netlify_config():
    """Verify Netlify configuration"""
    log_info("Checking Netlify configuration...")
    
    checks = []
    checks.append(check_file_exists('netlify.toml'))
    checks.append(check_file_exists('_redirects'))
    checks.append(check_file_exists('NETLIFY_DEPLOYMENT.md'))
    
    return all(checks)

def check_github_workflows():
    """Verify GitHub Actions workflows"""
    log_info("Checking GitHub Actions workflows...")
    
    workflows = [
        '.github/workflows/deploy-pages.yml',
        '.github/workflows/daily_ops.yml',
        '.github/workflows/backup.yml',
        '.github/workflows/trigger-local-scrape.yml'
    ]
    
    return all(check_file_exists(wf) for wf in workflows)

def check_dashboard_files():
    """Verify dashboard HTML files"""
    log_info("Checking dashboard files...")
    
    dashboards = [
        'index.html',
        'dashboard/index.html',
        'dashboard/pipeline.html',
        'dashboard/pipeline_matrix.html',
        'dashboard/global-tracker.html'
    ]
    
    return all(validate_html_structure(d) for d in dashboards)

def check_data_files():
    """Verify data JSON files"""
    log_info("Checking data files...")
    
    data_files = [
        'data/opportunities.json',
        'data/forecast.json',
        'data/scraper_stats.json',
        'data/processed/programs.json',
        'data/processed/qc_report.json'
    ]
    
    results = []
    for df in data_files:
        if os.path.exists(df):
            results.append(validate_json_file(df))
        else:
            # Don't fail on missing data files - they may be generated dynamically 
            # by scraping workflows or may not exist yet in a fresh clone
            log_warning(f"Data file not found (may be generated): {df}")
            results.append(True)
    
    return all(results)

def check_automation_scripts():
    """Verify automation scripts"""
    log_info("Checking automation scripts...")
    
    scripts = [
        'scripts/qc_validator.py',
        'scripts/validate_and_merge.py',
        'scripts/local_monitor.py',
        'scripts/scrapers/scrape_all.py'
    ]
    
    return all(check_file_exists(s) for s in scripts)

def check_documentation():
    """Verify documentation files"""
    log_info("Checking documentation...")
    
    docs = [
        'README.md',
        'AUTOMATION_SETUP.md',
        'NETLIFY_DEPLOYMENT.md',
        'BRANDING_UPDATES.md',
        'OPTIMIZATION_CHECKLIST.md'
    ]
    
    return all(check_file_exists(d) for d in docs)

def check_git_config():
    """Verify git configuration"""
    log_info("Checking git configuration...")
    
    checks = []
    checks.append(check_file_exists('.gitignore'))
    checks.append(check_file_exists('.nojekyll', required=False))
    checks.append(check_file_exists('CNAME', required=False))
    
    return all(checks)

def main():
    """Run all verification checks"""
    print(f"\n{BLUE}{'='*60}")
    print("NUVIEW Strategic Pipeline - Deployment Verification")
    print(f"{'='*60}{RESET}\n")
    
    checks = {
        "Netlify Configuration": check_netlify_config,
        "GitHub Workflows": check_github_workflows,
        "Dashboard Files": check_dashboard_files,
        "Data Files": check_data_files,
        "Automation Scripts": check_automation_scripts,
        "Documentation": check_documentation,
        "Git Configuration": check_git_config
    }
    
    results = {}
    for name, check_func in checks.items():
        print(f"\n{BLUE}--- {name} ---{RESET}")
        results[name] = check_func()
        print()
    
    # Summary
    print(f"\n{BLUE}{'='*60}")
    print("Verification Summary")
    print(f"{'='*60}{RESET}\n")
    
    for name, passed in results.items():
        status = f"{GREEN}✅ PASSED{RESET}" if passed else f"{RED}❌ FAILED{RESET}"
        print(f"{name}: {status}")
    
    all_passed = all(results.values())
    
    print(f"\n{BLUE}{'='*60}{RESET}\n")
    
    if all_passed:
        log_success("All verification checks passed! Repository is deployment-ready.")
        print(f"\n{GREEN}🚀 Ready to deploy to GitHub Pages and Netlify!{RESET}\n")
        return 0
    else:
        log_error("Some verification checks failed. Please review and fix issues.")
        print(f"\n{RED}❌ Not ready for deployment. Fix issues above.{RESET}\n")
        return 1

if __name__ == "__main__":
    sys.exit(main())
