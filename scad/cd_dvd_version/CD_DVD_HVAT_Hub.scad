/*
 * CD/DVD Version - Central HVAT Hub
 * Designed to fit inside the standard 15mm CD/DVD center hole.
 */

module cd_dvd_hvat_hub() {
    difference() {
        union() {
            cylinder(d=14.6, h=70, center=true, $fn=64);   // Fits CD hole
            // Mounting flanges
            translate([0,0,-25]) cylinder(d=24, h=6, center=true, $fn=64);
            translate([0,0, 25]) cylinder(d=24, h=6, center=true, $fn=64);
        }
        cylinder(d=5.2, h=80, center=true, $fn=32);  // Shaft hole
    }
}

cd_dvd_hvat_hub();
