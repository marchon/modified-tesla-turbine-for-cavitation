# Design Rationale & Key Specifications

This page summarizes the engineering decisions captured during the May 2026 design conversation.

## Goal Clarification

The device is **not** intended as a power-producing turbine. It is a **precision flow conditioner** whose sole job is to deliver exceptionally uniform, low-turbulence, spiraled gas or liquid from tangential inlets to a central exit that then feeds a cavitation chamber.

The original hybrid VAWT idea was retained in a modified form: a lightly loaded central **HVAT (Hybrid Vertical Axis Turbine)** rotor that uses residual swirl energy to further straighten and organize the exit flow rather than to extract net electrical power.

## Why HDD Platters?

Enterprise 3.5" platters (95 mm OD) from dead server drives are:

- Mirror-polished to sub-nanometer roughness — perfect boundary layer behavior
- Extremely consistent in thickness and flatness
- Free / very cheap in bulk
- Already have convenient central hub geometry and mounting holes

## Geometry That Matters

| Parameter              | Recommended Value      | Rationale |
|------------------------|------------------------|---------|
| Nozzle angle (from tangent) | 8–12° (10° default)   | Strong inward spiral without excessive radial velocity or shock |
| Number of nozzles      | 6                      | Excellent azimuthal uniformity; easy 3D printing |
| Inter-platter gap      | 0.8–1.5 mm (1.0 mm default) | Good channel count + practical printing + strong multi-channel effect |
| HVAT rotor diameter    | ~28 mm                 | Fits the natural central opening; provides active straightening |
| Diffuser divergence    | 6–8° half-angle        | Avoids flow separation while recovering pressure |

## Materials for Reproducibility

All structural parts are designed to be printed in PETG or ABS on a consumer FDM machine. The only non-printed "exotic" components are:

- 25 matched Enterprise HDD platters (cleaned with IPA)
- Two 608ZZ bearings (or ceramic)
- M3/M4 stainless hardware
- 5–8 mm shaft stock for the HVAT

This keeps the entire device accessible to the open LENR community.

## Relation to Greenyer / MFMP Research

The design directly attacks the "injection variability" problem in hydrodynamic and hybrid ultrasonic cavitation experiments. By providing a repeatable, multi-channel, low-turbulence spiral inlet + tunable HVAT + precision Venturi nozzle, experimenters can vary one parameter at a time (gas type, flow rate, residual swirl, ultrasonic power, foil material, deuterium concentration, etc.) while keeping the fluid dynamic boundary conditions far more constant than with a simple bubbler or horn.

This is exactly the spirit of the MFMP: radical accessibility + obsessive documentation + public data.

## Future Directions (Open)

- Servo-controlled variable-pitch HVAT
- Integrated data logging (pressure + temperature + neutron/gamma)
- Full OpenFOAM validation of the 10° / 6-nozzle baseline
- Larger (40+ platter) high-throughput version
- Metal (aluminum) housing for higher pressures or aggressive fluids

All OpenSCAD files are parametric so these variants are straightforward to explore.
