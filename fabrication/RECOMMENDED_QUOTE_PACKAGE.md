# Recommended Quote Package for External Fabrication

This folder contains everything you need to request professional manufacturing quotes (3D printing or CNC machining) for the **Precision Flow Conditioner** project.

## Quick Start

1. Decide which version(s) you want quoted:
   - **HDD Platter version** (higher performance)
   - **CD/DVD version** (much cheaper and easier to source)

2. Decide manufacturing method:
   - 3D Printing (most common and affordable)
   - CNC Machining (highest precision / metal parts)

3. Choose the appropriate spec document:
   - General / 3D Printing → `pcbway/PCBWay_Design_Spec_and_Upload_Guide.md`
   - Focused on CNC Metal → `pcbway/PCBWay_CNC_Metal_Spec.md`

4. Prepare your files (see below).

## Recommended Upload Package Structure

Create a ZIP with this structure:

```
Flow_Conditioner_Quote_Package_YYYY-MM-DD/

├── README_This_File.md
├── pcbway/
│   ├── PCBWay_Design_Spec_and_Upload_Guide.md   (always include)
│   ├── PCBWay_CNC_Metal_Spec.md                 (if requesting CNC)
│   └── ZIP_Contents_for_Upload.txt

├── Source_Files/
│   ├── scad/                                    (HDD version)
│   └── scad/cd_dvd_version/                     (CD/DVD version)

├── Calibration_Pieces/                          (optional but useful)
│   └── calibration_test_pieces/

├── Slicer_Profiles/                             (reference for 3D printing)
│   └── slicer_profiles/

└── STL_Files/                                   (you must export these)
    ├── HDD_Version/
    └── CD_DVD_Version/
```

## What to Export Before Uploading

You need to export the actual 3D models:

**From OpenSCAD**:
- Set `$fn = 128;` or higher for final exports
- Render (F6) then Export as STL for each major part

**Strongly recommended parts to export**:
- Main housing
- HVAT blades / rotor
- Bearing housers (most tolerance-critical)
- Spacers (batch)
- End plates
- Cavitation nozzle + orifice inserts
- Assembly jig

## Tips for Getting Good Quotes

- Be clear about quantities (1 set + spares is common)
- Mention you are open to hybrid manufacturing (e.g. CNC the bearing housers + nozzle, 3D print everything else)
- For CNC: Ask about surface finish on internal flow paths
- Attach the relevant spec document — it saves everyone time

## Folder Contents

- `pcbway/` — All documents prepared specifically for PCBWay (easily adaptable to other services)
- `RECOMMENDED_QUOTE_PACKAGE.md` — This file

---

This package was prepared as part of the open hardware project **Modified-Tesla-Turbine-For-Cavitation**.
