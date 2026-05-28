#!/usr/bin/env python3
"""
Projected Performance Graphs + Fine-Tuning Guidance
For the HDD Platter Flow Conditioner.

Generates sensitivity plots showing effects of:
- HVAT brake position (swirl control)
- Orifice diameter
- Inlet pressure / flow rate
- Gap size (design time)

Also outputs tuning recommendations.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT_DIR = "illustrations/performance_graphs"
os.makedirs(OUT_DIR, exist_ok=True)

def cavitation_number(v_jet, p_upstream=101325, p_vapor=2330):
    rho = 998.0
    return (p_upstream - p_vapor) / (0.5 * rho * v_jet**2)

def plot_performance_curves():
    fig, axes = plt.subplots(2, 2, figsize=(12, 9))
    fig.suptitle("Projected Performance Sensitivity — HDD Platter Flow Conditioner\n"
                 "(Default 25 platters @ 1.0 mm gap)", fontsize=12, fontweight='bold')

    # 1. Cavitation Number vs Orifice + Pressure
    ax1 = axes[0, 0]
    pressures = [0.3, 0.6, 1.0, 1.5]  # bar
    orifices = [6, 8, 10, 12]
    
    for p in pressures:
        v = np.linspace(1.5, 7.5, 50)
        sigma = cavitation_number(v, p_upstream=101325 + p*1e5)
        ax1.plot(v, sigma, label=f"{p} bar inlet")
    
    ax1.axhline(2.0, color='red', linestyle='--', alpha=0.6, label="Typical inception σ ≈ 2")
    ax1.set_xlabel("Jet velocity at orifice (m/s)")
    ax1.set_ylabel("Cavitation number σ")
    ax1.set_title("Effect of Inlet Pressure on Cavitation Intensity")
    ax1.legend(fontsize=8)
    ax1.grid(True, alpha=0.3)

    # 2. Effect of HVAT Brake (qualitative swirl reduction)
    ax2 = axes[0, 1]
    brake = np.linspace(0, 100, 100)  # 0 = free, 100 = locked
    swirl_reduction = 30 + 55 * (brake / 100)**0.7   # illustrative model
    jet_coherence = 40 + 50 * (brake / 100)**0.6
    
    ax2.plot(brake, swirl_reduction, 'b-', label="Residual swirl reduction (%)")
    ax2.plot(brake, jet_coherence, 'g-', label="Jet axial coherence (est.)")
    ax2.set_xlabel("HVAT Brake Position (% locked)")
    ax2.set_ylabel("Effect (%)")
    ax2.set_title("HVAT Brake Tuning Effect (Most Powerful Knob)")
    ax2.legend(fontsize=8)
    ax2.grid(True, alpha=0.3)
    ax2.axvline(35, color='purple', linestyle=':', alpha=0.7, label="Recommended starting point (~35%)")
    ax2.legend(fontsize=8)

    # 3. Reynolds Number vs Gap (design choice)
    ax3 = axes[1, 0]
    gaps = np.linspace(0.6, 1.8, 50)
    re_at_0_8bar = 1200 * (0.8 / gaps)   # rough scaling
    ax3.plot(gaps, re_at_0_8bar, 'r-', linewidth=2)
    ax3.axhline(2300, color='orange', linestyle='--', label="~Transition to turbulence")
    ax3.set_xlabel("Inter-platter gap (mm)")
    ax3.set_ylabel("Reynolds number in gap (at 0.8 bar)")
    ax3.set_title("Gap Size Impact on Flow Regime (Build-time Decision)")
    ax3.legend(fontsize=8)
    ax3.grid(True, alpha=0.3)

    # 4. Tuning Map
    ax4 = axes[1, 1]
    ax4.axis('off')
    tuning_text = """
FINE TUNING GUIDE (Most Impactful Adjustments)

1. HVAT BRAKE (Highest leverage)
   • 0-25%: Maximum swirl, more chaotic bubbles
   • 30-45%: Recommended starting zone (good coherence)
   • 60-100%: Very straight jet, lower vorticity

2. ORIFICE DIAMETER
   • 6 mm → Highest velocity, strongest cavitation
   • 8 mm → Balanced (good starting point)
   • 10-12 mm → Gentler, larger bubbles

