"""
NUVIEW Strategic Pipeline - Programs Generator
Automatically generates programs.json from opportunities.json for dashboard consumption
This enables fully automated dashboard updates without manual code intervention
Also generates priority_matrix.csv with priority scoring
"""

import json
import os
import sys
from datetime import datetime, timezone

import pandas as pd

# Color codes for console output
COLOR_GREEN = '\033[92m'
COLOR_BLUE = '\033[94m'
COLOR_RED = '\033[91m'
COLOR_RESET = '\033[0m'

# Keyword sets for categorization
SPACE_KEYWORDS = {'space', 'satellite', 'orbital'}
LIDAR_KEYWORDS = {'lidar'}
PLATFORM_KEYWORDS = {'platform'}

# Priority scoring constants
URGENCY_SCORES = {
    'urgent': 30,
    'near': 20,
    'future': 10
}

VALUE_TIER_SCORES = {
    'high': 30,      # >= $100M
    'medium': 20,    # $10M - $100M
    'low': 10        # < $10M
}

CATEGORY_SCORES = {
    'DaaS': 15,
    'Platform': 10,
    'R&D': 5
}

SOURCE_VERIFIED_SCORE = 10

def log_info(msg):
    print(f"{COLOR_BLUE}ℹ️  {msg}{COLOR_RESET}")

def log_success(msg):
    print(f"{COLOR_GREEN}✅ {msg}{COLOR_RESET}")

def log_error(msg):
    print(f"{COLOR_RED}❌ {msg}{COLOR_RESET}")

def contains_keywords(text, keywords):
    """Check if text contains any of the specified keywords"""
    if not text:
        return False
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in keywords)

def categorize_opportunity(opp):
    """
    Categorize opportunity into Funding, LiDAR, Space Systems, or Platform
    Based on category field and keywords in title/description
    """
    category = opp.get('category', '')
    title = opp.get('title', '')
    description = opp.get('description', '')
    
    # Primary categorization by category field
    if category == 'DaaS':
        # Check if it's space-based or platform-related
        if contains_keywords(title, SPACE_KEYWORDS) or contains_keywords(description, SPACE_KEYWORDS) or \
           contains_keywords(title, PLATFORM_KEYWORDS) or contains_keywords(description, PLATFORM_KEYWORDS):
            return 'spaceSystems'
        # Check if it's LiDAR-specific
        if contains_keywords(title, LIDAR_KEYWORDS) or contains_keywords(description, LIDAR_KEYWORDS):
            return 'lidar'
        return 'funding'
    
    elif category == 'R&D':
        # R&D can fall into different buckets
        if contains_keywords(title, SPACE_KEYWORDS) or contains_keywords(description, SPACE_KEYWORDS):
            return 'spaceSystems'
        if contains_keywords(title, LIDAR_KEYWORDS) or contains_keywords(description, LIDAR_KEYWORDS):
            return 'lidar'
        return 'funding'
    
    elif category == 'Platform':
        return 'platform'
    
    # Fallback - try to categorize by keywords
    if contains_keywords(title, LIDAR_KEYWORDS) or contains_keywords(description, LIDAR_KEYWORDS):
        return 'lidar'
    if contains_keywords(title, SPACE_KEYWORDS) or contains_keywords(description, SPACE_KEYWORDS) or \
       contains_keywords(title, PLATFORM_KEYWORDS) or contains_keywords(description, PLATFORM_KEYWORDS):
        return 'spaceSystems'
    
    return 'funding'

def format_value(amount_usd):
    """Format USD amount as readable string"""
    if amount_usd >= 1_000_000_000:
        return f"${amount_usd / 1_000_000_000:.2f}B"
    elif amount_usd >= 1_000_000:
        return f"${amount_usd / 1_000_000:.1f}M"
    elif amount_usd >= 1_000:
        return f"${amount_usd / 1_000:.1f}K"
    else:
        return f"${amount_usd:,.0f}"

def get_value_usd(opp):
    """Extract USD value from opportunity, checking multiple possible field names"""
    for field_name in ['amountUSD', 'valueUSD', 'funding.amountUSD']:
        if field_name == 'funding.amountUSD':
            funding = opp.get('funding', {})
            if isinstance(funding, dict) and 'amountUSD' in funding:
                return funding['amountUSD']
        elif field_name in opp:
            return opp[field_name]
    return 0

def is_valid_link(url):
    """Check if a URL is valid and not a placeholder"""
    if not url:
        return False
    return url not in ['#', '', 'none', 'None']

def calculate_priority_score(opp):
    """
    Calculate priority score for an opportunity based on dashboard rules
    
    Scoring factors:
    - Urgency: urgent (30 pts), near (20 pts), future (10 pts)
    - Value tier: >$100M (30 pts), $10M-$100M (20 pts), <$10M (10 pts)
    - Category: DaaS (15 pts), Platform (10 pts), R&D (5 pts)
    - Source verified: (10 pts)
    
    Total possible: 85 points
    """
    score = 0
    
    # Urgency scoring (30 max)
    urgency = opp.get('timeline', {}).get('urgency', opp.get('urgency', 'future'))
    score += URGENCY_SCORES.get(urgency, 10)  # Default to 'future' if unknown
    
    # Value tier scoring (30 max)
    value_usd = get_value_usd(opp)
    if value_usd >= 100_000_000:
        score += VALUE_TIER_SCORES['high']
    elif value_usd >= 10_000_000:
        score += VALUE_TIER_SCORES['medium']
    else:
        score += VALUE_TIER_SCORES['low']
    
    # Category scoring (15 max)
    category = opp.get('category', '')
    score += CATEGORY_SCORES.get(category, 0)
    
    # Source verification scoring (10 max)
    if opp.get('source_verified', False):
        score += SOURCE_VERIFIED_SCORE
    else:
        # Check if has valid sources
        link = opp.get('link', '')
        budget_link = opp.get('budgetSourceLink', '')
        agency_link = opp.get('agencyLink', '')
        if is_valid_link(link) or is_valid_link(budget_link) or is_valid_link(agency_link):
            score += SOURCE_VERIFIED_SCORE
    
    return score

