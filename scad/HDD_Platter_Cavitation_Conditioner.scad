/*
 * HDD Platter Precision Flow Conditioner for Cavitation Experiments
 * Parametric OpenSCAD model — 25-platter default (fully adjustable)
 *
 * =============================================================================
 * 3D PRINTING NOTES (Critical for success)
 * =============================================================================
 * Recommended Material: PETG (best balance of strength, chemical resistance, 
 *                         low warping). ASA is excellent alternative for outdoor/UV.
 *                         Avoid PLA for functional parts (too brittle, poor temp resistance).
 *
 * Recommended Settings:
 *   - Layer height: 0.2 mm (0.15 mm for critical mating surfaces)
 *   - Infill: 30-40% Gyroid or Cubic (higher on HVAT blades & bearing housers)
 *   - Perimeters: 4-5 (important for pressure tightness and strength)
 *   - Top/Bottom layers: 5-6
 *   - Print orientation: Flat on base (this file is designed for it)
 *   - Supports: None required if printed as intended
 *   - Brim: 8-10 mm recommended on first layer for large parts
 *
 * Critical Tolerances in this file:
 *   - Bearing bore: +0.10 to +0.15 mm interference for press fit (608ZZ)
 *   - Platter cavity: +1.5 to +2.0 mm total clearance
 *   - Nozzle slits: Aim for clean edges, no elephant's foot
 *
 * Post-processing:
 *   - Lightly sand mating faces if needed for flatness
 *   - Clean all holes thoroughly
 *   - Anneal PETG (optional but recommended for better chemical/heat resistance)
 *
 * Print time estimate (PETG, 0.2mm, 35% infill): ~18-22 hours for main housing.
 * =============================================================================
 *
 * This is the main housing + 6 tangential nozzles + central HVAT hub + diffuser.
 * Designed for stationary (or very lightly rotating) use as a scientific
 * low-turbulence spiral flow injector into a cavitation chamber.
 *
 * Target: Bob Greenyer / MFMP-style repeatable hydrodynamic + ultrasonic
 * (ULTR) cavitation experiments.
 *
 * All dimensions in mm.
 * Default: 25 Enterprise 3.5" platters (95 mm OD), 1.0 mm gaps.
 *
 * License: CERN OHL-S-2 (hardware) + MIT (this source)
 */

// ==================== PARAMETERS (tweak these) ====================
platter_od = 95;           // mm — actual Enterprise 3.5" platter diameter
num_platters = 25;         // change this for taller/shorter stack
platter_thick = 0.9;       // typical enterprise ~0.9 mm
gap = 1.0;                 // inter-platter gap (0.8-1.5 mm sweet range)
wall = 3.8;                // housing wall thickness

nozzle_count = 6;          // 4-8 recommended; 6 is excellent uniformity
nozzle_angle = 10;         // degrees from true tangential (8-12° optimal)
nozzle_w = 5.5;            // slit width at exit
nozzle_h = 1.8;            // height of each nozzle slit (slightly > gap)

hv_dia = 28;               // central HVAT rotor diameter (fits platter hub opening)
diffuser_len = 38;
diffuser_outlet_dia = 44;  // gentle expansion after HVAT

total_stack_h = num_platters * (platter_thick + gap) - gap;

// Derived
housing_od = platter_od + 2*wall + 12;   // generous for nozzles + manifold
housing_id = platter_od + 2;             // small clearance around platters

// ==================== MODULES ====================

module housing() {
    difference() {
        // Main outer cylinder
        cylinder(d = housing_od, h = total_stack_h + 14, center=true);
        
        // Inner cavity for platter stack (with small clearance)
        cylinder(d = housing_id, h = total_stack_h + 4, center=true);
        
        // 6 tangential nozzles (rotated around circumference)
        for (i = [0 : nozzle_count-1]) {
            rotate([0, 0, i * (360 / nozzle_count)]) {
                // Position nozzle at outer radius, angled
                rotate([0, 90 - nozzle_angle, 0])
                    translate([0, platter_od/2 + 3, 0])
                        linear_extrude(height = nozzle_h, center=true)
                            polygon(points = [
                                [-nozzle_w/2, -15],
                                [ nozzle_w/2, -15],
                                [ nozzle_w/2 + 4,  22],
                                [-nozzle_w/2 + 4,  22]
                            ]);
            }
        }
        
        // Central opening (will be refined by HVAT hub + diffuser)
        cylinder(d = hv_dia + 6, h = total_stack_h + 20, center=true);
    }
}

// End clamp plates (top and bottom) — clamp the platter stack rigidly
module end_clamp_plate(thickness = 6) {
    difference() {
        cylinder(d = platter_od + 24, h = thickness, center=true);
        // Central clearance for HVAT shaft / hub
        cylinder(d = hv_dia + 8, h = thickness + 1, center=true);
        // Bolt pattern matching typical platter holes (6x equally spaced)
        for (i = [0 : 5]) {
            rotate([0, 0, i * 60 + 15])
                translate([platter_od/2 - 8, 0, 0])
                    cylinder(d=4.2, h=thickness+2, center=true);  // M4 clearance
        }
    }
}

// Central HVAT mounting hub (hollow tube with flanges for bearings)
module hvat_hub() {
    difference() {
        union() {
            // Outer hub (press-fit / glue into platter central holes)
            cylinder(d = hv_dia + 6, h = total_stack_h + 32, center=true);
            // Lower bearing flange
            translate([0,0,-total_stack_h/2 - 8])
                cylinder(d = hv_dia + 18, h = 8, center=true);
            // Upper bearing flange
            translate([0,0, total_stack_h/2 + 8])
                cylinder(d = hv_dia + 18, h = 8, center=true);
        }
        // Hollow bore for shaft + bearings (8 mm ID for 608ZZ)
        cylinder(d = 8.2, h = total_stack_h + 50, center=true);
        // Inner relief so HVAT rotor spins freely
        cylinder(d = hv_dia - 1.5, h = total_stack_h + 40, center=true);
    }
}

// Simple conical diffuser after the HVAT (gentle expansion)
module diffuser() {
    translate([0, 0, total_stack_h/2 + 12])
        linear_extrude(height = diffuser_len, scale = diffuser_outlet_dia / hv_dia)
            circle(d = hv_dia + 2);
}

// Example usage — render the complete main assembly (comment/uncomment as needed)
$fn = 96;

housing();
translate([0,0, total_stack_h/2 + 3]) end_clamp_plate(6);
translate([0,0,-total_stack_h/2 - 3]) end_clamp_plate(6);
hvat_hub();
diffuser();

// For quick preview of one nozzle only:
// rotate([0,0,30]) translate([platter_od/2 + 5, 0, 0]) 
//     rotate([0,90-nozzle_angle,0]) 
//         linear_extrude(2) square([nozzle_w, 30], center=true);

// ==================== USAGE NOTES ====================
// 1. Render (F6) → Export as STL for the parts you need.
// 2. Print housing, two end plates, HVAT hub, diffuser in PETG.
// 3. Print 24 spacer rings (see separate SPACER_RING.scad) at 1.0 mm.
// 4. See docs/build.md and DESIGN_NOTES.md for full assembly order,
//    recommended orifice sizes, HVAT blade module, bearing housers,
//    sensor mounts, and the separate cavitation jet nozzle (Venturi).
// 5. All major dimensions are parametric — change num_platters, gap,
//    nozzle_angle, etc. and everything updates.
//
// This file is the "master" housing. Other modules (HVAT blades,
// spacers, jigs, full cavitation nozzle with orifice inserts) are in
// companion .scad files in this directory for easier maintenance.
