"""
NUVIEW Strategic Pipeline - Programs Generator
Automatically generates programs.json from opportunities.json for dashboard consumption
This enables fully automated dashboard updates without manual code intervention
"""

import json
import os
import sys
from datetime import datetime, timezone

# Color codes for console output
COLOR_GREEN = '\033[92m'
COLOR_BLUE = '\033[94m'
COLOR_RED = '\033[91m'
COLOR_RESET = '\033[0m'

# Keyword sets for categorization
SPACE_KEYWORDS = {'space', 'satellite', 'orbital'}
LIDAR_KEYWORDS = {'lidar'}
PLATFORM_KEYWORDS = {'platform'}

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

def convert_opportunity_to_program(opp):
    """Convert an opportunity object to a program object for dashboard"""
    value_usd = get_value_usd(opp)
    
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
        'budgetSourceLink': opp.get('budgetSourceLink', '')
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
    output_dir = 'data/processed'
    os.makedirs(output_dir, exist_ok=True)
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
