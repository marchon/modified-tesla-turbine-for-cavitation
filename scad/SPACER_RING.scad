/*
 * Precise spacer rings for HDD platter stack
 * 1.0 mm default (24 required for 25 platters @ 1 mm gap)
 * Lightening holes for material savings + easier printing
 * Parametric — change thickness or OD for your build
 */

module platter_spacer(od=95, thickness=1.0, id=30) {
    difference() {
        cylinder(d=od, h=thickness, center=true, $fn=96);
        cylinder(d=id, h=thickness+0.2, center=true, $fn=64);
        
        // 6 lightening holes (optional — remove if you want solid rings)
        for (i = [0:5]) {
            rotate([0,0,i*60 + 30])
                translate([od*0.32, 0, 0])
                    cylinder(d=6, h=thickness+0.2, center=true, $fn=32);
        }
    }
}

// Render one (or use in a loop in your slicer project)
platter_spacer(thickness=1.0);

// For batch export you can do:
// for (i=[1:24]) translate([i*3,0,0]) platter_spacer();
