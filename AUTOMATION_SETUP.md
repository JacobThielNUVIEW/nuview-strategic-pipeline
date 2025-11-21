# NUVIEW Strategic Pipeline - Automated Workflow Setup

## Overview

This document provides comprehensive setup instructions for the fully automated NUVIEW Strategic Pipeline system. The system enables:

1. **Automated CI/CD Pipeline** - Continuous integration and deployment on every push
2. **Remote-Triggered Local Scraping** - Trigger scraping from the dashboard
3. **Live Dashboard Updates** - Automatic updates when data changes
4. **Error Handling & Monitoring** - Automated alerts and issue tracking
5. **Secure Access Control** - Password-protected operations

---

## 🔧 Initial Setup

### Step 1: Configure GitHub Secrets

The system requires two secrets to be configured in your GitHub repository:

1. **Navigate to Repository Settings**
   - Go to your GitHub repository
   - Click on "Settings" tab
   - Navigate to "Secrets and variables" → "Actions"

2. **Create Required Secrets**

   **Secret 1: `NUVIEW_SCRAPE_TOKEN`**
   - Click "New repository secret"
   - Name: `NUVIEW_SCRAPE_TOKEN`
   - Value: Create a strong, random password (e.g., `NUV1EW_53cr3t_T0k3n_2024!`)
   - This token is used to authenticate scrape trigger requests
   - **Important**: Save this token securely - you'll need it to use the rocket button

   **Secret 2: `GH_PAT` (Optional, for advanced features)**
   - Click "New repository secret"  
   - Name: `GH_PAT`
   - Value: A GitHub Personal Access Token with `repo` and `workflow` permissions
   - To create: GitHub Settings → Developer settings → Personal access tokens → Generate new token
   - This enables the workflow to create issues and trigger other workflows

### Step 2: Enable GitHub Pages

1. Go to repository "Settings" → "Pages"
2. Under "Source", select "GitHub Actions"
3. Save the configuration
4. Your dashboard will be available at: `https://[username].github.io/[repo-name]/`

### Step 3: Configure GitHub Actions Permissions

1. Go to repository "Settings" → "Actions" → "General"
2. Under "Workflow permissions":
   - Select "Read and write permissions"
   - Check "Allow GitHub Actions to create and approve pull requests"
3. Save the configuration

---

## 🚀 Using the Dashboard Rocket Button

### What It Does

The floating rocket button in the bottom-right corner of the dashboard triggers your local machine to:
1. Pull the latest repository changes
2. Execute the scraping process
3. Validate the data
4. Push results back to the repository
5. Automatically update the dashboard

### How to Use

1. **On the Dashboard**:
   - Click the floating 🚀 rocket button
   - Enter your authentication token (the `NUVIEW_SCRAPE_TOKEN` you created)
   - Click "Launch Scrape"

2. **What Happens**:
   - A workflow is triggered that creates a signal file in the repository
   - Your local machine (running the monitor script) detects the signal
   - The scraping process executes automatically
   - Results are pushed back and the dashboard updates

3. **Monitoring Progress**:
   - Check the "Actions" tab in GitHub to see workflow progress
   - A GitHub issue is automatically created to track the scrape
   - The issue updates when your local machine completes the process

---

## 💻 Local Machine Setup

### Prerequisites

- Python 3.6 or higher
- Git configured with push access to the repository
- Repository cloned locally

### Installation

1. **Clone the repository** (if not already done):
   ```bash
   git clone https://github.com/JacobThielNUVIEW/nuview-strategic-pipeline.git
   cd nuview-strategic-pipeline
   ```

2. **Verify the monitor script**:
   ```bash
   python3 scripts/local_monitor.py --help
   ```

### Running the Monitor

The local monitor script watches for trigger signals from the dashboard and executes scrapes automatically.

**Option 1: Continuous Monitoring (Recommended)**

Run this in a terminal window or as a background process:

```bash
python3 scripts/local_monitor.py --watch
```

This will:
- Check for triggers every 60 seconds
- Automatically execute scrapes when triggered
- Push results back to the repository
- Continue running until stopped (Ctrl+C)

