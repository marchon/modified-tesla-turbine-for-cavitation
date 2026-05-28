/*
 * CAVITATION_NOZZLE.scad
 * Venturi-style converging-diverging nozzle + interchangeable orifice inserts
 * Optimized for high-velocity jet injection into liquid cavitation chamber.
 * Creates strong pressure drop + shear right at the exit for controlled bubble inception.
 *
 * Multiple orifice inserts (6/8/10/12 mm throat) for tuning intensity.
 * From the May 2026 Grok design conversation.
 */

// Main Venturi body (converging + throat + diverging)
module cavitation_jet_nozzle(in_d=28, throat_d=8, out_d=18, len=45) {
    difference() {
        // Outer body
        cylinder(d=in_d + 8, h=len, center=false, $fn=64);
        
        // Inlet cylinder
        cylinder(d=in_d, h=8, center=false, $fn=64);
        
        // Converging section (Venturi profile)
        translate([0,0,8])
            linear_extrude(height=12, scale=throat_d/in_d)
                circle(d=in_d, $fn=64);
        
        // Throat
        translate([0,0,20])
            cylinder(d=throat_d, h=5, center=false, $fn=64);
        
        // Diverging section
        translate([0,0,25])
            linear_extrude(height=20, scale=out_d/throat_d)
                circle(d=throat_d, $fn=64);
    }
}

// Removable orifice insert holder + family of inserts
module orifice_insert_holder() {
    difference() {
        cylinder(d=14, h=8, center=false, $fn=48);
        cylinder(d=12.2, h=9, center=false, $fn=48);  // holder bore
    }
}

module orifice_insert(throat_d=8) {
    difference() {
        cylinder(d=12, h=9, center=false, $fn=48);
        cylinder(d=throat_d, h=10, center=false, $fn=48);
    }
}

// Render examples
cavitation_jet_nozzle();
translate([40,0,0]) orifice_insert_holder();
translate([60,0,0]) orifice_insert(8);
translate([75,0,0]) orifice_insert(6);
translate([90,0,0]) orifice_insert(10);
translate([105,0,0]) orifice_insert(12);

// Print several orifice inserts for tuning bubble size/intensity during experiments.
