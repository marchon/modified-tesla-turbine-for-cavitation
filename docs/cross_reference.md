# Cross-Reference & Index

This section provides a consolidated lookup for the entire documentation. Use it as the "back of the book" reference when working with the device, code, or documentation.

---

## Core Terminology

| Term | Definition | Primary Section |
|------|------------|-----------------|
| **Tesla-style boundary layer flow** | Fluid adheres to closely spaced rotating or stationary discs; momentum transfers in thin layers producing spiral flow with low turbulence. | [Theory](theory_and_value) |
| **Cavitation number (σ)** | Dimensionless parameter σ = (P − P_v) / (0.5 ρ V²). Lower σ = more cavitation. Target regime often 0.2–1.5 for controlled studies. | [Theory](theory_and_value) |
| **HVAT (Hybrid Vertical Axis Turbine)** | Central rotor combining Savonius (drag) + helical Darrieus (lift) elements. Used here as tunable swirl straightener / brake, not power extractor. | [Design](design), [HVAT_BLADES.scad](../scad/HVAT_BLADES.scad) |
| **1 mm gap** | Critical inter-disc spacing. Too tight → viscous lock; too loose → turbulence. 1.0 mm chosen for 25-platter stack in ~50–55 mm height. | [Design](design) |
| **~10° tangent nozzles** | Six inlets at ~10° from true tangent. Induces organized pre-swirl without shock. | [CAVITATION_NOZZLE.scad](../scad/CAVITATION_NOZZLE.scad) |
| **Venturi cavitation nozzle** | Converging-diverging section with interchangeable orifice inserts (6/8/10/12 mm). Primary site of controlled bubble generation. | [Build](build), [Nozzle](engineering_drawings) |
| **Assembly jig** | Precision printed fixture that holds platters + spacers at exact 1.0 mm gaps during clamping. Essential for repeatability. | [ASSEMBLY_JIG.scad](../scad/ASSEMBLY_JIG.scad) |

---

## Major CAD Files & What They Produce

| File (HDD version) | Primary Outputs | Key Parameters | Notes |
|--------------------|-----------------|----------------|-------|
| `HDD_Platter_Cavitation_Conditioner.scad` | Main housing, nozzle manifold, diffuser, end plates | `num_platters=25`, `gap=1.0`, `nozzle_angle=10` | Orchestrator; renders full assembly |
| `HVAT_BLADES.scad` | Hybrid Savonius+Darrieus rotor + optional brake disc | `hv_dia=38`, `blade_count=4` | Central flow straightener/brake |
| `BEARING_HOUSERS.scad` | Upper & lower 608ZZ bearing carriers with brake mount | Bearing OD, shaft clearance | Critical alignment parts |
| `CAVITATION_NOZZLE.scad` | Venturi body + family of orifice inserts (6/8/10/12 mm) | `orifice_d=8` default | Includes multiple STLs via customizer |
| `SPACER_RING.scad` | 1.0 mm thick inter-platter rings (24 needed) | `thickness=1.0`, `count=24` | Print with high precision |
| `ASSEMBLY_JIG.scad` | Stack assembly & alignment fixture | Matches platter OD + bolt pattern | Print first; use for every build |
| `CLEAR_VIEWPORT.scad` | Transparent top plate with bolt pattern + sensor ports | Thickness, port sizes | Highly recommended for observation |
| `OPERATION_COVERS.scad` | Solid top/bottom plates for normal operation | — | Replaces viewport when not observing |
| `SHIPPING_INSERTS.scad` | 1.4 mm protective spacers for transport/storage | — | Prevents platter damage in transit |

All CD/DVD equivalents live in `scad/cd_dvd_version/`.

---

## Key OpenSCAD Parameters (Most Used for Tuning)

| Parameter | Default (HDD) | Effect | Typical Experiment Range |
|-----------|---------------|--------|--------------------------|
| `num_platters` / `num_discs` | 25 | Number of boundary layer channels | 15–30 (more = higher pressure drop, finer bubbles) |
| `gap` | 1.0 mm | Inter-disc spacing | 0.8–1.5 mm (print tolerance critical) |
| `nozzle_angle` | 10° | Inlet swirl angle from tangent | 5–15° |
| `hv_dia` | 38 mm | HVAT rotor diameter | 30–45 mm (larger = more braking) |
| `orifice_d` | 8 mm | Cavitation throat diameter | 6 mm (aggressive) / 8–10 mm (balanced) / 12 mm (gentle) |
| `disc_thickness` | ~0.9 mm (HDD) | Platter thickness | Fixed by media; CD/DVD ~1.2 mm |
| `housing_id` | 98 mm | Internal bore for platter stack | Slight clearance over OD |

Change at the top of the relevant .scad file, press F6 (render), export STL.

---

## Interchangeable Orifice Regimes (Guidance Only — Conceptual)

