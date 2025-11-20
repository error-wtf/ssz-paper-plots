#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Basic Usage Example - SSZ Plot Generation

Simple example showing how to generate plots from G79 observational data.

© 2025 Carmen Wrede, Lino Casu
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
"""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from generate_all_real_data_plots_master import (
    find_data_directory,
    load_real_data,
    generate
)

def main():
    """
    Basic usage: Load data and generate all plots
    """
    print("=" * 60)
    print("SSZ Plot Generation - Basic Example")
    print("=" * 60)
    
    # Step 1: Find data directory
    print("\n[1/3] Finding data directory...")
    try:
        data_dir = find_data_directory()
        print(f"✓ Found: {data_dir}")
    except FileNotFoundError as e:
        print(f"✗ Error: {e}")
        print("\nPlease ensure data/ folder exists with:")
        print("  - G79_temperatures.csv")
        print("  - G79_Rizzo2014_NH3_Table1.csv")
        print("  - G79_gamma_seg_profile.csv")
        print("  - G79_radio_predictions.csv")
        return 1
    
    # Step 2: Load observational data
    print("\n[2/3] Loading observational data...")
    try:
        data = load_real_data(data_dir)
        print(f"✓ Loaded {len(data)} datasets:")
        for key, df in data.items():
            if hasattr(df, '__len__'):
                print(f"  - {key}: {len(df)} points")
            else:
                print(f"  - {key}: {df}")
    except Exception as e:
        print(f"✗ Error loading data: {e}")
        return 1
    
    # Step 3: Generate all plots
    print("\n[3/3] Generating plots...")
    try:
        success = generate()
        if success:
            print("\n" + "=" * 60)
            print("SUCCESS! All plots generated.")
            print("=" * 60)
            print("\nOutput locations:")
            print("  - plots/real-data/      (8 plots)")
            print("  - plots/sharp-break/    (6 plots)")
            print("  - plots/                (2 framework plots)")
            print("\nView plots:")
            print("  - SHOW-PAPER-PLOTS.md   (detailed descriptions)")
            print("  - SHOW-ALL-PLOTS-VISUAL.md (visual gallery)")
            return 0
        else:
            print("\n✗ Plot generation failed")
            return 1
    except Exception as e:
        print(f"\n✗ Error generating plots: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == '__main__':
    sys.exit(main())
