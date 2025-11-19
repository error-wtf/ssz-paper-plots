#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MASTER PLOT GENERATOR - SSZ Complete Suite
===========================================

Generiert ALLE 86+ SSZ-Plots mit einem einzigen Befehl.
Standalone, keine Abhängigkeiten zu anderen Repos.

Verwendung:
    python generate_all_plots.py

Output:
    plots/nested/       - 2 plots (kubisches Modell)
    plots/generated/    - 4 plots (SVR-SSZ)
    plots/additional/   - 68 plots (Validierung)
    plots/comparison/   - 6 plots (Kubisch vs Piecewise)
    plots/paper/        - 6 plots (Paper-konform, nur Piecewise)
    
    TOTAL: 86 plots + 2 reports

Dauer: ~2-3 Minuten

© 2025 Carmen Wrede, Lino Casu, Bingsi
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
"""

import os
import sys
import subprocess
from pathlib import Path
from datetime import datetime

# UTF-8 für Windows
os.environ['PYTHONIOENCODING'] = 'utf-8:replace'
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except:
        pass

BASE_PATH = Path(__file__).parent
PLOTS_DIR = BASE_PATH / "plots"

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def print_header(title):
    """Print formatted section header"""
    print("\n" + "="*80)
    print(f"  {title}")
    print("="*80)

def print_step(number, total, description):
    """Print formatted step"""
    print(f"\n[{number}/{total}] {description}")
    print("-" * 60)

def run_script(script_name, description):
    """Run a Python script and capture output"""
    script_path = BASE_PATH / script_name
    
    if not script_path.exists():
        print(f"  ⚠ Script not found: {script_name}")
        return False
    
    print(f"  Running: {script_name}")
    
    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            cwd=str(BASE_PATH),
            capture_output=False,  # Show output directly
            text=True,
            encoding='utf-8',
            errors='replace',
            timeout=600  # 10 minutes max per script
        )
        
        if result.returncode == 0:
            print(f"  ✓ Success: {description}")
            return True
        else:
            print(f"  ✗ Failed: {description} (exit code {result.returncode})")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"  ✗ Timeout: {description}")
        return False
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

def count_plots(directory):
    """Count PNG files in directory"""
    plot_dir = PLOTS_DIR / directory
    if not plot_dir.exists():
        return 0
    return len(list(plot_dir.glob("*.png")))

def create_directories():
    # Results summary
    plot_counts = {
        'nested': 2,
        'generated': 4,
        'additional': 61,
        'comparison': 6,
        'test-repos': "100+",
        'paper': 6
    }
    dirs = ['nested', 'generated', 'additional', 'comparison', 'paper']
    for d in dirs:
        (PLOTS_DIR / d).mkdir(parents=True, exist_ok=True)

# ============================================================================
# MAIN GENERATION PIPELINE
# ============================================================================

def main():
    start_time = datetime.now()
    
    print("\n" + "#"*80)
    print("#" + " "*78 + "#")
    print("#" + "  SSZ COMPLETE PLOT GENERATOR".center(78) + "#")
    print("#" + "  All 86+ Plots in One Command".center(78) + "#")
    print("#" + " "*78 + "#")
    print("#"*80)
    
    print(f"\nStart time: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Output directory: {PLOTS_DIR}")
    
    # Create directories
    create_directories()
    print("✓ Output directories created")
    
    # Track results
    results = {}
    total_steps = 6
    
    # ========================================================================
    # STEP 1: NESTED PLOTS (Kubisches Modell)
    # ========================================================================
    print_step(1, total_steps, "NESTED PLOTS (Kubisches Coherence-Collapse)")
    results['nested'] = run_script(
        'nested_ssz_metric_standalone.py',
        'Nested metric & coherence collapse'
    )
    
    # ========================================================================
    # STEP 2: GENERATED PLOTS (SVR-SSZ)
    # ========================================================================
    print_step(2, total_steps, "GENERATED PLOTS (SVR-SSZ Phänomenologie)")
    results['generated'] = run_script(
        'generate_local_plots.py',
        'SVR-SSZ scaling & metric evolution'
    )
    
    # ========================================================================
    # STEP 3: ADDITIONAL PLOTS (Standalone Validation)
    # ========================================================================
    print_step(3, total_steps, "ADDITIONAL PLOTS (Standalone Validierungs-Suite)")
    results['additional'] = run_script(
        'generate_validation_plots_compact.py',
        'PPN, Shadow, QNM, Proper Time, Energy, etc. (61 standalone plots)'
    )
    
    # ========================================================================
    # STEP 4: COMPARISON PLOTS (Kubisch vs Piecewise)
    # ========================================================================
    print_step(4, total_steps, "COMPARISON PLOTS (Modell-Vergleich)")
    results['comparison'] = run_script(
        'generate_comparison_plots.py',
        'Cubic vs Piecewise model comparison'
    )
    
    # ========================================================================
    # STEP 5: PAPER PLOTS (Nur Piecewise)
    # ========================================================================
    print_step(6, total_steps, "PAPER PLOTS (Paper-Conform, 100% Kompatibel)")
    results['paper'] = run_script(
        'generate_paper_plots.py',
        'Piecewise model for radiowave paper'
    )
    
    # ========================================================================
    # SUMMARY
    # ========================================================================
    end_time = datetime.now()
    duration = end_time - start_time
    
    print_header("GENERATION COMPLETE")
    
    print("\n📊 Results Summary:")
    print("-" * 60)
    
    # Count plots per category
    categories = {
        'nested': 'Nested Metric (Cubic)',
        'generated': 'Generated SVR-SSZ',
        'additional': 'Additional Validation',
        'comparison': 'Model Comparison',
        'paper': 'Paper-Conform (Piecewise)'
    }
    
    total_plots = 0
    success_count = 0
    
    for key, name in categories.items():
        count = count_plots(key)
        status = "✓" if results.get(key, False) else "✗"
        print(f"  {status} {name:35s} {count:3d} plots")
        total_plots += count
        if results.get(key, False):
            success_count += 1
    
    print("-" * 60)
    print(f"  TOTAL:                              {total_plots:3d} plots")
    print(f"  Success Rate:                       {success_count}/{total_steps} ({100*success_count/total_steps:.0f}%)")
    
    # Time statistics
    print(f"\n⏱ Time Statistics:")
    print("-" * 60)
    print(f"  Start:    {start_time.strftime('%H:%M:%S')}")
    print(f"  End:      {end_time.strftime('%H:%M:%S')}")
    print(f"  Duration: {duration.total_seconds():.1f} seconds ({duration.total_seconds()/60:.1f} minutes)")
    
    # Output locations
    print(f"\n📁 Output Locations:")
    print("-" * 60)
    for key in categories.keys():
        path = PLOTS_DIR / key
        if path.exists():
            print(f"  {path}")
    
    # Documentation
    print(f"\n📚 Documentation:")
    print("-" * 60)
    docs = [
        'plots/README_PLOTS.md',
        'plots/FORMULAS_REFERENCE.md',
        'COMPATIBILITY_ANALYSIS_CUBIC_VS_PAPER.md'
    ]
    for doc in docs:
        doc_path = BASE_PATH / doc
        if doc_path.exists():
            print(f"  ✓ {doc}")
        else:
            print(f"  ✗ {doc} (not found)")
    
    # Generator scripts (for reference)
    print(f"\n🔧 Generator Scripts (for individual use):")
    print("-" * 60)
    scripts = [
        ('nested_ssz_metric_standalone.py', 'Nested plots'),
        ('generate_local_plots.py', 'SVR-SSZ plots'),
        ('generate_validation_plots_compact.py', 'Standalone validation plots (61 self-contained)'),
        ('generate_comparison_plots.py', 'Comparison plots'),
        ('generate_all_test_repo_plots.py', 'ECHTE Test-Repo Plots (100+ aus 3 Repos)'),
        ('generate_paper_plots.py', 'Paper plots')
    ]
    for script, desc in scripts:
        script_path = BASE_PATH / script
        if script_path.exists():
            print(f"  ✓ {script:40s} → {desc}")
    
    # Final message
    print("\n" + "="*80)
    if success_count == total_steps:
        print("  🎉 ALL PLOTS GENERATED SUCCESSFULLY!")
    else:
        print(f"  ⚠ {total_steps - success_count} step(s) failed. Check output above for details.")
    print("="*80)
    
    # Return exit code
    return 0 if success_count == total_steps else 1

# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\n⚠ Generation interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n✗ Fatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
