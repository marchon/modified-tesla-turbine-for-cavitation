# HDD Platter Precision Flow Conditioner

**A fully parametric, 3D-printable, open-hardware device for repeatable hydrodynamic cavitation experiments.**

Built around a stack of 25 highly polished Enterprise 3.5" HDD platters (Tesla-style boundary layer spiral) with an optional central Hybrid VAWT (HVAT) flow straightener. Designed specifically as a precision gas/liquid injection tool for LENR and cavitation research in the tradition of Bob Greenyer and the Martin Fleischmann Memorial Project (MFMP).

```{toctree}
:maxdepth: 2
:caption: Contents

design
build
testing
ultrasonic_hybrid
engineering_drawings
openscad
references
```

## Quick Highlights

- 25 platters, 1.0 mm gaps, 6 tangential nozzles at ~10° from tangent
- Fully parametric OpenSCAD — change stack height, gap, nozzle angle, HVAT size in one place
- Complete BOM, assembly jigs, shipping inserts, sensor ports, interchangeable cavitation orifices
- Hybrid hydrodynamic + 40 kHz ultrasonic (ULTR-style) ready
- Target use: controlled bubble dynamics, EVO/plasmoid studies, foil erosion, gas evolution, and anomalous effects research

## Status

Ready to build. All major OpenSCAD modules are complete. Sphinx documentation and the accompanying LaTeX technical report are being expanded from the original design conversation.

See the [GitHub repository](https://github.com/...) (to be populated) for the latest STLs, updates, and community test reports.

## License

Hardware (OpenSCAD, BOM, jigs, assembly docs): **CERN OHL-S-2** (Strongly Reciprocal)

Software, diagrams, Python models, Sphinx/LaTeX sources: **MIT**

## Acknowledgments

This device and its documentation grew out of an extended technical conversation with Grok (xAI) in May 2026. The goal was to turn a promising idea into a complete, replicable, open tool for the global LENR experimental community.

Special thanks to the MFMP / Bob Greenyer for the inspiration, the ULTR protocol, the emphasis on radical repeatability at low cost, and the public sharing of data and methods that make projects like this worthwhile.
