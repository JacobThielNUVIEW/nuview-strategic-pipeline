"""
NUVIEW Strategic Pipeline - Global Multilingual Keywords
Comprehensive keyword library for space-based LiDAR topographic data collection

Focus Areas:
- Space-based LiDAR systems
- Large-area topographic collections
- Bare-earth/DEM/DSM data products
- ICESat-2 and similar missions
- Elevation mapping and terrain analysis
"""

# Core LiDAR and Topographic Terms (English)
CORE_LIDAR_KEYWORDS = [
    "lidar", "LiDAR", "LIDAR", "light detection and ranging",
    "laser altimetry", "laser scanning", "photon counting",
    "space-based lidar", "spaceborne lidar", "satellite lidar",
    "airborne lidar", "aerial lidar", "bathymetric lidar",
    "topographic lidar", "full waveform lidar",
]

# ICESat and Space Missions
SPACE_MISSION_KEYWORDS = [
    "ICESAT", "ICESat", "ICESat-2", "ICESAT-2", "icesat",
    "GEDI", "Global Ecosystem Dynamics Investigation",
    "ATLAS", "Advanced Topographic Laser Altimeter System",
    "GLAS", "Geoscience Laser Altimeter System",
    "MOLA", "Mars Orbiter Laser Altimeter",
    "CALIOP", "Cloud-Aerosol Lidar with Orthogonal Polarization",
    "spaceborne laser", "satellite laser altimeter",
]

# Topographic and Elevation Terms
TOPOGRAPHIC_KEYWORDS = [
    "topographic", "topography", "terrain", "elevation",
    "DEM", "digital elevation model", "digital elevation data",
    "DSM", "digital surface model", "digital terrain model", "DTM",
    "bare earth", "bareearth", "bare-earth", "ground surface",
    "terrain mapping", "elevation mapping", "height data",
    "bathymetry", "bathymetric", "seafloor mapping",
    "canopy height", "tree height", "forest structure",
    "3D terrain", "3D elevation", "3D topography",
]

# USGS 3DEP and National Programs
NATIONAL_PROGRAM_KEYWORDS = [
    "3DEP", "3D Elevation Program", "USGS 3DEP",
    "National Elevation Dataset", "NED",
    "National Map", "The National Map",
    "Lidar Base Specification", "LBS",
    "Quality Level", "QL0", "QL1", "QL2",
    "USGS Lidar", "USGS elevation",
]

# Data-as-a-Service and Commercial
DAAS_KEYWORDS = [
    "DaaS", "Data as a Service", "data-as-a-service",
    "geospatial services", "mapping services",
    "lidar services", "elevation services",
    "cloud-based mapping", "on-demand mapping",
    "subscription mapping", "commercial mapping",
]

# Remote Sensing and Earth Observation
REMOTE_SENSING_KEYWORDS = [
    "remote sensing", "earth observation", "EO",
    "geospatial", "geodetic", "geodesy",
    "photogrammetry", "interferometry", "InSAR",
    "synthetic aperture radar", "SAR",
    "point cloud", "3D point cloud", "laser returns",
]

# Agency and Contract Terms
AGENCY_CONTRACT_KEYWORDS = [
    "USGS", "NASA", "NOAA", "USDA", "BLM", "FEMA",
    "Army Corps of Engineers", "USACE",
    "National Geospatial-Intelligence Agency", "NGA",
    "ESA", "European Space Agency",
    "JAXA", "Japan Aerospace Exploration Agency",
    "CSA", "Canadian Space Agency",
    "DLR", "German Aerospace Center",
    "acquisition", "procurement", "solicitation",
    "BAA", "Broad Agency Announcement",
    "RFP", "Request for Proposal", "RFI", "Request for Information",
    "SBIR", "Small Business Innovation Research",
    "contract", "grant", "cooperative agreement",
]

# Multilingual Keywords - Spanish
KEYWORDS_SPANISH = [
    "lidar", "láser", "detección láser",
    "topografía", "topográfico", "elevación",
    "modelo digital de elevación", "MDE",
    "modelo digital de superficie", "MDS",
    "terreno desnudo", "superficie terrestre",
    "mapeo", "cartografía", "altimetría",
    "teledetección", "observación de la tierra",
    "nube de puntos", "escaneo láser",
]

# Multilingual Keywords - French
KEYWORDS_FRENCH = [
    "lidar", "laser", "détection laser",
    "topographie", "topographique", "élévation",
    "modèle numérique d'élévation", "MNE",
    "modèle numérique de surface", "MNS",
    "modèle numérique de terrain", "MNT",
    "sol nu", "surface du sol",
    "cartographie", "altimétrie",
    "télédétection", "observation de la terre",
    "nuage de points", "balayage laser",
]

