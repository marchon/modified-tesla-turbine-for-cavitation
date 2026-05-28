#!/usr/bin/env python3
"""
Generate key diagrams for the HDD Platter Flow Conditioner project.

Includes matplotlib figures + TikZ source code for high-quality LaTeX inclusion.
Run: python3 python/generate_diagrams.py
"""

import os
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Arc, Wedge, Rectangle
import numpy as np

OUT_DIR = "diagrams"
LATEX_FIG_DIR = "latex/figures"
os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(LATEX_FIG_DIR, exist_ok=True)

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
    ax.set_title("HDD Platter Flow Conditioner — Cross Section (schematic)", pad=10)

    platter_y = np.linspace(-22, 22, 7)
    for y in platter_y:
        ax.plot([-42, 42], [y, y], color='#2c3e50', linewidth=2.5, solid_capstyle='round')

    housing = FancyBboxPatch((-52, -28), 104, 56, boxstyle="round,pad=0.02,rounding_size=4",
                             facecolor='#ecf0f1', edgecolor='#34495e', linewidth=1.5, alpha=0.6)
    ax.add_patch(housing)

    for sign in [-1, 1]:
        ax.add_patch(patches.Rectangle((42, sign*8), 18, 6, angle=sign*12,
                                       facecolor='#e74c3c', edgecolor='#c0392b', linewidth=1, alpha=0.85))
        ax.annotate('', xy=(44, sign*11), xytext=(58, sign*14),
                    arrowprops=dict(arrowstyle='->', color='#c0392b', lw=1.8))

    ax.add_patch(Circle((0, 0), 14, facecolor='#3498db', edgecolor='#2980b9', linewidth=1.5, alpha=0.35))
    ax.text(0, 0, "HVAT\nrotor", ha='center', va='center', fontsize=8, fontweight='bold', color='#1a5276')

    ax.plot([14, 32], [10, 18], color='#27ae60', linewidth=2)
    ax.plot([14, 32], [-10, -18], color='#27ae60', linewidth=2)
    ax.fill_between([14, 32], [-10, -18], [10, 18], alpha=0.2, color='#27ae60')
    ax.text(24, 0, "Diffuser", ha='center', va='center', fontsize=8, color='#1e8449')

    ax.annotate('', xy=(38, 0), xytext=(32, 0),
                arrowprops=dict(arrowstyle='->', color='#8e44ad', lw=2.5))
    ax.text(42, 4, "to cavitation\nchamber", ha='left', va='bottom', fontsize=7, color='#6c3483')

    ax.text(-48, 30, "Tangential\nnozzles (×6 @ ~10°)", ha='left', fontsize=7, color='#922b21')
    ax.text(-40, -32, "25 polished Enterprise platters\n1.0 mm gaps (default)", ha='left', fontsize=7, color='#2c3e50')

    ax.annotate('', xy=(-42, -25), xytext=(42, -25),
                arrowprops=dict(arrowstyle='<->', color='gray', lw=0.8))
    ax.text(0, -30, "95 mm OD platters", ha='center', fontsize=7, color='gray')

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "cross_section_schematic.png"), bbox_inches='tight')
    plt.savefig(os.path.join(OUT_DIR, "cross_section_schematic.svg"), bbox_inches='tight')
    plt.close()
    print("Wrote cross_section_schematic.*")


def plot_cavitation_number():
    fig, ax = plt.subplots(figsize=(7, 4))
    v = np.linspace(0.5, 8, 200)
    p_atm = 101325
    p_vap = 2330

    for throat_mm, label in [(6, "6 mm"), (8, "8 mm (baseline)"), (10, "10 mm"), (12, "12 mm")]:
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
    fig, ax = plt.subplots(figsize=(7, 4))
    flow_lpm = np.linspace(2, 40, 100)
    gap = 1.0

    effective_area_air = 0.00035
    v_air = (flow_lpm / 60000.0) / effective_area_air
    Re_air = 1.225 * v_air * (gap/1000) / 1.81e-5
    ax.plot(flow_lpm, Re_air, label="Air (1 mm gap)")

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


