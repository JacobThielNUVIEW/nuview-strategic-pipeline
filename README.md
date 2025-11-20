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
├── index.html              # Main dashboard UI redirect
├── dashboard/
│   ├── index.html          # Main strategic dashboard
│   ├── pipeline.html       # Pipeline view dashboard
│   ├── pipeline_matrix.html # Interactive flow visualization
│   └── global-tracker.html # Global opportunity tracker
├── data/
│   ├── opportunities.json  # Current opportunity pipeline (auto-updated)
│   ├── forecast.json       # Market forecast data (auto-updated)
│   └── processed/
│       ├── priority_matrix.csv # Global programs data for tracker
│       └── qc_report.json      # Quality control reports
├── scripts/
│   ├── scrapers/
│   │   └── scrape_all.py   # Daily data collection script
│   └── qc_validator.py     # Data quality validation
├── .github/
│   └── workflows/
│       ├── daily_ops.yml   # Automated daily updates
│       └── deploy-pages.yml # GitHub Pages deployment
└── requirements.txt        # Python dependencies
```

## Setup

### Prerequisites

- Python 3.10+
- Web browser (for viewing dashboard)

### Quick Start with Automated Setup Script (macOS)

For macOS users, we provide an automated setup script that handles everything:

```bash
# Download and run the setup script
curl -O https://raw.githubusercontent.com/JacobThielNUVIEW/nuview-strategic-pipeline/main/setup_and_run.sh
chmod +x setup_and_run.sh
./setup_and_run.sh --run-pipeline
```

This script will:
- Clone the repository to `/Users/JThiel/Documents/NUVIEW_Pipeline_tool/`
- Set up a Python virtual environment
- Install dependencies
- Run the data collection and validation scripts

For detailed documentation, see [SETUP_SCRIPT_README.md](SETUP_SCRIPT_README.md)

### Manual Installation

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

### Main Dashboard (`dashboard/index.html`)
1. **Executive Overview**: High-level market statistics and revenue targets
2. **Market Forecast**: Regional growth projections with CAGR analysis
3. **Priority Matrix**: Live data prioritization grid
4. **Analytics**: Charts showing opportunity distribution
5. **Critical Actions**: Live feed of upcoming deadlines and required actions

### Pipeline Dashboard (`dashboard/pipeline.html`)
1. **Summary Statistics**: Total opportunities, pipeline value, urgent actions, and LiDAR-prioritized count
2. **Agency Budget Funnel**: Filterable table organized by agency with sorting capabilities
3. **Current Opportunities**: Comprehensive table with DataTables for advanced filtering and sorting
4. **Market Forecast Summary**: Key forecast metrics and legislative targets

### Global Tracker (`dashboard/global-tracker.html`)
1. **Top 10 Programs**: Card-based display of top 10 global space/LiDAR programs by priority score
2. **Global Priority Matrix**: Comprehensive table showing all countries, agencies, programs, budgets, and NUVIEW priority scores
3. **Smart Highlighting**: Programs with priority score > 90 are highlighted for quick identification
4. **Data Access Information**: Shows data access type (Open, Commercial, Restricted, etc.) for each program
5. **Source Links**: Direct links to official program sources

## Updating Dashboard Data

The dashboards are fully data-driven and pull information from JSON files in the `/data` directory.

### Updating Opportunities

Edit `/data/opportunities.json` to add, modify, or remove opportunities. Follow this schema:

```json
{
  "meta": {
    "market_val": "14.13",
    "cagr": "19.43",
    "updated": "2025-11-20T03:58:04Z",
    "totalCount": 8
  },
  "opportunities": [
    {
      "id": "unique-id",
      "title": "Opportunity Title",
      "agency": "Agency Name",
      "pillar": "Federal/Commercial/Research",
      "category": "DaaS/R&D/Platform",
      "forecast_value": "$X,XXX,XXX",
      "link": "https://link-to-opportunity",
      "deadline": "YYYY-MM-DD",
      "next_action": "Action description",
      "timeline": {
        "daysUntil": 30,
        "urgency": "urgent/near/future"
      },
      "funding": {
        "amountUSD": 1000000
      }
    }
  ]
}
```

**Key Fields:**
- `urgency`: Set to "urgent" (< 30 days), "near" (30-90 days), or "future" (> 90 days)
- `category`: Use "DaaS" for LiDAR-specific opportunities (they get prioritized in summary)
- `amountUSD`: Numeric value in USD for proper sorting and calculations
- `daysUntil`: Can be negative for past deadlines

### Updating Market Forecast

Edit `/data/forecast.json` to update market projections:

```json
{
  "current_year": 2025,
  "current_value": 3.27,
  "forecast_2030": 403.0,
  "cagr_pct": 4.3,
  "legislative_targets": [
    {
      "bill": "Bill name or number",
      "impact": "Description of impact"
    }
  ]
}
```

### Updating Global Tracker Data

Edit `/data/processed/priority_matrix.csv` to add, modify, or remove global programs. Follow this schema:

```csv
country,agency_name,program_name,budget_amount_usd,nuview_priority_score,data_access,sources
United States,NASA,Earth System Observatory,850000000,95,Open,https://science.nasa.gov/earth/
```

**Key Fields:**
- `country`: Country or region name
- `agency_name`: Space agency or organization name
- `program_name`: Name of the space/LiDAR program
- `budget_amount_usd`: Budget in USD (numeric value, no commas)
- `nuview_priority_score`: Priority score from 0-100 (programs > 90 are highlighted)
- `data_access`: Data access type (Open, Commercial, Restricted, Open Partnership, Government)
- `sources`: URL to official program source (use first URL from comma-separated list)

### Testing Changes Locally

After updating data files:

1. Start local server:
   ```bash
   python -m http.server 8000
   ```

2. Open browsers to test all dashboards:
   - Main: `http://localhost:8000/dashboard/index.html`
   - Pipeline: `http://localhost:8000/dashboard/pipeline.html`
   - Global Tracker: `http://localhost:8000/dashboard/global-tracker.html`

