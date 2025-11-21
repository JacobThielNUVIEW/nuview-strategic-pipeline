#!/usr/bin/env python3
"""
NUVIEW Strategic Pipeline - Run All Scrapers
Convenience script to run all scrapers and display results
Usage: python scripts/run_all.py
"""

import sys
import os

# Add scripts directory to path
sys.path.insert(0, os.path.dirname(__file__))

# Import and run the scraper pipeline
from scrapers.scrape_all import run_pipeline

if __name__ == "__main__":
    print("=" * 80)
    print("NUVIEW STRATEGIC PIPELINE - RUN ALL SCRAPERS")
    print("=" * 80)
    print()
    
    # Run the complete pipeline
    run_pipeline()
    
    # Display summary
    print()
    print("=" * 80)
    print("SUMMARY:")
    print("- Check data/opportunities.json for all opportunities")
    print("- Check data/scraper_stats.json for scraper statistics")
    print("- Check data/forecast.json for market forecast")
    print("- Expected: ~128 opportunities from 68 scrapers")
    print("=" * 80)
