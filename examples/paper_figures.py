#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Paper Figures Example - Generate recommended plots for publications

© 2025 Carmen Wrede, Lino Casu
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from generate_all_real_data_plots_master import load_real_data, find_data_directory
from plots_real_compatibility import generate as gen_compat
from plots_real_piecewise_4panel import generate as gen_piecewise
from generate_sharp_break_plots import generate as gen_sharp

def generate_paper_figures():
    """Generate recommended figures for paper submission"""
    print("="*60)
    print("Generating Paper Figures")
    print("="*60)
    
    # Load data
    print("\n[1/3] Loading data...")
    data = load_real_data(find_data_directory())
    print("✓ Data loaded")
    
    # Figure 1: Model Compatibility (Main result)
    print("\n[2/3] Generating Figure 1: Model Compatibility...")
    gen_compat(data, output_dir='plots/paper/')
    print("✓ Figure 1 complete")
    
    # Figure 2: Piecewise 4-Panel (Comprehensive)
    print("\n[3/3] Generating Figure 2: Piecewise 4-Panel...")
    gen_piecewise(data, output_dir='plots/paper/')
    print("✓ Figure 2 complete")
    
    # Optional: Sharp Break Detection
    print("\nGenerating optional sharp break plots...")
    gen_sharp()
    
    print("\n" + "="*60)
    print("Paper figures ready in plots/paper/")
    print("="*60)

if __name__ == '__main__':
    generate_paper_figures()
