#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate local SVR-SSZ plots (no external dependencies)
Simplified version that only creates plots in plots_svr_ssz/
"""

© 2025 Carmen Wrede, Lino Casu
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4

import os
import sys
from pathlib import Path

os.environ['PYTHONIOENCODING'] = 'utf-8:replace'
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except:
        pass

import numpy as np
import matplotlib.pyplot as plt

BASE_PAPER = Path(r"E:\clone\PAPER-RESTORED")

def coherence_decay_and_scaling(outdir: Path):
    """Generate coherence_decay.png and coherence_scaling.png"""
    print("\n" + "="*80)
    print("GENERATING: Coherence decay and E-tau_f scaling plots")
    print("="*80)
    
    outdir.mkdir(parents=True, exist_ok=True)
    
    k = 1.0
    p = 2.2
    gamma_target = 1.9
    c_thresh = 0.1
    c0_values = np.linspace(1.5, 4.0, 6)
    
    t_max = 5.0
    dt = 0.001
    t_grid = np.arange(0.0, t_max + dt, dt)
    
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    
    tau_f_list = []
    E_list = []
    
    for c0 in c0_values:
        c_t = (c0 ** (1.0 - p) + k * (1.0 - p) * t_grid) ** (1.0 / (1.0 - p))
        
        mask = c_t <= c_thresh
        if np.any(mask):
            tau_f = t_grid[mask][0]
        else:
            tau_f = t_max
        
        q = gamma_target * (p - 1.0)
        E_release = c0 ** q
        
        tau_f_list.append(tau_f)
        E_list.append(E_release)
        
        ax1.plot(t_grid, c_t, label=f"c0={c0:.1f}, tau_f≈{tau_f:.2f}")
    
    ax1.axhline(c_thresh, color="k", linestyle="--", alpha=0.5, label="collapse threshold")
    ax1.set_xlabel("t (arb. units)")
    ax1.set_ylabel("c(t)")
    ax1.set_title("Coherence decay for different initial amplitudes c0")
    ax1.legend(fontsize=7)
    fig1.tight_layout()
    fig1.savefig(outdir / "coherence_decay.png", dpi=200)
    plt.close(fig1)
    print(f"  ✓ coherence_decay.png")
    
    # E-tau_f scaling
    tau_f_arr = np.array(tau_f_list)
    E_arr = np.array(E_list)
    
    log_tau = np.log10(tau_f_arr)
    log_E = np.log10(E_arr)
    
    coeffs = np.polyfit(log_tau, log_E, 1)
    gamma_fit, log_A = coeffs
    E_fit = 10 ** log_A * tau_f_arr ** gamma_fit
    
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    ax2.scatter(tau_f_arr, E_arr, label="samples", color="tab:blue")
    ax2.plot(tau_f_arr, E_fit, label=f"fit: E ~ tau_f^{gamma_fit:.2f} (target {gamma_target:.2f})", color="tab:red")
    ax2.set_xscale("log")
    ax2.set_yscale("log")
    ax2.set_xlabel("tau_f (collapse time)")
    ax2.set_ylabel("E (released energy, arb. units)")
    ax2.set_title("Energy-time scaling from coherence decay")
    ax2.legend()
    fig2.tight_layout()
    fig2.savefig(outdir / "coherence_scaling.png", dpi=200)
    plt.close(fig2)
    print(f"  ✓ coherence_scaling.png")


def effective_metric_evolution(outdir: Path):
    """Generate effective_metric_evolution.png"""
    print("\n" + "="*80)
    print("GENERATING: Effective metric evolution plot")
    print("="*80)
    
    outdir.mkdir(parents=True, exist_ok=True)
    
    k = 1.0
    p = 2.2
    c0 = 3.0
    t_max = 5.0
    dt = 0.001
    t_grid = np.arange(0.0, t_max + dt, dt)
    
    c_t = (c0 ** (1.0 - p) + k * (1.0 - p) * t_grid) ** (1.0 / (1.0 - p))
    
    F_SSZ_r0 = 0.6
    G_SSZ_r0 = 1.2
    
    a = 1.0
    b = -0.5
    
    F_eff = F_SSZ_r0 * c_t ** a
    G_eff = G_SSZ_r0 * c_t ** b
    
    fig, ax = plt.subplots(2, 1, figsize=(6, 6), sharex=True)
    
    ax[0].plot(t_grid, F_eff, color="tab:red")
    ax[0].set_ylabel("F_eff(t)")
    ax[0].set_title("Effective metric modulation in the g2 → g1 transition layer")
    
    ax[1].plot(t_grid, G_eff, color="tab:green")
    ax[1].set_xlabel("t (arb. units)")
    ax[1].set_ylabel("G_eff(t)")
    
    fig.tight_layout()
    fig.savefig(outdir / "effective_metric_evolution.png", dpi=200)
    plt.close(fig)
    print(f"  ✓ effective_metric_evolution.png")


def analyze_nested_metrics(output_dir='.'):
    """Generate nested metric analysis plot"""
    print("\n" + "="*80)
    print("GENERATING: Nested sub-metric analysis plot")
    print("="*80)
    
    M_sun = 1.98847e30
    G = 6.67430e-11
    C = 2.99792458e8
    
    alpha = 0.12
    r_c = 1.9
    r_s = 2 * G * M_sun / C**2
    
    # Radial profile
    r_norm = np.linspace(1.5, 10.0, 500)
    r = r_norm * r_s
    
    def gamma_seg(r):
        r_norm = r / r_s
        return 1.0 - alpha * np.exp(-(r_norm / r_c)**2)
    
    gamma = np.array([gamma_seg(ri) for ri in r])
    redshift = gamma
    blueshift = 1.0 / gamma
    
    # Create plots
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('SSZ Nested Sub-Metric: g^(2) subset g^(1)', fontsize=14, fontweight='bold')
    
    # Plot 1: Segmentation field
    ax = axes[0, 0]
    ax.plot(r_norm, gamma, 'b-', linewidth=2, label='γ_seg(r)')
    ax.axhline(1.0, color='gray', linestyle='--', alpha=0.5)
    ax.axhline(0.95, color='red', linestyle=':', label='Boundary γ=0.95')
    ax.set_xlabel('r / r_s', fontsize=11)
    ax.set_ylabel('γ_seg', fontsize=11)
    ax.set_title('Segmentation Field', fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Plot 2: Frequency shifts
    ax = axes[0, 1]
    ax.plot(r_norm, redshift, 'r-', linewidth=2, label='g^(2)→g^(1) (redshift)')
    ax.plot(r_norm, blueshift, 'b-', linewidth=2, label='g^(1)→g^(2) (blueshift)')
    ax.axhline(1.0, color='gray', linestyle='--', alpha=0.5)
    ax.set_xlabel('r / r_s', fontsize=11)
    ax.set_ylabel('Frequency shift factor', fontsize=11)
    ax.set_title('Causal Contact (Both Directions)', fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Plot 3: Metric ratio
    ax = axes[1, 0]
    gamma2 = gamma**2
    ax.plot(r_norm, gamma2, 'purple', linewidth=2, label='g^(2)_μν / g^(1)_μν = γ²')
    ax.axhline(1.0, color='gray', linestyle='--', alpha=0.5)
    ax.set_xlabel('r / r_s', fontsize=11)
    ax.set_ylabel('Metric ratio', fontsize=11)
    ax.set_title('Nested Structure: g^(2) = γ² · g^(1)', fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Plot 4: Broken reciprocity
    ax = axes[1, 1]
    reciprocity = gamma
    ax.plot(r_norm, reciprocity, 'darkgreen', linewidth=2)
    ax.axhline(1.0, color='gray', linestyle='--', alpha=0.5, label='Perfect reciprocity')
    ax.fill_between(r_norm, 0.99, 1.01, color='green', alpha=0.2, label='±1% zone')
    ax.set_xlabel('r / r_s', fontsize=11)
    ax.set_ylabel('dτ^(2) / dt^(1)', fontsize=11)
    ax.set_title('Broken Reciprocity: No Shared Time', fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    output_path = Path(output_dir) / 'plots_svr_ssz' / 'nested_submetric_analysis_local.png'
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"  ✓ nested_submetric_analysis_local.png")


if __name__ == "__main__":
    plot_dir = BASE_PAPER / "plots_svr_ssz"
    
    print("\n" + "#"*80)
    print("# SVR-SSZ LOCAL PLOT GENERATOR")
    print("#"*80)
    
    coherence_decay_and_scaling(plot_dir)
    effective_metric_evolution(plot_dir)
    analyze_nested_metrics(BASE_PAPER)
    
    print("\n" + "="*80)
    print("✓ All local plots generated successfully!")
    print(f"✓ Output directory: {plot_dir}")
    print("="*80)
