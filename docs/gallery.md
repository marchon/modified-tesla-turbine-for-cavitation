# Visual Gallery — Engineering Drawings, Cutaways, Animations & Performance Data

This page serves as a central visual reference for the HDD Platter Precision Flow Conditioner.

## 3D Cutaway Views (Higher Fidelity)

These sectional renderings reveal internal geometry and flow paths.

### Housing Internal Cutaway
![Housing Cutaway](_static/housing_cutaway_3d.png)

### Full Assembly Flow Path Cutaway
![Full Assembly Cutaway](_static/full_assembly_cutaway_3d.png)

### HVAT Rotor Detail
![HVAT Detail Cutaway](_static/hvat_detail_cutaway_3d.png)

### Cavitation Nozzle Internal
![Nozzle Cutaway](_static/nozzle_internal_cutaway_3d.png)

## Flow Path Animation

Progressive visualization of fluid behavior through the device.

![Flow Path Animation](_static/flow_path_animation.gif)

*20-frame animation showing: Tangential injection → Spiral development → HVAT conditioning → Final jet acceleration.*

## Performance Sensitivity Graphs

Projected behavior under different tuning operations.

![Performance Graphs](_static/performance_sensitivity.png)

These graphs illustrate the impact of the main control knobs (HVAT brake, orifice size, inlet pressure, gap). See `operation_setup_tune_test.md` for detailed guidance on how to make these adjustments in practice.

## All Engineering Drawings

Complete set of orthographic + isometric drawings for every major component.

- [Main Housing + Nozzles](engineering_drawings.md)
- [HVAT Rotor](engineering_drawings.md)
- [Cavitation Nozzle + Orifices](engineering_drawings.md)
- [Assembly Jig](engineering_drawings.md)
- [Bearing Housers](engineering_drawings.md)
- [Small Parts (Spacers, Covers, Viewport)](engineering_drawings.md)

## DXF Fabrication Profiles (with Layers)

Ready-to-use 2D profiles with proper layers (`CUT`, `DRILL`, `ANNOTATE`) and text labels:

- `bearing_houser_profile.dxf`
- `spacer_ring_1mm.dxf`
- `orifice_6mm.dxf` / `8mm` / `10mm` / `12mm`
- `viewport_bolt_pattern.dxf`

Located in the `dxf_exports/` directory at the project root.

---

These visuals were generated programmatically to accompany the OpenSCAD CAD files and are intended to support both understanding and fabrication.
