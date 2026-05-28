/*
 * HVAT_BLADES.scad
 * Hybrid Vertical Axis Turbine (HVAT) rotor blades
 * Savonius drag scoops (bottom, for starting torque) + Helical Darrius (lift, smooth running)
 * Used as active flow straightener / mixer in the central exhaust of the HDD platter stack.
 *
 * Print separately and mount on central shaft (3-5 mm carbon fiber or steel) with bearings.
 * Designed for low-friction free rotation or light braking.
 *
 * From the May 2026 Grok design conversation.
 */

module hybrid_hvat(height=60, dia=28, savonius_overlap=0.7, twist=180) {
    // Helical Darrius (lift blades) — 3 blades, helical twist
    for (i = [0:2]) {
        rotate([0, 0, i*120]) {
            linear_extrude(height=height, twist=twist, slices=60)
                translate([dia/2 * 0.65, 0, 0])
                    square([dia*0.18, 2.2], center=true);  // thin airfoil approx
        }
    }

    // Savonius drag scoops at bottom for self-starting torque
    for (i = [0:1]) {
        rotate([0, 0, i*180]) {
            linear_extrude(height=height*0.45, twist=0)
                difference() {
                    circle(d=dia*0.95);
                    translate([dia*0.25, 0, 0]) circle(d=dia*0.6);
                }
        }
    }

    // Central hub (hollow for shaft)
    difference() {
        cylinder(d=dia*0.28, h=height, center=true, $fn=48);
        cylinder(d=dia*0.12, h=height+1, center=true, $fn=32);
    }
}

// Usage example — render and export STL
hybrid_hvat(height=60, dia=28, twist=120);  // adjust twist for pitch
