#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Paper-Plot Consistency Analysis
================================
Deep analysis of ALL plots regarding scientific consistency with:
"Segmented Spacetime - Infalling Matter and Radiowaves"

Key Paper Concepts:
- g₁ (weak segmentation) vs g₂ (strong segmentation)
- Finite radius core (r > 0, no singularity)
- v_total = v_fall + v_eigen (velocity decomposition)
- Radiowave emission as early signature
- Radiowave precursors before optical outflows
- Energy horizon at g₁→g₂ boundary

© 2025 Carmen Wrede, Lino Casu, Bingsi
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
"""
import os
import sys
from pathlib import Path
from datetime import datetime
import re

# UTF-8 encoding
os.environ['PYTHONIOENCODING'] = 'utf-8:replace'
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except:
        pass

# Paper concepts to check
PAPER_CONCEPTS = {
    'g1_g2_regions': {
        'keywords': ['g1', 'g2', 'weak segmentation', 'strong segmentation', 'domain', 'region'],
        'description': 'g₁ (weak) vs g₂ (strong) segmentation regions',
        'importance': 'CRITICAL',
        'required_plots': 5
    },
    'finite_radius_core': {
        'keywords': ['finite radius', 'r>0', 'no singularity', 'core radius', 'r_core'],
        'description': 'Finite radius core (r > 0), no r=0 singularity',
        'importance': 'CRITICAL',
        'required_plots': 3
    },
    'velocity_decomposition': {
        'keywords': ['v_fall', 'v_eigen', 'v_total', 'velocity', 'infall'],
        'description': 'v_total = v_fall + v_eigen decomposition',
        'importance': 'CRITICAL',
        'required_plots': 4
    },
    'radiowave_emission': {
        'keywords': ['radio', 'radiowave', 'low frequency', 'precursor'],
        'description': 'Radiowave emission as early signature',
        'importance': 'CRITICAL',
        'required_plots': 5
    },
    'energy_horizon': {
        'keywords': ['energy horizon', 'boundary', 'g1 g2', 'transition'],
        'description': 'Energy horizon at g₁→g₂ boundary',
        'importance': 'HIGH',
        'required_plots': 3
    },
    'birkhoff_theorem': {
        'keywords': ['birkhoff', 'spherical symmetry', 'exterior'],
        'description': 'Birkhoff theorem and spherical symmetry',
        'importance': 'MEDIUM',
        'required_plots': 2
    },
    'infalling_matter': {
        'keywords': ['infall', 'accretion', 'matter', 'mass'],
        'description': 'Infalling matter dynamics',
        'importance': 'HIGH',
        'required_plots': 4
    },
    'excess_energy': {
        'keywords': ['excess energy', 'kinetic', 'released', 'dissipated'],
        'description': 'Excess kinetic energy release',
        'importance': 'HIGH',
        'required_plots': 3
    },
    'temporal_effects': {
        'keywords': ['time', 'temporal', 'slowdown', 'dilation'],
        'description': 'Time slowdown in g₂ region',
        'importance': 'HIGH',
        'required_plots': 3
    },
    'observational_predictions': {
        'keywords': ['observation', 'prediction', 'jet', 'outflow', 'precursor'],
        'description': 'Observational predictions (precursors, jets)',
        'importance': 'CRITICAL',
        'required_plots': 5
    },
}

class PaperPlotAnalyzer:
    def __init__(self, plot_dir, doc_file):
        self.plot_dir = Path(plot_dir)
        self.doc_file = Path(doc_file)
        self.plots = []
        self.concept_matches = {concept: [] for concept in PAPER_CONCEPTS.keys()}
        self.missing_concepts = []
        self.inconsistencies = []
        
    def load_documentation(self):
        """Load plot documentation"""
        print("\n" + "="*80)
        print("LOADING PLOT DOCUMENTATION")
        print("="*80)
        
        with open(self.doc_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract plot entries (simplified parsing)
        plot_sections = content.split('### 📊')
        
        for section in plot_sections[1:]:  # Skip first (header)
            lines = section.split('\n')
            title = lines[0].strip()
            
            # Find file path
            file_line = [l for l in lines if l.startswith('**File:**')]
            if file_line:
                file_path = file_line[0].replace('**File:**', '').strip().strip('`')
                
                # Get full description text
                description = '\n'.join(lines).lower()
                
                self.plots.append({
                    'title': title,
                    'file': file_path,
                    'description': description
                })
        
        print(f"Loaded {len(self.plots)} plot descriptions")
        return self.plots
    
    def analyze_concept_coverage(self):
        """Analyze which paper concepts are covered by plots"""
        print("\n" + "="*80)
        print("ANALYZING CONCEPT COVERAGE")
        print("="*80)
        
        for concept_id, concept_info in PAPER_CONCEPTS.items():
            keywords = concept_info['keywords']
            matches = []
            
            for plot in self.plots:
                # Check if any keyword appears in plot description
                plot_text = plot['description'].lower()
                if any(kw.lower() in plot_text for kw in keywords):
                    matches.append(plot)
            
            self.concept_matches[concept_id] = matches
            
            # Report
            required = concept_info['required_plots']
            found = len(matches)
            status = "✅" if found >= required else "⚠️" if found > 0 else "❌"
            
            print(f"\n{status} {concept_id}:")
            print(f"   Description: {concept_info['description']}")
            print(f"   Importance: {concept_info['importance']}")
            print(f"   Required plots: {required}")
            print(f"   Found plots: {found}")
            
            if found < required:
                self.missing_concepts.append({
                    'concept': concept_id,
                    'description': concept_info['description'],
                    'importance': concept_info['importance'],
                    'required': required,
                    'found': found,
                    'gap': required - found
                })
    
    def check_scientific_consistency(self):
        """Check for scientific inconsistencies"""
        print("\n" + "="*80)
        print("CHECKING SCIENTIFIC CONSISTENCY")
        print("="*80)
        
        inconsistencies = []
        
        # Check 1: r=0 singularity plots (should NOT exist)
        r_zero_plots = []
        for plot in self.plots:
            if any(term in plot['description'] for term in ['r=0', 'r = 0', 'singularity at r=0', 'point mass']):
                r_zero_plots.append(plot)
        
        if r_zero_plots:
            inconsistencies.append({
                'type': 'CRITICAL',
                'issue': 'r=0 singularity plots found',
                'description': 'Paper argues r > 0 always. These plots may show r=0 singularities.',
                'plots': r_zero_plots
            })
        
        # Check 2: GR-only plots without SSZ comparison
        gr_only = []
        for plot in self.plots:
            if 'general relativity' in plot['description'] or 'gr' in plot['description']:
                if 'ssz' not in plot['description'] and 'segmented' not in plot['description']:
                    gr_only.append(plot)
        
        if len(gr_only) > 10:
            inconsistencies.append({
                'type': 'MEDIUM',
                'issue': f'{len(gr_only)} plots show GR without SSZ comparison',
                'description': 'Paper extends GR. Plots should show SSZ vs GR comparison.',
                'plots': gr_only[:5]  # Show first 5
            })
        
        # Check 3: High-frequency emission in g₂ (should NOT exist)
        high_freq_g2 = []
        for plot in self.plots:
            if 'g2' in plot['description'] or 'strong segmentation' in plot['description']:
                if any(term in plot['description'] for term in ['x-ray', 'optical', 'uv', 'high frequency']):
                    high_freq_g2.append(plot)
        
        if high_freq_g2:
            inconsistencies.append({
                'type': 'CRITICAL',
                'issue': 'High-frequency emission in g₂ region',
                'description': 'Paper states g₂ cannot produce high-freq radiation.',
                'plots': high_freq_g2
            })
        
        # Check 4: Radiowave emission should precede optical
        temporal_order = self.check_temporal_order()
        if temporal_order:
            inconsistencies.append(temporal_order)
        
        self.inconsistencies = inconsistencies
        
        if inconsistencies:
            print(f"\n⚠️ Found {len(inconsistencies)} potential inconsistencies")
            for inc in inconsistencies:
                print(f"\n{inc['type']}: {inc['issue']}")
                print(f"   {inc['description']}")
                print(f"   Affected plots: {len(inc.get('plots', []))}")
        else:
            print("\n✅ No scientific inconsistencies detected")
    
    def check_temporal_order(self):
        """Check if plots show correct temporal order: radio before optical"""
        # This is a simplified check
        time_series_plots = [p for p in self.plots if 'time' in p['description'] or 'evolution' in p['description']]
        
        issues = []
        for plot in time_series_plots:
            if 'radio' in plot['description'] and 'optical' in plot['description']:
                # Should show radio first
                if 'optical before radio' in plot['description'] or 'optical precedes' in plot['description']:
                    issues.append(plot)
        
        if issues:
            return {
                'type': 'CRITICAL',
                'issue': 'Temporal order violation',
                'description': 'Paper predicts radio BEFORE optical. These plots may show opposite.',
                'plots': issues
            }
        return None
    
    def generate_recommendations(self):
        """Generate recommendations for missing plots"""
        print("\n" + "="*80)
        print("RECOMMENDATIONS FOR MISSING PLOTS")
        print("="*80)
        
        if not self.missing_concepts:
            print("\n✅ All critical concepts are well-covered!")
            return
        
        # Sort by importance
        importance_order = {'CRITICAL': 0, 'HIGH': 1, 'MEDIUM': 2, 'LOW': 3}
        sorted_missing = sorted(self.missing_concepts, 
                              key=lambda x: importance_order.get(x['importance'], 999))
        
        print("\nPriority order for new plots:\n")
        
        for i, missing in enumerate(sorted_missing, 1):
            print(f"{i}. [{missing['importance']}] {missing['concept']}")
            print(f"   Description: {missing['description']}")
            print(f"   Gap: {missing['gap']} plots needed (have {missing['found']}, need {missing['required']})")
            print(f"   Recommended plots:")
            
            # Generate specific recommendations
            recommendations = self.get_plot_recommendations(missing['concept'])
            for j, rec in enumerate(recommendations, 1):
                print(f"      {j}) {rec}")
            print()
    
    def get_plot_recommendations(self, concept_id):
        """Get specific plot recommendations for concept"""
        recommendations = {
            'g1_g2_regions': [
                "Segmentation field comparison: g₁ vs g₂ domains",
                "Spacetime density: radial profile showing g₁→g₂ transition",
                "Time dilation factor across g₁-g₂ boundary",
                "Energy density map showing two regions",
                "Matter trajectory through g₁→g₂ transition"
            ],
            'finite_radius_core': [
                "Core radius vs mass relation (r_core > 0 always)",
                "Interior geometry: no r=0 singularity",
                "Density profile with finite core",
                "Comparison: SSZ (r>0) vs GR (r→0)"
            ],
            'velocity_decomposition': [
                "v_total = v_fall + v_eigen decomposition diagram",
                "Velocity components vs radius",
                "Excess velocity (v_eigen) at g₁-g₂ boundary",
                "Impact velocity analysis"
            ],
            'radiowave_emission': [
                "Radiowave spectrum from excess energy",
                "Frequency distribution (radio-dominant)",
                "Radiowave precursor timeline",
                "Radio intensity vs infall velocity",
                "Multi-frequency light curve (radio first)"
            ],
            'energy_horizon': [
                "Energy horizon location (g₁→g₂ boundary)",
                "Energy absorption/release at boundary",
                "Matter-energy flow diagram"
            ],
            'observational_predictions': [
                "Radiowave precursor before jet formation",
                "Timeline: radio → X-ray → optical",
                "Predicted vs observed radio flares",
                "GX 339-4 / GRS 1915+105 comparison",
                "Asymmetric radio emission from oblique infall"
            ]
        }
        
        return recommendations.get(concept_id, ["Generate relevant plots for this concept"])
    
    def generate_report(self, output_file='PAPER_PLOT_CONSISTENCY_REPORT.md'):
        """Generate comprehensive markdown report"""
        lines = []
        
        lines.append("# Paper-Plot Consistency Analysis")
        lines.append(f"\n**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append(f"\n**Paper:** Segmented Spacetime - Infalling Matter and Radiowaves")
        lines.append(f"\n**Authors:** Carmen N Wrede, Lino P. Casu, Bingsi")
        lines.append(f"\n**Plots Analyzed:** {len(self.plots)}")
        lines.append("\n---\n")
        
        # Executive Summary
        lines.append("## Executive Summary\n")
        total_concepts = len(PAPER_CONCEPTS)
        critical_concepts = [c for c in PAPER_CONCEPTS.values() if c['importance'] == 'CRITICAL']
        critical_covered = sum(1 for mc in self.missing_concepts if mc['importance'] != 'CRITICAL')
        
        lines.append(f"- **Total Paper Concepts:** {total_concepts}")
        lines.append(f"- **Critical Concepts:** {len(critical_concepts)}")
        lines.append(f"- **Critical Coverage:** {len(critical_concepts) - len([m for m in self.missing_concepts if m['importance'] == 'CRITICAL'])}/{len(critical_concepts)}")
        lines.append(f"- **Inconsistencies Found:** {len(self.inconsistencies)}")
        lines.append(f"- **Missing Concept Coverage:** {len(self.missing_concepts)}/{total_concepts}")
        
        if len(self.inconsistencies) == 0 and len(self.missing_concepts) == 0:
            lines.append("\n✅ **Status:** EXCELLENT - All concepts covered, no inconsistencies")
        elif len([m for m in self.missing_concepts if m['importance'] == 'CRITICAL']) == 0:
            lines.append("\n⚠️ **Status:** GOOD - Critical concepts covered, minor gaps")
        else:
            lines.append("\n❌ **Status:** NEEDS WORK - Critical concepts missing")
        
        lines.append("\n---\n")
        
        # Concept Coverage
        lines.append("## Concept Coverage Analysis\n")
        
        for concept_id, concept_info in PAPER_CONCEPTS.items():
            matches = self.concept_matches[concept_id]
            required = concept_info['required_plots']
            found = len(matches)
            
            status = "✅" if found >= required else "⚠️" if found > 0 else "❌"
            
            lines.append(f"\n### {status} {concept_id}\n")
            lines.append(f"**Description:** {concept_info['description']}\n")
            lines.append(f"**Importance:** {concept_info['importance']}\n")
            lines.append(f"**Coverage:** {found}/{required} plots\n")
            
            if matches:
                lines.append(f"\n**Representative Plots:**")
                for plot in matches[:3]:  # Show top 3
                    lines.append(f"- `{plot['file']}`")
            else:
                lines.append("\n❌ **No plots found for this concept**")
            
            lines.append("\n")
        
        lines.append("\n---\n")
        
        # Scientific Inconsistencies
        lines.append("## Scientific Consistency Check\n")
        
        if self.inconsistencies:
            for inc in self.inconsistencies:
                lines.append(f"\n### {inc['type']}: {inc['issue']}\n")
                lines.append(f"{inc['description']}\n")
                
                if 'plots' in inc and inc['plots']:
                    lines.append(f"\n**Affected Plots ({len(inc['plots'])}):**")
                    for plot in inc['plots'][:5]:
                        lines.append(f"- `{plot['file']}`")
                    if len(inc['plots']) > 5:
                        lines.append(f"- ... and {len(inc['plots']) - 5} more")
                lines.append("\n")
        else:
            lines.append("✅ **No scientific inconsistencies detected**\n")
        
        lines.append("\n---\n")
        
        # Missing Coverage
        lines.append("## Missing Concept Coverage\n")
        
        if self.missing_concepts:
            importance_order = {'CRITICAL': 0, 'HIGH': 1, 'MEDIUM': 2, 'LOW': 3}
            sorted_missing = sorted(self.missing_concepts, 
                                  key=lambda x: importance_order.get(x['importance'], 999))
            
            for missing in sorted_missing:
                lines.append(f"\n### [{missing['importance']}] {missing['concept']}\n")
                lines.append(f"**Description:** {missing['description']}\n")
                lines.append(f"**Gap:** {missing['gap']} plots needed (have {missing['found']}, need {missing['required']})\n")
                
                # Recommendations
                recommendations = self.get_plot_recommendations(missing['concept'])
                lines.append(f"\n**Recommended Plots:**")
                for rec in recommendations:
                    lines.append(f"- {rec}")
                lines.append("\n")
        else:
            lines.append("✅ **All concepts adequately covered**\n")
        
        lines.append("\n---\n")
        
        # Overall Recommendations
        lines.append("## Overall Recommendations\n")
        
        if self.inconsistencies:
            lines.append("\n### 1. Fix Scientific Inconsistencies (URGENT)\n")
            for inc in self.inconsistencies:
                if inc['type'] == 'CRITICAL':
                    lines.append(f"- **{inc['issue']}**: {inc['description']}")
        
        if self.missing_concepts:
            critical_missing = [m for m in self.missing_concepts if m['importance'] == 'CRITICAL']
            if critical_missing:
                lines.append("\n### 2. Add Critical Missing Plots (HIGH PRIORITY)\n")
                for missing in critical_missing:
                    lines.append(f"- **{missing['concept']}**: {missing['gap']} plots needed")
        
        lines.append("\n### 3. Strengthen Paper-Plot Alignment\n")
        lines.append("- Ensure all key paper concepts have visual representation")
        lines.append("- Add explicit labels referencing paper sections")
        lines.append("- Create summary figure showing g₁→g₂ transition")
        lines.append("- Add radiowave timeline plots")
        
        lines.append("\n---\n")
        lines.append("\n*Analysis completed successfully.*\n")
        lines.append("\n© 2025 Carmen Wrede, Lino Casu, Bingsi\n")
        
        # Write report
        output_path = Path(output_file)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        
        print(f"\n✅ Report saved: {output_path}")
        return output_path

def main():
    """Main execution"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Analyze plot consistency with paper')
    parser.add_argument('--plots', default='plots/additional', help='Plot directory')
    parser.add_argument('--docs', default='plots/PLOT_DOCUMENTATION.md', help='Documentation file')
    parser.add_argument('--output', default='PAPER_PLOT_CONSISTENCY_REPORT.md', help='Output report')
    
    args = parser.parse_args()
    
    # Analyze
    analyzer = PaperPlotAnalyzer(args.plots, args.docs)
    analyzer.load_documentation()
    analyzer.analyze_concept_coverage()
    analyzer.check_scientific_consistency()
    analyzer.generate_recommendations()
    report_path = analyzer.generate_report(args.output)
    
    # Summary
    print("\n" + "="*80)
    print("ANALYSIS COMPLETE")
    print("="*80)
    print(f"Plots analyzed: {len(analyzer.plots)}")
    print(f"Concepts checked: {len(PAPER_CONCEPTS)}")
    print(f"Missing coverage: {len(analyzer.missing_concepts)}")
    print(f"Inconsistencies: {len(analyzer.inconsistencies)}")
    print(f"\n📄 Report: {report_path}")
    print("="*80)

if __name__ == "__main__":
    main()
