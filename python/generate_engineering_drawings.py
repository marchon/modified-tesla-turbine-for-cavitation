#!/usr/bin/env python3
"""
Engineering Drawings & Part Illustrations Generator
For the HDD Platter Precision Flow Conditioner project.

Generates:
- Professional orthographic engineering drawings (multi-view with dimensions)
- Pictorial / isometric simulations of the 3D printed parts
- Exploded assembly view
- Assembled device illustration

All dimensions are for the default 25-platter configuration from the design conversation.
Outputs high-resolution PNG + SVG suitable for docs, LaTeX, and fabrication.

Run: python3 python/generate_engineering_drawings.py
"""

import os
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, Polygon, FancyArrowPatch, Arc
from matplotlib.lines import Line2D
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.patheffects as path_effects

OUT_DIR = "illustrations"
os.makedirs(OUT_DIR, exist_ok=True)

# Common style for engineering drawings (thin/thick lines, no color except annotations)
plt.rcParams.update({
    "figure.dpi": 180,
    "savefig.dpi": 180,
    "font.family": "DejaVu Sans",
    "font.size": 8,
    "axes.linewidth": 0.6,
})


def save_fig(fig, basename):
    """Save both PNG and SVG."""
    png = os.path.join(OUT_DIR, f"{basename}.png")
    svg = os.path.join(OUT_DIR, f"{basename}.svg")
    fig.savefig(png, bbox_inches='tight', pad_inches=0.15, facecolor='white')
    fig.savefig(svg, bbox_inches='tight', pad_inches=0.15, facecolor='white')
    plt.close(fig)
    print(f"  → {basename}.png + .svg")


def draw_dimension(ax, start, end, text, offset=3, arrow_style='<->', text_offset=0.8):
    """Draw a dimension line with arrows and text."""
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    length = math.hypot(dx, dy)
    if length == 0:
        return

    # Perpendicular offset
    nx, ny = -dy / length, dx / length
    p1 = (start[0] + nx * offset, start[1] + ny * offset)
    p2 = (end[0] + nx * offset, end[1] + ny * offset)

    ax.annotate('', xy=p2, xytext=p1,
                arrowprops=dict(arrowstyle=arrow_style, color='black', lw=0.7,
                                mutation_scale=6))
    mid = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
    ax.text(mid[0] + nx * text_offset, mid[1] + ny * text_offset, text,
            fontsize=7, ha='center', va='center', color='#1a5276',
            rotation=math.degrees(math.atan2(dy, dx)))


