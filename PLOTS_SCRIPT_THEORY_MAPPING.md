# SSZ Plots: Script → Theorie → Output Mapping

**Datum:** 2025-11-19  
**Zweck:** Zuordnung welche Plots mit welchem Script und welcher Theorie generiert werden

---

## Übersichtstabelle

| Script | Output | Plots | Theorie/Modell | Zweck |
|--------|--------|-------|----------------|-------|
| `nested_ssz_metric_standalone.py` | `plots/nested/` | 2 | **Kubisch** | Aktuelle Implementation |
| `generate_local_plots.py` | `plots/generated/` | 4 | **Phänomenologisch** | SVR-SSZ Skalierung |
| `generate_validation_plots_compact.py` | `plots/additional/` | 61 | **Standalone Validierung** | Selbständig |
| `generate_comparison_plots.py` | `plots/comparison/` | 6 | **Kubisch + Piecewise** | Vergleich |
| `generate_paper_plots.py` | `plots/paper/` | 6 | **Piecewise (paper-konform)** | Publikation |
| `generate_all_plots.py` | alle | 79 | alle | Master-Script |

---

# 1. nested_ssz_metric_standalone.py

## Output Directory
```
plots/nested/
```

## Generierte Plots
1. `coherence_collapse_dynamics.png` (4 panels)
2. `nested_submetric_analysis.png` (4 panels)
3. `SSZ_NESTED_SUBMETRIC_REPORT.md` (Report)

## Verwendete Theorie: **KUBISCHES MODELL**

### Mathematische Grundlage
```python
Potential:
  V(Xi) = 0.5 * a * Xi² + (1/3) * b * Xi³

Parameter:
  a = 1.0
  b = -0.5
  Xi_c = -a/(2b) = 1.0

Gradient:
  dV/dXi = a*Xi + b*Xi²

Collapse Rate:
  C(Xi) = Γ₀ * [dV/dXi]²
```

### Charakteristika
- ✓ **Smooth** überall (C∞)
- ✓ **Konstruktionsbedingt irreversibel** (C ≥ 0)
- ✓ **Symmetrisch** um kritischen Punkt
- ✗ Kein scharfer Break
- ✗ Beide Seiten dynamisch

### Physikalische Interpretation
- **g₁ Region** (Xi < Xi_c): "Stabil" aber kleine Restdynamik
- **g₂ Region** (Xi > Xi_c): Unstabil, Collapse aktiv
- **Übergang**: Smooth, kontinuierlich
- **Verwendung**: Aktuelle Code-Implementation

---

# 2. generate_local_plots.py

## Output Directory
```
plots/generated/
```

## Generierte Plots
1. `coherence_decay.png`
2. `coherence_scaling.png`
3. `effective_metric_evolution.png`
4. `nested_submetric_analysis_local.png`

## Verwendete Theorie: **PHÄNOMENOLOGISCHES SVR-SSZ MODELL**

### Mathematische Grundlage
```python
Decay Law:
  dc/dt = -k * c^p

Analytische Lösung:
  c(t) = [c₀^(1-p) + k(1-p)t]^[1/(1-p)]

Energy-Time Scaling:
  E ~ τ_f^γ
  mit γ ≈ 1.9 (SVR empirisch)

Parameter:
  k = 1.0
  p = 2.2
  γ = 1.9
```

### Charakteristika
- ✓ **Finite-time collapse** (p > 1)
- ✓ **Nonlinear** (p ≠ 1)
- ✓ **Empirisch kalibriert** (γ ≈ 1.9)
- ✓ **Analytische Lösungen**

### Physikalische Interpretation
- **Coherence Decay**: Wie schnell Kohärenz zusammenbricht
- **Scaling**: Energie-Zeit Relation (passt zu Beobachtungen)
- **Metric Evolution**: Effektive Metrik während Collapse
- **Verwendung**: Phänomenologie, Vergleich mit Daten

---

# 3. generate_validation_plots_compact.py

## Output Directory
```
plots/additional/
```

## Generierte Plots (61 standalone validation plots)

**Komplett selbständig - keine externen Dependencies**

### Verwendetes Modell: **SSZ STANDARD METRIK**

