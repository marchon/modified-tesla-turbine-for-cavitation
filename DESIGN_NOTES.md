# Design Notes & Rationale — HDD Platter Precision Flow Conditioner

This document captures the core reasoning, trade-offs, and specifications that emerged from the May 2026 design conversation (Grok share conversation archived as PDF screenshots).

## Original Goal Evolution

1. Initial concept: Modified Tesla turbine (tangential inlet, inward spiral, central exhaust) possibly hybridized with a central Vertical Axis Wind Turbine (VAWT) stage for extra energy extraction from the exiting swirl.
2. Clarified goal: The device is **primarily a scientific instrument for cavitation experiments**, not a power generator. The "turbine" (disc stack) runs stationary or at very low controlled speed. Its job is to act as a **high-quality, multi-channel, low-turbulence spiral flow straightener / conditioner** that delivers exceptionally uniform, repeatable gas or liquid injection into a cavitation chamber.
3. Later refinement: Add a lightly loaded or free-spinning central **Hybrid VAWT (HVAT)** core (Savonius for starting torque + helical Darrius for smooth operation) that further organizes the exiting flow into a cleaner, more axial, vortex-stabilized jet without the device being optimized for net power output.

The result is a **compound flow conditioner**: classic boundary-layer Tesla spiral + active HVAT straightener + final diffuser + tunable Venturi cavitation nozzle.

## Why Polished Enterprise HDD Platters?

- Mirror-smooth surfaces (sub-nanometer roughness in the data zones) are ideal for boundary-layer adhesion with minimal disruption.
- Extremely consistent thickness (~0.8–1.0 mm) and flatness when selected from the same model.
- Cheap / free from scrap / eBay lots of dead Enterprise drives (the 3.5" ones with the nice thick platters).
- 95 mm OD gives a good working radius for tangential inlets while remaining compact.
- Pre-drilled mounting holes (standard pattern) make stacking and clamping trivial.

Community precedent exists for using these exact platters in DIY Tesla turbines and vertical-axis wind devices.

## Critical Geometry Choices (Stationary Flow Conditioner Mode)

### Nozzle Angle (from true tangential)
- 5–15° recommended.
- **~10° is the practical sweet spot** for strong, progressive inward spiral while keeping entry smooth and minimizing shocks.
- 0° (perfectly tangential) maximizes tangential velocity but can be less forgiving in 3D-printed parts.
- >20–30° shortens the spiral too much and increases unwanted radial velocity.

### Number of Nozzles
- 4–8 equally spaced.
- **6 nozzles** chosen as excellent compromise (good azimuthal uniformity without making individual nozzles impractically narrow).

### Inter-Platter Gap
- 0.5–2 mm literature range for air; **0.8–1.5 mm** practical starting point.
- Default: **1.0 mm** (24 spacers for 25 platters). Easy to print, robust, gives strong multi-channel effect.
- Tighter gaps → higher velocity / shear for given flow rate; more channels.
- Wider gaps → easier visualization, lower pressure drop, still excellent conditioning.

### HVAT Core (when used)
- Diameter sized to fit the natural central opening after platter hub cutouts (~25–30 mm).
- Hybrid blade set: Savonius scoops at bottom for self-start + helical Darrius for smooth high-speed running.
- Acts as **flow straightener / mixer**, not turbine. The swirl energy that would otherwise be wasted is used to organize the exit flow.
- Can be braked (printed caliper) to tune residual swirl strength or left free-running.
- Dramatically improves jet uniformity into the cavitation chamber.

### Cavitation Nozzle (exit)
- Venturi-style converging-diverging profile accelerates the conditioned flow and creates the sharp pressure drop needed for bubble inception right at the injection point into liquid.
- Removable orifice inserts (6/8/10/12 mm throat) let the experimenter tune velocity / bubble size distribution without reprinting the whole nozzle.
- Threaded or clamped interface to the user's cavitation chamber.

## Materials & Reproducibility Emphasis

Everything was chosen so that a competent maker with a consumer FDM printer + a stack of dead Enterprise HDDs can replicate the device to high precision:

- PETG or ABS for all printed parts (durability, chemical resistance to common chamber fluids).
- M3/M4 stainless hardware.
- Standard 608ZZ bearings (or better ceramic if budget allows).
- 5–8 mm carbon-fiber or precision steel shaft for the HVAT.
- No exotic machining required for the first version (though CNC platters or metal housing are obvious future upgrades).

## Relation to Bob Greenyer / MFMP Work

The design directly addresses a recurring practical need in Greenyer-style cavitation experiments:

- ULTR (ultrasonic + aluminum foil in water) demos are simple and visually dramatic, but injection is often crude (ultrasonic horn or basic bubbler).
- Controlled, low-turbulence, multi-channel gas injection upstream of the cavitation zone should give far more repeatable bubble clouds, pressure histories, and shear conditions.
- This enables cleaner before/after SEM/EDX on foils, better mass-spec on evolved gases, more reliable neutron or "strange radiation" diagnostics, and systematic variation of parameters (gas type including deuterium, flow rate, swirl strength via HVAT brake, ultrasonic power, etc.).

The device is explicitly offered as a potential contribution to the open LENR toolkit that Greenyer and the MFMP community maintain.

## Open Questions / Future Work Captured in Conversation

- Variable-pitch or servo-controlled central HVAT blades for on-the-fly swirl tuning.
- Integrated pressure sensors + data logging (MPX5700 or similar on the printed sensor mounts).
- Full CFD validation of the 10° / 6-nozzle / 1 mm gap configuration (OpenFOAM recommended).
- Deuterium sparging protocols and safety interlocks.
- Hybrid mounting of a real ultrasonic horn directly to the cavitation chamber or even to the nozzle body.
- Larger stack versions (40+ platters) for higher throughput.
- Metal (aluminum or stainless) version of the housing for high-pressure / corrosive fluids.

All OpenSCAD code is written parametrically (`num_platters`, `gap`, `nozzle_angle_deg`, etc.) so these explorations are low-friction.

## References & Sources (from conversation)

- Tesla turbine boundary-layer theory (classic papers + Wikipedia summaries).
- Community HDD-platter Tesla / VAWT builds (various YouTube and forum threads).
- Bob Greenyer / MFMP: ULTR demos, EVO/plasmoid discussions, cavitation transmutation data, ISCMNS presentations, RemoteView Substack, LENR-Forum threads.
- Specific video links preserved in the design conversation (ULTR how-to, soliton impact, hydrogen mass-spec, etc.).

---

This device exists because someone wanted to give the MFMP community a better, more scientific "straw" for blowing perfectly conditioned gas into their cavitation experiments. Everything else followed from that single clear goal.

Build it, film the spiral, measure the bubbles, share the anomalies (or the null results). That is the spirit of the project.
