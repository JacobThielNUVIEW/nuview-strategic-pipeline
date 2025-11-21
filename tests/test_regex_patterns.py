"""
Unit tests for regex patterns in scrapers
Tests budget extraction and other regex patterns
"""
import re


class TestBudgetRegex:
    """Tests for budget extraction regex patterns"""

    def test_budget_pattern_basic(self):
        """Test basic budget pattern extraction"""
        budget_pattern = re.compile(r'\bBudget:\s*\$?([0-9,]+)\b')

        # Test with dollar sign
        text1 = "Budget: $1,000,000 for project"
        matches = budget_pattern.findall(text1)
        assert len(matches) == 1
        assert matches[0] == "1,000,000"

        # Test without dollar sign
        text2 = "Budget: 500,000 allocated"
        matches = budget_pattern.findall(text2)
        assert len(matches) == 1
        assert matches[0] == "500,000"

    def test_budget_pattern_no_commas(self):
        """Test budget pattern with no commas"""
        budget_pattern = re.compile(r'\bBudget:\s*\$?([0-9,]+)\b')

        text = "Budget: $250000 approved"
        matches = budget_pattern.findall(text)
        assert len(matches) == 1
        assert matches[0] == "250000"

    def test_budget_pattern_no_match(self):
        """Test budget pattern with no matching text"""
        budget_pattern = re.compile(r'\bBudget:\s*\$?([0-9,]+)\b')

        text = "No budget information available"
        matches = budget_pattern.findall(text)
        assert len(matches) == 0

    def test_budget_pattern_multiple_spaces(self):
        """Test budget pattern with multiple spaces"""
        budget_pattern = re.compile(r'\bBudget:\s*\$?([0-9,]+)\b')

        text = "Budget:     $2,500,000 funded"
        matches = budget_pattern.findall(text)
        assert len(matches) == 1
        assert matches[0] == "2,500,000"


class TestKeywordPatterns:
    """Tests for keyword-based relevance filtering"""

    def test_bathymetry_exclusion(self):
        """Test that bathymetry data is properly identified for exclusion"""
        text1 = "This is a bathymetry survey project"
        assert "bathymetry" in text1.lower()

        text2 = "This is a topographic LiDAR project"
        assert "bathymetry" not in text2.lower()

    def test_topographic_keywords(self):
        """Test identification of topographic keywords"""
        topographic_keywords = ["lidar", "topographic", "dem", "dsm", "dtm", "elevation"]

        text1 = "LiDAR data collection for elevation mapping"
        has_keyword = any(keyword in text1.lower() for keyword in topographic_keywords)
        assert has_keyword is True

        text2 = "Random unrelated project description"
        has_keyword = any(keyword in text2.lower() for keyword in topographic_keywords)
        assert has_keyword is False

    def test_space_based_lidar_detection(self):
        """Test detection of space-based LiDAR mentions"""
        space_keywords = ["satellite", "space-based", "orbital", "spaceborne"]
        lidar_keywords = ["lidar", "laser scanning"]

        text1 = "Space-based LiDAR system for global mapping"
        has_space = any(keyword in text1.lower() for keyword in space_keywords)
        has_lidar = any(keyword in text1.lower() for keyword in lidar_keywords)
        assert has_space and has_lidar

        text2 = "Terrestrial LiDAR survey"
        has_space = any(keyword in text2.lower() for keyword in space_keywords)
        assert has_space is False
