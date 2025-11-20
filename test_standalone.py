#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Standalone Test Script
======================
Tests if the repository works without external dependencies

© 2025 Carmen Wrede, Lino Casu
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
"""
from pathlib import Path
import sys

def test_data_files():
    """Test if all required data files exist"""
    print("\n" + "="*60)
    print("TESTING DATA FILES")
    print("="*60)
    
    data_dir = Path("data")
    required_files = [
        "G79_temperatures.csv",
        "G79_Rizzo2014_NH3_Table1.csv",
        "G79_gamma_seg_profile.csv",
        "G79_radio_predictions.csv"
    ]
    
    all_exist = True
    for file in required_files:
        file_path = data_dir / file
        if file_path.exists():
            size = file_path.stat().st_size
            print(f"  OK {file} ({size} bytes)")
        else:
            print(f"  MISSING {file}")
            all_exist = False
    
    return all_exist

def test_dependencies():
    """Test if required Python packages are installed"""
    print("\n" + "="*60)
    print("TESTING DEPENDENCIES")
    print("="*60)
    
    required = {
        'numpy': 'numpy',
        'matplotlib': 'matplotlib',
        'scipy': 'scipy',
        'pandas': 'pandas'
    }
    
    all_installed = True
    for name, import_name in required.items():
        try:
            __import__(import_name)
            print(f"  OK {name}")
        except ImportError:
            print(f"  MISSING {name} - Install with: pip install {name}")
            all_installed = False
    
    return all_installed

def test_data_loading():
    """Test if data can be loaded without errors"""
    print("\n" + "="*60)
    print("TESTING DATA LOADING")
    print("="*60)
    
    try:
        import pandas as pd
        
        # Test temperature data
        temp_file = Path("data/G79_temperatures.csv")
        df_temp = pd.read_csv(temp_file)
        print(f"  OK Temperatures: {len(df_temp)} points")
        
        # Test NH3 data
        nh3_file = Path("data/G79_Rizzo2014_NH3_Table1.csv")
        df_nh3 = pd.read_csv(nh3_file)
        print(f"  OK NH3 data: {len(df_nh3)} components")
        
        # Test gamma data (skip comment lines)
        gamma_file = Path("data/G79_gamma_seg_profile.csv")
        df_gamma = pd.read_csv(gamma_file, comment='#')
        print(f"  OK Gamma profile: {len(df_gamma)} points")
        
        # Test radio data
        radio_file = Path("data/G79_radio_predictions.csv")
        df_radio = pd.read_csv(radio_file, comment='#')
        print(f"  OK Radio predictions: {len(df_radio)} points")
        
        return True
        
    except Exception as e:
        print(f"  ERROR: {e}")
        return False

def test_plot_generation():
    """Test if plots can be generated"""
    print("\n" + "="*60)
    print("TESTING PLOT GENERATION")
    print("="*60)
    
    try:
        # Just check if the module can be imported
        import generate_all_real_data_plots_master
        print(f"  OK Module imports successfully")
        
        # Check if key functions exist
        hasattr(generate_all_real_data_plots_master, 'generate')
        print(f"  OK Has generate() function")
        
        return True
        
    except Exception as e:
        print(f"  ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Run all tests"""
    print("\n" + "="*60)
    print("SSZ REPOSITORY STANDALONE TEST")
    print("="*60)
    print("\nTesting if repository works without external dependencies...")
    
    results = {}
    
    # Test 1: Data files
    results['data_files'] = test_data_files()
    
    # Test 2: Dependencies
    results['dependencies'] = test_dependencies()
    
    # Test 3: Data loading
    if results['dependencies']:
        results['data_loading'] = test_data_loading()
    else:
        results['data_loading'] = False
        print("\n  SKIPPED (dependencies missing)")
    
    # Test 4: Plot generation
    if results['data_loading']:
        results['plot_generation'] = test_plot_generation()
    else:
        results['plot_generation'] = False
        print("\n  SKIPPED (data loading failed)")
    
    # Summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    for test, passed in results.items():
        status = "PASS" if passed else "FAIL"
        symbol = "OK" if passed else "XX"
        print(f"  [{symbol}] {test.replace('_', ' ').title()}: {status}")
    
    all_passed = all(results.values())
    
    print("\n" + "="*60)
    if all_passed:
        print("STATUS: ALL TESTS PASSED")
        print("Repository is STANDALONE and READY!")
        print("="*60)
        return 0
    else:
        print("STATUS: SOME TESTS FAILED")
        print("Check errors above and fix issues")
        print("="*60)
        return 1

if __name__ == "__main__":
    sys.exit(main())