# =============================================================================
# 1. MAIN HOUSING + NOZZLES (most complex)
# =============================================================================
def generate_housing_drawing():
    fig = plt.figure(figsize=(11, 8))
    fig.suptitle("HDD Platter Flow Conditioner — Main Housing + Tangential Nozzles\n"
                 "Engineering Drawing (Default: 25 platters, 95 mm OD, 6× nozzles @ 10°)", 
                 fontsize=11, fontweight='bold', y=0.98)

    # --- TOP VIEW (orthographic) ---
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.set_title("TOP VIEW", fontsize=9, fontweight='bold')
    ax1.set_aspect('equal')
    ax1.set_xlim(-65, 65)
    ax1.set_ylim(-65, 65)
    ax1.set_xlabel("X (mm)")
    ax1.set_ylabel("Y (mm)")

    # Housing outline (top)
    housing = Circle((0, 0), 52, fill=False, color='black', linewidth=1.2)
    ax1.add_patch(housing)
    inner = Circle((0, 0), 48.5, fill=False, color='black', linewidth=0.6, linestyle='--')
    ax1.add_patch(inner)

    # 6 Nozzles (top view)
    for i in range(6):
        angle = i * 60 + 30
        rad = math.radians(angle)
        # Nozzle position
        nx = 48 * math.cos(rad)
        ny = 48 * math.sin(rad)
        # Draw nozzle rectangle (simplified)
        w = 8
        l = 14
        corners = [
            (nx + w/2 * math.cos(rad + math.pi/2), ny + w/2 * math.sin(rad + math.pi/2)),
            (nx - w/2 * math.cos(rad + math.pi/2), ny - w/2 * math.sin(rad + math.pi/2)),
            (nx - w/2 * math.cos(rad + math.pi/2) + l * math.cos(rad), 
             ny - w/2 * math.sin(rad + math.pi/2) + l * math.sin(rad)),
            (nx + w/2 * math.cos(rad + math.pi/2) + l * math.cos(rad), 
             ny + w/2 * math.sin(rad + math.pi/2) + l * math.sin(rad)),
        ]
        poly = Polygon(corners, closed=True, fill=False, edgecolor='#c0392b', linewidth=1.0)
        ax1.add_patch(poly)

    # Center HVAT opening
    ax1.add_patch(Circle((0, 0), 17, fill=False, color='#2980b9', linewidth=1.0, linestyle='--'))
    ax1.text(0, 0, "HVAT\nOpening\nØ28", ha='center', va='center', fontsize=6, color='#2980b9')

    ax1.grid(True, alpha=0.2, linestyle=':')
    ax1.axhline(0, color='gray', lw=0.3)
    ax1.axvline(0, color='gray', lw=0.3)

    # --- FRONT VIEW ---
    ax2 = fig.add_subplot(2, 2, 2)
    ax2.set_title("FRONT VIEW (Section A-A)", fontsize=9, fontweight='bold')
    ax2.set_aspect('equal')
    ax2.set_xlim(-55, 55)
    ax2.set_ylim(-40, 40)
    ax2.set_xlabel("X (mm)")
    ax2.set_ylabel("Z (mm)")

    # Housing body (rectangle)
    ax2.add_patch(Rectangle((-52, -28), 104, 56, fill=False, edgecolor='black', linewidth=1.2))
    # Inner cavity
    ax2.add_patch(Rectangle((-48.5, -24), 97, 48, fill=False, edgecolor='black', linewidth=0.6, linestyle='--'))

    # Nozzles (front) — two visible
    for sign in [-1, 1]:
        ax2.add_patch(Rectangle((42, sign*3), 14, 6, fill=False, edgecolor='#c0392b', linewidth=1.0))

    # HVAT zone
    ax2.add_patch(Rectangle((-17, -17), 34, 34, fill=False, edgecolor='#2980b9', linewidth=1.0, linestyle='--'))
    ax2.text(0, 0, "HVAT\nZone", ha='center', va='center', fontsize=6, color='#2980b9')

    # Diffuser
    ax2.plot([17, 35], [12, 20], 'g-', lw=1.2)
    ax2.plot([17, 35], [-12, -20], 'g-', lw=1.2)
    ax2.text(26, 0, "Diffuser", ha='center', va='center', fontsize=6, color='green')

    ax2.grid(True, alpha=0.2, linestyle=':')

    # Dimensions
    draw_dimension(ax2, (-52, -32), (52, -32), "104 mm (housing OD)", offset=4)
    draw_dimension(ax2, (48, -28), (48, 28), "56 mm (height)", offset=6)

    # --- ISOMETRIC / PICTORIAL SIMULATION ---
    ax3 = fig.add_subplot(2, 2, 3, projection='3d')
    ax3.set_title("ISOMETRIC VIEW — 3D Printed Part Simulation", fontsize=9, fontweight='bold')

    # Simple 3D representation of housing
    # (approximate cylinder + nozzles)
    theta = np.linspace(0, 2*np.pi, 60)
    z = np.linspace(-28, 28, 20)
    T, Z = np.meshgrid(theta, z)
    X = 52 * np.cos(T)
    Y = 52 * np.sin(T)
    ax3.plot_surface(X, Y, Z, alpha=0.25, color='#bdc3c7', linewidth=0)

    # Inner cavity (wireframe)
    Xi = 48.5 * np.cos(T)
    Yi = 48.5 * np.sin(T)
    ax3.plot_wireframe(Xi, Yi, Z, alpha=0.4, color='#7f8c8d', linewidth=0.3)

    # Nozzles (simplified boxes)
    for i in range(6):
        a = i * 60 * np.pi / 180 + np.pi/6
        for dz in [-10, 10]:
            ax3.plot([48*np.cos(a), 62*np.cos(a)],
                     [48*np.sin(a), 62*np.sin(a)],
                     [dz, dz], color='#e74c3c', lw=2)

    ax3.set_xlabel("X (mm)")
    ax3.set_ylabel("Y (mm)")
    ax3.set_zlabel("Z (mm)")
    ax3.set_xlim(-70, 70)
    ax3.set_ylim(-70, 70)
    ax3.set_zlim(-40, 40)
    ax3.view_init(elev=22, azim=35)

    # --- NOTES BOX ---
    ax4 = fig.add_subplot(2, 2, 4)
    ax4.axis('off')
    notes = """
ENGINEERING NOTES (Default Config)

Material: PETG or ABS (FDM 3D printed)
Layer height: 0.2 mm
Infill: 30–40%

Key Dimensions
• Housing OD: 104 mm
• Internal cavity: Ø97 mm
• Height (stack + clamps): 56 mm
• 6× Tangential Nozzles @ 10° from tangent
• Nozzle exit width: 5.5 mm
• Central HVAT opening: Ø28 mm + clearance
• Wall thickness: 3.8 mm

Tolerances
• Critical bores: ±0.2 mm
• General: ±0.4 mm

Print orientation: Flat on base (no supports needed)
    """
    ax4.text(0.02, 0.98, notes, transform=ax4.transAxes, fontsize=7.5,
             verticalalignment='top', family='monospace',
             bbox=dict(boxstyle='round', facecolor='#f8f9fa', edgecolor='#dee2e6'))

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    save_fig(fig, "engineering_drawing_housing")


