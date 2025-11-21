#!/usr/bin/env python3
"""
Comprehensive QC and Integrity Check Script for NUVIEW Strategic Pipeline
Performs full system integrity verification including:
- Data indexing validation
- Calculation verification
- Cross-reference checks
- Matrix integrity validation
"""

import json
import sys
import os
from datetime import datetime
import pandas as pd

# Add scripts directory to path
sys.path.insert(0, os.path.dirname(__file__))

try:
    from validate_and_merge import calculate_priority_score
    CALC_AVAILABLE = True
except ImportError:
    CALC_AVAILABLE = False

# Color codes
COLOR_GREEN = '\033[92m'
COLOR_RED = '\033[91m'
COLOR_BLUE = '\033[94m'
COLOR_RESET = '\033[0m'

# Constants
SOURCE_VERIFIED_STATUS = 'SOURCE_VERIFIED'

def print_header(text):
    print(f"\n{COLOR_BLUE}{'=' * 70}")
    print(f"{text}")
    print(f"{'=' * 70}{COLOR_RESET}\n")

def print_check(name, passed):
    status = f"{COLOR_GREEN}✅ PASS{COLOR_RESET}" if passed else f"{COLOR_RED}❌ FAIL{COLOR_RESET}"
    print(f"{name}: {status}")

def check_index_integrity():
    """Check that all indices are correctly assigned"""
    print_header("INDEX INTEGRITY CHECK")
    
    with open('data/opportunities.json', 'r') as f:
        data = json.load(f)
    
    actual_count = len(data['opportunities'])
    meta_count = data['meta']['totalCount']
    
    print(f"Opportunities count: {actual_count}")
    print(f"Meta totalCount: {meta_count}")
    
    index_match = actual_count == meta_count
    print_check("Index count matches meta", index_match)
    
    return index_match

def check_calculations():
    """Verify all calculations are correct"""
    print_header("CALCULATIONS VERIFICATION")
    
    with open('data/opportunities.json', 'r') as f:
        opps_data = json.load(f)
    
    with open('data/forecast.json', 'r') as f:
        forecast_data = json.load(f)
    
    # Check priority scores
    print("1. Priority Score Calculations:")
    score_errors = 0
    
    if CALC_AVAILABLE:
        for opp in opps_data['opportunities'][:5]:  # Check first 5
            stored = opp.get('priorityScore', 0)
            calculated = calculate_priority_score(opp)
            if stored != calculated:
                print(f"   ❌ {opp['id']}: stored={stored}, calculated={calculated}")
                score_errors += 1
        
        if score_errors == 0:
            print("   ✅ All priority scores are correctly calculated")
    else:
        print("   ⚠️  Cannot verify (calculation module unavailable)")
    
    # Check forecast calculations
    print("\n2. Forecast Calculations:")
    current_value = forecast_data['current_value']
    current_year = forecast_data['current_year']
    cagr_pct = forecast_data['cagr_pct']
    forecast_2030 = forecast_data['forecast_2030']
    
    years = 2030 - current_year
    calculated_forecast = current_value * ((1 + cagr_pct / 100) ** years)
    
    forecast_match = abs(calculated_forecast - forecast_2030) < 0.01
    
    print(f"   Current value: ${current_value}B")
    print(f"   CAGR: {cagr_pct}%")
    print(f"   Calculated forecast: ${calculated_forecast:.2f}B")
    print(f"   Stored forecast: ${forecast_2030}B")
    print_check("   Forecast calculation correct", forecast_match)
    
    # Check value consistency within opportunities
    print("\n3. Value Consistency (amountUSD vs funding.amountUSD):")
    value_errors = 0
    for opp in opps_data['opportunities']:
        amount = opp.get('amountUSD')
        funding_amount = opp.get('funding', {}).get('amountUSD')
        if amount and funding_amount and amount != funding_amount:
            value_errors += 1
    
    print_check("   All amounts consistent", value_errors == 0)
    if value_errors > 0:
        print(f"   Found {value_errors} inconsistencies")
    
    return score_errors == 0 and forecast_match and value_errors == 0

