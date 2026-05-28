# Build & Assembly Guide

This guide walks you through printing, preparing, and assembling the 25-platter HDD Platter Precision Flow Conditioner exactly as developed in the May 2026 design conversation.

## 1. Print All Parts

**→ See the comprehensive guide: [docs/printing_guide.md](printing_guide.md)**

The short version:
- **Best material**: PETG (ASA is excellent alternative)
- Use the separate OpenSCAD modules in `scad/`
- Layer height: 0.2 mm (0.12-0.15 mm for spacers and bearing bores)
- Infill: 30–50% (higher on HVAT blades and bearing housers)
- Supports: Not required on these designs

**Important:** Print a few test spacers and a bearing bore test ring **before** doing the full job. Spacer thickness and bearing bore are the most critical dimensions.

**Required prints (default 25-platter config):**

- 1 × Main housing + nozzles + diffuser (`HDD_Platter_Cavitation_Conditioner.scad`)
- 1 × HVAT rotor (`HVAT_BLADES.scad`)
- 2 × Bearing housers (`BEARING_HOUSERS.scad`)
- 24 × Spacer rings (1.0 mm) (`SPACER_RING.scad`)
- 26 × Shipping inserts (1.4 mm) (`SHIPPING_INSERTS.scad`)
- 1 × Assembly jig (`ASSEMBLY_JIG.scad`)
- 1 × Clear viewport (optional but highly recommended for testing) (`CLEAR_VIEWPORT.scad`)
- 1 × Solid top cover + 1 × Bottom jet cover (`OPERATION_COVERS.scad`)
- 1 × Cavitation jet nozzle body + 4+ orifice inserts (6/8/10/12 mm) (`CAVITATION_NOZZLE.scad`)
- 1 × Nozzle manifold (distributes compressed air to the 6 tangential inlets)
- 4 × Sensor mounts (for pressure transducers)
- HVAT brake disc + caliper (for tunable swirl)

Print a few extra spacers and inserts — they are small and easy to lose.

## 2. Prepare the Platters

1. Source 25 matched Enterprise 3.5" HDD platters (95 mm OD).
2. Clean **thoroughly** on both sides with 99% isopropyl alcohol. Any fingerprint or residue will create turbulence.
3. Inspect for warpage or damage. Replace any suspect platters.

## 3. Assemble the Platter Stack (Use the Jig)

1. Place the Assembly Jig on a flat surface.
2. Insert the bottom end clamp plate.
3. Alternate: platter → spacer ring → platter (24 spacers for 25 platters).
4. Finish with the top end clamp plate (or clear viewport for testing).
5. Insert 6–8 long M3/M4 screws through the aligned holes and tighten evenly in a star pattern (1–1.5 Nm). Do not overtighten.

The jig keeps everything perfectly straight and the gaps uniform.

## 4. Install into Housing + HVAT

1. Carefully slide the clamped stack into the main housing (still in the jig if helpful).
2. Align the tangential nozzle openings with the inter-platter gaps.
3. Secure top and bottom end plates fully.
4. Press lower 608ZZ bearing into lower bearing houser.
5. Screw lower bearing houser to bottom end plate.
6. Insert central shaft + HVAT rotor (center it in the stack).
7. Press upper bearing into upper houser and mount to top plate.
8. Add thin thrust washer if needed.
9. Mount brake disc + caliper on top of shaft (for swirl control).

## 5. Add Flow & Sensor Features

- Attach the 6-inlet nozzle manifold to the tangential nozzles (press-fit or screws + silicone tubing).
- Install the 4 sensor mounts over the side ports (MPX5700 or similar pressure sensors recommended).
- Screw or clamp the cavitation jet nozzle (with chosen orifice insert) to the bottom of the diffuser.
- Add top/bottom covers as needed.

## 6. Final Checks

- Rotate HVAT by hand — it should spin freely with minimal play.
- Verify all gaps are uniform by looking through the clear viewport (or by feel with a feeler gauge).
- For shipping: swap to thicker shipping inserts + solid covers.

The entire unit is now ready for low-pressure air testing and subsequent liquid cavitation experiments.

See `testing.md` for the recommended Greenyer-style protocol.
