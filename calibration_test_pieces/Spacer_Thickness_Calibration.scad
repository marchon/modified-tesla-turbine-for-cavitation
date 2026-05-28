/*
 * Spacer Thickness Calibration Test Piece
 * 
 * PURPOSE: Help you dial in your printer to hit the critical spacer thickness tolerance.
 * Target: ±0.05mm or better on 1.0mm or 1.3mm spacers.
 *
 * Print 5-6 of these, measure with digital calipers, and adjust flow rate / first layer height.
 *
 * Recommended use:
 * - Print at your intended layer height (0.12mm or 0.15mm recommended)
 * - Print all test pieces in one job
 * - Measure center and edges of each piece
 */

// Adjustable parameters
test_thickness = 1.0;      // Change to 1.3 for CD/DVD version
test_od = 95;              // 95 for HDD, 120 for CD/DVD
test_id = 30;

module calibration_spacer() {
    difference() {
        cylinder(d=test_od, h=test_thickness, center=true, $fn=96);
        cylinder(d=test_id, h=test_thickness+0.2, center=true, $fn=64);
        
        // 4 measurement markers (small notches)
        for (i = [0:3]) {
            rotate([0,0,i*90])
                translate([test_od/2 - 3, 0, 0])
                    cylinder(d=1.5, h=test_thickness+0.2, center=true, $fn=16);
        }
    }
}

// Print 6 test pieces
for (i = [0:5]) {
    translate([i * (test_od + 8), 0, 0])
        calibration_spacer();
}
