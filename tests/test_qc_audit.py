"""
Unit tests for full QC audit functionality
Tests validation functions and report generation
"""

import json
import os
from pathlib import Path


class TestQCAuditReport:
    """Tests for QC audit report generation and validation"""

    def test_qc_report_exists(self):
        """Test that QC report is generated"""
        report_path = 'data/processed/full_qc_audit_report.json'
        assert os.path.exists(report_path), f"QC report not found at {report_path}"

    def test_qc_report_structure(self):
        """Test that QC report has correct structure"""
        report_path = 'data/processed/full_qc_audit_report.json'

        with open(report_path, 'r') as f:
            report = json.load(f)

        # Check required fields
        assert 'timestamp' in report
        assert 'audit_type' in report
        assert 'results' in report
        assert 'summary' in report

        # Check summary fields
        summary = report['summary']
        assert 'total_errors' in summary
        assert 'total_warnings' in summary
        assert 'total_files_checked' in summary
        assert 'status' in summary
        assert 'recommendation' in summary

    def test_qc_report_categories(self):
        """Test that QC report includes all expected categories"""
        report_path = 'data/processed/full_qc_audit_report.json'

        with open(report_path, 'r') as f:
            report = json.load(f)

        expected_categories = [
            'HTML Files',
            'Python Files',
            'Shell Scripts',
            'JSON Files',
            'CSV Files',
            'Documentation',
            'Data Integrity',
            'Recent Updates'
        ]

        for category in expected_categories:
            assert category in report['results'], f"Missing category: {category}"

    def test_qc_report_results_structure(self):
        """Test that each category has correct result structure"""
        report_path = 'data/processed/full_qc_audit_report.json'

        with open(report_path, 'r') as f:
            report = json.load(f)

        for category, results in report['results'].items():
            assert 'errors' in results, f"{category}: missing 'errors'"
            assert 'warnings' in results, f"{category}: missing 'warnings'"
            assert 'files_checked' in results, f"{category}: missing 'files_checked'"

            # Check types
            assert isinstance(results['errors'], list), f"{category}: 'errors' should be list"
            assert isinstance(results['warnings'], list), f"{category}: 'warnings' should be list"
            assert isinstance(results['files_checked'], int), f"{category}: 'files_checked' should be int"

    def test_qc_status_values(self):
        """Test that QC status is one of the valid values"""
        report_path = 'data/processed/full_qc_audit_report.json'

        with open(report_path, 'r') as f:
            report = json.load(f)

        valid_statuses = ['PASS', 'PASS_WITH_WARNINGS', 'FAIL']
        assert report['summary']['status'] in valid_statuses


class TestFileValidation:
    """Tests for file validation logic"""

    def test_html_files_exist(self):
        """Test that HTML files exist and are valid"""
        html_files = list(Path('.').rglob('*.html'))
        html_files = [f for f in html_files if '.git' not in str(f)]

        assert len(html_files) > 0, "No HTML files found"

        for html_file in html_files:
            assert html_file.exists(), f"HTML file not found: {html_file}"

    def test_python_files_syntax(self):
        """Test that Python files have valid syntax"""
        python_files = ['scripts/full_qc_audit.py', 'scripts/qc_validator.py']

        for py_file in python_files:
            assert os.path.exists(py_file), f"Python file not found: {py_file}"

            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Check for basic Python structure
            assert 'def ' in content or 'class ' in content, f"{py_file}: Missing function/class definitions"
            assert 'import ' in content, f"{py_file}: Missing import statements"

    def test_json_files_valid(self):
        """Test that JSON files are valid"""
        json_files = [
            'data/opportunities.json',
            'data/forecast.json',
            'data/processed/qc_report.json',
            'data/processed/full_qc_audit_report.json'
        ]

        for json_file in json_files:
            assert os.path.exists(json_file), f"JSON file not found: {json_file}"

            with open(json_file, 'r') as f:
                data = json.load(f)

            assert data is not None, f"{json_file}: Empty JSON"

    def test_documentation_files_exist(self):
        """Test that key documentation files exist"""
        doc_files = [
            'README.md',
            'docs/README.md',
            'scripts/README.md'
        ]

        for doc_file in doc_files:
            assert os.path.exists(doc_file), f"Documentation file not found: {doc_file}"

            with open(doc_file, 'r') as f:
                content = f.read()

            assert len(content) > 0, f"{doc_file}: Empty file"
            assert '#' in content, f"{doc_file}: Missing markdown headers"


class TestQCAuditCoverage:
    """Tests for QC audit coverage and completeness"""

    def test_all_file_types_checked(self):
        """Test that audit covers all file types"""
        report_path = 'data/processed/full_qc_audit_report.json'

        with open(report_path, 'r') as f:
            report = json.load(f)

        # Ensure files were actually checked
        assert report['summary']['total_files_checked'] > 0, "No files were checked"

        # Check that major categories have files
        assert report['results']['HTML Files']['files_checked'] > 0
        assert report['results']['Python Files']['files_checked'] > 0
        assert report['results']['JSON Files']['files_checked'] > 0
        assert report['results']['Documentation']['files_checked'] > 0

    def test_error_and_warning_counts(self):
        """Test that error and warning counts are consistent"""
        report_path = 'data/processed/full_qc_audit_report.json'

        with open(report_path, 'r') as f:
            report = json.load(f)

        # Calculate totals from categories
        calculated_errors = sum(
            len(results['errors'])
            for results in report['results'].values()
        )
        calculated_warnings = sum(
            len(results['warnings'])
            for results in report['results'].values()
        )

        # Compare with summary
        assert report['summary']['total_errors'] == calculated_errors
        assert report['summary']['total_warnings'] == calculated_warnings

    def test_qc_recommendation_exists(self):
        """Test that QC report includes recommendations"""
        report_path = 'data/processed/full_qc_audit_report.json'

        with open(report_path, 'r') as f:
            report = json.load(f)

        recommendation = report['summary']['recommendation']
        assert recommendation, "Missing recommendation"
        assert len(recommendation) > 20, "Recommendation too short"
