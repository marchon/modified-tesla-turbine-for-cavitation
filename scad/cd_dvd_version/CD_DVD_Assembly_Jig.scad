/*
 * CD/DVD Version - Assembly Jig
 * Larger version for 120mm discs.
 * Critical for keeping the stack perfectly straight during clamping.
 */

module cd_dvd_assembly_jig() {
    difference() {
        // Large base plate
        cylinder(d=120 + 70, h=8, center=true, $fn=128);
        
        // Guide posts (taller for thicker stack)
        for (i = [0:3]) {
            rotate([0,0,i*90 + 45])
                translate([120/2 + 18, 0, 0])
                    cylinder(d=14, h=65, center=true, $fn=32);
        }
        
        // Central clearance for the disc stack
        cylinder(d=120 + 3, h=10, center=true, $fn=128);
        
        // Access cutouts
        for (i = [0:3]) {
            rotate([0,0,i*90])
                translate([75, 0, 0])
                    cube([35, 50, 12], center=true);
        }
    }
}

cd_dvd_assembly_jig();
