"""
NUVIEW Strategic Pipeline - Scraper Base Class
Base class for all specialized topographic opportunity scrapers
"""

import json
import random
from datetime import datetime, timezone, timedelta
from abc import ABC, abstractmethod
import sys
import os

# Add scripts directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

try:
    from global_keywords import calculate_keyword_score, is_topographic_relevant
    KEYWORDS_AVAILABLE = True
except ImportError:
    KEYWORDS_AVAILABLE = False

class BaseScraper(ABC):
    """Base class for all topographic opportunity scrapers"""
    
    def __init__(self, name, source_type, country="Global"):
        """
        Initialize scraper
        
        Args:
            name (str): Scraper name
            source_type (str): Type of source (Federal, International, Commercial, Research, etc.)
            country (str): Primary country/region
        """
        self.name = name
        self.source_type = source_type
        self.country = country
        self.opportunities = []
    
    @abstractmethod
    def scrape(self):
        """
        Scrape opportunities from source.
        Must be implemented by subclasses.
        
        Returns:
            list: List of opportunity dictionaries
        """
        pass
    
    def generate_opportunity(self, title, agency, amount_usd, days_until, category,
                           deadline_str, next_action, description="", link="https://sam.gov",
                           budget_source_link="#", agency_link="#"):
        """
        Generate a standardized opportunity record.
        
        Args:
            title (str): Opportunity title
            agency (str): Agency name
            amount_usd (int): Funding amount in USD
            days_until (int): Days until deadline
            category (str): Category (DaaS, R&D, Platform)
            deadline_str (str): Deadline date string
            next_action (str): Next action item
            description (str): Opportunity description
            link (str): Opportunity link
            budget_source_link (str): Budget source link
            agency_link (str): Agency website link
            
        Returns:
            dict: Standardized opportunity record
        """
        # Generate unique ID
        agency_clean = agency.lower().replace(' ', '-').replace('/', '-')
        opp_id = f"{agency_clean}-{random.randint(100, 999)}"
        
        # Determine urgency
        if days_until < 30:
            urgency = "urgent"
        elif days_until < 90:
            urgency = "near"
        else:
            urgency = "future"
        
        # Create opportunity record
        opportunity = {
            "id": opp_id,
            "title": title,
            "agency": agency,
            "pillar": self.source_type,
            "category": category,
            "description": description,
            "amountUSD": amount_usd,
            "daysUntilDeadline": days_until,
            "deadline": deadline_str,
            "next_action": next_action,
            "scrapedAt": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
            "forecast_value": f"${amount_usd:,}",
            "link": link,
            "budgetSourceLink": budget_source_link,
            "agencyLink": agency_link,
            "timeline": {
                "daysUntil": days_until,
                "urgency": urgency
            },
            "funding": {
                "amountUSD": amount_usd
            },
            "valueUSD": amount_usd,
            "urgency": urgency
        }
        
        return opportunity
    
    def calculate_future_date(self, days_from_now):
        """
        Calculate a future date string.
        
        Args:
            days_from_now (int): Number of days from now
            
        Returns:
            str: Date string in YYYY-MM-DD format
        """
        future_date = datetime.now(timezone.utc) + timedelta(days=days_from_now)
        return future_date.strftime("%Y-%m-%d")
    
    def save_results(self, output_dir="data/scrapers"):
        """
        Save scraper results to JSON file.
        
        Args:
            output_dir (str): Output directory path
        """
        os.makedirs(output_dir, exist_ok=True)
        
        filename = f"{self.name.lower().replace(' ', '_')}.json"
        filepath = os.path.join(output_dir, filename)
        
        data = {
            "scraper": self.name,
            "source_type": self.source_type,
            "country": self.country,
            "scraped_at": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
            "count": len(self.opportunities),
            "opportunities": self.opportunities
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        return filepath
    
    def get_results(self):
        """Get scraper results"""
        return self.opportunities
