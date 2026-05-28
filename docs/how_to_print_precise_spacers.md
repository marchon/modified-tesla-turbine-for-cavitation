# How to Hit ±0.05mm Spacer Thickness (Detailed Guide)

The spacer rings are the most critical printed parts for device performance. Inconsistent gaps destroy the low-turbulence flow you're trying to achieve.

**Target:** ±0.05 mm (ideally ±0.03 mm) on 1.0 mm or 1.3 mm spacers.

## Step-by-Step Calibration Process

### 1. Print the Calibration Set
Use the file:
`calibration_test_pieces/Spacer_Thickness_Calibration.scad`

Print 6–8 pieces in one job using your final intended settings.

### 2. Measure Properly
- Use a good digital caliper (0.01 mm resolution)
- Measure at center and at two points on the edge of each spacer
- Record all measurements
- Calculate average and standard deviation

### 3. Common Adjustments by Brand

#### Bambu Lab (X1/P1/A1) + Bambu Studio / Orca
- **Too thick overall**: Reduce "Flow rate" by 2–4% (try 96-98%)
- **Elephant's foot on first layer**: Increase "Initial Layer Height" to 0.22–0.25 mm
- **Inconsistent thickness**: Slow down "Top surface speed" to 80–100 mm/s
- Best profile base: Use the provided `PETG_High_Precision_for_Device.json`

#### Prusa MK4 / Mini + PrusaSlicer
- **Too thick**: Lower "Extrusion multiplier" to 0.96–0.98
- **First layer elephant's foot**: Enable "Elephant foot compensation" at 0.2–0.3 mm
- Use 0.15 mm or 0.12 mm QUALITY profile as base instead of 0.20 mm

#### Creality / Generic Printers + Cura or Orca
- **Too thick**: Reduce "Flow" to 96–98%
- **Inconsistent layers**: Increase "Wall Line Count" and slow down top layers
- Consider switching to a 0.15 mm or 0.12 mm profile for spacers specifically

### 4. Pro Tips for ±0.03 mm Results

- Print spacers **last**, after you've dialed in your printer on the big parts.
- Use the **same filament spool** for the entire spacer batch.
- Dry your filament (PETG especially loves moisture).
- Print with a **0.12 mm or 0.15 mm layer height** for spacers even if you use 0.2 mm everywhere else.
- Avoid "fuzzy skin" or any surface modifiers on spacers.
- After printing, let parts cool completely before measuring.

### 5. When to Give Up on a Batch

If after 2–3 calibration rounds your standard deviation is still > 0.08 mm, consider:
- Switching filament brands
- Printing solid (100% infill) spacers instead of using lightening holes
- Using a different material (some PETG brands are simply more consistent than others)

## Quick Decision Tree

- Average thickness > target + 0.08 mm → Reduce flow
- First layer much thicker than rest → Elephant foot compensation or first layer height
- High variation between pieces → Environmental (temperature, moisture, speed)

Good luck — consistent spacers are what separate a good device from a great one.
