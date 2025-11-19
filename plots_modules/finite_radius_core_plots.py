#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Finite Radius Core Plots
=========================
Critical plots showing r > 0 core (NO r=0 singularity)

Paper concept: Birkhoff theorem requires finite-radius interior.
SSZ predicts r_core > 0 always, preventing mathematical singularity.

© 2025 Carmen Wrede, Lino Casu, Bingsi
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from ssz_core_functions import *

def plot_core_radius_vs_mass(output_dir='plots/missing'):
    """
    Core radius vs mass relation showing r_core > 0 ALWAYS
    
    Key concept: SSZ prevents r→0 collapse
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Mass range: solar mass to supermassive BH
    M_solar = np.logspace(0, 10, 100)  # M☉
    
    # SSZ: Finite radius core
    # r_core ≈ r_s * (1 + Xi_max) where Xi_max saturates
    r_s = 2.95 * M_solar  # Schwarzschild radius in km
    Xi_max = 1.0  # Segmentation saturation
    r_core_ssz = r_s * (1 + Xi_max)  # Always > r_s
    
    # GR: Approaches r=0 (singularity)
    r_core_gr = np.zeros_like(M_solar)  # Point mass
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Left: Linear scale showing SSZ > 0
    ax1.loglog(M_solar, r_core_ssz, 'b-', linewidth=2.5, label='SSZ: $r_{core} = r_s(1+\\Xi_{max})$')
    ax1.loglog(M_solar, r_s, 'k--', linewidth=1.5, label='$r_s$ (Schwarzschild)', alpha=0.6)
    ax1.axhline(0, color='r', linestyle=':', linewidth=2, label='GR: $r=0$ (singularity)', alpha=0.7)
    
    ax1.fill_between(M_solar, r_s, r_core_ssz, alpha=0.2, color='blue', label='SSZ interior')
    ax1.fill_between(M_solar, 0, r_s, alpha=0.1, color='red', label='GR singularity region')
    
    ax1.set_xlabel('Mass ($M_\\odot$)', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Core Radius (km)', fontsize=12, fontweight='bold')
    ax1.set_title('SSZ: Finite Core prevents $r=0$ Singularity', fontsize=13, fontweight='bold')
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    
    # Right: Ratio showing SSZ always > GR
    ratio = r_core_ssz / r_s
    ax2.semilogx(M_solar, ratio, 'g-', linewidth=2.5)
    ax2.axhline(1, color='k', linestyle='--', linewidth=1.5, alpha=0.6, label='$r_s$ threshold')
    ax2.axhline(2, color='b', linestyle=':', linewidth=1.5, alpha=0.6, label='SSZ prediction')
    ax2.fill_between(M_solar, 1, ratio, alpha=0.2, color='green')
    
    ax2.set_xlabel('Mass ($M_\\odot$)', fontsize=12, fontweight='bold')
    ax2.set_ylabel('$r_{core} / r_s$', fontsize=12, fontweight='bold')
    ax2.set_title('SSZ Core Radius Ratio (always > 1)', fontsize=13, fontweight='bold')
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    output_file = output_dir / '1_core_radius_vs_mass_NO_SINGULARITY.png'
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"  ✓ Generated: {output_file.name}")
    return [str(output_file)]

def plot_interior_geometry(output_dir='plots/missing'):
    """
    Interior geometry showing NO r=0 singularity
    
    Radial profile: density, curvature finite at core
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Radius array (normalized to r_s)
    r_over_rs = np.linspace(0.1, 5, 500)
    
    # SSZ density (finite at core)
    # ρ(r) ~ 1/(1 + (r/r_core)²)  - finite at r→0
    r_core = 2.0  # In units of r_s
    rho_ssz = 1.0 / (1 + (r_over_rs / r_core)**2)
    
    # GR density (diverges at r→0)
    # ρ_GR ~ 1/r² - SINGULAR
    rho_gr = np.zeros_like(r_over_rs)
    mask = r_over_rs > 0.5  # Only valid outside horizon
    rho_gr[mask] = 1.0 / r_over_rs[mask]**2
    
    # SSZ curvature (finite)
    # R ~ ρ (finite)
    R_ssz = rho_ssz
    
    # GR curvature (diverges)
    R_gr = np.zeros_like(r_over_rs)
    R_gr[mask] = 1.0 / r_over_rs[mask]**3
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Density
    ax1.semilogy(r_over_rs, rho_ssz, 'b-', linewidth=2.5, label='SSZ (finite core)')
    ax1.semilogy(r_over_rs[mask], rho_gr[mask], 'r--', linewidth=2.5, label='GR (singular)', alpha=0.7)
    ax1.axvline(r_core, color='b', linestyle=':', alpha=0.5, label=f'$r_{{core}} = {r_core}r_s$')
    ax1.axvline(1, color='k', linestyle='--', alpha=0.5, label='$r_s$')
    
    ax1.fill_between(r_over_rs, 1e-3, rho_ssz, alpha=0.2, color='blue')
    
    ax1.set_xlabel('$r / r_s$', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Density $\\rho$ (arbitrary units)', fontsize=12, fontweight='bold')
    ax1.set_title('SSZ: Finite Density at Core (no divergence)', fontsize=13, fontweight='bold')
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim(1e-3, 1e2)
    
    # Curvature
    ax2.semilogy(r_over_rs, R_ssz, 'b-', linewidth=2.5, label='SSZ (finite)')
    ax2.semilogy(r_over_rs[mask], R_gr[mask], 'r--', linewidth=2.5, label='GR (singular)', alpha=0.7)
    ax2.axvline(r_core, color='b', linestyle=':', alpha=0.5, label=f'$r_{{core}}$')
    ax2.axvline(1, color='k', linestyle='--', alpha=0.5, label='$r_s$')
    
    ax2.fill_between(r_over_rs, 1e-3, R_ssz, alpha=0.2, color='blue')
    
    ax2.set_xlabel('$r / r_s$', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Curvature $R$ (arbitrary units)', fontsize=12, fontweight='bold')
    ax2.set_title('SSZ: Finite Curvature (no singularity)', fontsize=13, fontweight='bold')
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    ax2.set_ylim(1e-3, 1e3)
    
    plt.tight_layout()
    
    output_file = output_dir / '2_interior_geometry_FINITE_CURVATURE.png'
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"  ✓ Generated: {output_file.name}")
    return [str(output_file)]

def plot_ssz_vs_gr_core_comparison(output_dir='plots/missing'):
    """
    Direct comparison: SSZ (r>0) vs GR (r→0)
    
    Shows fundamental difference in interior structure
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    
    # Radial coordinates
    r_max = 5
    
    # SSZ: Finite core
    r_core = 2.0
    theta = np.linspace(0, 2*np.pi, 100)
    
    # Draw SSZ core (filled circle)
    x_core = r_core * np.cos(theta)
    y_core = r_core * np.sin(theta)
    ax.fill(x_core, y_core, color='blue', alpha=0.3, label='SSZ: Finite core ($r_{core} > 0$)')
    ax.plot(x_core, y_core, 'b-', linewidth=3)
    
    # Draw horizon
    x_horizon = 1.0 * np.cos(theta)
    y_horizon = 1.0 * np.sin(theta)
    ax.plot(x_horizon, y_horizon, 'k--', linewidth=2, label='Event horizon ($r_s$)')
    
    # GR: Point at r=0
    ax.plot(0, 0, 'rx', markersize=20, markeredgewidth=4, label='GR: Singularity at $r=0$')
    
    # g₁-g₂ boundary
    r_boundary = 3.0
    x_boundary = r_boundary * np.cos(theta)
    y_boundary = r_boundary * np.sin(theta)
    ax.plot(x_boundary, y_boundary, 'g:', linewidth=2.5, label='$g_1$-$g_2$ boundary')
    
    # Annotations
    ax.text(0, r_core + 0.3, '$r_{core} = 2r_s$', fontsize=12, ha='center', fontweight='bold', color='blue')
    ax.text(0, 1.3, '$r_s$', fontsize=11, ha='center', fontweight='bold')
    ax.text(0, r_boundary + 0.3, '$g_1 \\leftrightarrow g_2$', fontsize=11, ha='center', fontweight='bold', color='green')
    
    # Regions
    ax.text(0, -4.2, 'SSZ: No singularity\n$r_{min} = r_{core} > 0$', 
            fontsize=13, ha='center', fontweight='bold', color='blue',
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))
    
    ax.text(0, 4.2, 'GR: Point singularity\n$r \\to 0$ (unphysical)', 
            fontsize=13, ha='center', fontweight='bold', color='red',
            bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.8))
    
    ax.set_xlim(-r_max, r_max)
    ax.set_ylim(-r_max, r_max)
    ax.set_aspect('equal')
    ax.set_xlabel('$x / r_s$', fontsize=12, fontweight='bold')
    ax.set_ylabel('$y / r_s$', fontsize=12, fontweight='bold')
    ax.set_title('SSZ vs GR Interior: Finite Core prevents Singularity', fontsize=14, fontweight='bold')
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    output_file = output_dir / '3_SSZ_vs_GR_CORE_COMPARISON.png'
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"  ✓ Generated: {output_file.name}")
    return [str(output_file)]

def generate_all(output_dir='plots/missing'):
    """Generate all finite radius core plots"""
    print("\n[FINITE RADIUS CORE PLOTS]")
    print("-" * 60)
    
    all_plots = []
    all_plots.extend(plot_core_radius_vs_mass(output_dir))
    all_plots.extend(plot_interior_geometry(output_dir))
    all_plots.extend(plot_ssz_vs_gr_core_comparison(output_dir))
    
    print(f"  ✓ Generated {len(all_plots)} plots")
    return all_plots

if __name__ == "__main__":
    plots = generate_all()
    print(f"\nTotal: {len(plots)} plots")
