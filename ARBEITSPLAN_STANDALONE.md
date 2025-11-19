# ARBEITSPLAN: Standalone Additional Plots

## Problem
- Bisherige generate_validation_plots_compact.py: HALLUZINATION (leere Plots)
- Echte Test-Scripts sollen STANDALONE integriert werden
- Nicht Pipeline, sondern CODE auslesen und konsolidieren

## Phase 1: ECHTE Plot-Scripts identifizieren ✅
Gefunden via `grep plt.savefig`:
- **96 Treffer** in Unified Results
- **37 Treffer** in G79-Cygnus  
- **4 Treffer** in SSZ-Metric-Pure

**Wichtige mit Plots:**
1. ssz_stability_three_figures.py - 3 Plots ✓
2. generate_key_plots.py - Multiple plots
3. generate_eso_breakthrough_plots.py - Multiple plots
4. run_ssz_unified_validation.py
5. run_ssz_validation.py
6. G79: COMPLETE_PAPER_FIGURES.py - 8 Plots
7. G79: GENERATE_ENGLISH_HIGHLIGHTS.py - 6 Plots

**Test-Scripts OHNE Plots (nur Console):**
- test_ppn_exact.py ❌
- test_energy_conditions.py ❌
- test_c1_segments.py ❌
- test_vfall_duality.py ❌

## Phase 2: Code-Extraktion (Pro Script)

### 2.1 SSZ Core Code (einmal definieren)
```python
# SSZ Metric Functions
def gamma_seg(r, r_s, alpha, r_c):
    ...

def D(r, r_s, alpha, r_c):
    ...

def A_SSZ(r, M, alpha, r_c):
    ...
```

### 2.2 Plot-Kategorien
1. **Stability Plots** (ssz_stability_three_figures.py)
2. **Key Plots** (generate_key_plots.py)
3. **ESO Breakthrough** (generate_eso_breakthrough_plots.py)
4. **G79 Paper Figures** (COMPLETE_PAPER_FIGURES.py)
5. **G79 English Highlights** (GENERATE_ENGLISH_HIGHLIGHTS.py)

### 2.3 Dependencies eliminieren
- pandas → numpy arrays
- astropy → manuelle Konstanten
- custom imports → inline code

## Phase 3: Module erstellen

### Modul 1: `ssz_core.py`
```python
# SSZ metric, gamma_seg, D(r), etc.
# Konstanten: G, c, M_SUN
```

### Modul 2: `ssz_stability_plots.py`
```python
from ssz_core import *
# 3 Stability plots
```

### Modul 3: `ssz_key_plots.py`
```python
# Key validation plots
```

### Modul 4: `g79_plots.py`
```python
# G79 specific plots
```

## Phase 4: Konsolidierung

### generate_additional_plots_standalone_v2.py
```python
#!/usr/bin/env python3
import ssz_core
import ssz_stability_plots
import ssz_key_plots
import g79_plots

def main():
    # Generate all plots
    ssz_stability_plots.generate(output_dir)
    ssz_key_plots.generate(output_dir)
    g79_plots.generate(output_dir)
```

## Phase 5: Testing

1. Run standalone script
2. Verify plots match originals
3. Count plots
4. Document

## Zeitabschätzung
- Phase 2: 2-3 Stunden (Code extrahieren)
- Phase 3: 1 Stunde (Module erstellen)
- Phase 4: 30 Min (Konsolidieren)
- Phase 5: 30 Min (Testing)
- **TOTAL: 4-5 Stunden**

## Alternative: Schnelle Lösung
Statt ALLE Scripts:
- Nur die 10 wichtigsten mit meisten Plots
- Rest kann später ergänzt werden

**TOP 10:**
1. ssz_stability_three_figures.py
2. generate_key_plots.py  
3. generate_eso_breakthrough_plots.py
4. G79: COMPLETE_PAPER_FIGURES.py
5. G79: GENERATE_ENGLISH_HIGHLIGHTS.py
6. G79: TEST_TEMPERATURE_EQUATIONS_COMPLETE.py
7. G79: TEST_THREE_PHASE_DECOUPLING.py
8. run_ssz_unified_validation.py
9. run_ssz_validation.py
10. ssz_metric_pure: generate_validation_report.py

**Zeitabschätzung Quick:** 1-2 Stunden

---

## Nächste Schritte
1. Entscheidung: ALLE oder TOP 10?
2. Code-Extraktion starten
3. Module bauen
4. Testen