3. INLET PRESSURE
   • <0.4 bar: Visualization & low-intensity work
   • 0.6-1.0 bar: Standard operating range
   • >1.2 bar: High intensity (watch heating)

4. GAS TYPE (Major variable)
   • Air: Baseline
   • Argon: Brighter sonoluminescence
   • Deuterium-enriched: LENR-leaning experiments

Start here:
- 8 mm orifice
- 0.7-0.9 bar inlet
- HVAT brake ~35% locked
- Observe through viewport first
"""
    ax4.text(0.02, 0.98, tuning_text, transform=ax4.transAxes, fontsize=8,
             verticalalignment='top', family='monospace',
             bbox=dict(boxstyle='round', facecolor='#eafaf1', edgecolor='#27ae60'))

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "performance_sensitivity.png"), dpi=160, bbox_inches='tight')
    plt.savefig(os.path.join(OUT_DIR, "performance_sensitivity.svg"), bbox_inches='tight')
    plt.close()
    print("  → performance_sensitivity.png + .svg")

    # === NEW: What-if scenarios with strong disclaimers ===
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle("Simulated 'What-If' Performance (Software Estimates Only — Not CFD or Experimental Data)\n"
                 "These curves are directional guidance based on simplified analytical models. Real behavior will vary.", 
                 fontsize=11, fontweight='bold', color='#c0392b')

    # Left: Effect of number of discs on estimated flow uniformity (qualitative model)
    ax1 = axes[0]
    num_discs = np.arange(10, 45, 2)
    uniformity_index = 60 + 35 * (1 - np.exp(-0.08 * (num_discs - 10)))   # saturating improvement
    ax1.plot(num_discs, uniformity_index, 'b-o', markersize=4)
    ax1.set_xlabel("Number of Discs")
    ax1.set_ylabel("Estimated Flow Uniformity Index (arbitrary units)")
    ax1.set_title("More Discs → Better Channel-to-Channel Uniformity\n(plateaus around 30–35 discs)")
    ax1.grid(True, alpha=0.3)
    ax1.axvline(25, color='gray', linestyle='--', alpha=0.6, label="Default (25)")
    ax1.legend()

    # Right: Combined effect of gap + nozzle angle on estimated swirl at exit
    ax2 = axes[1]
    gaps = [0.8, 1.0, 1.3, 1.6]
    angles = np.linspace(5, 18, 50)
    for g in gaps:
        # Very rough model: tighter gaps + smaller angle = more swirl reduction before HVAT
        swirl = 70 - 25*np.log10(angles) * (1.4 - g)  
        ax2.plot(angles, np.clip(swirl, 20, 90), label=f"{g} mm gap")

    ax2.set_xlabel("Nozzle Angle from Tangent (°)")
    ax2.set_ylabel("Estimated Residual Swirl at Exit (qualitative)")
    ax2.set_title("Gap + Nozzle Angle Interaction on Pre-HVAT Swirl\n(Tighter gaps + shallower angles retain more organized swirl)")
    ax2.legend(title="Gap size", fontsize=8)
    ax2.grid(True, alpha=0.3)

    plt.figtext(0.5, 0.01, 
                "DISCLAIMER: These are simplified model outputs for exploration only. They do not replace physical testing or proper CFD. "
                "Actual results depend on surface finish, alignment precision, inlet conditions, fluid properties, and many other factors.",
                ha="center", fontsize=8, style='italic', color='#c0392b',
                bbox=dict(boxstyle="round", facecolor="#fff3cd", alpha=0.9))

    plt.tight_layout(rect=[0, 0.08, 1, 0.95])
    plt.savefig(os.path.join(OUT_DIR, "whatif_scenarios.png"), dpi=160, bbox_inches='tight')
    plt.savefig(os.path.join(OUT_DIR, "whatif_scenarios.svg"), bbox_inches='tight')
    plt.close()
    print("  → whatif_scenarios.png + .svg (with strong disclaimers)")

if __name__ == "__main__":
    print("Generating performance sensitivity graphs...")
    plot_performance_curves()
    print(f"\nGraphs saved to {OUT_DIR}/")