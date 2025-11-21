#!/usr/bin/env python3
"""
Local Scrape Monitor for NUVIEW Strategic Pipeline

This script runs on your local machine and monitors the repository for scrape triggers.
When a trigger is detected, it executes the scraping process and pushes results back.

Usage:
    python scripts/local_monitor.py --watch        # Continuous monitoring mode
    python scripts/local_monitor.py --check-once   # Check once and exit
    python scripts/local_monitor.py --scrape       # Force scrape without checking for trigger

Requirements:
    - Git repository must be configured with push access
    - Python 3.6+
    - Working directory should be the repository root
"""

import os
import sys
import json
import time
import subprocess
import argparse
from datetime import datetime, timezone
from pathlib import Path

# Configuration
SIGNAL_FILE = "data/signals/scrape_trigger.json"
CHECK_INTERVAL = 60  # seconds between checks in watch mode
REPO_ROOT = Path(__file__).parent.parent.absolute()

# ANSI color codes
COLOR_GREEN = '\033[92m'
COLOR_BLUE = '\033[94m'
COLOR_YELLOW = '\033[93m'
COLOR_RED = '\033[91m'
COLOR_RESET = '\033[0m'

def log_info(msg):
    """Log info message"""
    print(f"{COLOR_BLUE}ℹ️  {msg}{COLOR_RESET}")

def log_success(msg):
    """Log success message"""
    print(f"{COLOR_GREEN}✅ {msg}{COLOR_RESET}")

def log_warning(msg):
    """Log warning message"""
    print(f"{COLOR_YELLOW}⚠️  {msg}{COLOR_RESET}")

def log_error(msg):
    """Log error message"""
    print(f"{COLOR_RED}❌ {msg}{COLOR_RESET}")

def run_command(cmd, cwd=None):
    """Run a shell command and return output"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            cwd=cwd or REPO_ROOT,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip(), None
    except subprocess.CalledProcessError as e:
        return None, e.stderr.strip()

def git_pull():
    """Pull latest changes from remote"""
    log_info("Pulling latest changes from remote...")
    stdout, stderr = run_command("git pull origin main")
    if stderr:
        log_error(f"Git pull failed: {stderr}")
        return False
    log_success("Repository updated")
    return True

def check_for_trigger():
    """Check if there's a pending scrape trigger"""
    signal_path = REPO_ROOT / SIGNAL_FILE
    
    if not signal_path.exists():
        return None
    
    try:
        with open(signal_path, 'r') as f:
            signal_data = json.load(f)
        
        # Check if status is pending
        if signal_data.get('status') == 'pending':
            return signal_data
        
        return None
    except Exception as e:
        log_error(f"Error reading signal file: {e}")
        return None

def execute_scrape():
    """Execute the scraping process"""
    log_info("=" * 60)
    log_info("🕷️  EXECUTING LOCAL SCRAPE PROCESS")
    log_info("=" * 60)
    
    # Run the scrape script
    scrape_script = REPO_ROOT / "scripts" / "scrapers" / "scrape_all.py"
    
    if not scrape_script.exists():
        log_error(f"Scrape script not found: {scrape_script}")
        return False
    
    log_info(f"Running: python {scrape_script}")
    stdout, stderr = run_command(f"python3 {scrape_script}")
    
    # Check if scrape failed (stderr will be set by CalledProcessError)
    if stderr is not None:
        log_error(f"Scrape failed: {stderr}")
        return False
    
    if stdout:
        print(stdout)
    
    log_success("Scraping completed successfully")
    return True

def update_signal_status(status, message=""):
    """Update the trigger signal status"""
    signal_path = REPO_ROOT / SIGNAL_FILE
    
    if not signal_path.exists():
        log_warning("Signal file not found, creating new one")
        signal_data = {}
    else:
        with open(signal_path, 'r') as f:
            signal_data = json.load(f)
    
    signal_data['status'] = status
    signal_data['completed_time'] = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    
    if message:
        signal_data['message'] = message
    
    # Ensure directory exists
    signal_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(signal_path, 'w') as f:
        json.dump(signal_data, f, indent=2)
    
    log_success(f"Signal status updated to: {status}")

def git_commit_and_push(message):
    """Commit and push changes"""
    log_info("Committing and pushing changes...")
    
    # Configure git locally if not already configured
    run_command('git config --local user.email "local@nuview.space"')
    run_command('git config --local user.name "NUVIEW Local Scraper"')
    
    # Add all changes
    stdout, stderr = run_command("git add data/")
    
    # Check if there are changes to commit (diff --quiet returns non-zero if there are changes)
    stdout, stderr = run_command("git diff --staged --quiet")
    # If command succeeded (exit code 0), there are no changes
    if stderr is None:
        log_info("No changes to commit")
        return True
    
    # Commit
    stdout, stderr = run_command(f'git commit -m "{message}"')
    if stderr and "nothing to commit" not in stderr:
        if stderr:
            log_error(f"Git commit failed: {stderr}")
            return False
    
    # Get current branch
    current_branch, _ = run_command("git rev-parse --abbrev-ref HEAD")
    if not current_branch:
        log_error("Could not determine current branch")
        return False
    
    current_branch = current_branch.strip()
    log_info(f"Pushing to branch: {current_branch}")
    
    # Push to current branch (not hardcoded to main)
    stdout, stderr = run_command(f"git push origin {current_branch}")
    if stderr is not None:
        log_error(f"Git push failed: {stderr}")
        return False
    
    log_success("Changes pushed to remote repository")
    return True

