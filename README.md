# Modified Tesla Turbine for Cavitation — Precision Flow Conditioner

**TL;DR (Read This First):**  
This is currently a **theoretical design + tooling project**, not a validated scientific instrument.  
All performance graphs, bubble-size estimates, and "what-if" scenarios in this repository are simplified conceptual models only — they are **not** predictions and have **not** been validated by experiment or CFD.  
As of now, the author (George Lambert) has not built or tested a physical version of this device.

**Full honest assessment:** See [Project Status & Limitations](docs/project_status_and_limitations.md)

---

## What This Project Is

This repository contains a complete, open-source, fully parametric **design exploration** for a precision gas/liquid flow conditioner intended for cavitation experiments (especially in LENR and anomalous-phenomena research).

The central idea is to repurpose the classic Tesla turbine geometry — smooth, closely spaced discs with tangential inlets — but run the stack mostly stationary. Instead of generating power, the device functions as a high-quality, low-turbulence, multi-channel spiral flow straightener that can deliver unusually consistent and characterizable injection into a cavitation chamber.

Two parallel designs are provided:
- A higher-performance version based on polished Enterprise 3.5" hard-drive platters.
- A lower-cost, easier-to-source version based on standard CD/DVD discs.

**Important:** This project deliberately separates the physical hardware design from any performance claims. The hardware is buildable today. The performance models are speculative.

## Why This Approach Was Chosen — Research Background and Design Decisions

### The Core Problem

In cavitation-based LENR and related research, one of the biggest barriers to progress is poor experimental control and repeatability. Simple gas bubblers, ultrasonic horns, or basic liquid jets tend to produce highly chaotic and poorly characterized bubble clouds. Small, uncontrolled differences in bubble size, vorticity, and shear can produce wildly different results between runs and between different laboratories. This makes it very hard to know whether differing outcomes reflect real physics or just differences in how the bubbles were generated.

### Why a Stationary Tesla-Style Disc Stack?

The design re-uses the boundary-layer principles discovered by Nikola Tesla but inverts the usual goal. In a classic Tesla turbine, fluid spirals inward between smooth discs and extracts torque. Here the stack is kept mostly stationary so its primary job becomes **flow conditioning**:

- It naturally creates many parallel, relatively well-behaved flow channels.
- The long spiral path gives fluid time to develop organized boundary layers.
- It offers multiple independent control parameters (gap size, nozzle angle, number of discs, central rotor brake, etc.) that are difficult to achieve with simpler injectors.
- It can be built extremely cheaply using either scrap hard-drive platters or ordinary CD/DVD media plus 3D printing.

### Why the Central Hybrid VAWT (HVAT) Rotor?

After the fluid spirals inward, significant organized swirl remains. A small hybrid rotor (Savonius starting scoops + helical Darrieus blades) is placed in the center. This rotor is **not** primarily a power generator — it is an active, tunable flow straightener. The brake on this rotor gives the experimenter one of the most powerful ways to deliberately add or remove large-scale vorticity before the fluid reaches the cavitation zone, without having to reprint hardware.

### Why Two Versions?

- HDD platter version: superior surface finish and thinner discs → potentially better performance, but harder and more expensive to source.
- CD/DVD version: extremely cheap and easy to obtain → excellent for rapid prototyping and low-budget replication.

Maintaining both versions makes the project more accessible while still offering a higher-performance path when needed.

## What You Will Find in This Repository

✅ **Physical build files** — Complete parametric OpenSCAD designs for both HDD platter and CD/DVD versions (main housing, HVAT rotor, bearing housers, spacers, jigs, nozzle, covers, etc.)

✅ **Fabrication assets** — DXF files ready for laser cutting / CNC, plus PCBWay quote packages

✅ **3D printing & assembly instructions** — Detailed guides, calibration pieces, recommended settings, and step-by-step assembly procedures

✅ **Speculative analysis tools** — Python generators that produce engineering drawings, flow animations, performance graphs, and “what-if” simulations (all clearly labeled as simplified conceptual models)

✅ **Extensive documentation** — Research background, design decisions, theory, community value, and practical guides (Sphinx docs + formal LaTeX report)

