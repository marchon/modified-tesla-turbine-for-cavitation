/*
 * CLEAR_VIEWPORT.scad
 * Optional clear top plate (print in clear PETG) so you can observe the beautiful
 * inward spiral flow during low-pressure air tests.
 * Also functions as a solid cover when swapped with the printed version.
 * From the May 2026 Grok design conversation.
 */

module clear_viewport() {
    difference() {
        cylinder(d=95 + 28, h=6, center=true, $fn=64);
        // Central opening (match HVAT / diffuser)
        cylinder(d=28 + 6, h=7, center=true, $fn=48);
        
        // Bolt holes matching platter pattern (6x)
        for (i = [0:5]) {
            rotate([0,0,i*60 + 15])
                translate([95/2 - 8, 0, 0])
                    cylinder(d=4.2, h=8, center=true, $fn=16);
        }
    }
}

clear_viewport();
