#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SSZ Key Analysis Plots - Standalone
===================================
Regime performance analysis (from generate_key_plots.py)

© 2025 Carmen Wrede, Lino Casu, Bingsi
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

# Golden ratio
PHI = (1 + np.sqrt(5)) / 2

# Performance data by regime
REGIMES = {
    'Photon Sphere\n(r=2-3 r_s)': {'n': 45, 'wins': 37, 'with_phi': 82, 'without_phi': 7},
    'High Velocity\n(v>5% c)': {'n': 21, 'wins': 18, 'with_phi': 86, 'without_phi': 10},
    'Very Close\n(r<2 r_s)': {'n': 29, 'wins': 0, 'with_phi': 0, 'without_phi': 0},
    'Weak Field\n(r>10 r_s)': {'n': 40, 'wins': 15, 'with_phi': 37, 'without_phi': 35}
}

# Radius stratification
RADIUS_DATA = {
    'r_range': ['<1.5', '1.5-2', '2-2.5', '2.5-3', '3-5', '5-10', '>10'],
    'r_center': [1.2, 1.75, 2.25, 2.75, 4, 7.5, 15],
    'n': [10, 19, 22, 23, 24, 16, 29],
    'win_rate': [0, 0, 83, 81, 35, 40, 35]
}

def plot_stratified_performance(output_dir):
    """Plot 1: Performance by regime"""
    fig, ax = plt.subplots(figsize=(12, 7))
    
    regime_names = list(REGIMES.keys())
    win_rates = [REGIMES[r]['with_phi'] for r in regime_names]
    sample_sizes = [REGIMES[r]['n'] for r in regime_names]
    colors = ['#2ecc71', '#3498db', '#e74c3c', '#f39c12']
    
    bars = ax.barh(regime_names, win_rates, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
    
    for i, (regime, n) in enumerate(zip(regime_names, sample_sizes)):
        ax.text(win_rates[i] + 2, i, f'n={n}', va='center', fontsize=10, fontweight='bold')
    
    ax.axvline(50, color='red', linestyle='--', linewidth=2, alpha=0.7, label='50% (random)')
    ax.text(83, 0, 'φ/2 boundary\n≈1.618 r_s', va='center', ha='left', 
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7),
            fontsize=9, fontweight='bold')
    
    ax.set_xlabel('Win Rate (%)', fontsize=14, fontweight='bold')
    ax.set_ylabel('Physical Regime', fontsize=14, fontweight='bold')
    ax.set_title('SEG Performance by Physical Regime\n(WITH φ-based Geometry)', 
                 fontsize=16, fontweight='bold', pad=20)
    ax.set_xlim(0, 100)
    ax.legend(fontsize=11)
    ax.grid(axis='x', alpha=0.3)
    
    plt.tight_layout()
    out = Path(output_dir)/"key_stratified_performance.png"
    plt.savefig(out, dpi=300, bbox_inches='tight')
    plt.close()
    return str(out)

