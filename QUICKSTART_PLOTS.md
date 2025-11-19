# SSZ Plots - Quick Start Guide

**Schnellanleitung:** Alle 79 Plots in einem Befehl generieren

**Version:** 1.0  
**Stand:** 2025-11-19  
**Status:** Production-Ready

---

## 🚀 Einfachste Methode (Empfohlen)

```bash
python generate_all_plots.py
```

**Das war's!** Alle Plots werden automatisch generiert und in die richtigen Ordner sortiert.

---

## 📊 Was wird generiert?

| Kategorie | Plots | Beschreibung | Output |
|-----------|-------|--------------|--------|
| **Nested** | 2 + report | Kubisches Coherence-Collapse Modell | `plots/nested/` |
| **Generated** | 4 | SVR-SSZ Phänomenologie | `plots/generated/` |
| **Additional** | 61 | **Standalone Validierungs-Suite** | `plots/additional/` |
| **Comparison** | 6 | Kubisch vs Piecewise Vergleich | `plots/comparison/` |
| **Paper** | 6 | Paper-konform (nur Piecewise) | `plots/paper/` |
| **TOTAL** | **79 plots** | | |

---

## ⏱ Dauer

- **Gesamt:** ~45-60 Sekunden
- **Nested:** ~5 Sekunden
- **Generated:** ~5 Sekunden
- **Additional:** ~20 Sekunden (61 plots!)
- **Comparison:** ~10 Sekunden
- **Paper:** ~10 Sekunden

---

## 📁 Output-Struktur

```
plots/
├── nested/
│   ├── coherence_collapse_dynamics.png
│   ├── nested_submetric_analysis.png
│   └── SSZ_NESTED_SUBMETRIC_REPORT.md
│
├── generated/
│   ├── coherence_decay.png
│   ├── coherence_scaling.png
│   ├── effective_metric_evolution.png
│   └── nested_submetric_analysis_local.png
│
├── additional/
│   ├── ppn_beta.png, ppn_gamma.png, ...
│   ├── shadow_vs_mass.png, ...
│   ├── qnm_frequency.png, ...
│   ├── proper_time.png, ...
│   ├── energy_wec.png, ...
│   ├── continuity_c1.png, ...
│   ├── curvature_kretschmann.png, ...
│   ├── mass_reconstruction.png, ...
│   ├── g79_velocity.png, ...
│   └── multibody_binary.png, ...
│
├── comparison/
│   ├── model_comparison_potential.png
│   ├── model_comparison_collapse.png
│   ├── model_comparison_trajectories.png
│   ├── model_comparison_phase.png
│   ├── radiowave_lightcurves.png
│   └── paper_compatibility_summary.png
│
└── paper/
    ├── coherence_collapse_piecewise.png
    ├── radiowave_precursor_mechanism.png
    ├── g1_g2_boundary_physics.png
    ├── energy_release_profile.png
    ├── observational_predictions.png
    └── paper_summary_figure.png
```

---

## 📚 Dokumentation

Nach der Generierung:

```bash
# Übersicht aller Plots
cat plots/README_PLOTS.md

# Alle mathematischen Formeln
cat plots/FORMULAS_REFERENCE.md

# Modell-Kompatibilität
cat COMPATIBILITY_ANALYSIS_CUBIC_VS_PAPER.md
```

---

## 🔧 Einzelne Plots neu generieren

Wenn du nur bestimmte Plots neu generieren willst:

```bash
# Nur Nested Plots
python nested_ssz_metric_standalone.py

# Nur Generated Plots
python generate_local_plots.py

# Nur Additional Plots (standalone)
python generate_validation_plots_compact.py

# Nur Comparison Plots
python generate_comparison_plots.py

# Nur Paper Plots
python generate_paper_plots.py
```

---

## 🎯 Welche Plots für welchen Zweck?

### Für Presentations
→ `plots/paper/` (6 plots)
- Saubere, paper-konforme Plots
- Nur piecewise Modell (100% kompatibel)
- Publication-ready

### Für Analysen
→ `plots/comparison/` (6 plots)
- Kubisch vs Piecewise side-by-side
- Zeigt Unterschiede
- Für Diskussion

### Für Validierung
→ `plots/additional/` (61 plots)
- **Komplett standalone** (keine externen Dependencies!)
- PPN, Shadow, QNM, Energy, etc.
- Selbst-enthaltene Validierung

