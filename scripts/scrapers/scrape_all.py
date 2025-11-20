import json
import random
from datetime import datetime, timezone
import os

OUTPUT_FILE = "data/opportunities.json"
FORECAST_FILE = "data/forecast.json"

OPPORTUNITIES = [
    {"title": "USGS 3DEP LiDAR Acquisition 2026", "agency": "USGS", "amountUSD": 217000000, "daysUntilDeadline": 28, "category": "DaaS", "deadline": "2025-12-15", "next_action": "Submit Demo Brief"},
    {"title": "NASA ROSES Omnibus Earth Observation", "agency": "NASA", "amountUSD": 50000000, "daysUntilDeadline": 120, "category": "R&D", "deadline": "2026-03-01", "next_action": "Proposal Dev"},
    {"title": "ESA Digital Twin Earth Platform", "agency": "ESA", "amountUSD": 8000000, "daysUntilDeadline": 45, "category": "Platform", "deadline": "2026-01-20", "next_action": "Consortium Lead"},
    {"title": "DIU Spaceborne LiDAR BAA", "agency": "DIU", "amountUSD": 10000000, "daysUntilDeadline": 15, "category": "R&D", "deadline": "2025-12-01", "next_action": "Submit Whitepaper"}
]


def get_urgency(days):
    """Calculate urgency level based on days until deadline."""
    if days < 30:
        return "urgent"
    if days < 90:
        return "near"
    return "future"


def run_pipeline():
    """Main pipeline function to generate opportunities and forecast data."""
    print("🕷️  RUNNING DAILY INTEL UPDATE...")
    current_time = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    
    processed = []
    for opp in OPPORTUNITIES:
        clean_agency = opp['agency'].lower().replace(' ', '-').replace('/', '-')
        processed_opp = {
            "id": f"{clean_agency}-{random.randint(100, 999)}",
            "title": opp["title"],
            "agency": opp["agency"],
            "scrapedAt": current_time,
            "pillar": "Federal",
            "category": opp["category"],
            "forecast_value": f"${opp['amountUSD']:,}",
            "link": "https://sam.gov",
            "deadline": opp["deadline"],
            "next_action": opp["next_action"],
            "timeline": {
                "daysUntil": opp["daysUntilDeadline"],
                "urgency": get_urgency(opp["daysUntilDeadline"])
            },
            "funding": {
                "amountUSD": opp["amountUSD"]
            },
            # Keep legacy fields for backward compatibility
            "amountUSD": opp["amountUSD"],
            "daysUntilDeadline": opp["daysUntilDeadline"]
        }
        processed.append(processed_opp)
    
    # Save opportunities.json
    final_opps_json = {
        "meta": {
            "market_val": "14.13",
            "cagr": "19.43",
            "updated": current_time,
            "totalCount": len(processed)
        },
        "opportunities": processed
    }
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(final_opps_json, f, indent=2, ensure_ascii=False)
    
    # Generate market forecast data
    forecast_data = {
        "current_year": 2025,
        "current_value": 3.27,
        "forecast_2030": 403.0,
        "cagr_pct": 4.3,
        "legislative_targets": [
            {"bill": "H.R. 187 (MAPWaters)", "impact": "Water data mandate"}
        ]
    }
    
    # Save forecast.json
    with open(FORECAST_FILE, 'w', encoding='utf-8') as f:
        json.dump(forecast_data, f, indent=2, ensure_ascii=False)
        
    print(f"✅ DATA SYNCED: {len(processed)} opportunities and FORECAST data saved.")


if __name__ == "__main__":
    # Ensure data directory exists before trying to save files
    os.makedirs('data', exist_ok=True)
    run_pipeline()
