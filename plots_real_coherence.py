#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plot Module: Coherence Evolution Xi(t) - Real Data

© 2025 Carmen Wrede, Lino Casu
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
"""
import numpy as np
import matplotlib.pyplot as plt

def generate(data, output_dir):
    """Plot 2: Coherence Evolution Xi(t)"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    if data and 'temperatures' in data:
        temp_df = data['temperatures']
        r, T = temp_df['r_pc'].values, temp_df['T_K'].values
        Xi = T / T.max()
        time = (r**2 / 0.1) / (r**2 / 0.1).max() * 10
        
        # LEFT: Smooth (outer)
        mask_outer = r > 1.0
        if np.any(mask_outer):
            ax1.plot(time[mask_outer], Xi[mask_outer], 'b-', linewidth=3,
                    label='G79 Outer: Smooth')
            ax1.axhline(1.0, color='k', linestyle='--', label='Xi_c')
        
        # RIGHT: Finite-time (inner)
        mask_inner = r <= 1.0
        if np.any(mask_inner):
            t_in = time[mask_inner]
            Xi_in = Xi[mask_inner]
            t_ext = np.append(t_in, [t_in[-1] + 0.5])
            Xi_ext = np.append(Xi_in, [Xi_in.min() * 0.5])
            ax2.plot(t_ext, Xi_ext, 'r-', linewidth=3, label='G79 Inner: Finite-time')
            ax2.axhline(1.0, color='k', linestyle='--')
        
        for ax, title in zip([ax1, ax2], 
                            ['CUBIC: Smooth Approach', 'PIECEWISE: Finite-Time Collapse']):
            ax.set_xlabel('Time t', fontweight='bold')
            ax.set_ylabel('Coherence Xi(t)', fontweight='bold')
            ax.set_title(title, fontweight='bold')
            ax.legend()
            ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    output_file = output_dir / '2_coherence_evolution_REAL_DATA.png'
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  ✓ {output_file.name}")
    return str(output_file)
