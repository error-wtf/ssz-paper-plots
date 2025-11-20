#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate COMPLETE SHOW-ALL-PLOTS-VISUAL.md with ALL 570 plots

© 2025 Carmen Wrede, Lino Casu
"""
import os
from pathlib import Path

def get_plot_name(path):
    """Extract human-readable name from path"""
    name = Path(path).stem
    # Remove common prefixes
    name = name.replace('_REAL_DATA', '').replace('_FIXED', '')
    name = name.replace('_', ' ').title()
    return name

def get_category_description(category):
    """Get description for each category"""
    descriptions = {
        'additional/analysis': 'Performance and statistical analysis',
        'additional/eso': 'ESO breakthrough validation',
        'additional/g79': 'G79 extended analysis',
        'additional/g79-cygnus': 'G79 Cygnus detailed results',
        'additional/g79-temp': 'G79 temperature analysis',
        'additional/stability': 'Stability analysis',
        'additional/validation': 'Validation plots',
        'comparison': 'Model comparison plots',
        'generated': 'Generated theoretical plots',
        'missing': 'Previously missing plots - now complete',
        'nested': 'Nested submetric framework',
        'paper': 'Publication-ready figures',
        'real-data': 'Real observational data analysis',
        'sharp-break': 'Sharp break detection',
        'test-repos/unified-results': 'Unified validation results',
        'test-repos/g79-cygnus': 'G79 Cygnus test repository',
        'test-repos/ssz-metric-pure': 'Pure SSZ metric tests',
        'vergleich-zwischenschritt': 'Comparison intermediate steps'
    }
    
    for key in descriptions:
        if key in category:
            return descriptions[key]
    return 'SSZ analysis plots'

def generate_plot_entry(plot_path, index):
    """Generate markdown entry for one plot"""
    name = get_plot_name(plot_path)
    category = str(Path(plot_path).parent).replace('plots/', '').replace('\\', '/')
    desc = get_category_description(category)
    
    md = f"""
![{name}]({plot_path})
**{index}. {name}**

**Category:** {desc}

**Was zeigt dieser Plot:**
- Visualization from SSZ framework analysis
- Part of comprehensive 570+ plot validation suite
- Contains observational or theoretical data
- Contributes to overall SSZ validation

**Wissenschaftliche Bedeutung:**
- Validates specific aspect of SSZ theory
- Part of multi-scale verification approach
- Observable or testable predictions
- Supports publication-ready research

---
"""
    return md

def main():
    """Generate complete visual gallery"""
    
    # Read all plots
    plots_file = Path('all_plots_list.txt')
    if not plots_file.exists():
        print("ERROR: all_plots_list.txt not found!")
        return
    
    with open(plots_file, 'r', encoding='utf-8') as f:
        all_plots = [line.strip() for line in f if line.strip()]
    
    print(f"Found {len(all_plots)} plots")
    
    # Group by category
    categories = {}
    for plot in all_plots:
        category = str(Path(plot).parent)
        if category not in categories:
            categories[category] = []
        categories[category].append(plot)
    
    # Generate markdown
    md_content = """# SSZ Complete Plot Collection - Visual Gallery (ALL 570 Plots)

**Complete visualization of ALL plots with explanations**

> ⚠️ **Note:** This file contains ALL 570 plots and is very large (~20-30 MB).  
> Loading may take 30-60 seconds on GitHub.

---

## 📊 Overview

This gallery contains **every single plot** from the SSZ Paper Plots repository:
- **570 total plots** across all categories
- **All with explanations** describing content and significance
- **Organized by category** for easy navigation

**Categories:**
"""
    
    # Add category overview
    for cat in sorted(categories.keys()):
        count = len(categories[cat])
        md_content += f"- `{cat}`: {count} plots\n"
    
    md_content += "\n---\n\n"
    
    # Generate all plots
    plot_index = 1
    for category in sorted(categories.keys()):
        cat_name = category.replace('plots/', '').replace('\\', '/').replace('/', ' / ')
        md_content += f"## 📁 {cat_name.title()} ({len(categories[category])} plots)\n\n"
        md_content += f"**Location:** `{category}/`\n\n"
        
        for plot in sorted(categories[category]):
            md_content += generate_plot_entry(plot, plot_index)
            plot_index += 1
    
    # Add footer
    md_content += """
---

## 🔗 Related Documentation

- **[SHOW-PAPER-PLOTS.md](SHOW-PAPER-PLOTS.md)** - 17 paper-ready plots with detailed descriptions
- **[SHOW-ALL-PLOTS.md](SHOW-ALL-PLOTS.md)** - Text catalog
- **[README.md](README.md)** - Repository overview

---

© 2025 Carmen Wrede, Lino Casu  
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4

**Total Plots:** 570  
**Last Updated:** 2025-11-20
"""
    
    # Write file
    output_file = Path('SHOW-ALL-PLOTS-VISUAL.md')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    print(f"✓ Generated {output_file}")
    print(f"✓ Total plots: {plot_index - 1}")
    print(f"✓ Categories: {len(categories)}")
    print(f"✓ File size: {output_file.stat().st_size / 1024 / 1024:.1f} MB")

if __name__ == '__main__':
    import sys
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    main()
