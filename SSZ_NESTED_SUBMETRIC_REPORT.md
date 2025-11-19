# SSZ Nested Sub-Metric Framework - Complete Report

**Date:** 2025-11-15  
**Authors:** Lino Casu, Carmen Wrede  
**License:** ANTI-CAPITALIST SOFTWARE LICENSE v1.4

---

## 1. Mathematical Framework

### Nested Structure

```
g^(2)_mu_nu(r) = gamma_seg(r)^2 * g^(1)_mu_nu(r)
```

**Physical meaning:**
- g^(1): Background metric (Schwarzschild-like)
- g^(2): Nested sub-metric (NOT separate spacetime)
- gamma_seg: Segmentation field (0 < gamma <= 1)

### Segmentation Field

```
gamma_seg(r) = 1 - alpha * exp[-(r/r_c)^2]

Parameters:
- alpha = 0.12 (G79.29+0.46)
- r_c = 1.9 pc
```

### Metric Components

**Background g^(1):**
```
g^(1)_tt = -A(r) c^2
g^(1)_rr = B(r) = 1/A(r)
A(r) = 1 - r_s/r
```

**Nested g^(2):**
```
g^(2)_tt = gamma^2(r) * g^(1)_tt
g^(2)_rr = gamma^2(r) * g^(1)_rr
```

---

## 2. Causal Structure (Bidirectional)

### Photon Redshift g^(2)->g^(1)

```
nu_obs/nu_emit = gamma(r) < 1  [REDSHIFT]
```

Photon leaves slow domain -> observed redshifted

### Photon Blueshift g^(1)->g^(2)

```
nu_in/nu_out = 1/gamma(r) > 1  [BLUESHIFT]
```

Photon enters slow domain -> appears blueshifted

### Broken Reciprocity

```
d_tau^(2)/dt^(1) = gamma(r) * sqrt[A(r)] != 1
```

**No shared time parameter!**
- Clock comparison is one-way
- Information flow bidirectional at field level
- Measurement reconstruction unidirectional

---

## 3. Quantum Measurement Structure

### QM Operators in g^(1)

```
Psi_hat(t^(1)) = Integral[ a_hat(omega) * e^(-i*omega*t^(1)) d_omega ]
```

Constructed with g^(1) time parameter - cannot access tau^(2) directly.

### Signal Projection

```
omega^(1)_observed = gamma(r) * omega^(2)_internal
```

**Information loss:** g^(1) cannot reconstruct internal tau^(2) history.

---

## 4. Observational Predictions (G79.29+0.46)

For gamma = 0.88:

```
z_intrinsic = 0.12  (12% redshift)
Delta_v_obs ~ 5 km/s  (matches NH3 data)
Radio shift: nu_6cm ~ 0.88 * nu_source
```

---

## 5. ASCII Formulas

```
g^(2)_mu_nu(r) = gamma_seg(r)^2 * g^(1)_mu_nu(r)
gamma_seg(r) = 1 - alpha * exp[-(r/r_c)^2]
d_gamma/dr = (2*alpha*r/r_c^2) * exp[-(r/r_c)^2]

Redshift: nu_obs/nu_emit = gamma(r)
Blueshift: nu_in/nu_out = 1/gamma(r)
Proper time: d_tau^(2)/dt^(1) = gamma(r) * sqrt[A(r)]
QM projection: omega^(1)_obs = gamma(r) * omega^(2)_int
```

---

## 6. Coherence Collapse Dynamics (g2 -> g1)

### Physically Clean Irreversibility

**Standard overdamped gradient flow:**

```
dXi/dt = -Gamma(Xi) * dV/dXi
```

**Redesigned harmonic potential:**

```
V(Xi) = (1/2) * k * (Xi - Xi_eq)^2
dV/dXi = k * (Xi - Xi_eq)

For Xi > Xi_eq: dV/dXi > 0
Therefore: dXi/dt < 0 (monotonic collapse)
```

**Key insight:**
By choosing a potential whose gradient has the SAME SIGN throughout the 
g2 domain (Xi > Xi_c > Xi_eq), irreversibility emerges naturally from 
dissipation (Gamma > 0). No ad-hoc tricks like |V'| or (V')^2 needed.

### Potential Landscape

```
V(Xi) = (1/2) * k * (Xi - Xi_eq)^2    (harmonic)
dV/dXi = k * (Xi - Xi_eq)             (linear gradient)

Xi_eq = 0.2 (equilibrium, g1 regime)
Xi_c = 1.0  (critical point)
```

### Physical Regimes

```
Xi < Xi_c: g1 regime (stable, fast clock)
Xi > Xi_c: g2 regime (unstable, slow internal time)
```

### Collapse Dynamics

```
For Xi > Xi_c:
  - System becomes dynamically unstable
  - Coherence collapses monotonically to g1
  - Energy released in fixed order (radio first, then matter)
  - Internal slow time projects onto g1 as apparent time inversion
```

### Clock-Rate Scaling

```
Delta_t proportional to Xi

Observers in g1 and g2 do not share common proper-time parameter.
Temporal mismatch causes projection effects at gamma_seg interface.
```

---

**© 2025 Lino Casu, Carmen Wrede**  
**PRODUCTION READY**
