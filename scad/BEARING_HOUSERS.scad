/*
 * BEARING_HOUSERS.scad
 * Upper and lower bearing housers for the central HVAT rotor (608ZZ bearings)
 * Press-fit tolerance (+0.1 mm interference on bore).
 * Flanged for screwing to top/bottom end plates.
 *
 * From the May 2026 Grok design conversation.
 */

module bearing_houser(od=24, id=8.2, h=8, flange_d=32) {
    difference() {
        union() {
            // Main cylinder (press fit for bearing)
            cylinder(d=od, h=h, center=true, $fn=64);
            // Mounting flange
            cylinder(d=flange_d, h=3, center=true, $fn=64);
        }
        // Bearing bore (slight interference for press fit)
        cylinder(d=id, h=h+2, center=true, $fn=48);
    }
}

// Upper and lower (lower can be thicker for stability)
translate([0, 0, 0])   bearing_houser(h=8, flange_d=32);   // upper
translate([50, 0, 0]) bearing_houser(h=10, flange_d=32);  // lower (thicker)

// Mounting: screw flanges to top and bottom end plates.
// Add thin PTFE thrust washer between HVAT top and upper bearing if needed.
