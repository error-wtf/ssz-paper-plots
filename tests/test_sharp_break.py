#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test sharp break detection"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import numpy as np
from generate_all_real_data_plots_master import load_real_data, find_data_directory

def test_sharp_break_location():
    """Test that sharp break is detected at expected location"""
    data = load_real_data(find_data_directory())
    temp_df = data['temperatures']
    
    # Expected break location
    r_c_expected = 0.9  # pc
    tolerance = 0.3  # pc
    
    # Simple curvature detection
    r = temp_df['r_pc'].values
    T = temp_df['T_K'].values
    
    # Second derivative (simplified)
    if len(r) >= 3:
        d2T = np.diff(T, 2)
        r_mid = r[1:-1]
        max_curv_idx = np.argmax(np.abs(d2T))
        r_break = r_mid[max_curv_idx]
        
        diff = abs(r_break - r_c_expected)
        assert diff < tolerance, f"Break at {r_break:.2f} pc, expected {r_c_expected:.2f} pc"
        print(f"✓ test_sharp_break_location PASSED (detected at {r_break:.2f} pc)")
    else:
        print("⚠ Insufficient data points for curvature test")

if __name__ == '__main__':
    print("Running sharp break tests...\n")
    test_sharp_break_location()
    print("\nAll tests passed!")
