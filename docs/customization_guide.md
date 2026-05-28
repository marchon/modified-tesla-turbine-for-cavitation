# Customization Guide

This guide shows exactly how to modify the design for different experimental goals using the provided OpenSCAD models and Python tools.

**All changes are parametric** — no need to rewrite geometry from scratch.

## 1. OpenSCAD Parameter Customization (Easiest Starting Point)

### HDD Platter Version (`scad/HDD_Platter_Cavitation_Conditioner.scad`)

Open the file and edit the top section:

```scad
// ==================== PARAMETERS (tweak these) ====================
platter_od = 95;           // mm — actual Enterprise 3.5" platter diameter
num_platters = 25;         // change this for taller/shorter stack
platter_thick = 0.9;       // typical enterprise ~0.9 mm
gap = 1.0;                 // inter-platter gap (0.8-1.5 mm sweet range)

nozzle_count = 6;          // 4-8 recommended
nozzle_angle = 10;         // degrees from true tangential (8-12° optimal)
nozzle_w = 5.5;            // slit width at exit

hv_dia = 28;               // central HVAT rotor diameter
diffuser_len = 38;
diffuser_outlet_dia = 44;
```

**Common modifications and expected effects:**

- **Increase `num_platters` to 30–35**: More flow channels, potentially smoother output, taller device.
- **Decrease `gap` to 0.8 mm**: Higher velocity and shear for same flow rate (more intense cavitation possible, harder to print consistently).
- **Change `nozzle_angle` to 8°**: Stronger inward spiral, potentially better conditioning but higher pressure drop.
- **Change `nozzle_angle` to 15°**: Easier flow, less aggressive spiral.

After editing, press **F6** (Render), then **File → Export → Export as STL**.

### CD/DVD Version (`scad/cd_dvd_version/CD_DVD_Flow_Conditioner.scad`)

Similar parameters, but tuned for 120 mm discs:

```scad
disc_od = 120;
disc_thickness = 1.2;
num_discs = 20;            // Often fewer discs than HDD version because discs are thicker
gap = 1.2;                 // Slightly larger recommended gap

nozzle_angle = 10;
hv_dia = 32;               // Larger central hub for CD/DVD 15mm hole
```

**Tip**: The CD/DVD version is excellent for rapid prototyping different gap/nozzle configurations because blank discs are cheap and easy to source.

## 2. Python Generator Customization Examples

### Generate Performance Graphs for a Specific Configuration

Edit `python/generate_performance_graphs.py` or run it after modifying the internal models.

Example — to explore effect of very small gaps:

```python
# In generate_performance_graphs.py, modify the gap range
gaps = np.linspace(0.5, 1.5, 50)   # was 0.6 to 1.8
```

Then run:

```bash
python python/generate_performance_graphs.py
```

New graphs will be saved to `illustrations/performance_graphs/`.

### Generate Engineering Drawings for Custom Parameters

The drawing generator currently uses hardcoded defaults that match the OpenSCAD defaults.

To match a custom build:

1. Edit the top of `python/generate_engineering_drawings.py` (platter_od, num_platters, gap, nozzle_angle, etc.).
2. Run:

```bash
python python/generate_engineering_drawings.py
```

This will produce new PNG/SVG files reflecting your exact configuration.

### Generate DXF Files for Custom Disc Diameter

Example: You built the CD/DVD version with 20 discs at 1.3 mm gap:

Edit `python/generate_dxf_exports.py` and change:

```python
write_spacer_ring_dxf("my_custom_spacer.dxf", od=120, id=16, thickness=1.3)
```

Then run the script. The resulting DXF can be used directly for laser cutting alternative spacers (e.g., from thin plastic sheet or metal).

## 4. Before / After OpenSCAD Examples for Common Modifications

Here are practical before-and-after diffs for the most common useful changes.

### Example A: Switch from Default 25 platters @ 1.0 mm gap to a taller, gentler stack (32 platters @ 1.4 mm gap)

**Before (default):**
```scad
num_platters = 25;
gap = 1.0;
```

**After:**
```scad
num_platters = 32;   // +7 discs → more parallel channels
gap = 1.4;           // gentler flow, easier printing
```

Expected outcome: Smoother time-averaged flow, lower shear per channel, easier to manufacture spacers.

### Example B: More aggressive cavitation (smaller nozzle angle + smaller orifice)

**Before:**
```scad
nozzle_angle = 10;
```

**After (in the cavitation nozzle file as well):**
```scad
nozzle_angle = 7;    // stronger spiral
```

Then in your cavitation nozzle usage:
```scad
cavitation_jet_nozzle(..., throat_d=6);   // instead of 8 mm
```

