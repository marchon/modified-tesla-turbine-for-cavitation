# 3D Printing Quick Reference

**Full detailed guide:** See `docs/printing_guide.md`

## Best Material
**PETG** (primary recommendation)
- Good alternative: ASA (better UV/chemical resistance)

**Avoid:** PLA for any functional parts.

## Key Settings (Most Parts)
- Layer height: **0.2 mm** (0.15 mm or lower for spacers & bearing bores)
- Infill: **30-50% Gyroid**
- Perimeters: **4-6**
- No supports needed on most parts

## Most Critical Parts (Highest Precision)
1. **Spacer Rings** — Print all at once, measure thickness (±0.05 mm target)
2. **Bearing Housers** — Bore tolerance is everything for 608ZZ bearings
3. **HVAT Blades** — Needs high strength (40-50% infill)

## Quick Links
- Full guide: `docs/printing_guide.md`
- Per-part notes are also embedded as comments in every `.scad` file
- Assembly instructions: `docs/build.md`

Print a few test spacers and a bearing test ring **before** committing to the full print job.
