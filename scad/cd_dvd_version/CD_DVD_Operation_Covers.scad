/*
 * CD/DVD Version - Operation Covers (Top and Bottom)
 * Solid versions for when viewport is not needed, plus bottom jet cover.
 */

module cd_dvd_operation_cover(has_orifice=false, orifice_d=12) {
    difference() {
        cylinder(d=120 + 28, h=7, center=true, $fn=128);
        
        if (has_orifice) {
            cylinder(d=orifice_d, h=9, center=true, $fn=48);
        }
        
        // Bolt pattern
        for (i = [0:5]) {
            rotate([0,0,i*60 + 15])
                translate([120/2 - 10, 0, 0])
                    cylinder(d=4.3, h=9, center=true, $fn=16);
        }
    }
}

// Solid top cover
cd_dvd_operation_cover(has_orifice=false);

// Bottom jet cover with orifice
translate([70, 0, 0])
    cd_dvd_operation_cover(has_orifice=true, orifice_d=12);
