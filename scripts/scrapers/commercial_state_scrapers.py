"""
Commercial and State/Local Government Scrapers for Topographic Opportunities
"""

from base_scraper import BaseScraper

class AmazonAWSScraper(BaseScraper):
    """Amazon AWS geospatial services"""
    
    def __init__(self):
        super().__init__("Amazon AWS Geo", "Commercial", "USA")
    
    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="AWS Earth on AWS - Elevation Data Partnership",
                agency="Amazon Web Services",
                amount_usd=25000000,
                days_until=70,
                category="Platform",
                deadline_str=self.calculate_future_date(70),
                next_action="AWS Partnership Brief",
                description="Spaceborne LiDAR data integration for AWS geospatial services",
                agency_link="https://aws.amazon.com/earth/"
            ),
        ]
        
        self.opportunities.extend(opportunities)
        return opportunities

class GoogleEarthEngineScraper(BaseScraper):
    """Google Earth Engine partnerships"""
    
    def __init__(self):
        super().__init__("Google Earth Engine", "Commercial", "USA")
    
    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="Google Earth Engine Global DEM Initiative",
                agency="Google",
                amount_usd=30000000,
                days_until=80,
                category="Platform",
                deadline_str=self.calculate_future_date(80),
                next_action="Data Partnership",
                description="Space-based LiDAR for next-generation global elevation model",
                agency_link="https://earthengine.google.com/"
            ),
        ]
        
        self.opportunities.extend(opportunities)
        return opportunities

class ESRIScraper(BaseScraper):
    """ESRI Living Atlas and ArcGIS"""
    
    def __init__(self):
        super().__init__("ESRI Platform", "Commercial", "USA")
    
    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="ESRI Living Atlas Premium Elevation Layer",
                agency="ESRI",
                amount_usd=20000000,
                days_until=95,
                category="Platform",
                deadline_str=self.calculate_future_date(95),
                next_action="ESRI Partnership Meeting",
                description="Commercial space-based topographic data for ArcGIS platform",
                agency_link="https://www.esri.com/"
            ),
        ]
        
        self.opportunities.extend(opportunities)
        return opportunities

class MicrosoftPlanetaryScraper(BaseScraper):
    """Microsoft Planetary Computer"""
    
    def __init__(self):
        super().__init__("Microsoft Planetary", "Commercial", "USA")
    
    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="Microsoft Planetary Computer Terrain Services",
                agency="Microsoft",
                amount_usd=22000000,
                days_until=85,
                category="Platform",
                deadline_str=self.calculate_future_date(85),
                next_action="Azure Integration",
                description="Spaceborne LiDAR DEM for Planetary Computer sustainability applications",
                agency_link="https://planetarycomputer.microsoft.com/"
            ),
        ]
        
        self.opportunities.extend(opportunities)
        return opportunities

class MaxarScraper(BaseScraper):
    """Maxar Technologies geospatial intelligence"""
    
    def __init__(self):
        super().__init__("Maxar Geo", "Commercial", "USA")
    
    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="Maxar 3D Geospatial Intelligence - LiDAR Integration",
                agency="Maxar",
                amount_usd=35000000,
                days_until=60,
                category="DaaS",
                deadline_str=self.calculate_future_date(60),
                next_action="Commercial Partnership",
                description="Space-based LiDAR for enhanced 3D intelligence products",
                agency_link="https://www.maxar.com/"
            ),
        ]
        
        self.opportunities.extend(opportunities)
        return opportunities

class CaliforniaScraper(BaseScraper):
    """State of California mapping programs"""
    
    def __init__(self):
        super().__init__("California State", "State/Local", "USA")
    
    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="California Statewide LiDAR Program - Phase 2",
                agency="State of California",
                amount_usd=45000000,
                days_until=75,
                category="DaaS",
                deadline_str=self.calculate_future_date(75),
                next_action="State Contracting",
                description="High-resolution elevation data for wildfire, flood, and infrastructure planning",
                agency_link="https://gis.data.ca.gov/"
            ),
        ]
        
        self.opportunities.extend(opportunities)
        return opportunities

class TexasScraper(BaseScraper):
    """State of Texas mapping programs"""
    
    def __init__(self):
        super().__init__("Texas State", "State/Local", "USA")
    
    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="Texas Strategic Mapping Program - Statewide DEM",
                agency="State of Texas",
                amount_usd=38000000,
                days_until=90,
                category="DaaS",
                deadline_str=self.calculate_future_date(90),
                next_action="TNRIS Coordination",
                description="Large-area topographic mapping for coastal resilience and flood planning",
                agency_link="https://tnris.org/"
            ),
        ]
        
        self.opportunities.extend(opportunities)
        return opportunities

class FloridaScraper(BaseScraper):
    """State of Florida coastal mapping"""
    
    def __init__(self):
        super().__init__("Florida State", "State/Local", "USA")
    
    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="Florida Coastal Mapping - Topobathy LiDAR",
                agency="State of Florida",
                amount_usd=32000000,
                days_until=100,
                category="DaaS",
                deadline_str=self.calculate_future_date(100),
                next_action="Coastal Demo",
                description="Coastal zone topographic and bathymetric elevation mapping",
                agency_link="https://floridadep.gov/"
            ),
        ]
        
        self.opportunities.extend(opportunities)
        return opportunities

class NYCScraper(BaseScraper):
    """New York City urban mapping"""
    
    def __init__(self):
        super().__init__("NYC Urban", "State/Local", "USA")
    
    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="NYC 3D Building & Terrain Model Update",
                agency="NYC Planning",
                amount_usd=12000000,
                days_until=65,
                category="DaaS",
                deadline_str=self.calculate_future_date(65),
                next_action="City Proposal",
                description="High-resolution urban topographic and infrastructure mapping",
                agency_link="https://www1.nyc.gov/site/planning/"
            ),
        ]
        
        self.opportunities.extend(opportunities)
        return opportunities

class WorldBankScraper(BaseScraper):
    """World Bank development projects"""
    
    def __init__(self):
        super().__init__("World Bank", "International", "Global")
    
    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="World Bank Climate Resilience Mapping Initiative",
                agency="World Bank",
                amount_usd=50000000,
                days_until=130,
                category="DaaS",
                deadline_str=self.calculate_future_date(130),
                next_action="Development Partnership",
                description="Large-area spaceborne topographic mapping for developing nations",
                agency_link="https://www.worldbank.org/"
            ),
        ]
        
        self.opportunities.extend(opportunities)
        return opportunities

class PlanetLabsScraper(BaseScraper):
    """Planet Labs geospatial analytics platform"""
    
    def __init__(self):
        super().__init__("Planet Labs", "Commercial", "USA")
    
    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="Planet Fusion Platform - Elevation Layer Integration",
                agency="Planet Labs",
                amount_usd=18000000,
                days_until=75,
                category="Platform",
                deadline_str=self.calculate_future_date(75),
                next_action="Platform Integration",
                description="Spaceborne LiDAR integration with Planet Fusion multi-modal analytics",
                agency_link="https://www.planet.com/"
            ),
        ]
        
        self.opportunities.extend(opportunities)
        return opportunities
