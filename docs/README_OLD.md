# NUVIEW Strategic Pipeline

**Fully Automated Intelligence & Data Platform for Strategic Opportunities**

[![Deploy to GitHub Pages](https://github.com/JacobThielNUVIEW/nuview-strategic-pipeline/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/JacobThielNUVIEW/nuview-strategic-pipeline/actions/workflows/deploy-pages.yml)
[![Daily Global Topographic Sweep](https://github.com/JacobThielNUVIEW/nuview-strategic-pipeline/actions/workflows/daily_ops.yml/badge.svg)](https://github.com/JacobThielNUVIEW/nuview-strategic-pipeline/actions/workflows/daily_ops.yml)

## 🚀 Overview

The NUVIEW Strategic Pipeline is a fully automated, integrated workflow system that:

- **Automatically updates** code, dashboard, and site on every push
- **Triggers local scraping** remotely via an interactive dashboard button
- **Validates data quality** before deploying updates
- **Backs up data** automatically to prevent data loss
- **Monitors and alerts** on errors and failures
- **Deploys continuously** to a live GitHub Pages site

## ✨ Key Features

### 1. 🔄 Continuous Integration & Deployment
- Automatic deployment to GitHub Pages and Netlify on every push to `main`
- Live site updates within 30-60 seconds (Netlify) or 2 minutes (GitHub Pages)
- Integrated QC validation pipeline ensures data quality
- Optimized with CDN, caching, and compression for maximum performance

### 2. 🚀 Remote Scrape Triggering
- **Floating rocket button** on dashboard for easy access
- Password-protected for NUVIEW-only access
- Signals local machine to execute scraping process
- Automatic result propagation back to repository

### 3. 📊 Automated Data Pipeline
- Daily automated scraping at 3:00 AM UTC
- Multi-stage validation and quality control
- Smart merge and conflict resolution
- Error detection and automated alerting

### 4. 💾 Automated Backups
- Daily backups of all data files
- 30-day retention policy
- Integrity verification
- Compressed archives for efficient storage

### 5. 🔒 Security & Access Control
- Token-based authentication for critical operations
- Secure credential management via GitHub Secrets
- Access logging and audit trails
- Rate limiting and abuse prevention

### 6. 🎨 Professional Dashboard
- Modern, responsive UI with NUVIEW branding
- Real-time opportunity tracking
- Interactive pipeline visualization
- Top 10 opportunities matrix

## 🎯 Quick Start

### For Dashboard Users

1. **View the Live Dashboard**: 
   - Primary: [https://salesnuviewspace.netlify.app](https://salesnuviewspace.netlify.app)
   - Alternative: [https://jacobthielnuview.github.io/nuview-strategic-pipeline/](https://jacobthielnuview.github.io/nuview-strategic-pipeline/)

2. **Trigger a Data Update**:
   - Click the floating 🚀 rocket button (bottom-right)
   - Enter your NUVIEW authentication token
   - Follow the instructions to trigger via GitHub Actions

### For Developers

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/JacobThielNUVIEW/nuview-strategic-pipeline.git
   cd nuview-strategic-pipeline
   ```

2. **Run Local Monitor** (for automated scrape detection):
   ```bash
   python3 scripts/local_monitor.py --watch
   ```

3. **Manual Scrape**:
   ```bash
   python3 scripts/scrapers/scrape_all.py
   ```

## 📚 Documentation

- **[Automation Setup Guide](AUTOMATION_SETUP.md)** - Complete setup instructions
- **[Netlify Deployment Guide](NETLIFY_DEPLOYMENT.md)** - Netlify deployment and configuration
- **[Setup Script README](SETUP_SCRIPT_README.md)** - Original setup documentation
- **[Pipeline Matrix README](dashboard/PIPELINE_MATRIX_README.md)** - Dashboard features
- **[Branding Updates](BRANDING_UPDATES.md)** - UI/UX branding guidelines

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                  AUTOMATED WORKFLOW SYSTEM                   │
└─────────────────────────────────────────────────────────────┘

                    ┌──────────────────┐
                    │  GitHub Actions  │
                    │   (Scheduler)    │
                    └────────┬─────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
       ┌───────────┐  ┌───────────┐  ┌───────────┐
       │  Daily    │  │  Backup   │  │  Deploy   │
       │  Scrape   │  │  Data     │  │  Pages    │
       └─────┬─────┘  └─────┬─────┘  └─────┬─────┘
             │              │              │
             ▼              ▼              ▼
       ┌─────────────────────────────────────┐
       │        Data & Repository            │
       │    (opportunities.json, etc.)       │
       └────────────┬────────────────────────┘
                    │
                    ▼
       ┌─────────────────────────────────────┐
       │     GitHub Pages Dashboard          │
       │   (Live Site with Rocket Button)    │
       └─────────────────────────────────────┘
                    │
                    ▼
       ┌─────────────────────────────────────┐
       │      Local Monitor (Optional)       │
       │   (Watches for trigger signals)     │
       └─────────────────────────────────────┘
```

## 🛠️ Workflows

### 1. Daily Global Topographic Sweep
- **Schedule**: Daily at 3:00 AM UTC
- **Trigger**: Automatic / Manual
- **File**: `.github/workflows/daily_ops.yml`
- **Purpose**: Scrape, validate, and update data automatically

### 2. Deploy to GitHub Pages
- **Trigger**: On push to `main`
- **File**: `.github/workflows/deploy-pages.yml`
- **Purpose**: Continuous deployment of dashboard

### 3. Trigger Local Scrape
- **Trigger**: Manual (via dashboard or Actions)
- **File**: `.github/workflows/trigger-local-scrape.yml`
- **Purpose**: Signal local machine to execute scrape

### 4. Automated Backup
- **Schedule**: Daily at 4:00 AM UTC
- **Trigger**: Automatic / Manual
- **File**: `.github/workflows/backup.yml`
- **Purpose**: Create and verify data backups

## 🔧 Configuration

### Required GitHub Secrets

1. **`NUVIEW_SCRAPE_TOKEN`** - Authentication token for triggering scrapes
2. **`GH_PAT`** (Optional) - Personal Access Token for advanced features

### Deployment Options

This repository supports dual deployment:
- **GitHub Pages**: Automatic deployment via `.github/workflows/deploy-pages.yml`
- **Netlify**: Automatic deployment with enhanced performance and CDN
  - See [NETLIFY_DEPLOYMENT.md](NETLIFY_DEPLOYMENT.md) for setup instructions
  - Configured via `netlify.toml` for optimal performance

See [AUTOMATION_SETUP.md](AUTOMATION_SETUP.md) for detailed setup instructions.

## 📈 Data Flow

1. **Data Source** → Scraper script (`scrape_all.py`)
2. **Scraper** → Raw data (`opportunities.json`, `forecast.json`)
3. **QC Validator** → Quality check (`qc_validator.py`)
4. **Validation** → Commit to repository
5. **Git Push** → Triggers deployment workflow
6. **Deployment** → Live dashboard update

## 🎨 Dashboard Features

- **Top 10 Opportunities Matrix** - Highest-value opportunities
- **Pipeline Visualization** - Interactive workflow diagram
- **Category Filtering** - Funding, LiDAR, Space Systems, Platform
- **Global Search** - Find opportunities quickly
- **Floating Rocket Button** - Trigger remote updates
- **NUVIEW Branding** - Professional appearance

## 🤝 Contributing

This is a private NUVIEW project. For questions or issues:

1. Open a GitHub Issue
2. Contact the development team
3. Review workflow logs in Actions tab

## 📝 License

Proprietary - NUVIEW Internal Use Only

## 🙏 Support

For setup assistance or troubleshooting:
- Review the [Automation Setup Guide](AUTOMATION_SETUP.md)
- Check GitHub Actions logs
- Create an issue in the repository

---

**Last Updated**: November 2024  
**Maintained by**: NUVIEW Team
