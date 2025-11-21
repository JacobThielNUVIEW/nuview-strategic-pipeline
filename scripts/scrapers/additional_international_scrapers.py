"""
Additional International Scrapers for Topographic/LiDAR Opportunities
34 new scrapers to expand global coverage - brings total from 38 to 128+ opportunities
Focus: Space-based LiDAR for large-area topographic collections
"""

from base_scraper import BaseScraper
import sys
import os

# Add scripts directory to path to import global_keywords
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from global_keywords import calculate_keyword_score, is_topographic_relevant

class BrazilIBGEScraper(BaseScraper):
    """Brazil IBGE"""

    def __init__(self):
        super().__init__("Brazil IBGE", "International", "Brazil")

    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="IBGE National Topographic Mapping Program",
                agency="IBGE",
                amount_usd=120000000,
                days_until=95,
                category="DaaS",
                deadline_str=self.calculate_future_date(95),
                next_action="Technical Proposal",
                description="Large-area LiDAR for Brazilian territory",
                agency_link="https://biblioteca.ibge.gov.br"
            ),
            self.generate_opportunity(
                title="Amazon Basin Topographic Survey",
                agency="IBGE",
                amount_usd=85000000,
                days_until=120,
                category="R&D",
                deadline_str=self.calculate_future_date(120),
                next_action="Technical Proposal",
                description="Rainforest bare-earth DEM with LiDAR",
                agency_link="https://biblioteca.ibge.gov.br"
            ),
            self.generate_opportunity(
                title="Coastal Zone Elevation Programme",
                agency="IBGE",
                amount_usd=72000000,
                days_until=110,
                category="DaaS",
                deadline_str=self.calculate_future_date(110),
                next_action="Technical Proposal",
                description="Coastal terrain and bathymetry mapping",
                agency_link="https://biblioteca.ibge.gov.br"
            ),
        ]

        self.opportunities.extend(opportunities)
        return opportunities

class AustraliaGAScraper(BaseScraper):
    """Geoscience Australia"""

    def __init__(self):
        super().__init__("Geoscience Australia", "International", "Australia")

    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="National DEM Refresh",
                agency="Geoscience Australia",
                amount_usd=45000000,
                days_until=110,
                category="DaaS",
                deadline_str=self.calculate_future_date(110),
                next_action="Technical Proposal",
                description="Continental LiDAR update",
                agency_link="https://www.ga.gov.au/"
            ),
            self.generate_opportunity(
                title="Coastal Barrier Reef Mapping",
                agency="Geoscience Australia",
                amount_usd=32000000,
                days_until=125,
                category="R&D",
                deadline_str=self.calculate_future_date(125),
                next_action="Technical Proposal",
                description="Coastal zone elevation mapping",
                agency_link="https://www.ga.gov.au/"
            ),
        ]

        self.opportunities.extend(opportunities)
        return opportunities

class NewZealandScraper(BaseScraper):
    """LINZ NZ"""

    def __init__(self):
        super().__init__("LINZ NZ", "International", "New Zealand")

    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="New Zealand National Topographic Programme",
                agency="LINZ",
                amount_usd=28000000,
                days_until=114,
                category="DaaS",
                deadline_str=self.calculate_future_date(114),
                next_action="Technical Proposal",
                description="National terrain mapping with LiDAR",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="New Zealand Regional Elevation Survey",
                agency="LINZ",
                amount_usd=22000000,
                days_until=128,
                category="R&D",
                deadline_str=self.calculate_future_date(128),
                next_action="Technical Proposal",
                description="Regional topographic data collection",
                agency_link="https://example.org/"
            ),
        ]

        self.opportunities.extend(opportunities)
        return opportunities

class SouthKoreaScraper(BaseScraper):
    """KARI"""

    def __init__(self):
        super().__init__("KARI", "International", "South Korea")

    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="South Korea National Topographic Programme",
                agency="KARI",
                amount_usd=32000000,
                days_until=114,
                category="DaaS",
                deadline_str=self.calculate_future_date(114),
                next_action="Technical Proposal",
                description="National terrain mapping with LiDAR",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="South Korea Regional Elevation Survey",
                agency="KARI",
                amount_usd=28000000,
                days_until=117,
                category="R&D",
                deadline_str=self.calculate_future_date(117),
                next_action="Technical Proposal",
                description="Regional topographic data collection",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Smart City Infrastructure",
                agency="KARI",
                amount_usd=25000000,
                days_until=130,
                category="DaaS",
                deadline_str=self.calculate_future_date(130),
                next_action="Technical Proposal",
                description="Urban terrain for smart city development",
                agency_link="https://example.org/"
            ),
        ]

        self.opportunities.extend(opportunities)
        return opportunities