# =============================================================================
# 2. HVAT ROTOR
# =============================================================================
def generate_hvat_drawing():
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    fig.suptitle("HVAT Hybrid Rotor (Savonius + Helical Darrius)\n"
                 "Active Flow Straightener — 28 mm diameter × 60 mm height", 
                 fontsize=11, fontweight='bold')

    ax1, ax2, ax3, ax4 = axes.flatten()

    # Top view
    ax1.set_title("TOP VIEW", fontweight='bold')
    ax1.set_aspect('equal')
    ax1.set_xlim(-20, 20)
    ax1.set_ylim(-20, 20)
    for i in range(3):
        angle = i * 120
        rad = math.radians(angle)
        ax1.add_patch(Rectangle((9*math.cos(rad)-1, 9*math.sin(rad)-1), 2, 8, 
                                angle=angle, fill=False, edgecolor='#3498db', lw=1.2))
    ax1.add_patch(Circle((0,0), 4, fill=False, color='black', lw=1))
    ax1.grid(True, alpha=0.2)

    # Front view
    ax2.set_title("FRONT VIEW", fontweight='bold')
    ax2.set_aspect('equal')
    ax2.set_xlim(-18, 18)
    ax2.set_ylim(-35, 35)
    ax2.add_patch(Rectangle((-14, -30), 28, 60, fill=False, edgecolor='#3498db', lw=1.2))
    ax2.add_patch(Circle((0,0), 4, fill=False, color='black', lw=1))
    draw_dimension(ax2, (-14, -33), (14, -33), "28 mm dia", offset=3)
    draw_dimension(ax2, (16, -30), (16, 30), "60 mm height", offset=3)
    ax2.grid(True, alpha=0.2)

    # Isometric simulation
    ax3 = fig.add_subplot(2, 2, 3, projection='3d')
    ax3.set_title("ISOMETRIC — Printed Part Simulation", fontweight='bold')
    # Simple helical representation
    t = np.linspace(0, 4*np.pi, 200)
    for blade in range(3):
        phase = blade * 2*np.pi/3
        x = 10 * np.cos(t + phase)
        y = 10 * np.sin(t + phase)
        z = np.linspace(-30, 30, 200)
        ax3.plot(x, y, z, color='#3498db', lw=2.5)
    ax3.set_xlim(-18,18); ax3.set_ylim(-18,18); ax3.set_zlim(-35,35)
    ax3.view_init(25, 40)

    # Notes
    ax4.axis('off')
    notes = """
PARAMETERS (from conversation)
• Diameter: 28 mm
• Height: 60 mm
• 3× Helical Darrius blades (lift)
• 2× Savonius scoops at bottom (drag/start)
• Central bore: Ø4–5 mm for shaft
• Print: PETG, 0.2 mm layers, 35% infill

FUNCTION
Active flow straightener / vortex stabilizer
in the central exhaust of the platter stack.
Can be free-spinning, braked, or lightly driven.
"""
    ax4.text(0.05, 0.95, notes, transform=ax4.transAxes, fontsize=7.5,
             verticalalignment='top', family='monospace',
             bbox=dict(boxstyle='round', facecolor='#eaf2f8', edgecolor='#aed6f1'))

    plt.tight_layout()
    save_fig(fig, "engineering_drawing_hvat")


