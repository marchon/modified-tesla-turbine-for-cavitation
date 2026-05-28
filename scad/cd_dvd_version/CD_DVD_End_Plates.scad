/*
 * CD/DVD Version - End Clamp Plates
 * Larger diameter to match 120mm discs.
 */

module cd_dvd_end_plate(thickness=7) {
    difference() {
        cylinder(d=120 + 28, h=thickness, center=true, $fn=128);
        
        // Central hole sized for CD/DVD hub
        cylinder(d=16.5, h=thickness + 1, center=true, $fn=64);
        
        // 6x M4 bolt holes
        for (i = [0:5]) {
            rotate([0, 0, i*60 + 15])
                translate([120/2 - 10, 0, 0])
                    cylinder(d=4.3, h=thickness+2, center=true, $fn=16);
        }
    }
}

cd_dvd_end_plate(7);
