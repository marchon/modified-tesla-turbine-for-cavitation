# Tools and Software

This project relies on a modern, fully open-source toolchain for parametric design, analysis, visualization, fabrication data generation, and documentation.

All tools mentioned here are free (as in freedom and usually as in price) and widely available.

## Core Design & CAD

- **OpenSCAD** — The primary tool for all parametric 3D models (`scad/` directory).
  - Every part is defined with variables at the top of each `.scad` file so you can easily customize dimensions, number of discs, nozzle angles, etc.
  - Highly recommended for anyone wanting to modify the design.

- **FreeCAD** — Used for importing STL files and converting them to STEP format when needed for CNC quotation services (e.g., PCBWay).

## Visualization, Analysis & Fabrication Data Generation

All the following Python tools live in the `python/` directory and were developed specifically for this project:

- `generate_engineering_drawings.py` — Produces the full set of professional orthographic engineering drawings and 3D cutaway/isometric views (PNG + SVG).
- `generate_dxf_exports.py` — Creates 2D DXF profiles with proper layers (CUT, DRILL, ANNOTATE) for laser cutting or CNC of flat parts (spacers, orifice inserts, bolt patterns, etc.).
- `generate_flow_animation.py` — Generates the animated flow path visualization (individual frames + GIF).
- `generate_performance_graphs.py` — Creates the sensitivity plots showing effects of HVAT brake position, orifice size, inlet pressure, and gap on performance metrics.

These scripts use:
- **NumPy** — Numerical computations
- **Matplotlib** — All 2D plots, 3D visualizations, and diagram generation
- **Pillow (PIL)** — Image processing for animations and diagram post-processing
- **SciPy** (where applicable) — Additional scientific computing

## Documentation & Typesetting

- **Sphinx + MyST** — This entire documentation site (`docs/`)
- **LaTeX (TeX Live)** + **natbib** — The formal technical report (`latex/main.tex`)
- **Inkscape** — SVG editing and final figure preparation

## 3D Printing & Slicing

See the dedicated [Printing Guide](printing_guide.md) and [Quick Reference](../PRINTING.md).

Profile templates are provided in `slicer_profiles/` for:
- Bambu Studio / Orca Slicer (JSON)
- PrusaSlicer (INI)
- Cura (curaprofile)

## How to Customize the Design

The project is built from the ground up for easy customization:

### 1. OpenSCAD Parametric Models (`scad/` and `scad/cd_dvd_version/`)

Every major file starts with a clear `// PARAMETERS` section. Examples:

- `num_platters` or `num_discs`
- `gap`
- `nozzle_angle`
- `hv_dia` (HVAT diameter)
- Disc/platter diameter and thickness

Simply change the numbers at the top, render (F6), and export STL.

The CD/DVD version and HDD platter version are maintained in parallel so you can experiment with both.

### 2. Python Generators

Most generators accept parameters via command-line arguments or by editing the top of the script (e.g., changing default gap, number of frames in animation, pressure ranges in graphs, etc.).

Example:
```bash
python python/generate_performance_graphs.py
```

You can fork and modify any of these scripts to produce new plots, different DXF layers, or new diagram styles.

### 3. Calibration Pieces (`calibration_test_pieces/`)

Use these to dial in your specific printer + filament combination before committing to a full build:
- Spacer thickness calibration
- Bearing bore test rings
- Nozzle throat test rings
- Flatness test plate

### 4. DXF Exports (`dxf_exports/`)

These are generated from Python and can be further edited in Inkscape or imported directly into laser cutters / CNC software.

## Replicating the Device with 3D Printing and Assembly

The entire design philosophy prioritizes **radical replicability** using only consumer-grade equipment.

### 3D Printing Strengths of This Project
- All structural parts are designed to be printed on standard FDM printers (no resin required for the basic version).
- Minimal or zero supports needed on most parts.
- Critical tolerances (especially spacer thickness and bearing bores) are called out explicitly in the SCAD files and printing guides.
- Calibration test pieces are provided so you can validate your printer before printing the real parts.

### Assembly Advantages
- The dedicated `ASSEMBLY_JIG.scad` ensures the disc stack is perfectly straight and gaps are uniform — this is one of the biggest reasons the device performs well.
- Shipping inserts protect the precise gaps during transport.
- Clear viewport option allows visual verification of flow during initial air testing.

Detailed instructions are in:
- [Build & Assembly Guide](build.md)
- [Printing Guide](printing_guide.md)
- [How to Print Precise Spacers](how_to_print_precise_spacers.md)

## Navigation – Special Interest Areas

Use the following directory trees to quickly jump to areas of interest:

### CAD & Parametric Design
```
scad/
├── HDD_Platter_Cavitation_Conditioner.scad   ← Main housing (HDD version)
├── HVAT_BLADES.scad
├── BEARING_HOUSERS.scad
├── CAVITATION_NOZZLE.scad
├── SPACER_RING.scad
├── ASSEMBLY_JIG.scad
└── cd_dvd_version/                           ← Complete alternative design using CD/DVD discs
    ├── CD_DVD_Flow_Conditioner.scad
    └── ...
```

### Python Generators & Visualization
```
python/
├── generate_engineering_drawings.py          ← Orthographic + cutaway views
├── generate_dxf_exports.py                   ← Laser/CNC ready 2D profiles
├── generate_flow_animation.py                ← Flow development animation
└── generate_performance_graphs.py            ← Tuning sensitivity plots
```

### Fabrication & Calibration
```
calibration_test_pieces/                      ← Printer calibration tools
dxf_exports/                                  ← Ready-to-use DXF files
slicer_profiles/                              ← Bambu, Prusa, Cura profiles
fabrication/                                  ← PCBWay quote packages
```

### Documentation
```
docs/
├── printing_guide.md
├── build.md
├── tools_and_software.md                     ← This page
├── engineering_drawings.md
├── gallery.md
└── theory_and_value.md
```

See the root [PROJECT_STRUCTURE.md](../PROJECT_STRUCTURE.md) for the complete tree.

---

All of these tools and files are deliberately chosen or created so that a motivated individual or small group can replicate, understand, modify, and improve the device using only free software and common 3D printing hardware.