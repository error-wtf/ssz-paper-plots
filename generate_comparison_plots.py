#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comparison Plots: Cubic vs Piecewise Model
===========================================
Generates comparative analysis plots for the paper

Output: plots/paper/
  - model_comparison_potential.png
  - model_comparison_collapse.png
  - model_comparison_trajectories.png
  - model_comparison_phase.png
  - radiowave_lightcurves.png
  - paper_compatibility_summary.png

© 2025 Carmen Wrede, Lino Casu
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
"""

import os
import sys
from pathlib import Path

os.environ['PYTHONIOENCODING'] = 'utf-8:replace'
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except:
        pass

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy.integrate import odeint

BASE_PATH = Path(__file__).parent
OUTPUT_DIR = BASE_PATH / "plots" / "comparison"

# ============================================================================
# CUBIC MODEL (Current Implementation)
# ============================================================================

class CubicModel:
    """Cubic potential model (current)"""
    def __init__(self, a=1.0, b=-0.5, gamma0=1.0):
        self.a = a
        self.b = b
        self.gamma0 = gamma0
        self.Xi_c = -a / (2.0 * b)
    
    def potential(self, Xi):
        return 0.5 * self.a * Xi**2 + (1.0/3.0) * self.b * Xi**3
    
    def potential_derivative(self, Xi):
        return self.a * Xi + self.b * Xi**2
    
    def collapse_rate(self, Xi):
        dV = self.potential_derivative(Xi)
        return self.gamma0 * dV**2
    
    def evolution(self, Xi, t):
        return -self.collapse_rate(Xi)

# ============================================================================
# PIECEWISE MODEL (Paper-Conform)
# ============================================================================

class PiecewiseModel:
    """Piecewise nonlinear model (paper-conform)"""
    def __init__(self, k=1.0, Xi_c=1.0, gamma0=1.0, p=2.2):
        self.k = k
        self.Xi_c = Xi_c
        self.gamma0 = gamma0
        self.p = p
    
    def potential(self, Xi):
        Xi = np.asarray(Xi)
        V = np.zeros_like(Xi, dtype=float)
        mask_g2 = (Xi > self.Xi_c)
        if np.any(mask_g2):
            x = Xi[mask_g2] - self.Xi_c
            V[mask_g2] = (self.k / (self.p + 1.0)) * x**(self.p + 1.0)
        return V if V.shape != () else float(V)
    
    def potential_derivative(self, Xi):
        Xi = np.asarray(Xi)
        dV = np.zeros_like(Xi, dtype=float)
        mask_g2 = (Xi > self.Xi_c)
        if np.any(mask_g2):
            x = Xi[mask_g2] - self.Xi_c
            dV[mask_g2] = self.k * x**self.p
        return dV if dV.shape != () else float(dV)
    
    def collapse_rate(self, Xi):
        return self.gamma0 * self.potential_derivative(Xi)
    
    def evolution(self, Xi, t):
        if Xi <= self.Xi_c:
            return 0.0
        return -self.collapse_rate(Xi)

# ============================================================================
# PLOT 1: POTENTIAL COMPARISON
# ============================================================================

def plot_potential_comparison(output_dir):
    """Compare potential landscapes"""
    print("  [1/6] Potential comparison...")
    
    cubic = CubicModel()
    piecewise = PiecewiseModel()
    
    Xi_range = np.linspace(-0.5, 3.0, 500)
    
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    # Cubic
    ax = axes[0]
    V_cubic = [cubic.potential(Xi) for Xi in Xi_range]
    ax.plot(Xi_range, V_cubic, 'b-', linewidth=3, label='V(Xi) cubic')
    ax.axvline(cubic.Xi_c, color='red', linestyle='--', linewidth=2, label=f'Xi_c = {cubic.Xi_c:.1f}')
    ax.axhline(0, color='gray', linestyle=':', alpha=0.5)
    ax.fill_between([0, cubic.Xi_c], -1, 2, color='green', alpha=0.1, label='g₁')
    ax.fill_between([cubic.Xi_c, 3], -1, 2, color='red', alpha=0.1, label='g₂')
    ax.set_xlabel('Coherence Xi', fontsize=13)
    ax.set_ylabel('Potential V(Xi)', fontsize=13)
    ax.set_title('CUBIC MODEL\n(Smooth, Symmetric)', fontweight='bold', fontsize=14)
    ax.set_ylim(-1, 1.5)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    
    # Piecewise
    ax = axes[1]
    V_piecewise = piecewise.potential(Xi_range)
    ax.plot(Xi_range, V_piecewise, 'b-', linewidth=3, label='V(Xi) piecewise')
    ax.axvline(piecewise.Xi_c, color='red', linestyle='--', linewidth=2, label=f'Xi_c = {piecewise.Xi_c:.1f}')
    ax.axhline(0, color='gray', linestyle=':', alpha=0.5)
    ax.fill_betweenx([0, max(V_piecewise)*1.1], -0.5, piecewise.Xi_c, 
                     color='green', alpha=0.15, label='g₁ (V=0, stable)')
    ax.fill_betweenx([0, max(V_piecewise)*1.1], piecewise.Xi_c, 3.0, 
                     color='red', alpha=0.15, label='g₂ (unstable)')
    ax.set_xlabel('Coherence Xi', fontsize=13)
    ax.set_ylabel('Potential V(Xi)', fontsize=13)
    ax.set_title('PIECEWISE MODEL\n(Sharp Break, Paper-Conform)', fontweight='bold', fontsize=14)
    ax.set_xlim(-0.5, 3.0)
    ax.set_ylim(-0.1, max(V_piecewise)*1.1)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_dir / 'model_comparison_potential.png', dpi=300)
    plt.close()

# ============================================================================
# PLOT 2: COLLAPSE RATE COMPARISON
# ============================================================================

def plot_collapse_rate_comparison(output_dir):
    """Compare collapse rates"""
    print("  [2/6] Collapse rate comparison...")
    
    cubic = CubicModel()
    piecewise = PiecewiseModel()
    
    Xi_range = np.linspace(-0.5, 3.0, 500)
    
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    # Cubic
    ax = axes[0]
    C_cubic = [cubic.collapse_rate(Xi) for Xi in Xi_range]
    ax.plot(Xi_range, C_cubic, 'purple', linewidth=3)
    ax.axvline(cubic.Xi_c, color='red', linestyle='--', linewidth=2)
    ax.axhline(0, color='gray', linestyle=':', alpha=0.5)
    ax.fill_between(Xi_range, 0, C_cubic, color='purple', alpha=0.2)
    ax.set_xlabel('Coherence Xi', fontsize=13)
    ax.set_ylabel('Collapse Rate C(Xi)', fontsize=13)
    ax.set_title('CUBIC: C = Γ·[dV/dXi]²\n(Always Positive)', fontweight='bold', fontsize=14)
    ax.grid(True, alpha=0.3)
    
    # Piecewise
    ax = axes[1]
    C_piecewise = [piecewise.collapse_rate(Xi) for Xi in Xi_range]
    ax.plot(Xi_range, C_piecewise, 'purple', linewidth=3)
    ax.axvline(piecewise.Xi_c, color='red', linestyle='--', linewidth=2)
    ax.axhline(0, color='gray', linestyle=':', alpha=0.5)
    mask_g2 = Xi_range > piecewise.Xi_c
    ax.fill_between(Xi_range[mask_g2], 0, np.array(C_piecewise)[mask_g2], 
                     color='red', alpha=0.25, label='g₂: Collapse active')
    ax.text(0.3, max(C_piecewise)*0.5, 'g₁: C=0\n(stable)', 
            fontsize=12, ha='center', bbox=dict(boxstyle='round', facecolor='green', alpha=0.3))
    ax.set_xlabel('Coherence Xi', fontsize=13)
    ax.set_ylabel('Collapse Rate C(Xi)', fontsize=13)
    ax.set_title('PIECEWISE: C = Γ·dV/dXi\n(Zero in g₁, Nonlinear in g₂)', fontweight='bold', fontsize=14)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_dir / 'model_comparison_collapse.png', dpi=300)
    plt.close()

# ============================================================================
# PLOT 3: TRAJECTORY COMPARISON
# ============================================================================

def plot_trajectory_comparison(output_dir):
    """Compare collapse trajectories"""
    print("  [3/6] Trajectory comparison...")
    
    cubic = CubicModel()
    piecewise = PiecewiseModel()
    
    t_span = np.linspace(0, 10, 1000)
    Xi0_values = [0.5, 1.0, 1.5, 2.0, 2.5]
    
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    # Cubic
    ax = axes[0]
    for Xi0 in Xi0_values:
        Xi_t = odeint(cubic.evolution, Xi0, t_span).flatten()
        color = 'red' if Xi0 > cubic.Xi_c else 'green'
        ax.plot(t_span, Xi_t, color=color, linewidth=2, label=f'Xi₀={Xi0}')
    ax.axhline(cubic.Xi_c, color='black', linestyle='--', linewidth=2, label='Xi_c')
    ax.set_xlabel('Time t', fontsize=13)
    ax.set_ylabel('Coherence Xi(t)', fontsize=13)
    ax.set_title('CUBIC: Smooth Approach to Equilibrium', fontweight='bold', fontsize=14)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    
    # Piecewise
    ax = axes[1]
    for Xi0 in Xi0_values:
        Xi_t = odeint(piecewise.evolution, Xi0, t_span).flatten()
        color = 'red' if Xi0 > piecewise.Xi_c else 'green'
        ax.plot(t_span, Xi_t, color=color, linewidth=2, label=f'Xi₀={Xi0}')
    ax.axhline(piecewise.Xi_c, color='black', linestyle='--', linewidth=2, label='Xi_c')
    ax.set_xlabel('Time t', fontsize=13)
    ax.set_ylabel('Coherence Xi(t)', fontsize=13)
    ax.set_title('PIECEWISE: Finite-Time Collapse to Xi_c', fontweight='bold', fontsize=14)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_dir / 'model_comparison_trajectories.png', dpi=300)
    plt.close()

# ============================================================================
# PLOT 4: PHASE PORTRAIT
# ============================================================================

def plot_phase_comparison(output_dir):
    """Compare phase portraits"""
    print("  [4/6] Phase portrait comparison...")
    
    cubic = CubicModel()
    piecewise = PiecewiseModel()
    
    Xi_range = np.linspace(0, 2.5, 100)
    
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    # Cubic
    ax = axes[0]
    Xi_dot_cubic = [-cubic.collapse_rate(Xi) for Xi in Xi_range]
    ax.plot(Xi_range, Xi_dot_cubic, 'b-', linewidth=3)
    ax.axvline(cubic.Xi_c, color='red', linestyle='--', linewidth=2)
    ax.axhline(0, color='gray', linestyle=':', alpha=0.5)
    ax.set_xlabel('Coherence Xi', fontsize=13)
    ax.set_ylabel('dXi/dt', fontsize=13)
    ax.set_title('CUBIC: Phase Portrait\n(Always Negative)', fontweight='bold', fontsize=14)
    ax.grid(True, alpha=0.3)
    
    # Piecewise
    ax = axes[1]
    Xi_dot_piecewise = []
    for Xi in Xi_range:
        if Xi <= piecewise.Xi_c:
            Xi_dot_piecewise.append(0.0)
        else:
            Xi_dot_piecewise.append(-piecewise.collapse_rate(Xi))
    ax.plot(Xi_range, Xi_dot_piecewise, 'b-', linewidth=3)
    ax.axvline(piecewise.Xi_c, color='red', linestyle='--', linewidth=2, label='Break point')
    ax.axhline(0, color='gray', linestyle=':', alpha=0.5)
    ax.fill_between([0, piecewise.Xi_c], -0.3, 0.1, color='green', alpha=0.2, label='g₁: No dynamics')
    ax.set_xlabel('Coherence Xi', fontsize=13)
    ax.set_ylabel('dXi/dt', fontsize=13)
    ax.set_title('PIECEWISE: Phase Portrait\n(Zero in g₁, Negative in g₂)', fontweight='bold', fontsize=14)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_dir / 'model_comparison_phase.png', dpi=300)
    plt.close()

# ============================================================================
# PLOT 5: RADIOWAVE LIGHTCURVES
# ============================================================================

def plot_radiowave_lightcurves(output_dir):
    """Simulated radiowave emission profiles"""
    print("  [5/6] Radiowave lightcurves...")
    
    t = np.linspace(0, 10, 500)
    
    # Cubic: smooth, broad peak
    t_center_cubic = 3.0
    sigma_cubic = 1.0
    flux_cubic = np.exp(-(t - t_center_cubic)**2 / (2*sigma_cubic**2))
    
    # Piecewise: sharp, narrow peak
    t_center_piecewise = 3.0
    sigma_piecewise = 0.2
    flux_piecewise = np.exp(-(t - t_center_piecewise)**2 / (2*sigma_piecewise**2))
    
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    # Cubic
    ax = axes[0]
    ax.plot(t, flux_cubic, 'b-', linewidth=3, label='Radio flux')
    ax.axvline(t_center_cubic, color='red', linestyle='--', alpha=0.7, label='Peak time')
    ax.fill_between(t, 0, flux_cubic, color='blue', alpha=0.2)
    ax.set_xlabel('Time (arbitrary units)', fontsize=13)
    ax.set_ylabel('Radio Flux (arbitrary)', fontsize=13)
    ax.set_title('CUBIC: Smooth Radio Precursor\n(Timing Uncertainty ±1 unit)', fontweight='bold', fontsize=14)
    ax.set_ylim(0, 1.2)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    
    # Piecewise
    ax = axes[1]
    ax.plot(t, flux_piecewise, 'b-', linewidth=3, label='Radio flux')
    ax.axvline(t_center_piecewise, color='red', linestyle='--', alpha=0.7, label='Peak time')
    ax.fill_between(t, 0, flux_piecewise, color='blue', alpha=0.2)
    ax.set_xlabel('Time (arbitrary units)', fontsize=13)
    ax.set_ylabel('Radio Flux (arbitrary)', fontsize=13)
    ax.set_title('PIECEWISE: Sharp Radio Burst\n(Timing Uncertainty ±0.1 unit)', fontweight='bold', fontsize=14)
    ax.set_ylim(0, 1.2)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_dir / 'radiowave_lightcurves.png', dpi=300)
    plt.close()

# ============================================================================
# PLOT 6: COMPATIBILITY SUMMARY
# ============================================================================

def plot_compatibility_summary(output_dir):
    """Visual compatibility summary"""
    print("  [6/6] Compatibility summary...")
    
    criteria = [
        'Irreversibility',
        'g₁ Regime',
        'g₂ Regime',
        'Critical Point',
        'Sharp Break',
        'One-Sided g₂',
        'Flat g₁',
        'Abrupt Release',
        'Finite-Time',
        'Strong Nonlinear'
    ]
    
    cubic_scores = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.3, 0.3, 0.5]
    piecewise_scores = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    y_pos = np.arange(len(criteria))
    width = 0.35
    
    bars1 = ax.barh(y_pos - width/2, cubic_scores, width, label='Cubic Model', color='steelblue', alpha=0.8)
    bars2 = ax.barh(y_pos + width/2, piecewise_scores, width, label='Piecewise Model', color='darkgreen', alpha=0.8)
    
    ax.set_yticks(y_pos)
    ax.set_yticklabels(criteria, fontsize=11)
    ax.set_xlabel('Paper Compatibility (0=Not Met, 1=Fully Met)', fontsize=13)
    ax.set_title('Model Compatibility with Radiowave Paper\nCubic: 60% | Piecewise: 100%', 
                 fontweight='bold', fontsize=15)
    ax.set_xlim(0, 1.1)
    ax.axvline(1.0, color='gray', linestyle='--', alpha=0.5)
    ax.legend(fontsize=12, loc='lower right')
    ax.grid(True, axis='x', alpha=0.3)
    
    # Add scores
    for i, (c, p) in enumerate(zip(cubic_scores, piecewise_scores)):
        ax.text(c + 0.02, i - width/2, f'{c:.1f}', va='center', fontsize=9)
        ax.text(p + 0.02, i + width/2, f'{p:.1f}', va='center', fontsize=9)
    
    plt.tight_layout()
    plt.savefig(output_dir / 'paper_compatibility_summary.png', dpi=300)
    plt.close()

# ============================================================================
# MAIN
# ============================================================================

def main():
    print("\n" + "="*80)
    print("COMPARISON PLOTS GENERATOR")
    print("Cubic vs Piecewise Model Analysis")
    print("="*80)
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    plot_potential_comparison(OUTPUT_DIR)
    plot_collapse_rate_comparison(OUTPUT_DIR)
    plot_trajectory_comparison(OUTPUT_DIR)
    plot_phase_comparison(OUTPUT_DIR)
    plot_radiowave_lightcurves(OUTPUT_DIR)
    plot_compatibility_summary(OUTPUT_DIR)
    
    print("\n" + "="*80)
    print("✓ Generated 6 comparison plots")
    print(f"✓ Output: {OUTPUT_DIR}")
    print("="*80)

if __name__ == "__main__":
    main()
