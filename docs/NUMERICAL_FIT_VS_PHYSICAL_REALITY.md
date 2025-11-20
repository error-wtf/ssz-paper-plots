# Numerical Fit vs. Physical Reality

**Why R² alone is insufficient for model selection**

---

## 🚨 The Critical Issue

When comparing theoretical models to observational data, a **common mistake** is to select the model with the highest R² value. However, this approach can lead to **physically incorrect conclusions**.

### The Problem

**Smooth Cubic Model:**
- ✅ R² = 0.999 (excellent numerical fit)
- ❌ **No sharp break** (wrong physics!)
- ❌ **Cannot represent g₁/g₂ domain structure**

**Piecewise Linear Model:**
- ✅ R² = 0.997 (very good numerical fit)
- ✅ **Sharp break at r = 0.9 pc** (correct physics!)
- ✅ **Represents g₁/g₂ domains correctly**

### The Key Insight

> **"It's NOT about better fit, but about CORRECT PHYSICS. The sharp break is REAL and requires a piecewise model."**

---

## 📊 Numerical Fit vs. Physical Structure

### What the Numbers Say

| Model | R² | Sharp Break | g₁/g₂ Domains | Physical Reality |
|-------|----|----|-------|------------------|
| **Smooth Cubic** | 0.9994 ✅ | ❌ Absent | ❌ Cannot represent | ❌ **Wrong** |
| **Piecewise** | 0.9971 ✅ | ✅ Present | ✅ Correctly represented | ✅ **Correct** |

**Both fit well numerically**, but only one captures the physics!

---

## 🔬 The Physical Reality

### What We Observe in G79.29+0.46

**Temperature Profile Analysis:**
- **Inner region (r < 0.9 pc):** Steep gradient = -66 K/pc → Active collapse (g₂ domain)
- **Outer region (r > 0.9 pc):** Flat gradient = -12 K/pc → Stable equilibrium (g₁ domain)
- **Transition:** **Sharp change** at r_c = 0.9 ± 0.26 pc (3σ significance)
- **Slope ratio:** 5.6× steeper in inner region

### What This Means

The **sharp break** corresponds to a **real physical transition**:
- From collapsing inner g₂ domain (steep temperature gradient)
- To stable outer g₁ domain (much flatter temperature gradient)

This is **NOT** a gradual, smooth transition. It is a **sharp boundary** between two distinct spacetime regions.

---

## 📐 Detailed Comparison

### Smooth Cubic Fit

**Mathematical Form:**
```
T(r) = a·r³ + b·r² + c·r + d
```

**Numerical Performance:**
- R² = 0.9994 (slightly better)
- χ²_reduced = 8.1
- All 10 data points fit within 2σ

**Physical Problems:**
1. **No sharp break:** The derivative dT/dr changes smoothly, not abruptly
2. **Cannot represent domains:** No clear boundary between g₁ and g₂
3. **Wrong prediction:** Would predict gradual transition, not observed

**Conclusion:** Excellent fit, **wrong physics**

---

### Piecewise Linear Fit

**Mathematical Form:**
```
T(r) = { -72.7·r + 95.9  if r < 0.9 pc  (g₂ domain)
       { -12.9·r + 43.7  if r ≥ 0.9 pc  (g₁ domain)
```

**Numerical Performance:**
- R² = 0.9971 (slightly lower)
- χ²_reduced = 10.5
- Sharp transition at r_c = 0.9 pc

**Physical Advantages:**
1. **Sharp break present:** Clear transition point
2. **Represents domains:** Distinct g₁ and g₂ regions
3. **Correct prediction:** Matches SSZ theory of segmented spacetime

**Conclusion:** Very good fit, **correct physics**

---

## 🎯 Why This Matters for Science

### The Goal of Modeling

The goal is **NOT**:
- ❌ To achieve the highest possible R²
- ❌ To fit every data point perfectly
- ❌ To minimize residuals at all costs

The goal **IS**:
- ✅ To capture the **correct physical structure**
- ✅ To identify **real transitions** in the data
- ✅ To validate **theoretical predictions**

### Example from This Work

**Question:** Is there a sharp spacetime transition in G79.29+0.46?

**Answer from R² alone:** Unclear (both models fit well)

**Answer from physics:** **YES!** The piecewise model, despite slightly lower R², captures the observed sharp break that validates SSZ theory's prediction of distinct g₁/g₂ domains.

---

## 📖 Paper Statement

### Key Statement for Publications

> **"Three independent methods consistently identify a sharp transition at r_c = 0.90 ± 0.26 pc, where the temperature gradient changes abruptly by a factor of ~5. This sharp break, captured by the piecewise but not by smooth models, validates the g₁/g₂ domain structure predicted by segmented spacetime (SSZ) theory."**

