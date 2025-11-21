#!/usr/bin/env python3
"""
NUVIEW Strategic Pipeline - Run All Scrapers
Orchestrates all 34 specialized scrapers for topographic/LiDAR opportunities
Focus: Space-based LiDAR for large-area topographic collections (bare-earth/DEM/DSM)
"""

import sys
import os

# Add scripts directory to path
sys.path.insert(0, os.path.dirname(__file__))

# Import the main scraping orchestrator
from scrapers.scrape_all import run_pipeline

# List of all 34 scrapers integrated in the pipeline
SCRAPERS = [
    # US Federal Agencies (9 scrapers)
    "USGSScraper",
    "NASAScraper", 
    "NOAAScraper",
    "USACEScraper",
    "FEMAScraper",
    "NGAScraper",
    "DIUScraper",
    "USDAForestScraper",
    "BLMScraper",
    
    # International Space Agencies (8 scrapers)
    "ESAScraper",
    "JAXAScraper",
    "CSAScraper",
    "DLRScraper",
    "ISROScraper",
    "UKSAScraper",
    "CNSAScraper",
    "ASIScraper",
    
    # Research Institutions (6 scrapers)
    "NSFScraper",
    "DOEScraper",
    "NIHGeospatialScraper",
    "EUHorizonScraper",
    "MITScraper",
    "CaltechJPLScraper",
    
    # Commercial & State/Local (11 scrapers)
    "AmazonAWSScraper",
    "GoogleEarthEngineScraper",
    "ESRIScraper",
    "MicrosoftPlanetaryScraper",
    "MaxarScraper",
    "CaliforniaScraper",
    "TexasScraper",
    "FloridaScraper",
    "NYCScraper",
    "WorldBankScraper",
    "PlanetLabsScraper",
]

def main():
    """Main entry point for running all scrapers"""
    print(f"NUVIEW Strategic Pipeline - Running {len(SCRAPERS)} specialized scrapers")
    print("=" * 80)
    
    # Verify we have all 34 scrapers
    if len(SCRAPERS) != 34:
        print(f"⚠️  Warning: Expected 34 scrapers, found {len(SCRAPERS)}")
    
    # Run the pipeline
    try:
        run_pipeline()
        print("\n" + "=" * 80)
        print("✅ Pipeline execution completed successfully")
        return 0
    except Exception as e:
        print(f"\n❌ Pipeline execution failed: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