# =============================================================================
# 3. CAVITATION NOZZLE
# =============================================================================
def generate_nozzle_drawing():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5))
    fig.suptitle("Cavitation Jet Nozzle — Venturi + Interchangeable Orifice Inserts", fontsize=11, fontweight='bold')

    # Orthographic section
    ax1.set_title("SECTION VIEW — Venturi Profile", fontweight='bold')
    ax1.set_aspect('equal')
    ax1.set_xlim(-5, 55)
    ax1.set_ylim(-18, 18)

    # Body
    ax1.add_patch(Rectangle((0, -14), 45, 28, fill=False, edgecolor='black', lw=1.2))
    # Converging
    ax1.plot([5, 17], [12, 4], 'k-', lw=1.2)
    ax1.plot([5, 17], [-12, -4], 'k-', lw=1.2)
    # Throat
    ax1.add_patch(Rectangle((17, -4), 6, 8, fill=False, edgecolor='#e74c3c', lw=1.5))
    # Diverging
    ax1.plot([23, 43], [4, 9], 'k-', lw=1.2)
    ax1.plot([23, 43], [-4, -9], 'k-', lw=1.2)

    ax1.text(10, 0, "Inlet\nØ28", ha='center', va='center', fontsize=7)
    ax1.text(20, 0, "Throat\n(8 mm)", ha='center', va='center', fontsize=7, color='#c0392b')
    ax1.text(35, 0, "Outlet\nØ18", ha='center', va='center', fontsize=7)

    draw_dimension(ax1, (0, -16), (45, -16), "45 mm overall", offset=2)

    # Orifice family
    ax2.set_title("ORIFICE INSERT FAMILY (Interchangeable)", fontweight='bold')
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 50)
    ax2.axis('off')

    for i, d in enumerate([6, 8, 10, 12]):
        x = 12 + i * 22
        ax2.add_patch(Rectangle((x-6, 10), 12, 28, fill=False, edgecolor='#27ae60', lw=1.5))
        ax2.add_patch(Circle((x, 24), d/2, fill=False, edgecolor='#c0392b', lw=2))
        ax2.text(x, 5, f"Ø{d} mm", ha='center', fontsize=8, fontweight='bold')

    ax2.text(50, 42, "Print 4–6 inserts. Swap to tune\npressure drop and bubble intensity.", 
             ha='center', fontsize=8, style='italic')

    plt.tight_layout()
    save_fig(fig, "engineering_drawing_nozzle")


