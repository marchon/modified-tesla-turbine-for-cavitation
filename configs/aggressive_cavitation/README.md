# Aggressive Cavitation Configuration

**Intent**: Maximize cavitation intensity and bubble collapse violence.

**Key Changes**:
- Gap reduced to 0.75 mm (higher shear)
- Nozzle angle reduced to 7° (stronger spiral momentum transfer)
- Recommended orifice: 6 mm

**Expected Behavior** (from models):
- Higher jet velocity for given inlet pressure
- Lower cavitation number → more violent collapses
- Potentially smaller initial bubbles but higher energy release on collapse

**Use Case**: Studies looking for strong anomalous effects, sonoluminescence, or high-energy bubble dynamics.

**Warning**: Tighter gaps are harder to manufacture consistently. Use the calibration pieces extensively.

To use:
1. Copy the modified `HDD_Platter_Cavitation_Conditioner.scad` over your working copy (or use it as reference while editing parameters in the main file).
2. Also consider using the smaller orifice inserts.
3. Print extra spacers — tolerance is tight at this gap.