| Orifice | Nominal Throat Velocity (example 3 bar) | Expected Bubble Character | Recommended Starting Use |
|---------|-----------------------------------------|---------------------------|--------------------------|
| 6 mm | Highest | Finer, more numerous bubbles; higher σ risk of choking | Aggressive cavitation studies |
| 8 mm | High | Good balance; most MFMP-style work | Default / first tests |
| 10 mm | Medium | Larger bubbles, lower intensity | Gentle / high-flow throughput |
| 12 mm | Lower | Least aggressive; best for visualization | Visualization, calibration, low-pressure work |

**All values are from simplified 1D isentropic + Bernoulli estimates in the Python models.** Real behavior depends on upstream pressure, dissolved gas, surface tension, temperature, and geometry details not captured here.

---

## Printed Part Tolerances & Critical Dimensions

| Part | Critical Dimension | Target Tolerance | Print Recommendation |
|------|--------------------|------------------|----------------------|
| Spacers | Thickness 1.00 mm | ±0.05 mm (ideally ±0.03) | 0.2 mm layers, 4+ perimeters, 100% infill on first layer, measure every batch |
| Bearing housers | 608ZZ bore (22 mm) | ±0.1 mm | Print vertical, use calibration test piece first |
| Nozzle orifices | Throat ID (6/8/10/12) | ±0.15 mm | Print slow (30–40 mm/s), 0.15–0.2 mm layers |
| Assembly jig | Platter pocket + bolt holes | ±0.1 mm positional | Most important tool; verify with actual platters |
| HVAT blades | Hub bore & blade chord | ±0.15 mm | Support carefully; balance after print |

Always print the calibration set in `calibration_test_pieces/` first with your exact filament + slicer profile.

---

## Major Generated Artifacts

| Artifact | Generator | Purpose |
|----------|-----------|---------|
| `illustrations/engineering_drawing_*.png/svg` | `python/generate_engineering_drawings.py` | Orthographic + isometric + hidden-line for every part |
| `illustrations/cutaways/*.png/svg` | Same + manual Blender/Illustrator | 3D sectional views |
| `illustrations/flow_path_animation.gif` | `python/generate_flow_animation.py` | 20-frame progressive flow visualization |
| `illustrations/performance_graphs/*.png` + what-if variants | `python/generate_performance_graphs.py` | Sensitivity studies (all clearly labeled "conceptual model") |
| `dxf_exports/*.dxf` | `python/generate_dxf_exports.py` | 2D profiles for CNC/laser (layered: CUT, DRILL, ANNOTATE) |
| `docs/_static/*` + `latex/figures/` | Copied during build | Embedded in HTML / LaTeX / PDF |
| `stl/` (populated on demand) | OpenSCAD | Ready-to-print files |

---

## Performance Model Variables (All Speculative)

The graphs and tables in [Customization Guide](customization_guide) and [Gallery](gallery) come from `python/models/flow_conditioner.py` + `generate_performance_graphs.py`.

Key modeled quantities (read the source and the disclaimers!):

- Boundary layer thickness δ(x) ≈ 5 * sqrt(ν x / U)
- Spiral angle, residence time, Reynolds number per channel
- Estimated pressure drop vs. disc count and gap
- Crude bubble size distribution from orifice + downstream recovery
- HVAT braking torque (highly simplified actuator disk + VAWT coefficients)
- Hybrid ultrasonic synergy (qualitative only)

**None of these have been validated against physical hardware built by the author.**

---

## File & Directory Quick Map

See the full living document: [PROJECT_STRUCTURE.md](https://github.com/marchon/modified-tesla-turbine-for-cavitation/blob/main/PROJECT_STRUCTURE.md)

Key top-level directories you will touch:

- `scad/` + `scad/cd_dvd_version/` — All parametric CAD
- `python/` — Generators for drawings, DXFs, graphs, animations, models
- `docs/` — This Sphinx site (source of the PDF you are reading)
- `pdfs/` — Final built PDFs (Full Documentation book + Technical Report) — directly viewable on GitHub
- `illustrations/` — All publication-ready figures
- `configs/` — Ready-to-use example parameter sets (aggressive, gentle, maximum uniformity, CD/DVD rapid proto)
- `calibration_test_pieces/` — Must-print tolerance verification parts
- `slicer_profiles/` — Bambu/Orca, Prusa, Cura tuned profiles
- `dxf_exports/` — 2D fabrication data
- `fabrication/pcbway/` — CNC metal quote package
- `data/BOM.csv` — Master bill of materials
- `latex/` — Separate formal technical report (different scope from this PDF; final versions copied to pdfs/)

---

## How to Navigate This PDF Efficiently

- Use the **bookmarks / outline** (left sidebar in most PDF readers) — generated from the document headings.
- The **Table of Contents** appears early.
- Major sections start on new pages.
- Every figure has a caption and source note.
- The warnings in [Project Status & Limitations](project_status_and_limitations) are repeated in spirit throughout — read them once, then refer back here.

**Last updated**: 2026 — This is living open hardware documentation. Check the GitHub repository for community builds, test data, and revisions.

---

*Cross-reference compiled from the full Sphinx documentation tree. For the absolute latest, always consult the source Markdown files and the Python generators.*
