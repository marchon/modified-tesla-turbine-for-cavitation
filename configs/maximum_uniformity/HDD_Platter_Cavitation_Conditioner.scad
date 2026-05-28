/*
 * CONFIG: Maximum Uniformity
 * Goal: Best possible channel-to-channel and time-averaged flow consistency.
 */

platter_od = 95;
num_platters = 34;         // High channel count
platter_thick = 0.9;
gap = 1.1;                 // Sweet spot for uniformity vs manufacturability

nozzle_count = 8;          // More nozzles for better azimuthal uniformity
nozzle_angle = 8;          // Shallower for longer, smoother spiral development
nozzle_w = 4.8;
nozzle_h = 1.7;

hv_dia = 27;
diffuser_len = 45;         // Longer diffuser for gentler expansion
diffuser_outlet_dia = 46;

total_stack_h = num_platters * (platter_thick + gap) - gap;

housing_od = platter_od + 2*3.8 + 14;  // Slightly wider to accommodate 8 nozzles
housing_id = platter_od + 2;