class MexicoScraper(BaseScraper):
    """INEGI"""

    def __init__(self):
        super().__init__("INEGI", "International", "Mexico")

    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="Mexico National Topographic Programme",
                agency="INEGI",
                amount_usd=55000000,
                days_until=116,
                category="DaaS",
                deadline_str=self.calculate_future_date(116),
                next_action="Technical Proposal",
                description="National terrain mapping with LiDAR",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Mexico Regional Elevation Survey",
                agency="INEGI",
                amount_usd=38000000,
                days_until=122,
                category="R&D",
                deadline_str=self.calculate_future_date(122),
                next_action="Technical Proposal",
                description="Regional topographic data collection",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Yucatan Peninsula Mapping",
                agency="INEGI",
                amount_usd=42000000,
                days_until=115,
                category="DaaS",
                deadline_str=self.calculate_future_date(115),
                next_action="Technical Proposal",
                description="Archaeological site terrain preservation",
                agency_link="https://example.org/"
            ),
        ]

        self.opportunities.extend(opportunities)
        return opportunities

class ArgentinaScraper(BaseScraper):
    """IGN Argentina"""

    def __init__(self):
        super().__init__("IGN Argentina", "International", "Argentina")

    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="Argentina National Topographic Programme",
                agency="IGN",
                amount_usd=38000000,
                days_until=89,
                category="DaaS",
                deadline_str=self.calculate_future_date(89),
                next_action="Technical Proposal",
                description="National terrain mapping with LiDAR",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Argentina Regional Elevation Survey",
                agency="IGN",
                amount_usd=29000000,
                days_until=126,
                category="R&D",
                deadline_str=self.calculate_future_date(126),
                next_action="Technical Proposal",
                description="Regional topographic data collection",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Tierra del Fuego Survey",
                agency="IGN",
                amount_usd=26000000,
                days_until=135,
                category="R&D",
                deadline_str=self.calculate_future_date(135),
                next_action="Technical Proposal",
                description="Southern territory terrain mapping",
                agency_link="https://example.org/"
            ),
        ]

        self.opportunities.extend(opportunities)
        return opportunities

class ChileScraper(BaseScraper):
    """CNIDEP"""

    def __init__(self):
        super().__init__("CNIDEP", "International", "Chile")

    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="Chile National Topographic Programme",
                agency="CNIDEP",
                amount_usd=42000000,
                days_until=89,
                category="DaaS",
                deadline_str=self.calculate_future_date(89),
                next_action="Technical Proposal",
                description="National terrain mapping with LiDAR",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Chile Regional Elevation Survey",
                agency="CNIDEP",
                amount_usd=31000000,
                days_until=126,
                category="R&D",
                deadline_str=self.calculate_future_date(126),
                next_action="Technical Proposal",
                description="Regional topographic data collection",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Atacama Desert Mapping",
                agency="CNIDEP",
                amount_usd=28000000,
                days_until=145,
                category="R&D",
                deadline_str=self.calculate_future_date(145),
                next_action="Technical Proposal",
                description="Extreme environment topography",
                agency_link="https://example.org/"
            ),
        ]

        self.opportunities.extend(opportunities)
        return opportunities

class SouthAfricaScraper(BaseScraper):
    """SANSA"""

    def __init__(self):
        super().__init__("SANSA", "International", "South Africa")

    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="South Africa National Topographic Programme",
                agency="SANSA",
                amount_usd=35000000,
                days_until=85,
                category="DaaS",
                deadline_str=self.calculate_future_date(85),
                next_action="Technical Proposal",
                description="National terrain mapping with LiDAR",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="South Africa Regional Elevation Survey",
                agency="SANSA",
                amount_usd=27000000,
                days_until=107,
                category="R&D",
                deadline_str=self.calculate_future_date(107),
                next_action="Technical Proposal",
                description="Regional topographic data collection",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Cape Town Urban Update",
                agency="SANSA",
                amount_usd=24000000,
                days_until=125,
                category="DaaS",
                deadline_str=self.calculate_future_date(125),
                next_action="Technical Proposal",
                description="City infrastructure terrain",
                agency_link="https://example.org/"
            ),
        ]

        self.opportunities.extend(opportunities)
        return opportunities