def process_trigger(trigger_data):
    """Process a detected trigger"""
    log_info("=" * 60)
    log_success("🚀 SCRAPE TRIGGER DETECTED")
    log_info("=" * 60)
    log_info(f"Triggered by: {trigger_data.get('triggered_by', 'unknown')}")
    log_info(f"Trigger time: {trigger_data.get('trigger_time', 'unknown')}")
    log_info("")
    
    # Execute scrape
    scrape_success = execute_scrape()
    
    if scrape_success:
        # Update signal status
        update_signal_status('completed', 'Scrape completed successfully')
        
        # Commit and push
        commit_msg = f"🤖 Auto-update from local scrape - Completed at {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')} UTC"
        push_success = git_commit_and_push(commit_msg)
        
        if push_success:
            log_success("=" * 60)
            log_success("🎉 SCRAPE PROCESS COMPLETED SUCCESSFULLY")
            log_success("=" * 60)
            return True
        else:
            log_error("Failed to push changes to remote")
            update_signal_status('failed', 'Failed to push changes')
            return False
    else:
        log_error("Scraping process failed")
        update_signal_status('failed', 'Scraping process encountered errors')
        
        # Still try to push the failed status
        git_commit_and_push(f"❌ Scrape failed at {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')} UTC")
        return False

def watch_mode():
    """Continuous monitoring mode"""
    log_info("=" * 60)
    log_info("👁️  LOCAL SCRAPE MONITOR - WATCH MODE")
    log_info("=" * 60)
    log_info(f"Checking every {CHECK_INTERVAL} seconds for triggers...")
    log_info("Press Ctrl+C to stop")
    log_info("")
    
    try:
        while True:
            # Pull latest changes
            if not git_pull():
                log_warning("Failed to pull changes, will retry next cycle")
                time.sleep(CHECK_INTERVAL)
                continue
            
            # Check for trigger
            trigger_data = check_for_trigger()
            
            if trigger_data:
                process_trigger(trigger_data)
            else:
                log_info(f"No pending triggers found. Checking again in {CHECK_INTERVAL}s...")
            
            time.sleep(CHECK_INTERVAL)
            
    except KeyboardInterrupt:
        log_info("")
        log_info("Monitor stopped by user")
        sys.exit(0)

def check_once_mode():
    """Check for trigger once and exit"""
    log_info("Checking for trigger (one-time check)...")
    
    # Pull latest changes
    if not git_pull():
        log_error("Failed to pull changes")
        sys.exit(1)
    
    # Check for trigger
    trigger_data = check_for_trigger()
    
    if trigger_data:
        success = process_trigger(trigger_data)
        sys.exit(0 if success else 1)
    else:
        log_info("No pending triggers found")
        sys.exit(0)

def force_scrape_mode():
    """Force scrape without checking for trigger"""
    log_info("Force scraping (no trigger check)...")
    
    # Execute scrape
    scrape_success = execute_scrape()
    
    if scrape_success:
        # Commit and push
        commit_msg = f"🔧 Manual scrape - {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')} UTC"
        push_success = git_commit_and_push(commit_msg)
        
        if push_success:
            log_success("Manual scrape completed and pushed")
            sys.exit(0)
        else:
            log_error("Failed to push changes")
            sys.exit(1)
    else:
        log_error("Scraping failed")
        sys.exit(1)

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="NUVIEW Local Scrape Monitor",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/local_monitor.py --watch        # Continuous monitoring
  python scripts/local_monitor.py --check-once   # Check once and exit
  python scripts/local_monitor.py --scrape       # Force scrape
        """
    )
    
    parser.add_argument(
        '--watch',
        action='store_true',
        help='Continuous monitoring mode (default)'
    )
    parser.add_argument(
        '--check-once',
        action='store_true',
        help='Check for trigger once and exit'
    )
    parser.add_argument(
        '--scrape',
        action='store_true',
        help='Force scrape without checking for trigger'
    )
    
    args = parser.parse_args()
    
    # Change to repo root
    os.chdir(REPO_ROOT)
    
    # Determine mode
    if args.check_once:
        check_once_mode()
    elif args.scrape:
        force_scrape_mode()
    else:
        # Default to watch mode
        watch_mode()

if __name__ == "__main__":
    main()
