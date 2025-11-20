#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test data loading functionality"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from generate_all_real_data_plots_master import find_data_directory, load_real_data

def test_find_data_directory():
    """Test that data directory can be found"""
    data_dir = find_data_directory()
    assert data_dir.exists(), f"Data directory not found: {data_dir}"
    assert data_dir.is_dir(), f"Data path is not a directory: {data_dir}"
    print("✓ test_find_data_directory PASSED")

def test_load_temperatures():
    """Test temperature data loading"""
    data_dir = find_data_directory()
    data = load_real_data(data_dir)
    
    assert 'temperatures' in data, "Missing 'temperatures' key"
    temp_df = data['temperatures']
    assert len(temp_df) > 0, "Temperature data is empty"
    assert 'r_pc' in temp_df.columns, "Missing 'r_pc' column"
    assert 'T_K' in temp_df.columns, "Missing 'T_K' column"
    print(f"✓ test_load_temperatures PASSED ({len(temp_df)} points)")

def test_all_datasets():
    """Test all datasets load correctly"""
    data_dir = find_data_directory()
    data = load_real_data(data_dir)
    
    required_keys = ['temperatures', 'nh3', 'gamma', 'radio']
    for key in required_keys:
        assert key in data, f"Missing required key: {key}"
        print(f"  ✓ {key}: loaded")
    print("✓ test_all_datasets PASSED")

if __name__ == '__main__':
    print("Running data loading tests...\n")
    test_find_data_directory()
    test_load_temperatures()
    test_all_datasets()
    print("\nAll tests passed!")
