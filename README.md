# Modified Tesla Turbine for Cavitation — Precision HDD Platter Flow Conditioner

**TL;DR:**  
This is an interesting open hardware design idea with nice documentation and tooling.  
The performance graphs are speculative models, not data.  
The author has not built or tested it.  
Do not treat this as a proven better way to do cavitation experiments — yet.

> **⚠️ Critical Notice (Please Read First)**  
> This is an **open design exploration**, not a validated scientific instrument.  
> All performance graphs and models are simplified conceptual estimates only.  
> There is currently no experimental data from the author.  
> → Read the full **[Project Status & Limitations](docs/project_status_and_limitations.md)** before using or citing this work.

**Maturity Snapshot (May 2026)**

| Area                        | Status          | Can You Rely On It? |
|----------------------------|-----------------|---------------------|
| Physical design & docs     | Good            | Yes (for building) |
| Performance models/graphs  | Conceptual only | No |
| Experimental validation    | None by author  | No |
| Proven better than simple injection | Unknown    | No — untested |

**Open hardware precision gas/liquid injection device for repeatable hydrodynamic (and hybrid ultrasonic) cavitation experiments**, optimized for LENR/cavitation research in the style of Bob Greenyer and the Martin Fleischmann Memorial Project (MFMP).

This project packages a complete, buildable, fully parametric design for a stationary (or lightly braked) Tesla-style disc-stack flow conditioner built from scrapped Enterprise 3.5" HDD platters. The device delivers low-turbulence, uniformly spiraled flow from tangential inlets to a central exit — ideal for injecting controlled microbubbles or gas streams into a cavitation chamber with excellent repeatability.

## Key Features (from design conversation)

- **25× Enterprise 3.5" HDD platters** (95 mm OD, ~0.9 mm thick, nanometer-polished) at 1.0 mm gaps
- **6× tangential nozzles** at ~8–12° from tangent (sweet spot ~10°), slit geometry for uniform distribution into all inter-disc gaps
- **Optional central Hybrid VAWT (HVAT)** rotor (Savonius + helical Darrius blades) on 608ZZ bearings — acts as active flow straightener/mixer rather than power extractor; can be free-spinning, braked, or driven
- **Central diffuser** after HVAT for clean axial jet into chamber
- **Interchangeable Venturi-style cavitation jet nozzle** with orifice inserts (6/8/10/12 mm) for tuning pressure drop and bubble intensity
- Full sensor ports (pressure), clear viewport option, assembly jigs, shipping inserts, and alternative covers
- **Everything 3D-printable** (PETG/ABS recommended) + cheap scrap HDD platters

## Why This Design?

Standard Tesla turbines are power-producing devices (boundary-layer, inward spiral). Here the goal is **not electricity generation** but **precision flow conditioning** for scientific cavitation experiments:

- Highly repeatable bubble size distribution, pressure drop, and shear
- Multi-channel laminar-to-transitional spiral flow (far superior to a simple pipe or orifice)
- Polished surfaces + tight gaps → minimal turbulence, clean boundary layers
- Scalable (change platter count/gap in OpenSCAD)
- Low-cost, replicable with consumer 3D printer + dead hard drives

Directly supports Greenyer/MFMP-style work on hydrodynamic + ultrasonic (ULTR) cavitation, EVO/plasmoid formation, anomalous elemental changes, sonoluminescence, and potential LENR signatures in collapsing bubble clouds.

## Quick Start (Build & Test)

1. **Generate STLs**: Open the parametric OpenSCAD files in `scad/` (or paste the modules), set your platter count/gap/nozzle angle, render & export.
2. Print in PETG (0.2 mm layers, 25–40% infill). Print multiple orifice inserts.
3. Clean 25 Enterprise platters with isopropyl alcohol.
4. Use the printed assembly jig + spacers to build the clamped stack.
5. Mount in housing, add HVAT (optional but recommended for best conditioning), bearings, diffuser, viewport.
6. Low-pressure air test first (0.1–1 bar) — observe beautiful inward spiral through the clear viewport.
7. Connect central jet (with chosen orifice) into your cavitation chamber (water + foil, deuterated water, etc.).
8. Add 40 kHz 50–100 W ultrasonic transducer to the chamber for hybrid ULTR-style runs.

