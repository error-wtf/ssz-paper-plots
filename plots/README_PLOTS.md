# SSZ Plots - Übersicht und Dokumentation

**Datum:** 2025-11-19  
**Autoren:** Carmen Wrede, Lino Casu, Bingsi  
**Gesamt:** 79 plots + 1 report  
**Alle Scripts:** 100% Standalone (keine externen Repo-Dependencies)

---

## Verzeichnisstruktur

```
plots/
├── nested/        (2 plots + report) - Kubisches Coherence-Collapse Modell
├── generated/     (4 plots)         - SVR-SSZ Phänomenologie
├── additional/    (61 plots)        - Standalone Validierungstests ⭐
├── comparison/    (6 plots)         - Kubisch vs Piecewise Vergleich
└── paper/         (6 plots)         - Paper-konforme Piecewise Plots
```

---

## 1. NESTED PLOTS (plots/nested/)

### 1.1 coherence_collapse_dynamics.png
4-Panel Plot mit kubischem Potential-Modell:
- **(A) Potential:** V(Xi) = 0.5*a*Xi² + (1/3)*b*Xi³
- **(B) Trajektorien:** Zeitliche Evolution verschiedener Startwerte
- **(C) Collapse Rate:** C(Xi) = Γ*[dV/dXi]²
- **(D) Phase Portrait:** dXi/dt vs Xi

**Modell:** Kubisch (smooth, symmetrisch)

### 1.2 nested_submetric_analysis.png
4-Panel Plot der nested sub-metric Struktur:
- **(A) Segmentation Field:** γ_seg(r) = 1 - α*exp[-(r/r_c)²]
- **(B) Frequency Shifts:** Redshift (g²→g¹), Blueshift (g¹→g²)
- **(C) Metric Ratio:** g²/g¹ = γ²
- **(D) Broken Reciprocity:** dτ²/dt¹ ≠ 1

**Physik:** g² ist eingebettet in g¹, keine gemeinsame Zeit

### 1.3 SSZ_NESTED_SUBMETRIC_REPORT.md
Vollständiger technischer Report mit allen Formeln

---

## 2. GENERATED PLOTS (plots/generated/)

### 2.1 coherence_decay.png
Coherence amplitude c(t) mit Zerfallsgesetz dc/dt = -k*c^p
- Verschiedene Startwerte c₀
- Finite-time collapse zu c_thresh = 0.1
- Nonlinearität p = 2.2

### 2.2 coherence_scaling.png
Energy-time Skalierung: E ~ τ_f^γ
- Log-log Plot
- γ ≈ 1.9 (SVR empirischer Wert)
- Fit zu Beobachtungen

### 2.3 effective_metric_evolution.png
Effektive Metrik während g₂→g₁:
- F_eff(t) = F_SSZ * c(t)^a
- G_eff(t) = G_SSZ * c(t)^b
- 2 Panels

### 2.4 nested_submetric_analysis_local.png
Lokale nested metric Analyse

---

## 3. ADDITIONAL PLOTS (plots/additional/)

**Script:** `generate_validation_plots_compact.py`  
**Status:** 100% Standalone (keine externen Dependencies)  
**Plots:** 61 validation plots

### 3.1 PPN Tests (3 plots)
- `ppn_beta.png` - β Parameter (=1 im schwachen Feld)
- `ppn_gamma.png` - γ Parameter (=1 im schwachen Feld)
- `ppn_combined.png` - Kombinierte Analyse
- Validiert: SSZ = GR bei r >> r_s

### 3.2 Shadow Predictions (10 plots)
- `shadow_vs_mass.png` - Hauptplot
- `shadow_2.png` bis `shadow_10.png` - Verschiedene Massen
- b_SSZ vs b_GR (EHT-kompatibel)

### 3.3 QNM Frequencies (4 plots)
- `qnm_frequency.png` - Hauptplot
- `qnm_2.png`, `qnm_3.png`, `qnm_4.png` - l=2,3,4 Moden
- Quasi-normal modes (Eikonal-Limit)

### 3.4 Proper Time (7 plots)
- `proper_time.png` - Hauptplot
- `proper_time_2.png` bis `proper_time_7.png` - Verschiedene Massen
- SSZ bleibt endlich bei r→0