# Multilingual Keywords - German
KEYWORDS_GERMAN = [
    "lidar", "laser", "lasererfassung",
    "topographie", "topographisch", "höhe",
    "digitales höhenmodell", "DHM",
    "digitales oberflächenmodell", "DOM",
    "digitales geländemodell", "DGM",
    "nackter boden", "geländeoberfläche",
    "kartierung", "höhenmessung", "altimetrie",
    "fernerkundung", "erdbeobachtung",
    "punktwolke", "laserscannen",
]

# Multilingual Keywords - Italian
KEYWORDS_ITALIAN = [
    "lidar", "laser", "rilevamento laser",
    "topografia", "topografico", "elevazione",
    "modello digitale di elevazione", "MDE",
    "modello digitale di superficie", "MDS",
    "modello digitale del terreno", "MDT",
    "terreno nudo", "superficie del terreno",
    "mappatura", "cartografia", "altimetria",
    "telerilevamento", "osservazione della terra",
    "nuvola di punti", "scansione laser",
]

# Multilingual Keywords - Portuguese
KEYWORDS_PORTUGUESE = [
    "lidar", "laser", "detecção a laser",
    "topografia", "topográfico", "elevação",
    "modelo digital de elevação", "MDE",
    "modelo digital de superfície", "MDS",
    "modelo digital de terreno", "MDT",
    "solo nu", "superfície do solo",
    "mapeamento", "cartografia", "altimetria",
    "sensoriamento remoto", "observação da terra",
    "nuvem de pontos", "varredura a laser",
]

# Multilingual Keywords - Japanese
KEYWORDS_JAPANESE = [
    "lidar", "ライダー", "レーザー",
    "レーザー測距", "レーザースキャン",
    "地形", "地形図", "標高",
    "数値標高モデル", "DEM",
    "数値表面モデル", "DSM",
    "数値地形モデル", "DTM",
    "裸地", "地表面",
    "マッピング", "地図作成", "測高",
    "リモートセンシング", "地球観測",
    "点群", "ポイントクラウド",
]

# Multilingual Keywords - Chinese (Simplified)
KEYWORDS_CHINESE = [
    "lidar", "激光雷达", "激光",
    "激光测距", "激光扫描",
    "地形", "地形图", "高程",
    "数字高程模型", "DEM",
    "数字表面模型", "DSM",
    "数字地形模型", "DTM",
    "裸地", "地表",
    "制图", "测绘", "测高",
    "遥感", "地球观测",
    "点云", "激光点云",
]

# Multilingual Keywords - Russian
KEYWORDS_RUSSIAN = [
    "lidar", "лидар", "лазер",
    "лазерное сканирование", "лазерная альтиметрия",
    "топография", "топографический", "высота",
    "цифровая модель рельефа", "ЦМР",
    "цифровая модель поверхности", "ЦМП",
    "цифровая модель местности", "ЦММ",
    "голая земля", "поверхность земли",
    "картография", "картирование", "альтиметрия",
    "дистанционное зондирование", "наблюдение Земли",
    "облако точек", "лазерное сканирование",
]

# Technical Specifications and Standards
TECHNICAL_KEYWORDS = [
    "LAS", "LAZ", "E57", "point cloud format",
    "accuracy", "precision", "vertical accuracy",
    "horizontal accuracy", "point density",
    "returns", "first return", "last return", "multiple returns",
    "intensity", "reflectance", "RGB",
    "classification", "ground classification",
    "filtering", "noise removal", "outlier removal",
    "interpolation", "gridding", "rasterization",
    "vertical datum", "horizontal datum", "geoid",
    "WGS84", "NAD83", "NAVD88", "ITRF",
]

# Application Domains
APPLICATION_KEYWORDS = [
    "flood mapping", "flood modeling", "inundation",
    "forest inventory", "forestry", "vegetation",
    "urban planning", "smart cities", "infrastructure",
    "coastal zone", "shoreline", "erosion",
    "hazard assessment", "disaster response", "emergency management",
    "agriculture", "precision agriculture",
    "archaeology", "cultural heritage",
    "mining", "quarry", "excavation",
    "transportation", "road network", "railway",
    "utility corridor", "power line", "pipeline",
]

# Priority Scoring Keywords (High Value Indicators)
HIGH_PRIORITY_KEYWORDS = [
    "space-based", "spaceborne", "satellite",
    "large-area", "large area", "continental", "national", "global",
    "operational", "production", "commercial",
    "multi-year", "long-term", "sustained",
    "IDIQ", "indefinite delivery", "task order",
    "mission", "constellation", "fleet",
]

