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
- All dimensions match the default parameters in the OpenSCAD files. Change `num_platters`, `gap`, or `nozzle_angle` and you can regenerate updated drawings by extending the generator script.

## Source Code

The generator lives at:

```bash
python/generate_engineering_drawings.py
```

It uses only `matplotlib` (no external CAD rendering required) and produces both raster and vector output.

Future improvements could include:
- Full 2D DXF export for laser cutting
- More detailed tolerancing and GD&T callouts
- Rendered images from actual OpenSCAD STL files (once rendered on a machine with OpenSCAD GUI)

These illustrations satisfy the request to "illustrate all CAD objects both as engineering drawings and simulation of the generated output of parts."