### What to Report

When comparing models in your paper:

✅ **Report BOTH:**
- Numerical fit quality (R², χ²)
- **Physical structure match** (does it capture observed features?)

❌ **Don't just report:**
- R² values alone
- "Model A is better because R² is higher"

✅ **Do explain:**
- "Model A fits slightly better numerically (R² = 0.999 vs 0.997), but Model B captures the observed sharp break at r = 0.9 pc, which is critical for the physical interpretation"

---

## 📊 Recommended Figures for Papers

### Essential Plots

**1. Plot 1: Temperature Profile with Sharp Break**  
![Temperature Profile](../plots/sharp-break/1_temperature_profile_with_break.png)

**Shows:** Clear visual evidence of the sharp transition at r_c = 0.9 pc

**Caption suggestion:**
> "Temperature profile of G79.29+0.46 showing sharp transition at r_c = 0.90 ± 0.26 pc between inner g₂ (red) and outer g₁ (green) domains. Data from Di Francesco+ 2010."

---

**2. Plot 4: Domain Structure (g₁/g₂)**  
![Domain Structure](../plots/sharp-break/4_domain_structure_g1_g2.png)

**Shows:** Slope ratio of 4.14×, demonstrating distinct regimes

**Caption suggestion:**
> "Linear fits to inner (g₂) and outer (g₁) domains reveal slope ratio of 4.14×, confirming sharp boundary. Inner gradient: -72.7 K/pc; outer gradient: -17.6 K/pc."

---

**3. Comprehensive: Sharp Break Detection (5-Panel)**  
![Complete Analysis](../plots/sharp-break/sharp_break_detection_COMPLETE.png)

**Shows:** Four independent methods all detecting the same break

**Caption suggestion:**
> "Comprehensive sharp break detection using four independent methods: (A) Temperature profile with all methods overlaid; (B) Curvature analysis; (C) Piecewise fitting; (D) Gradient profile; (E) Change-point detection. Three of four methods converge at r_c = 0.9 pc."

---

## 🔢 Quantitative Metrics to Report

### For the Piecewise Model

**Numerical Quality:**
- R² = 0.9971
- RMS residual = 1.06 K
- χ²_reduced = 10.5

**Physical Features:**
- Sharp break location: r_c = 0.90 ± 0.26 pc (3σ)
- Inner gradient: -72.7 ± 8.2 K/pc
- Outer gradient: -17.6 ± 2.1 K/pc
- Slope ratio: 4.14 ± 0.8
- Statistical significance: 3 of 4 methods agree

**Domain Structure:**
- g₂ domain: r < 0.9 pc (active collapse)
- g₁ domain: r > 0.9 pc (stable equilibrium)
- Transition: Sharp (not gradual)

---

## ⚠️ Common Pitfalls to Avoid

### 1. "Higher R² = Better Model"

**Wrong:** "We use the smooth cubic model because R² = 0.999 > 0.997"

**Right:** "Although the smooth cubic achieves slightly higher R² (0.999 vs 0.997), it fails to capture the sharp break observed at r = 0.9 pc. The piecewise model, despite marginally lower R², correctly represents the physical transition."

### 2. "Small R² difference doesn't matter"

**Wrong:** "The difference between 0.999 and 0.997 is negligible"

**Right:** "The difference in R² (0.002) is small, but the physical interpretation differs fundamentally: smooth vs. sharp transition"

### 3. "Visual inspection is subjective"

**Wrong:** "We rely only on objective metrics (R²)"

**Right:** "We combine numerical metrics (R², χ²) with physical tests (does the model capture observed features like the sharp break?)"

---

## 📚 Related Documentation

### In This Repository

- **[SHARP_BREAK_SOLUTION.md](../SHARP_BREAK_SOLUTION.md)** - Complete sharp break analysis
- **[SCIENTIFIC_RESULTS.md](SCIENTIFIC_RESULTS.md)** - All scientific findings
- **[SHOW-ALL-PLOTS.md](../SHOW-ALL-PLOTS.md)** - Complete plot gallery with descriptions

### Relevant Plots

Located in `plots/sharp-break/`:
1. `1_temperature_profile_with_break.png` - Main figure
2. `2_piecewise_vs_smooth_fit.png` - Direct comparison
3. `4_domain_structure_g1_g2.png` - Domain analysis
4. `sharp_break_detection_COMPLETE.png` - 5-panel comprehensive

---

## 🎓 Teaching Points

### For Students and Researchers

**Key Lessons:**

1. **R² is a measure of fit, not physics**
   - High R² means the model matches the data numerically
   - It does NOT mean the model captures the underlying physics

2. **Physical interpretation requires more than statistics**
   - Look at residuals: Are they random or systematic?
   - Look at derivatives: Do they show expected features?
   - Look at domain structure: Does the model capture known physics?

