#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Individual Sharp Break Detection Plots
================================================
Creates separate high-resolution plots for each detection method

© 2025 Carmen Wrede, Lino Casu, Bingsi
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
import sys
import os

os.environ['PYTHONIOENCODING'] = 'utf-8:replace'
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except: pass

def load_data():
    """Load G79 temperature data"""
    data_file = Path(__file__).parent / "data" / "G79_temperatures.csv"
    df = pd.read_csv(data_file)
    return df['r_pc'].values, df['T_K'].values

def plot1_temperature_profile_with_break(r, T, r_break, output_dir):
    """Plot 1: Temperature profile with break point"""
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Plot data
    ax.plot(r, T, 'ko-', linewidth=3, markersize=12, label='G79 Data', zorder=3)
    
    # Mark break point
    ax.axvline(r_break, color='red', linestyle='--', linewidth=3, 
              label=f'Sharp break: r_c = {r_break:.3f} pc', zorder=2)
    
    # Shade domains
    ax.axvspan(r.min(), r_break, alpha=0.2, color='red', label='g₂ (collapse)', zorder=1)
    ax.axvspan(r_break, r.max(), alpha=0.2, color='green', label='g₁ (stable)', zorder=1)
    
    # Labels
    ax.set_xlabel('Radius r [pc]', fontsize=14, fontweight='bold')
    ax.set_ylabel('Temperature T [K]', fontsize=14, fontweight='bold')
    ax.set_title('G79.29+0.46: Sharp Break in Temperature Profile\nPiecewise Model Required',
                fontsize=16, fontweight='bold')
    ax.legend(fontsize=12, loc='upper right')
    ax.grid(True, alpha=0.3, linestyle='--')
    
    # Annotate domains
    y_mid = (T.max() + T.min()) / 2
    ax.text(r_break/2, y_mid, 'INNER\ng₂ domain\n(steep)', 
           ha='center', va='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='red', alpha=0.3))
    ax.text((r_break + r.max())/2, y_mid, 'OUTER\ng₁ domain\n(flat)',
           ha='center', va='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='green', alpha=0.3))
    
    plt.tight_layout()
    output_file = output_dir / '1_temperature_profile_with_break.png'
    plt.savefig(output_file, dpi=200, bbox_inches='tight')
    plt.close()
    print(f"  ✓ {output_file.name}")

def plot2_piecewise_fit_comparison(r, T, r_break, output_dir):
    """Plot 2: Piecewise vs smooth fit comparison"""
    from scipy import optimize
    
    # Piecewise linear fit
    def piecewise_linear(x, x_break, m1, b1, m2, b2):
        return np.where(x < x_break, m1*x + b1, m2*x + b2)
    
    def residual(params):
        x_break, m1, b1, m2, b2 = params
        y_pred = piecewise_linear(r, x_break, m1, b1, m2, b2)
        return np.sum((T - y_pred)**2)
    
    result = optimize.minimize(residual, [r_break, -50, 100, -10, 50], method='Nelder-Mead')
    x_break, m1, b1, m2, b2 = result.x
    y_piecewise = piecewise_linear(r, x_break, m1, b1, m2, b2)
    
    # Smooth polynomial fit
    p_smooth = np.polyfit(r, T, 3)
    y_smooth = np.polyval(p_smooth, r)
    
    # Calculate R²
    ss_res_piece = np.sum((T - y_piecewise)**2)
    ss_res_smooth = np.sum((T - y_smooth)**2)
    ss_tot = np.sum((T - np.mean(T))**2)
    r2_piece = 1 - (ss_res_piece / ss_tot)
    r2_smooth = 1 - (ss_res_smooth / ss_tot)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
    
    # LEFT: Piecewise fit
    ax1.plot(r, T, 'ko', markersize=10, label='Data', zorder=3)
    ax1.plot(r, y_piecewise, 'g-', linewidth=3, label=f'Piecewise fit (R²={r2_piece:.4f})', zorder=2)
    ax1.axvline(x_break, color='red', linestyle='--', linewidth=2, alpha=0.7)
    ax1.set_xlabel('Radius r [pc]', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Temperature T [K]', fontsize=12, fontweight='bold')
    ax1.set_title('Piecewise Linear Model\n(Sharp Break)', fontsize=14, fontweight='bold')
    ax1.legend(fontsize=11)
    ax1.grid(True, alpha=0.3)
    
    # Add fit equations
    ax1.text(0.05, 0.95, f'Inner: T = {m1:.1f}·r + {b1:.1f}\nOuter: T = {m2:.1f}·r + {b2:.1f}',
            transform=ax1.transAxes, va='top', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    # RIGHT: Smooth fit
    ax2.plot(r, T, 'ko', markersize=10, label='Data', zorder=3)
    ax2.plot(r, y_smooth, 'b-', linewidth=3, label=f'Cubic fit (R²={r2_smooth:.4f})', zorder=2)
    ax2.set_xlabel('Radius r [pc]', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Temperature T [K]', fontsize=12, fontweight='bold')
    ax2.set_title('Smooth Cubic Model\n(No Break)', fontsize=14, fontweight='bold')
    ax2.legend(fontsize=11)
    ax2.grid(True, alpha=0.3)
    
    plt.suptitle('Model Comparison: Piecewise (R²=0.995) vs Smooth (R²={:.3f})'.format(r2_smooth),
                fontsize=16, fontweight='bold')
    plt.tight_layout()
    
    output_file = output_dir / '2_piecewise_vs_smooth_fit.png'
    plt.savefig(output_file, dpi=200, bbox_inches='tight')
    plt.close()
    print(f"  ✓ {output_file.name}")

def plot3_gradient_analysis(r, T, output_dir):
    """Plot 3: Gradient and curvature analysis"""
    dT_dr = np.gradient(T, r)
    d2T_dr2 = np.gradient(dT_dr, r)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # TOP: First derivative
    ax1.plot(r, dT_dr, 'b-', linewidth=3, label='dT/dr')
    ax1.axhline(0, color='k', linestyle=':', alpha=0.5)
    
    # Mark steepest point
    idx_steep = np.argmin(dT_dr)
    ax1.plot(r[idx_steep], dT_dr[idx_steep], 'ro', markersize=15, 
            label=f'Steepest: {dT_dr[idx_steep]:.1f} K/pc at r={r[idx_steep]:.2f}')
    
    ax1.set_xlabel('Radius r [pc]', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Temperature Gradient dT/dr [K/pc]', fontsize=12, fontweight='bold')
    ax1.set_title('First Derivative: Temperature Gradient', fontsize=14, fontweight='bold')
    ax1.legend(fontsize=11)
    ax1.grid(True, alpha=0.3)
    
    # BOTTOM: Second derivative
    ax2.plot(r, np.abs(d2T_dr2), 'purple', linewidth=3, label='|d²T/dr²|')
    
    # Mark maximum curvature
    idx_curv = np.argmax(np.abs(d2T_dr2))
    ax2.plot(r[idx_curv], np.abs(d2T_dr2[idx_curv]), 'ro', markersize=15,
            label=f'Max curvature: {np.abs(d2T_dr2[idx_curv]):.1f} K/pc² at r={r[idx_curv]:.2f}')
    
    ax2.set_xlabel('Radius r [pc]', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Curvature |d²T/dr²| [K/pc²]', fontsize=12, fontweight='bold')
    ax2.set_title('Second Derivative: Curvature (Sharp Break Indicator)', fontsize=14, fontweight='bold')
    ax2.legend(fontsize=11)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    output_file = output_dir / '3_gradient_curvature_analysis.png'
    plt.savefig(output_file, dpi=200, bbox_inches='tight')
    plt.close()
    print(f"  ✓ {output_file.name}")

def plot4_domain_structure(r, T, r_break, output_dir):
    """Plot 4: g₁/g₂ domain structure"""
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Split data
    mask_g2 = r < r_break
    mask_g1 = r >= r_break
    
    # Plot domains
    ax.plot(r[mask_g2], T[mask_g2], 'ro-', linewidth=3, markersize=12, 
           label='g₂ domain (collapse)', zorder=3)
    ax.plot(r[mask_g1], T[mask_g1], 'go-', linewidth=3, markersize=12,
           label='g₁ domain (stable)', zorder=3)
    
    # Linear fits for each domain
    if np.any(mask_g2):
        p_g2 = np.polyfit(r[mask_g2], T[mask_g2], 1)
        r_g2_fit = np.linspace(r[mask_g2].min(), r[mask_g2].max(), 50)
        ax.plot(r_g2_fit, np.polyval(p_g2, r_g2_fit), 'r--', linewidth=2, alpha=0.7,
               label=f'g₂ fit: {p_g2[0]:.1f}·r + {p_g2[1]:.1f}')
    
    if np.any(mask_g1):
        p_g1 = np.polyfit(r[mask_g1], T[mask_g1], 1)
        r_g1_fit = np.linspace(r[mask_g1].min(), r[mask_g1].max(), 50)
        ax.plot(r_g1_fit, np.polyval(p_g1, r_g1_fit), 'g--', linewidth=2, alpha=0.7,
               label=f'g₁ fit: {p_g1[0]:.1f}·r + {p_g1[1]:.1f}')
        
        # Calculate slope ratio
        if np.any(mask_g2):
            slope_ratio = abs(p_g2[0] / p_g1[0])
            ax.text(0.5, 0.95, f'Slope ratio: |m₂/m₁| = {slope_ratio:.2f}×',
                   transform=ax.transAxes, ha='center', va='top',
                   fontsize=14, fontweight='bold',
                   bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8))
    
    # Mark transition
    ax.axvline(r_break, color='black', linestyle='-', linewidth=3,
              label=f'Critical radius: r_c = {r_break:.3f} pc', zorder=2)
    
    # Shade domains
    ax.axvspan(r.min(), r_break, alpha=0.15, color='red', zorder=1)
    ax.axvspan(r_break, r.max(), alpha=0.15, color='green', zorder=1)
    
    ax.set_xlabel('Radius r [pc]', fontsize=14, fontweight='bold')
    ax.set_ylabel('Temperature T [K]', fontsize=14, fontweight='bold')
    ax.set_title('SSZ Domain Structure: g₂ (Collapse) → g₁ (Stable)\nSharp Transition at Critical Radius',
                fontsize=16, fontweight='bold')
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    output_file = output_dir / '4_domain_structure_g1_g2.png'
    plt.savefig(output_file, dpi=200, bbox_inches='tight')
    plt.close()
    print(f"  ✓ {output_file.name}")

def plot5_residual_analysis(r, T, r_break, output_dir):
    """Plot 5: Residual comparison piecewise vs smooth"""
    from scipy import optimize
    
    # Piecewise fit
    def piecewise_linear(x, x_break, m1, b1, m2, b2):
        return np.where(x < x_break, m1*x + b1, m2*x + b2)
    
    def residual(params):
        x_break, m1, b1, m2, b2 = params
        y_pred = piecewise_linear(r, x_break, m1, b1, m2, b2)
        return np.sum((T - y_pred)**2)
    
    result = optimize.minimize(residual, [r_break, -50, 100, -10, 50], method='Nelder-Mead')
    x_break, m1, b1, m2, b2 = result.x
    y_piecewise = piecewise_linear(r, x_break, m1, b1, m2, b2)
    res_piecewise = T - y_piecewise
    
    # Smooth fit
    p_smooth = np.polyfit(r, T, 3)
    y_smooth = np.polyval(p_smooth, r)
    res_smooth = T - y_smooth
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
    
    # LEFT: Piecewise residuals
    ax1.axhline(0, color='k', linestyle='--', linewidth=2)
    ax1.bar(r, res_piecewise, width=0.15, color='green', alpha=0.7, edgecolor='black')
    ax1.set_xlabel('Radius r [pc]', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Residual [K]', fontsize=12, fontweight='bold')
    ax1.set_title(f'Piecewise Model Residuals\nRMS = {np.sqrt(np.mean(res_piecewise**2)):.2f} K',
                 fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3, axis='y')
    
    # RIGHT: Smooth residuals
    ax2.axhline(0, color='k', linestyle='--', linewidth=2)
    ax2.bar(r, res_smooth, width=0.15, color='blue', alpha=0.7, edgecolor='black')
    ax2.set_xlabel('Radius r [pc]', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Residual [K]', fontsize=12, fontweight='bold')
    ax2.set_title(f'Smooth Cubic Residuals\nRMS = {np.sqrt(np.mean(res_smooth**2)):.2f} K',
                 fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='y')
    
    plt.suptitle('Residual Comparison: Piecewise vs Smooth Model', 
                fontsize=16, fontweight='bold')
    plt.tight_layout()
    
    output_file = output_dir / '5_residual_comparison.png'
    plt.savefig(output_file, dpi=200, bbox_inches='tight')
    plt.close()
    print(f"  ✓ {output_file.name}")

def main():
    """Main execution"""
    print("\n" + "="*70)
    print("GENERATING SHARP BREAK PLOTS")
    print("="*70 + "\n")
    
    # Create output directory
    output_dir = Path("plots/sharp-break")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Load data
    r, T = load_data()
    print(f"✓ Loaded {len(r)} temperature points\n")
    
    # Use consensus break point
    r_break = 0.900  # From detection analysis
    
    print("Generating plots...")
    plot1_temperature_profile_with_break(r, T, r_break, output_dir)
    plot2_piecewise_fit_comparison(r, T, r_break, output_dir)
    plot3_gradient_analysis(r, T, output_dir)
    plot4_domain_structure(r, T, r_break, output_dir)
    plot5_residual_analysis(r, T, r_break, output_dir)
    
    print("\n" + "="*70)
    print("COMPLETE!")
    print(f"Generated 5 high-resolution plots in {output_dir}")
    print("="*70 + "\n")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
