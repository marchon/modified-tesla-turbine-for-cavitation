/*
 * ASSEMBLY_JIG.scad
 * Flat assembly jig that holds the platter stack perfectly straight during clamping.
 * Critical for even gaps and alignment.
 *
 * =============================================================================
 * 3D PRINTING NOTES
 * =============================================================================
 * This part must be very flat and rigid.
 *
 * Material: PETG or ABS. Needs good stiffness.
 *
 * Settings:
 *   - Layer height: 0.2 mm is fine
 *   - Infill: 35-40%
 *   - Perimeters: 5 (needs to stay flat under clamping force)
 *   - Print flat on the large face
 *   - Use a good first layer (critical for flatness)
 *
 * Post-processing:
 *   - Check flatness with a straight edge after printing
 *   - Sand bottom if necessary
 * =============================================================================
 *
 * From the May 2026 Grok design conversation.
 */

module assembly_jig() {
    difference() {
        union() {
            // Base plate
            cylinder(d=95 + 80, h=8, center=true, $fn=64);
            // Tall guide posts (match platter OD + clearance)
            for (i = [0:3]) {
                rotate([0,0,i*90 + 45])
                    translate([95/2 + 20, 0, 0])
                        cylinder(d=12, h=60, center=true, $fn=32);
            }
        }
        // Central clearance for the stack during assembly
        cylinder(d=95 + 2, h=10, center=true, $fn=64);
        
        // Access windows / cutouts for fingers/tools
        for (i = [0:3]) {
            rotate([0,0,i*90])
                translate([60, 0, 0])
                    cube([30, 40, 12], center=true);
        }
    }
}

assembly_jig();
