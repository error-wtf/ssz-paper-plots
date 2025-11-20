#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Custom Plots Example - Create your own SSZ plots

© 2025 Carmen Wrede, Lino Casu
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import numpy as np
import matplotlib.pyplot as plt
from generate_all_real_data_plots_master import find_data_directory, load_real_data

def custom_temperature_analysis(data, output_dir='plots/custom/'):
    """Example: Create custom temperature analysis plot"""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    temp_df = data['temperatures']
    r = temp_df['r_pc'].values
    T = temp_df['T_K'].values
    
    # Create custom visualization
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Left: Temperature vs Radius
    ax1.scatter(r, T, s=100, alpha=0.6, edgecolors='black', linewidth=1.5)
    ax1.set_xlabel('Radius (pc)', fontsize=12)
    ax1.set_ylabel('Temperature (K)', fontsize=12)
    ax1.set_title('Custom Temperature Profile', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    # Right: Log-scale
    ax2.scatter(r, T, s=100, alpha=0.6, edgecolors='black', linewidth=1.5, color='red')
    ax2.set_xscale('log')
    ax2.set_yscale('log')
    ax2.set_xlabel('Radius (pc, log scale)', fontsize=12)
    ax2.set_ylabel('Temperature (K, log scale)', fontsize=12)
    ax2.set_title('Log-Log Temperature Profile', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3, which='both')
    
    plt.tight_layout()
    output_file = output_dir / 'custom_temperature_analysis.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"✓ Created: {output_file}")
    return output_file

if __name__ == '__main__':
    print("Custom Plot Example\n" + "="*60)
    data = load_real_data(find_data_directory())
    custom_temperature_analysis(data)
    print("Done!")
