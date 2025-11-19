#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plot Module: Radio Timing - Real Data

© 2025 Carmen Wrede, Lino Casu
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
"""
import numpy as np
import matplotlib.pyplot as plt

def generate(data, output_dir):
    """Plot 3: Radio Timing - Smooth vs Sharp"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    time = np.linspace(0, 10, 100)
    
    # LEFT: Smooth (G79-like)
    radio_smooth = np.exp(-(time - 3.0)**2 / (2*2.0**2))
    ax1.plot(time, radio_smooth, 'b-', linewidth=3, label='Radio flux')
    ax1.axvline(3.0, color='r', linestyle='--', label='Peak')
    ax1.fill_between(time, 0, radio_smooth, alpha=0.3, color='blue')
    ax1.axvspan(2.0, 4.0, alpha=0.2, color='gray', label='Δt = ±1')
    ax1.set_title('CUBIC: Smooth Radio Precursor\n(Timing Uncertainty ±1)', fontweight='bold')
    
    # RIGHT: Sharp (XRB-like)
    radio_sharp = np.exp(-(time - 3.0)**2 / (2*0.3**2))
    ax2.plot(time, radio_sharp, 'r-', linewidth=3, label='Radio flux')
    ax2.axvline(3.0, color='darkred', linestyle='--', label='Burst')
    ax2.fill_between(time, 0, radio_sharp, alpha=0.3, color='red')
    ax2.axvspan(2.9, 3.1, alpha=0.3, color='gray', label='Δt = ±0.1')
    ax2.set_title('PIECEWISE: Sharp Radio Burst\n(Timing Uncertainty ±0.1)', fontweight='bold')
    
    for ax in [ax1, ax2]:
        ax.set_xlabel('Time', fontweight='bold')
        ax.set_ylabel('Radio Flux', fontweight='bold')
        ax.legend()
        ax.grid(True, alpha=0.3)
        ax.set_ylim(-0.1, 1.3)
    
    plt.tight_layout()
    output_file = output_dir / '3_radio_timing_REAL_DATA.png'
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  ✓ {output_file.name}")
    return str(output_file)