✅ **Customization software** — Easy-to-modify scripts and example configuration folders so you can explore your own design variations

In short: **You get the complete hardware design + the software and documentation to understand, build, test, and customize it.**

## Why People Should Build and Test It

This design was created specifically to help the community move toward higher-quality, more repeatable cavitation experiments. If multiple independent researchers build versions of this device (or improved descendants), they will at least be starting from a more comparable fluid-dynamic baseline than is typical today. That makes it far more meaningful when different groups do — or do not — see the same effects.

Even if your results show that a simpler method works just as well (or better), that data is extremely valuable. Honest null results and careful comparisons are exactly what the field needs.

## How to Set It Up and Operate It

See the following guides (recommended reading order):

1. [Project Status & Limitations](docs/project_status_and_limitations.md) — Start here.
2. [Theory, Design Rationale & Value to the Community](docs/theory_and_value.md)
3. [Tools and Software](docs/tools_and_software.md) + [Customization Guide](docs/customization_guide.md)
4. [Printing Guide](docs/printing_guide.md) + [Quick Printing Reference](PRINTING.md)
5. [Build & Assembly Guide](docs/build.md)
6. [Operation, Setup, Tuning & Testing](docs/operation_setup_tune_test.md)

## How to Get Started – Step by Step (Recommended Path)

1. **Read the honest status first**  
   → [Project Status & Limitations](docs/project_status_and_limitations.md)

2. **Understand what you’re actually building**  
   → [Theory, Design Rationale & Value to the Community](docs/theory_and_value.md)

3. **Decide which version you want to build**  
   - HDD platter version (higher performance, harder to source)  
   - CD/DVD version (cheap, easy to source, great for prototyping)

4. **Review the tools and customization options**  
   → [Tools and Software](docs/tools_and_software.md) + [Customization Guide](docs/customization_guide.md)

5. **Print the calibration pieces first** (critical)  
   Use the files in `calibration_test_pieces/` to validate that your printer + filament can hit the required tolerances (especially spacer thickness and bearing bores).

6. **Print the Assembly Jig + a small test stack**  
   This is the most important tool in the project. Print it and a handful of spacers to practice getting perfectly uniform gaps.

7. **Print the full device**  
   Follow the [Printing Guide](docs/printing_guide.md) and [Build & Assembly Guide](docs/build.md).

8. **Start testing safely**  
   Begin with low-pressure air characterization through the clear viewport before moving to liquid cavitation tests. See [Operation, Setup, Tuning & Testing](docs/operation_setup_tune_test.md).

9. **Iterate using the provided tools**  
   Use the Python generators and example configs in the `configs/` folder to explore modifications.

**In a real hurry?**  
→ Read [Im-Impatient-So-Just-Get-Me-Started.md](Im-Impatient-So-Just-Get-Me-Started.md) for the absolute minimum needed to start building.

---

**Minimum to understand before you start building:**

- This device is a **flow conditioner**, not a power-generating turbine.
- Its job is to turn chaotic inlet flow into a clean, repeatable, low-turbulence spiral jet.
- The real value comes from **controllability and characterization**, not raw power.
- All performance predictions in the repo are **speculative models** — not measured results.

### The Problem This Tries to Address

In cavitation-based LENR and related research (inspired heavily by the work of Bob Greenyer and the Martin Fleischmann Memorial Project), one of the biggest practical obstacles to progress is **lack of experimental control and repeatability**.

Common injection methods (simple gas bubblers, direct ultrasonic horns, or basic liquid jets) tend to produce highly chaotic and poorly characterized bubble clouds. Small, uncontrolled differences in bubble size distribution, vorticity, shear rates, and pre-existing microbubbles can lead to dramatically different results between runs and between different laboratories.

This makes it extremely difficult to know whether differing outcomes are due to real physical effects or simply differences in how the bubbles were created.

### Why a Modified Tesla-Style Disc Stack?

The design deliberately re-purposes the boundary-layer principles discovered by Nikola Tesla. In a classic Tesla turbine, fluid enters tangentially at the periphery and spirals inward between smooth discs via viscous drag. Here we keep the geometry but run the stack mostly stationary so that its primary function becomes **flow conditioning** rather than torque production.

