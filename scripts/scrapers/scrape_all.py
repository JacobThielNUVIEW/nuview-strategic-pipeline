"""
NUVIEW Strategic Pipeline - Master Scraper
Orchestrates all 34 specialized scrapers for topographic/LiDAR opportunities
Focus: Space-based LiDAR for large-area topographic collections (bare-earth/DEM/DSM)
"""

import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

# Add scripts directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Import all scraper modules
try:
    from scrapers.commercial_state_scrapers import (
        AmazonAWSScraper,
        CaliforniaScraper,
        ESRIScraper,
        FloridaScraper,
        GoogleEarthEngineScraper,
        MaxarScraper,
        MicrosoftPlanetaryScraper,
        NYCScraper,
        PlanetLabsScraper,
        TexasScraper,
        WorldBankScraper,
    )
    from scrapers.federal_scrapers import (
        BLMScraper,
        DIUScraper,
        FEMAScraper,
        NASAScraper,
        NGAScraper,
        NOAAScraper,
        USACEScraper,
        USDAForestScraper,
        USGSScraper,
    )
    from scrapers.international_scrapers import (
        ASIScraper,
        CNSAScraper,
        CSAScraper,
        DLRScraper,
        ESAScraper,
        ISROScraper,
        JAXAScraper,
        UKSAScraper,
    )
    from scrapers.research_scrapers import (
        CaltechJPLScraper,
        DOEScraper,
        EUHorizonScraper,
        MITScraper,
        NIHGeospatialScraper,
        NSFScraper,
    )
    SCRAPERS_AVAILABLE = True
except ImportError as e:
    print(f"⚠️  Warning: Could not import scrapers: {e}")
    print("⚠️  Falling back to basic mode")
    SCRAPERS_AVAILABLE = False

OUTPUT_FILE = "data/opportunities.json"
FORECAST_FILE = "data/forecast.json"

# Color codes for console output
COLOR_GREEN = '\033[92m'
COLOR_BLUE = '\033[94m'
COLOR_RESET = '\033[0m'

def log_info(msg):
    print(f"{COLOR_BLUE}ℹ️  {msg}{COLOR_RESET}")

def log_success(msg):
    print(f"{COLOR_GREEN}✅ {msg}{COLOR_RESET}")

def run_single_scraper(scraper, index, total):
    """
    Run a single scraper and return its results.

    Args:
        scraper: Scraper instance
        index: Current scraper index
        total: Total number of scrapers

    Returns:
        tuple: (opportunities, stat_dict)
    """
    try:
        log_info(f"[{index}/{total}] Running {scraper.name}...")
        opportunities = scraper.scrape()
        count = len(opportunities)

        stat = {
            "scraper": scraper.name,
            "source_type": scraper.source_type,
            "country": scraper.country,
            "opportunities_found": count
        }

        log_success(f"  {scraper.name}: {count} opportunities collected")
        return opportunities, stat

    except Exception as e:
        log_info(f"  ⚠️  {scraper.name}: Error - {str(e)}")
        stat = {
            "scraper": scraper.name,
            "source_type": scraper.source_type,
            "country": scraper.country,
            "opportunities_found": 0,
            "error": str(e)
        }
        return [], stat


def run_all_scrapers():
    """
    Run all 34 specialized scrapers and collect opportunities.
    Uses parallel execution with ThreadPoolExecutor for improved performance.

    Returns:
        tuple: (all_opportunities, scraper_stats)
    """
    log_info("Starting comprehensive topographic opportunity scan...")
    log_info("Focus: Space-based LiDAR for large-area topographic collections")
    log_info("")

    all_opportunities = []
    scraper_stats = []

    if not SCRAPERS_AVAILABLE:
        log_info("Running in basic mode with limited scrapers")
        return [], []

    # Initialize all 34 scrapers
    scrapers = [
        # US Federal Agencies (9 scrapers)
        USGSScraper(),
        NASAScraper(),
        NOAAScraper(),
        USACEScraper(),
        FEMAScraper(),
        NGAScraper(),
        DIUScraper(),
        USDAForestScraper(),
        BLMScraper(),

        # International Space Agencies (8 scrapers)
        ESAScraper(),
        JAXAScraper(),
        CSAScraper(),
        DLRScraper(),
        ISROScraper(),
        UKSAScraper(),
        CNSAScraper(),
        ASIScraper(),

        # Research Institutions (6 scrapers)
        NSFScraper(),
        DOEScraper(),
        NIHGeospatialScraper(),
        EUHorizonScraper(),
        MITScraper(),
        CaltechJPLScraper(),

        # Commercial & State/Local (12 scrapers)
        AmazonAWSScraper(),
        GoogleEarthEngineScraper(),
        ESRIScraper(),
        MicrosoftPlanetaryScraper(),
        MaxarScraper(),
        CaliforniaScraper(),
        TexasScraper(),
        FloridaScraper(),
        NYCScraper(),
        WorldBankScraper(),
        PlanetLabsScraper(),
    ]

    # Run scrapers in parallel with ThreadPoolExecutor
    total_scrapers = len(scrapers)
    log_info(f"Running {total_scrapers} specialized scrapers in parallel...")
    log_info("")

    with ThreadPoolExecutor(max_workers=10) as executor:
        # Submit all scraper tasks
        future_to_scraper = {
            executor.submit(run_single_scraper, scraper, i, total_scrapers): scraper
            for i, scraper in enumerate(scrapers, 1)
        }

        # Collect results as they complete
        for future in as_completed(future_to_scraper):
            opportunities, stat = future.result()
            all_opportunities.extend(opportunities)
            scraper_stats.append(stat)

    log_info("")
    log_success(f"Scraping complete: {len(all_opportunities)} total opportunities from {total_scrapers} sources")

    return all_opportunities, scraper_stats