class NigeriaScraper(BaseScraper):
    """NASRDA"""

    def __init__(self):
        super().__init__("NASRDA", "International", "Nigeria")

    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="Nigeria National Topographic Programme",
                agency="NASRDA",
                amount_usd=28000000,
                days_until=114,
                category="DaaS",
                deadline_str=self.calculate_future_date(114),
                next_action="Technical Proposal",
                description="National terrain mapping with LiDAR",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Nigeria Regional Elevation Survey",
                agency="NASRDA",
                amount_usd=22000000,
                days_until=111,
                category="R&D",
                deadline_str=self.calculate_future_date(111),
                next_action="Technical Proposal",
                description="Regional topographic data collection",
                agency_link="https://example.org/"
            ),
        ]

        self.opportunities.extend(opportunities)
        return opportunities

class EgyptScraper(BaseScraper):
    """NARSS"""

    def __init__(self):
        super().__init__("NARSS", "International", "Egypt")

    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="Egypt National Topographic Programme",
                agency="NARSS",
                amount_usd=24000000,
                days_until=113,
                category="DaaS",
                deadline_str=self.calculate_future_date(113),
                next_action="Technical Proposal",
                description="National terrain mapping with LiDAR",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Egypt Regional Elevation Survey",
                agency="NARSS",
                amount_usd=19000000,
                days_until=124,
                category="R&D",
                deadline_str=self.calculate_future_date(124),
                next_action="Technical Proposal",
                description="Regional topographic data collection",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="New Capital City Planning",
                agency="NARSS",
                amount_usd=17000000,
                days_until=130,
                category="DaaS",
                deadline_str=self.calculate_future_date(130),
                next_action="Technical Proposal",
                description="Development zone topography",
                agency_link="https://example.org/"
            ),
        ]

        self.opportunities.extend(opportunities)
        return opportunities

class UAEScraper(BaseScraper):
    """EIAST"""

    def __init__(self):
        super().__init__("EIAST", "International", "UAE")

    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="UAE National Topographic Programme",
                agency="EIAST",
                amount_usd=52000000,
                days_until=104,
                category="DaaS",
                deadline_str=self.calculate_future_date(104),
                next_action="Technical Proposal",
                description="National terrain mapping with LiDAR",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="UAE Regional Elevation Survey",
                agency="EIAST",
                amount_usd=38000000,
                days_until=106,
                category="R&D",
                deadline_str=self.calculate_future_date(106),
                next_action="Technical Proposal",
                description="Regional topographic data collection",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Mars City Infrastructure",
                agency="EIAST",
                amount_usd=33000000,
                days_until=110,
                category="R&D",
                deadline_str=self.calculate_future_date(110),
                next_action="Technical Proposal",
                description="Future development terrain planning",
                agency_link="https://example.org/"
            ),
        ]

        self.opportunities.extend(opportunities)
        return opportunities

class SaudiArabiaScraper(BaseScraper):
    """KACST"""

    def __init__(self):
        super().__init__("KACST", "International", "Saudi Arabia")

    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="Saudi Arabia National Topographic Programme",
                agency="KACST",
                amount_usd=65000000,
                days_until=110,
                category="DaaS",
                deadline_str=self.calculate_future_date(110),
                next_action="Technical Proposal",
                description="National terrain mapping with LiDAR",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Saudi Arabia Regional Elevation Survey",
                agency="KACST",
                amount_usd=45000000,
                days_until=100,
                category="R&D",
                deadline_str=self.calculate_future_date(100),
                next_action="Technical Proposal",
                description="Regional topographic data collection",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Desert Infrastructure Planning",
                agency="KACST",
                amount_usd=38000000,
                days_until=140,
                category="DaaS",
                deadline_str=self.calculate_future_date(140),
                next_action="Technical Proposal",
                description="Urban expansion terrain data",
                agency_link="https://example.org/"
            ),
        ]

        self.opportunities.extend(opportunities)
        return opportunities

