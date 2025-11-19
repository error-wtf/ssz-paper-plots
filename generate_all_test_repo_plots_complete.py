#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
COMPLETE TEST-REPO PLOTS GENERATOR
===================================
Führt ALLE Python-Scripts aus den Test-Repos aus (STILL) und sammelt ALLE Plots.

© 2025 Carmen Wrede, Lino Casu, Bingsi
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
"""
import os, sys
from pathlib import Path
import subprocess
import shutil

os.environ['PYTHONIOENCODING'] = 'utf-8:replace'
if sys.platform == 'win32':
    try: sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except: pass

BASE_PATH = Path(__file__).parent
OUTPUT_DIR = BASE_PATH / "plots" / "additional"

REPO1 = Path(r"E:\clone\Segmented-Spacetime-Mass-Projection-Unified-Results")
REPO2 = Path(r"E:\clone\g79-cygnus-test")
REPO3 = Path(r"E:\clone\ssz-metric-pure")

def run_silent(script_path, cwd, timeout=120):
    """Führt Script STILL aus (keine Console-Ausgabe)"""
    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            cwd=str(cwd),
            capture_output=True,  # STILL!
            text=True,
            encoding='utf-8',
            errors='replace',
            timeout=timeout
        )
        return result.returncode == 0
    except:
        return False

def collect_all_pngs(repo_path, output_dir):
    """Sammelt ALLE PNGs rekursiv"""
    collected = 0
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for png_file in repo_path.rglob('*.png'):
        if '.venv' in str(png_file) or '__pycache__' in str(png_file):
            continue
        try:
            # Eindeutiger Name mit Pfad-Prefix
            rel_path = png_file.relative_to(repo_path)
            dest_name = str(rel_path).replace('\\', '_').replace('/', '_')
            dest = output_dir / dest_name
            shutil.copy(png_file, dest)
            collected += 1
        except:
            pass
    return collected

def main():
    print("\n" + "="*80)
    print("COMPLETE TEST-REPO PLOTS - ALLE TESTS STILL AUSFÜHREN")
    print("="*80)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    total_scripts = 0
    total_success = 0
    total_plots = 0
    
    # REPO 1: Unified Results
    print(f"\n[1/3] UNIFIED RESULTS - Alle Python-Scripts")
    print("-" * 60)
    if REPO1.exists():
        # Root-level Scripts
        for script in REPO1.glob('*.py'):
            if script.name.startswith('test_') or 'validation' in script.name.lower() or 'generate' in script.name.lower():
                total_scripts += 1
                print(f"  {script.name[:50]:50s}", end='', flush=True)
                if run_silent(script, REPO1):
                    print(" ✓")
                    total_success += 1
                else:
                    print(" ✗")
        
        # tests/ Verzeichnis
        tests_dir = REPO1 / "tests"
        if tests_dir.exists():
            for script in tests_dir.rglob('test_*.py'):
                total_scripts += 1
                print(f"  {script.name[:50]:50s}", end='', flush=True)
                if run_silent(script, REPO1):
                    print(" ✓")
                    total_success += 1
                else:
                    print(" ✗")
        
        # scripts/tests/ Verzeichnis
        scripts_tests = REPO1 / "scripts" / "tests"
        if scripts_tests.exists():
            for script in scripts_tests.rglob('test_*.py'):
                total_scripts += 1
                print(f"  {script.name[:50]:50s}", end='', flush=True)
                if run_silent(script, REPO1):
                    print(" ✓")
                    total_success += 1
                else:
                    print(" ✗")
        
        print(f"\n  Sammle alle PNGs...")
        plots = collect_all_pngs(REPO1, OUTPUT_DIR / "unified-results")
        print(f"  ✓ {plots} plots gesammelt")
        total_plots += plots
    
    # REPO 2: G79-Cygnus
    print(f"\n[2/3] G79-CYGNUS - Alle Python-Scripts")
    print("-" * 60)
    if REPO2.exists():
        for script in REPO2.rglob('*.py'):
            if script.name.startswith('TEST_') or script.name.startswith('COMPLETE_') or script.name.startswith('GENERATE_'):
                total_scripts += 1
                print(f"  {script.name[:50]:50s}", end='', flush=True)
                if run_silent(script, REPO2, timeout=600):
                    print(" ✓")
                    total_success += 1
                else:
                    print(" ✗")
        
        print(f"\n  Sammle alle PNGs...")
        plots = collect_all_pngs(REPO2, OUTPUT_DIR / "g79-cygnus")
        print(f"  ✓ {plots} plots gesammelt")
        total_plots += plots
    
    # REPO 3: SSZ-Metric-Pure
    print(f"\n[3/3] SSZ-METRIC-PURE - Alle Python-Scripts")
    print("-" * 60)
    if REPO3.exists():
        for script in REPO3.rglob('*.py'):
            if 'test' in script.name.lower() or 'validate' in script.name.lower() or 'generate' in script.name.lower():
                total_scripts += 1
                print(f"  {script.name[:50]:50s}", end='', flush=True)
                if run_silent(script, REPO3):
                    print(" ✓")
                    total_success += 1
                else:
                    print(" ✗")
        
        print(f"\n  Sammle alle PNGs...")
        plots = collect_all_pngs(REPO3, OUTPUT_DIR / "ssz-metric-pure")
        print(f"  ✓ {plots} plots gesammelt")
        total_plots += plots
    
    print("\n" + "="*80)
    print("COMPLETE")
    print("="*80)
    print(f"\n  Scripts ausgeführt:  {total_scripts}")
    print(f"  Scripts erfolgreich: {total_success}")
    print(f"  Plots gesammelt:     {total_plots}")
    print(f"\n  Output: {OUTPUT_DIR}")
    print("="*80)
    
    return total_plots

if __name__ == "__main__":
    try:
        plots = main()
        sys.exit(0 if plots > 0 else 1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
