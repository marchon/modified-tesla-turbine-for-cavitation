# Quickstart: Im-Impatient-So-Just-Get-Me-Started

**Minimum you need to know to actually build and run this thing.**

> **⚠️ Warning**: All performance claims and graphs in this project are simplified conceptual models. The author has not yet built or tested a physical version. Treat everything as a starting point for your own experiments. See [Project Status & Limitations](project_status_and_limitations) for full disclaimers.

---

## What You Are Actually Building

A **precision flow conditioner**, not a power turbine.

It takes messy inlet flow (air or liquid) and turns it into a clean, low-turbulence, spiraling jet using stacked smooth discs (inspired by Tesla’s boundary-layer turbine). The goal is to create a more repeatable and characterizable bubble cloud when this jet hits your cavitation chamber.

There are two versions:
- **HDD Platter version** — better performance, harder to source
- **CD/DVD version** — cheap and easy to source (recommended for first builds)

---

## Full Bill of Materials (Default 25-Disc HDD Version)

| Item | Qty | Material | Notes | Source |
|------|-----|----------|-------|--------|
| Enterprise 3.5" HDD platters (95 mm) | 25 | Polished aluminum | Match thickness, clean with IPA | Scrap/eBay Enterprise drives |
| PETG or ABS filament | ~800 g | PETG preferred | 0.2 mm layers, 30-40% infill | Your printer |
| M3/M4 stainless screws (30-60 mm) | 12-16 | Stainless | For clamping | Hardware store |
| M3/M4 nuts + washers | As needed | Stainless | - | Hardware store |
| Printed spacer rings (1.0 mm) | 24 | PETG | `SPACER_RING.scad` | 3D print |
| Printed shipping inserts (1.4 mm) | 26 | PETG | `SHIPPING_INSERTS.scad` | 3D print |
| Clear viewport plate (optional) | 1 | Clear PETG | `CLEAR_VIEWPORT.scad` | 3D print |
| Solid top + bottom covers | 2 | PETG | `OPERATION_COVERS.scad` | 3D print |
| Assembly jig | 1 | PETG/PLA | `ASSEMBLY_JIG.scad` | 3D print |
| HVAT rotor (hybrid Savonius + Darrieus) | 1 | PETG | `HVAT_BLADES.scad` | 3D print |
| HVAT brake disc + caliper | 1 set | PETG | - | 3D print |
| 608ZZ bearings | 2 | Standard | 8 mm ID | Skateboard/hardware |
| 5-8 mm shaft (carbon fiber preferred) | ~80 mm | Carbon fiber | For HVAT rotor | - |
| Printed bearing housers (upper + lower) | 2 | PETG | `BEARING_HOUSERS.scad` | 3D print |
| Nozzle manifold | 1 | PETG | - | 3D print |
| Cavitation jet nozzle (Venturi) | 1 | PETG | `CAVITATION_NOZZLE.scad` | 3D print |
| Orifice inserts (6/8/10/12 mm) | 4+ | PETG | Start with 8 mm | 3D print |
| Sensor mounts | 4 | PETG | For MPX5700 or similar | 3D print |
| 6 mm ID tubing | ~1 m | Food-grade silicone/PVC | - | - |
| Hose barbs / push fittings | 6-8 | Brass/plastic | - | - |
| Threaded inserts (M3/M4) | As needed | Brass | - | - |
| Isopropyl alcohol 99% | 500 ml+ | - | For cleaning platters | - |

**Optional but recommended**: Thrust washer, base/stand, longer diffuser extension.

---

## Parts You Must 3D Print (Filenames)

**HDD Platter Version (default):**

- `HDD_Platter_Cavitation_Conditioner.scad` → Main housing + nozzles + diffuser
- `HVAT_BLADES.scad` → HVAT rotor
- `BEARING_HOUSERS.scad` → Upper and lower bearing housers
- `SPACER_RING.scad` → 24× 1.0 mm spacers
- `SHIPPING_INSERTS.scad` → 26× 1.4 mm shipping inserts
- `ASSEMBLY_JIG.scad` → Assembly jig (most important tool)
- `CLEAR_VIEWPORT.scad` → Clear viewport (highly recommended)
- `OPERATION_COVERS.scad` → Solid top + bottom jet covers
- `CAVITATION_NOZZLE.scad` → Venturi nozzle + orifice inserts

**CD/DVD Version** (alternative, cheaper):
All files are in `scad/cd_dvd_version/`

---

## Assembly Diagrams

**Recommended**:
- `illustrations/exploded_assembly.png` — Best overall exploded view
- `illustrations/cutaways/full_assembly_cutaway_3d.png` — Shows internal flow path
- `illustrations/cutaways/housing_cutaway_3d.png` — Shows platter stack + HVAT inside housing

These are also available as SVGs and in `docs/_static/`.

---

## Minimum Assembly Instructions (HDD Version)

1. **Print the Assembly Jig** first.
2. **Clean all 25 platters** thoroughly with 99% isopropyl alcohol.
3. Build the disc stack **inside the jig**:
   - Bottom end plate
   - Alternate: platter → 1.0 mm spacer → platter (24 spacers)
   - Top end plate (or clear viewport for testing)
4. Clamp with long M3/M4 screws through the aligned holes. Tighten evenly.
5. Slide the clamped stack into the main housing.
6. Install HVAT rotor on shaft + bearings inside the central hub.
7. Mount bearing housers and brake caliper.
8. Attach nozzle manifold and cavitation nozzle (start with 8 mm orifice).
9. Mount the whole device vertically above or beside your cavitation chamber.

**Start testing with low-pressure air** through the clear viewport before introducing liquid.

Full detailed steps: see the [Build](build) page in this documentation.

---

**Print the calibration pieces before anything else.**  
Spacer thickness and bearing bore tolerances are make-or-break for this device.

Good luck. Build it. Test it. Tell us what actually happens.

---

**Next steps after the quickstart:**

- Read the full [Design](design) and [Theory](theory_and_value) sections for the "why".
- Use the [Customization Guide](customization_guide) to tune parameters.
- Follow the detailed [Build](build) and [Printing Guide](printing_guide) when you are ready to fabricate.
- Review the complete [Bill of Materials](software_bill_of_materials) and [Engineering Drawings](engineering_drawings).

The standalone version of this quickstart is also available as [Im-Impatient-So-Just-Get-Me-Started.md](https://github.com/marchon/modified-tesla-turbine-for-cavitation/blob/main/Im-Impatient-So-Just-Get-Me-Started.md) in the repository root.