### 3.5 Energy Conditions (11 plots)
- `energy_1.png` bis `energy_11.png`
- WEC, DEC, SEC Proxies

### 3.6 Continuity (8 plots)
- `continuity_1.png` bis `continuity_8.png`
- C¹ Tests der Metrik

### 3.7 Curvature (8 plots)
- `curvature_1.png` bis `curvature_8.png`
- Kretschmann scalar (keine Singularität)

### 3.8 Additional Tests (10 plots)
- `additional_1.png` bis `additional_10.png`
- Weitere Validierungen

---

## 4. COMPARISON PLOTS (plots/comparison/)

Vergleicht **Kubisches** vs **Piecewise** Modell

### 4.1 model_comparison_potential.png
Potentiallandschaften Side-by-Side
- Links: Kubisch (smooth, symmetrisch)
- Rechts: Piecewise (sharp break bei Xi_c)

### 4.2 model_comparison_collapse.png
Collapse-Raten
- Kubisch: C > 0 überall
- Piecewise: C = 0 in g₁, > 0 in g₂

### 4.3 model_comparison_trajectories.png
Trajektorien
- Kubisch: Smooth approach
- Piecewise: Finite-time collapse

### 4.4 model_comparison_phase.png
Phase portraits
- Zeigt Unterschiede in Dynamik

### 4.5 radiowave_lightcurves.png
Simulierte Radio-Lichtkurven
- Kubisch: Breit (σ=1.0)
- Piecewise: Schmal (σ=0.2)

### 4.6 paper_compatibility_summary.png
Balkendiagramm:
- Kubisch: 60% paper-kompatibel
- Piecewise: 100% paper-kompatibel

---

## 5. PAPER PLOTS (plots/paper/)

**NUR Piecewise Modell** (100% paper-konform)

### 5.1 coherence_collapse_piecewise.png
4-Panel Hauptfigur (nur piecewise):
- Sharp break at Xi_c
- g₁ absolutely stable (V=0)
- g₂ one-sided (Xi > Xi_c)
- Finite-time collapse

### 5.2 radiowave_precursor_mechanism.png
4-Panel Radiowave-Mechanismus:
- **(A) Velocity Decomposition:** v_total = v_fall + v_eigen
- **(B) Frequency Suppression:** Nur Radio < GHz
- **(C) Timeline:** Radio days/weeks vor Optical
- **(D) Mechanism Summary:** 6-Schritt Prozess

### 5.3 g1_g2_boundary_physics.png
Schematische g₁/g₂ Grenze:
- Sharp transition bei γ = 0.5
- Energy horizon (nicht event horizon!)

### 5.4 energy_release_profile.png
Energie-Freisetzung vs Xi:
- E(Xi) = (k/(p+1))*(Xi-Xi_c)^(p+1)
- Nur in g₂ aktiv

### 5.5 observational_predictions.png
Beobachtungsvorhersagen:
1. Radio precursors (90% confidence)
2. Long-duration radio (80%)
3. No early UV/X-ray (70%)
4. Radio-jet correlation (60%)
5. Velocity signatures (50%)

### 5.6 paper_summary_figure.png
Zusammenfassung für Paper:
- Oben: Physik (Potential, Collapse, Features)
- Unten: Beobachtungen (Precursors, Timing)

---

## Generator-Scripts

1. **nested_ssz_metric_standalone.py** → plots/nested/ (2 plots)
2. **generate_local_plots.py** → plots/generated/ (4 plots)
3. **generate_validation_plots_compact.py** → plots/additional/ (61 plots) ⭐
4. **generate_comparison_plots.py** → plots/comparison/ (6 plots)
5. **generate_paper_plots.py** → plots/paper/ (6 plots)

**Master-Script:**
- **generate_all_plots.py** - Generiert alle 79 plots in einem Befehl

**Dokumentation:**
- **README_PLOTS.md** - Übersicht aller Plots
- **FORMULAS_REFERENCE.md** - Mathematische Formeln
- **PLOTS_SCRIPT_THEORY_MAPPING.md** - Script → Theorie Mapping
- **COMPATIBILITY_ANALYSIS_CUBIC_VS_PAPER.md** - Modell-Vergleich

---

## Mathematische Formeln

Siehe separate Datei: **FORMULAS_REFERENCE.md**

---

© 2025 Carmen Wrede, Lino Casu, Bingsi  
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