def convert_opportunity_to_program(opp):
    """Convert an opportunity object to a program object for dashboard"""
    value_usd = get_value_usd(opp)
    priority_score = calculate_priority_score(opp)
    
    program = {
        'id': opp.get('id', ''),
        'title': opp.get('title', ''),
        'agency': opp.get('agency', ''),
        'category': opp.get('category', 'Funding'),
        'pillar': opp.get('pillar', 'Federal'),
        'value': format_value(value_usd),
        'valueUSD': value_usd,
        'deadline': opp.get('deadline', ''),
        'daysUntil': opp.get('timeline', {}).get('daysUntil', opp.get('daysUntilDeadline', 0)),
        'urgency': opp.get('timeline', {}).get('urgency', opp.get('urgency', 'future')),
        'nextAction': opp.get('next_action', 'Review'),
        'description': opp.get('description', ''),
        'link': opp.get('link', ''),
        'agencyLink': opp.get('agencyLink', ''),
        'budgetSourceLink': opp.get('budgetSourceLink', ''),
        'priorityScore': priority_score
    }
    
    return program

def generate_programs_json():
    """
    Main function to generate programs.json from opportunities.json
    """
    log_info("Starting programs.json generation from opportunities.json")
    log_info("=" * 70)
    
    # Load opportunities.json
    opportunities_file = 'data/opportunities.json'
    if not os.path.exists(opportunities_file):
        log_error(f"Input file not found: {opportunities_file}")
        return False
    
    try:
        with open(opportunities_file, 'r', encoding='utf-8') as f:
            opps_data = json.load(f)
    except json.JSONDecodeError as e:
        log_error(f"Invalid JSON in {opportunities_file}: {e}")
        return False
    
    opportunities = opps_data.get('opportunities', [])
    log_info(f"Loaded {len(opportunities)} opportunities from {opportunities_file}")
    
    # Categorize opportunities into program types
    categorized = {
        'funding': [],
        'lidar': [],
        'spaceSystems': [],
        'platform': []
    }
    
    for opp in opportunities:
        bucket = categorize_opportunity(opp)
        program = convert_opportunity_to_program(opp)
        categorized[bucket].append(program)
    
    # Sort each category by value (descending)
    for category in categorized:
        categorized[category].sort(key=lambda x: x['valueUSD'], reverse=True)
    
    # Prepare output directory
    output_dir = 'data/processed'
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate priority matrix CSV
    log_info("")
    log_info("Generating priority matrix...")
    all_programs = []
    for category_programs in categorized.values():
        all_programs.extend(category_programs)
    
    # Sort all programs by priority score (descending)
    all_programs.sort(key=lambda x: x['priorityScore'], reverse=True)
    
    # Create priority matrix DataFrame
    priority_matrix = []
    for rank, program in enumerate(all_programs, 1):
        priority_matrix.append({
            'rank': rank,
            'title': program['title'],
            'agency': program['agency'],
            'pillar': program['pillar'],
            'category': program['category'],
            'value': program['value'],
            'valueUSD': program['valueUSD'],
            'priorityScore': program['priorityScore'],
            'urgency': program['urgency'],
            'daysUntil': program['daysUntil'],
            'deadline': program['deadline'],
            'nextAction': program['nextAction']
        })
    
    # Save priority matrix as CSV
    priority_matrix_path = os.path.join(output_dir, 'priority_matrix.csv')
    try:
        df = pd.DataFrame(priority_matrix)
        df.to_csv(priority_matrix_path, index=False)
        log_success(f"Successfully generated {priority_matrix_path}")
    except Exception as e:
        log_error(f"Failed to write {priority_matrix_path}: {e}")
    
    # Count programs
    total_programs = sum(len(programs) for programs in categorized.values())
    
    log_info("")
    log_info("Program Distribution:")
    log_info(f"  • Funding Programs: {len(categorized['funding'])}")
    log_info(f"  • LiDAR Programs: {len(categorized['lidar'])}")
    log_info(f"  • Space Systems Programs: {len(categorized['spaceSystems'])}")
    log_info(f"  • Platform Programs: {len(categorized['platform'])}")
    log_info(f"  • Total: {total_programs}")
    
    # Create programs.json structure
    programs_data = {
        'meta': {
            'updated': datetime.now(timezone.utc).isoformat(),
            'totalPrograms': total_programs,
            'categories': ['Funding', 'LiDAR', 'Space Systems', 'Platform'],
            'generated_from': 'opportunities.json',
            'generator_version': '1.0.0'
        },
        'programs': categorized
    }
    
    # Save programs.json
    output_file = os.path.join(output_dir, 'programs.json')
    
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(programs_data, f, indent=2, ensure_ascii=False)
        log_success(f"Successfully generated {output_file}")
        log_info("")
        log_info("=" * 70)
        log_success("programs.json generation complete!")
        log_info("Dashboard will automatically reflect these changes on next deployment")
        return True
    except Exception as e:
        log_error(f"Failed to write {output_file}: {e}")
        return False

if __name__ == "__main__":
    success = generate_programs_json()
    sys.exit(0 if success else 1)
