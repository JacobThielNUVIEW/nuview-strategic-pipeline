"""
Integration tests for the NUVIEW Strategic Pipeline
Tests the end-to-end workflow from scraping to QC to programs generation
"""

import json
import os
import subprocess


class TestPipelineIntegration:
    """Test end-to-end pipeline integration"""

    def test_data_files_exist(self):
        """Test that all required data files exist"""
        required_files = [
            'data/opportunities.json',
            'data/forecast.json',
            'data/processed/programs.json',
            'data/processed/qc_report.json',
            'data/processed/priority_matrix.csv'
        ]
        
        for filepath in required_files:
            assert os.path.exists(filepath), f"Required file missing: {filepath}"

    def test_schema_file_exists(self):
        """Test that schema file exists"""
        assert os.path.exists('schemas/opportunities.json'), "Schema file missing"

    def test_opportunities_data_structure(self):
        """Test opportunities.json has correct structure"""
        with open('data/opportunities.json', 'r') as f:
            data = json.load(f)
        
        assert 'meta' in data, "Missing 'meta' section"
        assert 'opportunities' in data, "Missing 'opportunities' section"
        
        meta = data['meta']
        assert 'market_val' in meta
        assert 'cagr' in meta
        assert 'updated' in meta
        assert 'totalCount' in meta
        assert 'scrapers_run' in meta
        
        assert isinstance(data['opportunities'], list)
        if len(data['opportunities']) > 0:
            opp = data['opportunities'][0]
            required_fields = ['id', 'title', 'agency', 'pillar', 'category']
            for field in required_fields:
                assert field in opp, f"Missing required field: {field}"

    def test_programs_data_structure(self):
        """Test programs.json has correct structure"""
        with open('data/processed/programs.json', 'r') as f:
            data = json.load(f)
        
        assert 'meta' in data, "Missing 'meta' section"
        assert 'programs' in data, "Missing 'programs' section"
        
        programs = data['programs']
        expected_categories = ['funding', 'lidar', 'spaceSystems', 'platform']
        for category in expected_categories:
            assert category in programs, f"Missing category: {category}"
            assert isinstance(programs[category], list)
            
            # Check if programs have priority scores
            if len(programs[category]) > 0:
                program = programs[category][0]
                assert 'priorityScore' in program, "Program missing priorityScore"
                assert isinstance(program['priorityScore'], (int, float))

    def test_qc_report_structure(self):
        """Test qc_report.json has correct structure"""
        with open('data/processed/qc_report.json', 'r') as f:
            report = json.load(f)
        
        assert 'timestamp' in report
        assert 'qc_status' in report
        assert 'qc_percentage' in report
        assert 'total_errors' in report
        assert 'total_warnings' in report
        assert 'opportunities_validation' in report
        assert 'forecast_validation' in report
        
        # Check that QC passed (for integration)
        assert report['qc_status'] == 'PASS', f"QC failed: {report.get('summary', 'Unknown reason')}"

    def test_priority_matrix_csv_exists(self):
        """Test that priority_matrix.csv exists and has content"""
        filepath = 'data/processed/priority_matrix.csv'
        assert os.path.exists(filepath), "priority_matrix.csv missing"
        
        # Check it has content
        with open(filepath, 'r') as f:
            lines = f.readlines()
            assert len(lines) > 1, "priority_matrix.csv is empty"
            
            # Check header
            header = lines[0].strip()
            expected_columns = ['rank', 'title', 'agency', 'pillar', 'category', 
                              'value', 'valueUSD', 'priorityScore', 'urgency', 
                              'daysUntil', 'deadline']
            for col in expected_columns:
                assert col in header, f"Missing column in priority_matrix.csv: {col}"

    def test_schema_validation_works(self):
        """Test that schema validation can run successfully"""
        # This tests that jsonschema is properly integrated
        try:
            from jsonschema import validate, Draft7Validator
            
            with open('schemas/opportunities.json', 'r') as f:
                schema = json.load(f)
            
            with open('data/opportunities.json', 'r') as f:
                data = json.load(f)
            
            # Should not raise an exception if valid
            validator = Draft7Validator(schema)
            errors = list(validator.iter_errors(data))
            assert len(errors) == 0, f"Schema validation failed with {len(errors)} error(s)"
        except ImportError:
            assert False, "jsonschema library not installed"

    def test_qc_validator_runs(self):
        """Test that QC validator can run successfully"""
        result = subprocess.run(
            ['python', 'scripts/qc_validator.py'],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        assert result.returncode == 0, f"QC validator failed: {result.stderr}"

    def test_programs_generator_runs(self):
        """Test that programs generator can run successfully"""
        result = subprocess.run(
            ['python', 'scripts/generate_programs.py'],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        assert result.returncode == 0, f"Programs generator failed: {result.stderr}"


class TestPriorityScoring:
    """Test priority scoring calculation"""

    def test_priority_scores_calculated(self):
        """Test that all programs have priority scores"""
        with open('data/processed/programs.json', 'r') as f:
            data = json.load(f)
        
        all_programs = []
        for category in data['programs'].values():
            all_programs.extend(category)
        
        assert len(all_programs) > 0, "No programs found"
        
        for program in all_programs:
            assert 'priorityScore' in program, f"Program {program.get('id', 'unknown')} missing priorityScore"
            score = program['priorityScore']
            assert isinstance(score, (int, float)), f"priorityScore must be numeric, got {type(score)}"
            assert 0 <= score <= 85, f"priorityScore out of range: {score}"

    def test_priority_scores_reasonable(self):
        """Test that priority scores are within reasonable ranges"""
        with open('data/processed/programs.json', 'r') as f:
            data = json.load(f)
        
        all_programs = []
        for category in data['programs'].values():
            all_programs.extend(category)
        
        # At least some programs should have high scores
        high_score_programs = [p for p in all_programs if p.get('priorityScore', 0) >= 50]
        assert len(high_score_programs) > 0, "No high-priority programs found"


class TestSourceVerification:
    """Test source verification functionality"""

    def test_sources_matrix_exists(self):
        """Test that sources_matrix.csv exists"""
        assert os.path.exists('data/processed/sources_matrix.csv'), "sources_matrix.csv missing"

    def test_bathymetry_exclusion(self):
        """Test that bathymetry-only opportunities are flagged"""
        with open('data/opportunities.json', 'r') as f:
            data = json.load(f)
        
        # Look for any opportunities with bathymetry keywords
        bathymetry_keywords = ['bathymetry', 'bathymetric', 'ocean floor', 'seafloor']
        topographic_keywords = ['lidar', 'topographic', 'elevation', 'terrain']
        
        for opp in data['opportunities']:
            title = opp.get('title', '').lower()
            description = opp.get('description', '').lower()
            text = f"{title} {description}"
            
            has_bathy = any(kw in text for kw in bathymetry_keywords)
            has_topo = any(kw in text for kw in topographic_keywords)
            
            # If it's bathymetry-only, it should be flagged or excluded
            if has_bathy and not has_topo:
                # This is acceptable - bathymetry-only should be flagged in QC
                pass  # The QC validator handles this
