# PCBWay CNC Metal Quotation Specification (Premium / Research Version)

This document is specifically for requesting **CNC machined metal versions** of the Precision Flow Conditioner.

Use this when you want the highest possible precision, best surface finish on flow paths, or maximum chemical resistance.

## Recommended Approach for CNC

**Best parts to machine in metal** (in priority order):

1. **Bearing Housers** — Critical bore tolerance. Metal gives best results.
2. **End Plates** — Flatness is important.
3. **Cavitation Nozzle Body** — Excellent internal surface finish possible.
4. **Main Housing** — Possible but expensive due to size.
5. **HVAT Hub** — Good candidate.

**Spacers** are still best 3D printed in most cases (too many parts to machine economically).

## Recommended Materials from PCBWay List

| Material              | Recommendation | Pros                                      | Cons                          | Best For |
|-----------------------|----------------|-------------------------------------------|-------------------------------|----------|
| **Aluminum**          | **Top choice** | Easy to machine, good corrosion resistance, lightweight, affordable | Softer than steel | Most users, general research |
| **Stainless Steel**   | Excellent      | Excellent chemical resistance, strong     | More expensive, harder to machine | Harsh chemicals / long-term use |
| **Brass**             | Good           | Good corrosion resistance, nice finish    | Softer, more expensive        | Specialized experiments |
| **Titanium**          | Premium        | Outstanding corrosion resistance          | Very expensive                | High-end / long-term research rigs |
| **Mild Steel**        | Not recommended| Cheap                                     | Will rust quickly             | - |
| **Alloy/Tool Steel**  | Possible       | Very strong                               | Heavy, needs protection       | Structural parts only |

**Strong recommendation**: Start with **6061 Aluminum** unless you have a specific reason for stainless or titanium.

## File Preparation for CNC Quotation

For best results with CNC:

- Provide **STEP** or **IGES** files when possible (more accurate than STL for machining).
- If only STLs are available, clearly note this and request they convert or ask for clarification.
- Include the full OpenSCAD source so they can see design intent and tolerances.

**Suggested upload package** (similar to 3D print package but focused):

- This CNC spec document
- STEP files (if you converted them via FreeCAD)
- High-quality STLs as backup
- The main `PCBWay_Design_Spec_and_Upload_Guide.md`
- Source OpenSCAD files

## Critical Tolerances for CNC

Please highlight these in your message to PCBWay:

- Bearing bores: **8.15 – 8.25 mm** (for standard 608ZZ bearings). Tight tolerance required.
- Spacer thickness: Not applicable for CNC (still recommend 3D printed).
- End plate flatness: Important — request they hold good flatness.
- Internal flow surfaces (especially nozzle): Request good surface finish (Ra 1.6 or better if possible).

## Suggested Quotation Request Text (copy-paste)

```
I am requesting a quote for CNC machining of parts for a scientific flow conditioner device.

Please see the attached:
- PCBWay_CNC_Metal_Spec.md (this document)
- PCBWay_Design_Spec_and_Upload_Guide.md
- Source files and STLs

I am primarily interested in Aluminum 6061 (or 304 Stainless as alternative).

Priority parts:
1. Bearing Housers (2 per set) - critical bore tolerance
2. End Plates (2 per set)
3. Cavitation Nozzle body + several orifice inserts

Please quote for 1 complete set + 1 spare set.

I can provide STEP files if preferred over STL.
```

## Next Steps After Quotation

Once you receive pricing:
- Consider ordering only the highest-tolerance parts in metal (bearing housers + nozzle) and 3D printing the rest.
- This hybrid approach often gives the best price/performance.

---

This spec is meant to be used together with the main design specification.
