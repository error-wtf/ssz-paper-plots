#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test plot generation"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from generate_all_real_data_plots_master import load_real_data, find_data_directory
from plots_real_collapse_rate import generate as gen_collapse

def test_single_plot_generation():
    """Test generating a single plot"""
    data = load_real_data(find_data_directory())
    output_dir = Path('test_output')
    output_dir.mkdir(exist_ok=True)
    
    plot_file = gen_collapse(data, output_dir=str(output_dir))
    assert plot_file.exists(), f"Plot not created: {plot_file}"
    assert plot_file.suffix == '.png', "Plot is not PNG format"
    assert plot_file.stat().st_size > 1000, "Plot file too small"
    
    # Cleanup
    plot_file.unlink()
    output_dir.rmdir()
    
    print("✓ test_single_plot_generation PASSED")

if __name__ == '__main__':
    print("Running plot generation tests...\n")
    test_single_plot_generation()
    print("\nAll tests passed!")
