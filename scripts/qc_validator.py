"""
QC Validator for NUVIEW Topographic Pipeline Data
Validates opportunities.json and forecast.json for quality and completeness
Outputs qc_report.json with detailed validation results
"""

import json
import os
import sys
from datetime import datetime, timezone

# Required fields for opportunities
REQUIRED_OPP_FIELDS = ['id', 'title', 'agency', 'pillar', 'category', 'forecast_value', 
                       'link', 'deadline', 'next_action', 'timeline', 'funding']
REQUIRED_TIMELINE_FIELDS = ['daysUntil', 'urgency']
REQUIRED_FUNDING_FIELDS = ['amountUSD']
VALID_CATEGORIES = ['DaaS', 'R&D', 'Platform']
VALID_URGENCIES = ['urgent', 'near', 'future']

# NUVIEW color codes for console output
COLOR_GREEN = '\033[92m'  # Success
COLOR_ORANGE = '\033[93m' # Warning
COLOR_RED = '\033[91m'    # Error
COLOR_BLUE = '\033[94m'   # Info
COLOR_RESET = '\033[0m'

def log_info(msg):
    """Log info message in NUVIEW blue"""
    print(f"{COLOR_BLUE}ℹ️  {msg}{COLOR_RESET}")

def log_success(msg):
    """Log success message in NUVIEW green"""
    print(f"{COLOR_GREEN}✅ {msg}{COLOR_RESET}")

def log_warning(msg):
    """Log warning message in NUVIEW orange"""
    print(f"{COLOR_ORANGE}⚠️  {msg}{COLOR_RESET}")

def log_error(msg):
    """Log error message in NUVIEW red"""
    print(f"{COLOR_RED}❌ {msg}{COLOR_RESET}")

def validate_opportunities_file(filepath):
    """Validate opportunities.json structure and content"""
    errors = []
    warnings = []
    
    log_info(f"Validating {filepath}...")
    
    if not os.path.exists(filepath):
        errors.append(f"File not found: {filepath}")
        return errors, warnings, None
    
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        errors.append(f"Invalid JSON in {filepath}: {str(e)}")
        return errors, warnings, None
    
    # Check meta section
    if 'meta' not in data:
        errors.append("Missing 'meta' section")
    else:
        meta = data['meta']
        for field in ['market_val', 'cagr', 'updated', 'totalCount']:
            if field not in meta:
                errors.append(f"Missing meta.{field}")
    
    # Check opportunities array
    if 'opportunities' not in data:
        errors.append("Missing 'opportunities' array")
        return errors, warnings, data
    
    opportunities = data['opportunities']
    
    if not isinstance(opportunities, list):
        errors.append("'opportunities' must be an array")
        return errors, warnings, data
    
    if len(opportunities) == 0:
        warnings.append("No opportunities found (empty array)")
    
    # Validate each opportunity
    for idx, opp in enumerate(opportunities):
        # Check required fields
        for field in REQUIRED_OPP_FIELDS:
            if field not in opp:
                errors.append(f"Opportunity {idx}: Missing required field '{field}'")
        
        # Validate category
        if 'category' in opp and opp['category'] not in VALID_CATEGORIES:
            warnings.append(f"Opportunity {idx} ({opp.get('id', 'unknown')}): Invalid category '{opp['category']}' (expected: {VALID_CATEGORIES})")
        
        # Validate timeline
        if 'timeline' in opp:
            timeline = opp['timeline']
            for field in REQUIRED_TIMELINE_FIELDS:
                if field not in timeline:
                    errors.append(f"Opportunity {idx} ({opp.get('id', 'unknown')}): Missing timeline.{field}")
            
            if 'urgency' in timeline and timeline['urgency'] not in VALID_URGENCIES:
                errors.append(f"Opportunity {idx} ({opp.get('id', 'unknown')}): Invalid urgency '{timeline['urgency']}' (expected: {VALID_URGENCIES})")
        
        # Validate funding
        if 'funding' in opp:
            funding = opp['funding']
            for field in REQUIRED_FUNDING_FIELDS:
                if field not in funding:
                    errors.append(f"Opportunity {idx} ({opp.get('id', 'unknown')}): Missing funding.{field}")
            
            if 'amountUSD' in funding and not isinstance(funding['amountUSD'], (int, float)):
                errors.append(f"Opportunity {idx} ({opp.get('id', 'unknown')}): funding.amountUSD must be numeric")
        
        # Check for topographic/LiDAR relevance
        if 'title' in opp:
            title_lower = opp['title'].lower()
            topographic_keywords = ['lidar', 'topographic', 'elevation', '3dep', 'dem', 'mapping', 'terrain']
            if not any(keyword in title_lower for keyword in topographic_keywords):
                # Check category as well
                if opp.get('category') != 'DaaS':
                    warnings.append(f"Opportunity {idx} ({opp.get('id', 'unknown')}): May not be topographic-related (no relevant keywords found)")
    
    # Validate meta.totalCount matches actual count
    if 'meta' in data and 'totalCount' in data['meta']:
        if data['meta']['totalCount'] != len(opportunities):
            errors.append(f"meta.totalCount ({data['meta']['totalCount']}) doesn't match actual count ({len(opportunities)})")
    
    return errors, warnings, data

