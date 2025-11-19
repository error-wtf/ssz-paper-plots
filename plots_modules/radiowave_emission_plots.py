#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Radiowave Emission Plots
=========================
Critical plots for radiowave precursor predictions

Paper prediction: Radiowaves appear BEFORE optical/X-ray
Mechanism: Excess energy release in g₂ region

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

def plot_radiowave_spectrum_from_excess_energy(output_dir='plots/missing'):
    """
    Radiowave spectrum generated from excess kinetic energy
    
    Shows frequency distribution: radio-dominated
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Frequency range
    freq = np.logspace(6, 18, 1000)  # Hz (Radio to X-ray)
    
    # Frequency bands
    radio_mask = freq < 1e10
    optical_mask = (freq >= 4e14) & (freq <= 8e14)
    xray_mask = freq > 1e17
    
    # SSZ prediction: Low frequency dominance
    # Power ~ 1/f^α where α > 0 (steep spectrum)
    alpha = 2.5  # Steep decline
    f0 = 1e9  # Reference frequency (1 GHz)
    
    # Excess energy spectrum
    P_excess = (f0 / freq)**alpha
    P_excess = P_excess / np.max(P_excess)  # Normalize
    
    # GR: No emission mechanism
    P_gr = np.zeros_like(freq)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Top: Full spectrum
    ax1.loglog(freq, P_excess, 'b-', linewidth=2.5, label='SSZ: Excess energy emission')
    ax1.loglog(freq, P_gr, 'r--', linewidth=2, label='GR: No emission', alpha=0.7)
    
    # Mark frequency bands
    ax1.axvspan(freq[0], 1e10, alpha=0.2, color='green', label='Radio (dominant)')
    ax1.axvspan(4e14, 8e14, alpha=0.2, color='yellow', label='Optical (suppressed)')
    ax1.axvspan(1e17, freq[-1], alpha=0.2, color='red', label='X-ray (suppressed)')
    
    ax1.set_xlabel('Frequency (Hz)', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Power (arbitrary units)', fontsize=12, fontweight='bold')
    ax1.set_title('SSZ: Radiowave Spectrum from Excess Energy (v_eigen)', fontsize=13, fontweight='bold')
    ax1.legend(fontsize=10, loc='upper right')
    ax1.grid(True, alpha=0.3, which='both')
    ax1.set_ylim(1e-5, 2)
    
    # Bottom: Energy distribution by band
    radio_energy = np.trapz(P_excess[radio_mask], freq[radio_mask])
    optical_energy = np.trapz(P_excess[optical_mask], freq[optical_mask]) if np.any(optical_mask) else 0
    xray_energy = np.trapz(P_excess[xray_mask], freq[xray_mask])
    
    total = radio_energy + optical_energy + xray_energy
    percentages = [radio_energy/total*100, optical_energy/total*100, xray_energy/total*100]
    
    bands = ['Radio\n(<10 GHz)', 'Optical\n(visible)', 'X-ray\n(>10¹⁷ Hz)']
    colors = ['green', 'yellow', 'red']
    
    bars = ax2.bar(bands, percentages, color=colors, alpha=0.7, edgecolor='black', linewidth=2)
    ax2.set_ylabel('Energy Fraction (%)', fontsize=12, fontweight='bold')
    ax2.set_title('Energy Distribution: Radio Dominance in SSZ', fontsize=13, fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='y')
    
    # Add percentage labels
    for bar, pct in zip(bars, percentages):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{pct:.1f}%', ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    plt.tight_layout()
    
    output_file = output_dir / '4_radiowave_spectrum_EXCESS_ENERGY.png'
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"  ✓ Generated: {output_file.name}")
    return [str(output_file)]

def plot_multi_frequency_timeline(output_dir='plots/missing'):
    """
    Multi-frequency light curve: Radio BEFORE Optical/X-ray
    
    KEY PREDICTION: Temporal ordering
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Time array (days)
    time = np.linspace(0, 100, 500)
    
    # SSZ prediction: Radio precursor
    # Radio peaks at t=20 days
    t_radio = 20
    sigma_radio = 8
    radio_flux = np.exp(-(time - t_radio)**2 / (2*sigma_radio**2))
    
    # X-ray appears at t=50 days (30 days AFTER radio)
    t_xray = 50
    sigma_xray = 5
    xray_flux = 0.6 * np.exp(-(time - t_xray)**2 / (2*sigma_xray**2))
    
    # Optical jet appears at t=65 days (45 days after radio)
    t_optical = 65
    sigma_optical = 7
    optical_flux = 0.8 * np.exp(-(time - t_optical)**2 / (2*sigma_optical**2))
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), sharex=True)
    
    # Top: Light curves
    ax1.plot(time, radio_flux, 'g-', linewidth=3, label='Radio (1.4 GHz)')
    ax1.plot(time, xray_flux, 'r-', linewidth=3, label='X-ray (2-10 keV)')
    ax1.plot(time, optical_flux, 'b-', linewidth=3, label='Optical (V-band)')
    
    # Mark key events
    ax1.axvline(t_radio, color='g', linestyle='--', alpha=0.5, linewidth=2)
    ax1.axvline(t_xray, color='r', linestyle='--', alpha=0.5, linewidth=2)
    ax1.axvline(t_optical, color='b', linestyle='--', alpha=0.5, linewidth=2)
    
    # Annotations
    ax1.text(t_radio, 1.05, 'Radio\nprecursor', ha='center', fontsize=11, fontweight='bold', color='green')
    ax1.text(t_xray, 0.65, 'X-ray\nrise', ha='center', fontsize=11, fontweight='bold', color='red')
    ax1.text(t_optical, 0.85, 'Optical\njet', ha='center', fontsize=11, fontweight='bold', color='blue')
    
    # Time delays
    ax1.annotate('', xy=(t_xray, 0.5), xytext=(t_radio, 0.5),
                arrowprops=dict(arrowstyle='<->', lw=2, color='black'))
    ax1.text((t_radio + t_xray)/2, 0.55, f'Δt = {t_xray-t_radio} days',
            ha='center', fontsize=10, fontweight='bold')
    
    ax1.set_ylabel('Flux (arbitrary)', fontsize=12, fontweight='bold')
    ax1.set_title('SSZ Prediction: Radiowave Precursor BEFORE Optical/X-ray', fontsize=14, fontweight='bold')
    ax1.legend(fontsize=11, loc='upper right')
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim(-0.1, 1.2)
    
    # Bottom: Cumulative energy
    radio_cum = np.cumsum(radio_flux) / np.sum(radio_flux)
    xray_cum = np.cumsum(xray_flux) / np.sum(xray_flux)
    optical_cum = np.cumsum(optical_flux) / np.sum(optical_flux)
    
    ax2.plot(time, radio_cum, 'g-', linewidth=3, label='Radio (cumulative)')
    ax2.plot(time, xray_cum, 'r-', linewidth=3, label='X-ray (cumulative)')
    ax2.plot(time, optical_cum, 'b-', linewidth=3, label='Optical (cumulative)')
    
    ax2.axhline(0.5, color='k', linestyle=':', alpha=0.5)
    ax2.set_xlabel('Time (days)', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Cumulative Energy Fraction', fontsize=12, fontweight='bold')
    ax2.set_title('Cumulative Energy Release: Radio First', fontsize=13, fontweight='bold')
    ax2.legend(fontsize=11)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    output_file = output_dir / '5_radiowave_BEFORE_optical_TIMELINE.png'
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"  ✓ Generated: {output_file.name}")
    return [str(output_file)]

