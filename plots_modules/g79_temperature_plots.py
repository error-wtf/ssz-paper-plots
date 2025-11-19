#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
G79 Temperature Equation Plots - Standalone
===========================================
Complete test suite for temperature equations (from TEST_TEMPERATURE_EQUATIONS_COMPLETE.py)

© 2025 Carmen Wrede, Lino Casu, Bingsi
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

# Physical constants
ALPHA = 0.12
ALPHA_ERR = 0.03
R_C = 1.9  # pc
T_0 = 240.0  # K
T_LOCAL_INNER = 80.0  # K

# Observed shell temperatures
SHELL_R = np.array([1.2, 2.3, 4.5])  # pc
SHELL_T = np.array([500, 200, 60])  # K

def gamma_seg(r, alpha=ALPHA, r_c=R_C):
    """Temporal density function γ_seg(r) = 1 - α exp[-(r/r_c)²]"""
    return 1.0 - alpha * np.exp(-(r / r_c)**2)

def T_basic(r, T_0=T_0):
    """Basic temperature T(r) = T₀ γ_seg(r)"""
    return T_0 * gamma_seg(r)

def T_observed_g1(r, T_local=T_LOCAL_INNER):
    """Temperature observed from g^(1): T_obs = T_local / γ_seg"""
    return T_local / gamma_seg(r)

def T_local_g2(r, T_obs=T_0):
    """Local temperature in g^(2): T_local = T_obs × γ_seg"""
    return T_obs * gamma_seg(r)

def u_observed_g2(r, u_local=1.0):
    """Energy density in g^(2): u_obs^(2) = γ_seg⁴ × u_local"""
    return gamma_seg(r)**4 * u_local

def u_observed_g1(r, u_local=1.0):
    """Energy density in g^(1): u_obs^(1) = u_local / γ_seg⁴"""
    return u_local / gamma_seg(r)**4

def plot_gamma_seg(output_dir):
    """Plot 1: Temporal density function"""
    r_range = np.linspace(0.1, 5.0, 200)
    gamma_vals = gamma_seg(r_range)
    gamma_upper = gamma_seg(r_range, ALPHA + ALPHA_ERR, R_C)
    gamma_lower = gamma_seg(r_range, ALPHA - ALPHA_ERR, R_C)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(r_range, gamma_vals, 'b-', linewidth=3, label=r'$\gamma_{\mathrm{seg}}(r)$')
    ax.fill_between(r_range, gamma_lower, gamma_upper, alpha=0.25, color='blue',
                    label=r'$\pm 1\sigma$ uncertainty')
    ax.axhline(y=1, color='gray', linestyle='--', linewidth=2, alpha=0.5)
    ax.set_xlabel(r'Radius $r$ [pc]', fontweight='bold')
    ax.set_ylabel(r'Temporal density $\gamma_{\mathrm{seg}}$', fontweight='bold')
    ax.set_title('Eq. (10): Temporal Density Function', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.25, linestyle=':', linewidth=0.9)
    ax.legend(loc='lower right', framealpha=0.95)
    plt.tight_layout()
    
    out = Path(output_dir)/"temp_eq10_gamma_seg.png"
    plt.savefig(out, dpi=300, bbox_inches='tight')
    plt.close()
    return str(out)

def plot_T_basic(output_dir):
    """Plot 2: Basic temperature profile"""
    r_range = np.linspace(0.1, 5.0, 200)
    T_vals = T_basic(r_range)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(r_range, T_vals, 'r-', linewidth=3, label=r'$T(r) = T_0 \gamma_{\mathrm{seg}}(r)$')
    ax.plot(SHELL_R, SHELL_T, 'bs', markersize=11, markeredgecolor='darkblue',
            markeredgewidth=2, zorder=5, label='Observed shells')
    ax.errorbar(SHELL_R, SHELL_T, yerr=0.2*SHELL_T, fmt='none', ecolor='blue',
                elinewidth=2, capsize=5, capthick=2, alpha=0.7)
    ax.set_xlabel(r'Radius $r$ [pc]', fontweight='bold')
    ax.set_ylabel(r'Temperature $T$ [K]', fontweight='bold')
    ax.set_title('Eq. (9): Basic Temperature Profile', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.25, linestyle=':', linewidth=0.9)
    ax.legend(loc='upper right', framealpha=0.95)
    plt.tight_layout()
    
    out = Path(output_dir)/"temp_eq09_T_basic.png"
    plt.savefig(out, dpi=300, bbox_inches='tight')
    plt.close()
    return str(out)