```
Segmentation Field:
  γ_seg(r) = 1 - α * exp[-(r/r_c)²]

SSZ Metrik:
  A_SSZ(r) = D(r) * A_GR(r)
  D(r) = 1 / (1 + Xi(r))
  Xi(r) = 1 - γ_seg(r)

GR Vergleich:
  A_GR(r) = 1 - r_s/r
```

### 3.1 PPN Tests (3 plots)
- `ppn_beta.png` - β Parameter (SSZ = GR = 1.0)
- `ppn_gamma.png` - γ Parameter (SSZ = GR = 1.0)
- `ppn_combined.png` - Beide zusammen

**Theorie:** Post-Newtonian Parameter im schwachen Feld
```
β_SSZ = 1.0 + O(α²) ≈ 1.0
γ_SSZ = 1.0 + O(α²) ≈ 1.0

→ SSZ = GR für r >> r_s
```

### 3.2 Shadow Predictions (10 plots)
- `shadow_vs_mass.png`
- `shadow_2.png` bis `shadow_12.png`

**Theorie:** Black-hole shadow (photon sphere)
```
b_SSZ = r_ph * √[1/A_SSZ(r_ph)]

mit A_SSZ(r) = D(r) * (1 - r_s/r)
D(r) = 1/(1 + α*exp[-(r/r_c)²])
```

### 3.3 QNM Frequencies (4 plots)
- `qnm_frequency.png`
- `qnm_2.png` bis `qnm_8.png`

**Theorie:** Quasi-normal modes (Eikonal limit)
```
ω_R ~ c / r_ph

SSZ modifiziert r_ph → modifiziert QNM
```

### 3.4 Proper Time (7 plots)
- `proper_time.png`
- `proper_time_2.png` bis `proper_time_10.png`

**Theorie:** Zeit-Dilatation
```
d_tau/dt = √[A_SSZ(r)]

SSZ: Bleibt endlich bei r → 0
GR: Geht zu 0 bei r → r_s
```

### 3.5 Energy Conditions (11 plots)
- `energy_wec.png` (Weak)
- `energy_2.png` bis `energy_15.png` (DEC, SEC, NEC)

**Theorie:** Energie-Bedingungen
```
WEC: ρ + P_r ≥ 0
DEC: ρ ≥ |P_r|
SEC: ρ + P_r + 2P_t ≥ 0

SSZ: Erfüllt für r ≥ 5r_s
```

### 3.6 Continuity (8 plots)
- `continuity_c1.png`
- `continuity_2.png` bis `continuity_12.png`

**Theorie:** Metrik-Glätte
```
C¹: dA/dr kontinuierlich
C²: d²A/dr² kontinuierlich

SSZ: C¹ überall
```

### 3.7 Curvature (8 plots)
- `curvature_1.png` bis `curvature_8.png`

**Theorie:** Krümmungs-Invarianten
```
K = R_μνρσ R^μνρσ

GR:   K_GR ~ (r_s/r)⁶ → ∞ bei r→0
SSZ:  K_SSZ = D⁶(r) * K_GR → endlich!

Keine Singularität in SSZ
```

### 3.8 Additional Tests (10 plots)
- `additional_1.png` bis `additional_10.png`

**Theorie:** Weitere Validierungen
```
Verschiedene Test-Szenarien
Placeholder für erweiterte Tests
```

## Verwendetes Modell: **SSZ METRIK (STANDARD)**

```
Segmentation Field:
  γ_seg(r) = 1 - α * exp[-(r/r_c)²]

SSZ Metrik:
  A_SSZ(r) = D(r) * A_GR(r)
  D(r) = 1 / (1 + Xi(r))

Nested:
  g²_μν = γ²_seg * g¹_μν
```

---

# 4. generate_comparison_plots.py

## Output Directory
```
plots/comparison/
```

## Generierte Plots
1. `model_comparison_potential.png`
2. `model_comparison_collapse.png`
3. `model_comparison_trajectories.png`
4. `model_comparison_phase.png`
5. `radiowave_lightcurves.png`
6. `paper_compatibility_summary.png`

## Verwendete Theorie: **KUBISCH + PIECEWISE (BEIDE)**

### Side-by-Side Vergleich

#### Links: Kubisches Modell
```python
V_cubic(Xi) = 0.5*a*Xi² + (1/3)*b*Xi³
C_cubic(Xi) = Γ * [a*Xi + b*Xi²]²

Eigenschaften:
  - Smooth
  - Symmetrisch
  - C > 0 überall
```

