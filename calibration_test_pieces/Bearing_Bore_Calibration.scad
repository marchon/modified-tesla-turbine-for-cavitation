/*
 * 608ZZ Bearing Bore Calibration Set
 *
 * Print these rings to find the perfect bore size for your printer + filament combination.
 * Target for 608ZZ bearings (8.00mm OD): Usually 8.15 - 8.25mm printed bore.
 *
 * Test pieces go from 8.10mm to 8.30mm in 0.05mm steps.
 */

module bearing_test_ring(bore_d) {
    difference() {
        cylinder(d=26, h=8, center=true, $fn=64);   // Outer diameter matches typical houser
        cylinder(d=bore_d, h=9, center=true, $fn=64);
    }
}

// Generate test set
sizes = [8.10, 8.15, 8.20, 8.25, 8.30];

for (i = [0:len(sizes)-1]) {
    translate([i * 30, 0, 0])
        bearing_test_ring(sizes[i]);
}