# Combine all keyword lists
ALL_KEYWORDS = (
    CORE_LIDAR_KEYWORDS +
    SPACE_MISSION_KEYWORDS +
    TOPOGRAPHIC_KEYWORDS +
    NATIONAL_PROGRAM_KEYWORDS +
    DAAS_KEYWORDS +
    REMOTE_SENSING_KEYWORDS +
    AGENCY_CONTRACT_KEYWORDS +
    KEYWORDS_SPANISH +
    KEYWORDS_FRENCH +
    KEYWORDS_GERMAN +
    KEYWORDS_ITALIAN +
    KEYWORDS_PORTUGUESE +
    KEYWORDS_JAPANESE +
    KEYWORDS_CHINESE +
    KEYWORDS_RUSSIAN +
    TECHNICAL_KEYWORDS +
    APPLICATION_KEYWORDS +
    HIGH_PRIORITY_KEYWORDS
)

# Create sets for efficient lookup (handles Unicode properly)
ALL_KEYWORDS_SET = set(kw.lower() for kw in ALL_KEYWORDS)
HIGH_PRIORITY_SET = set(kw.lower() for kw in HIGH_PRIORITY_KEYWORDS)

def calculate_keyword_score(text, case_sensitive=False):
    """
    Calculate relevance score based on keyword matches in text.

    Args:
        text (str): Text to analyze
        case_sensitive (bool): Whether to perform case-sensitive matching

    Returns:
        dict: Score breakdown with total_score and category scores
    """
    if not text:
        return {"total_score": 0, "matches": 0, "categories": {}}

    # Normalize text for searching
    search_text = text if case_sensitive else text.lower()

    # Count matches by category
    categories = {
        "core_lidar": sum(1 for kw in CORE_LIDAR_KEYWORDS if (kw if case_sensitive else kw.lower()) in search_text),
        "space_mission": sum(1 for kw in SPACE_MISSION_KEYWORDS if (kw if case_sensitive else kw.lower()) in search_text),
        "topographic": sum(1 for kw in TOPOGRAPHIC_KEYWORDS if (kw if case_sensitive else kw.lower()) in search_text),
        "national_program": sum(1 for kw in NATIONAL_PROGRAM_KEYWORDS if (kw if case_sensitive else kw.lower()) in search_text),
        "daas": sum(1 for kw in DAAS_KEYWORDS if (kw if case_sensitive else kw.lower()) in search_text),
        "high_priority": sum(1 for kw in HIGH_PRIORITY_KEYWORDS if (kw if case_sensitive else kw.lower()) in search_text),
    }

    # Calculate weighted score (high priority keywords count more)
    total_score = (
        categories["core_lidar"] * 10 +
        categories["space_mission"] * 15 +
        categories["topographic"] * 8 +
        categories["national_program"] * 12 +
        categories["daas"] * 10 +
        categories["high_priority"] * 20
    )

    total_matches = sum(categories.values())

    return {
        "total_score": total_score,
        "matches": total_matches,
        "categories": categories
    }

def is_topographic_relevant(text, min_score=10):
    """
    Check if text is relevant to topographic/LiDAR opportunities.

    Args:
        text (str): Text to check
        min_score (int): Minimum score threshold for relevance

    Returns:
        bool: True if text is relevant, False otherwise
    """
    if not text:
        return False

    score_data = calculate_keyword_score(text)
    return score_data["total_score"] >= min_score

def extract_matching_keywords(text, case_sensitive=False):
    """
    Extract all matching keywords from text.

    Args:
        text (str): Text to analyze
        case_sensitive (bool): Whether to perform case-sensitive matching

    Returns:
        list: List of matched keywords
    """
    if not text:
        return []

    search_text = text if case_sensitive else text.lower()
    matched = []

    for keyword in ALL_KEYWORDS:
        search_kw = keyword if case_sensitive else keyword.lower()
        if search_kw in search_text:
            matched.append(keyword)

    return matched

if __name__ == "__main__":
    # Test the keyword scoring system
    print("NUVIEW Strategic Pipeline - Global Keywords Test\n")

    test_cases = [
        "USGS 3DEP LiDAR Acquisition for National Topographic Mapping",
        "ICESat-2 Mission Data Processing and Analysis",
        "Spaceborne LiDAR for Large-Area Bare-Earth DEM Generation",
        "Digital Elevation Model Production from Satellite Data",
        "General IT Services Contract",
        "Topografía láser y modelo digital de elevación",  # Spanish
        "Topographie laser et modèle numérique d'élévation",  # French
        "激光雷达地形测绘",  # Chinese
    ]

    for i, test_text in enumerate(test_cases, 1):
        print(f"Test {i}: {test_text[:60]}...")
        score_data = calculate_keyword_score(test_text)
        print(f"  Score: {score_data['total_score']}")
        print(f"  Matches: {score_data['matches']}")
        print(f"  Relevant: {is_topographic_relevant(test_text)}")
        print(f"  Categories: {score_data['categories']}")
        print()
