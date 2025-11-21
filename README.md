# 🚀 NUVIEW Strategic Pipeline

**LIVE SITE:**
[https://jacobthielnuview.github.io/nuview-strategic-pipeline/](https://jacobthielnuview.github.io/nuview-strategic-pipeline/)

**Enterprise-Grade Automated Intelligence & Data Platform for Strategic Business Development**

[![Deploy to GitHub Pages](https://github.com/JacobThielNUVIEW/nuview-strategic-pipeline/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/JacobThielNUVIEW/nuview-strategic-pipeline/actions/workflows/deploy-pages.yml)
[![Daily Global Topographic Sweep](https://github.com/JacobThielNUVIEW/nuview-strategic-pipeline/actions/workflows/daily_ops.yml/badge.svg)](https://github.com/JacobThielNUVIEW/nuview-strategic-pipeline/actions/workflows/daily_ops.yml)

---

## 🎯 Overview

The NUVIEW Strategic Pipeline is a **fully automated, end-to-end business intelligence platform** that continuously monitors, analyzes, and prioritizes global opportunities in topographic mapping, geospatial analytics, and data services—built for modern enterprise and government needs.

**Key Differentiators:**
- ✅ **100% Automated** - Zero manual intervention required
- 📊 **Real-time Dashboard** - Live updates within 30-60 seconds
- 🔄 **Continuous Data Flow** - Scraper → Validator → Generator → Dashboard
- 🛡️ **Quality Assured** - Multi-stage validation with 100% QC pass requirement
- 🌍 **Global Coverage** - 34 specialized scrapers across federal, international, research, and commercial sources

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    AUTOMATED WORKFLOW SYSTEM                                   │
│                                                                               │
│  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐                    │
│  │   GitHub     │     │   Scrapers   │     │   Quality    │                    │
│  │   Actions    │ ──> │   (34)       │ ──> │   Control    │                    │
│  │  Scheduler   │     │              │     │   Validator  │                    │
│  └──────────────┘     └──────────────┘     └──────┬───────┘                    │
│                                                     │                          │
│                                            ┌────────▼────────┐                 │
│                                            │   Programs      │                 │
│                                            │   Generator     │                 │
│                                            └────────┬────────┘                 │
│                                                     │                          │
│  ┌──────────────────────────────────────────────────▼──────────┐               │
│  │              DATA REPOSITORY                                 │               │
│  │  • opportunities.json  • forecast.json  • programs.json     │               │
│  └──────────────────────────┬───────────────────────────────────┘               │
│                             │                                       │
│                             ▼                                       │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │           LIVE DASHBOARD (GitHub Pages)                     │   │
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
├── 📄 netlify.toml            # Netlify configuration (legacy)
├── 📄 robots.txt              # SEO configuration
└── 📄 CNAME                   # Custom domain configuration (if any)
```

---

## 🚀 Quick Start

### For Dashboard Users

1. **View Live Dashboard**:
   - [https://jacobthielnuview.github.io/nuview-strategic-pipeline/](https://jacobthielnuview.github.io/nuview-strategic-pipeline/)

2. **Trigger Data Update:**
   - Click floating 🚀 rocket button (bottom-right)
   - Enter NUVIEW authentication token
   - Follow instructions to trigger via GitHub Actions

### For Developers

1. **Clone Repository:**
   ```bash
   git clone https://github.com/JacobThielNUVIEW/nuview-strategic-pipeline.git
   cd nuview-strategic-pipeline
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Scraper Manually:**
   ```bash
   python scripts/scrapers/scrape_all.py
   ```

4. **Generate Dashboard Data:**
   ```bash
   python scripts/generate_programs.py
   ```

5. **Validate Data Quality:**
   ```bash
   python scripts/qc_validator.py
   ```

---

## (Remaining content unchanged, existing TOC and sections retained)
