# Quick Start Guide - SSZ Real Data Plots

**Get started in 5 minutes!**

---

## Step 1: Install Dependencies (1 minute)

```bash
pip install numpy matplotlib scipy pandas
```

**That's it!** No special libraries needed.

---

## Step 2: Generate All Plots (10 seconds)

```bash
cd E:\clone\PAPER-RESTORED
python generate_all_real_data_plots_master.py
```

**Output:**
```
Using data from: E:\clone\PAPER-RESTORED\data
✓ Loaded temperatures: 10 points
✓ Loaded nh3: 3 points
✓ Loaded gamma: 10 points
✓ Loaded radio: 20 points

Generating plots...
  ✓ 1_collapse_rate_REAL_DATA.png
  ✓ 2_coherence_evolution_REAL_DATA.png
  ✓ 3_radio_timing_REAL_DATA.png
  ✓ 4_model_compatibility_REAL_DATA.png
  ✓ 5_potential_landscapes_REAL_DATA.png
  ✓ 6_irreversible_collapse_4panel_REAL_DATA.png
  ✓ 7_piecewise_4panel_REAL_DATA.png

COMPLETE! Generated 7 plots in plots\real-data
```

---

## Step 3: View Results (instant)

```bash
cd plots/real-data/
explorer .   # Windows
open .       # macOS
nautilus .   # Linux
```

**You'll see 8 high-resolution PNG files:**
1. Collapse rate from real data
2. Coherence evolution
3. Radio timing comparison
4. **Model compatibility** (100% vs 60%) ⭐
5. Potential landscapes
6. Irreversible collapse (4-panel)
7. Piecewise model (4-panel)
8. Radiowave precursor predictions

---

## Step 4 (Optional): Sharp Break Detection

```bash
# Comprehensive analysis
python detect_sharp_break.py

# Individual plots
python generate_sharp_break_plots.py
```

**Output:** 7 plots in `plots/sharp-break/`

**Key Result:** Sharp break detected at r_c = 0.9 ± 0.26 pc (3σ)

---

## Next Steps

### For Papers
- Use plot 4 (model compatibility)
- Use plot 1 from sharp-break (temperature profile)
- Cite: Di Francesco+ 2010, Rizzo+ 2014

### For Presentations
- Plot 4: Shows 100% vs 60% compatibility
- Sharp-break plot 4: Shows g₁/g₂ domains

### For Analysis
```python
from generate_all_real_data_plots_master import load_real_data

data = load_real_data()
temp_df = data['temperatures']
# Do custom analysis
```

---

## Common Issues

### "ModuleNotFoundError"
```bash
pip install numpy matplotlib scipy
```

### "No such file or directory: data/G79_temperatures.csv"
Make sure you're in the `PAPER-RESTORED` directory:
```bash
cd E:\clone\PAPER-RESTORED
pwd  # Should show PAPER-RESTORED
```

### Plots look pixelated
Edit script and increase DPI:
```python
plt.savefig(output_file, dpi=300)  # Instead of 150
```

---

## That's It!

**Total time:** ~5 minutes  
**Generated:** 15 plots (8 + 7)  
**All data:** Peer-reviewed publications  

**Ready for paper submission!** ✅

---

© 2025 Carmen Wrede, Lino Casu  
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
