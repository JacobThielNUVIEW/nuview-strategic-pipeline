# NUVIEW Strategic Pipeline - Scripts

This directory contains all automation scripts and tools for the NUVIEW Strategic Pipeline system.

## 📁 Directory Structure

```
scripts/
├── scrapers/              # Data collection scrapers
│   ├── scrape_all.py     # Master scraper orchestrator
│   ├── base_scraper.py   # Base scraper class
│   ├── federal_scrapers.py       # US Federal agency scrapers
│   ├── international_scrapers.py # International space agency scrapers
│   ├── research_scrapers.py      # Research institution scrapers
│   ├── commercial_state_scrapers.py # Commercial & state scrapers
│   └── usgs.py           # USGS-specific scraper
├── qc/                   # Quality control tools
│   └── validate_and_merge.py    # Data validation and merge
├── qc_validator.py       # Main QC validation script
├── comprehensive_qc_check.py    # Comprehensive QC checks
├── generate_programs.py  # Auto-generate programs.json from opportunities.json
├── validate_and_merge.py # Validation and merge utilities
├── global_keywords.py    # Global keyword definitions
└── local_monitor.py      # Local scrape trigger monitor
```

## 🔧 Core Scripts

### Data Collection
- **`scrapers/scrape_all.py`** - Orchestrates all 34 specialized scrapers for topographic/LiDAR opportunities
  - Runs automatically via daily_ops.yml workflow
  - Outputs: `data/opportunities.json`, `data/forecast.json`

### Data Processing
- **`generate_programs.py`** - Automatically generates `programs.json` from `opportunities.json`
  - Categorizes opportunities into: Funding, LiDAR, Space Systems, Platform
  - Runs after QC validation in the workflow
  - Enables automated dashboard updates

### Quality Control
- **`qc_validator.py`** - Validates data quality and completeness
  - Checks required fields and data integrity
  - Generates QC report and source verification matrix
  - Outputs: `data/processed/qc_report.json`, `data/processed/sources_matrix.csv`

- **`comprehensive_qc_check.py`** - Additional comprehensive QC checks
  - Index integrity validation
  - Calculation verification
  - Cross-reference validation
  - Matrix integrity checks

- **`full_qc_audit.py`** - Complete repository quality control audit
  - HTML, Python, Shell, JSON, CSV validation
  - Documentation quality checks
  - Data integrity verification
  - Recent updates and regression detection
  - Outputs: `data/processed/full_qc_audit_report.json`
  - See: [docs/FULL_QC_AUDIT.md](../docs/FULL_QC_AUDIT.md)

### Monitoring
- **`local_monitor.py`** - Monitors for remote scrape trigger signals
  - Watches for trigger files from GitHub Actions
  - Executes local scraping when triggered

## 🚀 Usage

### Run All Scrapers
```bash
python scripts/scrapers/scrape_all.py
```

### Generate Programs Data
```bash
python scripts/generate_programs.py
```

### Validate Data Quality
```bash
# Standard QC validation
python scripts/qc_validator.py

# Comprehensive data checks
python scripts/comprehensive_qc_check.py

# Full repository audit
python scripts/full_qc_audit.py
```

### Monitor for Remote Triggers
```bash
python scripts/local_monitor.py --watch
```

## 🔄 Automated Workflow

The scripts are automatically executed by GitHub Actions workflows:

1. **Daily Scraping** (`daily_ops.yml`)
   - Runs: `scrape_all.py` → `qc_validator.py` → `generate_programs.py`
   - Schedule: Daily at 3:00 AM UTC
   - Output: Updated opportunities.json, programs.json, QC reports

2. **Local Scrape Trigger** (`trigger-local-scrape.yml`)
   - Monitored by: `local_monitor.py`
   - Trigger: Manual via dashboard button

## 📝 Development

### Adding New Scrapers
1. Create scraper class in appropriate scrapers file
2. Inherit from `BaseScraper`
3. Implement `scrape()` method
4. Add to scraper list in `scrape_all.py`

### Modifying Data Pipeline
- Update `generate_programs.py` to change categorization logic
- Update `qc_validator.py` to add/modify validation rules
- Test changes locally before committing

## 🔍 Dependencies

See `requirements.txt` in project root:
- pandas >= 2.2.0 (for data processing and CSV export)
- Python 3.11+ required

## 📞 Support

For script issues or questions:
- Check script output logs in GitHub Actions
- Review error messages in QC reports
- Contact NUVIEW development team

---
**Last Updated**: November 2024  
**Maintained by**: NUVIEW Team