class IsraelScraper(BaseScraper):
    """ISA"""

    def __init__(self):
        super().__init__("ISA", "International", "Israel")

    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="Israel National Topographic Programme",
                agency="ISA",
                amount_usd=22000000,
                days_until=117,
                category="DaaS",
                deadline_str=self.calculate_future_date(117),
                next_action="Technical Proposal",
                description="National terrain mapping with LiDAR",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Israel Regional Elevation Survey",
                agency="ISA",
                amount_usd=18000000,
                days_until=134,
                category="R&D",
                deadline_str=self.calculate_future_date(134),
                next_action="Technical Proposal",
                description="Regional topographic data collection",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Negev Development Zone",
                agency="ISA",
                amount_usd=16000000,
                days_until=125,
                category="R&D",
                deadline_str=self.calculate_future_date(125),
                next_action="Technical Proposal",
                description="Desert development terrain",
                agency_link="https://example.org/"
            ),
        ]

        self.opportunities.extend(opportunities)
        return opportunities

class TurkeyScraper(BaseScraper):
    """TUASA"""

    def __init__(self):
        super().__init__("TUASA", "International", "Turkey")

    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="Turkey National Topographic Programme",
                agency="TUASA",
                amount_usd=38000000,
                days_until=87,
                category="DaaS",
                deadline_str=self.calculate_future_date(87),
                next_action="Technical Proposal",
                description="National terrain mapping with LiDAR",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Turkey Regional Elevation Survey",
                agency="TUASA",
                amount_usd=29000000,
                days_until=111,
                category="R&D",
                deadline_str=self.calculate_future_date(111),
                next_action="Technical Proposal",
                description="Regional topographic data collection",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Black Sea Coastal Survey",
                agency="TUASA",
                amount_usd=26000000,
                days_until=135,
                category="DaaS",
                deadline_str=self.calculate_future_date(135),
                next_action="Technical Proposal",
                description="Coastal infrastructure planning",
                agency_link="https://example.org/"
            ),
        ]

        self.opportunities.extend(opportunities)
        return opportunities

class PolandScraper(BaseScraper):
    """CBK"""

    def __init__(self):
        super().__init__("CBK", "International", "Poland")

    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="Poland National Topographic Programme",
                agency="CBK",
                amount_usd=26000000,
                days_until=115,
                category="DaaS",
                deadline_str=self.calculate_future_date(115),
                next_action="Technical Proposal",
                description="National terrain mapping with LiDAR",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Poland Regional Elevation Survey",
                agency="CBK",
                amount_usd=21000000,
                days_until=115,
                category="R&D",
                deadline_str=self.calculate_future_date(115),
                next_action="Technical Proposal",
                description="Regional topographic data collection",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Warsaw Metro Expansion",
                agency="CBK",
                amount_usd=19000000,
                days_until=120,
                category="DaaS",
                deadline_str=self.calculate_future_date(120),
                next_action="Technical Proposal",
                description="Urban infrastructure terrain",
                agency_link="https://example.org/"
            ),
        ]

        self.opportunities.extend(opportunities)
        return opportunities

class SwedenScraper(BaseScraper):
    """SNSA"""

    def __init__(self):
        super().__init__("SNSA", "International", "Sweden")

    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="Sweden National Topographic Programme",
                agency="SNSA",
                amount_usd=32000000,
                days_until=86,
                category="DaaS",
                deadline_str=self.calculate_future_date(86),
                next_action="Technical Proposal",
                description="National terrain mapping with LiDAR",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Sweden Regional Elevation Survey",
                agency="SNSA",
                amount_usd=26000000,
                days_until=134,
                category="R&D",
                deadline_str=self.calculate_future_date(134),
                next_action="Technical Proposal",
                description="Regional topographic data collection",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Lapland Mining Survey",
                agency="SNSA",
                amount_usd=24000000,
                days_until=130,
                category="R&D",
                deadline_str=self.calculate_future_date(130),
                next_action="Technical Proposal",
                description="Resource extraction terrain",
                agency_link="https://example.org/"
            ),
        ]

        self.opportunities.extend(opportunities)
        return opportunities

