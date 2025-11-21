"""
QC Validator for NUVIEW Topographic Pipeline Data
Validates opportunities.json and forecast.json for quality and completeness
Outputs qc_report.json with detailed validation results
Generates source verification matrix (sources_matrix.csv)
"""

import json
import os
import sys
from datetime import datetime, timezone
import pandas as pd

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
            description_lower = opp.get('description', '').lower()
            combined_text = f"{title_lower} {description_lower}"
            topographic_keywords = ['lidar', 'topographic', 'elevation', '3dep', 'dem', 'mapping', 'terrain']
            if not any(keyword in combined_text for keyword in topographic_keywords):
                # Check category as well
                if opp.get('category') != 'DaaS':
                    title = opp.get('title', 'Unknown Title')
                    opp_id = opp.get('id', 'unknown')
                    warnings.append(f"Opportunity '{title}' ({opp_id}): May not be topographic-related (no relevant keywords found in title or description)")
    
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

def extract_country_from_pillar(pillar, agency):
    """Extract country from pillar or agency name"""
    country_map = {
        'Federal': 'USA',
        'Commercial': 'USA',
        'State': 'USA',
        'USGS': 'USA',
        'NASA': 'USA',
        'NGA': 'USA',
        'DIU': 'USA',
        'USDA Forest Service': 'USA',
        'JAXA': 'Japan',
        'ISRO': 'India',
        'DLR': 'Germany',
        'ESA': 'Europe',
        'EU Commission': 'Europe',
        'UKSA': 'UK',
        'CSA': 'Canada',
        'CNSA': 'China'
    }
    
    # Try agency first
    if agency in country_map:
        return country_map[agency]
    
    # Try pillar
    if pillar in country_map:
        return country_map[pillar]
    
    # Try to extract from pillar if it's descriptive
    pillar_lower = pillar.lower() if pillar else ''
    if 'japan' in pillar_lower:
        return 'Japan'
    elif 'india' in pillar_lower:
        return 'India'
    elif 'germany' in pillar_lower or 'german' in pillar_lower:
        return 'Germany'
    elif 'europe' in pillar_lower or 'eu' in pillar_lower:
        return 'Europe'
    elif 'uk' in pillar_lower or 'britain' in pillar_lower:
        return 'UK'
    elif 'canada' in pillar_lower:
        return 'Canada'
    elif 'china' in pillar_lower:
        return 'China'
    
    # Default to Global if unknown
    return 'Global'

def is_bathymetry_only(title, description):
    """Check if the opportunity is bathymetry-only (out of scope)"""
    bathymetry_keywords = ['bathymetry', 'bathymetric', 'ocean floor', 'seafloor', 'underwater mapping', 
                           'subsea', 'seabed', 'marine survey', 'hydrographic', 'ocean depth']
    topographic_keywords = ['lidar', 'topographic', 'elevation', '3dep', 'dem', 'terrain', 'dtm', 'dsm',
                           'terrestrial', 'land surface', 'above water']
    
    text = f"{title} {description}".lower()
    
    # Check if bathymetry keywords present
    has_bathymetry = any(keyword in text for keyword in bathymetry_keywords)
    
    # Check if topographic keywords present
    has_topographic = any(keyword in text for keyword in topographic_keywords)
    
    # It's bathymetry-only if it has bathymetry keywords but no topographic keywords
    return has_bathymetry and not has_topographic

def validate_source(url):
    """Validate if a source URL is valid and not a placeholder"""
    if not url or url == '#' or url == '' or url.lower() == 'none':
        return False
    
    # Check if it's a real URL
    if url.startswith('http://') or url.startswith('https://'):
        return True
    
    return False

