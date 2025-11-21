"""
NUVIEW Strategic Pipeline - Validate and Merge Script
Validates scraped data and merges it with existing opportunities
Handles deduplication, priority scoring, and data quality checks
"""

import json
import os
import sys
from datetime import datetime, timezone

# Add scripts directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

try:
    from global_keywords import calculate_keyword_score, is_topographic_relevant
    KEYWORDS_AVAILABLE = True
except ImportError:
    print("Warning: global_keywords module not found. Priority scoring will be limited.")
    KEYWORDS_AVAILABLE = False

# Color codes for console output
COLOR_GREEN = '\033[92m'
COLOR_ORANGE = '\033[93m'
COLOR_RED = '\033[91m'
COLOR_BLUE = '\033[94m'
COLOR_RESET = '\033[0m'

def log_info(msg):
    print(f"{COLOR_BLUE}ℹ️  {msg}{COLOR_RESET}")

def log_success(msg):
    print(f"{COLOR_GREEN}✅ {msg}{COLOR_RESET}")

def log_warning(msg):
    print(f"{COLOR_ORANGE}⚠️  {msg}{COLOR_RESET}")

def log_error(msg):
    print(f"{COLOR_RED}❌ {msg}{COLOR_RESET}")

def calculate_priority_score(opportunity):
    """
    Calculate priority score for an opportunity based on multiple factors.

    Score components:
    - Keyword relevance (0-100 points)
    - Funding amount (0-50 points)
    - Urgency (0-30 points)
    - Space-based LiDAR bonus (0-20 points)

    Returns:
        int: Priority score (0-200)
    """
    score = 0

    # 1. Keyword relevance score
    if KEYWORDS_AVAILABLE:
        title = opportunity.get('title', '')
        description = opportunity.get('description', '')
        combined_text = f"{title} {description}"

        keyword_data = calculate_keyword_score(combined_text)
        # Normalize to 0-100
        keyword_score = min(100, keyword_data['total_score'])
        score += keyword_score
    else:
        # Basic relevance check without keywords module
        title_lower = opportunity.get('title', '').lower()
        if 'lidar' in title_lower or 'topographic' in title_lower:
            score += 50

    # 2. Funding amount score (0-50 points)
    funding_amount = 0
    if 'funding' in opportunity and 'amountUSD' in opportunity['funding']:
        funding_amount = opportunity['funding']['amountUSD']
    elif 'amountUSD' in opportunity:
        funding_amount = opportunity['amountUSD']

    # Scale funding amount to 0-50 points
    # $1M = 10 points, $10M = 20 points, $100M+ = 50 points
    if funding_amount >= 100000000:  # $100M+
        score += 50
    elif funding_amount >= 50000000:  # $50M-$100M
        score += 40
    elif funding_amount >= 10000000:  # $10M-$50M
        score += 30
    elif funding_amount >= 1000000:  # $1M-$10M
        score += 20
    elif funding_amount >= 100000:  # $100K-$1M
        score += 10

    # 3. Urgency score (0-30 points)
    urgency = opportunity.get('urgency')
    if not urgency and 'timeline' in opportunity:
        urgency = opportunity['timeline'].get('urgency')

    if urgency == 'urgent':
        score += 30
    elif urgency == 'near':
        score += 20
    elif urgency == 'future':
        score += 10

    # 4. Space-based LiDAR bonus (0-20 points)
    title_lower = opportunity.get('title', '').lower()
    desc_lower = opportunity.get('description', '').lower()
    combined_lower = f"{title_lower} {desc_lower}"

    if any(term in combined_lower for term in ['space-based', 'spaceborne', 'satellite', 'icesat']):
        score += 20

    return min(200, score)  # Cap at 200

def format_priority_label(country_or_region, score):
    """
    Format priority label in the format: "top {Country/Region}: score {score}"

    Args:
        country_or_region (str): Country or region name
        score (int): Priority score

    Returns:
        str: Formatted priority label
    """
    return f"top {country_or_region}: score {score}"

def deduplicate_opportunities(opportunities):
    """
    Remove duplicate opportunities based on title and agency.

    Args:
        opportunities (list): List of opportunity dictionaries

    Returns:
        list: Deduplicated list of opportunities
    """
    seen = set()
    unique = []

    for opp in opportunities:
        # Create a key from title and agency
        title = opp.get('title', '').strip().lower()
        agency = opp.get('agency', '').strip().lower()
        key = f"{title}|{agency}"

        if key not in seen:
            seen.add(key)
            unique.append(opp)
        else:
            log_warning(f"Duplicate removed: {opp.get('title', 'Unknown')} ({opp.get('agency', 'Unknown')})")

    return unique

