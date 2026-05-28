/*
 * CONFIG: Aggressive Cavitation
 * Goal: Maximize jet velocity and cavitation intensity for strong bubble collapse.
 *
 * Key changes from default:
 *   - Shallower nozzle angle (stronger spiral → more momentum concentration)
 *   - Smaller default orifice in usage examples (6mm)
 *   - Tighter gap for higher local velocities
 */

platter_od = 95;
num_platters = 22;         // Slightly fewer for higher velocity per channel
platter_thick = 0.9;
gap = 0.75;                // Tighter gap → higher shear

nozzle_count = 6;
nozzle_angle = 7;          // Shallower = stronger organized spiral
nozzle_w = 5.0;
nozzle_h = 1.6;

hv_dia = 26;               // Slightly smaller for tighter central flow
diffuser_len = 32;
diffuser_outlet_dia = 40;

total_stack_h = num_platters * (platter_thick + gap) - gap;

housing_od = platter_od + 2*3.8 + 12;
housing_id = platter_od + 2;

// ... rest of the file is identical to the main HDD_Platter_Cavitation_Conditioner.scad
// (copy the modules from the main file when using this config)
