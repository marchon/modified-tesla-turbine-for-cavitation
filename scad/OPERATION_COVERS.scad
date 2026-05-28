/*
 * OPERATION_COVERS.scad
 * Solid top and bottom covers (alternative to clear viewport).
 * Top cover can have central jet orifice when used without HVAT.
 * From the May 2026 Grok design conversation.
 */

module operation_cover(has_central_orifice=false, orifice_d=12) {
    difference() {
        cylinder(d=95 + 28, h=6, center=true, $fn=64);
        if (has_central_orifice) {
            cylinder(d=orifice_d, h=8, center=true, $fn=48);
        }
        // Bolt pattern
        for (i = [0:5]) {
            rotate([0,0,i*60 + 15])
                translate([95/2 - 8, 0, 0])
                    cylinder(d=4.2, h=8, center=true, $fn=16);
        }
    }
}

// Top solid cover (no orifice)
operation_cover(has_central_orifice=false);

// Bottom jet cover (with orifice for direct chamber connection)
translate([60,0,0]) operation_cover(has_central_orifice=true, orifice_d=12);