# =============================================================================
# 4. ASSEMBLY JIG
# =============================================================================
def generate_jig_drawing():
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title("Assembly Jig — Critical Tool for Precise Platter Stacking\n"
                 "Ensures perfectly uniform 1.0 mm gaps and alignment", fontsize=10, fontweight='bold')
    ax.set_aspect('equal')
    ax.set_xlim(-70, 70)
    ax.set_ylim(-70, 70)

    # Base
    ax.add_patch(Circle((0, 0), 55, fill=False, edgecolor='#2c3e50', lw=2))
    # Guide posts
    for angle in [45, 135, 225, 315]:
        rad = math.radians(angle)
        ax.add_patch(Circle((42*math.cos(rad), 42*math.sin(rad)), 6, fill=False, edgecolor='#e74c3c', lw=1.5))
    # Central clearance
    ax.add_patch(Circle((0, 0), 48, fill=False, edgecolor='gray', lw=1, linestyle='--'))

    ax.text(0, 0, "Central\nclearance\nfor stack", ha='center', va='center', fontsize=7, color='gray')
    ax.text(0, -62, "4× Guide Posts (Ø12 mm × 60 mm tall)", ha='center', fontsize=8)

    draw_dimension(ax, (-55, -50), (55, -50), "110 mm overall diameter", offset=8)
    plt.tight_layout()
    save_fig(fig, "engineering_drawing_jig")


# =============================================================================
# 5. Exploded Assembly View (the money shot)
# =============================================================================
def generate_exploded_view():
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title("EXPLODED ASSEMBLY VIEW — All Major 3D-Printed Components\n"
                 "HDD Platter Flow Conditioner (25-platter configuration)", fontsize=11, fontweight='bold')

    # Simplified exploded layers (Z positions represent assembly order)
    layers = [
        (0,  "Bottom End Plate + Bearing Houser", '#3498db'),
        (12, "Platter Stack (25× platters + 24 spacers)", '#2c3e50'),
        (28, "Top End Plate + Clear Viewport (optional)", '#27ae60'),
        (38, "HVAT Rotor + Shaft + Bearings", '#9b59b6'),
        (48, "Main Housing (with 6 tangential nozzles)", '#e74c3c'),
        (58, "Nozzle Manifold + Cavitation Jet Nozzle", '#f39c12'),
    ]

    for z, label, color in layers:
        ax.text(0, 0, z, label, fontsize=8, ha='center', va='center',
                bbox=dict(boxstyle='round,pad=0.3', facecolor=color, alpha=0.6), color='white', fontweight='bold')

    ax.set_xlim(-40, 40)
    ax.set_ylim(-40, 40)
    ax.set_zlim(-5, 70)
    ax.view_init(elev=18, azim=-55)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Assembly Direction (Z)")

    plt.tight_layout()
    save_fig(fig, "exploded_assembly")


# =============================================================================
# 6. Assembled Device Simulation
# =============================================================================
def generate_assembled_simulation():
    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title("ASSEMBLED DEVICE — Simulation of Final 3D-Printed + Platter Assembly\n"
                 "(with clear viewport installed for visualization)", fontsize=10, fontweight='bold')

    # Approximate outer housing
    theta = np.linspace(0, 2*np.pi, 50)
    z = np.linspace(-25, 35, 30)
    T, Z = np.meshgrid(theta, z)
    X = 52 * np.cos(T)
    Y = 52 * np.sin(T)
    ax.plot_surface(X, Y, Z, alpha=0.15, color='#95a5a6')

    # Platters (stacked discs)
    for i, zz in enumerate(np.linspace(-20, 20, 9)):
        r = np.linspace(0, 47, 20)
        th = np.linspace(0, 2*np.pi, 40)
        R, TH = np.meshgrid(r, th)
        XX = R * np.cos(TH)
        YY = R * np.sin(TH)
        ZZ = np.full_like(XX, zz)
        ax.plot_surface(XX, YY, ZZ, alpha=0.6, color='#34495e', linewidth=0)

    # HVAT (central)
    t = np.linspace(0, 6*np.pi, 120)
    for blade in range(3):
        phase = blade * 2*np.pi/3
        x = 9 * np.cos(t + phase)
        y = 9 * np.sin(t + phase)
        z = np.linspace(-15, 22, 120)
        ax.plot(x, y, z, color='#8e44ad', lw=2.2)

    ax.set_xlim(-60, 60)
    ax.set_ylim(-60, 60)
    ax.set_zlim(-30, 45)
    ax.view_init(elev=20, azim=42)
    ax.set_xlabel("X (mm)")
    ax.set_ylabel("Y (mm)")
    ax.set_zlabel("Z (mm)")

    plt.tight_layout()
    save_fig(fig, "assembled_device_simulation")