**Option 2: Check Once**

Useful for testing or manual checks:

```bash
python3 scripts/local_monitor.py --check-once
```

**Option 3: Force Scrape**

Execute a scrape immediately without waiting for a trigger:

```bash
python3 scripts/local_monitor.py --scrape
```

### Running as a Background Service (Linux/Mac)

For 24/7 operation, run the monitor as a systemd service:

1. **Create service file** `/etc/systemd/system/nuview-monitor.service`:
   ```ini
   [Unit]
   Description=NUVIEW Pipeline Monitor
   After=network.target

   [Service]
   Type=simple
   User=YOUR_USERNAME
   WorkingDirectory=/path/to/nuview-strategic-pipeline
   ExecStart=/usr/bin/python3 /path/to/nuview-strategic-pipeline/scripts/local_monitor.py --watch
   Restart=always
   RestartSec=10

   [Install]
   WantedBy=multi-user.target
   ```

2. **Enable and start the service**:
   ```bash
   sudo systemctl enable nuview-monitor
   sudo systemctl start nuview-monitor
   sudo systemctl status nuview-monitor
   ```

### Running on Windows

Use Windows Task Scheduler:

1. Open Task Scheduler
2. Create New Task
3. Set trigger: "At system startup"
4. Set action: `python C:\path\to\scripts\local_monitor.py --watch`
5. Configure to run whether user is logged in or not

---

## 🔄 Automated Workflows

### 1. Daily Automated Scraping

**Workflow**: `.github/workflows/daily_ops.yml`

**Schedule**: Runs daily at 3:00 AM UTC

**What it does**:
- Automatically scrapes data from all configured sources
- Validates data quality (QC checks)
- Pushes validated data to the main branch
- Updates the live dashboard
- Creates alerts if validation fails

**Manual trigger**: Go to Actions → "Daily Global Topographic Sweep" → "Run workflow"

### 2. Continuous Deployment

**Workflow**: `.github/workflows/deploy-pages.yml`

**Trigger**: On every push to `main` branch

**What it does**:
- Builds the dashboard
- Deploys to GitHub Pages
- Updates the live site within ~2 minutes

### 3. Local Scrape Trigger

**Workflow**: `.github/workflows/trigger-local-scrape.yml`

**Trigger**: Via dashboard rocket button (workflow_dispatch)

**What it does**:
- Validates authentication token
- Creates a signal file for local machine
- Creates monitoring issue
- Waits for local machine to complete

---

## 📊 Data Flow

```
┌─────────────────────────────────────────────────────────────┐
│                     AUTOMATED PIPELINE                      │
└─────────────────────────────────────────────────────────────┘

1. TRIGGER (Manual/Scheduled)
   │
   ├─► Dashboard Rocket Button → GitHub Workflow → Signal File
   └─► Daily Schedule (3 AM UTC) → GitHub Actions

2. LOCAL EXECUTION
   │
   ├─► Local Monitor detects signal
   ├─► Executes scrape_all.py
   ├─► Generates opportunities.json & forecast.json
   └─► Runs QC validation

3. VALIDATION & COMMIT
   │
   ├─► QC Validator checks data quality
   ├─► If PASS: Commit & push to main
   └─► If FAIL: Create alert issue

4. DEPLOYMENT
   │
   ├─► Push to main triggers deploy workflow
   ├─► GitHub Pages rebuilds site
   └─► Dashboard updates (live in ~2 minutes)

5. MONITORING
   │
   ├─► GitHub Issues track all operations
   ├─► Workflow logs available in Actions tab
   └─► QC reports stored in data/processed/
```

---

## 🔒 Security Features

### Authentication

- **Token-based authentication** for scrape triggers
- Tokens stored as GitHub Secrets (never exposed in code)
- Password input field uses type="password" (masked input)
- Authentication happens server-side in GitHub Actions

### Access Control

- Only users with the correct token can trigger scrapes
- GitHub Actions permissions scoped to minimum required
- No credentials stored in client-side code

### Data Protection

- All data transfers use HTTPS
- Git commits are authenticated via SSH/HTTPS
- Secrets never logged or exposed in workflow outputs

