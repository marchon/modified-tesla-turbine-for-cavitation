/*
 * Flatness Test Plate
 * 
 * Useful for checking bed leveling and first layer consistency across a large area.
 * Especially important before printing large parts like the main housing or end plates.
 */

module flatness_test_plate() {
    difference() {
        cylinder(d=110, h=1.5, center=true, $fn=64);
        
        // Grid of small holes for measurement reference
        for (x = [-40:20:40]) {
            for (y = [-40:20:40]) {
                translate([x, y, 0])
                    cylinder(d=2, h=2, center=true, $fn=16);
            }
        }
    }
}

flatness_test_plate();
