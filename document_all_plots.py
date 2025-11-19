#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plot Documentation Generator
=============================
Automatically generates complete documentation for EVERY plot.

For each plot creates:
- Title & Description
- Physical quantities shown
- Calculations/Methods
- Interpretation
- Use cases
- Technical details (size, format, etc.)

© 2025 Carmen Wrede, Lino Casu, Bingsi
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
"""
import os
import sys
from pathlib import Path
from datetime import datetime
from PIL import Image
import re

# UTF-8 encoding
os.environ['PYTHONIOENCODING'] = 'utf-8:replace'
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except:
        pass

# Plot metadata extraction patterns
PHYSICS_PATTERNS = {
    'ppn': ['PPN', 'β', 'γ', 'post-newtonian'],
    'shadow': ['shadow', 'photon sphere', 'r_ph', 'impact parameter'],
    'qnm': ['QNM', 'quasi-normal', 'frequency', 'ringdown'],
    'energy': ['energy condition', 'WEC', 'DEC', 'SEC', 'stress-energy'],
    'proper_time': ['proper time', 'time dilation', 'dτ/dt'],
    'metric': ['metric', 'A(r)', 'g_μν', 'schwarzschild'],
    'stability': ['stability', 'bomb', 'perturbation'],
    'phi': ['φ', 'golden ratio', '1.618', 'phi'],
    'temperature': ['temperature', 'T(r)', 'thermal'],
    'velocity': ['velocity', 'v(r)', 'expansion'],
    'curvature': ['curvature', 'Ricci', 'Kretschmann', 'R_μν'],
    'eso': ['ESO', 'breakthrough', 'data quality'],
    'g79': ['G79', 'nebula', 'cygnus'],
    'validation': ['validation', 'test', 'comparison'],
    'regime': ['regime', 'stratification', 'radius'],
}

PLOT_CATEGORIES = {
    'stability': {
        'name': 'Stability Analysis',
        'description': 'Black hole stability tests and bomb scenarios'
    },
    'validation': {
        'name': 'Validation Tests',
        'description': 'PPN, Shadow, QNM, Energy Conditions validation'
    },
    'g79': {
        'name': 'G79.29+0.46 Nebula',
        'description': 'Temperature, velocity, and multi-shell analysis'
    },
    'analysis': {
        'name': 'Performance Analysis',
        'description': 'Regime analysis, φ-geometry impact, stratification'
    },
    'eso': {
        'name': 'ESO Breakthrough',
        'description': 'Professional spectroscopy validation results'
    },
    'g79-temp': {
        'name': 'G79 Temperature Equations',
        'description': 'Complete temperature equation test suite'
    },
}

class PlotDocumenter:
    def __init__(self, plot_dir):
        self.plot_dir = Path(plot_dir)
        self.docs = {}
        
    def extract_physics_from_name(self, filename):
        """Extract physics topics from filename"""
        topics = []
        filename_lower = filename.lower()
        
        for topic, keywords in PHYSICS_PATTERNS.items():
            if any(kw.lower() in filename_lower for kw in keywords):
                topics.append(topic)
        
        return topics
    
    def analyze_plot(self, plot_path):
        """Analyze single plot and extract metadata"""
        info = {
            'filename': plot_path.name,
            'path': str(plot_path.relative_to(self.plot_dir)),
            'category': plot_path.parent.name,
            'physics_topics': self.extract_physics_from_name(plot_path.name),
        }
        
        # Image metadata
        try:
            with Image.open(plot_path) as img:
                info['dimensions'] = f"{img.width}x{img.height}"
                info['format'] = img.format
                info['mode'] = img.mode
                info['dpi'] = img.info.get('dpi', (72, 72))
        except Exception as e:
            info['dimensions'] = 'Unknown'
            info['format'] = 'Unknown'
        
        # File size
        size_kb = plot_path.stat().st_size / 1024
        info['size_kb'] = f"{size_kb:.1f}"
        
        return info
    
    def generate_plot_description(self, info):
        """Generate detailed description for plot"""
        filename = info['filename']
        topics = info['physics_topics']
        
        # Generate title
        title = filename.replace('_', ' ').replace('.png', '').title()
        
        # Generate description based on topics
        descriptions = []
        
        if 'ppn' in topics:
            descriptions.append("Shows Post-Newtonian parameters β and γ, validating weak-field limit compatibility with General Relativity.")
        
        if 'shadow' in topics:
            descriptions.append("Displays black hole shadow radius predictions across different mass ranges, comparing SSZ with GR.")
        
        if 'qnm' in topics:
            descriptions.append("Illustrates quasi-normal mode frequencies for black hole ringdown, showing SSZ metric predictions.")
        
        if 'energy' in topics:
            descriptions.append("Tests energy conditions (WEC, DEC, SEC) for the effective stress-energy tensor derived from the SSZ metric.")
        
        if 'proper_time' in topics:
            descriptions.append("Shows proper time dilation factor dτ/dt as function of radius, demonstrating finite behavior at r→0.")
        
        if 'stability' in topics:
            descriptions.append("Analyzes black hole stability via segment density, resonance maps, and energy evolution in bomb scenarios.")
        
        if 'phi' in topics:
            descriptions.append("Demonstrates φ (golden ratio) geometric foundations and their impact on model performance.")
        
        if 'temperature' in topics:
            descriptions.append("Shows temperature profiles and dual-frame effects in segmented spacetime for nebular structures.")
        
        if 'g79' in topics:
            descriptions.append("Analyzes G79.29+0.46 nebula observations using segmented spacetime framework.")
        
        if 'eso' in topics:
            descriptions.append("Presents ESO professional spectroscopy validation results showing 97.9% predictive accuracy.")
        
        if 'regime' in topics:
            descriptions.append("Shows performance stratification across physical regimes (photon sphere, high velocity, weak field).")
        
        if not descriptions:
            descriptions.append("Visualization of SSZ metric properties and validation results.")
        
        return {
            'title': title,
            'description': ' '.join(descriptions)
        }
    
    def generate_physics_section(self, info):
        """Generate physics quantities section"""
        topics = info['physics_topics']
        quantities = []
        
        if 'ppn' in topics:
            quantities.extend([
                "**β (PPN parameter)**: Preferred-frame effects",
                "**γ (PPN parameter)**: Space curvature",
                "**U = GM/(rc²)**: Gravitational potential"
            ])
        
        if 'shadow' in topics:
            quantities.extend([
                "**b/r_s**: Shadow radius (normalized)",
                "**r_ph**: Photon sphere radius",
                "**M**: Black hole mass"
            ])
        
        if 'qnm' in topics:
            quantities.extend([
                "**ω_R**: Real frequency (Hz)",
                "**l**: Angular momentum mode",
                "**M**: Black hole mass"
            ])
        
        if 'energy' in topics:
            quantities.extend([
                "**ρ**: Energy density (kg/m³)",
                "**p_r**: Radial pressure (Pa)",
                "**p_t**: Tangential pressure (Pa)"
            ])
        
        if 'proper_time' in topics:
            quantities.extend([
                "**dτ/dt**: Proper time factor",
                "**A(r)**: Metric function",
                "**r/r_s**: Normalized radius"
            ])
        
        if 'stability' in topics:
            quantities.extend([
                "**Ξ(r)**: Segment density",
                "**ω(r)**: Resonance frequency",
                "**E/E₀**: Normalized energy"
            ])
        
        if 'phi' in topics:
            quantities.extend([
                "**φ = (1+√5)/2**: Golden ratio ≈ 1.618",
                "**Win Rate**: Prediction success (%)",
                "**Impact (pp)**: Percentage point difference"
            ])
        
        if 'temperature' in topics:
            quantities.extend([
                "**T(r)**: Temperature (K)",
                "**γ_seg(r)**: Temporal density",
                "**u**: Energy density"
            ])
        
        return quantities if quantities else ["**Various SSZ metric quantities**"]
    
    def generate_calculations_section(self, info):
        """Generate calculations/methods section"""
        topics = info['physics_topics']
        methods = []
        
        if 'ppn' in topics:
            methods.append("Post-Newtonian expansion: A(U) = 1 - 2U + 2U² + ε₃U³")
        
        if 'shadow' in topics:
            methods.append("Photon sphere: r_ph = 1.5r_s (GR) vs 1.55r_s (SSZ)")
            methods.append("Shadow radius: b = r_ph√(1/A(r_ph))")
        
        if 'qnm' in topics:
            methods.append("Eikonal approximation for quasi-normal modes")
            methods.append("Frequency: ω = c/r_ph with SSZ correction")
        
        if 'energy' in topics:
            methods.append("Einstein field equations: G_μν = 8πT_μν")
            methods.append("Effective stress-energy from metric derivatives")
        
        if 'stability' in topics:
            methods.append("Segment density: Ξ(r) = Ξ_max(1 - exp(-φr/r_s))")
            methods.append("Bomb evolution: E_{t+1} = E_t(1 + λ - λ²K²)")
        
        if 'phi' in topics:
            methods.append("φ-based kernel: K(r) ~ exp(-φr/r_c)")
            methods.append("Statistical validation: binomial test, χ² analysis")
        
        if 'temperature' in topics:
            methods.append("T(r) = T₀ · γ_seg(r)")
            methods.append("Dual frame: T_obs = T_local / γ_seg")
        
        return methods if methods else ["Standard SSZ metric calculations"]
    
    def generate_interpretation(self, info):
        """Generate interpretation section"""
        topics = info['physics_topics']
        interpretations = []
        
        if 'ppn' in topics:
            interpretations.append("SSZ matches GR in weak-field limit (β=γ=1), ensuring compatibility with Solar System tests.")
        
        if 'shadow' in topics:
            interpretations.append("SSZ predicts slightly larger shadow radius than GR, potentially observable with Event Horizon Telescope.")
        
        if 'energy' in topics:
            interpretations.append("Energy conditions satisfied for r ≥ 5r_s, demonstrating physical validity of effective geometry.")
        
        if 'stability' in topics:
            interpretations.append("Stability criterion λ < 1/K² prevents superradiant instabilities via φ-based saturation.")
        
        if 'phi' in topics:
            interpretations.append("φ (golden ratio) emerges as fundamental geometric parameter, not arbitrary fitting constant.")
        
        if 'eso' in topics:
            interpretations.append("97.9% accuracy with professional spectroscopy validates model with highest-quality data.")
        
        return interpretations if interpretations else ["Demonstrates key SSZ metric properties and predictions."]
    
    def generate_use_cases(self, info):
        """Generate use cases section"""
        topics = info['physics_topics']
        uses = []
        
        if any(t in topics for t in ['ppn', 'shadow', 'qnm', 'energy']):
            uses.extend([
                "Paper figures for observational predictions",
                "Comparison with experimental constraints"
            ])
        
        if 'validation' in topics or 'eso' in topics:
            uses.extend([
                "Validation documentation",
                "Data quality assessment"
            ])
        
        if any(t in topics for t in ['g79', 'temperature']):
            uses.extend([
                "Nebula analysis application",
                "Temperature structure interpretation"
            ])
        
        if 'phi' in topics or 'regime' in topics:
            uses.extend([
                "Statistical analysis visualization",
                "Performance assessment"
            ])
        
        uses.extend([
            "Educational material",
            "Presentation graphics"
        ])
        
        return uses
    
    def document_plot(self, plot_path):
        """Generate complete documentation for single plot"""
        info = self.analyze_plot(plot_path)
        desc_info = self.generate_plot_description(info)
        
        doc = {
            'filename': info['filename'],
            'path': info['path'],
            'category': PLOT_CATEGORIES.get(info['category'], {}).get('name', info['category']),
            'title': desc_info['title'],
            'description': desc_info['description'],
            'physics_quantities': self.generate_physics_section(info),
            'calculations': self.generate_calculations_section(info),
            'interpretation': self.generate_interpretation(info),
            'use_cases': self.generate_use_cases(info),
            'technical': {
                'dimensions': info['dimensions'],
                'format': info['format'],
                'size_kb': info['size_kb'],
                'topics': info['physics_topics']
            }
        }
        
        return doc
    
    def document_all(self):
        """Document all plots"""
        print("\n" + "="*80)
        print("PLOT DOCUMENTATION GENERATOR")
        print("="*80)
        print(f"Directory: {self.plot_dir}")
        print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        plot_files = list(self.plot_dir.rglob('*.png'))
        print(f"\nFound {len(plot_files)} plots")
        print("\nGenerating documentation...")
        
        for i, plot_path in enumerate(plot_files, 1):
            if i % 10 == 0:
                print(f"  Progress: {i}/{len(plot_files)}")
            
            doc = self.document_plot(plot_path)
            
            category = doc['category']
            if category not in self.docs:
                self.docs[category] = []
            
            self.docs[category].append(doc)
        
        print(f"  Progress: {len(plot_files)}/{len(plot_files)} - Complete!")
        
        return self.docs
    
    def generate_markdown(self, output_path='PLOT_DOCUMENTATION.md'):
        """Generate markdown documentation"""
        lines = []
        
        lines.append("# Complete Plot Documentation\n")
        lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        lines.append(f"**Directory:** `{self.plot_dir}`\n")
        lines.append(f"**Total Plots:** {sum(len(plots) for plots in self.docs.values())}\n")
        lines.append("\n---\n")
        
        # Table of Contents
        lines.append("## Table of Contents\n")
        for i, category in enumerate(sorted(self.docs.keys()), 1):
            cat_anchor = category.lower().replace(' ', '-')
            lines.append(f"{i}. [{category}](#{cat_anchor}) ({len(self.docs[category])} plots)")
        lines.append("\n---\n")
        
        # Document each category
        for category in sorted(self.docs.keys()):
            cat_desc = PLOT_CATEGORIES.get(category, {}).get('description', '')
            
            lines.append(f"\n## {category}\n")
            if cat_desc:
                lines.append(f"*{cat_desc}*\n")
            lines.append(f"**Total plots:** {len(self.docs[category])}\n")
            lines.append("\n---\n")
            
            # Document each plot
            for plot in sorted(self.docs[category], key=lambda x: x['filename']):
                lines.append(f"\n### 📊 {plot['title']}\n")
                lines.append(f"**File:** `{plot['path']}`\n")
                lines.append(f"\n#### Description\n{plot['description']}\n")
                
                lines.append(f"\n#### Physical Quantities\n")
                for qty in plot['physics_quantities']:
                    lines.append(f"- {qty}")
                
                lines.append(f"\n\n#### Calculations & Methods\n")
                for calc in plot['calculations']:
                    lines.append(f"- {calc}")
                
                lines.append(f"\n\n#### Physical Interpretation\n")
                for interp in plot['interpretation']:
                    lines.append(f"- {interp}")
                
                lines.append(f"\n\n#### Use Cases\n")
                for use in plot['use_cases']:
                    lines.append(f"- {use}")
                
                lines.append(f"\n\n#### Technical Details\n")
                lines.append(f"- **Dimensions:** {plot['technical']['dimensions']}")
                lines.append(f"- **Format:** {plot['technical']['format']}")
                lines.append(f"- **Size:** {plot['technical']['size_kb']} KB")
                lines.append(f"- **Topics:** {', '.join(plot['technical']['topics']) if plot['technical']['topics'] else 'general'}")
                
                lines.append("\n\n---\n")
        
        lines.append("\n\n## Summary Statistics\n")
        lines.append(f"- **Total Categories:** {len(self.docs)}")
        lines.append(f"- **Total Plots:** {sum(len(plots) for plots in self.docs.values())}")
        lines.append(f"- **Average per Category:** {sum(len(plots) for plots in self.docs.values()) / len(self.docs):.1f}")
        
        lines.append("\n\n---\n")
        lines.append("\n*Documentation generated automatically from plot analysis.*\n")
        lines.append("\n© 2025 Carmen Wrede, Lino Casu, Bingsi\n")
        
        # Write documentation
        output_file = self.plot_dir.parent / output_path
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        
        print(f"\n✅ Documentation saved: {output_file}")
        return output_file

def main():
    """Main execution"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate complete plot documentation')
    parser.add_argument('--dir', default='plots/additional', help='Plot directory')
    parser.add_argument('--output', default='PLOT_DOCUMENTATION.md', help='Output filename')
    
    args = parser.parse_args()
    
    plot_dir = Path(args.dir)
    
    if not plot_dir.exists():
        print(f"❌ Error: Directory not found: {plot_dir}")
        sys.exit(1)
    
    # Generate documentation
    documenter = PlotDocumenter(plot_dir)
    docs = documenter.document_all()
    doc_path = documenter.generate_markdown(args.output)
    
    # Print summary
    print("\n" + "="*80)
    print("DOCUMENTATION COMPLETE")
    print("="*80)
    print(f"Categories:  {len(docs)}")
    print(f"Total plots: {sum(len(plots) for plots in docs.values())}")
    print(f"\n📄 Documentation: {doc_path}")
    print("="*80)

if __name__ == "__main__":
    main()
