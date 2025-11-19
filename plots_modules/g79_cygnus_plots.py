#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
G79.29+0.46 Plots - Standalone
==============================
Paper figures for G79.29+0.46 nebula (from COMPLETE_PAPER_FIGURES.py)

© 2025 Carmen Wrede, Lino Casu, Bingsi
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from pathlib import Path

# G79 Constants
PC_M = 3.0857e16
M_SUN = 1.989e30
ALPHA = 0.12
R_C = 1.9
T0 = 240  # K
V0 = 10.0  # km/s
V_OBS = 15.0  # km/s

def gamma_seg_g79(r, alpha=ALPHA, r_c=R_C):
    """G79 segmentation field"""
    return 1 - alpha * np.exp(-(r / r_c)**2)

def T_profile(r):
    """Temperature profile"""
    return T0 * gamma_seg_g79(r)

def v_observed(r):
    """Observed velocity"""
    return V0 / gamma_seg_g79(r)

def plot_energy_release(output_dir):
    """Figure 6: Energy release mechanism"""
    r_range = np.linspace(0.1, 5.0, 500)
    
    fig = plt.figure(figsize=(14, 10))
    gs = GridSpec(2, 2, hspace=0.3, wspace=0.3)
    
    v_launch = 10
    v_char = 50
    gamma = gamma_seg_g79(r_range)
    v_release = np.sqrt(v_launch**2 + v_char**2 * (1 - gamma))
    
    ax1 = fig.add_subplot(gs[0, :])
    ax1.plot(r_range, v_release, 'r-', linewidth=2.5, label='v_obs (with release)')
    ax1.axhline(y=v_launch, color='b', linestyle='--', linewidth=2, label=f'v_launch={v_launch} km/s')
    ax1.axhline(y=V_OBS, color='green', linestyle=':', linewidth=2, label=f'Observed: {V_OBS} km/s')
    ax1.axvline(x=2.5, color='black', linestyle='--', alpha=0.5, label='g⁽²⁾→g⁽¹⁾ boundary')
    ax1.fill_between(r_range, v_launch, v_release, alpha=0.3, color='orange')
    ax1.set_xlabel('Radius [pc]'); ax1.set_ylabel('Velocity [km/s]')
    ax1.set_title('Energy Release at Metric Boundary (Eq. 17, Section 5.6)', fontweight='bold')
    ax1.legend(); ax1.grid(True, alpha=0.3)
    
    ax2 = fig.add_subplot(gs[1, 0])
    delta_v = v_release - v_launch
    ax2.plot(r_range, delta_v, 'purple', linewidth=2.5)
    ax2.fill_between(r_range, 0, delta_v, alpha=0.3, color='purple')
    ax2.axhline(y=5, color='green', linestyle='--')
    ax2.set_xlabel('Radius [pc]'); ax2.set_ylabel('Δv_release [km/s]')
    ax2.set_title('Velocity Boost', fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    ax3 = fig.add_subplot(gs[1, 1])
    T_local = 150
    Delta_T = T_local * (1 - gamma)
    ax3.plot(r_range, Delta_T, 'orange', linewidth=2.5)
    ax3.fill_between(r_range, 0, Delta_T, alpha=0.3, color='orange')
    ax3.set_xlabel('Radius [pc]'); ax3.set_ylabel('ΔT_recouple [K]')
    ax3.set_title('Temperature Release (Eq. 18)', fontweight='bold')
    ax3.grid(True, alpha=0.3)
    
    out = Path(output_dir)/"g79_energy_release.png"
    plt.savefig(out, dpi=300, bbox_inches='tight')
    plt.close()
    return str(out)

def plot_multi_shell(output_dir):
    """Figure 7: Multi-shell structure"""
    r_range = np.linspace(0.1, 5.0, 500)
    
    fig, ax = plt.subplots(figsize=(12, 8))
    shells = [
        {'r': 1.2, 'T': 500, 'label': 'Inner shell', 'color': 'red'},
        {'r': 2.3, 'T': 200, 'label': 'Middle shell', 'color': 'orange'},
        {'r': 4.5, 'T': 60, 'label': 'Outer shell', 'color': 'blue'}
    ]
    ax.plot(r_range, gamma_seg_g79(r_range), 'b-', linewidth=3, label='γ_seg(r)')
    for shell in shells:
        r_sh, gamma_sh = shell['r'], gamma_seg_g79(shell['r'])
        ax.plot(r_sh, gamma_sh, 'o', color=shell['color'], markersize=15, 
               label=f"{shell['label']}: r={r_sh} pc, T={shell['T']} K")
        ax.axvline(x=r_sh, color=shell['color'], linestyle=':', alpha=0.5)
    ax.axhline(y=1, color='gray', linestyle='--', alpha=0.5)
    ax.set_xlabel('Radius [pc]'); ax.set_ylabel('γ_seg')
    ax.set_title('Three-Layer Structure of G79.29+0.46 (Section 5.1)', fontweight='bold')
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout()
    
    out = Path(output_dir)/"g79_multi_shell_structure.png"
    plt.savefig(out, dpi=300, bbox_inches='tight')
    plt.close()
    return str(out)

def plot_lbv_comparison(output_dir):
    """Figure 8: LBV Comparison"""
    r_range = np.linspace(0.1, 5.0, 500)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    nebulae = {
        'G79.29+0.46': {'alpha': 0.12, 'r_c': 1.9, 'color': 'blue'},
        'η Carinae': {'alpha': 0.15, 'r_c': 2.5, 'color': 'red'},
        'AG Carinae': {'alpha': 0.10, 'r_c': 3.0, 'color': 'green'}
    }
    for name, params in nebulae.items():
        gamma_neb = gamma_seg_g79(r_range, params['alpha'], params['r_c'])
        ax1.plot(r_range, gamma_neb, linewidth=2.5, color=params['color'], 
                label=f"{name} (α={params['alpha']}, r_c={params['r_c']} pc)")
    ax1.axhline(y=1, color='gray', linestyle='--', alpha=0.5)
    ax1.set_xlabel('Radius [pc]'); ax1.set_ylabel('γ_seg')
    ax1.set_title('γ_seg Profiles: LBV Comparison (Section 6.2)', fontweight='bold')
    ax1.legend(); ax1.grid(True, alpha=0.3)
    
    for name, params in nebulae.items():
        gamma_neb = gamma_seg_g79(r_range, params['alpha'], params['r_c'])
        ratio = 1/gamma_neb - 1
        ax2.plot(r_range, ratio, linewidth=2.5, color=params['color'], label=name)
    ax2.axhline(y=0.1, color='black', linestyle='--', linewidth=2, label='Universal ratio ~0.1 (Eq. 20)')
    ax2.set_xlabel('Radius [pc]'); ax2.set_ylabel('Δv/v₀ = γ_seg⁻¹ - 1')
    ax2.set_title('Universal Scaling Ratio', fontweight='bold')
    ax2.legend(); ax2.grid(True, alpha=0.3)
    plt.tight_layout()
    
    out = Path(output_dir)/"g79_nebulae_comparison.png"
    plt.savefig(out, dpi=300, bbox_inches='tight')
    plt.close()
    return str(out)

def plot_summary_dashboard(output_dir):
    """Figure 9: Summary Dashboard"""
    r_range = np.linspace(0.1, 5.0, 500)
    
    fig = plt.figure(figsize=(16, 12))
    gs = GridSpec(3, 3, hspace=0.35, wspace=0.35)
    
    # Panel 1: γ_seg
    ax1 = fig.add_subplot(gs[0, :])
    ax1.plot(r_range, gamma_seg_g79(r_range), 'b-', linewidth=3)
    ax1.set_title('γ_seg(r) Profile', fontweight='bold')
    ax1.set_ylabel('γ_seg'); ax1.grid(True, alpha=0.3)
    
    # Panel 2: Temperature
    ax2 = fig.add_subplot(gs[1, 0])
    ax2.plot(r_range, T_profile(r_range), 'r-', linewidth=2)
    ax2.set_title('Temperature'); ax2.set_ylabel('T [K]')
    ax2.grid(True, alpha=0.3)
    
    # Panel 3: Velocity
    ax3 = fig.add_subplot(gs[1, 1])
    ax3.plot(r_range, v_observed(r_range), 'g-', linewidth=2)
    ax3.set_title('Velocity'); ax3.set_ylabel('v [km/s]')
    ax3.grid(True, alpha=0.3)
    
    # Panel 4: Frequency
    ax4 = fig.add_subplot(gs[1, 2])
    nu_obs = 100 * gamma_seg_g79(r_range)
    ax4.plot(r_range, nu_obs, 'purple', linewidth=2)
    ax4.set_title('Radio Frequency'); ax4.set_ylabel('ν [GHz]')
    ax4.grid(True, alpha=0.3)
    
    # Panel 5: Mass (simplified)
    ax5 = fig.add_subplot(gs[2, 0])
    r_mass = np.linspace(0.5, 5, 100)
    gamma_vals = gamma_seg_g79(r_mass)
    M_proxy = np.cumsum((1-gamma_vals) * r_mass**2)
    M_norm = M_proxy / M_proxy[-1] * 8.7
    ax5.plot(r_mass, M_norm, 'orange', linewidth=2)
    ax5.set_title('Core Mass'); ax5.set_ylabel('M [M_☉]')
    ax5.set_xlabel('Radius [pc]'); ax5.grid(True, alpha=0.3)
    
    # Panel 6: Time dilation
    ax6 = fig.add_subplot(gs[2, 1])
    ax6.plot(r_range, (1-gamma_seg_g79(r_range))*100, 'brown', linewidth=2)
    ax6.set_title('Time Dilation'); ax6.set_ylabel('(1-γ) [%]')
    ax6.set_xlabel('Radius [pc]'); ax6.grid(True, alpha=0.3)
    
    # Panel 7: Δv
    ax7 = fig.add_subplot(gs[2, 2])
    delta_v = V0 * (1/gamma_seg_g79(r_range) - 1)
    ax7.plot(r_range, delta_v, 'cyan', linewidth=2)
    ax7.set_title('Velocity Excess'); ax7.set_ylabel('Δv [km/s]')
    ax7.set_xlabel('Radius [pc]'); ax7.grid(True, alpha=0.3)
    
    plt.suptitle('Segmented Spacetime - Complete Overview', fontsize=16, fontweight='bold', y=0.995)
    out = Path(output_dir)/"g79_summary_dashboard.png"
    plt.savefig(out, dpi=300, bbox_inches='tight')
    plt.close()
    return str(out)

def generate_all(output_dir):
    """Generate all G79 plots"""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    plots = []
    print("  [1/4] Energy release...")
    plots.append(plot_energy_release(output_dir))
    
    print("  [2/4] Multi-shell structure...")
    plots.append(plot_multi_shell(output_dir))
    
    print("  [3/4] LBV comparison...")
    plots.append(plot_lbv_comparison(output_dir))
    
    print("  [4/4] Summary dashboard...")
    plots.append(plot_summary_dashboard(output_dir))
    
    return plots