def plot_radio_intensity_vs_infall_velocity(output_dir='plots/missing'):
    """
    Radio intensity correlation with v_eigen (infall velocity)
    
    Prediction: Faster infall → stronger radio emission
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Infall velocity (fraction of c)
    v_eigen = np.linspace(0, 0.8, 100)
    
    # Radio power ~ v_eigen² (kinetic energy)
    radio_power = v_eigen**2
    
    # Scatter with some realistic spread
    np.random.seed(42)
    v_sample = np.random.uniform(0.1, 0.7, 50)
    radio_sample = v_sample**2 * (1 + 0.2 * np.random.randn(50))
    radio_sample = np.clip(radio_sample, 0, None)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Left: Power law
    ax1.plot(v_eigen, radio_power, 'b-', linewidth=3, label='SSZ: $P_{radio} \\propto v_{eigen}^2$')
    ax1.scatter(v_sample, radio_sample, s=100, alpha=0.6, color='green', 
               edgecolors='black', linewidths=1.5, label='Simulated observations', zorder=5)
    
    ax1.set_xlabel('Infall Velocity $v_{eigen}$ (c)', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Radio Power (arbitrary)', fontsize=12, fontweight='bold')
    ax1.set_title('Radio Emission vs Infall Velocity', fontsize=13, fontweight='bold')
    ax1.legend(fontsize=11)
    ax1.grid(True, alpha=0.3)
    
    # Right: Correlation coefficient
    bins = [0, 0.2, 0.4, 0.6, 0.8]
    bin_centers = [(bins[i] + bins[i+1])/2 for i in range(len(bins)-1)]
    mean_radio = []
    
    for i in range(len(bins)-1):
        mask = (v_sample >= bins[i]) & (v_sample < bins[i+1])
        if np.any(mask):
            mean_radio.append(np.mean(radio_sample[mask]))
        else:
            mean_radio.append(0)
    
    ax2.bar(bin_centers, mean_radio, width=0.18, alpha=0.7, color='purple',
           edgecolor='black', linewidth=2, label='Mean radio power')
    
    ax2.set_xlabel('Infall Velocity Bin (c)', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Mean Radio Power', fontsize=12, fontweight='bold')
    ax2.set_title('Binned Correlation Analysis', fontsize=13, fontweight='bold')
    ax2.legend(fontsize=11)
    ax2.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    
    output_file = output_dir / '6_radio_vs_infall_velocity_CORRELATION.png'
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"  ✓ Generated: {output_file.name}")
    return [str(output_file)]

def generate_all(output_dir='plots/missing'):
    """Generate all radiowave emission plots"""
    print("\n[RADIOWAVE EMISSION PLOTS]")
    print("-" * 60)
    
    all_plots = []
    all_plots.extend(plot_radiowave_spectrum_from_excess_energy(output_dir))
    all_plots.extend(plot_multi_frequency_timeline(output_dir))
    all_plots.extend(plot_radio_intensity_vs_infall_velocity(output_dir))
    
    print(f"  ✓ Generated {len(all_plots)} plots")
    return all_plots

if __name__ == "__main__":
    plots = generate_all()
    print(f"\nTotal: {len(plots)} plots")