def plot_phi_geometry_impact(output_dir):
    """Plot 2: WITH vs WITHOUT φ-geometry"""
    fig, ax = plt.subplots(figsize=(12, 8))
    
    regime_names = list(REGIMES.keys())
    x = np.arange(len(regime_names))
    width = 0.35
    
    with_phi = [REGIMES[r]['with_phi'] for r in regime_names]
    without_phi = [REGIMES[r]['without_phi'] for r in regime_names]
    
    bars1 = ax.bar(x - width/2, with_phi, width, label='WITH φ-geometry', 
                   color='#2ecc71', alpha=0.8, edgecolor='black', linewidth=1.5)
    bars2 = ax.bar(x + width/2, without_phi, width, label='WITHOUT φ-geometry', 
                   color='#e74c3c', alpha=0.8, edgecolor='black', linewidth=1.5)
    
    for i, (w_phi, wo_phi) in enumerate(zip(with_phi, without_phi)):
        impact = w_phi - wo_phi
        if impact > 5:
            ax.text(i, max(w_phi, wo_phi) + 5, f'+{impact} pp', 
                   ha='center', fontsize=10, fontweight='bold', color='green')
    
    ax.axhline(50, color='gray', linestyle='--', linewidth=1.5, alpha=0.5, label='50% (random)')
    ax.set_ylabel('Win Rate (%)', fontsize=14, fontweight='bold')
    ax.set_title('φ-Geometry Impact: WITH vs WITHOUT φ-based Corrections', 
                 fontsize=16, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(regime_names, fontsize=11)
    ax.legend(fontsize=12, loc='upper left')
    ax.set_ylim(0, 100)
    ax.grid(axis='y', alpha=0.3)
    
    textstr = f'Overall Impact:\nWITH φ: 51%\nWITHOUT φ: 0%\nΔ = +51 pp'
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
    ax.text(0.98, 0.97, textstr, transform=ax.transAxes, fontsize=11,
            verticalalignment='top', horizontalalignment='right', bbox=props, fontweight='bold')
    
    plt.tight_layout()
    out = Path(output_dir)/"key_phi_geometry_impact.png"
    plt.savefig(out, dpi=300, bbox_inches='tight')
    plt.close()
    return str(out)

def plot_winrate_vs_radius(output_dir):
    """Plot 3: Win rate vs radius (φ/2 boundary)"""
    fig, ax = plt.subplots(figsize=(14, 8))
    
    r_centers = RADIUS_DATA['r_center']
    win_rates = RADIUS_DATA['win_rate']
    sample_sizes = RADIUS_DATA['n']
    
    scatter = ax.scatter(r_centers, win_rates, s=[n*20 for n in sample_sizes], 
                        c=win_rates, cmap='RdYlGn', alpha=0.7, edgecolors='black', 
                        linewidth=2, vmin=0, vmax=100)
    
    r_smooth = np.linspace(min(r_centers), max(r_centers), 300)
    win_smooth = np.interp(r_smooth, r_centers, win_rates)
    ax.plot(r_smooth, win_smooth, 'b-', alpha=0.3, linewidth=2, label='Trend')
    
    ax.axvline(PHI, color='gold', linestyle='--', linewidth=3, alpha=0.9, 
              label=f'φ/2 boundary ≈ {PHI:.3f} r_s')
    ax.axvspan(1.5, 3, alpha=0.15, color='green', label='Photon Sphere Region')
    
    peak_idx = win_rates.index(max(win_rates))
    ax.annotate(f'PEAK: {max(win_rates)}%\nat r≈{r_centers[peak_idx]} r_s', 
               xy=(r_centers[peak_idx], max(win_rates)), 
               xytext=(r_centers[peak_idx]+2, max(win_rates)-15),
               arrowprops=dict(arrowstyle='->', lw=2, color='red'),
               fontsize=12, fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8))
    
    ax.axvspan(0, 2, alpha=0.2, color='red', label='Failure Region (r<2)')
    
    ax.set_xlabel('Radius (r/r_s)', fontsize=14, fontweight='bold')
    ax.set_ylabel('Win Rate (%)', fontsize=14, fontweight='bold')
    ax.set_title('SEG Performance vs Radius: φ/2 Boundary Validation\n(Marker size = sample size)', 
                 fontsize=16, fontweight='bold', pad=20)
    ax.set_xlim(0, 20)
    ax.set_ylim(-5, 100)
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(alpha=0.3)
    
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label('Win Rate (%)', fontsize=12, fontweight='bold')
    
    plt.tight_layout()
    out = Path(output_dir)/"key_winrate_vs_radius.png"
    plt.savefig(out, dpi=300, bbox_inches='tight')
    plt.close()
    return str(out)