Full BOM, step-by-step assembly, and testing protocol live in the documentation.

## Repository Contents

- `scad/` — All parametric OpenSCAD modules (main housing + nozzles + HVAT blades + bearing housers + spacers + jigs + cavitation nozzle + viewport + shipping inserts). Fully documented.
- `docs/` — Sphinx documentation (theory, design rationale, build guide, OpenSCAD reference, experimental protocols, LENR context).
- `latex/` — Technical report / whitepaper with equations, figures, and references.
- `diagrams/` — Vector flow schematics, cross-sections, velocity profiles, assembly exploded views, cavitation number plots (generated from code).
- `python/` — Simple physics models (Reynolds number in gaps, cavitation index, spiral velocity estimator, diagram generators).
- `data/` — BOM.csv, material notes, references to Greenyer videos/papers.
- `stl/` — Reference (generated) STL files for the default 25-platter configuration.

## Documentation

Build the docs locally:

```bash
cd docs
python -m pip install -r ../requirements-docs.txt
make html
# open _build/html/index.html
```

The LaTeX paper:

```bash
cd latex
pdflatex main.tex   # run 2–3 times for references/figures
```

## Safety & Experimental Notes

- Start with low pressure air and plain water + aluminum foil (classic Greenyer ULTR signature test).
- Use proper shielding and monitoring (neutron, gamma, temperature, pressure logs) if pursuing LENR-style claims.
- Deuterium-enriched water or D₂ gas sparging is discussed in the design notes — handle flammables safely.
- Document everything (video through viewport, before/after SEM/EDX on foils, mass-spec on evolved gas).

This device is explicitly intended as a **contributor-built tool for the open LENR community**. Designs, data, and results should be shared publicly (MFMP channels, LENR-Forum, etc.).

## License

Hardware designs (OpenSCAD, 3D models, BOM, assembly instructions): CERN Open Hardware Licence v2 Strongly Reciprocal (OHL-S-2) or later.

Software / documentation / diagrams: MIT License.

See `LICENSE` and `LICENSE-HARDWARE` for full text.

## Credits & References

- Project conceived and developed by **George Lambert** (Litchfield, NH) in collaboration with Grok (xAI), May 2026.
  - Email: marchon@gmail.com
  - LinkedIn: [linkedin.com/in/podjacker](https://www.linkedin.com/in/podjacker)
- Primary inspiration and target user: Bob Greenyer / Martin Fleischmann Memorial Project (MFMP) — ULTR experiments, EVOs, cavitation transmutation research.
- Tesla turbine fundamentals: boundary-layer adhesion, inward spiral (classic literature + Wikipedia / research papers).
- HDD platter builds: community examples from Tesla turbine / wind turbine hobbyists (polished platters ideal for low-Reynolds boundary layer work).

## Status

**Ready to print and test.** All major OpenSCAD modules are complete and parametric. The Sphinx site and LaTeX report are being populated from the full design conversation.

Pull requests, test reports, SEM photos, and replication data from the MFMP community are extremely welcome.

---

**"Precision, repeatability, and low cost — the three things that turn fringe claims into real science."**

Build it. Test it. Share the data. Let's give Bob Greenyer (and the broader community) a better tool for the work.

## Quick Links (in-repo)

- [Design Notes & Rationale](docs/design.md) (or Sphinx equivalent)
- [Full BOM](data/BOM.csv)
- [OpenSCAD Master File](scad/HDD_Platter_Cavitation_Conditioner.scad)
- [Assembly Instructions](docs/build.md)
- [Testing Protocol for Greenyer-Style Experiments](docs/testing.md)
- [LaTeX Technical Report](latex/main.pdf) (after build)
