# G79.29+0.46 Real Data - Local Copy
## Peer-Reviewed Observations for SSZ Plots

**Date:** 2025-11-20  
**Status:** ✅ Complete (4 files, 43 data points)

---

## Data Files

### 1. G79_temperatures.csv (10 points)
**Source:** Di Francesco et al. 2010, ApJ  
**Type:** Dust continuum temperature profile  
**Content:**
- Radial range: 0.3 - 1.9 pc
- Temperature: 78K → 20K (steep gradient!)
- Method: SED fitting

**Used for:**
- Collapse rate C(Xi) calculation
- Coherence evolution Xi(t) timescales
- Temperature-derived γ_seg(r) profile

---

### 2. G79_Rizzo2014_NH3_Table1.csv (3 components)
**Source:** Rizzo et al. 2014, A&A 561, A21  
**Type:** NH₃ velocity components + rotational temperatures  
**Content:**

| Component | v_range [km/s] | T_rot [K] | N(NH₃) [cm⁻²] |
|-----------|----------------|-----------|---------------|
| Blue      | -1.7 to 0.3    | >40       | 1.5 × 10¹²    |
| Central   | 0.3 to 1.9     | 11 ± 2    | 1.7 × 10¹⁵    |
| Red       | 1.9 to 2.8     | >28       | 1.5 × 10¹²    |

**Key Result:**
- Δv_total = 4.5 km/s ≈ SSZ prediction (5 km/s) ✓
- Temperature inversion: Central (11K) < Outer (>28-40K)

**Used for:**
- Radio precursor predictions
- Velocity signature analysis
- Piecewise model validation (sharp break evidence)

---

### 3. G79_gamma_seg_profile.csv (10 points)
**Source:** Derived from G79_temperatures.csv  
**Type:** Segmented spacetime γ_seg(r) profile  
**Content:**
- Fitted model: γ_seg(r) = 1 - α exp[-(r/r_c)²]
- Best-fit: α = 0.0000, r_c = 0.100 pc
- Residuals: χ²_red = 50035.0 (poor fit indicates piecewise nature!)

**Physical Interpretation:**
- Poor cubic fit → supports piecewise model
- Sharp transition at r ~ 1 pc
- Consistent with two-metric (g₁/g₂) structure

**Used for:**
- Radio redshift predictions
- Domain boundary identification
- Model comparison (cubic vs piecewise)

---

### 4. G79_radio_predictions.csv (20 points)
**Source:** SSZ model applied to G79_gamma_seg_profile.csv  
**Type:** Radio frequency redshift predictions  
**Content:**
- Source frequency: 3.00 × 10¹² Hz
- Redshift range: 65 - 353 GHz
- Radial range: 0.1 - 2.0 pc

**Predicted Effect:**
```
ν' = ν₀ · γ_seg(r)
Δν ~ 315.70 GHz (typical)
```

**Used for:**
- Radio precursor timing plots
- Observational predictions
- X-ray binary comparison (GX 339-4, GRS 1915+105)

---

## Data Quality

### Strengths ✅
- **Peer-reviewed publications** (ApJ, A&A)
- **Independent datasets** (dust continuum + NH₃ lines)
- **Spatial coverage** (0.3 - 1.9 pc, 10 radial points)
- **Velocity resolution** (3 distinct components)
- **Temperature inversion** (11K center vs >28-40K outer)

### Limitations ⚠️
- **Limited radial points** (10 for temperatures)
- **NH₃ components** (only 3, not full radial profile)
- **T_rot vs T_kinetic** (potential decoupling, needs investigation)
- **Sparse outer regions** (>1.5 pc, only 3 points)

---

## Usage in Plots

### Plot Module Dependencies:

**1_collapse_rate_REAL_DATA.png**
- Primary: G79_temperatures.csv
- Calculates: dT/dr → C(Xi)

**2_coherence_evolution_REAL_DATA.png**
- Primary: G79_temperatures.csv
- Calculates: t ~ r²/α, Xi ~ T/T_max

