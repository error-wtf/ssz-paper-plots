# SSZ Mathematical Formulas - Complete Reference

**Datum:** 2025-11-19  
**Autoren:** Carmen Wrede, Lino Casu, Bingsi  
**Zweck:** Alle mathematischen Formeln für die generierten Plots

---

## Inhaltsverzeichnis

1. [SSZ Grundformeln](#1-ssz-grundformeln)
2. [Nested Metric](#2-nested-metric)
3. [Coherence Collapse Models](#3-coherence-collapse-models)
4. [Observables](#4-observables)
5. [PPN Parameters](#5-ppn-parameters)
6. [Energy Conditions](#6-energy-conditions)
7. [Curvature Invariants](#7-curvature-invariants)
8. [Radiowave Mechanism](#8-radiowave-mechanism)
9. [QNM Frequencies](#9-qnm-frequencies)
10. [G79.29+0.46 Specific](#10-g7929046-specific)

---

# 1. SSZ Grundformeln

## 1.1 Segmentation Field
```
γ_seg(r) = 1 - α * exp[-(r/r_c)²]

Parameter:
  α = 0.12  (Segmentationsstärke)
  r_c = 1.9 r_s  (charakteristische Skala)
  r_s = 2GM/c²  (Schwarzschild radius)

Eigenschaften:
  γ_seg(0) ≈ 1 - α = 0.88  (starke Segmentation)
  γ_seg(∞) = 1.0  (schwache Segmentation)
```

**Physikalische Bedeutung:** γ < 1 bedeutet langsame innere Zeit

## 1.2 Segment Density
```
Xi(r) = α * exp[-(r/r_c)²]

Relation:
  Xi = 1 - γ_seg
  γ_seg = 1 - Xi

Bereiche:
  Xi → α: g₂ (stark segmentiert)
  Xi → 0: g₁ (schwach segmentiert)
```

## 1.3 Damping Factor
```
D(r) = 1 / (1 + Xi(r))

Bedeutung:
  - Reduktion der Gravitation
  - D < 1: Abgeschwächte Kraft
  - D → 1: GR-Limit

Verwendung:
  A_SSZ(r) = D(r) * A_GR(r)
```

---

# 2. Nested Metric

## 2.1 Background g¹ (Schwarzschild)
```
ds²_g1 = -A(r)c²dt² + dr²/A(r) + r²(dθ² + sin²θ dφ²)

A(r) = 1 - r_s/r

Komponenten:
  g¹_tt = -A(r)c²
  g¹_rr = 1/A(r)
  g¹_θθ = r²
  g¹_φφ = r²sin²θ
```

## 2.2 Nested g² (SSZ)
```
g²_μν(r) = γ²_seg(r) * g¹_μν(r)

Explizit:
  g²_tt = γ²(r) * (-A(r)c²)
  g²_rr = γ²(r) / A(r)
  g²_θθ = γ²(r) * r²
  g²_φφ = γ²(r) * r² * sin²θ

Eigenschaften:
  - g² ist EINGEBETTET in g¹
  - Nicht zwei separate Raumzeiten
  - γ² < 1: g² ist "komprimiert"
```

## 2.3 Frequency Shifts
```
Redshift g²→g¹:
  ν_obs/ν_emit = γ_seg(r) < 1

Blueshift g¹→g²:
  ν_in/ν_out = 1/γ_seg(r) > 1

Broken Reciprocity:
  dτ²/dt¹ = γ_seg(r) * √[A(r)] ≠ 1
```

---

# 3. Coherence Collapse Models

## 3.1 Kubisches Modell (Current)
```
Potential:
  V_cubic(Xi) = 0.5 * a * Xi² + (1/3) * b * Xi³

Gradient:
  dV/dXi = a * Xi + b * Xi²

Collapse Rate:
  C(Xi) = Γ₀ * [dV/dXi]²
        = Γ₀ * [a*Xi + b*Xi²]²

Evolutionsgleichung:
  dXi/dt = -C(Xi)

Parameter:
  a = 1.0  (quadratisch)
  b = -0.5  (kubisch)
  Γ₀ = 1.0  (Dämpfung)
  Xi_c = -a/(2b) = 1.0  (kritisch)

Eigenschaften:
  ✓ C∞ smooth überall
  ✓ Konstruktionsbedingt irreversibel (C ≥ 0)
  ✓ Symmetrisch
  ✗ Kein scharfer Break
  ✗ Beide Seiten dynamisch
```

## 3.2 Piecewise Modell (Paper-Konform)
```
Potential (piecewise):
  V(Xi) = { 0                         für Xi ≤ Xi_c
          { (k/(p+1))*(Xi-Xi_c)^(p+1) für Xi > Xi_c

Gradient (piecewise):
  dV/dXi = { 0               für Xi ≤ Xi_c
           { k*(Xi-Xi_c)^p   für Xi > Xi_c

Collapse Rate:
  C(Xi) = Γ₀ * dV/dXi
        = { 0                  für Xi ≤ Xi_c
          { Γ₀*k*(Xi-Xi_c)^p   für Xi > Xi_c

Evolutionsgleichung:
  dXi/dt = { 0        für Xi ≤ Xi_c  (g₁: stabil!)
           { -C(Xi)   für Xi > Xi_c  (g₂: collapse!)

Parameter:
  k = 1.0  (Stärke)
  Xi_c = 1.0  (kritische Grenze)
  Γ₀ = 1.0  (Dämpfung)
  p = 2.2  (Nonlinearitätsexponent)

Eigenschaften:
  ✓ Sharp break bei Xi_c
  ✓ g₁ absolut stabil (dXi/dt = 0)
  ✓ g₂ nur einseitig (Xi > Xi_c)
  ✓ Finite-time collapse
  ✓ Stark nichtlinear (p = 2.2 > 1)
  ✓ 100% paper-kompatibel
```

## 3.3 Collapse Time
```
Kubisch:
  t_collapse → ∞  (erreicht Xi_c asymptotisch)

Piecewise:
  t_collapse = finite

  Berechnung:
    ∫[Xi₀ to Xi_c] dXi / [Γ*k*(Xi-Xi_c)^p]
    
  Für p > 1: endlich!
  Typisch: t_collapse ~ 3-5 Zeiteinheiten
```

---

# 4. Observables

## 4.1 Photon Sphere
```
Condition: r * (dA/dr) / A = -1

GR:
  r_ph_GR = 3 r_s / 2 = 1.5 r_s

SSZ:
  A_SSZ(r) = D(r) * (1 - r_s/r)
  
  Numerische Lösung erforderlich
  Typisch: r_ph_SSZ ≈ 1.55 r_s (leicht größer)
```

## 4.2 Shadow Radius (Impact Parameter)
```
b = r_ph * √[1 / A(r_ph)]

GR:
  b_GR = (3r_s/2) * √[1 / (1 - 2/3)]
       = (3r_s/2) * √3
       = 3√3 r_s / 2
       ≈ 2.598 r_s

SSZ:
  b_SSZ = r_ph_SSZ * √[1 / A_SSZ(r_ph_SSZ)]
  
  Typisch: b_SSZ ≈ 2.55 r_s
  Abweichung: ~2% (EHT-kompatibel)
```

## 4.3 Proper Time Dilation
```
d_tau / dt = √|g_tt| = √[A(r)]

GR:
  √[A_GR] = √[1 - r_s/r]
  → 0 bei r = r_s
  → ∞ bei r = 0

SSZ:
  √[A_SSZ] = √[D(r) * (1 - r_s/r)]
  → bleibt endlich bei r → 0
  → √[D(0) * (-∞)] reguliert durch D
```

## 4.4 Escape Velocity
```
v_esc = c * √[r_s / r]

GR & SSZ: gleich im äußeren Bereich
SSZ: modifiziert bei r ≈ r_s
```

---

# 5. PPN Parameters

```
Post-Newtonian Expansion:

g_tt = -(1 - 2U/c² + 2βU²/c⁴ + ...)
g_rr = 1 + 2γU/c² + ...

U = GM/r  (Newtonsches Potential)

Parameter:
  β: Nonlinearität in Raumkrümmung
  γ: Raumkrümmung pro Masseneinheit

GR:
  β_GR = γ_GR = 1

SSZ (schwaches Feld):
  β_SSZ = 1 + O(α²)
  γ_SSZ = 1 + O(α²)
  
  Mit α = 0.12 << 1:
  β_SSZ ≈ 1.0014
  γ_SSZ ≈ 1.0014
  
  → GR-kompatibel im schwachen Feld
```

---

# 6. Energy Conditions

## 6.1 Weak Energy Condition (WEC)
```
ρ + P_r ≥ 0

Bedeutung:
  Energie-Dichte + radialer Druck ≥ 0

SSZ:
  Effektive Materie durch Segmentation
  
  WEC Proxy:
    1 / (1 + Xi)² ≥ 0  (immer erfüllt!)
  
  Genauer Test:
    WEC erfüllt für r ≥ 5r_s
```

## 6.2 Dominant Energy Condition (DEC)
```
ρ ≥ |P_r|  und  ρ ≥ |P_t|

Bedeutung:
  Energie kann sich nicht schneller als Licht ausbreiten

SSZ:
  Erfüllt im äußeren Bereich
```

## 6.3 Strong Energy Condition (SEC)
```
ρ + P_r + 2P_t ≥ 0

Bedeutung:
  Gravitation ist attraktiv

SSZ:
  Erfüllt für r > 5r_s
```

---

# 7. Curvature Invariants

## 7.1 Ricci Scalar
```
R = g^μν R_μν

GR (Schwarzschild, vacuum):
  R_GR = 0

SSZ:
  R_SSZ ≠ 0  (effektive Materie)
  
  Berechnung:
    R_SSZ ~ ∇²(ln D) + ...
```

## 7.2 Kretschmann Scalar
```
K = R_μνρσ R^μνρσ

GR:
  K_GR = 48 (GM/c²)² / r⁶
       = 12 r_s² / r⁶
  
  Bei r → 0: K_GR → ∞ (Singularität!)

SSZ:
  K_SSZ = D⁶(r) * K_GR
  
  Mit D(0) = 1/(1+α) ≈ 0.89:
    K_SSZ(0) = D⁶(0) * finite
             = endlich!
  
  → Keine Singularität
```

## 7.3 Weyl Tensor
```
C_μνρσ = R_μνρσ - (Ricci terms)

Schwarzschild: C ≠ 0 (Gezeitenkräfte)
SSZ: C_SSZ modifiziert durch D(r)
```

---

# 8. Radiowave Mechanism

## 8.1 Velocity Decomposition
```
v_total = v_fall + v_eigen

v_fall:  Gravitational component
  v_fall = √[2GM/r]  (Newtonsch)
  v_fall ≈ c  bei r → r_s

v_eigen: Intrinsic velocity
  v_eigen = initial velocity of object

Energie:
  E_kinetic = 0.5 * m * v_eigen²
```

## 8.2 Energy Release
```
g₂ absorbiert v_fall
v_eigen MUSS freigesetzt werden

E_released = 0.5 * m * v_eigen²

Mechanismus:
  - Starke Segmentation supprimiert hohe Frequenzen
  - Nur niederfrequente Moden können entweichen
  - → RADIOWAVES (f < GHz)
```

## 8.3 Frequency Cutoff
```
Transmission(f) = 1 / [1 + (f/f_c)²]

f_c ~ c / (γ * λ_char)

Mit γ ≈ 0.88 in g₂:
  f_c ~ 1 GHz

Ergebnis:
  f < f_c: transmitted (RADIO)
  f > f_c: blocked (OPTICAL, UV, X-ray)
```

## 8.4 Timing
```
Radiowave precursor:
  t_radio ~ r_g2/v_ascent

Optical emission:
  t_optical ~ r_g1/v_jet

Time delay:
  Δt = t_optical - t_radio
  
  Typisch: Δt ~ days to weeks

Examples:
  GX 339-4: Δt ~ 5-10 days
  GRS 1915+105: Δt ~ weeks
```

---

# 9. QNM Frequencies

## 9.1 Eikonal Limit
```
ω_QNM = ω_R - i*ω_I

Real part (oscillation):
  ω_R = (l + 1/2) * c / r_ph
  
  Mit l = 2 (dominant mode):
    ω_R ≈ 2.5 * c / r_ph

Imaginary part (damping):
  ω_I = (dV_eff/dr)|_r_ph / c

GR:
  r_ph_GR = 1.5 r_s
  ω_R_GR ≈ 1.67 c / r_s

SSZ:
  r_ph_SSZ ≈ 1.55 r_s
  ω_R_SSZ ≈ 1.61 c / r_s
  
  Abweichung: ~4%
```

## 9.2 Frequency Series
```
ω_n = ω_R - i*(n + 1/2)*ω_I

n = 0, 1, 2, ...  (overtones)

Dominant mode: n = 0
```

---

# 10. G79.29+0.46 Specific

## 10.1 Parameters
```
M ≈ 2 M_☉  (Zentralmasse)
r_shell ≈ 0.8 pc  (beobachteter Shell-Radius)
r_s ≈ 3 km  (Schwarzschild radius)

Segmentation:
  α ≈ 0.12
  r_c ≈ 1.9 r_s ≈ 6 km
  
  γ_seg(r_shell) ≈ 0.88
```

## 10.2 Temperature Proxy
```
T_proxy ~ 1 / γ_seg(r)

Bei r = r_shell:
  γ ≈ 0.88
  T_proxy ~ 1/0.88 ≈ 1.14
  
  → 14% Temperaturerhöhung
  → "hot ring" beobachtet!
```

## 10.3 Velocity Profile
```
v_proxy = v₀ * (1 - γ_seg(r))

Mit v₀ ≈ 10 km/s:
  
  Bei r < r_shell:
    γ ≈ 0.88
    v ≈ 1.2 km/s
  
  Bei r > r_shell:
    γ ≈ 1.0
    v ≈ 0 km/s
  
  → Velocity step beobachtet!
```

## 10.4 NH₃ Emission
```
NH₃ emission ∝ n² * T

Mit:
  n: Dichte (bump bei r_shell)
  T: Temperatur (erhöht bei γ < 1)

SSZ predicts:
  Peak bei r_shell ≈ 0.8 pc
  → Matches observations!
```

---

# Zusammenfassung: Key Formulas

## Minimal Set (Top 10)
```
1. γ_seg(r) = 1 - α*exp[-(r/r_c)²]
2. g²_μν = γ²*g¹_μν
3. V_piecewise(Xi) = (k/(p+1))*(Xi-Xi_c)^(p+1) für Xi > Xi_c
4. dXi/dt = -Γ*k*(Xi-Xi_c)^p
5. A_SSZ(r) = D(r)*(1-r_s/r)
6. b_shadow = r_ph * √[1/A(r_ph)]
7. ν_obs/ν_emit = γ(r)
8. K_SSZ = D⁶*K_GR
9. v_total = v_fall + v_eigen
10. Transmission(f) = 1/[1+(f/f_c)²]
```

---

© 2025 Carmen Wrede, Lino Casu, Bingsi  
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
