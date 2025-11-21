# NUVIEW Strategic Pipeline

**Global Budget & Workflow Intelligence for Space-Based LiDAR Topographic Mapping**

[![Daily Sweep](https://github.com/JacobThielNUVIEW/nuview-strategic-pipeline/actions/workflows/daily_ops.yml/badge.svg)](https://github.com/JacobThielNUVIEW/nuview-strategic-pipeline/actions/workflows/daily_ops.yml)
[![Deploy Pages](https://github.com/JacobThielNUVIEW/nuview-strategic-pipeline/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/JacobThielNUVIEW/nuview-strategic-pipeline/actions/workflows/deploy-pages.yml)

## 🎯 Mission

The NUVIEW Strategic Pipeline is an automated intelligence system designed to identify, track, and prioritize global opportunities for **space-based LiDAR topographic data collection** with a focus on **large-area mapping** and **bare-earth/DEM/DSM products**.

## 🌟 Key Features

### Comprehensive Data Collection
- **34 Specialized Scrapers** covering federal agencies, international space organizations, research institutions, and commercial platforms
- **Multilingual Support** with keywords in 8 languages (English, Spanish, French, German, Italian, Portuguese, Japanese, Chinese, Russian)
- **Daily Automated Updates** via GitHub Actions workflow
- **38+ Active Opportunities** tracked from global sources

### Intelligent Priority Scoring
- **0-200 Point Scoring System** based on:
  - Keyword relevance to space-based LiDAR and topographic mapping
  - Contract value and funding amount
  - Deadline urgency
  - Strategic fit with NUVIEW capabilities
  - Space-based mission bonus multipliers

### Quality Assurance
- **Automated QC Validation** ensuring data quality and completeness
- **Deduplication** to prevent duplicate opportunities
- **Topographic Relevance Filtering** using advanced keyword matching
- **Unicode Support** for international character handling

### Interactive Dashboard
- **Real-time Opportunity Tracking** with priority matrix visualization
- **Category Filtering** (DaaS, R&D, Platform)
- **Urgency Indicators** (Urgent, Near-term, Future)
- **Global Search** across all fields
- **Pipeline Flow Visualization** with interactive tooltips

---

## 📊 Scraper Matrix

### US Federal Agencies (9 Scrapers)
| Agency | Focus Area | Typical Contract Size |
|--------|-----------|---------------------|
| **USGS 3DEP** | National 3D Elevation Program, QL0/QL1 LiDAR | $40M - $220M |
| **NASA** | ICESat-2, GEDI, Space-based Earth observation | $12M - $50M |
| **NOAA** | Coastal topobathy, bathymetric LiDAR | $18M - $35M |
| **USACE** | Flood mapping, infrastructure DEM | $30M - $45M |
| **FEMA** | Risk MAP elevation data, flood modeling | $25M - $35M |
| **NGA** | Geospatial intelligence, 3D mapping | $40M - $60M |
| **DIU** | Defense innovation, next-gen spaceborne LiDAR | $10M - $20M |
| **USDA Forest Service** | Forest inventory, canopy height mapping | $20M - $30M |
| **BLM** | Public lands topographic mapping | $15M - $25M |

### International Space Agencies (8 Scrapers)
| Agency | Region | Focus Area |
|--------|--------|-----------|
| **ESA** | Europe | Copernicus, Digital Twin Earth |
| **JAXA** | Japan | ALOS missions, topographic mapping |
| **CSA** | Canada | Arctic terrain mapping |
| **DLR** | Germany | TanDEM-X follow-on missions |
| **ISRO** | India | National topographic mapping |
| **UKSA** | UK | Climate & environment monitoring |
| **CNSA** | China | Belt & Road Initiative mapping |
| **ASI** | Italy | COSMO-SkyMed enhancement |

### Research Institutions (6 Scrapers)
| Institution | Type | Typical Grant Size |
|------------|------|-------------------|
| **NSF** | Federal research | $8M - $15M |
| **DOE** | Energy/environmental | $10M - $20M |
| **NIH** | Geospatial health | $5M - $10M |
| **EU Horizon** | European research | $30M - $50M |
| **MIT Lincoln Lab** | Defense research | $15M - $25M |
| **Caltech JPL** | NASA partnership | $15M - $25M |

### Commercial & State/Local (11 Scrapers)
| Organization | Category | Focus |
|-------------|----------|-------|
| **Amazon AWS** | Cloud platform | Earth on AWS elevation services |
| **Google Earth Engine** | Analytics platform | Global DEM integration |
| **ESRI** | GIS platform | Living Atlas premium layers |
| **Microsoft** | Cloud platform | Planetary Computer terrain |
| **Maxar** | Geospatial intel | 3D intelligence products |
| **Planet Labs** | EO analytics | Fusion platform integration |
| **California** | State government | Wildfire/flood planning |
| **Texas** | State government | Coastal resilience |
| **Florida** | State government | Topobathy coastal mapping |
| **NYC** | Local government | Urban 3D modeling |
| **World Bank** | International dev | Climate resilience (global) |

---

## 🏗️ Architecture

```
nuview-strategic-pipeline/
├── scripts/
│   ├── global_keywords.py          # Multilingual keyword library
│   ├── validate_and_merge.py       # Data validation & priority scoring
│   ├── qc_validator.py             # Quality control checks
│   └── scrapers/
│       ├── base_scraper.py         # Base class for all scrapers
│       ├── scrape_all.py           # Master orchestrator (34 scrapers)
│       ├── federal_scrapers.py     # US federal agency scrapers
│       ├── international_scrapers.py # Space agency scrapers
│       ├── research_scrapers.py    # Research institution scrapers
│       └── commercial_state_scrapers.py # Commercial/state scrapers
├── data/
│   ├── opportunities.json          # Current opportunities (with priority scores)
│   ├── forecast.json              # Market forecast data
│   ├── scraper_stats.json         # Scraper performance statistics
│   └── processed/
│       ├── qc_report.json         # Quality control report
│       └── programs.json          # Processed program data
├── dashboard/
│   ├── index.html                 # Main dashboard
│   ├── pipeline.html              # Pipeline visualization
│   ├── pipeline_matrix.html       # Detailed matrix view
│   └── global-tracker.html        # Global opportunity tracker
├── .github/workflows/
│   ├── daily_ops.yml             # Daily automated scraping
│   └── deploy-pages.yml          # GitHub Pages deployment
└── README.md                      # This file
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+ (3.10+ recommended)
- Git
- Internet connection for data collection

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/JacobThielNUVIEW/nuview-strategic-pipeline.git
cd nuview-strategic-pipeline
```

2. **No external dependencies required:**
All scripts use Python standard library modules only.

3. **Run the pipeline:**
```bash
python3 scripts/scrapers/scrape_all.py
```

4. **Validate data:**
```bash
python3 scripts/qc_validator.py
```

5. **Add priority scores:**
```bash
python3 scripts/validate_and_merge.py
```

### Automated Setup (macOS)
See [SETUP_SCRIPT_README.md](SETUP_SCRIPT_README.md) for automated installation and scheduling.

---

## 💻 Usage

### Manual Execution

**Run complete pipeline:**
```bash
# 1. Scrape all sources (34 scrapers)
python3 scripts/scrapers/scrape_all.py

# 2. Validate data quality
python3 scripts/qc_validator.py

# 3. Calculate priority scores and merge
python3 scripts/validate_and_merge.py
```

**Test keyword matching:**
```bash
python3 scripts/global_keywords.py
```

### Automated Daily Updates

The pipeline runs automatically at 3 AM UTC daily via GitHub Actions:
- Scrapes all 34 sources
- Validates data quality
- Commits updates if QC passes
- Deploys dashboard updates

View workflow status: [Actions Tab](https://github.com/JacobThielNUVIEW/nuview-strategic-pipeline/actions)

---

## 📈 Data Schema

### Opportunity Record Format
```json
{
  "id": "usgs-702",
  "title": "USGS 3DEP LiDAR Acquisition 2026",
  "agency": "USGS",
  "pillar": "Federal",
  "category": "DaaS",
  "description": "Large-area spaceborne LiDAR for National 3D Elevation Program",
  "amountUSD": 217000000,
  "valueUSD": 217000000,
  "daysUntilDeadline": 28,
  "deadline": "2025-12-15",
  "urgency": "urgent",
  "next_action": "Submit Demo Brief",
  "priorityScore": 134,
  "priorityLabel": "top USA: score 134",
  "scrapedAt": "2025-11-20T23:14:28Z",
  "forecast_value": "$217,000,000",
  "link": "https://sam.gov",
  "budgetSourceLink": "#",
  "agencyLink": "https://www.usgs.gov/3d-elevation-program",
  "timeline": {
    "daysUntil": 28,
    "urgency": "urgent"
  },
  "funding": {
    "amountUSD": 217000000
  }
}
```

### Priority Scoring Formula

**Total Score (0-200 points):**

1. **Keyword Relevance (0-100 points)**
   - Core LiDAR terms: 10 points each
   - Space mission terms: 15 points each  
   - Topographic terms: 8 points each
   - National programs: 12 points each
   - DaaS keywords: 10 points each
   - High priority (space-based, large-area): 20 points each

2. **Funding Amount (0-50 points)**
   - $100M+: 50 points
   - $50M-$100M: 40 points
   - $10M-$50M: 30 points
   - $1M-$10M: 20 points
   - $100K-$1M: 10 points

3. **Urgency (0-30 points)**
   - Urgent (<30 days): 30 points
   - Near-term (30-90 days): 20 points
   - Future (>90 days): 10 points

4. **Space-Based Bonus (0-20 points)**
   - Contains: space-based, spaceborne, satellite, ICESat: +20 points

---

## 🔍 Keyword Coverage

### Core Technologies
- LiDAR, laser altimetry, photon counting
- Space-based, spaceborne, satellite sensors
- ICESat-2, ATLAS, GEDI, GLAS
- Point cloud, laser returns, full waveform

### Topographic Products
- DEM (Digital Elevation Model)
- DSM (Digital Surface Model)
- DTM (Digital Terrain Model)
- Bare-earth, ground surface
- Bathymetry, topobathy

### Programs & Standards
- USGS 3DEP, National Elevation Dataset
- Quality Levels: QL0, QL1, QL2
- LiDAR Base Specification (LBS)
- Data formats: LAS, LAZ, E57

### Multilingual Support
- Spanish: topografía, modelo digital de elevación
- French: topographie, modèle numérique d'élévation
- German: topographie, digitales höhenmodell
- Italian: topografia, modello digitale di elevazione
- Portuguese: topografia, modelo digital de elevação
- Japanese: 地形, 数値標高モデル
- Chinese: 地形, 数字高程模型
- Russian: топография, цифровая модель рельефа

---

## 📊 Dashboard Features

Access the live dashboard: [GitHub Pages](https://jacobthielnuview.github.io/nuview-strategic-pipeline/)

### Main Dashboard (`dashboard/index.html`)
- **Executive Overview** with key metrics
- **Top 10 Opportunity Matrix** with priority ranking
- **Interactive Pipeline Diagram** with tooltips
- **Category Filtering** (Funding, LiDAR, Space Systems, Platform)
- **Global Search** across all fields
- **Urgency Badges** for quick status identification

### Pipeline Matrix (`dashboard/pipeline_matrix.html`)
- Detailed opportunity breakdown
- Source attribution
- Budget links
- Agency websites

### Global Tracker (`dashboard/global-tracker.html`)
- Geographic distribution
- International opportunities
- Agency coverage map

---

## 🔒 Quality Control

### Automated Validation (`qc_validator.py`)
- **Schema Validation**: Required fields present
- **Data Type Checks**: Numeric fields are numbers
- **Category Validation**: Valid categories (DaaS, R&D, Platform)
- **Urgency Validation**: Valid urgency levels
- **Topographic Relevance**: Keyword-based filtering
- **Count Verification**: Meta count matches array length

### QC Report Format
```json
{
  "timestamp": "2025-11-20T23:14:28Z",
  "qc_status": "PASS",
  "qc_percentage": 100,
  "total_errors": 0,
  "total_warnings": 2,
  "opportunities_validation": {
    "errors": [],
    "warnings": ["Opportunity may not be topographic-related"]
  },
  "summary": "QC PASSED with 0 errors and 2 warnings"
}
```

---

## 🤝 Contributing

This is a proprietary repository for NUVIEW Space Technologies, Inc.

For internal contributions:
1. Create a feature branch
2. Make changes
3. Test with `python3 scripts/scrapers/scrape_all.py`
4. Validate with `python3 scripts/qc_validator.py`
5. Submit pull request

---

## 📝 License

Proprietary - NUVIEW Space Technologies, Inc.  
All rights reserved.

---

## 🔗 Key Threads & Focus Areas

### NUVIEW Critical Threads
1. **Space-Based LiDAR DaaS**: Commercial spaceborne elevation services
2. **Large-Area Topographic Collections**: Continental/national scale mapping
3. **Bare-Earth DEM/DSM Production**: High-quality ground surface models
4. **ICESat-2 Integration**: NASA mission data partnerships
5. **Federal 3DEP Expansion**: USGS program participation
6. **International Partnerships**: ESA, JAXA, CSA collaborations
7. **Platform Integrations**: AWS, Google, ESRI, Microsoft partnerships

### Target Markets
- Federal agencies (USGS, NASA, NOAA, FEMA, NGA)
- State governments (CA, TX, FL)
- International space agencies
- Commercial geospatial platforms
- Research institutions

---

## 📞 Support

For questions or issues:
- Internal: Contact NUVIEW Strategic Team
- Technical: Review workflow logs in GitHub Actions
- Data Quality: Check QC reports in `data/processed/qc_report.json`

---

## 🎯 Roadmap

### Completed ✅
- 34 specialized scrapers
- Multilingual keyword system (8 languages)
- Priority scoring algorithm
- Automated QC validation
- GitHub Actions automation
- Interactive dashboard

### Upcoming 🚧
- Machine learning-based relevance scoring
- Automated proposal generation
- Integration with CRM systems
- Real-time slack/email notifications
- Historical trend analysis
- Competitive intelligence module

---

**Last Updated:** November 2025  
**Version:** 2.0  
**Maintained by:** NUVIEW Space Technologies Strategic Team