def plot_stratification_robustness(output_dir):
    """Plot 4: 3D stratification"""
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    # BY RADIUS
    regimes_short = ['PS', 'HV', 'VC', 'WF']
    wins_by_radius = [82, 86, 0, 37]
    ax = axes[0]
    bars = ax.bar(regimes_short, wins_by_radius, color=['#2ecc71', '#3498db', '#e74c3c', '#f39c12'],
                  alpha=0.8, edgecolor='black', linewidth=2)
    ax.axhline(50, color='red', linestyle='--', linewidth=2, alpha=0.7)
    ax.set_ylabel('Win Rate (%)', fontsize=12, fontweight='bold')
    ax.set_title('BY RADIUS\n(DOMINANT FACTOR)', fontsize=13, fontweight='bold', color='darkgreen')
    ax.set_ylim(0, 100)
    ax.grid(axis='y', alpha=0.3)
    ax.text(0.5, 0.95, 'Effect Size:\n82 pp', transform=ax.transAxes,
            ha='center', va='top', fontsize=11, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
    
    # BY DATA SOURCE
    sources = ['NED', 'Non-NED']
    wins_by_source = [45, 53]
    ax = axes[1]
    bars = ax.bar(sources, wins_by_source, color=['#95a5a6', '#7f8c8d'],
                  alpha=0.8, edgecolor='black', linewidth=2)
    ax.axhline(50, color='red', linestyle='--', linewidth=2, alpha=0.7, label='50%')
    ax.set_ylabel('Win Rate (%)', fontsize=12, fontweight='bold')
    ax.set_title('BY DATA SOURCE\n(NO EFFECT)', fontsize=13, fontweight='bold', color='gray')
    ax.set_ylim(0, 100)
    ax.grid(axis='y', alpha=0.3)
    ax.text(0.5, 0.95, 'χ² test:\np > 0.05', transform=ax.transAxes,
            ha='center', va='top', fontsize=11, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.7))
    
    # BY COMPLETENESS
    completeness = ['Complete', 'Partial']
    wins_by_completeness = [52, 48]
    ax = axes[2]
    bars = ax.bar(completeness, wins_by_completeness, color=['#95a5a6', '#7f8c8d'],
                  alpha=0.8, edgecolor='black', linewidth=2)
    ax.axhline(50, color='red', linestyle='--', linewidth=2, alpha=0.7, label='50%')
    ax.set_ylabel('Win Rate (%)', fontsize=12, fontweight='bold')
    ax.set_title('BY COMPLETENESS\n(NO EFFECT)', fontsize=13, fontweight='bold', color='gray')
    ax.set_ylim(0, 100)
    ax.grid(axis='y', alpha=0.3)
    ax.text(0.5, 0.95, 'χ² test:\np > 0.05', transform=ax.transAxes,
            ha='center', va='top', fontsize=11, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.7))
    
    fig.suptitle('3D Stratification: Physics (Radius) Dominates, Not Data Quality', 
                 fontsize=16, fontweight='bold', y=1.02)
    
    plt.tight_layout()
    out = Path(output_dir)/"key_stratification_robustness.png"
    plt.savefig(out, dpi=300, bbox_inches='tight')
    plt.close()
    return str(out)

def plot_performance_heatmap(output_dir):
    """Plot 5: Performance heatmap"""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    categories = ['Photon\nSphere', 'High\nVelocity', 'Very\nClose', 'Weak\nField']
    metrics = ['Win Rate\n(%)', 'Sample\nSize', 'p-value\n(log10)', 'φ Impact\n(pp)']
    
    data = np.array([
        [82, 45, -4, 75],
        [86, 21, -2.8, 76],
        [0, 29, -4, 0],
        [37, 40, -0.8, 3]
    ])
    
    data_normalized = data.copy()
    for j in range(data.shape[1]):
        col = data[:, j]
        if col.max() != col.min():
            data_normalized[:, j] = (col - col.min()) / (col.max() - col.min())
    
    im = ax.imshow(data_normalized.T, cmap='RdYlGn', aspect='auto', vmin=0, vmax=1)
    
    ax.set_xticks(np.arange(len(categories)))
    ax.set_yticks(np.arange(len(metrics)))
    ax.set_xticklabels(categories, fontsize=12, fontweight='bold')
    ax.set_yticklabels(metrics, fontsize=12, fontweight='bold')
    
    for i in range(len(categories)):
        for j in range(len(metrics)):
            if j == 2:
                text = ax.text(i, j, f'{data[i, j]:.1f}',
                              ha="center", va="center", color="black", fontsize=10, fontweight='bold')
            else:
                text = ax.text(i, j, f'{data[i, j]:.0f}',
                              ha="center", va="center", color="black", fontsize=10, fontweight='bold')
    
    ax.set_title('Performance Metrics Heatmap by Regime', fontsize=16, fontweight='bold', pad=20)
    
    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label('Normalized Value', rotation=270, labelpad=20, fontsize=12, fontweight='bold')
    
    plt.tight_layout()
    out = Path(output_dir)/"key_performance_heatmap.png"
    plt.savefig(out, dpi=300, bbox_inches='tight')
    plt.close()
    return str(out)

def generate_all(output_dir):
    """Generate all 5 key analysis plots"""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    plots = []
    print("  [1/5] Stratified performance...")
    plots.append(plot_stratified_performance(output_dir))
    
    print("  [2/5] φ-geometry impact...")
    plots.append(plot_phi_geometry_impact(output_dir))
    
    print("  [3/5] Win rate vs radius...")
    plots.append(plot_winrate_vs_radius(output_dir))
    
    print("  [4/5] Stratification robustness...")
    plots.append(plot_stratification_robustness(output_dir))
    
    print("  [5/5] Performance heatmap...")
    plots.append(plot_performance_heatmap(output_dir))
    
    return plots