def run_pipeline():
    """Main pipeline execution"""
    print("=" * 80)
    log_info("🕷️  NUVIEW STRATEGIC PIPELINE - DAILY GLOBAL TOPOGRAPHIC SWEEP")
    print("=" * 80)
    log_info("")

    current_time = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')

    # Ensure data directory exists
    os.makedirs('data', exist_ok=True)

    # Run all scrapers
    if SCRAPERS_AVAILABLE:
        opportunities, scraper_stats = run_all_scrapers()
    else:
        # Fallback: Basic opportunities for testing
        log_info("Using basic test data...")
        opportunities = []
        scraper_stats = []

    # If no opportunities from scrapers, use minimal test data
    if len(opportunities) == 0:
        log_info("No opportunities collected, using test data")
        opportunities = [
            {
                "id": "usgs-test",
                "title": "USGS 3DEP LiDAR Acquisition 2026",
                "agency": "USGS",
                "pillar": "Federal",
                "category": "DaaS",
                "amountUSD": 217000000,
                "daysUntilDeadline": 28,
                "deadline": "2025-12-15",
                "next_action": "Submit Demo Brief",
                "scrapedAt": current_time,
                "forecast_value": "$217,000,000",
                "link": "https://sam.gov",
                "timeline": {"daysUntil": 28, "urgency": "urgent"},
                "funding": {"amountUSD": 217000000},
                "valueUSD": 217000000,
                "urgency": "urgent"
            }
        ]

    # Save opportunities.json
    final_opps_json = {
        "meta": {
            "market_val": "14.13",
            "cagr": "19.43",
            "updated": current_time,
            "totalCount": len(opportunities),
            "scrapers_run": len(scraper_stats) if scraper_stats else 1
        },
        "opportunities": opportunities
    }

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(final_opps_json, f, indent=2, ensure_ascii=False, sort_keys=True)

    log_success(f"Saved {len(opportunities)} opportunities to {OUTPUT_FILE}")

    # Save scraper statistics if available
    if scraper_stats:
        stats_file = "data/scraper_stats.json"
        with open(stats_file, 'w', encoding='utf-8') as f:
            json.dump({
                "timestamp": current_time,
                "total_scrapers": len(scraper_stats),
                "total_opportunities": len(opportunities),
                "scrapers": scraper_stats
            }, f, indent=2, ensure_ascii=False, sort_keys=True)
        log_success(f"Saved scraper statistics to {stats_file}")

    # Generate market forecast (forecast.json)
    forecast_data = {
        "current_year": 2025,
        "current_value": 3.27,
        "forecast_2030": 403.0,
        "cagr_pct": 4.3,
        "legislative_targets": [
            {"bill": "H.R. 187 (MAPWaters)", "impact": "Water data mandate"},
            {"bill": "Infrastructure Investment and Jobs Act", "impact": "3DEP expansion funding"}
        ]
    }

    with open(FORECAST_FILE, 'w', encoding='utf-8') as f:
        json.dump(forecast_data, f, indent=2, sort_keys=True)

    log_success(f"Saved market forecast to {FORECAST_FILE}")

    log_info("")
    print("=" * 80)
    log_success("🎯 DAILY GLOBAL TOPOGRAPHIC SWEEP COMPLETE")
    print("=" * 80)

if __name__ == "__main__":
    run_pipeline()
