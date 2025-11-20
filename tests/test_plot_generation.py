#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test suite for plot generation functionality

Tests:
- Single plot generation
- Plot file validation
- Image format checks
- File size validation
- Cleanup operations

© 2025 Carmen Wrede, Lino Casu
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
"""
import os
import sys
from pathlib import Path
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# UTF-8 handling
os.environ['PYTHONIOENCODING'] = 'utf-8:replace'
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except:
        pass

from generate_all_real_data_plots_master import load_real_data, find_data_directory

def test_plot_generation_basic():
    """Test 1: Basic plot generation"""
    print("\n" + "="*80)
    print("TEST 1: BASIC PLOT GENERATION")
    print("="*80)
    
    try:
        # Import specific plot module
        from plots_real_collapse_rate import generate as gen_collapse
        
        # Load data
        data = load_real_data(find_data_directory())
        
        # Create test output directory
        output_dir = Path('test_output')
        output_dir.mkdir(exist_ok=True)
        
        print(f"✓ Data loaded successfully")
        print(f"  Output directory: {output_dir.absolute()}")
        
        # Generate plot
        plot_file = gen_collapse(data, output_dir=str(output_dir))
        
        assert plot_file.exists(), f"Plot not created: {plot_file}"
        print(f"✓ Plot file created: {plot_file.name}")
        
        # Validate file
        assert plot_file.suffix == '.png', f"Wrong format: {plot_file.suffix}"
        print(f"  Format: PNG ✓")
        
        file_size = plot_file.stat().st_size
        assert file_size > 1000, f"File too small: {file_size} bytes"
        print(f"  Size: {file_size:,} bytes ✓")
        
        # Cleanup
        plot_file.unlink()
        output_dir.rmdir()
        print(f"✓ Cleanup complete")
        
        print("="*80)
        return True
        
    except Exception as e:
        print(f"✗ FAILED: {e}")
        print("="*80)
        # Cleanup on failure
        try:
            if plot_file.exists():
                plot_file.unlink()
            if output_dir.exists():
                output_dir.rmdir()
        except:
            pass
        return False

def test_multiple_plots():
    """Test 2: Generate multiple plots"""
    print("\n" + "="*80)
    print("TEST 2: MULTIPLE PLOT GENERATION")
    print("="*80)
    
    try:
        # Import plot modules
        from plots_real_collapse_rate import generate as gen1
        from plots_real_coherence import generate as gen2
        
        data = load_real_data(find_data_directory())
        output_dir = Path('test_output')
        output_dir.mkdir(exist_ok=True)
        
        print(f"✓ Generating multiple plots...")
        
        # Generate plots
        plot1 = gen1(data, output_dir=str(output_dir))
        plot2 = gen2(data, output_dir=str(output_dir))
        
        assert plot1.exists(), "Plot 1 not created"
        assert plot2.exists(), "Plot 2 not created"
        
        print(f"  ✓ Plot 1: {plot1.name}")
        print(f"  ✓ Plot 2: {plot2.name}")
        
        # Cleanup
        plot1.unlink()
        plot2.unlink()
        output_dir.rmdir()
        
        print("✓ Multiple plots generated successfully")
        print("="*80)
        return True
        
    except Exception as e:
        print(f"✗ FAILED: {e}")
        print("="*80)
        # Cleanup
        try:
            for f in output_dir.glob('*.png'):
                f.unlink()
            output_dir.rmdir()
        except:
            pass
        return False

def test_plot_dimensions():
    """Test 3: Validate plot dimensions"""
    print("\n" + "="*80)
    print("TEST 3: PLOT DIMENSIONS VALIDATION")
    print("="*80)
    
    try:
        from PIL import Image
        from plots_real_collapse_rate import generate as gen_collapse
        
        data = load_real_data(find_data_directory())
        output_dir = Path('test_output')
        output_dir.mkdir(exist_ok=True)
        
        # Generate plot
        plot_file = gen_collapse(data, output_dir=str(output_dir))
        
        # Check dimensions
        img = Image.open(plot_file)
        width, height = img.size
        
        print(f"✓ Plot dimensions: {width}×{height} px")
        
        # Reasonable size checks
        assert width >= 800, f"Width too small: {width}"
        assert height >= 400, f"Height too small: {height}"
        assert width <= 3000, f"Width too large: {width}"
        assert height <= 3000, f"Height too large: {height}"
        
        print(f"  ✓ Dimensions within acceptable range")
        
        # Cleanup
        plot_file.unlink()
        output_dir.rmdir()
        
        print("="*80)
        return True
        
    except ImportError:
        print("⚠️  PIL not available, skipping dimension check")
        print("="*80)
        return True  # Don't fail if PIL missing
    except Exception as e:
        print(f"✗ FAILED: {e}")
        print("="*80)
        try:
            plot_file.unlink()
            output_dir.rmdir()
        except:
            pass
        return False

if __name__ == '__main__':
    print("\n" + "="*80)
    print("SSZ PAPER PLOTS - PLOT GENERATION TEST SUITE")
    print("="*80)
    
    results = []
    results.append(("Basic Plot Generation", test_plot_generation_basic()))
    results.append(("Multiple Plots", test_multiple_plots()))
    results.append(("Plot Dimensions", test_plot_dimensions()))
    
    # Summary
    print("\n" + "="*80)
    print("TEST SUMMARY")
    print("="*80)
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status}: {name}")
    
    print(f"\nResults: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 ALL TESTS PASSED!")
        sys.exit(0)
    else:
        print(f"\n⚠️  {total - passed} test(s) failed")
        sys.exit(1)
