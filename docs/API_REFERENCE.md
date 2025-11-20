# API Reference - SSZ Plot Generation

**Complete code documentation for plot generation and data handling**

---

## 📚 Table of Contents

- [Core Modules](#core-modules)
- [Data Loading](#data-loading)
- [Plot Generation](#plot-generation)
- [Sharp Break Detection](#sharp-break-detection)
- [Custom Integration](#custom-integration)

---

## Core Modules

### `generate_all_real_data_plots_master.py`

**Main entry point for generating all plots**

```python
def generate():
    """
    Generate all 17 paper-ready plots from peer-reviewed data
    
    Returns:
        bool: True if successful, False otherwise
        
    Output:
        - plots/real-data/ (8 plots)
        - plots/sharp-break/ (6 plots)
        - plots/ (2 framework plots)
    """
```

**Usage:**
```python
python generate_all_real_data_plots_master.py
```

---

## Data Loading

### `find_data_directory()`

```python
def find_data_directory():
    """
    Locate data directory with observational files
    
    Priority:
        1. Local data/ folder (standalone)
        2. Sibling g79-cygnus-test directory
        3. External paths
        
    Returns:
        Path: Path to data directory
        
    Raises:
        FileNotFoundError: If no data directory found
    """
```

### `load_real_data(data_dir)`

```python
def load_real_data(data_dir):
    """
    Load all observational data from CSV files
    
    Args:
        data_dir (Path): Path to data directory
        
    Returns:
        dict: Dictionary with keys:
            - 'temperatures': G79 temperature DataFrame
            - 'nh3': NH3 velocity components DataFrame
            - 'gamma': Gamma_seg profile DataFrame
            - 'radio': Radio predictions DataFrame
            
    Data Sources:
        - G79_temperatures.csv: Di Francesco+ 2010
        - G79_Rizzo2014_NH3_Table1.csv: Rizzo+ 2014
        - G79_gamma_seg_profile.csv: Fitted profile
        - G79_radio_predictions.csv: SSZ predictions
    """
```

---

## Plot Generation

### Individual Plot Modules

Each plot module follows the same pattern:

```python
def generate(data, output_dir='plots/real-data/'):
    """
    Generate specific plot using loaded data
    
    Args:
        data (dict): Data dictionary from load_real_data()
        output_dir (str): Output directory path
        
    Returns:
        Path: Path to generated plot file
        
    Raises:
        ValueError: If required data missing
    """
```

### Available Plot Modules

**Real Data Plots:**
- `plots_real_collapse_rate.py` - Collapse rate analysis
- `plots_real_coherence.py` - Coherence evolution
- `plots_real_radio_timing.py` - Radio timing comparison
- `plots_real_compatibility.py` - Model compatibility
- `plots_real_potentials.py` - Potential landscapes
- `plots_real_collapse_4panel.py` - 4-panel collapse dynamics
- `plots_real_piecewise_4panel.py` - 4-panel piecewise model

**Example Usage:**
```python
from plots_real_collapse_rate import generate as gen_collapse

# Load data first
data = load_real_data(find_data_directory())

# Generate specific plot
plot_path = gen_collapse(data, output_dir='plots/real-data/')
print(f"Generated: {plot_path}")
```

---

## Sharp Break Detection

### `detect_sharp_break.py`

**Main sharp break detection module**

```python
def detect_sharp_break(r, T, methods=['curvature', 'piecewise', 'gradient', 'changepoint']):
    """
    Detect sharp break in temperature profile using multiple methods
    
    Args:
        r (array): Radial distances in pc
        T (array): Temperatures in K
        methods (list): Methods to use for detection
        
    Returns:
        dict: Results dictionary with:
            - 'r_c': Detected break radius (pc)
            - 'r_c_err': Uncertainty (pc)
            - 'significance': Statistical significance (sigma)
            - 'methods_agree': Number of methods agreeing
            - 'individual_results': Dict of results per method
            
    Methods:
        - 'curvature': Maximum curvature detection
        - 'piecewise': Optimal piecewise fit
        - 'gradient': Gradient change detection
        - 'changepoint': Bayesian changepoint detection
    """
```

**Example:**
```python
from detect_sharp_break import detect_sharp_break
import numpy as np
import pandas as pd

# Load G79 temperature data
df = pd.read_csv('data/G79_temperatures.csv')
r = df['r_pc'].values
T = df['T_K'].values

# Detect break
results = detect_sharp_break(r, T)

print(f"Break location: {results['r_c']:.2f} ± {results['r_c_err']:.2f} pc")
print(f"Significance: {results['significance']:.1f} sigma")
print(f"Methods agreeing: {results['methods_agree']}/4")
```

---

## Custom Integration

### Adding Your Own Data

**Step 1: Prepare CSV files**

```csv
# your_data.csv
r_pc,T_K
0.1,100
0.2,90
0.3,80
...
```

**Step 2: Create custom loader**

```python
import pandas as pd
from pathlib import Path

def load_custom_data(csv_path):
    """Load your custom observational data"""
    df = pd.read_csv(csv_path)
    
    # Validate required columns
    assert 'r_pc' in df.columns, "Missing r_pc column"
    assert 'T_K' in df.columns, "Missing T_K column"
    
    return {
        'temperatures': df,
        'source': 'Your Source et al. 2025'
    }
```

**Step 3: Generate plots with your data**

```python
from plots_real_collapse_rate import generate as gen_collapse

# Load your data
data = load_custom_data('path/to/your_data.csv')

# Generate plot
gen_collapse(data, output_dir='plots/custom/')
```

---

### Creating Custom Plots

**Template for new plot module:**

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Custom Plot Module: Your Plot Name

© 2025 Your Name
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
"""
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def generate(data, output_dir='plots/custom/'):
    """
    Generate your custom plot
    
    Args:
        data (dict): Data dictionary with required keys
        output_dir (str): Output directory
        
    Returns:
        Path: Path to generated plot
    """
    # Ensure output directory exists
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Extract data
    if 'temperatures' not in data:
        raise ValueError("Missing 'temperatures' in data")
    
    temp_df = data['temperatures']
    r = temp_df['r_pc'].values
    T = temp_df['T_K'].values
    
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Your plotting code here
    ax.plot(r, T, 'o-', label='Observations')
    
    # Customize
    ax.set_xlabel('Radius (pc)', fontsize=12)
    ax.set_ylabel('Temperature (K)', fontsize=12)
    ax.set_title('Your Custom Plot', fontsize=14, fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Save
    output_file = output_dir / 'your_custom_plot.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"✓ Generated: {output_file}")
    return output_file

if __name__ == '__main__':
    # Test generation
    from generate_all_real_data_plots_master import find_data_directory, load_real_data
    
    data = load_real_data(find_data_directory())
    generate(data)
```

---

## Data Structures

### Temperature Data

```python
DataFrame columns:
- r_pc: float       # Radius in parsecs
- T_K: float        # Temperature in Kelvin
```

### NH3 Velocity Data

```python
DataFrame columns:
- component: str              # Component name (Central/Blue/Red)
- v_min_kms: float           # Minimum velocity (km/s)
- v_max_kms: float           # Maximum velocity (km/s)
- Trot_K: float              # Rotation temperature (K)
- Trot_err_K: float          # Temperature uncertainty
- N_NH3_cm2: float           # Column density (cm^-2)
- N_NH3_err_cm2: float       # Density uncertainty
- Trot_limit_type: str       # 'measured' or 'lower_limit'
```

### Gamma Profile Data

```python
DataFrame columns:
- radius_pc: float           # Radius in parsecs
- T_data_K: float           # Observed temperature
- T_fit_K: float            # Fitted temperature
- gamma_seg: float          # γ_seg metric parameter
- residual_K: float         # Residual (data - fit)
```

### Radio Predictions

```python
DataFrame columns:
- time_days: float          # Time in days
- radio_flux: float         # Predicted radio flux
- mechanism: str            # Physical mechanism
- confidence: float         # Prediction confidence (0-1)
```

---

## Error Handling

### Common Errors

**FileNotFoundError:**
```python
try:
    data_dir = find_data_directory()
except FileNotFoundError:
    print("Data directory not found!")
    print("Please ensure data/ folder exists with CSV files")
```

**Missing Data:**
```python
if 'temperatures' not in data:
    raise ValueError("Required 'temperatures' key missing in data dict")
```

**Invalid Data:**
```python
if len(data['temperatures']) < 5:
    raise ValueError("Insufficient data points (need at least 5)")
```

---

## Performance Tips

### Batch Generation

```python
# Generate all plots in one go
generate()  # From master script

# Or selectively:
from plots_real_collapse_rate import generate as gen1
from plots_real_coherence import generate as gen2

data = load_real_data(find_data_directory())

gen1(data)
gen2(data)
# ... etc
```

### Memory Management

```python
import matplotlib.pyplot as plt

# Always close figures after saving
plt.savefig(output_file)
plt.close()  # Free memory

# Or use context manager
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
```

---

## Testing

### Unit Tests

```python
import pytest
from generate_all_real_data_plots_master import load_real_data, find_data_directory

def test_data_loading():
    """Test data can be loaded"""
    data_dir = find_data_directory()
    data = load_real_data(data_dir)
    
    assert 'temperatures' in data
    assert len(data['temperatures']) > 0
    
def test_plot_generation():
    """Test plot generation succeeds"""
    from plots_real_collapse_rate import generate
    
    data = load_real_data(find_data_directory())
    output = generate(data, output_dir='test_output/')
    
    assert output.exists()
    assert output.suffix == '.png'
```

Run tests:
```bash
pytest tests/ -v
```

---

## Dependencies

### Required

```python
numpy>=1.20.0
matplotlib>=3.3.0
scipy>=1.6.0
```

### Optional

```python
pandas>=1.2.0  # For DataFrame operations
pytest>=6.0.0  # For testing
```

Install:
```bash
pip install numpy matplotlib scipy
pip install pandas pytest  # optional
```

---

## Examples

See `examples/` directory for complete working examples:
- `examples/basic_usage.py` - Simple usage
- `examples/custom_plots.py` - Custom plot creation
- `examples/paper_figures.py` - Generate paper figures

---

## Troubleshooting

### Plot not generated?

1. Check data directory exists: `ls data/`
2. Verify CSV files present
3. Check output directory permissions
4. Review error messages

### Wrong data displayed?

1. Verify CSV file format
2. Check column names match expected
3. Validate data ranges (physical values)

### Low quality plots?

Change DPI:
```python
plt.savefig(output_file, dpi=300)  # Higher quality
```

---

## Support

- **Documentation:** [README.md](../README.md)
- **Issues:** [GitHub Issues](https://github.com/error-wtf/ssz-paper-plots/issues)
- **Email:** mail@error.wtf

---

© 2025 Carmen Wrede, Lino Casu  
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4

**Last Updated:** 2025-11-20
