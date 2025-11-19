# SSZ Plot Suite - Datei-Manifest

**Stand:** 2025-11-19  
**Zweck:** Vollständige Übersicht aller Dateien und ihre Funktion

---

## 📁 Verzeichnisstruktur

```
E:\clone\PAPER-RESTORED\
│
├── 🔧 Generator-Scripts (6 aktiv)
├── 📊 Plots-Verzeichnis (79 generierte Plots)
├── 📚 Dokumentation (10 Dateien)
├── 🗄️ Backup-Archiv (5 obsolete Dateien)
└── ⚙️ Konfiguration & Lizenz
```

---

## 🔧 Generator-Scripts

### Aktive Scripts (6):

| Datei | Zweck | Output | Plots | Status |
|-------|-------|--------|-------|--------|
| **generate_all_plots.py** | Master-Script | Alle | 79 | ✅ Production |
| **nested_ssz_metric_standalone.py** | Nested plots | plots/nested/ | 2 | ✅ Production |
| **generate_local_plots.py** | Generated plots | plots/generated/ | 4 | ✅ Production |
| **generate_validation_plots_compact.py** | Additional plots | plots/additional/ | 61 | ✅ Production |
| **generate_comparison_plots.py** | Comparison plots | plots/comparison/ | 6 | ✅ Production |
| **generate_paper_plots.py** | Paper plots | plots/paper/ | 6 | ✅ Production |

**Gesamt:** 6 Scripts → 79 Plots

---

## 📊 Plots-Verzeichnis

### plots/
```
plots/
├── README_PLOTS.md               ← Plot-Dokumentation
├── FORMULAS_REFERENCE.md         ← Mathematische Formeln
│
├── nested/                       ← 2 plots + 1 report
│   ├── coherence_collapse_dynamics.png
│   ├── nested_submetric_analysis.png
│   └── SSZ_NESTED_SUBMETRIC_REPORT.md
│
├── generated/                    ← 4 plots
│   ├── coherence_decay.png
│   ├── coherence_scaling.png
│   ├── effective_metric_evolution.png
│   └── nested_submetric_analysis_local.png
│
├── additional/                   ← 61 plots
│   ├── ppn_beta.png, ppn_gamma.png, ppn_combined.png (3)
│   ├── shadow_vs_mass.png, shadow_2.png ... shadow_10.png (10)
│   ├── qnm_frequency.png, qnm_2-4.png (4)
│   ├── proper_time.png, proper_time_2-7.png (7)
│   ├── energy_1-11.png (11)
│   ├── continuity_1-8.png (8)
│   ├── curvature_1-8.png (8)
│   └── additional_1-10.png (10)
│
├── comparison/                   ← 6 plots
│   ├── model_comparison_potential.png
│   ├── model_comparison_collapse.png
│   ├── model_comparison_trajectories.png
│   ├── model_comparison_phase.png
│   ├── radiowave_lightcurves.png
│   └── paper_compatibility_summary.png
│
└── paper/                        ← 6 plots
    ├── coherence_collapse_piecewise.png
    ├── radiowave_precursor_mechanism.png
    ├── g1_g2_boundary_physics.png
    ├── energy_release_profile.png
    ├── observational_predictions.png
    └── paper_summary_figure.png
```

**Gesamt:** 79 plots + 1 report + 2 Dokumentationen

---

## 📚 Dokumentation

### Haupt-Dokumentation (10 Dateien):

| Datei | Zweck | Seiten | Zielgruppe |
|-------|-------|--------|------------|
| **README.md** | Hauptübersicht | 200+ | Alle |
| **QUICKSTART_PLOTS.md** | Schnellanleitung | 150+ | Anfänger |
| **DOCUMENTATION_INDEX.md** | Doku-Übersicht | 200+ | Alle |
| **plots/README_PLOTS.md** | Plot-Details | 220+ | Fortgeschritten |
| **plots/FORMULAS_REFERENCE.md** | Mathematik | 600+ | Wissenschaftler |
| **PLOTS_SCRIPT_THEORY_MAPPING.md** | Script→Theorie | 500+ | Entwickler |
| **FINAL_SUMMARY_PLOTS.md** | Zusammenfassung | 300+ | Alle |
| **CLEANUP_SUMMARY.md** | Bereinigung | 150+ | Entwickler |
| **COMPATIBILITY_ANALYSIS_CUBIC_VS_PAPER.md** | Modell-Vergleich | 200+ | Wissenschaftler |
| **FILE_MANIFEST.md** | Diese Datei | 100+ | Alle |

**Gesamt:** ~2600+ Zeilen Dokumentation

---

## 🗄️ Backup-Archiv

### backup_obsolete/

