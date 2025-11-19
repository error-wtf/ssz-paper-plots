#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plot Module: Collapse Rate C(Xi) - Real Data

 2025 Carmen Wrede, Lino Casu
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
"""

© 2025 Carmen Wrede, Lino Casu
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
import numpy as np
import matplotlib.pyplot as plt

def generate(data, output_dir):
    """Plot 1: Collapse Rate C(Xi) from G79 temperature data"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    if data and 'temperatures' in data:
        temp_df = data['temperatures']
        r = temp_df['r_pc'].values
        T = temp_df['T_K'].values
        
        # Xi ~ r/r_crit
        r_crit = 1.0
        Xi = r / r_crit
        
        # Collapse rate from -dT/dr
        dT_dr = np.gradient(T, r)
        C_rate = -dT_dr / np.max(np.abs(dT_dr))
        
        # LEFT: Collapse rate
        ax1.plot(Xi, C_rate, 'b-', linewidth=3, label='G79 Data')
        ax1.axhline(0, color='k', linestyle='--', alpha=0.5)
        ax1.axvline(1.0, color='r', linestyle='--', label='r_crit')
        ax1.axvspan(0, 1.0, alpha=0.2, color='green', label='g₁')
        ax1.axvspan(1.0, Xi.max(), alpha=0.2, color='red', label='g₂')
        ax1.set_xlabel('Coherence Xi', fontweight='bold')
        ax1.set_ylabel('Collapse Rate C(Xi)', fontweight='bold')
        ax1.set_title('G79: C = F[-dV/dXi]³\n(Always Positive)', fontweight='bold')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # RIGHT: Piecewise detection
        mask_inner = Xi <= 1.0
        mask_outer = Xi > 1.0
        C_inner = np.mean(C_rate[mask_inner]) if np.any(mask_inner) else 0
        C_outer = np.mean(C_rate[mask_outer]) if np.any(mask_outer) else 0
        
        ax2.bar(['Inner\n(r<r_c)', 'Outer\n(r>r_c)'], [C_inner, C_outer],
               color=['green', 'red'], alpha=0.7, edgecolor='black', linewidth=2)
        ax2.set_ylabel('Mean Collapse Rate', fontweight='bold')
        ax2.set_title('PIECEWISE: Zero in g₁, Nonlinear in g₂', fontweight='bold')
        ax2.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    output_file = output_dir / '1_collapse_rate_REAL_DATA.png'
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  ✓ {output_file.name}")
    return str(output_file)
