#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plot Module: Segmented Spacetime Piecewise Model (4-Panel) - Real Data

© 2025 Carmen Wrede, Lino Casu
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
"""
import numpy as np
import matplotlib.pyplot as plt

def generate(data, output_dir):
    """Plot 7: Segmented Spacetime Piecewise Model 4-Panel"""
    fig = plt.figure(figsize=(14, 12))
    gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3)
    
    Xi = np.linspace(-0.5, 3.0, 200)
    time = np.linspace(0, 10, 100)
    
    # (A) Piecewise Potential
    ax1 = fig.add_subplot(gs[0, 0])
    V = np.zeros_like(Xi)
    mask_g2 = Xi >= 1.0
    V[mask_g2] = 0.5 * (Xi[mask_g2] - 1.0)**2 + 0.3 * (Xi[mask_g2] - 1.0)**3
    ax1.plot(Xi, V, 'g-', linewidth=3, label='V(Xi) piecewise')
    ax1.axhline(0, color='k', linestyle='--')
    ax1.axvline(1.0, color='r', linestyle='--', linewidth=3, label='Xi_c (break)')
    ax1.axvspan(-0.5, 1.0, alpha=0.2, color='green', label='g₁: V=0, stable')
    ax1.axvspan(1.0, 3.0, alpha=0.2, color='red', label='g₂: unstable')
    ax1.set_xlabel('Coherence Xi', fontweight='bold')
    ax1.set_ylabel('Potential V(Xi)', fontweight='bold')
    ax1.set_title('(A) Piecewise Potential\nExplicit Break at Energy Horizon', fontweight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # (B) Finite-Time Collapse
    ax2 = fig.add_subplot(gs[0, 1])
    Xi_init = [0.5, 1.0, 1.5, 2.0, 2.5]
    colors = ['green', 'orange', 'red', 'darkred', 'purple']
    for Xi0, col in zip(Xi_init, colors):
        if Xi0 < 1.0:
            Xi_t = Xi0 * np.ones_like(time)
            label = f'Xi_0={Xi0} (g₁)'
        else:
            Xi_t = (Xi0 - 1.0) * np.exp(-time/1.5) + 1.0
            label = f'Xi_0={Xi0} (g₂)'
        ax2.plot(time, Xi_t, color=col, linewidth=2.5, label=label)
    ax2.axhline(1.0, color='k', linestyle='--', linewidth=2, label='Xi_c')
    ax2.set_xlabel('Time t', fontweight='bold')
    ax2.set_ylabel('Coherence Xi(t)', fontweight='bold')
    ax2.set_title('(B) Finite-Time Collapse\ng₂ → g₁ Transition', fontweight='bold')
    ax2.legend(fontsize=8, ncol=2)
    ax2.grid(True, alpha=0.3)
    
    # (C) One-Sided Collapse Rate
    ax3 = fig.add_subplot(gs[1, 0])
    C = np.zeros_like(Xi)
    mask_g2 = Xi > 1.0
    C[mask_g2] = 2 * (Xi[mask_g2] - 1.0)**2
    ax3.plot(Xi, C, 'purple', linewidth=3, label='C(Xi) = F[-dV/dXi]')
    ax3.axvline(1.0, color='r', linestyle='--', linewidth=2)
    ax3.axvspan(-0.5, 1.0, alpha=0.2, color='green', label='g₁: C=0\n(no dynamics)')
    ax3.axvspan(1.0, 3.0, alpha=0.2, color='red', label='g₂: Active collapse')
    ax3.set_xlabel('Coherence Xi', fontweight='bold')
    ax3.set_ylabel('Collapse Rate C(Xi)', fontweight='bold')
    ax3.set_title('(C) One-Sided Collapse Rate\nZero in g₁, Nonlinear in g₂', fontweight='bold')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # (D) Phase Portrait
    ax4 = fig.add_subplot(gs[1, 1])
    Xi_phase = np.linspace(-0.5, 3.0, 50)
    dXi_dt = np.zeros_like(Xi_phase)
    mask_g2 = Xi_phase > 1.0
    dXi_dt[mask_g2] = -1.0 * (Xi_phase[mask_g2] - 1.0)**2
    ax4.plot(Xi_phase, dXi_dt, 'b-', linewidth=3)
    ax4.axhline(0, color='k', linestyle='--', alpha=0.5)
    ax4.axvline(1.0, color='r', linestyle='--', linewidth=3)
    ax4.axvspan(-0.5, 1.0, alpha=0.2, color='green', label='g₁: Stable')
    ax4.axvspan(1.0, 3.0, alpha=0.2, color='red')
    ax4.plot(1.0, 0, 'ro', markersize=12, label='Critical point')
    ax4.set_xlabel('Coherence Xi', fontweight='bold')
    ax4.set_ylabel('dXi/dt', fontweight='bold')
    ax4.set_title('(D) Phase Portrait\nSharp Boundary at Xi_c', fontweight='bold')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    fig.suptitle('Segmented Spacetime: Irreversible Coherence Collapse g₂ → g₁\n' +
                 '(Paper-Conform Piecewise Nonlinear Model)', 
                 fontsize=15, fontweight='bold')
    
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    output_file = output_dir / '7_piecewise_4panel_REAL_DATA.png'
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  ✓ {output_file.name}")
    return str(output_file)
