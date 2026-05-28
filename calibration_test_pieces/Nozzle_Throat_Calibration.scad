/*
 * Nozzle Throat Diameter Calibration Set
 * 
 * The throat diameter of the cavitation nozzle is one of the most important
 * experimental variables. Small changes have large effects on jet velocity.
 *
 * Print these and measure the actual printed diameter (they often come out
 * slightly undersized due to shrinkage/cooling).
 */

module nozzle_test_ring(throat_d) {
    difference() {
        cylinder(d=14, h=6, center=true, $fn=48);
        cylinder(d=throat_d, h=7, center=true, $fn=48);
    }
}

// Common sizes used in the project
sizes = [5.8, 6.0, 7.8, 8.0, 9.8, 10.0, 11.8, 12.0];

for (i = [0:len(sizes)-1]) {
    translate([i * 18, 0, 0])
        nozzle_test_ring(sizes[i]);
}