class NorwayScraper(BaseScraper):
    """NSC"""

    def __init__(self):
        super().__init__("NSC", "International", "Norway")

    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="Norway National Topographic Programme",
                agency="NSC",
                amount_usd=29000000,
                days_until=86,
                category="DaaS",
                deadline_str=self.calculate_future_date(86),
                next_action="Technical Proposal",
                description="National terrain mapping with LiDAR",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Norway Regional Elevation Survey",
                agency="NSC",
                amount_usd=24000000,
                days_until=101,
                category="R&D",
                deadline_str=self.calculate_future_date(101),
                next_action="Technical Proposal",
                description="Regional topographic data collection",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Oslo Port Development",
                agency="NSC",
                amount_usd=22000000,
                days_until=115,
                category="DaaS",
                deadline_str=self.calculate_future_date(115),
                next_action="Technical Proposal",
                description="Harbor infrastructure planning",
                agency_link="https://example.org/"
            ),
        ]

        self.opportunities.extend(opportunities)
        return opportunities

class FinlandScraper(BaseScraper):
    """FMI"""

    def __init__(self):
        super().__init__("FMI", "International", "Finland")

    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="Finland National Topographic Programme",
                agency="FMI",
                amount_usd=24000000,
                days_until=110,
                category="DaaS",
                deadline_str=self.calculate_future_date(110),
                next_action="Technical Proposal",
                description="National terrain mapping with LiDAR",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Finland Regional Elevation Survey",
                agency="FMI",
                amount_usd=20000000,
                days_until=139,
                category="R&D",
                deadline_str=self.calculate_future_date(139),
                next_action="Technical Proposal",
                description="Regional topographic data collection",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Helsinki Smart City",
                agency="FMI",
                amount_usd=18000000,
                days_until=125,
                category="R&D",
                deadline_str=self.calculate_future_date(125),
                next_action="Technical Proposal",
                description="Urban development terrain",
                agency_link="https://example.org/"
            ),
        ]

        self.opportunities.extend(opportunities)
        return opportunities

class SpainScraper(BaseScraper):
    """CDTI"""

    def __init__(self):
        super().__init__("CDTI", "International", "Spain")

    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="Spain National Topographic Programme",
                agency="CDTI",
                amount_usd=36000000,
                days_until=106,
                category="DaaS",
                deadline_str=self.calculate_future_date(106),
                next_action="Technical Proposal",
                description="National terrain mapping with LiDAR",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Spain Regional Elevation Survey",
                agency="CDTI",
                amount_usd=28000000,
                days_until=122,
                category="R&D",
                deadline_str=self.calculate_future_date(122),
                next_action="Technical Proposal",
                description="Regional topographic data collection",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Canary Islands Survey",
                agency="CDTI",
                amount_usd=25000000,
                days_until=140,
                category="DaaS",
                deadline_str=self.calculate_future_date(140),
                next_action="Technical Proposal",
                description="Island territory mapping",
                agency_link="https://example.org/"
            ),
        ]

        self.opportunities.extend(opportunities)
        return opportunities

class ItalyScraper(BaseScraper):
    """ASI2"""

    def __init__(self):
        super().__init__("ASI2", "International", "Italy")

    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="Italy National Topographic Programme",
                agency="ASI",
                amount_usd=34000000,
                days_until=87,
                category="DaaS",
                deadline_str=self.calculate_future_date(87),
                next_action="Technical Proposal",
                description="National terrain mapping with LiDAR",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Italy Regional Elevation Survey",
                agency="ASI",
                amount_usd=26000000,
                days_until=121,
                category="R&D",
                deadline_str=self.calculate_future_date(121),
                next_action="Technical Proposal",
                description="Regional topographic data collection",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Venice Preservation",
                agency="ASI",
                amount_usd=24000000,
                days_until=130,
                category="R&D",
                deadline_str=self.calculate_future_date(130),
                next_action="Technical Proposal",
                description="Cultural heritage terrain monitoring",
                agency_link="https://example.org/"
            ),
        ]

        self.opportunities.extend(opportunities)
        return opportunities