Key reasons this geometry was chosen:

- It naturally creates many parallel, relatively laminar flow channels.
- The spiral path gives fluid time to develop organized boundary layers.
- It is inherently scalable (just change the number of discs or gap).
- It can be built extremely cheaply using either scrap hard drive platters or ordinary CD/DVD media + 3D printing.
- It offers multiple independent control parameters (gap size, nozzle angle, number of discs, central rotor brake, etc.) that are difficult to achieve with simpler injectors.

### Why the Central Hybrid VAWT (HVAT) Rotor?

After the fluid spirals inward through the discs, significant organized swirl remains. Instead of wasting this energy, a small hybrid vertical-axis rotor (combination of Savonius starting scoops and helical Darrieus blades) is placed in the center. This rotor is **not** primarily intended to generate electricity. Its job is to act as an active, tunable flow straightener that can reduce unwanted large-scale vorticity before the fluid exits into the cavitation zone.

The brake on this rotor becomes one of the most powerful "knobs" available to the experimenter for controlling the character of the jet without reprinting hardware.

### Why Two Versions (HDD Platters vs CD/DVD)?

- **HDD platter version**: Superior surface finish (mirror-polished), thinner discs, potentially better performance. Harder and more expensive to source matched sets.
- **CD/DVD version**: Extremely cheap and easy to obtain, thicker discs, larger diameter. Slightly inferior surface quality but excellent for rapid prototyping and low-budget replication.

Maintaining both versions makes the project more accessible while still offering a higher-performance path for serious research.

## Intended Benefit to the Community

The long-term goal is to help raise the quality floor of cavitation and LENR-related experiments by providing a relatively low-cost, well-characterized, and replicable injection platform.

If multiple independent researchers build similar (or improved) versions of this device, they will at least be starting from a more comparable fluid-dynamic baseline than is common today. This should make it more meaningful when different groups do — or do not — observe the same effects.

The project emphasizes:
- Calibration pieces so builders can actually know the real dimensions of their hardware.
- Clear documentation of design decisions and trade-offs.
- Example configurations for different experimental goals.
- Separation between the physical hardware and any speculative performance models.

## Why You Should Consider Building and Testing This

- If you are doing cavitation experiments and are frustrated by poor repeatability.
- If you want a well-documented, open platform that others can also build.
- If you are interested in systematic parameter studies (different swirl levels, different gap sizes, hybrid hydrodynamic + ultrasonic, different gases, etc.).
- If you want to contribute real experimental data to the broader community.

Even null results or "it didn't work better than X" findings would be valuable.

## Repository Contents

This repository deliberately contains **both the physical design assets and the speculative tooling**:

- Complete parametric OpenSCAD designs for both the HDD platter and CD/DVD versions (including all jigs, housings, nozzles, HVAT components, etc.).
- Multiple Python tools for generating engineering drawings, DXF fabrication files, flow animations, and performance sensitivity plots.
- Extensive Sphinx documentation covering theory, design rationale, building, printing, operation, and customization.
- A formal LaTeX technical report.
- Calibration test pieces.
- Example configuration folders with pre-tuned parameter sets.
- Fabrication support files (including packages for getting quotes from services like PCBWay).
- DXF files ready for laser cutting or CNC.

See [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) for a detailed breakdown of everything in the repo.

## Current Status (May 2026)

This project is at an early but well-documented design stage. See the dedicated [Project Status & Limitations](docs/project_status_and_limitations.md) page for a full maturity assessment.

## Getting the Code

The canonical repository is:

**https://github.com/marchon/modified-tesla-turbine-for-cavitation**

```bash
git clone https://github.com/marchon/modified-tesla-turbine-for-cavitation.git
```

---

**License**: Hardware designs under CERN Open Hardware Licence v2 Strongly Reciprocal (OHL-S-2). Software and documentation under MIT.

This is an open invitation to the community. Build it. Test it. Break it. Improve it. Share what you learn — especially when it doesn't work as hoped. That is how real progress happens.

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
- [LaTeX Technical Report](pdfs/Modified_Tesla_Turbine_for_Cavitation_-_Technical_Report.pdf) (after build)
