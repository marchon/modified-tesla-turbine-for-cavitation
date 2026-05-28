# Ultrasonic Hybrid (ULTR-Style) Integration

The platter flow conditioner was explicitly designed to be paired with ultrasonic cavitation in the style of Bob Greenyer’s well-known ULTR experiments.

## Why Hybridize?

Pure ultrasonic or pure hydrodynamic cavitation each have strengths and weaknesses. Combining a precision-controlled hydrodynamic jet (from the HDD platter stack + HVAT) with a 40 kHz ultrasonic field gives experimenters the best of both:

- Highly repeatable bubble size distribution and injection conditions (from the platter device)
- Violent collapse energy from the ultrasonic field
- Ability to tune vorticity (via HVAT brake) while the ultrasonic horn provides the main power

Greenyer and others have reported that certain anomalous effects (microspheres, transmutation signatures, “strange radiation”) appear more reliably or intensely in well-controlled hybrid setups.

## Recommended Transducer Setup

- Frequency: 40 kHz (sweet spot for strong cavitation in water without excessive heating)
- Power: 50–100 W for small chambers (2–5 L). Larger chambers need proportionally more.
- Driver: Cheap generic ultrasonic cleaner boards on AliExpress/eBay work surprisingly well for initial experiments. For more control, use a dedicated laboratory ultrasonic processor with horn.
- Mounting:
  - Bolt or epoxy the transducer/horn to the bottom of the cavitation chamber (most common).
  - Or immerse the nozzle exit directly into a small ultrasonic bath.
  - Use the clear viewport on the platter device to observe how the conditioned gas stream interacts with the ultrasonic field.

## Expected Observable Signatures (from Greenyer’s Work)

When running the hybrid system you should look for:

- Classic foil erosion: “snakes”, craters, pitting
- Microsphere formation (often iron-rich and crenelated — a Greenyer signature)
- Gas evolution (H₂ and others)
- Possible light flashes (sonoluminescence) in darkened conditions
- Temperature anomalies or excess heat (monitor carefully)
- Transmutation traces on witness foils (requires SEM/EDX or mass spectrometry after the run)
- “Strange radiation” tracks on CR-39 or other detectors (advanced / controversial)

## Tuning Parameters

Record these for every run:

- Inlet pressure / total flow rate through the platter device
- HVAT rotation speed and brake setting (this directly affects swirl and bubble clustering)
- Ultrasonic power and frequency
- Gas type (air, argon for brighter SL, deuterium-enriched for fusion-leaning claims)
- Orifice diameter (6/8/10/12 mm)
- Witness material and placement
- Chamber geometry and liquid volume

The combination of the platter device’s low-turbulence spiral + tunable HVAT + ultrasonic field gives you far more knobs than a simple ultrasonic cleaner alone.

## Practical Tips

- Start with plain water + aluminum foil + 8 mm orifice + moderate ultrasonic power. Get the baseline “ULTR look” working first.
- Then introduce the conditioned gas stream and observe how the bubble cloud changes.
- Many researchers report that pre-existing microbubbles from the hydrodynamic jet seed the ultrasonic cavitation and change the collapse dynamics.

See the exact video links and data in `references.md`.

This hybrid approach is one of the most promising low-cost, high-documentation directions in current open LENR/cavitation research.