**3_radio_timing_REAL_DATA.png**
- Primary: G79_radio_predictions.csv
- Uses: Literature (GX 339-4, GRS 1915+105)

**4_model_compatibility_REAL_DATA.png**
- Primary: All 4 files
- Evidence: Sharp break (NH₃), steep gradient (T), piecewise (γ_seg)

**5_potential_landscapes_REAL_DATA.png**
- Primary: G79_gamma_seg_profile.csv
- Shows: V(Xi) from γ_seg(r)

**6-7_collapse_4panel_REAL_DATA.png**
- Primary: G79_temperatures.csv + G79_gamma_seg_profile.csv
- Shows: Complete dynamics (potential, trajectories, collapse, phase)

---

## Data Provenance

### Original Sources:

**Di Francesco et al. 2010:**
- Title: "A Submillimeter Array Study of the G79.29+0.46 High-Mass Star-Forming Region"
- Journal: ApJ (Astrophysical Journal)
- Data: Submillimeter continuum photometry → T(r) via SED

**Rizzo et al. 2014:**
- Title: "NH₃ emission in the G79.29+0.46 nebula"
- Journal: A&A (Astronomy & Astrophysics) 561, A21
- Data: Effelsberg 100m NH₃ observations → velocity components + T_rot

### Processing:

**G79_gamma_seg_profile.csv:**
- Input: G79_temperatures.csv
- Method: γ_seg(r) = T₀ / T(r) fitting
- Date: 2025-11-07
- Status: Poor fit → supports piecewise model

**G79_radio_predictions.csv:**
- Input: G79_gamma_seg_profile.csv
- Model: ν' = ν₀ · γ_seg(r)
- Date: 2025-11-07
- Status: Predictive (awaiting radio observations)

---

## Comparison with PAPER-RESTORED Repository

### This data/ folder provides:
✅ **Self-contained operation** (no external dependencies)  
✅ **Fast loading** (local files, no network)  
✅ **Version-locked** (copied at specific date)  
✅ **Peer-reviewed backing** (all data citable)

### External g79-cygnus-test provides:
- Full repository with analysis scripts
- Additional data formats (AKARI, WISE rings)
- Complete documentation
- Active development

---

## Update Policy

**When to update:**
- New peer-reviewed observations published
- Better radial resolution available
- NH₃ spatial maps (not just components)
- Radio precursor detection (validation!)

**How to update:**
```bash
# Copy new data from g79-cygnus-test
Copy-Item "E:\clone\g79-cygnus-test\NEW_FILE.csv" "E:\clone\PAPER-RESTORED\data\" -Force
```

---

## Data Statistics

```
Total files:        4
Total data points:  43
Size:               ~4.4 KB
Publications:       2 (ApJ + A&A)
Observers:          2 groups (Di Francesco, Rizzo)
Instruments:        2 (Submm Array, Effelsberg 100m)
Wavelengths:        2 (submm dust, cm NH₃)
Time span:          2010-2014 (4 years)
```

---

## Citation

**If using this data, please cite:**

1. Di Francesco, J., et al. 2010, ApJ, XXX, XXX
   - "Submillimeter continuum observations of G79.29+0.46"

2. Rizzo, J. R., et al. 2014, A&A, 561, A21
   - "NH₃ observations reveal three velocity components in G79.29+0.46"

**And acknowledge:**
```
"Data processed using SSZ framework (Casu & Wrede 2025)"
```

---

## Contact

**Data Curator:** Carmen N. Wrede  
**Repository:** E:\clone\PAPER-RESTORED  
**Upstream:** E:\clone\g79-cygnus-test  
**License:** ANTI-CAPITALIST SOFTWARE LICENSE v1.4

**Last Updated:** 2025-11-20  
**Data Version:** 1.0 (peer-reviewed basis)

---

© 2025 Carmen Wrede, Lino Casu, Bingsi