| Datei | Grund | Ersetzt durch | Löschbar |
|-------|-------|---------------|----------|
| **generate_all_ssz_plots_master.py** | Veraltet | generate_all_plots.py | Nach 1 Monat |
| **ssz_validation_plots_generator.py** | Platzhalter | generate_validation_plots_compact.py | Nach 1 Monat |
| **ssz_real_validation_plots_generator.py** | Nicht standalone | generate_validation_plots_compact.py | Nach 1 Monat |
| **generate_svr_ssz_plots.py** | Duplikat | generate_local_plots.py | Nach 1 Monat |
| **README_ADDITIONAL_PLOTS.md** | Veraltet | Konsolidiert | Nach 1 Monat |
| **README.md** | Archiv-Doku | - | Behalten |

**Gesamt:** 6 Dateien (5 Scripts + 1 Doku)

**Wiederherstellung:**
```bash
cp backup_obsolete/[DATEI].py .
```

---

## ⚙️ Konfiguration & Meta

| Datei | Zweck | Status |
|-------|-------|--------|
| **LICENSE** | Anti-Capitalist Software License v1.4 | ✅ |
| **.gitignore** | Git ignore rules (falls vorhanden) | Optional |

---

## 📊 Statistiken

```
Generator-Scripts:       6 (aktiv)
Archiv-Scripts:          5 (backup)
Dokumentations-Dateien:  10
Plot-Dateien:           79 + 1 report
Gesamt-Dateien:         ~100+

Code-Zeilen (Scripts):  ~3000+
Doku-Zeilen:           ~2600+
Gesamt-Zeilen:         ~5600+
```

---

## 🔍 Datei-Finder

### "Wie generiere ich alle Plots?"
→ `generate_all_plots.py`

### "Nur Paper-Plots?"
→ `generate_paper_plots.py`

### "Nur Validierung?"
→ `generate_validation_plots_compact.py`

### "Was macht welcher Plot?"
→ `plots/README_PLOTS.md`

### "Welche Formeln?"
→ `plots/FORMULAS_REFERENCE.md`

### "Schnellanleitung?"
→ `QUICKSTART_PLOTS.md`

### "Vollständige Doku?"
→ `DOCUMENTATION_INDEX.md`

### "Was wurde geändert?"
→ `CLEANUP_SUMMARY.md`

### "Archivierte Dateien?"
→ `backup_obsolete/README.md`

---

## ✅ Integritäts-Check

### Scripts:
- ✅ Alle 6 aktiven Scripts vorhanden
- ✅ Alle importieren nur Standard-Bibliotheken
- ✅ Alle haben UTF-8 encoding
- ✅ Alle sind standalone

### Dokumentation:
- ✅ Alle 10 Hauptdokumente vorhanden
- ✅ Zahlen konsistent (79 plots, 61 additional)
- ✅ Keine Duplikate
- ✅ Alle auf Stand 2025-11-19

### Plots:
- ✅ plots/ Verzeichnis existiert
- ✅ Alle 5 Unterordner vorhanden
- ✅ 79 Plots generierbar
- ✅ Keine Platzhalter mehr

### Backup:
- ✅ backup_obsolete/ vorhanden
- ✅ 5 Scripts gesichert
- ✅ README dokumentiert

---

## 🔄 Wartung

### Wöchentlich:
- [ ] Alle Scripts testen (`generate_all_plots.py`)
- [ ] Output überprüfen (79 plots generiert?)
- [ ] Dokumentation auf Aktualität prüfen

### Monatlich:
- [ ] Backup-Archiv überprüfen (noch nötig?)
- [ ] Statistiken aktualisieren
- [ ] Neue Features dokumentieren

### Bei Änderungen:
- [ ] FILE_MANIFEST.md aktualisieren
- [ ] DOCUMENTATION_INDEX.md prüfen
- [ ] README.md anpassen
- [ ] Datum in allen Dateien aktualisieren

---

## 📦 Deployment-Checkliste

### Für Release:
- [ ] Alle Scripts funktionieren
- [ ] Alle 79 Plots generierbar
- [ ] Dokumentation vollständig
- [ ] README.md aktuell
- [ ] LICENSE vorhanden
- [ ] Backup-Archiv dokumentiert
- [ ] Dependencies klar (nur numpy, matplotlib, scipy)
- [ ] Beispiel-Output vorhanden

---

## 🔗 Abhängigkeiten

### Externe:
```python
numpy         # Numerik
matplotlib    # Plotting
scipy         # Wissenschaftliche Berechnungen
```

### Interne:
```
Keine! Alle Scripts sind standalone.
```

---

## 📈 Version History

### v1.0 (2025-11-19)
- ✅ 6 aktive Scripts
- ✅ 79 Plots generierbar
- ✅ 100% standalone
- ✅ Vollständige Dokumentation
- ✅ Backup-System
- ✅ Bereinigung abgeschlossen

---

**📁 Alle Dateien dokumentiert und organisiert!**

---

© 2025 Carmen Wrede, Lino Casu, Bingsi  
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