3. Verify:
   - All tables populate correctly
   - Filtering and sorting work
   - Summary statistics calculate properly
   - No console errors

### Using the Pipeline Dashboard

**Filtering:**
- Click agency buttons to filter the Agency Budget Funnel table
- Use DataTables search boxes for custom filtering

**Sorting:**
- Click any column header to sort
- Default sort: Urgency (ascending) then Value (descending)

**Summary Calculations:**
- **LiDAR-Prioritized**: Counts opportunities with category "DaaS" or containing "LiDAR" in title
- **Urgent Actions**: Counts opportunities with urgency = "urgent"
- **Total Pipeline Value**: Sums all opportunity funding amounts

## GitHub Pages Deployment

This repository is configured to deploy to GitHub Pages automatically. The deployment workflow is triggered on every push to the `main` branch.

### Initial Setup

To enable GitHub Pages for the first time:

1. Go to repository **Settings** → **Pages**
2. Under **Source**, select **GitHub Actions**
3. The workflow will automatically deploy on the next push to `main`

The dashboard will be accessible at: `https://jacobthielnuview.github.io/nuview-strategic-pipeline/`

### SEO Privacy

The site is configured with search engine privacy measures:
- **robots.txt** at the repository root blocks all crawlers
- **Meta robots tag** (`<meta name="robots" content="noindex, nofollow">`) in dashboard pages prevents indexing
- The dashboard link is kept unlisted (not advertised in README or main index)

**Note:** This provides privacy through obscurity and noindex directives, not password protection.

### Adding Password Protection (Future Enhancement)

When password protection is needed, consider these options:

#### Option 1: Static Site Password Protection (JavaScript-based)
- **Pros**: Simple, no server required, works with GitHub Pages
- **Cons**: Not highly secure (password visible in source), suitable for basic protection only
- **Implementation**:
  1. Add a password check script at the top of `dashboard/index.html`
  2. Use SHA-256 hashing to verify password
  3. Store hashed password in the HTML (not plaintext)
  4. Example libraries: [PageCrypt](https://github.com/Greenheart/pagecrypt), [StatiCrypt](https://github.com/robinmoisson/staticrypt)

#### Option 2: GitHub Pages with Cloudflare Access
- **Pros**: Secure, professional authentication
- **Cons**: Requires Cloudflare account, more setup
- **Implementation**:
  1. Point a custom domain to GitHub Pages
  2. Configure Cloudflare DNS
  3. Enable Cloudflare Access
  4. Set up authentication rules (email OTP, SSO, etc.)

#### Option 3: Move to Private Hosting
- **Pros**: Full control, secure authentication, can use frameworks like Next.js with NextAuth
- **Cons**: Requires hosting costs (Vercel, Netlify, AWS, etc.)
- **Implementation**:
  1. Deploy to Vercel/Netlify with private repository
  2. Add authentication middleware
  3. Use services like Auth0, NextAuth, or custom authentication

#### Option 4: GitHub Pages with External Auth Service
- **Pros**: Relatively simple, leverages existing services
- **Cons**: Third-party dependency
- **Implementation**:
  1. Use services like Auth0, Firebase Auth, or AWS Cognito
  2. Add authentication script to dashboard pages
  3. Redirect unauthenticated users to login page

**Recommended Approach**: For basic protection, use Option 1 (StatiCrypt). For production-grade security, use Option 2 (Cloudflare Access) or Option 3 (private hosting with proper authentication).

**Current Status**: No password protection is implemented. The dashboard is accessible via direct link but not indexed by search engines.

## Contributing

When adding new opportunities or updating market data:
1. Ensure data follows the JSON schema in existing files
2. Test locally before pushing
3. Verify both dashboards render correctly
4. Update the `totalCount` in meta when adding/removing opportunities

## License

Proprietary - NUVIEW Space Technologies, Inc.
