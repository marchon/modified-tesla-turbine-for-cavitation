/*
 * SHIPPING_INSERTS.scad
 * Thicker inserts (1.4 mm) to protect the precise 1.0 mm gaps during shipping/transport.
 * Replace with normal 1.0 mm spacers for operation.
 * Print 24-26 of these.
 * From the May 2026 Grok design conversation.
 */

module shipping_insert(thick=1.4) {
    difference() {
        cylinder(d=95, h=thick, center=true, $fn=64);
        cylinder(d=30, h=thick+0.2, center=true, $fn=48);
        
        // Lightening / easy removal tabs
        for (i = [0:2]) {
            rotate([0,0,i*120])
                translate([95*0.35, 0, 0])
                    cube([8, thick+1, 12], center=true);
        }
    }
}

// Example: one insert
shipping_insert(1.4);
