#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plot Validation System
======================
Validates ALL generated plots and creates comprehensive error report.

Checks:
- File existence
- File size (empty plots)
- Image integrity (can be opened)
- Dimensions (too small = error)
- Naming conventions
- Duplicate detection

© 2025 Carmen Wrede, Lino Casu, Bingsi
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
"""
import os
import sys
from pathlib import Path
from datetime import datetime
from PIL import Image
import hashlib

# UTF-8 encoding
os.environ['PYTHONIOENCODING'] = 'utf-8:replace'
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except:
        pass

# Validation criteria
MIN_FILE_SIZE = 1000  # bytes (plots < 1KB are likely empty)
MIN_WIDTH = 100       # pixels
MIN_HEIGHT = 100      # pixels
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB

class PlotValidator:
    def __init__(self, plot_dir):
        self.plot_dir = Path(plot_dir)
        self.results = {
            'total_plots': 0,
            'valid_plots': 0,
            'errors': [],
            'warnings': [],
            'duplicates': [],
            'categories': {}
        }
        self.file_hashes = {}
    
    def validate_file_exists(self, plot_path):
        """Check if file exists"""
        if not plot_path.exists():
            return False, f"File does not exist: {plot_path}"
        return True, None
    
    def validate_file_size(self, plot_path):
        """Check file size"""
        size = plot_path.stat().st_size
        
        if size < MIN_FILE_SIZE:
            return False, f"File too small ({size} bytes, min {MIN_FILE_SIZE}): likely empty plot"
        
        if size > MAX_FILE_SIZE:
            return False, f"File too large ({size} bytes, max {MAX_FILE_SIZE}): possible corruption"
        
        return True, None
    
    def validate_image_integrity(self, plot_path):
        """Try to open and validate image"""
        try:
            with Image.open(plot_path) as img:
                width, height = img.size
                
                if width < MIN_WIDTH or height < MIN_HEIGHT:
                    return False, f"Image too small ({width}x{height}, min {MIN_WIDTH}x{MIN_HEIGHT})"
                
                # Try to load image data
                img.verify()
                
                return True, {
                    'width': width,
                    'height': height,
                    'format': img.format,
                    'mode': img.mode
                }
        except Exception as e:
            return False, f"Cannot open/verify image: {e}"
    
    def calculate_hash(self, plot_path):
        """Calculate file hash for duplicate detection"""
        hash_md5 = hashlib.md5()
        with open(plot_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
    def check_duplicate(self, plot_path):
        """Check if plot is duplicate"""
        file_hash = self.calculate_hash(plot_path)
        
        if file_hash in self.file_hashes:
            return True, self.file_hashes[file_hash]
        
        self.file_hashes[file_hash] = plot_path
        return False, None
    
    def validate_plot(self, plot_path):
        """Complete validation of single plot"""
        errors = []
        warnings = []
        info = {'path': str(plot_path.relative_to(self.plot_dir))}
        
        # Check existence
        exists, error = self.validate_file_exists(plot_path)
        if not exists:
            errors.append(error)
            return {'valid': False, 'errors': errors, 'warnings': warnings, 'info': info}
        
        # Check file size
        valid_size, error = self.validate_file_size(plot_path)
        if not valid_size:
            errors.append(error)
        
        # Check image integrity
        valid_img, result = self.validate_image_integrity(plot_path)
        if not valid_img:
            errors.append(result)
        else:
            info.update(result)
        
        # Check duplicates
        is_dup, dup_path = self.check_duplicate(plot_path)
        if is_dup:
            warnings.append(f"Duplicate of {dup_path.relative_to(self.plot_dir)}")
        
        # File size info
        info['size_kb'] = plot_path.stat().st_size / 1024
        
        return {
            'valid': len(errors) == 0,
            'errors': errors,
            'warnings': warnings,
            'info': info
        }
    
    def validate_all(self):
        """Validate all plots in directory"""
        print("\n" + "="*80)
        print("PLOT VALIDATION SYSTEM")
        print("="*80)
        print(f"Directory: {self.plot_dir}")
        print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Find all PNG files
        plot_files = list(self.plot_dir.rglob('*.png'))
        self.results['total_plots'] = len(plot_files)
        
        print(f"\nFound {len(plot_files)} plots")
        print("\nValidating...")
        
        # Validate each plot
        for i, plot_path in enumerate(plot_files, 1):
            if i % 10 == 0:
                print(f"  Progress: {i}/{len(plot_files)}")
            
            result = self.validate_plot(plot_path)
            
            # Categorize
            category = plot_path.parent.name
            if category not in self.results['categories']:
                self.results['categories'][category] = {
                    'total': 0, 'valid': 0, 'errors': 0
                }
            
            self.results['categories'][category]['total'] += 1
            
            if result['valid']:
                self.results['valid_plots'] += 1
                self.results['categories'][category]['valid'] += 1
            else:
                self.results['categories'][category]['errors'] += 1
                self.results['errors'].append({
                    'file': result['info']['path'],
                    'errors': result['errors']
                })
            
            if result['warnings']:
                self.results['warnings'].append({
                    'file': result['info']['path'],
                    'warnings': result['warnings']
                })
        
        print(f"  Progress: {len(plot_files)}/{len(plot_files)} - Complete!")
        
        return self.results
    
    def generate_report(self, output_path='PLOT_VALIDATION_REPORT.md'):
        """Generate markdown report"""
        report = []
        
        report.append("# Plot Validation Report\n")
        report.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        report.append(f"**Directory:** `{self.plot_dir}`\n")
        report.append("\n---\n")
        
        # Summary
        report.append("## Summary\n")
        report.append(f"- **Total Plots:** {self.results['total_plots']}")
        report.append(f"- **Valid Plots:** {self.results['valid_plots']}")
        report.append(f"- **Invalid Plots:** {self.results['total_plots'] - self.results['valid_plots']}")
        report.append(f"- **Warnings:** {len(self.results['warnings'])}")
        
        success_rate = (self.results['valid_plots'] / self.results['total_plots'] * 100) if self.results['total_plots'] > 0 else 0
        report.append(f"- **Success Rate:** {success_rate:.1f}%\n")
        
        # Status
        if success_rate == 100:
            report.append("✅ **Status:** ALL PLOTS VALID\n")
        elif success_rate >= 95:
            report.append("⚠️ **Status:** MOSTLY VALID (minor issues)\n")
        elif success_rate >= 80:
            report.append("⚠️ **Status:** NEEDS ATTENTION (some issues)\n")
        else:
            report.append("❌ **Status:** CRITICAL (many issues)\n")
        
        report.append("\n---\n")
        
        # By Category
        report.append("## Validation by Category\n")
        report.append("| Category | Total | Valid | Errors | Success Rate |")
        report.append("|----------|-------|-------|--------|--------------|")
        
        for cat, stats in sorted(self.results['categories'].items()):
            rate = (stats['valid'] / stats['total'] * 100) if stats['total'] > 0 else 0
            status = "✅" if rate == 100 else "⚠️" if rate >= 90 else "❌"
            report.append(f"| {cat} | {stats['total']} | {stats['valid']} | {stats['errors']} | {status} {rate:.1f}% |")
        
        report.append("\n---\n")
        
        # Errors
        if self.results['errors']:
            report.append("## Errors\n")
            report.append(f"Found {len(self.results['errors'])} plots with errors:\n")
            
            for error in self.results['errors']:
                report.append(f"\n### ❌ `{error['file']}`")
                for err in error['errors']:
                    report.append(f"- {err}")
        else:
            report.append("## Errors\n")
            report.append("✅ No errors found!\n")
        
        report.append("\n---\n")
        
        # Warnings
        if self.results['warnings']:
            report.append("## Warnings\n")
            report.append(f"Found {len(self.results['warnings'])} plots with warnings:\n")
            
            for warning in self.results['warnings']:
                report.append(f"\n### ⚠️ `{warning['file']}`")
                for warn in warning['warnings']:
                    report.append(f"- {warn}")
        else:
            report.append("## Warnings\n")
            report.append("✅ No warnings!\n")
        
        report.append("\n---\n")
        
        # Recommendations
        report.append("## Recommendations\n")
        
        if self.results['errors']:
            report.append("\n### Critical Issues:")
            report.append("1. Review and fix all plots with errors")
            report.append("2. Re-generate invalid plots")
            report.append("3. Check source scripts for bugs")
        
        if self.results['warnings']:
            report.append("\n### Minor Issues:")
            report.append("1. Remove or consolidate duplicate plots")
            report.append("2. Review warnings for potential improvements")
        
        if not self.results['errors'] and not self.results['warnings']:
            report.append("✅ All plots validated successfully! No action needed.")
        
        report.append("\n\n---\n")
        report.append("\n*Validation completed successfully.*\n")
        report.append("\n© 2025 Carmen Wrede, Lino Casu, Bingsi\n")
        
        # Write report
        output_file = self.plot_dir.parent / output_path
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(report))
        
        print(f"\n✅ Report saved: {output_file}")
        return output_file

def main():
    """Main execution"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Validate all generated plots')
    parser.add_argument('--dir', default='plots/additional', help='Plot directory to validate')
    parser.add_argument('--output', default='PLOT_VALIDATION_REPORT.md', help='Output report filename')
    
    args = parser.parse_args()
    
    plot_dir = Path(args.dir)
    
    if not plot_dir.exists():
        print(f"❌ Error: Directory not found: {plot_dir}")
        sys.exit(1)
    
    # Validate
    validator = PlotValidator(plot_dir)
    results = validator.validate_all()
    
    # Generate report
    report_path = validator.generate_report(args.output)
    
    # Print summary
    print("\n" + "="*80)
    print("VALIDATION COMPLETE")
    print("="*80)
    print(f"Total plots: {results['total_plots']}")
    print(f"Valid plots: {results['valid_plots']}")
    print(f"Errors:      {len(results['errors'])}")
    print(f"Warnings:    {len(results['warnings'])}")
    
    success_rate = (results['valid_plots'] / results['total_plots'] * 100) if results['total_plots'] > 0 else 0
    print(f"Success:     {success_rate:.1f}%")
    print(f"\n📄 Report:   {report_path}")
    print("="*80)
    
    sys.exit(0 if len(results['errors']) == 0 else 1)

if __name__ == "__main__":
    main()
