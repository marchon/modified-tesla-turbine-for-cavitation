/*
 * CD/DVD Version - Clear Viewport Plate
 * For observing the spiral flow during air testing.
 * Print in clear PETG if possible.
 */

module cd_dvd_clear_viewport() {
    difference() {
        cylinder(d=120 + 28, h=7, center=true, $fn=128);
        
        // Central opening
        cylinder(d=33, h=9, center=true, $fn=64);
        
        // Bolt holes
        for (i = [0:5]) {
            rotate([0,0,i*60 + 15])
                translate([120/2 - 10, 0, 0])
                    cylinder(d=4.3, h=9, center=true, $fn=16);
        }
    }
}

cd_dvd_clear_viewport();