def plot_dual_frame_temperature(output_dir):
    """Plot 3: Dual-frame temperature"""
    r_range = np.linspace(0.1, 5.0, 200)
    T_obs_from_g1 = T_observed_g1(r_range)
    T_loc_in_g2 = T_local_g2(r_range)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    ax1.plot(r_range, T_obs_from_g1, 'r-', linewidth=3,
             label=r'$T_{\mathrm{obs}} = T_{\mathrm{local}} / \gamma_{\mathrm{seg}}$')
    ax1.axhline(y=T_LOCAL_INNER, color='gray', linestyle='--', linewidth=2, alpha=0.5,
               label=f'T_local = {T_LOCAL_INNER} K')
    ax1.set_xlabel(r'Radius $r$ [pc]', fontweight='bold')
    ax1.set_ylabel(r'Observed Temperature $T_{\mathrm{obs}}$ [K]', fontweight='bold')
    ax1.set_title(r'From $g^{(1)}$ Frame: Apparent Heating', fontsize=13, fontweight='bold')
    ax1.grid(True, alpha=0.25, linestyle=':', linewidth=0.9)
    ax1.legend(loc='upper right', framealpha=0.95)
    
    ax2.plot(r_range, T_loc_in_g2, 'b-', linewidth=3,
             label=r'$T_{\mathrm{local}} = T_{\mathrm{obs}} \times \gamma_{\mathrm{seg}}$')
    ax2.axhline(y=T_0, color='gray', linestyle='--', linewidth=2, alpha=0.5,
               label=f'T_obs = {T_0} K')
    ax2.set_xlabel(r'Radius $r$ [pc]', fontweight='bold')
    ax2.set_ylabel(r'Local Temperature $T_{\mathrm{local}}$ [K]', fontweight='bold')
    ax2.set_title(r'In $g^{(2)}$ Domain: Effective Cooling', fontsize=13, fontweight='bold')
    ax2.grid(True, alpha=0.25, linestyle=':', linewidth=0.9)
    ax2.legend(loc='upper right', framealpha=0.95)
    
    plt.tight_layout()
    out = Path(output_dir)/"temp_eq15_dual_frame_temperature.png"
    plt.savefig(out, dpi=300, bbox_inches='tight')
    plt.close()
    return str(out)

def plot_energy_density(output_dir):
    """Plot 4: Energy density relations"""
    r_range = np.linspace(0.1, 5.0, 200)
    u_g2 = u_observed_g2(r_range)
    u_g1 = u_observed_g1(r_range)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    ax1.plot(r_range, u_g2, 'b-', linewidth=3,
             label=r'$u_{\mathrm{obs}}^{(2)} = \gamma_{\mathrm{seg}}^4 \times u_{\mathrm{local}}$')
    ax1.axhline(y=1.0, color='gray', linestyle='--', linewidth=2, alpha=0.5,
               label='u_local = 1')
    ax1.set_xlabel(r'Radius $r$ [pc]', fontweight='bold')
    ax1.set_ylabel(r'Energy Density $u^{(2)}$ [normalized]', fontweight='bold')
    ax1.set_title(r'In $g^{(2)}$ Domain: Energy Suppression', fontsize=13, fontweight='bold')
    ax1.grid(True, alpha=0.25, linestyle=':', linewidth=0.9)
    ax1.legend(loc='lower right', framealpha=0.95)
    
    ax2.plot(r_range, u_g1, 'r-', linewidth=3,
             label=r'$u_{\mathrm{obs}}^{(1)} = u_{\mathrm{local}} / \gamma_{\mathrm{seg}}^4$')
    ax2.axhline(y=1.0, color='gray', linestyle='--', linewidth=2, alpha=0.5,
               label='u_local = 1')
    ax2.set_xlabel(r'Radius $r$ [pc]', fontweight='bold')
    ax2.set_ylabel(r'Energy Density $u^{(1)}$ [normalized]', fontweight='bold')
    ax2.set_title(r'From $g^{(1)}$ Frame: Energy Enhancement', fontsize=13, fontweight='bold')
    ax2.grid(True, alpha=0.25, linestyle=':', linewidth=0.9)
    ax2.legend(loc='upper left', framealpha=0.95)
    
    plt.tight_layout()
    out = Path(output_dir)/"temp_eq16_energy_density.png"
    plt.savefig(out, dpi=300, bbox_inches='tight')
    plt.close()
    return str(out)

def plot_temperature_recouple(output_dir):
    """Plot 5: Temperature recouple"""
    r_range = np.linspace(0.1, 5.0, 200)
    Delta_T = T_LOCAL_INNER * (1 - gamma_seg(r_range))
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(r_range, Delta_T, 'orange', linewidth=3,
            label=r'$\Delta T_{\mathrm{recouple}} = T_{\mathrm{local}}(1 - \gamma_{\mathrm{seg}})$')
    ax.fill_between(r_range, 0, Delta_T, alpha=0.3, color='orange')
    ax.set_xlabel(r'Radius $r$ [pc]', fontweight='bold')
    ax.set_ylabel(r'$\Delta T_{\mathrm{recouple}}$ [K]', fontweight='bold')
    ax.set_title('Eq. (18): Temperature Released at Recoupling', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.25, linestyle=':', linewidth=0.9)
    ax.legend(loc='upper right', framealpha=0.95)
    plt.tight_layout()
    
    out = Path(output_dir)/"temp_eq18_temperature_recouple.png"
    plt.savefig(out, dpi=300, bbox_inches='tight')
    plt.close()
    return str(out)

def generate_all(output_dir):
    """Generate all temperature plots"""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    plots = []
    print("  [1/5] Temporal density...")
    plots.append(plot_gamma_seg(output_dir))
    
    print("  [2/5] Basic temperature...")
    plots.append(plot_T_basic(output_dir))
    
    print("  [3/5] Dual-frame temperature...")
    plots.append(plot_dual_frame_temperature(output_dir))
    
    print("  [4/5] Energy density...")
    plots.append(plot_energy_density(output_dir))
    
    print("  [5/5] Temperature recouple...")
    plots.append(plot_temperature_recouple(output_dir))
    
    return plots