def validate_opportunity(opp, index):
    """
    Validate a single opportunity record.

    Args:
        opp (dict): Opportunity record
        index (int): Index of opportunity in list

    Returns:
        tuple: (is_valid, errors, warnings)
    """
    errors = []
    warnings = []

    # Required fields
    required_fields = ['id', 'title', 'agency']
    for field in required_fields:
        if field not in opp or not opp[field]:
            errors.append(f"Opportunity {index}: Missing required field '{field}'")

    # Check for topographic relevance
    if 'title' in opp:
        title = opp['title']
        if KEYWORDS_AVAILABLE:
            if not is_topographic_relevant(title, min_score=5):
                warnings.append(f"Opportunity {index} ({opp.get('id', 'unknown')}): May not be topographic-relevant")
        else:
            # Basic check without keywords module
            title_lower = title.lower()
            if not any(term in title_lower for term in ['lidar', 'topographic', 'elevation', 'dem', 'mapping']):
                warnings.append(f"Opportunity {index} ({opp.get('id', 'unknown')}): May not be topographic-relevant")

    # Check funding information
    if 'funding' in opp:
        if 'amountUSD' not in opp['funding']:
            warnings.append(f"Opportunity {index} ({opp.get('id', 'unknown')}): Missing funding.amountUSD")
    elif 'amountUSD' not in opp:
        warnings.append(f"Opportunity {index} ({opp.get('id', 'unknown')}): No funding information available")

    is_valid = len(errors) == 0
    return is_valid, errors, warnings

def merge_opportunities(existing_file, new_opportunities):
    """
    Merge new opportunities with existing data file.

    Args:
        existing_file (str): Path to existing opportunities.json
        new_opportunities (list): List of new opportunities to merge

    Returns:
        dict: Merged data structure
    """
    log_info(f"Merging {len(new_opportunities)} new opportunities...")

    # Load existing data if file exists
    existing_data = {
        "meta": {
            "market_val": "14.13",
            "cagr": "19.43",
            "updated": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
            "totalCount": 0
        },
        "opportunities": []
    }

    if os.path.exists(existing_file):
        try:
            with open(existing_file, 'r', encoding='utf-8') as f:
                existing_data = json.load(f)
            log_info(f"Loaded {len(existing_data.get('opportunities', []))} existing opportunities")
        except Exception as e:
            log_warning(f"Could not load existing data: {e}")

    # Combine opportunities
    all_opportunities = existing_data.get('opportunities', []) + new_opportunities

    # Deduplicate
    unique_opportunities = deduplicate_opportunities(all_opportunities)

    # Calculate priority scores and add priority labels
    for opp in unique_opportunities:
        priority_score = calculate_priority_score(opp)
        opp['priorityScore'] = priority_score

        # Add priority label with country/region info
        # Extract country from agency or pillar
        country = "Global"
        if opp.get('agency') == 'USGS' or opp.get('pillar') == 'Federal':
            country = "USA"
        elif opp.get('agency') == 'ESA':
            country = "Europe"
        elif opp.get('agency') == 'NASA':
            country = "USA"
        elif opp.get('agency') == 'JAXA':
            country = "Japan"

        opp['priorityLabel'] = format_priority_label(country, priority_score)

    # Sort by priority score (descending)
    unique_opportunities.sort(key=lambda x: x.get('priorityScore', 0), reverse=True)

    # Update metadata
    existing_data['opportunities'] = unique_opportunities
    existing_data['meta']['totalCount'] = len(unique_opportunities)
    existing_data['meta']['updated'] = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')

    log_success(f"Merged data contains {len(unique_opportunities)} unique opportunities")

    return existing_data

def main():
    """Main validation and merge logic"""
    log_info("=" * 70)
    log_info("NUVIEW TOPOGRAPHIC PIPELINE - VALIDATE AND MERGE")
    log_info("=" * 70)
    log_info("")

    # Check if we're validating existing data or merging new data
    opportunities_file = 'data/opportunities.json'

    if not os.path.exists(opportunities_file):
        log_error(f"Opportunities file not found: {opportunities_file}")
        log_info("Run scrape_all.py first to generate initial data.")
        return 1

    # Load opportunities
    try:
        with open(opportunities_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        log_error(f"Failed to load opportunities file: {e}")
        return 1

    opportunities = data.get('opportunities', [])
    log_info(f"Loaded {len(opportunities)} opportunities for validation")
    log_info("")

    # Validate each opportunity
    all_errors = []
    all_warnings = []
    valid_count = 0

    for idx, opp in enumerate(opportunities):
        is_valid, errors, warnings = validate_opportunity(opp, idx)
        if is_valid:
            valid_count += 1
        all_errors.extend(errors)
        all_warnings.extend(warnings)

    # Add priority scores if not present
    needs_scoring = False
    for opp in opportunities:
        if 'priorityScore' not in opp:
            needs_scoring = True
            break

    if needs_scoring:
        log_info("Calculating priority scores...")
        merged_data = merge_opportunities(opportunities_file, [])

        # Save updated data
        with open(opportunities_file, 'w', encoding='utf-8') as f:
            json.dump(merged_data, f, indent=2, ensure_ascii=False)

        log_success("Priority scores added and data saved")

    # Display validation results
    log_info("")
    log_info("=" * 70)
    log_info("VALIDATION RESULTS")
    log_info("=" * 70)

    if all_errors:
        log_error(f"Found {len(all_errors)} error(s):")
        for err in all_errors:
            log_error(f"  • {err}")
    else:
        log_success("No errors found")

    log_info("")

    if all_warnings:
        log_warning(f"Found {len(all_warnings)} warning(s):")
        for warn in all_warnings:
            log_warning(f"  • {warn}")
    else:
        log_success("No warnings")

    log_info("")
    log_success(f"Valid opportunities: {valid_count}/{len(opportunities)}")
    log_info("=" * 70)

    return 0 if len(all_errors) == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
