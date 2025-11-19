# Complete Test Pipeline Integration - ALLE 161 Scripts

**Ziel:** ALLE Berechnungen aus ALLEN Test-Scripts als Plots konsolidieren
**Gefunden:** 222 plt.savefig matches in 105 Files

## Phase 1: Analyse (2h)

### 1.1 Kategorisierung nach Typ:
- **Validation Scripts** (run_ssz_*.py)
- **Test Scripts** (test_*.py)
- **Analysis Scripts** (*_analysis.py, *_validation.py)
- **Proof/Sweep Scripts** (ssz_proof_sweep_*.py)
- **Visualization Scripts** (create_*.py, generate_*.py)
- **Example Scripts** (segspace_*.py, phi_*.py)

### 1.2 Prioritäten:
1. **Tier 1 - Core Validation (20 Scripts):**
   - run_ssz_unified_validation.py (6 plots)
   - run_ssz_validation.py (3 plots)
   - run_ssz_theory_validation.py (3 plots)
   - generate_key_plots.py (5 plots)
   - generate_eso_breakthrough_plots.py (4 plots)
   - ssz_stability_three_figures.py (3 plots)
   - segspace_all_in_one_extended.py (3 plots)
   - phi_test.py (3 plots)

2. **Tier 2 - Proof & Sweep (15 Scripts):**
   - ssz_proof_sweep_v*.py (4-5 plots each)
   - Evidenz-SSZ analysis scripts

3. **Tier 3 - Tests with Plots (30 Scripts):**
   - All test_*.py with plt.savefig
   - Specific physics tests

4. **Tier 4 - Specialized (40 Scripts):**
   - Segwave visualizations
   - Ring analysis
   - Cosmos tests
   - Multi-body scenarios

## Phase 2: Module Organization (4h)

### Module Structure:
```
plots_modules/
├── tier1_core_validation/
│   ├── ssz_unified_validation.py
│   ├── ssz_theory_validation.py
│   └── ssz_validation.py
├── tier2_proof_sweep/
│   ├── ssz_proof_sweep_v3.py
│   ├── ssz_proof_sweep_v4.py
│   └── ssz_proof_sweep_v6.py
├── tier3_physics_tests/
│   ├── test_ppn_plots.py
│   ├── test_energy_plots.py
│   ├── test_continuity_plots.py
│   └── test_curvature_plots.py
├── tier4_specialized/
│   ├── segwave_visuals.py
│   ├── ring_analysis.py
│   └── cosmos_multibody.py
└── comprehensive/
    ├── all_segspace_plots.py
    ├── all_phi_plots.py
    └── all_bound_energy_plots.py
```

## Phase 3: Code Extraction (8h)

### Extraction Strategy:
1. **Read each script**
2. **Identify plot-generating sections**
3. **Extract core calculations**
4. **Remove external dependencies**
5. **Consolidate into module**
6. **Add to master generator**

### Per-Script Workflow:
```python
# 1. Read original
original = read_file(script_path)

# 2. Extract plot functions
plot_funcs = extract_plot_functions(original)

# 3. Extract dependencies
deps = identify_dependencies(original)

# 4. Inline dependencies
standalone = inline_dependencies(plot_funcs, deps)

# 5. Create module
create_module(standalone, module_name)
```

## Phase 4: Testing & Integration (2h)

### Test Each Module:
```bash
python plots_modules/tier1_core_validation/ssz_unified_validation.py
python plots_modules/tier2_proof_sweep/ssz_proof_sweep_v6.py
# ... etc
```

### Integration Test:
```bash
python generate_all_additional_plots_complete.py
# Should generate 200-400+ plots
```

## Phase 5: Documentation (1h)

### Create:
- `PLOT_CATALOG.md` - Complete list of all plots
- `MODULE_REFERENCE.md` - Module documentation
- `EXTRACTION_LOG.md` - What was extracted from where

## Current Progress:

### ✅ Completed (52 plots in 7 modules):
1. ssz_stability_plots.py
2. ssz_validation_plots.py
3. g79_cygnus_plots.py
4. ssz_key_analysis_plots.py
5. ssz_eso_breakthrough_plots.py
6. g79_temperature_plots.py
7. ssz_core_functions.py

### ⏳ In Progress:
8. Analyzing remaining 105 files with plt.savefig

### 📋 TODO (95+ files):
- 95 files with plt.savefig noch zu verarbeiten
- ~100-150 additional modules zu erstellen
- Integration & Testing

## Estimated Total:

**Scripts to Process:** 105 unique files
**Estimated Plots:** 300-500 total
**Estimated Modules:** 30-50 modules
**Total Time Remaining:** ~15-20 hours

## Build Strategy:

### Parallel Build:
1. **Stream 1:** Tier 1 Core Validation (highest priority)
2. **Stream 2:** Tier 2 Proof/Sweep (mathematical foundation)
3. **Stream 3:** Tier 3 Physics Tests (comprehensive coverage)

### Batch Processing:
- Process 5-10 scripts per module
- Group similar scripts together
- Share common functions

## File Organization:

```
E:\clone\PAPER-RESTORED\
├── ssz_core_functions.py (done)
├── plots_modules/
│   ├── __init__.py
│   ├── [7 modules done]
│   └── [~40 modules to build]
├── generate_additional_plots_v3.py (master)
└── PLOT_CATALOG.md (generated)
```

## Next Immediate Steps:

1. ✅ Create this plan
2. ⏳ Start Tier 1 module extraction
3. ⬜ Build 5 Tier 1 modules
4. ⬜ Test Tier 1 modules
5. ⬜ Move to Tier 2
6. ⬜ Repeat until complete

**This is a marathon, not a sprint. Systematic execution = success.**

© 2025 Carmen Wrede, Lino Casu, Bingsi
