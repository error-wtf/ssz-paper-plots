#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Script: Generate ALL Plots with Real G79 Data
=====================================================
Generates 7 complete plot categories with peer-reviewed observations

© 2025 Carmen Wrede, Lino Casu, Bingsi
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
import sys
import os

os.environ['PYTHONIOENCODING'] = 'utf-8:replace'
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except: pass

def find_g79_data():
    """Locate G79 data - prioritize local data/ folder"""
    local_data = Path(__file__).parent / "data"
    
    # PRIORITY 1: Local data folder (self-contained)
    if local_data.exists():
        return local_data
    
    # PRIORITY 2: Sibling g79-cygnus-test directory
    paths = [
        Path(__file__).parent.parent / "g79-cygnus-test",
        Path("E:/clone/g79-cygnus-test")
    ]
    for p in paths:
        if p.exists(): return p
    
    return None

def load_real_data():
    """Load all G79 data"""
    data_dir = find_g79_data()
    if not data_dir:
        print("⚠ Data directory not found!")
        return None
    
    print(f"Using data from: {data_dir}")
    
    data = {}
    
    # Define file locations (adapt for local vs external)
    if data_dir.name == "data":
        # Local data/ folder structure
        files = {
            'temperatures': data_dir / "G79_temperatures.csv",
            'nh3': data_dir / "G79_Rizzo2014_NH3_Table1.csv",
            'gamma': data_dir / "G79_gamma_seg_profile.csv",
            'radio': data_dir / "G79_radio_predictions.csv"
        }
    else:
        # External g79-cygnus-test structure
        files = {
            'temperatures': data_dir / "data/G79_temperatures.csv",
            'nh3': data_dir / "G79_Rizzo2014_NH3_Table1.csv",
            'gamma': data_dir / "G79_gamma_seg_profile.csv",
            'radio': data_dir / "G79_radio_predictions.csv"
        }
    
    for key, fpath in files.items():
        if fpath.exists():
            data[key] = pd.read_csv(fpath, comment='#')
            print(f"✓ Loaded {key}: {len(data[key])} points")
        else:
            print(f"⚠ Missing {key}: {fpath.name}")
    
    return data

# Import plot modules
import plots_real_collapse_rate
import plots_real_coherence
import plots_real_radio_timing
import plots_real_compatibility
import plots_real_potentials
import plots_real_collapse_4panel
import plots_real_piecewise_4panel

def main():
    print("\n" + "="*70)
    print("GENERATING ALL PLOTS WITH REAL G79 DATA")
    print("="*70 + "\n")
    
    # Load data
    print("Loading real data...")
    data = load_real_data()
    
    # Create output directory
    output_dir = Path("plots/real-data")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate all plots
    print("\nGenerating plots...")
    plots = []
    
    plots.append(plots_real_collapse_rate.generate(data, output_dir))
    plots.append(plots_real_coherence.generate(data, output_dir))
    plots.append(plots_real_radio_timing.generate(data, output_dir))
    plots.append(plots_real_compatibility.generate(data, output_dir))
    plots.append(plots_real_potentials.generate(data, output_dir))
    plots.append(plots_real_collapse_4panel.generate(data, output_dir))
    plots.append(plots_real_piecewise_4panel.generate(data, output_dir))
    
    print("\n" + "="*70)
    print(f"COMPLETE! Generated {len(plots)} plots in {output_dir}")
    print("="*70 + "\n")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