#### Rechts: Piecewise Modell
```python
V_piecewise(Xi) = { 0                      Xi ≤ Xi_c
                  { (k/(p+1))*(Xi-Xi_c)^(p+1)  Xi > Xi_c

C_piecewise(Xi) = { 0              Xi ≤ Xi_c
                  { Γ*k*(Xi-Xi_c)^p  Xi > Xi_c

Eigenschaften:
  - Sharp break
  - Einseitig
  - C = 0 in g₁
```

### Zweck
- **Visualisierung** der Unterschiede
- **Vor-/Nachteile** beider Modelle
- **Kompatibilität** mit Paper (60% vs 100%)

---

# 5. generate_paper_plots.py

## Output Directory
```
plots/paper/
```

## Generierte Plots
1. `coherence_collapse_piecewise.png` (4 panels)
2. `radiowave_precursor_mechanism.png` (4 panels)
3. `g1_g2_boundary_physics.png`
4. `energy_release_profile.png`
5. `observational_predictions.png`
6. `paper_summary_figure.png`

## Verwendete Theorie: **PIECEWISE NONLINEAR (100% PAPER-KONFORM)**

### Mathematische Grundlage (AUSSCHLIESSLICH Piecewise)
```python
Potential (piecewise):
  V(Xi) = { 0                         Xi ≤ Xi_c  (g₁: FLAT)
          { (k/(p+1))*(Xi-Xi_c)^(p+1) Xi > Xi_c  (g₂: RISING)

Gradient (piecewise):
  dV/dXi = { 0               Xi ≤ Xi_c  (NO FORCE)
           { k*(Xi-Xi_c)^p   Xi > Xi_c  (STRONG)

Collapse Rate:
  C(Xi) = { 0                  Xi ≤ Xi_c  (g₁: STABIL!)
          { Γ₀*k*(Xi-Xi_c)^p   Xi > Xi_c  (g₂: COLLAPSE!)

Evolution:
  dXi/dt = -C(Xi)

Parameter:
  k = 1.0
  Xi_c = 1.0
  Γ₀ = 1.0
  p = 2.2  (stark nichtlinear)
```

### Charakteristika (Paper-Requirements)
- ✅ **Sharp break** bei Xi_c (explizit!)
- ✅ **g₁ absolut stabil** (dV/dXi = 0, dXi/dt = 0)
- ✅ **g₂ einseitig** (nur für Xi > Xi_c)
- ✅ **Finite-time collapse** (p > 1)
- ✅ **Stark nichtlinear** (p = 2.2)
- ✅ **Irreversibel** (konstruktionsbedingt)

### Physikalische Interpretation (Paper)
- **g₁**: Weak segmentation, fast clock, **STABLE** (keine Dynamik!)
- **g₂**: Strong segmentation, slow time, **UNSTABLE** (aktiver Collapse)
- **Xi_c**: Energy horizon (nicht event horizon!)
- **Übergang**: Abrupt, diskret, messbar

### Radiowave-Mechanismus
```
v_total = v_fall + v_eigen

g₂ absorbiert: v_fall
MUSS freigeben: v_eigen → RADIOWAVES

Frequency cutoff:
  f < f_c ≈ 1 GHz: transmitted (RADIO)
  f > f_c: blocked (OPTICAL, UV, X-ray)

Timeline:
  t_radio (days/weeks vor Optical)
```

### Verwendung
- **Für Paper:** "Segmented Spacetime - Infalling Matter and Radiowaves"
- **100% kompatibel** mit allen Paper-Anforderungen
- **Publication-ready**

---

# 6. generate_all_plots.py

## Output Directory
```
Alle (nested, generated, additional, comparison, paper)
```

## Funktion
**Master-Script** das alle anderen Scripts aufruft:

```python
1. nested_ssz_metric_standalone.py   → plots/nested/
2. generate_local_plots.py           → plots/generated/
3. ssz_validation_plots_generator.py → plots/additional/
4. generate_comparison_plots.py      → plots/comparison/
5. generate_paper_plots.py           → plots/paper/
```

## Verwendete Theorien
**Alle** (orchestriert alle anderen Scripts)

## Zweck
- **Ein Befehl** für alle Plots
- **Standalone** (keine externen Abhängigkeiten)
- **Automatisch sortiert** in thematische Ordner
- **Progress tracking** und Statistiken