def generate_source_verification_matrix(opportunities_data):
    """
    Generate source verification matrix from opportunities data
    Returns: pandas DataFrame with verification matrix
    """
    log_info("Generating source verification matrix...")
    
    if not opportunities_data or 'opportunities' not in opportunities_data:
        log_error("No opportunities data available for matrix generation")
        return None, 0, 0
    
    opportunities = opportunities_data['opportunities']
    matrix_rows = []
    missing_sources_count = 0
    bathymetry_flagged_count = 0
    
    for idx, opp in enumerate(opportunities):
        # Extract base fields
        agency_name = opp.get('agency', 'Unknown')
        program_name = opp.get('title', 'Unknown')
        budget_amount_usd = opp.get('amountUSD', 0)
        nuview_priority_score = opp.get('priorityScore', 0)
        data_access = opp.get('category', 'Unknown')
        pillar = opp.get('pillar', '')
        description = opp.get('description', '')
        
        # Extract country
        country = extract_country_from_pillar(pillar, agency_name)
        
        # Collect all sources
        link = opp.get('link', '')
        budget_source_link = opp.get('budgetSourceLink', '')
        agency_link = opp.get('agencyLink', '')
        
        # Build sources string
        valid_sources = []
        if validate_source(link):
            valid_sources.append(link)
        if validate_source(budget_source_link):
            valid_sources.append(budget_source_link)
        if validate_source(agency_link):
            valid_sources.append(agency_link)
        
        sources_str = '; '.join(valid_sources) if valid_sources else 'NO_SOURCE'
        
        # Check if bathymetry-only
        is_bathy_only = is_bathymetry_only(program_name, description)
        
        # Build verification note
        verification_notes = []
        
        if not valid_sources:
            verification_notes.append('MISSING_SOURCE')
            missing_sources_count += 1
            log_warning(f"Missing source for opportunity: {program_name} ({opp.get('id', 'unknown')})")
        else:
            verification_notes.append('SOURCE_VERIFIED')
        
        if is_bathy_only:
            verification_notes.append('BATHYMETRY_ONLY_FLAGGED')
            bathymetry_flagged_count += 1
            log_warning(f"Bathymetry-only flagged: {program_name} ({opp.get('id', 'unknown')})")
        
        verification = ', '.join(verification_notes) if verification_notes else 'VERIFIED'
        
        # Create row
        row = {
            'textrank': idx + 1,  # Initial rank, will be re-sorted by priority
            'country': country,
            'agency_name': agency_name,
            'program_name': program_name,
            'budget_amount_usd': budget_amount_usd,
            'nuview_priority_score': nuview_priority_score,
            'data_access': data_access,
            'sources': sources_str,
            'verification': verification
        }
        
        matrix_rows.append(row)
    
    # Create DataFrame
    df = pd.DataFrame(matrix_rows)
    
    # Sort by priority score (descending) and re-assign textrank
    df = df.sort_values(by='nuview_priority_score', ascending=False).reset_index(drop=True)
    df['textrank'] = range(1, len(df) + 1)
    
    # Check for NaN values
    if df.isnull().any().any():
        log_warning("Matrix contains null/NaN values, filling with defaults...")
        df = df.fillna({
            'textrank': 0,
            'country': 'Unknown',
            'agency_name': 'Unknown',
            'program_name': 'Unknown',
            'budget_amount_usd': 0,
            'nuview_priority_score': 0,
            'data_access': 'Unknown',
            'sources': 'NO_SOURCE',
            'verification': 'UNVERIFIED'
        })
    
    log_info(f"Matrix generated: {len(df)} opportunities")
    log_info(f"Opportunities missing sources: {missing_sources_count}")
    log_info(f"Bathymetry-only flagged: {bathymetry_flagged_count}")
    
    return df, missing_sources_count, bathymetry_flagged_count

def export_source_matrix(df, output_path='data/processed/sources_matrix.csv'):
    """Export source verification matrix to CSV"""
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False)
        log_success(f"Source matrix exported to {output_path}")
        return True
    except Exception as e:
        log_error(f"Failed to export source matrix: {str(e)}")
        return False

def generate_qc_report(opp_errors, opp_warnings, forecast_errors, forecast_warnings, matrix_export_status=None, matrix_stats=None):
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
    
    # Add matrix export status if provided
    if matrix_export_status is not None:
        report["source_matrix_export"] = {
            "status": "SUCCESS" if matrix_export_status else "FAILED",
            "output_path": "data/processed/sources_matrix.csv"
        }
        
        if matrix_stats:
            report["source_matrix_export"]["statistics"] = matrix_stats
    
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
    
    # Generate source verification matrix
    log_info("")
    log_info("=" * 60)
    log_info("SOURCE VERIFICATION MATRIX GENERATION")
    log_info("=" * 60)
    
    matrix_export_status = False
    matrix_stats = None
    
    if opp_data and 'opportunities' in opp_data:
        matrix_df, missing_sources, bathymetry_flagged = generate_source_verification_matrix(opp_data)
        
        if matrix_df is not None:
            matrix_export_status = export_source_matrix(matrix_df)
            
            # Collect statistics
            matrix_stats = {
                "total_opportunities": len(matrix_df),
                "missing_sources": missing_sources,
                "bathymetry_flagged": bathymetry_flagged,
                "verified_opportunities": len(matrix_df) - missing_sources
            }
    else:
        log_error("Cannot generate source matrix: No opportunity data available")
    
    # Generate report with matrix status
    report, qc_pass = generate_qc_report(opp_errors, opp_warnings, forecast_errors, forecast_warnings, 
                                         matrix_export_status, matrix_stats)
    
    # Save report
    os.makedirs('data/processed', exist_ok=True)
    report_path = 'data/processed/qc_report.json'
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    log_info("")
    log_info("=" * 60)
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
    
    # Display matrix export status
    if matrix_export_status:
        log_success("Source matrix export: SUCCESS")
        if matrix_stats:
            log_info(f"  • Total opportunities: {matrix_stats['total_opportunities']}")
            log_info(f"  • Verified opportunities: {matrix_stats['verified_opportunities']}")
            log_info(f"  • Missing sources: {matrix_stats['missing_sources']}")
            log_info(f"  • Bathymetry flagged: {matrix_stats['bathymetry_flagged']}")
    else:
        log_error("Source matrix export: FAILED")
    
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
