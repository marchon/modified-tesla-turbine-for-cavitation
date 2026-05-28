# Software Bill of Materials (SBOM)

This document lists all major software components used to design, analyze, visualize, and document the Precision Flow Conditioner project.

## Design & CAD

- **OpenSCAD** (2021.01 or newer) — Primary parametric modeling tool for all 3D parts.
- **FreeCAD** — Used for STL → STEP conversion when preparing files for CNC quotation services.

## Analysis & Visualization

- **Python 3** (3.10+)
  - NumPy — Numerical computations for flow models and performance graphs
  - Matplotlib — All engineering drawings, 3D cutaways, plots, and diagram generation
  - Pillow (PIL) — Image processing for flow animation frames
  - SciPy (optional) — Additional scientific utilities

## Documentation & Typesetting

- **Sphinx** + **MyST Parser** + **Furo** theme — This documentation website
- **LaTeX** (TeX Live 2026) + **natbib** — Formal technical report (`latex/main.tex`)
- **Inkscape** — Final SVG editing and figure preparation

## 3D Printing & Fabrication Data

- **Bambu Studio / Orca Slicer** / **PrusaSlicer** / **Cura** — Slicing (profile templates provided in `slicer_profiles/`)
- Custom Python generators (see `python/`) for DXF laser/CNC files and performance data

## Version Control & Collaboration

- Git
- GitHub (or equivalent)

All of the above are free and open source software.

This SBOM is intended to help replicators understand the complete digital toolchain required to work with or extend the project.
