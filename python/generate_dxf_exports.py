#!/usr/bin/env python3
"""
Lightweight DXF Export Generator
For key 2D profiles from the HDD Platter Flow Conditioner project.

Since no ezdxf/dxfwrite is installed, this produces valid minimal DXF files
using pure text (ASCII DXF R12 format). Suitable for laser cutters, CNC,
or import into FreeCAD / Inkscape / Fusion 360.

Focuses on flat parts that benefit most from 2D cutting:
- Spacer rings
- Shipping inserts
- Orifice inserts
- Clear viewport / covers (bolt patterns)

Run: python3 python/generate_dxf_exports.py
"""

import os
import math

OUT_DIR = "dxf_exports"
os.makedirs(OUT_DIR, exist_ok=True)

def write_dxf_header(f):
    f.write("999\nHDD Platter Flow Conditioner - 2D Fabrication Profiles\n")
    f.write("0\nSECTION\n2\nHEADER\n")
    f.write("9\n$ACADVER\n1\nAC1009\n")  # DXF R12
    f.write("0\nENDSEC\n")
    f.write("0\nSECTION\n2\nENTITIES\n")

def write_dxf_footer(f):
    f.write("0\nENDSEC\n0\nEOF\n")

def circle(f, cx, cy, r, layer="CUT"):
    f.write(f"0\nCIRCLE\n8\n{layer}\n")
    f.write(f"10\n{cx}\n20\n{cy}\n40\n{r}\n")

def text(f, x, y, txt, layer="ANNOTATE", height=3.0):
    f.write(f"0\nTEXT\n8\n{layer}\n")
    f.write(f"10\n{x}\n20\n{y}\n40\n{height}\n")
    f.write(f"1\n{txt}\n")

def write_spacer_ring_dxf(filename, od=95.0, id=30.0, thickness=1.0, num_lightening=6):
    """Spacer ring with layers + annotations."""
    path = os.path.join(OUT_DIR, filename)
    with open(path, "w") as f:
        write_dxf_header(f)
        circle(f, 0, 0, od/2, "CUT")
        circle(f, 0, 0, id/2, "CUT")
        for i in range(num_lightening):
            angle = math.radians(i * 360 / num_lightening + 30)
            hx = 32 * math.cos(angle)
            hy = 32 * math.sin(angle)
            circle(f, hx, hy, 3.0, "CUT")
        text(f, -25, -42, "SPACER 1.0mm - CUT OUTER + HOLES", "ANNOTATE", 2.5)
        text(f, -25, -48, "Material: PETG or thin sheet", "ANNOTATE", 2.0)
        write_dxf_footer(f)
    print(f"  → {filename}")

def write_orifice_insert_dxf(filename, outer_d=12.0, throat_d=8.0):
    path = os.path.join(OUT_DIR, filename)
    with open(path, "w") as f:
        write_dxf_header(f)
        circle(f, 0, 0, outer_d/2, "CUT")
        circle(f, 0, 0, throat_d/2, "CUT")
        text(f, -5.5, -7.5, f"ORIFICE INSERT Ø{throat_d}mm", "ANNOTATE", 2.2)
        write_dxf_footer(f)
    print(f"  → {filename}")

def write_viewport_bolt_pattern_dxf(filename, od=123.0, bolt_circle_r=39.0, num_bolts=6, hole_d=4.2):
    """Bolt pattern for viewport / end plates with annotations."""
    path = os.path.join(OUT_DIR, filename)
    with open(path, "w") as f:
        write_dxf_header(f)
        circle(f, 0, 0, od/2, "CUT")
        for i in range(num_bolts):
            angle = math.radians(i * 360 / num_bolts + 15)
            bx = bolt_circle_r * math.cos(angle)
            by = bolt_circle_r * math.sin(angle)
            circle(f, bx, by, hole_d/2, "DRILL")
        text(f, -28, -52, "VIEWPORT / END PLATE BOLT CIRCLE", "ANNOTATE", 2.5)
        text(f, -28, -58, "6x M4 holes @ 39mm radius", "ANNOTATE", 2.0)
        write_dxf_footer(f)
    print(f"  → {filename}")

if __name__ == "__main__":
    print("Generating DXF fabrication profiles...")
    write_spacer_ring_dxf("spacer_ring_1mm.dxf", od=95, id=30, thickness=1.0)
    write_orifice_insert_dxf("orifice_8mm.dxf", outer_d=12, throat_d=8)
    write_orifice_insert_dxf("orifice_6mm.dxf", outer_d=12, throat_d=6)
    write_orifice_insert_dxf("orifice_10mm.dxf", outer_d=12, throat_d=10)
    write_orifice_insert_dxf("orifice_12mm.dxf", outer_d=12, throat_d=12)
    write_viewport_bolt_pattern_dxf("viewport_bolt_pattern.dxf")
    print(f"\nDXF files written to {OUT_DIR}/ (importable into most CAD/CAM software)")
    print("Note: These are 2D profiles only. For full 3D, use the OpenSCAD source files.")
