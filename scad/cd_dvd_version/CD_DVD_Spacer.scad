/*
 * Spacer for CD/DVD Version
 * Recommended thickness: 1.2 - 1.5mm (to match thicker CD/DVD discs)
 */

module cd_dvd_spacer(od=120, thickness=1.3, id=16) {
    difference() {
        cylinder(d=od, h=thickness, center=true, $fn=128);
        cylinder(d=id, h=thickness+0.2, center=true, $fn=64);
        
        // Lightening holes
        for (i = [0:7]) {
            rotate([0,0,i*45 + 22.5])
                translate([od*0.34, 0, 0])
                    cylinder(d=7, h=thickness+0.2, center=true, $fn=32);
        }
    }
}

cd_dvd_spacer(thickness=1.3);
