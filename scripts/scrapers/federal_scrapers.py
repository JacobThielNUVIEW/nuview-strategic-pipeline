"""
US Federal Agency Scrapers for Topographic/LiDAR Opportunities
"""

from base_scraper import BaseScraper

class USGSScraper(BaseScraper):
    """USGS 3DEP and topographic mapping opportunities"""
    
    def __init__(self):
        super().__init__("USGS 3DEP", "Federal", "USA")
    
    def scrape(self):
        # USGS 3DEP LiDAR opportunities
        opportunities = [
            self.generate_opportunity(
                title="USGS 3DEP LiDAR Acquisition 2026 - Phase 1",
                agency="USGS",
                amount_usd=217000000,
                days_until=28,
                category="DaaS",
                deadline_str=self.calculate_future_date(28),
                next_action="Submit Demo Brief",
                description="Large-area spaceborne LiDAR for National 3D Elevation Program. QL0/QL1 bare-earth DEM generation.",
                agency_link="https://www.usgs.gov/3d-elevation-program"
            ),
            self.generate_opportunity(
                title="USGS National Map Topographic Data Services",
                agency="USGS",
                amount_usd=45000000,
                days_until=60,
                category="DaaS",
                deadline_str=self.calculate_future_date(60),
                next_action="Capability Statement",
                description="Multi-year IDIQ for topographic data collection and processing services",
                agency_link="https://www.usgs.gov/programs/national-geospatial-program/national-map"
            ),
        ]
        
        self.opportunities.extend(opportunities)
        return opportunities

class NASAScraper(BaseScraper):
    """NASA space-based LiDAR and Earth observation opportunities"""
    
    def __init__(self):
        super().__init__("NASA Space LiDAR", "Federal", "USA")
    
    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="NASA ROSES ICESat-2 Science Team Augmentation",
                agency="NASA",
                amount_usd=12000000,
                days_until=45,
                category="R&D",
                deadline_str=self.calculate_future_date(45),
                next_action="Proposal Preparation",
                description="ICESat-2 ATLAS data processing and topographic applications research",
                agency_link="https://science.nasa.gov/earth-science/"
            ),
            self.generate_opportunity(
                title="NASA Commercial Spaceborne LiDAR Partnership",
                agency="NASA",
                amount_usd=25000000,
                days_until=90,
                category="R&D",
                deadline_str=self.calculate_future_date(90),
                next_action="Partner Coordination",
                description="Commercial space-based LiDAR for large-area topographic mapping",
                agency_link="https://science.nasa.gov/earth-science/"
            ),
        ]
        
        self.opportunities.extend(opportunities)
        return opportunities

class NOAAScraper(BaseScraper):
    """NOAA coastal and bathymetric LiDAR opportunities"""
    
    def __init__(self):
        super().__init__("NOAA Coastal", "Federal", "USA")
    
    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="NOAA Coastal Topobathy LiDAR Services",
                agency="NOAA",
                amount_usd=18000000,
                days_until=55,
                category="DaaS",
                deadline_str=self.calculate_future_date(55),
                next_action="Technical Demo",
                description="Topobathymetric LiDAR for coastal zone mapping and elevation data",
                agency_link="https://coast.noaa.gov/"
            ),
        ]
        
        self.opportunities.extend(opportunities)
        return opportunities

class USACEScraper(BaseScraper):
    """US Army Corps of Engineers topographic mapping"""
    
    def __init__(self):
        super().__init__("USACE Mapping", "Federal", "USA")
    
    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="USACE National DEM Production Contract",
                agency="USACE",
                amount_usd=32000000,
                days_until=70,
                category="DaaS",
                deadline_str=self.calculate_future_date(70),
                next_action="Past Performance Review",
                description="High-resolution DEM generation for flood mapping and infrastructure planning",
                agency_link="https://www.usace.army.mil/"
            ),
        ]
        
        self.opportunities.extend(opportunities)
        return opportunities

class FEMAScraper(BaseScraper):
    """FEMA flood mapping and elevation data"""
    
    def __init__(self):
        super().__init__("FEMA Flood", "Federal", "USA")
    
    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="FEMA Risk MAP Elevation Data Collection",
                agency="FEMA",
                amount_usd=28000000,
                days_until=65,
                category="DaaS",
                deadline_str=self.calculate_future_date(65),
                next_action="Capability Brief",
                description="LiDAR-derived elevation data for flood risk mapping and modeling",
                agency_link="https://www.fema.gov/flood-maps"
            ),
        ]
        
        self.opportunities.extend(opportunities)
        return opportunities

class NGAScraper(BaseScraper):
    """National Geospatial-Intelligence Agency"""
    
    def __init__(self):
        super().__init__("NGA Geoint", "Federal", "USA")
    
    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="NGA Commercial Space-Based 3D Mapping",
                agency="NGA",
                amount_usd=45000000,
                days_until=40,
                category="DaaS",
                deadline_str=self.calculate_future_date(40),
                next_action="Security Clearance Prep",
                description="Commercial spaceborne LiDAR and 3D topographic intelligence products",
                agency_link="https://www.nga.mil/"
            ),
        ]
        
        self.opportunities.extend(opportunities)
        return opportunities

class DIUScraper(BaseScraper):
    """Defense Innovation Unit"""
    
    def __init__(self):
        super().__init__("DIU Innovation", "Federal", "USA")
    
    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="DIU Spaceborne LiDAR BAA",
                agency="DIU",
                amount_usd=15000000,
                days_until=15,
                category="R&D",
                deadline_str=self.calculate_future_date(15),
                next_action="Submit Whitepaper",
                description="Next-generation space-based LiDAR for rapid large-area mapping",
                agency_link="https://www.diu.mil/"
            ),
        ]
        
        self.opportunities.extend(opportunities)
        return opportunities

class USDAForestScraper(BaseScraper):
    """USDA Forest Service LiDAR for forestry"""
    
    def __init__(self):
        super().__init__("USDA Forest", "Federal", "USA")
    
    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="USFS National Forest LiDAR Inventory",
                agency="USDA Forest Service",
                amount_usd=22000000,
                days_until=80,
                category="DaaS",
                deadline_str=self.calculate_future_date(80),
                next_action="Forest Demo",
                description="LiDAR for forest inventory, canopy height, and bare-earth terrain mapping",
                agency_link="https://www.fs.usda.gov/"
            ),
        ]
        
        self.opportunities.extend(opportunities)
        return opportunities

class BLMScraper(BaseScraper):
    """Bureau of Land Management"""
    
    def __init__(self):
        super().__init__("BLM Mapping", "Federal", "USA")
    
    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="BLM Public Lands Topographic Mapping",
                agency="BLM",
                amount_usd=16000000,
                days_until=95,
                category="DaaS",
                deadline_str=self.calculate_future_date(95),
                next_action="Site Assessment",
                description="Large-area topographic mapping for public land management and resource planning",
                agency_link="https://www.blm.gov/"
            ),
        ]
        
        self.opportunities.extend(opportunities)
        return opportunities
