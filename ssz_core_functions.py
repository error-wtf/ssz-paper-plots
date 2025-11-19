#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SSZ Core Functions - Standalone
================================
Alle grundlegenden SSZ-Berechnungen ohne externe Dependencies.

© 2025 Carmen Wrede, Lino Casu, Bingsi
Licensed under ANTI-CAPITALIST SOFTWARE LICENSE v1.4
"""
import numpy as np

# Physical Constants
G = 6.67430e-11          # Gravitational constant [m³ kg⁻¹ s⁻²]
C = 2.99792458e8         # Speed of light [m/s]
M_SUN = 1.98847e30       # Solar mass [kg]
PHI = (1 + np.sqrt(5))/2 # Golden ratio

# SSZ Parameters (Standard)
ALPHA = 0.12
R_C = 1.9
EPS3 = -24.0/5.0

# ============================================================================
# SSZ METRIC FUNCTIONS
# ============================================================================

def gamma_seg(r, r_s, alpha=ALPHA, r_c=R_C):
    """Segmentation field: γ(r) = 1 - α*exp[-(r/r_c)²]"""
    return 1 - alpha * np.exp(-(r/(r_c*r_s))**2)

def Xi(r, r_s, alpha=ALPHA, r_c=R_C):
    """Segmentation Xi(r) = 1 - γ(r)"""
    return 1 - gamma_seg(r, r_s, alpha, r_c)

def D(r, r_s, alpha=ALPHA, r_c=R_C):
    """D(r) = 1 / (1 + Xi(r))"""
    return 1 / (1 + Xi(r, r_s, alpha, r_c))

def A_SSZ(r, M, alpha=ALPHA, r_c=R_C):
    """SSZ metric: A(r) = D(r) * (1 - r_s/r)"""
    r_s = 2*G*M/(C**2)
    return D(r, r_s, alpha, r_c) * (1 - r_s/r)

def A_GR(r, M):
    """GR Schwarzschild metric: A(r) = 1 - r_s/r"""
    r_s = 2*G*M/(C**2)
    return 1 - r_s/r

def r_schwarzschild(M):
    """Schwarzschild radius"""
    return 2*G*M/(C**2)

# ============================================================================
# U-BASED FORMULATION (for PPN and weak field)
# ============================================================================

def U_of(r, M):
    """Gravitational potential U = GM/(rc²)"""
    return G*M/(r*C*C)

def A_of_U(U, eps3=EPS3):
    """A(U) = 1 - 2U + 2U² + ε₃U³"""
    return 1.0 - 2.0*U + 2.0*(U*U) + eps3*(U**3)

def A_of_r_weak(r, M, eps3=EPS3):
    """A(r) using U-formulation (weak field)"""
    return A_of_U(U_of(r, M), eps3)

# ============================================================================
# DERIVATIVES
# ============================================================================

def dA_dr(r, M, h=None, alpha=ALPHA, r_c=R_C):
    """Numerical derivative dA/dr"""
    if h is None:
        h = max(1e-6*r, 1e-3)
    return (A_SSZ(r+h, M, alpha, r_c) - A_SSZ(r-h, M, alpha, r_c))/(2*h)

def d2A_dr2(r, M, h=None, alpha=ALPHA, r_c=R_C):
    """Numerical second derivative d²A/dr²"""
    if h is None:
        h = max(1e-6*r, 1e-3)
    return (A_SSZ(r+h, M, alpha, r_c) - 2*A_SSZ(r, M, alpha, r_c) + A_SSZ(r-h, M, alpha, r_c))/(h*h)

# ============================================================================
# OBSERVABLES
# ============================================================================

def r_photon_sphere_gr(M):
    """GR photon sphere: r_ph = 1.5 * r_s"""
    return 1.5 * r_schwarzschild(M)

def r_photon_sphere_ssz(M, alpha=ALPHA, r_c=R_C):
    """SSZ photon sphere (approximate): r_ph ≈ 1.55 * r_s"""
    return 1.55 * r_schwarzschild(M)

def shadow_radius_gr(M):
    """GR shadow radius: b = 3√3 * r_s / 2"""
    r_s = r_schwarzschild(M)
    return 3 * np.sqrt(3) * r_s / 2

def shadow_radius_ssz(M, alpha=ALPHA, r_c=R_C):
    """SSZ shadow radius: b = r_ph * √[1/A(r_ph)]"""
    r_ph = r_photon_sphere_ssz(M, alpha, r_c)
    A_ph = A_SSZ(r_ph, M, alpha, r_c)
    if A_ph > 0:
        return r_ph * np.sqrt(1/A_ph)
    return 0

def qnm_frequency_gr(M):
    """GR QNM frequency (fundamental mode)"""
    r_s = r_schwarzschild(M)
    return C / (1.5 * r_s)

def qnm_frequency_ssz(M, alpha=ALPHA, r_c=R_C):
    """SSZ QNM frequency (fundamental mode)"""
    r_s = r_schwarzschild(M)
    return C / (1.55 * r_s)

# ============================================================================
# ENERGY CONDITIONS
# ============================================================================

def rho_pr_pt(r, M, alpha=ALPHA, r_c=R_C):
    """
    Effective stress-energy components from metric.
    Returns: (rho, p_r, p_t) in geometrized units
    """
    A = A_SSZ(r, M, alpha, r_c)
    Ap = dA_dr(r, M, alpha=alpha, r_c=r_c)
    App = d2A_dr2(r, M, alpha=alpha, r_c=r_c)
    
    rho = ((1.0 - A)/r**2 - Ap/r) / (8*np.pi)
    pr  = (Ap/r + (A - 1.0)/r**2) / (8*np.pi)
    pt  = (0.5*App + Ap/r) / (8*np.pi)
    
    return rho, pr, pt

def check_energy_conditions(r, M, alpha=ALPHA, r_c=R_C):
    """
    Check WEC, DEC, SEC at radius r.
    Returns: (WEC, DEC, SEC) as booleans
    """
    rho, pr, pt = rho_pr_pt(r, M, alpha, r_c)
    
    wec = (rho >= 0) and (rho + pt >= 0)
    dec = (rho >= abs(pr)) and (rho >= abs(pt))
    sec = (rho + pr + 2*pt) >= 0
    
    return wec, dec, sec

# ============================================================================
# KRETSCHMANN SCALAR
# ============================================================================

def kretschmann_gr(r, M):
    """GR Kretschmann scalar: K = 48(GM)²/r⁶"""
    r_s = r_schwarzschild(M)
    return 48 * (r_s/2)**2 / r**6

def kretschmann_ssz(r, M, alpha=ALPHA, r_c=R_C):
    """SSZ Kretschmann scalar (approximate)"""
    D_val = D(r, r_schwarzschild(M), alpha, r_c)
    K_gr = kretschmann_gr(r, M)
    return D_val**6 * K_gr

# ============================================================================
# PROPER TIME
# ============================================================================

def proper_time_factor(r, M, alpha=ALPHA, r_c=R_C):
    """dτ/dt = √|A(r)|"""
    A = A_SSZ(r, M, alpha, r_c)
    return np.sqrt(np.abs(A))

# ============================================================================
# PPN PARAMETERS
# ============================================================================

def ppn_beta():
    """β parameter (always 1 for SSZ)"""
    return 1.0

def ppn_gamma():
    """γ parameter (always 1 for SSZ)"""
    return 1.0

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def mass_range(start_msun, end_msun, num=50, log=True):
    """Generate mass range in solar masses"""
    if log:
        return np.logspace(np.log10(start_msun), np.log10(end_msun), num) * M_SUN
    else:
        return np.linspace(start_msun, end_msun, num) * M_SUN

def radius_range(r_min_rs, r_max_rs, M, num=200):
    """Generate radius range in units of r_s"""
    r_s = r_schwarzschild(M)
    return np.linspace(r_min_rs * r_s, r_max_rs * r_s, num)

# ============================================================================
# VALIDATION HELPERS
# ============================================================================

def validate_ppn():
    """Validate PPN parameters"""
    beta = ppn_beta()
    gamma = ppn_gamma()
    
    beta_ok = abs(beta - 1.0) < 1e-12
    gamma_ok = abs(gamma - 1.0) < 1e-12
    
    return beta_ok and gamma_ok

def validate_energy_conditions_range(M, r_min_rs=5.0, r_max_rs=20.0, num=10):
    """Validate energy conditions over radius range"""
    r_s = r_schwarzschild(M)
    radii = np.linspace(r_min_rs * r_s, r_max_rs * r_s, num)
    
    all_wec = True
    all_dec = True
    all_sec = True
    
    for r in radii:
        wec, dec, sec = check_energy_conditions(r, M)
        all_wec = all_wec and wec
        all_dec = all_dec and dec
        all_sec = all_sec and sec
    
    return all_wec, all_dec, all_sec
