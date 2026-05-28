/*
 * CONFIG: Gentle High Throughput
 * Goal: High flow rate with relatively gentle cavitation conditions.
 */

platter_od = 95;
num_platters = 28;         // More channels for throughput
platter_thick = 0.9;
gap = 1.5;                 // Larger gap = easier flow, gentler conditions

nozzle_count = 6;
nozzle_angle = 13;         // Steeper angle = less resistance
nozzle_w = 6.5;
nozzle_h = 2.2;

hv_dia = 30;
diffuser_len = 40;
diffuser_outlet_dia = 48;

total_stack_h = num_platters * (platter_thick + gap) - gap;

housing_od = platter_od + 2*3.8 + 12;
housing_id = platter_od + 2;

// ... rest of modules same as main file