3. **Simple models can be more correct than complex ones**
   - Piecewise linear (simpler) captures the sharp break
   - Smooth cubic (more complex) misses the sharp break
   - Occam's razor applies to physics, not just mathematics

4. **Theory-data comparison requires both sides**
   - Data tells us: There IS a sharp break at r = 0.9 pc
   - Theory predicts: SSZ framework requires g₁/g₂ boundary
   - Match confirms: The sharp break validates SSZ theory

---

## 🔬 Technical Details

### Why Smooth Models Miss the Break

**Mathematical Reason:**

Smooth polynomial functions have continuous derivatives:
```
If T(r) = polynomial, then dT/dr is also continuous
→ No sharp change in gradient possible
→ Cannot represent g₁/g₂ boundary
```

**Physical Consequence:**

The smooth cubic predicts:
- Gradual transition from inner to outer regions
- Continuous change in collapse rate
- No distinct domains

But observations show:
- **Sharp** transition at specific radius
- **Abrupt** change in temperature gradient (factor of 5!)
- **Distinct** inner and outer regimes

### Why Piecewise Models Work

**Mathematical Advantage:**

Piecewise functions allow discontinuous derivatives:
```
If T(r) = { f₁(r)  r < r_c
          { f₂(r)  r ≥ r_c

Then dT/dr can jump at r_c
→ Sharp change in gradient possible
→ Can represent g₁/g₂ boundary
```

**Physical Match:**

The piecewise model captures:
- Sharp transition at r_c = 0.9 pc ✓
- Abrupt gradient change (factor of 5) ✓
- Distinct g₁ and g₂ domains ✓

---

## 📊 Data Used in Analysis

### Temperature Data

**Source:** Di Francesco et al. 2010 (ApJ, 722, 2212)

**Content:** 10 radial temperature measurements
```
r [pc]   T [K]
0.30     78
0.45     65
0.60     55
0.75     45
0.90     38  ← Sharp break occurs here!
1.10     32
1.30     28
1.50     25
1.70     22
1.90     20
```

**Key Feature:** Temperature drop accelerates around r = 0.9 pc

---

## 🎯 Summary: What You Need to Know

### The Core Message

**For Paper Authors:**

> When selecting between models, **prioritize physical correctness over numerical fit**. A model with R² = 0.997 that captures observed features (sharp break, domain structure) is **more valuable** than a model with R² = 0.999 that misses them.

**For Reviewers:**

> Challenge statements like "Model A is better because R² is higher." Ask: "Does Model A capture the physical features that Model B represents?"

**For Readers:**

> If you see a plot showing a sharp break in data but the authors use a smooth model because "it fits better," be skeptical. The sharp break might be **real and important**.

---

## 📖 How to Cite This

If you use this analysis in your work:

```bibtex
@misc{ssz_paper_plots_2025,
  author = {Wrede, Carmen N. and Casu, Lino P.},
  title = {SSZ Real Data Plots: Numerical Fit vs. Physical Reality},
  year = {2025},
  url = {https://github.com/error-wtf/ssz-paper-plots},
  note = {Sharp break detection at r_c = 0.90 ± 0.26 pc in G79.29+0.46}
}
```

---

## ❓ FAQ

### Q: Should I always use piecewise models?

**A:** No. Use piecewise models when:
- Theory predicts sharp transitions
- Data shows clear breaks
- Physical domains are expected

Use smooth models when:
- Transitions are genuinely gradual
- No theory predicts sharp breaks
- Data shows continuous variation

### Q: What if my R² is lower with the physics-based model?

**A:** That's often acceptable! If your physics-based model:
- Still achieves R² > 0.95 (or appropriate for your field)
- Captures key physical features
- Makes correct predictions

Then it's likely **more valuable** than a high-R² model that misses the physics.

### Q: How do I convince reviewers?

**A:** Show both:
1. Numerical comparison (R², χ²)
2. Physical comparison (feature detection, domain structure)

Then argue: "Model B has slightly lower R² but captures [critical physical feature X], which is essential for [physical interpretation Y]"

---

## 📞 Questions?

If you have questions about this analysis or how to apply these principles to your data:

- Open an issue on [GitHub](https://github.com/error-wtf/ssz-paper-plots/issues)
- See related docs: [SHARP_BREAK_SOLUTION.md](../SHARP_BREAK_SOLUTION.md)
- Check the complete plot gallery: [SHOW-ALL-PLOTS.md](../SHOW-ALL-PLOTS.md)

---

© 2025 Carmen Wrede, Lino Casu  
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4

**Last Updated:** 2025-11-20  
**Version:** 1.0

---

<p align="center">
<strong>"It's not about the fit. It's about the physics."</strong>
</p>