---

# Theorie-Übersicht: Kubisch vs Piecewise

## Kubisches Modell

### Formel
```
V(Xi) = 0.5*a*Xi² + (1/3)*b*Xi³
```

### Eigenschaften
| Feature | Status | Kommentar |
|---------|--------|-----------|
| Smooth | ✅ | C∞ überall |
| Sharp break | ❌ | Kontinuierlich |
| g₁ stable | ⚠️ | Kleine Restdynamik |
| g₂ one-sided | ❌ | Beide Seiten |
| Finite-time | ⚠️ | Langsam |
| Paper-conform | 60% | Teilweise |

### Verwendung
- **nested_ssz_metric_standalone.py**
- **generate_comparison_plots.py** (linke Seite)

### Zweck
- Aktuelle Code-Implementation
- Mathematisch elegant
- Glatte Übergänge

---

## Piecewise Modell

### Formel
```
V(Xi) = { 0                         Xi ≤ Xi_c
        { (k/(p+1))*(Xi-Xi_c)^(p+1) Xi > Xi_c
```

### Eigenschaften
| Feature | Status | Kommentar |
|---------|--------|-----------|
| Smooth | ❌ | Piecewise (nicht C¹) |
| Sharp break | ✅ | Explizit bei Xi_c |
| g₁ stable | ✅ | dXi/dt = 0 exakt |
| g₂ one-sided | ✅ | Nur Xi > Xi_c |
| Finite-time | ✅ | p = 2.2 > 1 |
| Paper-conform | 100% | Alle Requirements |

### Verwendung
- **generate_paper_plots.py** (ausschließlich!)
- **generate_comparison_plots.py** (rechte Seite)

### Zweck
- **Paper-Publikation**
- Physikalisch korrekt für Radiowave-Mechanismus
- Observational predictions

---

## SSZ Standard Metrik

### Formel
```
γ_seg(r) = 1 - α * exp[-(r/r_c)²]
A_SSZ(r) = D(r) * A_GR(r)
D(r) = 1 / (1 + Xi(r))
```

### Verwendung
- **ssz_validation_plots_generator.py** (alle 68 plots)
- Basis für alle anderen Modelle

### Zweck
- Validierung
- Test gegen GR
- Observables (Shadow, QNM, etc.)

---

## Phänomenologisches SVR-SSZ

### Formel
```
dc/dt = -k * c^p
E ~ τ_f^γ (γ ≈ 1.9)
```

### Verwendung
- **generate_local_plots.py** (4 plots)

### Zweck
- Empirische Skalierung
- Vergleich mit Daten
- Keine fundamentale Theorie

---

# Zusammenfassung: Script → Theorie Mapping

```
Script                              → Theorie           → Plots  → Zweck
================================================================================
nested_ssz_metric_standalone.py     → KUBISCH           → 2      → Implementation
generate_local_plots.py             → PHÄNOMENOLOGISCH  → 4      → Empirie
ssz_validation_plots_generator.py   → SSZ STANDARD      → 68     → Validierung
generate_comparison_plots.py        → BEIDE             → 6      → Vergleich
generate_paper_plots.py             → PIECEWISE         → 6      → Publikation
generate_all_plots.py               → ALLE              → 86     → Master
```

---

# Entscheidungshilfe: Welches Script für welchen Zweck?

## Für Paper "Infalling Matter and Radiowaves"
→ **generate_paper_plots.py**
- Nur Piecewise Modell
- 100% paper-konform
- Radiowave-Mechanismus
- 6 publication-ready plots

## Für aktuelle Code-Implementation
→ **nested_ssz_metric_standalone.py**
- Kubisches Modell
- Wie Code funktioniert
- 2 plots + report

## Für Validierung gegen GR
→ **ssz_validation_plots_generator.py**
- SSZ Standard Metrik
- PPN, Shadow, QNM, etc.
- 68 plots

## Für Modell-Diskussion
→ **generate_comparison_plots.py**
- Beide Modelle side-by-side
- Vor-/Nachteile
- 6 comparison plots

## Für alles auf einmal
→ **generate_all_plots.py**
- Master-Script
- 86 plots
- ~1 Minute

---

© 2025 Carmen Wrede, Lino Casu, Bingsi  
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
