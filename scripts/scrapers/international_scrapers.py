"""
International Space Agency Scrapers for Topographic/LiDAR Opportunities
"""

from base_scraper import BaseScraper

class ESAScraper(BaseScraper):
    """European Space Agency - Earth observation and LiDAR"""
    
    def __init__(self):
        super().__init__("ESA Copernicus", "International", "Europe")
    
    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="ESA Digital Twin Earth LiDAR Platform",
                agency="ESA",
                amount_usd=35000000,
                days_until=45,
                category="Platform",
                deadline_str=self.calculate_future_date(45),
                next_action="Consortium Lead",
                description="Space-based LiDAR for Digital Twin Earth topographic layer",
                agency_link="https://www.esa.int/"
            ),
            self.generate_opportunity(
                title="ESA Copernicus Expansion - Elevation Services",
                agency="ESA",
                amount_usd=28000000,
                days_until=75,
                category="DaaS",
                deadline_str=self.calculate_future_date(75),
                next_action="Technical Proposal",
                description="Commercial elevation data services for Copernicus program",
                agency_link="https://www.esa.int/Applications/Observing_the_Earth/Copernicus"
            ),
        ]
        
        self.opportunities.extend(opportunities)
        return opportunities

class JAXAScraper(BaseScraper):
    """Japan Aerospace Exploration Agency"""
    
    def __init__(self):
        super().__init__("JAXA Earth", "International", "Japan")
    
    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="JAXA ALOS-4 Topographic Mission Support",
                agency="JAXA",
                amount_usd=18000000,
                days_until=120,
                category="R&D",
                deadline_str=self.calculate_future_date(120),
                next_action="International Partnership",
                description="Spaceborne LiDAR integration for ALOS-4 global topographic mapping",
                agency_link="https://global.jaxa.jp/"
            ),
        ]
        
        self.opportunities.extend(opportunities)
        return opportunities

class CSAScraper(BaseScraper):
    """Canadian Space Agency"""
    
    def __init__(self):
        super().__init__("CSA EO", "International", "Canada")
    
    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="CSA Arctic Topographic Mapping Program",
                agency="CSA",
                amount_usd=22000000,
                days_until=85,
                category="DaaS",
                deadline_str=self.calculate_future_date(85),
                next_action="Arctic Capability Demo",
                description="Space-based LiDAR for Arctic and sub-Arctic terrain mapping",
                agency_link="https://www.asc-csa.gc.ca/"
            ),
        ]
        
        self.opportunities.extend(opportunities)
        return opportunities

class DLRScraper(BaseScraper):
    """German Aerospace Center"""
    
    def __init__(self):
        super().__init__("DLR Remote Sensing", "International", "Germany")
    
    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="DLR TanDEM-X Follow-On LiDAR Mission",
                agency="DLR",
                amount_usd=30000000,
                days_until=100,
                category="R&D",
                deadline_str=self.calculate_future_date(100),
                next_action="Mission Planning",
                description="Next-generation spaceborne LiDAR for high-resolution global DEM",
                agency_link="https://www.dlr.de/"
            ),
        ]
        
        self.opportunities.extend(opportunities)
        return opportunities

class ISROScraper(BaseScraper):
    """Indian Space Research Organisation"""
    
    def __init__(self):
        super().__init__("ISRO Cartography", "International", "India")
    
    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="ISRO National Topographic Mapping - LiDAR Phase",
                agency="ISRO",
                amount_usd=25000000,
                days_until=110,
                category="DaaS",
                deadline_str=self.calculate_future_date(110),
                next_action="India Partnership",
                description="Spaceborne LiDAR for national elevation mapping and disaster management",
                agency_link="https://www.isro.gov.in/"
            ),
        ]
        
        self.opportunities.extend(opportunities)
        return opportunities

class UKSAScraper(BaseScraper):
    """UK Space Agency"""
    
    def __init__(self):
        super().__init__("UKSA EO", "International", "UK")
    
    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="UKSA Climate & Environment LiDAR Services",
                agency="UKSA",
                amount_usd=20000000,
                days_until=90,
                category="DaaS",
                deadline_str=self.calculate_future_date(90),
                next_action="UK Partnership Brief",
                description="Commercial space-based topographic data for climate monitoring",
                agency_link="https://www.gov.uk/government/organisations/uk-space-agency"
            ),
        ]
        
        self.opportunities.extend(opportunities)
        return opportunities

class CNSAScraper(BaseScraper):
    """China National Space Administration"""
    
    def __init__(self):
        super().__init__("CNSA Mapping", "International", "China")
    
    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="CNSA Belt & Road Topographic Mapping",
                agency="CNSA",
                amount_usd=40000000,
                days_until=130,
                category="DaaS",
                deadline_str=self.calculate_future_date(130),
                next_action="International Coordination",
                description="Large-area spaceborne LiDAR for Belt and Road Initiative countries",
                agency_link="http://www.cnsa.gov.cn/english/"
            ),
        ]
        
        self.opportunities.extend(opportunities)
        return opportunities

class ASIScraper(BaseScraper):
    """Italian Space Agency"""
    
    def __init__(self):
        super().__init__("ASI Earth Obs", "International", "Italy")
    
    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="ASI COSMO-SkyMed Topographic Enhancement",
                agency="ASI",
                amount_usd=16000000,
                days_until=105,
                category="R&D",
                deadline_str=self.calculate_future_date(105),
                next_action="Technical Review",
                description="LiDAR augmentation for COSMO-SkyMed elevation products",
                agency_link="https://www.asi.it/"
            ),
        ]
        
        self.opportunities.extend(opportunities)
        return opportunities