### Für Implementation
→ `plots/nested/` und `plots/generated/`
- Aktuelle Implementation (kubisch)
- SVR-SSZ Phänomenologie

---

## ⚠️ Troubleshooting

### Problem: "Script not found"
```bash
# Lösung: Stelle sicher du bist im richtigen Verzeichnis
cd E:\clone\PAPER-RESTORED
python generate_all_plots.py
```

### Problem: "Permission denied"
```bash
# Lösung: Lösche alte Plots zuerst
rm -rf plots/*
python generate_all_plots.py
```

### Problem: "Import error"
```bash
# Lösung: Installiere Dependencies
pip install numpy matplotlib scipy
```

---

## 💡 Tipps & Best Practices

### Performance:
1. **Erste Generierung:** Kann länger dauern (~60s, Compile-Zeit)
2. **Re-Generation:** Ist schneller (~45s, Cache genutzt)
3. **Selektiv:** Nutze einzelne Scripts für schnelle Updates
4. **Parallel:** Mehrere Scripts gleichzeitig nicht empfohlen

### Dateien:
5. **Backup:** Alte Plots werden überschrieben!
6. **Output:** Prüfe plots/ Verzeichnis nach Generierung
7. **Logs:** Bei Fehlern in Console-Output schauen

### Verwendung:
8. **Paper:** Nutze generate_paper_plots.py (100% konform)
9. **Validierung:** generate_validation_plots_compact.py ist standalone
10. **Übersicht:** generate_all_plots.py für kompletten Satz

---

## 📊 Output-Beispiel

```
################################################################################
#                          SSZ COMPLETE PLOT GENERATOR                         #
#                          All 86+ Plots in One Command                        #
################################################################################

Start time: 2025-11-19 21:22:06
Output directory: E:\clone\PAPER-RESTORED\plots
✓ Output directories created

[1/5] NESTED PLOTS (Kubisches Coherence-Collapse)
  Running: nested_ssz_metric_standalone.py
  ✓ Success: Nested metric & coherence collapse

[2/5] GENERATED PLOTS (SVR-SSZ Phänomenologie)
  Running: generate_local_plots.py
  ✓ Success: SVR-SSZ scaling & metric evolution

[3/5] ADDITIONAL PLOTS (Validierungs-Suite)
  Running: ssz_validation_plots_generator.py
  ✓ Success: PPN, Shadow, QNM, Energy, Continuity, Curvature

[4/5] COMPARISON PLOTS (Modell-Vergleich)
  Running: generate_comparison_plots.py
  ✓ Success: Cubic vs Piecewise model comparison

[5/5] PAPER PLOTS (Paper-Conform, 100% Kompatibel)
  Running: generate_paper_plots.py
  ✓ Success: Piecewise model for radiowave paper

================================================================================
  🎉 ALL PLOTS GENERATED SUCCESSFULLY!
================================================================================
  plots/nested/      → 2 plots
  plots/generated/   → 4 plots
  plots/additional/  → 68 plots
  plots/comparison/  → 6 plots
  plots/paper/       → 6 plots
  TOTAL: 86 plots
================================================================================
```

---

## 🎉 Fertig!

Jetzt hast du alle Plots. Siehe:
- **README_PLOTS.md** für Details zu jedem Plot
- **FORMULAS_REFERENCE.md** für alle Formeln
- Einzelne PNG-Dateien in `plots/` Unterordnern

---

## 🔗 Weitere Dokumentation

- **README.md** - Hauptübersicht
- **plots/README_PLOTS.md** - Detaillierte Plot-Beschreibungen
- **plots/FORMULAS_REFERENCE.md** - Mathematische Formeln
- **PLOTS_SCRIPT_THEORY_MAPPING.md** - Script → Theorie Zuordnung
- **FINAL_SUMMARY_PLOTS.md** - Vollständige Zusammenfassung
- **DOCUMENTATION_INDEX.md** - Dokumentations-Übersicht

---

## 📊 Zusammenfassung

```
✅ 79 Plots in 5 Kategorien
✅ 100% Standalone (keine externen Dependencies)
✅ ~45-60 Sekunden Generierungszeit
✅ 6 Generator-Scripts
✅ Vollständige Dokumentation
✅ Publication-Ready (300 DPI)
```

---

**🎉 Viel Erfolg mit den SSZ Plots!**

© 2025 Carmen Wrede, Lino Casu, Bingsi  
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