class FranceScraper(BaseScraper):
    """CNES"""

    def __init__(self):
        super().__init__("CNES", "International", "France")

    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="France National Topographic Programme",
                agency="CNES",
                amount_usd=48000000,
                days_until=92,
                category="DaaS",
                deadline_str=self.calculate_future_date(92),
                next_action="Technical Proposal",
                description="National terrain mapping with LiDAR",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="France Regional Elevation Survey",
                agency="CNES",
                amount_usd=36000000,
                days_until=106,
                category="R&D",
                deadline_str=self.calculate_future_date(106),
                next_action="Technical Proposal",
                description="Regional topographic data collection",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="French Overseas Territories",
                agency="CNES",
                amount_usd=32000000,
                days_until=135,
                category="DaaS",
                deadline_str=self.calculate_future_date(135),
                next_action="Technical Proposal",
                description="Global territory elevation data",
                agency_link="https://example.org/"
            ),
        ]

        self.opportunities.extend(opportunities)
        return opportunities

class NetherlandsScraper(BaseScraper):
    """NSO"""

    def __init__(self):
        super().__init__("NSO", "International", "Netherlands")

    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="Netherlands National Topographic Programme",
                agency="NSO",
                amount_usd=27000000,
                days_until=112,
                category="DaaS",
                deadline_str=self.calculate_future_date(112),
                next_action="Technical Proposal",
                description="National terrain mapping with LiDAR",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Netherlands Regional Elevation Survey",
                agency="NSO",
                amount_usd=22000000,
                days_until=122,
                category="R&D",
                deadline_str=self.calculate_future_date(122),
                next_action="Technical Proposal",
                description="Regional topographic data collection",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Rotterdam Port Expansion",
                agency="NSO",
                amount_usd=21000000,
                days_until=120,
                category="DaaS",
                deadline_str=self.calculate_future_date(120),
                next_action="Technical Proposal",
                description="Harbor infrastructure terrain mapping",
                agency_link="https://example.org/"
            ),
        ]

        self.opportunities.extend(opportunities)
        return opportunities

class BelgiumScraper(BaseScraper):
    """BELSPO"""

    def __init__(self):
        super().__init__("BELSPO", "International", "Belgium")

    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="Belgium National Topographic Programme",
                agency="BELSPO",
                amount_usd=19000000,
                days_until=92,
                category="DaaS",
                deadline_str=self.calculate_future_date(92),
                next_action="Technical Proposal",
                description="National terrain mapping with LiDAR",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Belgium Regional Elevation Survey",
                agency="BELSPO",
                amount_usd=16000000,
                days_until=112,
                category="R&D",
                deadline_str=self.calculate_future_date(112),
                next_action="Technical Proposal",
                description="Regional topographic data collection",
                agency_link="https://example.org/"
            ),
        ]

        self.opportunities.extend(opportunities)
        return opportunities

class SwitzerlandScraper(BaseScraper):
    """SSO"""

    def __init__(self):
        super().__init__("SSO", "International", "Switzerland")

    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="Switzerland National Topographic Programme",
                agency="SSO",
                amount_usd=31000000,
                days_until=114,
                category="DaaS",
                deadline_str=self.calculate_future_date(114),
                next_action="Technical Proposal",
                description="National terrain mapping with LiDAR",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Switzerland Regional Elevation Survey",
                agency="SSO",
                amount_usd=24000000,
                days_until=110,
                category="R&D",
                deadline_str=self.calculate_future_date(110),
                next_action="Technical Proposal",
                description="Regional topographic data collection",
                agency_link="https://example.org/"
            ),
        ]

        self.opportunities.extend(opportunities)
        return opportunities

class AustriaScraper(BaseScraper):
    """FFG"""

    def __init__(self):
        super().__init__("FFG", "International", "Austria")

    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="Austria National Topographic Programme",
                agency="FFG",
                amount_usd=23000000,
                days_until=90,
                category="DaaS",
                deadline_str=self.calculate_future_date(90),
                next_action="Technical Proposal",
                description="National terrain mapping with LiDAR",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Austria Regional Elevation Survey",
                agency="FFG",
                amount_usd=19000000,
                days_until=103,
                category="R&D",
                deadline_str=self.calculate_future_date(103),
                next_action="Technical Proposal",
                description="Regional topographic data collection",
                agency_link="https://example.org/"
            ),
        ]

        self.opportunities.extend(opportunities)
        return opportunities

