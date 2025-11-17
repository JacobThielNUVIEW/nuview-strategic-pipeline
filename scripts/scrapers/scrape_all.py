import json
import datetime
import random
import os

OUTPUT_FILE = "data/opportunities.json"

def determine_pillar(title, agency):
    t = (title + " " + agency).lower()
    if any(x in t for x in ['dod', 'navy', 'army', 'diu', 'nga', 'defense']): return "Defense"
    if any(x in t for x in ['nasa', 'usgs', 'noaa', 'doe', 'federal', 'bill']): return "Federal"
    if any(x in t for x in ['state', 'dot', 'california', 'florida', 'texas']): return "State/Local"
    if any(x in t for x in ['esa', 'world bank', 'global', 'jaxa', 'wgic']): return "International"
    return "Commercial"

def run_pipeline():
    print("🕷️  GENERATING STRATEGIC DATA...")
    current_time = datetime.datetime.utcnow().isoformat() + "Z"
    
    raw_data = [
        {"title": "DIU — Project DRM-3 (Alternative PNT)", "agency": "DOD/DIU", "funding": "$3M–$8M", "deadline": "2025-11-16", "action": "Submit Demo Brief"},
        {"title": "USGS GPSC Subcontracting (High-Revisit)", "agency": "USGS", "funding": "$5M–$25M", "deadline": "2025-12-15", "action": "Prime Outreach"},
        {"title": "Mining — Stockpile Volumetrics POC", "agency": "Commercial", "funding": "$50k–$400k/yr", "deadline": "2025-12-31", "action": "Identify Site"},
        {"title": "California Statewide LiDAR Refresh", "agency": "CalTrans", "funding": "$20M–$50M", "deadline": "2027-01-01", "action": "Capture Strategy"},
        {"title": "NASA ROSES-2025 Omnibus", "agency": "NASA", "funding": "$5M+", "deadline": "2026-12-31", "action": "Proposal Dev"},
        {"title": "Florida Seafloor Mapping", "agency": "FL GIO", "funding": "$10M (BIL)", "deadline": "2025-12-31", "action": "Teaming Agreement"},
        {"title": "ESA Living Planet Fellowship", "agency": "ESA", "funding": "€60k", "deadline": "2025-09-28", "action": "Draft Proposal"},
        {"title": "H.R. 187: MAPWaters Act", "agency": "Federal", "funding": "Appropriations", "deadline": "FY2026", "action": "Monitor"}
    ]

    # Sort by Deadline
    raw_data.sort(key=lambda x: x['deadline'])

    processed = []
    for op in raw_data:
        pillar = determine_pillar(op['title'], op['agency'])
        processed.append({
            "id": str(random.randint(1000,9999)),
            "title": op['title'],
            "pillar": pillar,
            "deadline": op['deadline'],
            "forecast_value": op['funding'],
            "next_action": op['action'],
            "owner": "TBD",
            "link": "https://sam.gov"
        })

    output = { 
        "opportunities": processed, 
        "meta": { 
            "updated": current_time,
            "market_val": 14.13, 
            "cagr": 19.43 
        } 
    }

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(output, f, indent=2)
        
    print(f"✅ PIPELINE UPDATED: {len(raw_data)} Critical Actions saved.")

if __name__ == "__main__":
    run_pipeline()
