# SSZ Plot Generation Suite

**Standalone Plot Generator für SSZ (Segmented Spacetime) Theorie**

**Version:** 1.0  
**Datum:** 2025-11-19  
**Status:** Production-Ready

---

## 🎯 Schnellstart

```bash
# Ein Befehl für alle 79 Plots:
python generate_all_plots.py

# Dauer: ~45-60 Sekunden
# Output: plots/ mit 5 Unterordnern
```

**Das war's!** Alle Plots werden automatisch generiert.

---

## 📊 Was wird generiert?

| Kategorie | Plots | Beschreibung | Output |
|-----------|-------|--------------|--------|
| **Nested** | 2 + report | Kubisches Coherence-Collapse Modell | `plots/nested/` |
| **Generated** | 4 | SVR-SSZ Phänomenologie | `plots/generated/` |
| **Additional** | 61 | Standalone Validierungs-Suite | `plots/additional/` |
| **Comparison** | 6 | Kubisch vs Piecewise Vergleich | `plots/comparison/` |
| **Paper** | 6 | Paper-konforme Piecewise Plots | `plots/paper/` |
| **TOTAL** | **79 plots** | | |

---

## ✅ Key Features

- **100% Standalone** - Keine externen Repo-Dependencies
- **Cross-Platform** - Windows & Linux
- **Schnell** - 79 Plots in unter 1 Minute
- **Modular** - Jede Kategorie einzeln nutzbar
- **Dokumentiert** - Vollständige Dokumentation aller Plots
- **Publication-Ready** - Alle Plots in 300 DPI

---

## 📁 Verzeichnisstruktur

```
E:\clone\PAPER-RESTORED\
│
├── generate_all_plots.py                    ← Master-Script
│
├── Generator-Scripts/
│   ├── nested_ssz_metric_standalone.py      ← 2 plots
│   ├── generate_local_plots.py              ← 4 plots
│   ├── generate_validation_plots_compact.py ← 61 plots ⭐
│   ├── generate_comparison_plots.py         ← 6 plots
│   └── generate_paper_plots.py              ← 6 plots
│
├── plots/                                   ← Generierte Plots
│   ├── nested/      (2 + report)
│   ├── generated/   (4)
│   ├── additional/  (61) ⭐
│   ├── comparison/  (6)
│   ├── paper/       (6)
│   ├── README_PLOTS.md
│   └── FORMULAS_REFERENCE.md
│
├── Dokumentation/
│   ├── QUICKSTART_PLOTS.md                  ← Start hier!
│   ├── PLOTS_SCRIPT_THEORY_MAPPING.md       ← Script → Theorie
│   ├── FINAL_SUMMARY_PLOTS.md               ← Vollständige Übersicht
│   ├── CLEANUP_SUMMARY.md                   ← Bereinigungsprotokoll
│   └── COMPATIBILITY_ANALYSIS_CUBIC_VS_PAPER.md
│
└── backup_obsolete/                         ← Archiv (falls nötig)
    └── README.md
```

---

## 🚀 Verwendung

### Option 1: Alle Plots auf einmal
```bash
python generate_all_plots.py
```
**Output:** 79 plots in ~45-60 Sekunden

### Option 2: Einzelne Kategorien
```bash
# Nested plots (kubisches Modell)
python nested_ssz_metric_standalone.py

# Generated plots (phänomenologisch)
python generate_local_plots.py

# Additional plots (Validierung, 61 plots!)
python generate_validation_plots_compact.py

# Comparison plots (Modell-Vergleich)
python generate_comparison_plots.py

# Paper plots (paper-konform)
python generate_paper_plots.py
```

---

## 📚 Dokumentation

### Einstieg:
1. **QUICKSTART_PLOTS.md** - Schnellanleitung (Start hier!)
2. **README.md** - Diese Datei

### Details:
3. **plots/README_PLOTS.md** - Beschreibung aller Plots
4. **plots/FORMULAS_REFERENCE.md** - Mathematische Formeln
5. **PLOTS_SCRIPT_THEORY_MAPPING.md** - Script → Theorie → Plot Zuordnung

### Erweitert:
6. **FINAL_SUMMARY_PLOTS.md** - Vollständige Zusammenfassung
7. **CLEANUP_SUMMARY.md** - Bereinigungsprotokoll
8. **COMPATIBILITY_ANALYSIS_CUBIC_VS_PAPER.md** - Modell-Vergleich

---

## 🔧 Dependencies

### Minimal:
```bash
pip install numpy matplotlib scipy
```

### Empfohlen (für beste Ergebnisse):
```bash
pip install numpy matplotlib scipy pillow
```

**Das war's!** Keine speziellen SSZ-Libraries nötig.

---

## 🎯 Anwendungsfälle

### Für Paper "Infalling Matter and Radiowaves":
```bash
python generate_paper_plots.py
# → plots/paper/ (6 plots, 100% paper-konform)
```

### Für Validierung der SSZ-Theorie:
```bash
python generate_validation_plots_compact.py
# → plots/additional/ (61 plots, standalone)
```

### Für Modell-Diskussion (Kubisch vs Piecewise):
```bash
python generate_comparison_plots.py
# → plots/comparison/ (6 plots)
```

### Für Präsentationen/Übersicht:
```bash
python generate_all_plots.py
# → Alle 79 plots in allen Kategorien
```

---

## 📊 Plot-Kategorien im Detail

### 1. Nested Plots (plots/nested/)
**Modell:** Kubisches Potential  
**Plots:** 2 + 1 report