# =============================================================================
# 7. Bearing Housers (Upper + Lower)
# =============================================================================
def generate_bearing_housers_drawing():
    fig, axes = plt.subplots(1, 2, figsize=(11, 5))
    fig.suptitle("Bearing Housers — Upper & Lower (608ZZ)\nPress-fit + Flanged Mounting", fontsize=11, fontweight='bold')

    for idx, (ax, title, h) in enumerate([
        (axes[0], "UPPER BEARING HOUSER", 8),
        (axes[1], "LOWER BEARING HOUSER (thicker base)", 10)
    ]):
        ax.set_title(title, fontweight='bold')
        ax.set_aspect('equal')
        ax.set_xlim(-25, 25)
        ax.set_ylim(-5, 20)

        # Main cylinder (press fit bore)
        ax.add_patch(Rectangle((-12, 0), 24, h, fill=False, edgecolor='#2c3e50', lw=1.5))
        # Flange
        ax.add_patch(Rectangle((-16, 0), 32, 3, fill=False, edgecolor='#e67e22', lw=1.5))

        # Bore (for 608ZZ)
        ax.add_patch(Rectangle((-4.1, -1), 8.2, h+2, fill=False, edgecolor='#c0392b', lw=1.2, linestyle='--'))

        ax.text(0, h/2, "Ø24 mm\nPress-fit\nfor 608ZZ", ha='center', va='center', fontsize=7, color='#2c3e50')
        ax.text(0, 1.5, "Flange Ø32 mm", ha='center', fontsize=7, color='#e67e22')

        draw_dimension(ax, (-16, -3), (16, -3), "32 mm flange", offset=2)
        draw_dimension(ax, (13, 0), (13, h), f"{h} mm height", offset=3)

        ax.grid(True, alpha=0.2, linestyle=':')

    plt.tight_layout()
    save_fig(fig, "engineering_drawing_bearing_housers")


