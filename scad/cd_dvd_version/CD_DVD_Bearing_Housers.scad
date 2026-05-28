/*
 * CD/DVD Version - Bearing Housers
 * Adapted for larger central hub (CD 15mm hole) and slightly different scale.
 *
 * Print with high precision on the bore (see main printing guide).
 */

module cd_dvd_bearing_houser(od=28, id=8.2, h=9, flange_d=36) {
    difference() {
        union() {
            cylinder(d=od, h=h, center=true, $fn=64);
            cylinder(d=flange_d, h=3, center=true, $fn=64);
        }
        cylinder(d=id, h=h+2, center=true, $fn=48);
    }
}

// Upper and lower versions
translate([0, 0, 0])   cd_dvd_bearing_houser(h=9);
translate([40, 0, 0])  cd_dvd_bearing_houser(h=11);  // thicker lower