Expected: Higher jet velocity and lower cavitation number → more violent bubble collapse.

### Example C: Maximize HVAT conditioning effect (larger rotor for CD/DVD version)

In `scad/cd_dvd_version/CD_DVD_Flow_Conditioner.scad`:

**Before:**
```scad
hv_dia = 32;
```

**After:**
```scad
hv_dia = 36;   // larger rotor for stronger swirl conditioning
```

Remember to also adjust the corresponding hub and bearing houser files in the same folder.

### Example D: Quick prototyping with CD/DVD version (fewer discs)

In `scad/cd_dvd_version/CD_DVD_Flow_Conditioner.scad`:

**Before:**
```scad
num_discs = 20;
```

**After (for very fast iteration):**
```scad
num_discs = 12;   // shorter stack, faster prints, good for initial tuning
```

This is excellent when you want to test multiple gap or angle combinations quickly.

**Pro tip**: Keep your "golden" working parameters in a separate text file or commented block at the top of each SCAD file so you can easily switch between "research mode" and "rapid prototype mode".


## 3. Visual "Customization Quick Reference" Diagram

A diagram has been generated showing the main control knobs and their primary effects:

**Location**: 
- `illustrations/performance_graphs/customization_quick_reference.png` (and .svg)
- Printable one-page A4 PDF: `illustrations/performance_graphs/Customization_Quick_Reference_Printable.pdf` (also in `docs/_static/`)

It is also embedded in the Sphinx documentation under the Tools and Software section for easy navigation.

The diagram illustrates the relationship between:

- Gap size → Reynolds number & flow regime
- Nozzle angle → Spiral strength vs. pressure drop
- HVAT brake position → Swirl reduction vs. jet coherence
- Number of discs → Number of parallel channels vs. stack height
- Orifice diameter → Jet velocity & cavitation intensity

(If the file does not exist yet in your checkout, run `python python/generate_performance_graphs.py` after the latest updates.)

## 4. Simulated Performance Characteristics (Important Disclaimers)

The graphs in `illustrations/performance_graphs/` are **software estimates only**, based on simplified analytical models (continuity + boundary layer scaling + cavitation number definitions).

**They are NOT CFD results** and should be treated as directional guidance only.

### What Different Configurations Are Expected to Do (Qualitative)

**Smaller gaps (0.6–0.8 mm)**:
- Higher local velocities for the same mass flow
- Higher Reynolds numbers → transition toward more turbulent (but still organized) flow
- Potentially more intense shear and smaller initial bubble sizes
- Harder to manufacture consistently

**Larger gaps (1.4–1.8 mm)**:
- Lower velocities, gentler cavitation
- Easier printing and assembly
- Possibly larger, more chaotic bubbles

**Lower nozzle angle (6–8°)**:
- Longer spiral path inside the stack
- More opportunity for boundary layer momentum transfer
- Higher pressure drop across the device

**Higher nozzle angle (12–15°)**:
- Shorter, more direct flow path
- Easier to drive high flow rates
- Less conditioning effect

**HVAT brake partially engaged (30–50% locked)**:
- Significant reduction in residual swirl
- Much cleaner, more axial jet entering the cavitation chamber
- One of the highest-leverage "tuning knobs" available without reprinting parts

**More discs (30+)**:
- More parallel flow channels
- Potentially smoother time-averaged output
- Taller overall device, more material usage

These behaviors are consistent with boundary layer theory and observed behavior in similar devices, but every physical build will deviate based on surface finish, alignment precision, inlet manifold quality, etc.

**Recommendation**: Use the Python generators to explore "what if" scenarios, then validate with your physical prototype using the calibration pieces and viewport.

## Next Steps for Experimenters

1. Start with the default parameters in both the HDD and CD/DVD versions.
2. Use the calibration pieces to lock in your printer's real-world tolerances.
3. Build one device with the defaults.
4. Use the Python tools to predict the effect of one change at a time.
5. Modify only that parameter, rebuild, and compare results.

### Ready-to-Use Example Configurations

For convenience, several pre-tuned configurations are provided in the `configs/` directory:

- `aggressive_cavitation/` — Maximize collapse intensity
- `gentle_high_throughput/` — High flow with milder conditions
- `maximum_uniformity/` — Best conditioning quality
- `rapid_prototyping_cd_dvd/` — Fast iteration using cheap discs

Each folder contains a modified `.scad` file + a README explaining the rationale and expected behavior. Copy the file into your working directory to use it.

This systematic approach is exactly what makes the device valuable for serious cavitation research.

All source files are designed to make this kind of iterative experimentation as frictionless as possible.