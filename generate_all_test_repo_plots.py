#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ECHTE TEST-REPO PLOTS GENERATOR
================================

Generiert ALLE Plots aus den drei echten Test-Repos:
1. E:\clone\Segmented-Spacetime-Mass-Projection-Unified-Results
2. E:\clone\g79-cygnus-test
3. E:\clone\ssz-metric-pure

Output: plots/test-repos/ mit allen echten Test-Plots

© 2025 Carmen Wrede, Lino Casu, Bingsi
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
"""

import os
import sys
from pathlib import Path
import subprocess
import shutil

os.environ['PYTHONIOENCODING'] = 'utf-8:replace'
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except:
        pass

BASE_PATH = Path(__file__).parent
OUTPUT_DIR = BASE_PATH / "plots" / "test-repos"

# Die drei echten Test-Repos
REPO1 = Path(r"E:\clone\Segmented-Spacetime-Mass-Projection-Unified-Results")
REPO2 = Path(r"E:\clone\g79-cygnus-test")
REPO3 = Path(r"E:\clone\ssz-metric-pure")

# Echte Plot-generierende Scripts aus den Repos (gefunden via grep plt.savefig)
PLOT_SCRIPTS = {
    'unified_results': [
        'run_ssz_unified_validation.py',
        'run_ssz_validation.py',
        'run_ssz_theory_validation.py',
        'generate_key_plots.py',
        'generate_eso_breakthrough_plots.py',
        'ssz_stability_three_figures.py',
        'ssz_test_suite.py',
        'ssz_unified_suite.py',
        'bound_energy_plot.py',
        'phi_test.py',
        'vergleich_2.py',
        'segspace_all_in_one.py',
        'segspace_all_in_one_extended.py',
    ],
    'g79_cygnus': [
        'COMPLETE_PAPER_FIGURES.py',
        'GENERATE_ENGLISH_HIGHLIGHTS.py',
        'TEST_TEMPERATURE_EQUATIONS_COMPLETE.py',
        'TEST_THREE_PHASE_DECOUPLING.py',
    ],
    'ssz_metric': [
        'generate_validation_report.py',
        'examples/basic_usage.py',
    ]
}

def run_script(script_path, cwd, timeout=300):
    """Führt ein Script aus und gibt Status zurück"""
    try:
        print(f"    Running: {script_path.name}...")
        result = subprocess.run(
            [sys.executable, str(script_path)],
            cwd=str(cwd),
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace',
            timeout=timeout
        )
        if result.returncode == 0:
            print(f"      ✓ Success")
            return True
        else:
            print(f"      ⚠ Exited with code {result.returncode}")
            return False
    except subprocess.TimeoutExpired:
        print(f"      ⚠ Timeout after {timeout}s")
        return False
    except Exception as e:
        print(f"      ✗ Error: {e}")
        return False

def collect_plots(repo_path, output_subdir):
    """Sammelt alle PNG-Dateien aus einem Repo"""
    collected = 0
    output_path = OUTPUT_DIR / output_subdir
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Suche nach PNGs
    for pattern in ['*.png', 'out/*.png', 'outputs/*.png', 'plots/*.png', 
                    'results/*.png', 'figures/*.png']:
        for png_file in repo_path.glob(pattern):
            if '.venv' not in str(png_file) and '__pycache__' not in str(png_file):
                try:
                    dest = output_path / png_file.name
                    shutil.copy(png_file, dest)
                    collected += 1
                except Exception as e:
                    print(f"      ⚠ Copy failed: {png_file.name} - {e}")
    
    return collected

def main():
    print("\n" + "="*80)
    print("ECHTE TEST-REPO PLOTS GENERATOR")
    print("="*80)
    print(f"\nOutput: {OUTPUT_DIR}")
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    total_scripts = 0
    total_success = 0
    total_plots = 0
    
    # ========================================================================
    # REPO 1: Segmented-Spacetime-Mass-Projection-Unified-Results
    # ========================================================================
    print(f"\n[1/3] UNIFIED RESULTS REPO")
    print("-" * 60)
    print(f"Path: {REPO1}")
    
    if REPO1.exists():
        for script_name in PLOT_SCRIPTS['unified_results']:
            script_path = REPO1 / script_name
            if script_path.exists():
                total_scripts += 1
                if run_script(script_path, REPO1):
                    total_success += 1
            else:
                print(f"    ⚠ Not found: {script_name}")
        
        # Sammle Plots
        print(f"\n  Collecting plots...")
        plots = collect_plots(REPO1, "unified-results")
        print(f"  ✓ Collected {plots} plots")
        total_plots += plots
    else:
        print(f"  ✗ Repo not found!")
    
    # ========================================================================
    # REPO 2: g79-cygnus-test
    # ========================================================================
    print(f"\n[2/3] G79 CYGNUS TEST REPO")
    print("-" * 60)
    print(f"Path: {REPO2}")
    
    if REPO2.exists():
        for script_name in PLOT_SCRIPTS['g79_cygnus']:
            script_path = REPO2 / script_name
            if script_path.exists():
                total_scripts += 1
                if run_script(script_path, REPO2, timeout=600):
                    total_success += 1
            else:
                print(f"    ⚠ Not found: {script_name}")
        
        # Sammle Plots
        print(f"\n  Collecting plots...")
        plots = collect_plots(REPO2, "g79-cygnus")
        print(f"  ✓ Collected {plots} plots")
        total_plots += plots
    else:
        print(f"  ✗ Repo not found!")
    
    # ========================================================================
    # REPO 3: ssz-metric-pure
    # ========================================================================
    print(f"\n[3/3] SSZ METRIC PURE REPO")
    print("-" * 60)
    print(f"Path: {REPO3}")
    
    if REPO3.exists():
        for script_name in PLOT_SCRIPTS['ssz_metric']:
            script_path = REPO3 / script_name
            if script_path.exists():
                total_scripts += 1
                if run_script(script_path, REPO3):
                    total_success += 1
            else:
                print(f"    ⚠ Not found: {script_name}")
        
        # Sammle Plots
        print(f"\n  Collecting plots...")
        plots = collect_plots(REPO3, "ssz-metric-pure")
        print(f"  ✓ Collected {plots} plots")
        total_plots += plots
    else:
        print(f"  ✗ Repo not found!")
    
    # ========================================================================
    # SUMMARY
    # ========================================================================
    print("\n" + "="*80)
    print("GENERATION COMPLETE")
    print("="*80)
    print(f"\n📊 Summary:")
    print(f"  Scripts found:     {total_scripts}")
    print(f"  Scripts success:   {total_success}")
    print(f"  Plots collected:   {total_plots}")
    print(f"\n📁 Output:")
    print(f"  {OUTPUT_DIR}/unified-results/")
    print(f"  {OUTPUT_DIR}/g79-cygnus/")
    print(f"  {OUTPUT_DIR}/ssz-metric-pure/")
    print("="*80)
    
    return total_plots

if __name__ == "__main__":
    try:
        plots = main()
        sys.exit(0 if plots > 0 else 1)
    except Exception as e:
        print(f"\n✗ Fatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
