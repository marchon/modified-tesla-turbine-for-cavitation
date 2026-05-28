#!/usr/bin/env python3
"""
Generate key diagrams for the HDD Platter Flow Conditioner project.

Run from repo root:
    python -m python.generate_diagrams

Outputs go to diagrams/ (SVG + PNG where sensible).
"""

import os
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Arc, Wedge
import numpy as np

OUT_DIR = "diagrams"
os.makedirs(OUT_DIR, exist_ok=True)

plt.rcParams.update({
    "figure.dpi": 150,
    "savefig.dpi": 150,
    "font.size": 9,
    "axes.grid": True,
    "grid.alpha": 0.3,
})


def draw_cross_section():
    """Schematic cross-section of the platter stack + nozzles + HVAT + diffuser."""
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.set_xlim(-70, 70)
    ax.set_ylim(-45, 45)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title("HDD Platter Flow Conditioner — Cross Section (schematic, not to scale)", pad=10)

    # Platters (simplified discs)
    platter_y = np.linspace(-22, 22, 7)
    for y in platter_y:
        ax.plot([-42, 42], [y, y], color='#2c3e50', linewidth=2.5, solid_capstyle='round')

    # Housing
    housing = FancyBboxPatch((-52, -28), 104, 56, boxstyle="round,pad=0.02,rounding_size=4",
                             facecolor='#ecf0f1', edgecolor='#34495e', linewidth=1.5, alpha=0.6)
    ax.add_patch(housing)

    # Nozzles (6, shown as 2 in section)
    for sign in [-1, 1]:
        # Nozzle body
        ax.add_patch(patches.Rectangle((42, sign*8), 18, 6, angle=sign*12,
                                       facecolor='#e74c3c', edgecolor='#c0392b', linewidth=1, alpha=0.85))
        # Arrow showing tangential-ish inlet
        ax.annotate('', xy=(44, sign*11), xytext=(58, sign*14),
                    arrowprops=dict(arrowstyle='->', color='#c0392b', lw=1.8))

    # Central HVAT region (simplified rotor)
    ax.add_patch(Circle((0, 0), 14, facecolor='#3498db', edgecolor='#2980b9', linewidth=1.5, alpha=0.35))
    ax.text(0, 0, "HVAT\nrotor", ha='center', va='center', fontsize=8, fontweight='bold', color='#1a5276')

    # Diffuser
    ax.plot([14, 32], [10, 18], color='#27ae60', linewidth=2)
    ax.plot([14, 32], [-10, -18], color='#27ae60', linewidth=2)
    ax.fill_between([14, 32], [-10, -18], [10, 18], alpha=0.2, color='#27ae60')
    ax.text(24, 0, "Diffuser", ha='center', va='center', fontsize=8, color='#1e8449')

    # Exit jet
    ax.annotate('', xy=(38, 0), xytext=(32, 0),
                arrowprops=dict(arrowstyle='->', color='#8e44ad', lw=2.5))
    ax.text(42, 4, "to cavitation\nchamber", ha='left', va='bottom', fontsize=7, color='#6c3483')

    # Labels
    ax.text(-48, 30, "Tangential\nnozzles (×6 @ ~10°)", ha='left', fontsize=7, color='#922b21')
    ax.text(-40, -32, "25 polished Enterprise platters\n1.0 mm gaps (default)", ha='left', fontsize=7, color='#2c3e50')

    # Dimension arrows
    ax.annotate('', xy=(-42, -25), xytext=(42, -25),
                arrowprops=dict(arrowstyle='<->', color='gray', lw=0.8))
    ax.text(0, -30, "95 mm OD platters", ha='center', fontsize=7, color='gray')

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "cross_section_schematic.png"), bbox_inches='tight')
    plt.savefig(os.path.join(OUT_DIR, "cross_section_schematic.svg"), bbox_inches='tight')
    plt.close()
    print("Wrote cross_section_schematic.*")


def plot_cavitation_number():
    """Cavitation number vs jet velocity for several orifice sizes."""
    fig, ax = plt.subplots(figsize=(7, 4))

    v = np.linspace(0.5, 8, 200)  # m/s
    p_atm = 101325
    p_vap = 2330  # water ~20°C

    for throat_mm, label in [(6, "6 mm"), (8, "8 mm (baseline)"), (10, "10 mm"), (12, "12 mm")]:
        # Simple Bernoulli-style velocity scaling (illustrative only)
        # Assume fixed upstream pressure drop for the example
        sigma = (p_atm - p_vap) / (0.5 * 998 * v**2)
        ax.plot(v, sigma, label=f"Orifice {label}")

    ax.axhline(2.0, color='red', linestyle='--', alpha=0.6, label="Typical inception threshold (σ ≈ 2)")
    ax.set_xlabel("Jet velocity at orifice (m/s)")
    ax.set_ylabel("Cavitation number σ")
    ax.set_title("Cavitation Number vs. Exit Velocity (water, 1 atm)")
    ax.legend(loc='upper right', fontsize=8)
    ax.set_xlim(0.5, 8)
    ax.set_ylim(0, 12)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "cavitation_number.png"), bbox_inches='tight')
    plt.savefig(os.path.join(OUT_DIR, "cavitation_number.svg"), bbox_inches='tight')
    plt.close()
    print("Wrote cavitation_number.*")


def plot_reynolds():
    """Reynolds number in the gaps vs. flow rate (air and water examples)."""
    fig, ax = plt.subplots(figsize=(7, 4))

    flow_lpm = np.linspace(2, 40, 100)
    gap = 1.0  # mm

    # Very rough area estimate for 24 gaps around 95 mm mean radius
    # This is illustrative only
    effective_area_air = 0.00035  # m² (tuned to give reasonable Re)
    v_air = (flow_lpm / 60000.0) / effective_area_air
    Re_air = 1.225 * v_air * (gap/1000) / 1.81e-5

    ax.plot(flow_lpm, Re_air, label="Air (1 mm gap)")

    # Water example (much higher Re)
    effective_area_water = 0.00012
    v_water = (flow_lpm / 60000.0) / effective_area_water
    Re_water = 998 * v_water * (gap/1000) / 0.001
    ax.plot(flow_lpm, Re_water / 50, label="Water (1 mm gap, /50 for scale)")

    ax.axhline(2000, color='orange', linestyle=':', alpha=0.7, label="~Laminar–turbulent transition (air)")
    ax.set_xlabel("Total volume flow (L/min)")
    ax.set_ylabel("Reynolds number (gap height)")
    ax.set_title("Approximate Reynolds Number in Inter-Platter Gaps")
    ax.legend(fontsize=8)
    ax.set_yscale('log')
    ax.grid(True, alpha=0.3, which='both')

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "reynolds_number.png"), bbox_inches='tight')
    plt.savefig(os.path.join(OUT_DIR, "reynolds_number.svg"), bbox_inches='tight')
    plt.close()
    print("Wrote reynolds_number.*")


if __name__ == "__main__":
    print("Generating project diagrams...")
    draw_cross_section()
    plot_cavitation_number()
    plot_reynolds()
    print(f"\nAll diagrams written to {OUT_DIR}/")