def validate_forecast_file(filepath):
    """Validate forecast.json structure and content"""
    errors = []
    warnings = []
    
    log_info(f"Validating {filepath}...")
    
    if not os.path.exists(filepath):
        errors.append(f"File not found: {filepath}")
        return errors, warnings, None
    
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        errors.append(f"Invalid JSON in {filepath}: {str(e)}")
        return errors, warnings, None
    
    # Check required fields
    required_fields = ['current_year', 'current_value', 'forecast_2030', 'cagr_pct']
    for field in required_fields:
        if field not in data:
            errors.append(f"Missing required field '{field}'")
    
    # Validate numeric fields
    if 'current_value' in data and not isinstance(data['current_value'], (int, float)):
        errors.append("current_value must be numeric")
    
    if 'forecast_2030' in data and not isinstance(data['forecast_2030'], (int, float)):
        errors.append("forecast_2030 must be numeric")
    
    if 'cagr_pct' in data and not isinstance(data['cagr_pct'], (int, float)):
        errors.append("cagr_pct must be numeric")
    
    # Check legislative_targets if present
    if 'legislative_targets' in data:
        if not isinstance(data['legislative_targets'], list):
            errors.append("legislative_targets must be an array")
        else:
            for idx, target in enumerate(data['legislative_targets']):
                if 'bill' not in target:
                    warnings.append(f"legislative_targets[{idx}]: Missing 'bill' field")
                if 'impact' not in target:
                    warnings.append(f"legislative_targets[{idx}]: Missing 'impact' field")
    
    return errors, warnings, data

def generate_qc_report(opp_errors, opp_warnings, forecast_errors, forecast_warnings):
    """Generate QC report JSON"""
    total_errors = len(opp_errors) + len(forecast_errors)
    total_warnings = len(opp_warnings) + len(forecast_warnings)
    
    qc_pass = total_errors == 0
    qc_percentage = 100 if qc_pass else 0  # Binary pass/fail
    
    report = {
        "timestamp": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
        "qc_status": "PASS" if qc_pass else "FAIL",
        "qc_percentage": qc_percentage,
        "total_errors": total_errors,
        "total_warnings": total_warnings,
        "opportunities_validation": {
            "errors": opp_errors,
            "warnings": opp_warnings
        },
        "forecast_validation": {
            "errors": forecast_errors,
            "warnings": forecast_warnings
        },
        "summary": f"QC {'PASSED' if qc_pass else 'FAILED'} with {total_errors} errors and {total_warnings} warnings"
    }
    
    return report, qc_pass

def main():
    """Main QC validation logic"""
    log_info("=" * 60)
    log_info("NUVIEW TOPOGRAPHIC PIPELINE - QC VALIDATION")
    log_info("=" * 60)
    
    # Validate opportunities.json
    opp_errors, opp_warnings, opp_data = validate_opportunities_file('data/opportunities.json')
    
    # Validate forecast.json
    forecast_errors, forecast_warnings, forecast_data = validate_forecast_file('data/forecast.json')
    
    # Generate report
    report, qc_pass = generate_qc_report(opp_errors, opp_warnings, forecast_errors, forecast_warnings)
    
    # Save report
    os.makedirs('data/processed', exist_ok=True)
    report_path = 'data/processed/qc_report.json'
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    log_info(f"QC report saved to {report_path}")
    log_info("")
    
    # Display results
    if opp_errors:
        log_error(f"Opportunities validation: {len(opp_errors)} error(s)")
        for err in opp_errors:
            log_error(f"  • {err}")
    else:
        log_success("Opportunities validation: PASSED")
    
    if opp_warnings:
        log_warning(f"Opportunities validation: {len(opp_warnings)} warning(s)")
        for warn in opp_warnings:
            log_warning(f"  • {warn}")
    
    log_info("")
    
    if forecast_errors:
        log_error(f"Forecast validation: {len(forecast_errors)} error(s)")
        for err in forecast_errors:
            log_error(f"  • {err}")
    else:
        log_success("Forecast validation: PASSED")
    
    if forecast_warnings:
        log_warning(f"Forecast validation: {len(forecast_warnings)} warning(s)")
        for warn in forecast_warnings:
            log_warning(f"  • {warn}")
    
    log_info("")
    log_info("=" * 60)
    
    if qc_pass:
        log_success(f"QC STATUS: PASS (100%)")
        log_success(f"Summary: {report['summary']}")
        log_info("=" * 60)
        return 0
    else:
        log_error(f"QC STATUS: FAIL (0%)")
        log_error(f"Summary: {report['summary']}")
        log_error("Data will NOT be pushed to main branch")
        log_info("=" * 60)
        return 1

if __name__ == "__main__":
    sys.exit(main())
