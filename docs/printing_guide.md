# Comprehensive 3D Printing Guide

This is the definitive guide for successfully printing all parts of the HDD Platter Precision Flow Conditioner.

## Material Recommendations

| Material | Recommendation | Pros | Cons | Notes |
|----------|----------------|------|------|-------|
| **PETG** | **Best overall choice** | Excellent chemical resistance, good strength, low warping, easy to print | Can be stringy | Primary recommendation for most users |
| **ASA** | Excellent alternative | UV resistant, very good chemical resistance, tough | Slightly harder to print than PETG | Great if device will see sunlight or chemicals |
| **ABS** | Acceptable | Good strength, widely available | Warps more, needs enclosure | Only if you have good ABS printing setup |
| **PLA** | **Not recommended** | Easy to print | Brittle, poor chemical/heat resistance | Will fail in real use |
| **Nylon** | Advanced | Very tough | Hygroscopic, difficult | Only for experienced users |
| **Polycarbonate** | Advanced | Extremely tough | Very difficult to print | Overkill for most builds |

**Winner for most people: PETG**

## Per-Part Printing Recommendations

### High Priority / High Tolerance Parts

| Part | Material | Layer Height | Infill | Perimeters | Special Notes |
|------|----------|--------------|--------|------------|---------------|
| **Spacer Rings** (24+) | PETG | 0.12-0.15 mm | 80-100% | 4-5 | **Most critical part**. Print all at once from same spool. Measure thickness. |
| **Bearing Housers** | PETG/ASA | 0.15 mm | 50%+ | 6+ | Bore tolerance is everything. Test print first. |
| **HVAT Blades** | PETG/ASA | 0.15-0.2 mm | 40-50% | 5+ | High strength needed. Balance after printing. |
| **Main Housing** | PETG | 0.2 mm | 30-40% | 4-5 | Large part — good first layer + brim essential. |
| **Cavitation Nozzle** | PETG/ASA | 0.15-0.2 mm | 40% | 4 | Sand internal surfaces for best flow. |

### Lower Priority Parts

- Assembly Jig: 0.2mm, 35% infill, 5 perimeters (needs to stay flat)
- Clear Viewport: 0.2mm, 30% infill (use clear PETG if possible)
- Shipping Inserts: 0.2mm, 30% infill (thicker = more protection)
- Operation Covers: 0.2mm, 30-35% infill

## Slicer-Specific Recommendations

### Bambu Studio / Orca Slicer (Recommended)
- Use **0.2mm Standard** profile as base
- Increase **Wall loops** to 4-5 for structural parts
- Set **Infill** to Gyroid 35%+ for most parts
- Enable **Arachne** wall generator
- Use **Thick bridges** for the large housing

### PrusaSlicer
- Use **0.2mm QUALITY** or **0.15mm QUALITY**
- Increase **Perimeters** manually
- Use **Gyroid** infill
- Enable **Elephant foot compensation** (0.2-0.3mm) for spacers

### Cura
- Use **Standard Quality** or create custom 0.15-0.2mm profile
- Increase **Wall Line Count** to 5
- Use **Gyroid** or **Cubic** infill
- Enable **Fuzzy Skin** on non-critical external surfaces (optional)

## Critical Tolerances & How to Achieve Them

1. **Spacer Thickness (±0.05 mm target)**
   - Print at very fine layers (0.12-0.15mm)
   - Print everything in one job from the same filament
   - Measure 5 random spacers after printing
   - Adjust flow rate if consistently off

2. **Bearing Bore (608ZZ)**
   - Target: 8.15 – 8.25 mm
   - Print a test ring first with different sizes
   - Vertical printing of the bore gives best roundness

3. **Nozzle Throat Diameter**
   - Critical for experimental repeatability
   - Print orifices at finest layer height possible
   - Consider printing them solid (100% infill)

## Common Problems & Solutions

| Problem | Likely Cause | Solution |
|---------|--------------|----------|
| Spacers too thick | Elephant's foot + high flow | Increase first layer height, reduce flow 3-5% |
| Bearing too loose | Wrong tolerance in model or poor cooling | Print with smaller bore test, improve cooling |
| Housing warps | Poor bed adhesion / cooling | Use brim, enclosure for ABS, good first layer |
| Poor surface on internal flow paths | Low perimeters | Increase perimeters to 5+ |
| HVAT doesn't spin freely | Bearing bore issues or debris | Ream/sand bore, clean thoroughly |

## Post-Processing Recommendations

- **Annealing PETG** (optional but recommended for chemical resistance): 80°C for 1 hour in oven
- Light sanding on mating surfaces and internal flow paths
- Thorough cleaning of all holes and threads
- For orifices: Consider drilling to final size if you have the bits

## See Also

- `docs/how_to_print_precise_spacers.md` — Detailed guide for hitting the most critical tolerance in the project (±0.05 mm on spacers)

## Recommended Workflow

1. Print 5-6 test spacers first → measure and dial in flow
2. Print a test bearing houser ring → verify bore fit
3. Print the Assembly Jig + a few spacers
4. Print the HVAT blades (high strength)
5. Print the main housing (biggest time investment)
6. Print remaining small parts

This order lets you catch problems early.

---

For the absolute latest recommendations and community results, check the GitHub issues and discussions once the project is public.
