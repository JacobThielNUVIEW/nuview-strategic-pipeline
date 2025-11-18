# NUVIEW Strategic Pipeline

A comprehensive market intelligence and opportunity tracking dashboard for NUVIEW's LiDAR business development.

## Overview

This project provides a real-time view of global LiDAR market opportunities, forecasts, and action items. It combines automated data collection with an interactive web dashboard to track federal contracts, research opportunities, and market trends.

## Features

- **Market Forecast Dashboard**: Interactive visualization of global LiDAR market growth (2026-2034)
- **Opportunity Tracking**: Real-time federal and commercial opportunity pipeline
- **Automated Updates**: Daily intelligence updates via GitHub Actions
- **Responsive Design**: Mobile-friendly interface with NUVIEW branding

## Project Structure

```
.
├── index.html              # Main dashboard UI
├── data/
│   ├── opportunities.json  # Current opportunity pipeline (auto-updated)
│   ├── forecast.json       # Market forecast data (auto-updated)
│   └── priority_matrix.csv # Opportunity prioritization matrix
├── scripts/
│   └── scrapers/
│       └── scrape_all.py   # Daily data collection script
├── .github/
│   └── workflows/
│       └── daily_ops.yml   # Automated daily updates
└── requirements.txt        # Python dependencies
```

## Setup

### Prerequisites

- Python 3.10+
- Web browser (for viewing dashboard)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/JacobThielNUVIEW/nuview-strategic-pipeline.git
cd nuview-strategic-pipeline
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

### Running Locally

1. Generate fresh data:
```bash
python scripts/scrapers/scrape_all.py
```

2. Start a local web server:
```bash
python -m http.server 8000
```

3. Open your browser to: `http://localhost:8000`

## Data Updates

The repository is configured with automated daily updates via GitHub Actions:
- **Schedule**: Daily at 3:00 AM UTC
- **Trigger**: Manual via workflow_dispatch
- **Updates**: Refreshes `opportunities.json` and `forecast.json`

## Dashboard Sections

1. **Executive Overview**: High-level market statistics and revenue targets
2. **Market Forecast**: Regional growth projections with CAGR analysis
3. **Critical Actions**: Live feed of upcoming deadlines and required actions

## Contributing

When adding new opportunities or updating market data:
1. Ensure data follows the JSON schema in existing files
2. Test locally before pushing
3. Verify the dashboard renders correctly

## License

Proprietary - NUVIEW Space Technologies, Inc.
