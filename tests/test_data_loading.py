#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test suite for SSZ Paper Plots data loading functionality

Tests:
- Data directory detection
- CSV file loading
- Data structure validation
- Column presence and types
- Data quality checks

© 2025 Carmen Wrede, Lino Casu
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
"""
import os
import sys
from pathlib import Path
import pandas as pd
import numpy as np

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# UTF-8 handling (Windows compatibility)
os.environ['PYTHONIOENCODING'] = 'utf-8:replace'
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except: 
        pass

from generate_all_real_data_plots_master import find_data_directory, load_real_data

def test_find_data_directory():
    """Test 1: Data directory can be found"""
    print("\n" + "="*80)
    print("TEST 1: FIND DATA DIRECTORY")
    print("="*80)
    
    try:
        data_dir = find_data_directory()
        assert data_dir.exists(), f"Data directory not found: {data_dir}"
        assert data_dir.is_dir(), f"Data path is not a directory: {data_dir}"
        
        print(f"✓ Data directory found: {data_dir}")
        print(f"  Absolute path: {data_dir.absolute()}")
        
        # List contents
        csv_files = list(data_dir.glob("*.csv"))
        print(f"  CSV files found: {len(csv_files)}")
        for csv in csv_files:
            print(f"    - {csv.name}")
        
        print("="*80)
        return True
        
    except Exception as e:
        print(f"✗ FAILED: {e}")
        print("="*80)
        return False

def test_load_temperatures():
    """Test 2: Temperature data loads correctly"""
    print("\n" + "="*80)
    print("TEST 2: LOAD TEMPERATURE DATA")
    print("="*80)
    
    try:
        data_dir = find_data_directory()
        data = load_real_data(data_dir)
        
        assert 'temperatures' in data, "Missing 'temperatures' key"
        temp_df = data['temperatures']
        assert len(temp_df) > 0, "Temperature data is empty"
        
        print(f"✓ Temperature data loaded")
        print(f"  Data points: {len(temp_df)}")
        print(f"  Columns: {list(temp_df.columns)}")
        
        # Validate required columns
        assert 'r_pc' in temp_df.columns, "Missing 'r_pc' column"
        assert 'T_K' in temp_df.columns, "Missing 'T_K' column"
        print(f"  ✓ Required columns present")
        
        # Data range checks
        r_min, r_max = temp_df['r_pc'].min(), temp_df['r_pc'].max()
        T_min, T_max = temp_df['T_K'].min(), temp_df['T_K'].max()
        
        print(f"  Radius range: {r_min:.2f} - {r_max:.2f} pc")
        print(f"  Temperature range: {T_min:.1f} - {T_max:.1f} K")
        
        # Physical sanity checks
        assert r_min >= 0, "Negative radius found"
        assert T_min > 0, "Non-positive temperature found"
        assert r_max < 100, "Unrealistic radius (> 100 pc)"
        assert T_max < 1000, "Unrealistic temperature (> 1000 K)"
        
        print(f"  ✓ Physical values in valid ranges")
        print("="*80)
        return True
        
    except Exception as e:
        print(f"✗ FAILED: {e}")
        print("="*80)
        return False

def test_load_nh3_data():
    """Test 3: NH3 velocity component data loads correctly"""
    print("\n" + "="*80)
    print("TEST 3: LOAD NH3 VELOCITY DATA")
    print("="*80)
    
    try:
        data_dir = find_data_directory()
        data = load_real_data(data_dir)
        
        assert 'nh3' in data, "Missing 'nh3' key"
        nh3_df = data['nh3']
        assert len(nh3_df) > 0, "NH3 data is empty"
        
        print(f"✓ NH3 data loaded")
        print(f"  Components: {len(nh3_df)}")
        print(f"  Columns: {list(nh3_df.columns)}")
        
        # Expected columns (flexible check)
        expected_cols = ['component', 'v_min_kms', 'v_max_kms']
        present_cols = [col for col in expected_cols if col in nh3_df.columns]
        print(f"  ✓ {len(present_cols)}/{len(expected_cols)} expected columns found")
        
        # Display components
        if 'component' in nh3_df.columns:
            components = nh3_df['component'].tolist()
            print(f"  Components: {components}")
        
        print("="*80)
        return True
        
    except Exception as e:
        print(f"✗ FAILED: {e}")
        print("="*80)
        return False

def test_load_gamma_profile():
    """Test 4: Gamma seg profile loads correctly"""
    print("\n" + "="*80)
    print("TEST 4: LOAD GAMMA PROFILE DATA")
    print("="*80)
    
    try:
        data_dir = find_data_directory()
        data = load_real_data(data_dir)
        
        assert 'gamma' in data, "Missing 'gamma' key"
        gamma_df = data['gamma']
        assert len(gamma_df) > 0, "Gamma data is empty"
        
        print(f"✓ Gamma profile loaded")
        print(f"  Data points: {len(gamma_df)}")
        print(f"  Columns: {list(gamma_df.columns)}")
        
        # Check for gamma_seg column
        if 'gamma_seg' in gamma_df.columns:
            gamma_min = gamma_df['gamma_seg'].min()
            gamma_max = gamma_df['gamma_seg'].max()
            print(f"  γ_seg range: {gamma_min:.3f} - {gamma_max:.3f}")
            
            # γ_seg should be ~0.6-1.0
            assert 0.3 < gamma_min < 1.5, f"γ_seg out of expected range: {gamma_min}"
            assert 0.3 < gamma_max < 1.5, f"γ_seg out of expected range: {gamma_max}"
            print(f"  ✓ γ_seg values in physical range")
        
        print("="*80)
        return True
        
    except Exception as e:
        print(f"✗ FAILED: {e}")
        print("="*80)
        return False

def test_load_radio_predictions():
    """Test 5: Radio predictions load correctly"""
    print("\n" + "="*80)
    print("TEST 5: LOAD RADIO PREDICTIONS")
    print("="*80)
    
    try:
        data_dir = find_data_directory()
        data = load_real_data(data_dir)
        
        assert 'radio' in data, "Missing 'radio' key"
        radio_df = data['radio']
        assert len(radio_df) > 0, "Radio data is empty"
        
        print(f"✓ Radio predictions loaded")
        print(f"  Data points: {len(radio_df)}")
        print(f"  Columns: {list(radio_df.columns)}")
        
        print("="*80)
        return True
        
    except Exception as e:
        print(f"✗ FAILED: {e}")
        print("="*80)
        return False

def test_data_consistency():
    """Test 6: Cross-dataset consistency checks"""
    print("\n" + "="*80)
    print("TEST 6: DATA CONSISTENCY CHECKS")
    print("="*80)
    
    try:
        data_dir = find_data_directory()
        data = load_real_data(data_dir)
        
        print("✓ All datasets loaded successfully")
        
        # Check all required keys present
        required = ['temperatures', 'nh3', 'gamma', 'radio']
        for key in required:
            assert key in data, f"Missing key: {key}"
            print(f"  ✓ {key}: present")
        
        # Check no NaN values in temperature data
        temp_df = data['temperatures']
        nan_count = temp_df.isnull().sum().sum()
        print(f"  NaN values in temperature data: {nan_count}")
        assert nan_count == 0, f"Found {nan_count} NaN values"
        
        # Check data types
        assert pd.api.types.is_numeric_dtype(temp_df['r_pc']), "r_pc not numeric"
        assert pd.api.types.is_numeric_dtype(temp_df['T_K']), "T_K not numeric"
        print(f"  ✓ Data types valid")
        
        print("\n" + "="*80)
        print("ALL DATA LOADING TESTS PASSED ✓")
        print("="*80)
        return True
        
    except Exception as e:
        print(f"✗ FAILED: {e}")
        print("="*80)
        return False

if __name__ == '__main__':
    print("\n" + "="*80)
    print("SSZ PAPER PLOTS - DATA LOADING TEST SUITE")
    print("="*80)
    
    results = []
    results.append(("Find Data Directory", test_find_data_directory()))
    results.append(("Load Temperatures", test_load_temperatures()))
    results.append(("Load NH3 Data", test_load_nh3_data()))
    results.append(("Load Gamma Profile", test_load_gamma_profile()))
    results.append(("Load Radio Predictions", test_load_radio_predictions()))
    results.append(("Data Consistency", test_data_consistency()))
    
    # Summary
    print("\n" + "="*80)
    print("TEST SUMMARY")
    print("="*80)
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status}: {name}")
    
    print(f"\nResults: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 ALL TESTS PASSED!")
        sys.exit(0)
    else:
        print(f"\n⚠️  {total - passed} test(s) failed")
        sys.exit(1)
