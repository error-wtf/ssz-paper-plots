#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SSZ Additional Plots Generator V2 - STANDALONE
===============================================
Konsolidiert ALLE Plots aus den Test-Repos in standalone Module.

© 2025 Carmen Wrede, Lino Casu, Bingsi
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
"""
import os
import sys
from pathlib import Path
from datetime import datetime

os.environ['PYTHONIOENCODING'] = 'utf-8:replace'
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except:
        pass

# Import all plot modules
sys.path.insert(0, str(Path(__file__).parent))
from plots_modules import (
    ssz_stability_plots,
    ssz_validation_plots,
    g79_cygnus_plots,
    ssz_key_analysis_plots,
    ssz_eso_breakthrough_plots,
    g79_temperature_plots
)

OUTPUT_DIR = Path(__file__).parent / "plots" / "additional"

def main():
    start_time = datetime.now()
    
    print("\n" + "="*80)
    print("SSZ ADDITIONAL PLOTS GENERATOR V2 - STANDALONE")
    print("="*80)
    print(f"Output: {OUTPUT_DIR}")
    print(f"Start: {start_time.strftime('%H:%M:%S')}")
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    all_plots = []
    module_count = 0
    
    # ========================================================================
    # MODULE 1: Stability Plots (3 plots)
    # ========================================================================
    print(f"\n[1/4] SSZ STABILITY PLOTS")
    print("-" * 60)
    try:
        plots = ssz_stability_plots.generate_all(OUTPUT_DIR / "stability")
        all_plots.extend(plots)
        module_count += 1
        print(f"  ✓ Generated {len(plots)} plots")
    except Exception as e:
        print(f"  ✗ Error: {e}")
    
    # ========================================================================
    # MODULE 2: Validation Plots (~30 plots)
    # ========================================================================
    print(f"\n[2/4] SSZ VALIDATION PLOTS")
    print("-" * 60)
    try:
        plots = ssz_validation_plots.generate_all(OUTPUT_DIR / "validation")
        all_plots.extend(plots)
        module_count += 1
        print(f"  ✓ Generated {len(plots)} plots")
    except Exception as e:
        print(f"  ✗ Error: {e}")
    
    # ========================================================================
    # MODULE 3: G79 Cygnus Plots (4 plots)
    # ========================================================================
    print(f"\n[3/4] G79 CYGNUS PLOTS")
    print("-" * 60)
    try:
        plots = g79_cygnus_plots.generate_all(OUTPUT_DIR / "g79")
        all_plots.extend(plots)
        module_count += 1
        print(f"  ✓ Generated {len(plots)} plots")
    except Exception as e:
        print(f"  ✗ Error: {e}")
    
    # ========================================================================
    # MODULE 4: Key Analysis Plots (5 plots)
    # ========================================================================
    print(f"\n[4/6] KEY ANALYSIS PLOTS")
    print("-" * 60)
    try:
        plots = ssz_key_analysis_plots.generate_all(OUTPUT_DIR / "analysis")
        all_plots.extend(plots)
        module_count += 1
        print(f"  ✓ Generated {len(plots)} plots")
    except Exception as e:
        print(f"  ✗ Error: {e}")
    
    # ========================================================================
    # MODULE 5: ESO Breakthrough Plots (4 plots)
    # ========================================================================
    print(f"\n[5/6] ESO BREAKTHROUGH PLOTS")
    print("-" * 60)
    try:
        plots = ssz_eso_breakthrough_plots.generate_all(OUTPUT_DIR / "eso")
        all_plots.extend(plots)
        module_count += 1
        print(f"  ✓ Generated {len(plots)} plots")
    except Exception as e:
        print(f"  ✗ Error: {e}")
    
    # ========================================================================
    # MODULE 6: G79 Temperature Plots (5 plots)
    # ========================================================================
    print(f"\n[6/6] G79 TEMPERATURE PLOTS")
    print("-" * 60)
    try:
        plots = g79_temperature_plots.generate_all(OUTPUT_DIR / "g79-temp")
        all_plots.extend(plots)
        module_count += 1
        print(f"  ✓ Generated {len(plots)} plots")
    except Exception as e:
        print(f"  ✗ Error: {e}")
    
    # ========================================================================
    # SUMMARY
    # ========================================================================
    end_time = datetime.now()
    duration = end_time - start_time
    
    print("\n" + "="*80)
    print("GENERATION COMPLETE")
    print("="*80)
    print(f"\n📊 Summary:")
    print(f"  Modules successful:  {module_count}/6")
    print(f"  Total plots:         {len(all_plots)}")
    print(f"\n⏱ Time:")
    print(f"  Start:    {start_time.strftime('%H:%M:%S')}")
    print(f"  End:      {end_time.strftime('%H:%M:%S')}")
    print(f"  Duration: {duration.total_seconds():.1f}s")
    print(f"\n📁 Output: {OUTPUT_DIR}")
    print("="*80)
    
    return len(all_plots)

if __name__ == "__main__":
    try:
        plot_count = main()
        sys.exit(0 if plot_count > 0 else 1)
    except KeyboardInterrupt:
        print("\n\n⚠ Interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n✗ Fatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
