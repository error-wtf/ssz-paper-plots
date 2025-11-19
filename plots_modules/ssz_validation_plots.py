#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SSZ Validation Plots - Standalone
==================================
PPN, Shadow, QNM, Energy Conditions, Proper Time Tests

© 2025 Carmen Wrede, Lino Casu, Bingsi
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from ssz_core_functions import *

# ============================================================================
# PPN PLOTS
# ============================================================================

def plot_ppn_parameters(output_dir):
    """PPN β and γ parameters"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # β parameter
    ax1.bar(['GR', 'SSZ'], [1.0, ppn_beta()], color=['#2E86AB', '#A23B72'], alpha=0.8)
    ax1.axhline(1, color='red', ls='--', lw=2, label='β=1 (GR)')
    ax1.set_ylabel('β', fontsize=14)
    ax1.set_title('PPN β Parameter', fontsize=16, fontweight='bold')
    ax1.set_ylim(0.95, 1.05)
    ax1.grid(alpha=0.3)
    ax1.legend()
    
    # γ parameter
    ax2.bar(['GR', 'SSZ'], [1.0, ppn_gamma()], color=['#2E86AB', '#A23B72'], alpha=0.8)
    ax2.axhline(1, color='red', ls='--', lw=2, label='γ=1 (GR)')
    ax2.set_ylabel('γ', fontsize=14)
    ax2.set_title('PPN γ Parameter', fontsize=16, fontweight='bold')
    ax2.set_ylim(0.95, 1.05)
    ax2.grid(alpha=0.3)
    ax2.legend()
    
    plt.tight_layout()
    out = Path(output_dir)/"ppn_combined.png"
    plt.savefig(out, dpi=300, bbox_inches='tight')
    plt.close()
    
    return [str(out)]

# ============================================================================
# SHADOW PLOTS
# ============================================================================

def plot_shadow_vs_mass(output_dir):
    """Shadow radius vs mass"""
    M_arr = mass_range(1, 1e9, 50, log=True)
    b_GR = [shadow_radius_gr(M) / r_schwarzschild(M) for M in M_arr]
    b_SSZ = [shadow_radius_ssz(M) / r_schwarzschild(M) for M in M_arr]
    
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.semilogx(M_arr/M_SUN, b_GR, 'b-', lw=3, label='GR', alpha=0.7)
    ax.semilogx(M_arr/M_SUN, b_SSZ, 'r--', lw=3, label='SSZ', alpha=0.7)
    ax.set_xlabel('Mass (M☉)', fontsize=14)
    ax.set_ylabel('b/r_s', fontsize=14)
    ax.set_title('Shadow Radius vs Mass', fontsize=16, fontweight='bold')
    ax.legend(fontsize=12)
    ax.grid(alpha=0.3)
    plt.tight_layout()
    
    out = Path(output_dir)/"shadow_vs_mass.png"
    plt.savefig(out, dpi=300, bbox_inches='tight')
    plt.close()
    
    return str(out)

def plot_shadow_individual_masses(output_dir):
    """Shadow plots for different masses"""
    masses = [1, 10, 100, 1000, 1e4, 1e6, 4.3e6, 1e8, 1e9]
    plots = []
    
    for i, M_factor in enumerate(masses, 1):
        M = M_factor * M_SUN
        r_s = r_schwarzschild(M)
        r = radius_range(1.1, 10, M, 200)
        
        A_gr = [A_GR(ri, M) for ri in r]
        A_ssz = [A_SSZ(ri, M) for ri in r]
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(r/r_s, A_gr, 'b-', lw=2, label='GR', alpha=0.7)
        ax.plot(r/r_s, A_ssz, 'r--', lw=2, label='SSZ', alpha=0.7)
        ax.set_xlabel('r/r_s', fontsize=12)
        ax.set_ylabel('A(r)', fontsize=12)
        ax.set_title(f'Metric Function: M={M_factor:.1e}M☉', fontsize=14, fontweight='bold')
        ax.legend()
        ax.grid(alpha=0.3)
        plt.tight_layout()
        
        out = Path(output_dir)/f"shadow_{i+1}.png"
        plt.savefig(out, dpi=300, bbox_inches='tight')
        plt.close()
        plots.append(str(out))
    
    return plots

# ============================================================================
# QNM PLOTS
# ============================================================================

def plot_qnm_frequencies(output_dir):
    """QNM frequencies vs mass"""
    M_arr = mass_range(1, 1e9, 50, log=True)
    omega_GR = [qnm_frequency_gr(M) for M in M_arr]
    omega_SSZ = [qnm_frequency_ssz(M) for M in M_arr]
    
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.loglog(M_arr/M_SUN, omega_GR, 'b-', lw=3, label='GR', alpha=0.7)
    ax.loglog(M_arr/M_SUN, omega_SSZ, 'r--', lw=3, label='SSZ', alpha=0.7)
    ax.set_xlabel('Mass (M☉)', fontsize=14)
    ax.set_ylabel('ω_R (Hz)', fontsize=14)
    ax.set_title('QNM Frequencies', fontsize=16, fontweight='bold')
    ax.legend(fontsize=12)
    ax.grid(alpha=0.3, which='both')
    plt.tight_layout()
    
    out = Path(output_dir)/"qnm_frequency.png"
    plt.savefig(out, dpi=300, bbox_inches='tight')
    plt.close()
    
    return str(out)

def plot_qnm_modes(output_dir):
    """QNM for different l-modes"""
    M_arr = mass_range(1, 1e9, 50, log=True)
    plots = []
    
    for l in [2, 3, 4]:
        omega_GR = [qnm_frequency_gr(M) * (l + 0.5) for M in M_arr]
        omega_SSZ = [qnm_frequency_ssz(M) * (l + 0.5) for M in M_arr]
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.loglog(M_arr/M_SUN, omega_GR, 'b-', lw=2, label=f'GR(l={l})', alpha=0.7)
        ax.loglog(M_arr/M_SUN, omega_SSZ, 'r--', lw=2, label=f'SSZ(l={l})', alpha=0.7)
        ax.set_xlabel('Mass (M☉)', fontsize=12)
        ax.set_ylabel(f'ω_{{l={l}}} (Hz)', fontsize=12)
        ax.set_title(f'QNM l={l} Mode', fontsize=14, fontweight='bold')
        ax.legend()
        ax.grid(alpha=0.3, which='both')
        plt.tight_layout()
        
        out = Path(output_dir)/f"qnm_{l}.png"
        plt.savefig(out, dpi=300, bbox_inches='tight')
        plt.close()
        plots.append(str(out))
    
    return plots

# ============================================================================
# PROPER TIME PLOTS
# ============================================================================

def plot_proper_time_main(output_dir):
    """Main proper time plot"""
    M = 4.3e6 * M_SUN
    r = radius_range(1.01, 20, M, 500)
    
    tau_GR = [np.sqrt(abs(A_GR(ri, M))) for ri in r]
    tau_SSZ = [proper_time_factor(ri, M) for ri in r]
    
    r_s = r_schwarzschild(M)
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.plot(r/r_s, tau_GR, 'b-', lw=3, label='GR', alpha=0.7)
    ax.plot(r/r_s, tau_SSZ, 'r--', lw=3, label='SSZ', alpha=0.7)
    ax.set_xlabel('r/r_s', fontsize=14)
    ax.set_ylabel('dτ/dt', fontsize=14)
    ax.set_title('Proper Time: SSZ Finite at r→0', fontsize=16, fontweight='bold')
    ax.legend(fontsize=12)
    ax.grid(alpha=0.3)
    plt.tight_layout()
    
    out = Path(output_dir)/"proper_time.png"
    plt.savefig(out, dpi=300, bbox_inches='tight')
    plt.close()
    
    return str(out)

def plot_proper_time_masses(output_dir):
    """Proper time for different masses"""
    masses = [1, 10, 100, 1000, 1e6, 1e9]
    plots = []
    
    for i, M_factor in enumerate(masses, 1):
        M = M_factor * M_SUN
        r = radius_range(1.01, 10, M, 200)
        r_s = r_schwarzschild(M)
        
        tau_gr = [np.sqrt(abs(A_GR(ri, M))) for ri in r]
        tau_ssz = [proper_time_factor(ri, M) for ri in r]
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(r/r_s, tau_gr, 'b-', lw=2, label='GR', alpha=0.7)
        ax.plot(r/r_s, tau_ssz, 'r--', lw=2, label='SSZ', alpha=0.7)
        ax.set_xlabel('r/r_s', fontsize=12)
        ax.set_ylabel('dτ/dt', fontsize=12)
        ax.set_title(f'Proper Time: M={M_factor:.1e}M☉', fontsize=14, fontweight='bold')
        ax.legend()
        ax.grid(alpha=0.3)
        plt.tight_layout()
        
        out = Path(output_dir)/f"proper_time_{i+1}.png"
        plt.savefig(out, dpi=300, bbox_inches='tight')
        plt.close()
        plots.append(str(out))
    
    return plots

# ============================================================================
# ENERGY CONDITION PLOTS
# ============================================================================

def plot_energy_conditions(output_dir):
    """Energy conditions for different radii"""
    M = 4.3e6 * M_SUN
    r_s = r_schwarzschild(M)
    radii_rs = [1.2, 1.5, 2, 3, 5, 10, 20, 50, 100]
    
    plots = []
    for i, r_factor in enumerate(radii_rs, 1):
        r = r_factor * r_s
        rho, pr, pt = rho_pr_pt(r, M)
        wec, dec, sec = check_energy_conditions(r, M)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        conditions = ['WEC', 'DEC', 'SEC']
        values = [wec, dec, sec]
        colors = ['green' if v else 'red' for v in values]
        
        ax.bar(conditions, [1 if v else 0 for v in values], color=colors, alpha=0.7)
        ax.set_ylim(0, 1.2)
        ax.set_ylabel('Pass (1) / Fail (0)')
        ax.set_title(f'Energy Conditions at r={r_factor:.1f}r_s', fontsize=14, fontweight='bold')
        ax.grid(alpha=0.3)
        
        # Add text
        text = f"ρ = {rho:.2e}\np_r = {pr:.2e}\np_t = {pt:.2e}"
        ax.text(0.7, 0.5, text, transform=ax.transAxes, fontsize=10,
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        plt.tight_layout()
        out = Path(output_dir)/f"energy_{i}.png"
        plt.savefig(out, dpi=300, bbox_inches='tight')
        plt.close()
        plots.append(str(out))
    
    return plots

# ============================================================================
# MASTER FUNCTION
# ============================================================================

def generate_all(output_dir):
    """Generate all validation plots"""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    all_plots = []
    
    print("  [1/6] PPN parameters...")
    all_plots.extend(plot_ppn_parameters(output_dir))
    
    print("  [2/6] Shadow predictions...")
    all_plots.append(plot_shadow_vs_mass(output_dir))
    all_plots.extend(plot_shadow_individual_masses(output_dir))
    
    print("  [3/6] QNM frequencies...")
    all_plots.append(plot_qnm_frequencies(output_dir))
    all_plots.extend(plot_qnm_modes(output_dir))
    
    print("  [4/6] Proper time...")
    all_plots.append(plot_proper_time_main(output_dir))
    all_plots.extend(plot_proper_time_masses(output_dir))
    
    print("  [5/6] Energy conditions...")
    all_plots.extend(plot_energy_conditions(output_dir))
    
    print("  [6/6] Additional tests...")
    # Placeholder for more tests
    
    return all_plots