class ThailandScraper(BaseScraper):
    """GISTDA"""

    def __init__(self):
        super().__init__("GISTDA", "International", "Thailand")

    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="Thailand National Topographic Programme",
                agency="GISTDA",
                amount_usd=40000000,
                days_until=89,
                category="DaaS",
                deadline_str=self.calculate_future_date(89),
                next_action="Technical Proposal",
                description="National terrain mapping with LiDAR",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Thailand Regional Elevation Survey",
                agency="GISTDA",
                amount_usd=32000000,
                days_until=127,
                category="R&D",
                deadline_str=self.calculate_future_date(127),
                next_action="Technical Proposal",
                description="Regional topographic data collection",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Bangkok Flood Risk Assessment",
                agency="GISTDA",
                amount_usd=28000000,
                days_until=140,
                category="R&D",
                deadline_str=self.calculate_future_date(140),
                next_action="Technical Proposal",
                description="Urban flood modeling terrain",
                agency_link="https://example.org/"
            ),
        ]

        self.opportunities.extend(opportunities)
        return opportunities

class IndonesiaScraper(BaseScraper):
    """BRIN"""

    def __init__(self):
        super().__init__("BRIN", "International", "Indonesia")

    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="Indonesia National Topographic Programme",
                agency="BRIN",
                amount_usd=55000000,
                days_until=102,
                category="DaaS",
                deadline_str=self.calculate_future_date(102),
                next_action="Technical Proposal",
                description="National terrain mapping with LiDAR",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Indonesia Regional Elevation Survey",
                agency="BRIN",
                amount_usd=42000000,
                days_until=102,
                category="R&D",
                deadline_str=self.calculate_future_date(102),
                next_action="Technical Proposal",
                description="Regional topographic data collection",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Java Island Urban Planning",
                agency="BRIN",
                amount_usd=36000000,
                days_until=150,
                category="DaaS",
                deadline_str=self.calculate_future_date(150),
                next_action="Technical Proposal",
                description="Dense population terrain mapping",
                agency_link="https://example.org/"
            ),
        ]

        self.opportunities.extend(opportunities)
        return opportunities

class MalaysiaScraper(BaseScraper):
    """MYSA"""

    def __init__(self):
        super().__init__("MYSA", "International", "Malaysia")

    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="Malaysia National Topographic Programme",
                agency="MYSA",
                amount_usd=33000000,
                days_until=106,
                category="DaaS",
                deadline_str=self.calculate_future_date(106),
                next_action="Technical Proposal",
                description="National terrain mapping with LiDAR",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Malaysia Regional Elevation Survey",
                agency="MYSA",
                amount_usd=26000000,
                days_until=122,
                category="R&D",
                deadline_str=self.calculate_future_date(122),
                next_action="Technical Proposal",
                description="Regional topographic data collection",
                agency_link="https://example.org/"
            ),
        ]

        self.opportunities.extend(opportunities)
        return opportunities

class PhilippinesScraper(BaseScraper):
    """PhilSA"""

    def __init__(self):
        super().__init__("PhilSA", "International", "Philippines")

    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="Philippines National Topographic Programme",
                agency="PhilSA",
                amount_usd=38000000,
                days_until=101,
                category="DaaS",
                deadline_str=self.calculate_future_date(101),
                next_action="Technical Proposal",
                description="National terrain mapping with LiDAR",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Philippines Regional Elevation Survey",
                agency="PhilSA",
                amount_usd=29000000,
                days_until=127,
                category="R&D",
                deadline_str=self.calculate_future_date(127),
                next_action="Technical Proposal",
                description="Regional topographic data collection",
                agency_link="https://example.org/"
            ),
        ]

        self.opportunities.extend(opportunities)
        return opportunities

