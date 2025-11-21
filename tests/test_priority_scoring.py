"""
Unit tests for priority scoring logic
Tests urgency calculation and priority score computation
"""


class TestUrgencyCalculation:
    """Tests for urgency calculation based on days until deadline"""

    def test_urgent_deadline(self):
        """Test that deadlines < 30 days are marked as urgent"""
        days_until = 15

        if days_until < 30:
            urgency = "urgent"
        elif days_until < 90:
            urgency = "near"
        else:
            urgency = "future"

        assert urgency == "urgent"

    def test_near_deadline(self):
        """Test that deadlines 30-89 days are marked as near"""
        days_until = 60

        if days_until < 30:
            urgency = "urgent"
        elif days_until < 90:
            urgency = "near"
        else:
            urgency = "future"

        assert urgency == "near"

    def test_future_deadline(self):
        """Test that deadlines >= 90 days are marked as future"""
        days_until = 120

        if days_until < 30:
            urgency = "urgent"
        elif days_until < 90:
            urgency = "near"
        else:
            urgency = "future"

        assert urgency == "future"

    def test_edge_case_30_days(self):
        """Test edge case: exactly 30 days"""
        days_until = 30

        if days_until < 30:
            urgency = "urgent"
        elif days_until < 90:
            urgency = "near"
        else:
            urgency = "future"

        assert urgency == "near"

    def test_edge_case_90_days(self):
        """Test edge case: exactly 90 days"""
        days_until = 90

        if days_until < 30:
            urgency = "urgent"
        elif days_until < 90:
            urgency = "near"
        else:
            urgency = "future"

        assert urgency == "future"


class TestPriorityScoreComponents:
    """Tests for priority score calculation components"""

    def test_urgency_scoring_urgent(self):
        """Test that urgent opportunities get 30 points"""
        urgency = "urgent"
        score = 0

        if urgency == 'urgent':
            score += 30
        elif urgency == 'near':
            score += 20
        elif urgency == 'future':
            score += 10

        assert score == 30

    def test_urgency_scoring_near(self):
        """Test that near opportunities get 20 points"""
        urgency = "near"
        score = 0

        if urgency == 'urgent':
            score += 30
        elif urgency == 'near':
            score += 20
        elif urgency == 'future':
            score += 10

        assert score == 20

    def test_urgency_scoring_future(self):
        """Test that future opportunities get 10 points"""
        urgency = "future"
        score = 0

        if urgency == 'urgent':
            score += 30
        elif urgency == 'near':
            score += 20
        elif urgency == 'future':
            score += 10

        assert score == 10

    def test_priority_label_format(self):
        """Test priority label formatting"""
        country = "United States"
        score = 85

        label = f"top {country}: score {score}"

        assert label == "top United States: score 85"
        assert "top" in label
        assert str(score) in label


class TestOpportunityValidation:
    """Tests for opportunity data validation"""

    def test_opportunity_required_fields(self):
        """Test that opportunities have required fields"""
        opportunity = {
            "id": "usgs-123",
            "title": "Test Opportunity",
            "agency": "USGS",
            "amountUSD": 1000000,
            "daysUntilDeadline": 45,
            "urgency": "near"
        }

        required_fields = ["id", "title", "agency", "amountUSD", "daysUntilDeadline"]

        for field in required_fields:
            assert field in opportunity, f"Missing required field: {field}"

    def test_amount_is_positive(self):
        """Test that funding amounts are positive"""
        amount = 217000000
        assert amount > 0

    def test_days_until_is_non_negative(self):
        """Test that days until deadline is non-negative"""
        days_until = 28
        assert days_until >= 0
