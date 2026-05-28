# PCBWay Design Specification & File Upload Guide

This document is intended to be submitted along with CAD files when requesting a quotation from PCBWay for either **3D printing** or **CNC machining** of parts for the HDD Platter / CD-DVD Precision Flow Conditioner.

## Project Overview

**Project Name**: Precision Flow Conditioner for Cavitation Experiments (HDD Platter + CD/DVD variants)

**Purpose**: Scientific instrument for repeatable hydrodynamic and hybrid ultrasonic cavitation experiments, targeted at Low Energy Nuclear Reaction (LENR) and bubble dynamics research.

**Key Requirements**:
- High dimensional accuracy on critical features (especially spacer thickness and bearing bores)
- Good surface finish on internal flow paths
- Chemical resistance to water and various gases
- Ability to hold tight gaps (0.8–1.5 mm) between discs

## Two Design Variants

### Variant A: HDD Platter Version (Higher Performance)
- Uses 95 mm Enterprise hard drive platters
- Superior surface finish
- Best for serious research

### Variant B: CD/DVD Version (Low Cost / Accessible)
- Uses standard 120 mm CD or DVD discs
- Much cheaper and easier to source
- Good for prototyping and education

**Please quote both variants** if possible, or specify which one you are quoting.

## Recommended Manufacturing Methods & Materials

### Option 1: 3D Printing (Recommended for most parts)
**Preferred Materials** (from PCBWay list):
- **ABS**
- **Polycarbonate (PC)**
- **Nylon**

**Why these?**
- Good chemical resistance
- Reasonable temperature resistance
- Sufficient strength for the application

**PETG is also excellent** but is not listed in your current material options. If you can print PETG, it is our top choice.

### Option 2: CNC Machining (For highest precision / metal versions)
**Recommended Materials**:
- **Aluminum** (good all-rounder, easy to machine)
- **Stainless steel** (excellent chemical resistance)
- **Brass** (good corrosion resistance)
- **Titanium** (premium, very corrosion resistant – expensive)

**Best candidates for CNC**:
- Bearing housers (tolerances are critical)
- End plates
- Nozzle bodies (for best internal surface finish)

## Parts List & Recommendations

| Part                        | Recommended Process | Preferred Material     | Notes / Critical Features |
|----------------------------|---------------------|------------------------|---------------------------|
| Main Housing + Nozzles     | 3D Print           | ABS / PC / Nylon      | Large part, good first layer needed |
| HVAT Rotor (blades)        | 3D Print           | ABS / PC / Nylon      | High strength required |
| Bearing Housers            | CNC or high-precision 3D Print | Aluminum or PC     | **Bore tolerance critical** (8.15–8.25 mm for 608ZZ) |
| Spacers (24–30 pcs)        | 3D Print           | PC / Nylon            | **Highest precision requirement** (±0.05 mm) |
| End Plates                 | 3D Print or CNC    | ABS / Aluminum        | Must be flat |
| Cavitation Nozzle + Orifices | 3D Print or CNC   | PC / Aluminum         | Internal surface finish important |
| Assembly Jig               | 3D Print           | ABS                   | Needs to stay flat |

## File Preparation Instructions for Upload

**Supported formats**: STL (easiest), STEP, IGES, etc.

**Recommended approach**:

1. Export all parts as **high-resolution STL** from OpenSCAD (use `$fn=128` or higher for final exports).
2. Zip the following folders/files:
   - `scad/` (all source files)
   - `scad/cd_dvd_version/` (alternative design)
   - `calibration_test_pieces/`
   - This specification document (`PCBWay_Design_Spec_and_Upload_Guide.md`)

3. For quotation, you can upload:
   - Individual STLs, **or**
   - One ZIP containing everything

**Note**: OpenSCAD cannot directly export STEP/IGES. If you need native CAD format:
- Import the STL into FreeCAD
- Convert to solid and export as STEP

## Quotation Request Checklist

When uploading, please include the following information in your message to PCBWay:

- This specification document
- Which variant(s) you want quoted (HDD, CD/DVD, or both)
- Whether you want 3D printing, CNC, or both options
- Preferred materials (see table above)
- Any quantity requirements (we usually need 1–2 full sets + spares)
- Whether you want the parts post-processed (sanded, polished, etc.)

## Contact / Version

**Project maintained at**: Modified-Tesla-Turbine-For-Cavitation repository

**Date of this spec**: May 2026

---

Thank you for your quotation. We look forward to working with you on this open scientific hardware project.