def draw_nozzle_angle_diagram():
    """Simple diagram showing nozzle angle from true tangential."""
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.set_xlim(-5, 55)
    ax.set_ylim(-5, 55)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title("Nozzle Angle Recommendation (~10° from Tangent)")

    # Draw a simplified disc edge arc
    theta = np.linspace(0, 90, 100)
    r = 40
    x = r * np.cos(np.radians(theta))
    y = r * np.sin(np.radians(theta))
    ax.plot(x, y, 'k-', linewidth=2, label="Platter edge")

    # True tangential
    ax.annotate('', xy=(0, 40), xytext=(20, 40),
                arrowprops=dict(arrowstyle='->', color='blue', lw=2))
    ax.text(10, 43, "True tangential (0°)", color='blue', fontsize=9)

    # 10° nozzle
    angle = 10
    ax.annotate('', xy=(0, 40), xytext=(20, 40 + 20*math.tan(math.radians(angle))),
                arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax.text(22, 48, "Recommended\n~8–12° (10° default)", color='red', fontsize=9)

    # Angle arc
    arc = Arc((0, 40), 15, 15, angle=90, theta1=0, theta2=angle, color='green', lw=1.5)
    ax.add_patch(arc)
    ax.text(8, 48, "10°", color='green', fontsize=10)

    ax.text(5, 10, "Tangential inlets create the\ninward spiral via boundary layer", fontsize=8, style='italic')

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "nozzle_angle.png"), bbox_inches='tight')
    plt.savefig(os.path.join(OUT_DIR, "nozzle_angle.svg"), bbox_inches='tight')
    plt.close()
    print("Wrote nozzle_angle.*")


def write_tikz_sources():
    """Write high-quality TikZ source files for inclusion in the LaTeX report."""
    # Simple cross-section TikZ
    tikz_cross = r"""
% tikz_cross_section.tex
% Include with \input{latex/figures/tikz_cross_section.tex}
\begin{tikzpicture}[scale=0.7]
  % Platters
  \foreach \y in {-2.2,-1.1,0,1.1,2.2} {
    \draw[thick] (-4.2,\y) -- (4.2,\y);
  }
  % Housing
  \draw[rounded corners, fill=gray!10] (-5.2,-3) rectangle (5.2,3);
  % HVAT
  \draw[fill=blue!30] (0,0) circle (1.4);
  \node at (0,0) {HVAT};
  % Diffuser
  \draw[thick, green!60!black] (1.4,1) -- (3.2,1.8);
  \draw[thick, green!60!black] (1.4,-1) -- (3.2,-1.8);
  % Exit arrow
  \draw[->, thick, purple] (3.2,0) -- (4.5,0) node[right] {to chamber};
  % Nozzles (simplified)
  \draw[fill=red!70] (4.2,0.8) -- (5.5,1.2) -- (5.5,0.6) -- (4.2,0.4);
  \draw[fill=red!70] (4.2,-0.8) -- (5.5,-1.2) -- (5.5,-0.6) -- (4.2,-0.4);
\end{tikzpicture}
"""
    with open(os.path.join(LATEX_FIG_DIR, "tikz_cross_section.tex"), "w") as f:
        f.write(tikz_cross)

    # Nozzle angle TikZ
    tikz_angle = r"""
% tikz_nozzle_angle.tex
\begin{tikzpicture}[scale=0.8]
  \draw[thick] (0,0) arc (0:90:4);
  \draw[->, blue, thick] (4,0) -- (4,1.5) node[above] {True tangent (0°)};
  \draw[->, red, thick] (4,0) -- (3.7,1.8) node[above] {10° (recommended)};
  \draw[green!60!black, thick] (4,0) arc (0:10:0.8);
  \node at (4.8,0.6) {10°};
\end{tikzpicture}
"""
    with open(os.path.join(LATEX_FIG_DIR, "tikz_nozzle_angle.tex"), "w") as f:
        f.write(tikz_angle)

    print("Wrote TikZ sources to latex/figures/")


if __name__ == "__main__":
    print("Generating project diagrams and TikZ sources...")
    draw_cross_section()
    plot_cavitation_number()
    plot_reynolds()
    draw_nozzle_angle_diagram()
    write_tikz_sources()
    print(f"\nAll diagrams + TikZ written.")