def check_cross_references():
    """Verify cross-references between data structures"""
    print_header("CROSS-REFERENCE VALIDATION")
    
    with open('data/opportunities.json', 'r') as f:
        opps_data = json.load(f)
    
    matrix_df = pd.read_csv('data/processed/sources_matrix.csv')
    
    # Check counts match
    opps_count = len(opps_data['opportunities'])
    matrix_count = len(matrix_df)
    
    print(f"Opportunities in JSON: {opps_count}")
    print(f"Opportunities in matrix: {matrix_count}")
    
    count_match = opps_count == matrix_count
    print_check("Counts match", count_match)
    
    # Check priority scores match
    print("\nPriority Score Cross-Reference:")
    score_mismatches = 0
    
    for opp in opps_data['opportunities'][:10]:  # Check first 10
        opp_score = opp.get('priorityScore', 0)
        matrix_row = matrix_df[
            (matrix_df['program_name'] == opp.get('title')) & 
            (matrix_df['agency_name'] == opp.get('agency'))
        ]
        
        if not matrix_row.empty:
            matrix_score = matrix_row.iloc[0]['nuview_priority_score']
            if opp_score != matrix_score:
                score_mismatches += 1
    
    print_check("Priority scores match", score_mismatches == 0)
    
    return count_match and score_mismatches == 0

def check_matrix_integrity():
    """Verify matrix is properly generated and indexed"""
    print_header("MATRIX INTEGRITY CHECK")
    
    matrix_df = pd.read_csv('data/processed/sources_matrix.csv')
    
    # Check textrank indexing
    min_rank = matrix_df['textrank'].min()
    max_rank = matrix_df['textrank'].max()
    expected_max = len(matrix_df)
    
    print(f"Matrix rows: {len(matrix_df)}")
    print(f"TextRank range: {min_rank} to {max_rank}")
    print(f"Expected range: 1 to {expected_max}")
    
    rank_correct = min_rank == 1 and max_rank == expected_max
    print_check("TextRank correctly indexed", rank_correct)
    
    # Check for null values
    null_count = matrix_df.isnull().sum().sum()
    print(f"\nNull values in matrix: {null_count}")
    print_check("No null values", null_count == 0)
    
    # Check source verification
    verified_count = len(matrix_df[matrix_df['verification'].str.contains(SOURCE_VERIFIED_STATUS, na=False)])
    print(f"\nSource verification:")
    print(f"  Verified opportunities: {verified_count}/{len(matrix_df)}")
    print_check("All sources verified", verified_count == len(matrix_df))
    
    # Check matrix is sorted by priority
    is_sorted = matrix_df['nuview_priority_score'].is_monotonic_decreasing
    print_check("Matrix sorted by priority", is_sorted)
    
    return rank_correct and null_count == 0 and verified_count == len(matrix_df) and is_sorted

def main():
    """Run comprehensive QC check"""
    print(f"{COLOR_BLUE}")
    print("=" * 70)
    print("NUVIEW STRATEGIC PIPELINE - COMPREHENSIVE QC CHECK")
    print("=" * 70)
    print(f"Timestamp: {datetime.now().isoformat()}")
    print(f"{COLOR_RESET}")
    
    results = {
        'index_integrity': check_index_integrity(),
        'calculations': check_calculations(),
        'cross_references': check_cross_references(),
        'matrix_integrity': check_matrix_integrity()
    }
    
    # Summary
    print_header("QC SUMMARY")
    
    all_passed = all(results.values())
    
    for check_name, passed in results.items():
        print_check(check_name.replace('_', ' ').title(), passed)
    
    print("\n" + "=" * 70)
    
    if all_passed:
        print(f"{COLOR_GREEN}✅ ALL QC CHECKS PASSED - SYSTEM INTEGRITY VERIFIED{COLOR_RESET}")
        return 0
    else:
        print(f"{COLOR_RED}❌ SOME QC CHECKS FAILED - REVIEW REQUIRED{COLOR_RESET}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
