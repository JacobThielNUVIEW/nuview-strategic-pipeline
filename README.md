# 🚀 NUVIEW Strategic Pipeline

**Enterprise-Grade Automated Intelligence & Data Platform for Strategic Business Development**

[![Deploy to GitHub Pages](https://github.com/JacobThielNUVIEW/nuview-strategic-pipeline/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/JacobThielNUVIEW/nuview-strategic-pipeline/actions/workflows/deploy-pages.yml)
[![Daily Global Topographic Sweep](https://github.com/JacobThielNUVIEW/nuview-strategic-pipeline/actions/workflows/daily_ops.yml/badge.svg)](https://github.com/JacobThielNUVIEW/nuview-strategic-pipeline/actions/workflows/daily_ops.yml)

---

## 🎯 Overview

The NUVIEW Strategic Pipeline is a **fully automated, end-to-end business intelligence platform** that continuously monitors, analyzes, and prioritizes global opportunities in topographic mapping, LiDAR, and space-based Earth observation.

**Key Differentiators:**
- ✅ **100% Automated** - Zero manual intervention required
- 📊 **Real-time Dashboard** - Live updates within 30-60 seconds
- 🔄 **Continuous Data Flow** - Scraper → Validator → Generator → Dashboard
- 🛡️ **Quality Assured** - Multi-stage validation with 100% QC pass requirement
- 🌍 **Global Coverage** - 34 specialized scrapers across federal, international, research, and commercial sources

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                    AUTOMATED WORKFLOW SYSTEM                         │
│                                                                      │
│  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐       │
│  │   GitHub     │     │   Scrapers   │     │   Quality    │       │
│  │   Actions    │ ──> │   (34)       │ ──> │   Control    │       │
│  │  Scheduler   │     │              │     │   Validator  │       │
│  └──────────────┘     └──────────────┘     └──────┬───────┘       │
│                                                     │               │
│                                            ┌────────▼────────┐      │
│                                            │   Programs      │      │
│                                            │   Generator     │      │
│                                            └────────┬────────┘      │
│                                                     │               │
│  ┌──────────────────────────────────────────────────▼──────────┐   │
│  │              DATA REPOSITORY                                 │   │
│  │  • opportunities.json  • forecast.json  • programs.json     │   │
│  └──────────────────────────┬───────────────────────────────────┘   │
│                             │                                       │
│                             ▼                                       │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │           LIVE DASHBOARD (Netlify + GitHub Pages)           │   │
│  │  • Executive Summary  • Pipeline Matrix  • Global Tracker   │   │
│  └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 📂 Repository Structure

```
nuview-strategic-pipeline/
├── 📁 .github/workflows/      # Automated CI/CD pipelines
│   ├── daily_ops.yml          # Daily scraping & data update (3AM UTC)
│   ├── deploy-pages.yml       # Dashboard deployment
│   ├── backup.yml             # Automated backups (4AM UTC)
│   └── trigger-local-scrape.yml # Remote scrape trigger
│
├── 📁 dashboard/              # Live web dashboard
│   ├── index.html             # Main dashboard
│   ├── pipeline.html          # Pipeline visualization
│   ├── pipeline_matrix.html   # Top opportunities matrix
│   ├── global-tracker.html    # Global opportunity tracker
│   ├── executive-summary.html # Executive summary page
│   └── scripts-documentation.html # Scripts documentation
│
├── 📁 scripts/                # Automation scripts & tools
│   ├── scrapers/              # 34 specialized scrapers
│   ├── generate_programs.py   # Auto-generate dashboard data
│   ├── qc_validator.py        # Quality control validation
│   └── local_monitor.py       # Local scrape monitor
│
├── 📁 data/                   # Live data repository
│   ├── opportunities.json     # Raw opportunities data
│   ├── forecast.json          # Market forecast data
│   └── processed/
│       ├── programs.json      # Processed dashboard data
│       ├── qc_report.json     # Quality control report
│       └── sources_matrix.csv # Source verification matrix
│
├── 📁 docs/                   # Comprehensive documentation
│   ├── AUTOMATION_SETUP.md    # Setup guide
│   ├── NETLIFY_DEPLOYMENT.md  # Deployment guide
│   ├── BRANDING_UPDATES.md    # Branding guidelines
│   └── README.md              # Documentation index
│
├── 📁 assets/                 # Static assets
│   └── nuview-logo.svg        # NUVIEW logo
│
├── 📁 backups/                # Automated data backups
│
├── 📄 README.md               # This file
├── 📄 requirements.txt        # Python dependencies
├── 📄 netlify.toml            # Netlify configuration
├── 📄 robots.txt              # SEO configuration
└── 📄 CNAME                   # Custom domain configuration
```

---

## ✨ Key Features

### 🤖 Fully Automated Data Pipeline

**Scraping → Validation → Generation → Deployment** - All automatic, no manual steps

1. **Data Collection** (Daily 3:00 AM UTC)
   - 34 specialized scrapers across federal, international, research, and commercial sources
   - Focus: Space-based LiDAR for large-area topographic collections

2. **Quality Control**
   - Multi-stage validation ensures data integrity
   - Required fields verification
   - Source verification matrix generation
   - 100% QC pass required before deployment

3. **Dashboard Data Generation** (NEW!)
   - Automatically generates `programs.json` from `opportunities.json`
   - Categorizes into: Funding, LiDAR, Space Systems, Platform
   - No manual code changes needed - fully automated

4. **Continuous Deployment**
   - Auto-deploys to Netlify (30-60 seconds)
   - Auto-deploys to GitHub Pages (2 minutes)
   - Live dashboard updates without intervention

### 📊 Professional Dashboard

- **Executive Summary** - High-level KPIs and metrics
- **Pipeline Matrix** - Top 10 opportunities by value
- **Global Tracker** - Comprehensive opportunity tracking
- **Pipeline Visualization** - Interactive workflow diagram
- **Remote Trigger** - Floating rocket button for on-demand updates

### 🔒 Security & Reliability

- Token-based authentication for critical operations
- Automated daily backups with 30-day retention
- Error detection and alerting
- Rate limiting and abuse prevention

---

## 🚀 Quick Start

### For Dashboard Users

1. **View Live Dashboard**:
   - Primary: [https://salesnuviewspace.netlify.app](https://salesnuviewspace.netlify.app)
   - Alternative: [https://jacobthielnuview.github.io/nuview-strategic-pipeline/](https://jacobthielnuview.github.io/nuview-strategic-pipeline/)

2. **Trigger Data Update**:
   - Click floating 🚀 rocket button (bottom-right)
   - Enter NUVIEW authentication token
   - Follow instructions to trigger via GitHub Actions

### For Developers

1. **Clone Repository**:
   ```bash
   git clone https://github.com/JacobThielNUVIEW/nuview-strategic-pipeline.git
   cd nuview-strategic-pipeline
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Scraper Manually**:
   ```bash
   python scripts/scrapers/scrape_all.py
   ```

4. **Generate Dashboard Data**:
   ```bash
   python scripts/generate_programs.py
   ```

5. **Validate Data Quality**:
   ```bash
   python scripts/qc_validator.py
   ```

---

## 📊 Data Flow

### Automated Pipeline (Daily)

```
1. GitHub Actions Scheduler (3:00 AM UTC)
          ↓
2. Run All Scrapers (scrape_all.py)
   • Collects data from 34 sources
   • Outputs: opportunities.json, forecast.json
          ↓
3. Quality Control (qc_validator.py)
   • Validates data integrity
   • Generates QC report & source matrix
   • Must pass 100% to proceed
          ↓
4. Generate Programs Data (generate_programs.py) ✨ NEW!
   • Converts opportunities → programs
   • Categorizes by type
   • Outputs: programs.json
          ↓
5. Commit & Push to Main Branch
   • opportunities.json
   • forecast.json
   • programs.json
   • qc_report.json
          ↓
6. Automatic Dashboard Deployment
   • Netlify (30-60 seconds)
   • GitHub Pages (2 minutes)
          ↓
7. Live Dashboard Updates 🎉
```

---

## 🔧 Configuration

### Required GitHub Secrets

- **`NUVIEW_SCRAPE_TOKEN`** - Authentication for remote scrape triggering
- **`GH_PAT`** (Optional) - Personal Access Token for advanced features

### Deployment Configuration

**Dual Deployment Setup:**
- **Netlify** - Primary deployment with CDN and optimizations
- **GitHub Pages** - Secondary deployment for redundancy

See [`docs/NETLIFY_DEPLOYMENT.md`](docs/NETLIFY_DEPLOYMENT.md) for setup instructions.

---

## 📚 Documentation

### Setup & Configuration
- **[Automation Setup Guide](docs/AUTOMATION_SETUP.md)** - Complete setup instructions
- **[Setup Script README](docs/SETUP_SCRIPT_README.md)** - Original setup documentation

### Deployment
- **[Netlify Deployment Guide](docs/NETLIFY_DEPLOYMENT.md)** - Netlify setup and configuration
- **[Final Deployment Summary](docs/FINAL_DEPLOYMENT_SUMMARY.md)** - Deployment status

### Design & Development
- **[Branding Guidelines](docs/BRANDING_UPDATES.md)** - UI/UX standards
- **[Scripts Documentation](scripts/README.md)** - Script reference guide
- **[Dashboard README](dashboard/PIPELINE_MATRIX_README.md)** - Dashboard features

### Testing & Quality
- **[Testing Report](docs/TESTING_REPORT.md)** - Comprehensive testing results
- **[QC Summary](docs/QC_SUMMARY_REPORT.md)** - Quality control metrics
- **[Optimization Checklist](docs/OPTIMIZATION_CHECKLIST.md)** - Performance improvements

---

## 🛠️ Workflows

### 1. Daily Global Topographic Sweep
- **File**: `.github/workflows/daily_ops.yml`
- **Schedule**: Daily at 3:00 AM UTC
- **Trigger**: Automatic / Manual
- **Purpose**: Scrape, validate, generate, and deploy data automatically

### 2. Deploy to GitHub Pages
- **File**: `.github/workflows/deploy-pages.yml`
- **Trigger**: On push to `main`
- **Purpose**: Continuous dashboard deployment

### 3. Automated Backup
- **File**: `.github/workflows/backup.yml`
- **Schedule**: Daily at 4:00 AM UTC
- **Trigger**: Automatic / Manual
- **Purpose**: Create and verify data backups

### 4. Trigger Local Scrape
- **File**: `.github/workflows/trigger-local-scrape.yml`
- **Trigger**: Manual (via dashboard or Actions)
- **Purpose**: Signal local machine to execute scrape

---

## 🔄 Recent Updates

### Latest Enhancements

✅ **Automated Data Pipeline** (Phase 2 Complete)
- Created `generate_programs.py` to auto-generate dashboard data
- Updated workflows to generate `programs.json` automatically
- Dashboard now updates without any manual code intervention

✅ **Version Standardization** (Phase 1 Complete)
- All workflows use Python 3.11
- Standardized GitHub Actions versions (checkout@v4, setup-python@v5, etc.)
- Updated requirements.txt with explicit versions

---

## 🤝 Contributing

This is a **private NUVIEW project**. For questions or issues:

1. Open a GitHub Issue
2. Contact the NUVIEW development team
3. Review workflow logs in Actions tab

---

## 📝 License

**Proprietary - NUVIEW Internal Use Only**

---

## 🙏 Support

For setup assistance or troubleshooting:
- 📖 Review the [Documentation](docs/README.md)
- 🔍 Check [GitHub Actions Logs](https://github.com/JacobThielNUVIEW/nuview-strategic-pipeline/actions)
- 🐛 Create an [Issue](https://github.com/JacobThielNUVIEW/nuview-strategic-pipeline/issues)
- 📧 Contact NUVIEW development team

---

**Last Updated**: November 2024  
**Version**: 2.0.0 (Automated Pipeline)  
**Maintained by**: NUVIEW Team  
**Status**: 🟢 Production - Fully Operational
