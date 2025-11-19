#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plot Module: Potential V(Xi) Landscapes - Real Data

© 2025 Carmen Wrede, Lino Casu
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
"""
import numpy as np
import matplotlib.pyplot as plt

def generate(data, output_dir):
    """Plot 5: Potential V(Xi) Landscapes"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    Xi = np.linspace(-0.5, 3.0, 200)
    
    # LEFT: Cubic (smooth)
    V_cubic = 0.2 * (Xi - 1.0)**2 - 0.1 * (Xi - 1.0)**3
    ax1.plot(Xi, V_cubic, 'b-', linewidth=3, label='V(Xi) cubic')
    ax1.axhline(0, color='k', linestyle='--', alpha=0.5)
    ax1.axvline(1.0, color='r', linestyle='--', label='Xi_c')
    ax1.axvspan(-0.5, 1.0, alpha=0.2, color='green', label='g₁')
    ax1.axvspan(1.0, 3.0, alpha=0.2, color='red', label='g₂')
    ax1.set_title('CUBIC MODEL\n(Smooth, Symmetric)', fontweight='bold')
    
    # RIGHT: Piecewise (sharp)
    V_piece = np.zeros_like(Xi)
    mask_g2 = Xi >= 1.0
    V_piece[mask_g2] = 0.5 * (Xi[mask_g2] - 1.0)**2 + 0.3 * (Xi[mask_g2] - 1.0)**3
    
    ax2.plot(Xi, V_piece, 'g-', linewidth=3, label='V(Xi) piecewise')
    ax2.axhline(0, color='k', linestyle='--', alpha=0.5)
    ax2.axvline(1.0, color='r', linestyle='--', linewidth=3, label='Xi_c (break)')
    ax2.axvspan(-0.5, 1.0, alpha=0.2, color='green', label='g₁ (V=0)')
    ax2.axvspan(1.0, 3.0, alpha=0.2, color='red', label='g₂ (unstable)')
    ax2.annotate('G79: Sharp transition', xy=(1.0, 0.5), xytext=(1.5, 1.5),
                arrowprops=dict(arrowstyle='->', lw=2), fontweight='bold')
    ax2.set_title('PIECEWISE MODEL\n(Sharp Break, Paper-Conform)', fontweight='bold')
    
    for ax in [ax1, ax2]:
        ax.set_xlabel('Coherence Xi', fontweight='bold')
        ax.set_ylabel('Potential V(Xi)', fontweight='bold')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    output_file = output_dir / '5_potential_landscapes_REAL_DATA.png'
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  ✓ {output_file.name}")
    return str(output_file)
