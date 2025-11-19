#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Excess Energy Release Plots
============================
Shows v_eigen (excess kinetic energy) release mechanism

Paper concept: g₂ absorbs v_fall but NOT v_eigen
Excess energy must be released as radiowaves

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

def plot_velocity_decomposition_diagram(output_dir='plots/missing'):
    """
    v_total = v_fall + v_eigen decomposition
    
    Shows which component is absorbed vs released
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    fig, ax = plt.subplots(1, 1, figsize=(12, 10))
    
    # Setup
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Draw g₁-g₂ boundary
    ax.axvline(5, ymin=0.2, ymax=0.8, color='green', linewidth=4, linestyle='--', label='$g_1$-$g_2$ boundary')
    ax.text(5, 8.5, '$g_1 \\leftrightarrow g_2$ boundary', ha='center', fontsize=14, fontweight='bold', color='green')
    
    # Regions
    ax.text(2.5, 9, '$g_1$ (weak segmentation)', ha='center', fontsize=13, fontweight='bold', 
           bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
    ax.text(7.5, 9, '$g_2$ (strong segmentation)', ha='center', fontsize=13, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))
    
    # Infalling object
    y_obj = 5
    ax.scatter(3, y_obj, s=500, color='blue', edgecolors='black', linewidths=2, zorder=10, label='Infalling matter')
    
    # Velocity vectors
    # v_total
    ax.arrow(3, y_obj, 1.5, 0, head_width=0.3, head_length=0.2, fc='black', ec='black', linewidth=3)
    ax.text(3.75, y_obj + 0.5, '$v_{total}$', fontsize=12, fontweight='bold')
    
    # v_fall (gravitational)
    ax.arrow(3, y_obj - 1, 1, 0, head_width=0.25, head_length=0.15, fc='red', ec='red', linewidth=2.5, linestyle='--')
    ax.text(3.5, y_obj - 1.5, '$v_{fall}$ (gravitational)', fontsize=11, fontweight='bold', color='red')
    
    # v_eigen (intrinsic)
    ax.arrow(3, y_obj + 1, 0.5, 0, head_width=0.25, head_length=0.15, fc='blue', ec='blue', linewidth=2.5, linestyle='-.')
    ax.text(3.25, y_obj + 1.5, '$v_{eigen}$ (intrinsic)', fontsize=11, fontweight='bold', color='blue')
    
    # At boundary
    ax.scatter(5, y_obj, s=300, color='orange', marker='*', edgecolors='black', linewidths=2, zorder=10)
    
    # What happens at boundary
    # v_fall absorbed
    ax.text(6.5, y_obj - 1.5, '$v_{fall}$ absorbed by $g_2$', fontsize=11, fontweight='bold', color='red',
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
    
    # v_eigen MUST be released
    ax.arrow(6, y_obj + 1, -1, 0, head_width=0.3, head_length=0.2, fc='purple', ec='purple', linewidth=3)
    ax.text(5.5, y_obj + 1.8, '$v_{eigen}$ RELEASED', fontsize=12, fontweight='bold', color='purple')
    ax.text(5.5, y_obj + 2.5, '(as radiowaves)', fontsize=11, fontweight='bold', color='purple', style='italic')
    
    # Energy conservation equation
    eq_text = '$E_{total} = E_{gravitational} + E_{kinetic}$\n$E_{released} = \\frac{1}{2}m v_{eigen}^2$'
    ax.text(5, 1, eq_text, ha='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))
    
    ax.set_title('Velocity Decomposition at $g_1$-$g_2$ Boundary', fontsize=15, fontweight='bold')
    
    plt.tight_layout()
    
    output_file = output_dir / '7_velocity_decomposition_DIAGRAM.png'
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"  ✓ Generated: {output_file.name}")
    return [str(output_file)]

def plot_energy_budget_at_boundary(output_dir='plots/missing'):
    """
    Energy budget showing absorption vs release
    
    Conservation: E_in = E_absorbed + E_released
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Example scenarios
    scenarios = ['Slow\ninfall', 'Medium\ninfall', 'Fast\ninfall', 'Ultra-fast\ninfall']
    v_fall_frac = np.array([0.7, 0.6, 0.5, 0.4])  # Fraction of total
    v_eigen_frac = 1 - v_fall_frac
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Left: Stacked bar chart
    x = np.arange(len(scenarios))
    width = 0.6
    
    p1 = ax1.bar(x, v_fall_frac, width, label='$E_{gravitational}$ (absorbed)', color='red', alpha=0.7)
    p2 = ax1.bar(x, v_eigen_frac, width, bottom=v_fall_frac, label='$E_{kinetic}$ (released)', color='blue', alpha=0.7)
    
    ax1.set_ylabel('Energy Fraction', fontsize=12, fontweight='bold')
    ax1.set_title('Energy Budget at $g_1$-$g_2$ Boundary', fontsize=13, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(scenarios, fontsize=11)
    ax1.legend(fontsize=11)
    ax1.grid(True, alpha=0.3, axis='y')
    ax1.axhline(1, color='k', linestyle='--', linewidth=2, alpha=0.5)
    
    # Add percentage labels
    for i, (vf, ve) in enumerate(zip(v_fall_frac, v_eigen_frac)):
        ax1.text(i, vf/2, f'{vf*100:.0f}%', ha='center', va='center', 
                fontsize=11, fontweight='bold', color='white')
        ax1.text(i, vf + ve/2, f'{ve*100:.0f}%', ha='center', va='center',
                fontsize=11, fontweight='bold', color='white')
    
    # Right: Released energy vs v_eigen
    v_eigen = np.linspace(0, 0.9, 100)  # In units of c
    E_released = 0.5 * v_eigen**2  # Kinetic energy (m=1, c=1)
    
    ax2.plot(v_eigen, E_released, 'b-', linewidth=3, label='$E_{released} = \\frac{1}{2}v_{eigen}^2$')
    ax2.fill_between(v_eigen, 0, E_released, alpha=0.3, color='blue')
    
    # Mark example points
    v_examples = [0.3, 0.5, 0.7]
    for v in v_examples:
        E = 0.5 * v**2
        ax2.scatter(v, E, s=150, color='red', edgecolors='black', linewidths=2, zorder=5)
        ax2.text(v, E + 0.03, f'$v={v}c$', ha='center', fontsize=10, fontweight='bold')
    
    ax2.set_xlabel('Intrinsic Velocity $v_{eigen}$ (c)', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Released Energy (mc²)', fontsize=12, fontweight='bold')
    ax2.set_title('Released Energy vs Intrinsic Velocity', fontsize=13, fontweight='bold')
    ax2.legend(fontsize=11)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    output_file = output_dir / '8_energy_budget_CONSERVATION.png'
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"  ✓ Generated: {output_file.name}")
    return [str(output_file)]

def plot_energy_flow_diagram(output_dir='plots/missing'):
    """
    Energy flow from g₁ through boundary to g₂
    
    Sankey-style diagram showing paths
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    fig, ax = plt.subplots(1, 1, figsize=(14, 8))
    
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(5, 9.5, 'Energy Flow at $g_1$-$g_2$ Boundary', ha='center', fontsize=16, fontweight='bold')
    
    # Input (left side)
    ax.text(1, 7, 'INPUT\n$E_{total}$', ha='center', va='center', fontsize=13, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.9, edgecolor='black', linewidth=2))
    
    # Boundary (center)
    ax.axvline(5, ymin=0.1, ymax=0.9, color='green', linewidth=6, linestyle='--', alpha=0.7)
    ax.text(5, 0.5, '$g_1 \\leftrightarrow g_2$', ha='center', fontsize=12, fontweight='bold', 
           color='green', rotation=90)
    
    # Outputs (right side)
    # Absorbed
    ax.text(8.5, 7.5, 'ABSORBED\n$E_{fall}$\n(to $g_2$ core)', ha='center', va='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.9, edgecolor='black', linewidth=2))
    
    # Released
    ax.text(8.5, 4.5, 'RELEASED\n$E_{eigen}$\n(as radiowaves)', ha='center', va='center', fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9, edgecolor='black', linewidth=2))
    
    # Flow arrows
    # Input to boundary
    ax.annotate('', xy=(4.5, 7), xytext=(2, 7),
               arrowprops=dict(arrowstyle='->', lw=4, color='black'))
    ax.text(3.25, 7.3, '$E_{total}$', fontsize=11, fontweight='bold')
    
    # Boundary to absorbed
    ax.annotate('', xy=(7.5, 7.5), xytext=(5.5, 7.2),
               arrowprops=dict(arrowstyle='->', lw=3, color='red'))
    ax.text(6.5, 7.6, '70%', fontsize=11, fontweight='bold', color='red')
    
    # Boundary to released
    ax.annotate('', xy=(7.5, 4.5), xytext=(5.5, 5.8),
               arrowprops=dict(arrowstyle='->', lw=3, color='blue'))
    ax.text(6.5, 5.3, '30%', fontsize=11, fontweight='bold', color='blue')
    
    # Conservation equation
    eq_text = 'Energy Conservation:\n$E_{total} = E_{fall} + E_{eigen}$\n$100\\% = 70\\% + 30\\%$ (example)'
    ax.text(5, 1.5, eq_text, ha='center', fontsize=11, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.9, edgecolor='black', linewidth=2))
    
    plt.tight_layout()
    
    output_file = output_dir / '9_energy_flow_DIAGRAM.png'
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"  ✓ Generated: {output_file.name}")
    return [str(output_file)]

def generate_all(output_dir='plots/missing'):
    """Generate all excess energy plots"""
    print("\n[EXCESS ENERGY PLOTS]")
    print("-" * 60)
    
    all_plots = []
    all_plots.extend(plot_velocity_decomposition_diagram(output_dir))
    all_plots.extend(plot_energy_budget_at_boundary(output_dir))
    all_plots.extend(plot_energy_flow_diagram(output_dir))
    
    print(f"  ✓ Generated {len(all_plots)} plots")
    return all_plots

if __name__ == "__main__":
    plots = generate_all()
    print(f"\nTotal: {len(plots)} plots")
