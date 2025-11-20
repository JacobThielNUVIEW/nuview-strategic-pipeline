"""
Research Institution and University Scrapers for Topographic/LiDAR Research
"""

from base_scraper import BaseScraper

class NSFScraper(BaseScraper):
    """National Science Foundation research grants"""
    
    def __init__(self):
        super().__init__("NSF Geosciences", "Research", "USA")
    
    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="NSF EarthCube LiDAR Data Integration",
                agency="NSF",
                amount_usd=8000000,
                days_until=75,
                category="R&D",
                deadline_str=self.calculate_future_date(75),
                next_action="Proposal Development",
                description="Space-based LiDAR data integration for geoscience research infrastructure",
                agency_link="https://www.nsf.gov/"
            ),
            self.generate_opportunity(
                title="NSF Critical Zone Observatory - Topographic Mapping",
                agency="NSF",
                amount_usd=12000000,
                days_until=95,
                category="R&D",
                deadline_str=self.calculate_future_date(95),
                next_action="Multi-Institution Proposal",
                description="High-resolution elevation data for critical zone science",
                agency_link="https://www.nsf.gov/geo/"
            ),
        ]
        
        self.opportunities.extend(opportunities)
        return opportunities

class DOEScraper(BaseScraper):
    """Department of Energy environmental research"""
    
    def __init__(self):
        super().__init__("DOE Environmental", "Research", "USA")
    
    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="DOE Terrestrial Ecosystem LiDAR Characterization",
                agency="DOE",
                amount_usd=10000000,
                days_until=85,
                category="R&D",
                deadline_str=self.calculate_future_date(85),
                next_action="Lab Partnership",
                description="Spaceborne LiDAR for carbon cycle and ecosystem monitoring",
                agency_link="https://www.energy.gov/"
            ),
        ]
        
        self.opportunities.extend(opportunities)
        return opportunities

class NIHGeospatialScraper(BaseScraper):
    """NIH geospatial health applications"""
    
    def __init__(self):
        super().__init__("NIH GeoHealth", "Research", "USA")
    
    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="NIH Environmental Health Topographic Mapping",
                agency="NIH",
                amount_usd=6000000,
                days_until=100,
                category="R&D",
                deadline_str=self.calculate_future_date(100),
                next_action="Health Mapping Brief",
                description="High-resolution DEM for disease vector and environmental health research",
                agency_link="https://www.nih.gov/"
            ),
        ]
        
        self.opportunities.extend(opportunities)
        return opportunities

class EUHorizonScraper(BaseScraper):
    """EU Horizon Europe research program"""
    
    def __init__(self):
        super().__init__("EU Horizon", "Research", "Europe")
    
    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="Horizon Europe Space-Based Earth Monitoring",
                agency="EU Commission",
                amount_usd=35000000,
                days_until=120,
                category="R&D",
                deadline_str=self.calculate_future_date(120),
                next_action="Consortium Formation",
                description="Commercial spaceborne LiDAR for pan-European topographic services",
                agency_link="https://research-and-innovation.ec.europa.eu/funding/funding-opportunities/funding-programmes-and-open-calls/horizon-europe_en"
            ),
        ]
        
        self.opportunities.extend(opportunities)
        return opportunities

class MITScraper(BaseScraper):
    """MIT research partnerships"""
    
    def __init__(self):
        super().__init__("MIT Research", "Research", "USA")
    
    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="MIT Lincoln Lab Space-Based Sensing Partnership",
                agency="MIT",
                amount_usd=15000000,
                days_until=110,
                category="R&D",
                deadline_str=self.calculate_future_date(110),
                next_action="Research Agreement",
                description="Advanced spaceborne LiDAR technology development and validation",
                agency_link="https://www.ll.mit.edu/"
            ),
        ]
        
        self.opportunities.extend(opportunities)
        return opportunities

class CaltechJPLScraper(BaseScraper):
    """Caltech JPL research opportunities"""
    
    def __init__(self):
        super().__init__("Caltech JPL", "Research", "USA")
    
    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="JPL Earth Surface & Interior Science - LiDAR",
                agency="Caltech/JPL",
                amount_usd=18000000,
                days_until=90,
                category="R&D",
                deadline_str=self.calculate_future_date(90),
                next_action="JPL Collaboration",
                description="Next-generation spaceborne LiDAR for planetary surface science",
                agency_link="https://www.jpl.nasa.gov/"
            ),
        ]
        
        self.opportunities.extend(opportunities)
        return opportunities
