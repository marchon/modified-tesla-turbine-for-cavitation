# Operation: Setup, Tuning, Testing, and Result Tracking

This page provides concrete, step-by-step guidance for using the HDD Platter Flow Conditioner in real experiments.

## 1. Initial Setup (First Build)

### Mechanical Assembly Checklist

- [ ] All 25 platters thoroughly cleaned with 99% IPA on both faces.
- [ ] Stack assembled in the jig using 1.0 mm spacers (24 pcs).
- [ ] HVAT rotor spins freely on bearings with very low friction (critical).
- [ ] Bearing housers securely mounted to end plates.
- [ ] Nozzle manifold attached and leak-free at low pressure.
- [ ] Clear viewport installed for first characterization runs.

### First Air Test (Mandatory)

Connect low-pressure regulated air (start at 0.1–0.3 bar).

Observe through the viewport:

- Is the inward spiral symmetric and beautiful?
- Are all channels participating?
- How does the HVAT behave with brake fully open vs. lightly applied?

**Record video.** This footage is scientifically valuable on its own.

## 2. Tuning Methodology

### Primary Control Knobs (in rough order of impact)

| Knob                    | Effect                                      | Typical Range                  | Notes |
|-------------------------|---------------------------------------------|--------------------------------|-------|
| Inlet pressure / flow   | Overall velocity and Re in gaps             | 0.1 – 1.5 bar (air)            | Start low |
| HVAT brake position     | Residual swirl strength & jet coherence     | Fully open → fully locked      | Most powerful tuning parameter |
| Orifice diameter        | Final jet velocity & cavitation number σ    | 6, 8, 10, 12 mm                | Smaller = more intense |
| Inter-platter gap       | Channel count vs. velocity (build-time)     | 0.8 – 1.5 mm                   | Fixed after assembly |
| Gas type                | Density, viscosity, dissolved gas effects   | Air, Ar, D₂, etc.              | Major variable for LENR work |

### Recommended Tuning Sequence

1. Fix orifice at 8 mm.
2. Characterize spiral + HVAT behavior across a pressure sweep with brake open.
3. Find the brake setting that gives the subjectively “cleanest” exit jet (least turbulence, best axial coherence).
4. Lock that brake position (or note the setting) and begin liquid tests.
5. Later, deliberately vary brake position as an experimental axis.

## 3. Testing Protocols

### Level 1: Air Characterization (Do This First)

- Multiple pressures
- Brake open / 50% / closed
- High-speed or 4K video of spiral and exit jet
- Optional: smoke or fog for flow visualization

### Level 2: Basic Hydrodynamic Cavitation

- Distilled water + aluminum foil witness
- Conditioned air or argon injection
- Systematic orifice swap
- Document foil changes vs. injection parameters

### Level 3: Hybrid ULTR (Highest Value)

Combine the platter device with 40 kHz ultrasound.

Key matrix variables:
- With vs. without pre-conditioned gas stream
- Different HVAT brake settings
- Argon vs. air vs. deuterium-enriched
- Ultrasonic power levels

This is where the device is expected to show its greatest advantage over simpler injection methods.

## 4. Result Tracking (Minimum Viable Dataset)

For every meaningful run, record at minimum:

**Fluid dynamic boundary conditions**
- Inlet pressure (or mass flow if available)
- HVAT state (brake position or measured RPM)
- Orifice diameter
- Gas type + any pre-treatment

**Acoustic / Energy input**
- Ultrasonic power and frequency
- Transducer mounting location

**Environmental**
- Starting liquid temperature and volume
- Ambient conditions

**Observations**
- Video (through viewport + chamber)
- Still photos of foil before/after
- Temperature rise during run
- Any visible light emission
- Gas evolution notes

**Post-run analysis (when possible)**
- SEM/EDX on foil
- Mass spectrometry on evolved gas
- Radiation detector logs (with controls)

The device’s purpose is to make the first category (“Fluid dynamic boundary conditions”) dramatically more repeatable and characterizable than in previous work.

## 5. Safety & Best Practices

- Always start with air and plain water.
- Use proper pressure regulation and relief.
- Deuterium work: treat as flammable gas; use small quantities and good ventilation.
- When using ultrasound + high voltage drivers, follow electrical safety practices.
- If pursuing radiation claims, use appropriate detectors and conservative interpretation.

## 6. Iteration Ideas

Once you have baseline data, consider:

- Variable-pitch or servo-controlled HVAT (future OpenSCAD module)
- Integrated pressure sensors on the printed mounts
- Different platter counts or gaps for throughput vs. conditioning trade-offs
- Metal housing version for higher pressures or corrosive fluids
- Direct coupling of the cavitation nozzle into a sealed chamber with optical access

Document everything and share it. That is how this tool becomes genuinely valuable to the broader research effort.

---

See also:
- `build.md` for mechanical assembly details
- `testing.md` for the detailed Greenyer-style protocol
- `theory_and_value.md` for the scientific rationale