# =============================================================================
# 8. Spacers, Covers & Viewport (small but critical parts)
# =============================================================================
def generate_small_parts_drawing():
    fig = plt.figure(figsize=(12, 7))
    fig.suptitle("Small Critical Parts — Spacers, Shipping Inserts, Covers & Viewport", fontsize=11, fontweight='bold')

    # Spacer Ring
    ax1 = fig.add_subplot(2, 3, 1)
    ax1.set_title("SPACER RING (1.0 mm)", fontweight='bold')
    ax1.set_aspect('equal')
    ax1.set_xlim(-55, 55)
    ax1.set_ylim(-55, 55)
    ax1.add_patch(Circle((0, 0), 47.5, fill=False, edgecolor='#27ae60', lw=2))
    ax1.add_patch(Circle((0, 0), 15, fill=False, edgecolor='black', lw=1, linestyle='--'))
    for i in range(6):
        angle = i * 60 + 30
        rad = math.radians(angle)
        ax1.add_patch(Circle((32*math.cos(rad), 32*math.sin(rad)), 3, fill=False, edgecolor='gray', lw=0.8))
    ax1.text(0, 0, "1.0 mm\nthick", ha='center', va='center', fontsize=8)
    draw_dimension(ax1, (-47.5, -52), (47.5, -52), "95 mm OD", offset=5)

    # Shipping Insert
    ax2 = fig.add_subplot(2, 3, 2)
    ax2.set_title("SHIPPING INSERT (1.4 mm)", fontweight='bold')
    ax2.set_aspect('equal')
    ax2.set_xlim(-55, 55)
    ax2.set_ylim(-55, 55)
    ax2.add_patch(Circle((0, 0), 47.5, fill=False, edgecolor='#e74c3c', lw=2))
    ax2.add_patch(Circle((0, 0), 15, fill=False, edgecolor='black', lw=1, linestyle='--'))
    ax2.text(0, 0, "1.4 mm\n(thicker for\ntransport)", ha='center', va='center', fontsize=7, color='#c0392b')

    # Clear Viewport
    ax3 = fig.add_subplot(2, 3, 3)
    ax3.set_title("CLEAR VIEWPORT PLATE", fontweight='bold')
    ax3.set_aspect('equal')
    ax3.set_xlim(-60, 60)
    ax3.set_ylim(-60, 60)
    ax3.add_patch(Circle((0, 0), 61.5, fill=False, edgecolor='#3498db', lw=2))
    ax3.add_patch(Circle((0, 0), 17, fill=False, edgecolor='black', lw=1, linestyle='--'))
    for i in range(6):
        angle = i * 60 + 15
        rad = math.radians(angle)
        ax3.add_patch(Circle((39*math.cos(rad), 39*math.sin(rad)), 2.1, fill=False, edgecolor='black', lw=0.8))
    ax3.text(0, 0, "Clear PETG\n(for visual\ninspection)", ha='center', va='center', fontsize=7)

    # Solid Top Cover
    ax4 = fig.add_subplot(2, 3, 4)
    ax4.set_title("SOLID TOP COVER", fontweight='bold')
    ax4.set_aspect('equal')
    ax4.set_xlim(-60, 60)
    ax4.set_ylim(-60, 60)
    ax4.add_patch(Circle((0, 0), 61.5, fill=False, edgecolor='#7f8c8d', lw=2))
    for i in range(6):
        angle = i * 60 + 15
        rad = math.radians(angle)
        ax4.add_patch(Circle((39*math.cos(rad), 39*math.sin(rad)), 2.1, fill=False, edgecolor='black', lw=0.8))
    ax4.text(0, 0, "Solid cover\n(no viewport)", ha='center', va='center', fontsize=7)

    # Bottom Jet Cover
    ax5 = fig.add_subplot(2, 3, 5)
    ax5.set_title("BOTTOM JET COVER (with orifice)", fontweight='bold')
    ax5.set_aspect('equal')
    ax5.set_xlim(-60, 60)
    ax5.set_ylim(-60, 60)
    ax5.add_patch(Circle((0, 0), 61.5, fill=False, edgecolor='#7f8c8d', lw=2))
    ax5.add_patch(Circle((0, 0), 6, fill=False, edgecolor='#e74c3c', lw=2))
    ax5.text(0, 0, "Orifice\nØ6-12 mm", ha='center', va='center', fontsize=7, color='#c0392b')

    # Notes
    ax6 = fig.add_subplot(2, 3, 6)
    ax6.axis('off')
    notes = """
PRINT NOTES (all parts)
• Material: PETG preferred
• Layer: 0.2 mm
• Infill: 30-40%
• No supports needed on most

CRITICAL TOLERANCES
• Spacer thickness: ±0.05 mm
  (use good filament & calibration)
• Bearing bore: +0.10 mm interference
• All bolt holes: 4.2 mm (M4 clearance)
"""
    ax6.text(0.05, 0.95, notes, transform=ax6.transAxes, fontsize=7.2,
             verticalalignment='top', family='monospace',
             bbox=dict(boxstyle='round', facecolor='#fef9e7', edgecolor='#f4d03f'))

    plt.tight_layout()
    save_fig(fig, "engineering_drawing_small_parts")


# =============================================================================
# Main entry point
# =============================================================================
if __name__ == "__main__":
    print("Generating engineering drawings and part illustrations...")
    generate_housing_drawing()
    generate_hvat_drawing()
    generate_nozzle_drawing()
    generate_jig_drawing()
    generate_bearing_housers_drawing()
    generate_small_parts_drawing()
    generate_exploded_view()
    generate_assembled_simulation()
    print(f"\nAll illustrations written to {OUT_DIR}/")
    print("Open the PNGs or SVGs for high-quality engineering views and part simulations.")