---

## 🐛 Troubleshooting

### Dashboard Not Updating

1. Check GitHub Actions tab for failed workflows
2. Verify GitHub Pages is enabled and deployed
3. Clear browser cache (Ctrl+Shift+R)
4. Check that data files exist in `data/` directory

### Local Monitor Not Detecting Triggers

1. Ensure monitor is running: `ps aux | grep local_monitor`
2. Check git can pull: `git pull origin main`
3. Verify signal file exists: `ls -la data/signals/`
4. Check monitor logs for errors

### Authentication Fails

1. Verify `NUVIEW_SCRAPE_TOKEN` secret is set in GitHub
2. Ensure token matches exactly (no extra spaces)
3. Check workflow logs in Actions tab for auth errors

### QC Validation Failures

1. Check `data/processed/qc_report.json` for details
2. Review workflow logs in Actions tab
3. Verify data files have correct structure
4. Check for missing required fields

### Workflow Permission Errors

1. Go to Settings → Actions → General
2. Ensure "Read and write permissions" is selected
3. Check "Allow GitHub Actions to create and approve pull requests"

---

## 📈 Monitoring & Maintenance

### Daily Checks

- Review GitHub Actions for failed workflows
- Check for open issues with `qc-failure` label
- Verify dashboard is displaying latest data

### Weekly Maintenance

- Review QC reports for data quality trends
- Check local monitor uptime
- Verify backup data is being generated
- Review GitHub Actions usage/quotas

### Monthly Reviews

- Audit authentication tokens (rotate if needed)
- Review and close old monitoring issues
- Update documentation if process changes
- Check for GitHub Actions updates

---

## 📚 Additional Resources

### File Structure

```
nuview-strategic-pipeline/
├── .github/
│   └── workflows/
│       ├── daily_ops.yml           # Daily automated scraping
│       ├── deploy-pages.yml        # Continuous deployment
│       └── trigger-local-scrape.yml # Remote scrape trigger
├── dashboard/
│   └── index.html                  # Main dashboard with rocket button
├── data/
│   ├── opportunities.json          # Scraped opportunities data
│   ├── forecast.json              # Market forecast data
│   ├── processed/
│   │   ├── programs.json          # Processed programs
│   │   └── qc_report.json         # Quality control reports
│   └── signals/
│       └── scrape_trigger.json    # Trigger signals for local machine
├── scripts/
│   ├── local_monitor.py           # Local machine monitor
│   ├── qc_validator.py            # Quality control validator
│   └── scrapers/
│       └── scrape_all.py          # Main scraping script
└── requirements.txt               # Python dependencies
```

### Key Concepts

- **Signal File**: A JSON file created by the workflow to communicate with local machine
- **QC Validation**: Quality control checks that ensure data integrity
- **Workflow Dispatch**: GitHub Actions feature for manual workflow triggering
- **GitHub Pages**: Static site hosting directly from repository

### Support

For issues or questions:
1. Create an issue in the GitHub repository
2. Check existing issues for similar problems
3. Review GitHub Actions logs for error details
4. Consult this documentation

---

## 🎯 Quick Reference

### Essential Commands

```bash
# Start monitoring
python3 scripts/local_monitor.py --watch

# Check for trigger once
python3 scripts/local_monitor.py --check-once

# Force scrape now
python3 scripts/local_monitor.py --scrape

# Run QC validation
python3 scripts/qc_validator.py

# Run scraper manually
python3 scripts/scrapers/scrape_all.py
```

### Important URLs

- **Dashboard**: `https://[username].github.io/[repo-name]/`
- **GitHub Actions**: `https://github.com/[username]/[repo-name]/actions`
- **Repository Settings**: `https://github.com/[username]/[repo-name]/settings`
- **GitHub Issues**: `https://github.com/[username]/[repo-name]/issues`

### Configuration Files

- **Secrets**: Repository Settings → Secrets and variables → Actions
- **Pages**: Repository Settings → Pages
- **Permissions**: Repository Settings → Actions → General

---

**Last Updated**: November 2024  
**Version**: 1.0  
**Maintainer**: NUVIEW Team