- Coherence collapse dynamics (4 panels)
- Nested submetric analysis (4 panels)
- Technical report (Markdown)

**Verwendung:** Aktuelle Implementation, glatte Übergänge

### 2. Generated Plots (plots/generated/)
**Modell:** Phänomenologisch (SVR-SSZ)  
**Plots:** 4

- Coherence decay
- Coherence scaling (E ~ τ^1.9)
- Effective metric evolution
- Nested submetric analysis

**Verwendung:** Empirische Skalierung, Vergleich mit Beobachtungen

### 3. Additional Plots (plots/additional/) ⭐
**Modell:** SSZ Standard Metrik  
**Plots:** 61 (STANDALONE!)

**Breakdown:**
- PPN Tests (3): β, γ Parameter
- Shadow Predictions (10): Verschiedene Massen
- QNM Frequencies (4): l=2,3,4 Moden
- Proper Time (7): Zeit-Dilatation
- Energy Conditions (11): WEC, DEC, SEC
- Continuity (8): C¹ Tests
- Curvature (8): Kretschmann scalar
- Additional (10): Weitere Validierungen

**Verwendung:** Vollständige Validierung, komplett selbständig

### 4. Comparison Plots (plots/comparison/)
**Modell:** Kubisch + Piecewise  
**Plots:** 6

- Potential comparison
- Collapse rate comparison
- Trajectories
- Phase portraits
- Radiowave lightcurves
- Compatibility summary (60% vs 100%)

**Verwendung:** Modell-Diskussion, Vor-/Nachteile zeigen

### 5. Paper Plots (plots/paper/)
**Modell:** Piecewise (100% paper-konform)  
**Plots:** 6

- Coherence collapse (4 panels)
- Radiowave precursor mechanism (4 panels)
- g₁/g₂ boundary physics
- Energy release profile
- Observational predictions
- Paper summary figure

**Verwendung:** Publikation "Infalling Matter and Radiowaves"

---

## 🔬 Wissenschaftliche Grundlagen

### SSZ Metrik:
```
γ_seg(r) = 1 - α * exp[-(r/r_c)²]
A_SSZ(r) = D(r) * A_GR(r)
D(r) = 1 / (1 + Xi(r))
```

### Kubisches Modell:
```
V(Xi) = 0.5*a*Xi² + (1/3)*b*Xi³
C(Xi) = Γ₀ * [dV/dXi]²
```

### Piecewise Modell:
```
V(Xi) = { 0                         Xi ≤ Xi_c
        { (k/(p+1))*(Xi-Xi_c)^(p+1) Xi > Xi_c
```

**Details:** Siehe `plots/FORMULAS_REFERENCE.md`

---

## ⚡ Performance

```
Kategorie           Zeit        Plots
─────────────────────────────────────
Nested              ~5s         2
Generated           ~5s         4
Additional          ~20s        61
Comparison          ~10s        6
Paper               ~10s        6
─────────────────────────────────────
TOTAL               ~45-60s     79
```

---

## 🐛 Troubleshooting

### Problem: "ModuleNotFoundError: No module named 'numpy'"
**Lösung:**
```bash
pip install numpy matplotlib scipy
```

### Problem: "Permission denied" beim Schreiben
**Lösung:**
```bash
# Lösche alte Plots zuerst
rm -rf plots/*
python generate_all_plots.py
```

### Problem: Script startet nicht
**Lösung:**
```bash
# Prüfe Python-Version (mindestens 3.8)
python --version

# Stelle sicher du bist im richtigen Verzeichnis
cd E:\clone\PAPER-RESTORED
```

---

## 📝 Changelog

### Version 1.0 (2025-11-19)
- ✅ Alle 79 Plots generieren erfolgreich
- ✅ 100% standalone (keine externen Repo-Dependencies)
- ✅ Vollständige Dokumentation
- ✅ Bereinigung: 9 → 6 Scripts
- ✅ Backup-System für obsolete Dateien
- ✅ Cross-platform kompatibel

---

## 🤝 Autoren

**Carmen Wrede** - SSZ Theorie, Piecewise Modell  
**Lino Casu** - Mathematische Grundlagen  
**Bingsi** - Implementation, Plot-Generator

---

## 📄 Lizenz

**ANTI-CAPITALIST SOFTWARE LICENSE v1.4**

Dieses Projekt ist unter der Anti-Capitalist Software License lizenziert.
Siehe LICENSE-Datei für Details.

---

## 🔗 Weitere Ressourcen

### Papers:
- Segmented Spacetime Theory
- Infalling Matter and Radiowaves
- (Weitere in `papers/` Verzeichnis)

### Hauptrepo:
- `E:\clone\Segmented-Spacetime-Mass-Projection-Unified-Results`
- (Für erweiterte Tests und vollständige Suite)

---

## ✨ Features im Detail

### Standalone
- Keine Abhängigkeit von anderen Repos
- Nur Standard-Python-Bibliotheken
- Funktioniert überall

### Modular
- Jede Kategorie einzeln nutzbar
- Master-Script für alles
- Flexible Verwendung

### Dokumentiert
- 8 Dokumentations-Dateien
- Jeder Plot erklärt
- Alle Formeln dokumentiert

### Publication-Ready
- 300 DPI Auflösung
- Professionelles Layout
- Paper-konforme Plots verfügbar

---

**🎉 Bereit für Verwendung in Paper, Präsentationen und Diskussionen!**

---

**Support:** Siehe Dokumentation in `QUICKSTART_PLOTS.md` und `plots/README_PLOTS.md`

© 2025 Carmen Wrede, Lino Casu, Bingsi  
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