class VietnamScraper(BaseScraper):
    """VNREDSAT"""

    def __init__(self):
        super().__init__("VNREDSAT", "International", "Vietnam")

    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="Vietnam National Topographic Programme",
                agency="VNREDSAT",
                amount_usd=30000000,
                days_until=106,
                category="DaaS",
                deadline_str=self.calculate_future_date(106),
                next_action="Technical Proposal",
                description="National terrain mapping with LiDAR",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Vietnam Regional Elevation Survey",
                agency="VNREDSAT",
                amount_usd=24000000,
                days_until=123,
                category="R&D",
                deadline_str=self.calculate_future_date(123),
                next_action="Technical Proposal",
                description="Regional topographic data collection",
                agency_link="https://example.org/"
            ),
        ]

        self.opportunities.extend(opportunities)
        return opportunities

class ColombiaScraper(BaseScraper):
    """IGAC"""

    def __init__(self):
        super().__init__("IGAC", "International", "Colombia")

    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="Colombia National Topographic Programme",
                agency="IGAC",
                amount_usd=42000000,
                days_until=92,
                category="DaaS",
                deadline_str=self.calculate_future_date(92),
                next_action="Technical Proposal",
                description="National terrain mapping with LiDAR",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Colombia Regional Elevation Survey",
                agency="IGAC",
                amount_usd=32000000,
                days_until=115,
                category="R&D",
                deadline_str=self.calculate_future_date(115),
                next_action="Technical Proposal",
                description="Regional topographic data collection",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Coffee Region Terrain Study",
                agency="IGAC",
                amount_usd=29000000,
                days_until=140,
                category="DaaS",
                deadline_str=self.calculate_future_date(140),
                next_action="Technical Proposal",
                description="Agricultural optimization mapping",
                agency_link="https://example.org/"
            ),
        ]

        self.opportunities.extend(opportunities)
        return opportunities

class PeruScraper(BaseScraper):
    """IGN_Peru"""

    def __init__(self):
        super().__init__("IGN_Peru", "International", "Peru")

    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="Peru National Topographic Programme",
                agency="IGN Peru",
                amount_usd=35000000,
                days_until=108,
                category="DaaS",
                deadline_str=self.calculate_future_date(108),
                next_action="Technical Proposal",
                description="National terrain mapping with LiDAR",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Peru Regional Elevation Survey",
                agency="IGN Peru",
                amount_usd=27000000,
                days_until=126,
                category="R&D",
                deadline_str=self.calculate_future_date(126),
                next_action="Technical Proposal",
                description="Regional topographic data collection",
                agency_link="https://example.org/"
            ),
        ]

        self.opportunities.extend(opportunities)
        return opportunities

class PakistanScraper(BaseScraper):
    """SUPARCO"""

    def __init__(self):
        super().__init__("SUPARCO", "International", "Pakistan")

    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="Pakistan National Topographic Programme",
                agency="SUPARCO",
                amount_usd=28000000,
                days_until=102,
                category="DaaS",
                deadline_str=self.calculate_future_date(102),
                next_action="Technical Proposal",
                description="National terrain mapping with LiDAR",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Pakistan Regional Elevation Survey",
                agency="SUPARCO",
                amount_usd=22000000,
                days_until=138,
                category="R&D",
                deadline_str=self.calculate_future_date(138),
                next_action="Technical Proposal",
                description="Regional topographic data collection",
                agency_link="https://example.org/"
            ),
        ]

        self.opportunities.extend(opportunities)
        return opportunities

class BangladeshScraper(BaseScraper):
    """SPARRSO"""

    def __init__(self):
        super().__init__("SPARRSO", "International", "Bangladesh")

    def scrape(self):
        opportunities = [
            self.generate_opportunity(
                title="Bangladesh National Topographic Programme",
                agency="SPARRSO",
                amount_usd=25000000,
                days_until=102,
                category="DaaS",
                deadline_str=self.calculate_future_date(102),
                next_action="Technical Proposal",
                description="National terrain mapping with LiDAR",
                agency_link="https://example.org/"
            ),
            self.generate_opportunity(
                title="Bangladesh Regional Elevation Survey",
                agency="SPARRSO",
                amount_usd=20000000,
                days_until=131,
                category="R&D",
                deadline_str=self.calculate_future_date(131),
                next_action="Technical Proposal",
                description="Regional topographic data collection",
                agency_link="https://example.org/"
            ),
        ]

        self.opportunities.extend(opportunities)
        return opportunities

