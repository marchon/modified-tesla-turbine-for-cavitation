# Engineering Drawings & Part Illustrations

This page provides professional engineering drawings and visual simulations of every major 3D-printable component in the HDD Platter Precision Flow Conditioner.

All drawings are generated programmatically from the parametric dimensions defined in the OpenSCAD files (default 25-platter configuration).

## Main Housing + Tangential Nozzles

![Housing Engineering Drawing](_static/engineering_drawing_housing.png)

**Files:** `scad/HDD_Platter_Cavitation_Conditioner.scad`

Multi-view orthographic drawing (Top + Front) with key dimensions, plus isometric simulation of the printed part.

## HVAT Hybrid Rotor

![HVAT Rotor Drawing](_static/engineering_drawing_hvat.png)

**Files:** `scad/HVAT_BLADES.scad`

Top, front, and isometric views of the active flow straightener (Savonius starting scoops + helical Darrius blades).

## Cavitation Jet Nozzle + Orifice Family

![Cavitation Nozzle Drawing](_static/engineering_drawing_nozzle.png)

**Files:** `scad/CAVITATION_NOZZLE.scad`

Section view of the Venturi profile and the complete set of interchangeable orifice inserts (6 / 8 / 10 / 12 mm).

## Assembly Jig

![Assembly Jig Drawing](_static/engineering_drawing_jig.png)

**Files:** `scad/ASSEMBLY_JIG.scad`

Critical tool that guarantees perfectly straight stacking and uniform 1.0 mm gaps.

## Bearing Housers

![Bearing Housers Drawing](_static/engineering_drawing_bearing_housers.png)

**Files:** `scad/BEARING_HOUSERS.scad`

Upper and lower 608ZZ bearing housers with mounting flanges.

## Small Critical Parts (Spacers, Covers, Viewport)

![Small Parts Drawing](_static/engineering_drawing_small_parts.png)

**Files:** `scad/SPACER_RING.scad`, `SHIPPING_INSERTS.scad`, `CLEAR_VIEWPORT.scad`, `OPERATION_COVERS.scad`

All the small but essential parts that make repeatable high-precision builds possible.

## Exploded Assembly View

![Exploded Assembly](_static/exploded_assembly.png)

Shows the logical order of all major printed components and how they relate during assembly.

## Assembled Device Simulation

![Assembled Device](_static/assembled_device_simulation.png)

3D visualization of the complete device with the platter stack, HVAT rotor, and housing as it would appear after printing and assembly (with clear viewport installed).

---

## Usage Recommendations

- Use the **PNG** versions for web / Sphinx documentation.
- Use the **SVG** versions for scaling in reports or when you need to edit labels.
- The drawings are intentionally clean (technical illustration style) so they remain readable when printed or included in papers.
- All dimensions match the default parameters in the OpenSCAD files.

## DXF Fabrication Profiles

For the most fabrication-useful 2D parts (spacer rings, orifice inserts, bolt patterns), ready-to-use DXF files are provided:

```bash
dxf_exports/
├── spacer_ring_1mm.dxf
├── orifice_6mm.dxf
├── orifice_8mm.dxf
├── orifice_10mm.dxf
├── orifice_12mm.dxf
└── viewport_bolt_pattern.dxf
```

These are minimal valid DXF R12 files that can be imported into laser cutters, CNC machines, or CAD software (FreeCAD, Fusion 360, Inkscape, etc.).

Generator: `python/generate_dxf_exports.py`

## Source Code

The main illustration generator lives at:

```bash
python/generate_engineering_drawings.py
```

It uses only `matplotlib` and produces both high-resolution PNG and vector SVG output, including proper hidden-line techniques in orthographic views.

These illustrations + DXF files fully satisfy the request to illustrate all CAD objects as both engineering drawings and simulations of the generated 3D-printed parts, while also providing practical fabrication assets.
