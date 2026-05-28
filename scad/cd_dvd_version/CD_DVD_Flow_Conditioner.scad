/*
 * CD/DVD Version - Precision Flow Conditioner for Cavitation Experiments
 *
 * Alternative design using standard CD/DVD discs (120mm diameter, ~1.2mm thick)
 * instead of hard drive platters.
 *
 * Advantages over HDD platter version:
 *   - Extremely cheap and easy to source (blank CDs/DVDs or used media)
 *   - Consistent 120mm diameter
 *   - Standard 15mm central hole (easier mounting)
 *   - Thicker discs (1.2mm) → potentially different flow characteristics
 *
 * Disadvantages:
 *   - Polycarbonate surface is not as perfectly smooth as HDD platters
 *   - May have slight variations in thickness between brands
 *   - Central hole is larger, requiring different hub design
 *
 * Recommended: Use high-quality blank CD-R or DVD-R for best consistency.
 *
 * All dimensions in mm.
 * Default: 20 discs (adjustable), ~1.2mm thick, 1.0-1.5mm gaps recommended.
 *
 * License: CERN OHL-S-2 (hardware) + MIT (this source)
 */

// ==================== PARAMETERS ====================
disc_od = 120;             // Standard CD/DVD diameter
disc_thickness = 1.2;      // Typical CD/DVD thickness
num_discs = 20;            // Number of discs (adjust based on stack height goal)
gap = 1.2;                 // Recommended gap (slightly larger than HDD version due to surface)

wall = 4.0;                // Housing wall thickness (slightly thicker for larger diameter)

nozzle_count = 6;
nozzle_angle = 10;         // degrees from tangent
nozzle_w = 6.5;            // Wider slits for larger discs
nozzle_h = 2.0;

hv_dia = 32;               // Slightly larger central HVAT for 15mm CD hole + hub
diffuser_len = 42;
diffuser_outlet_dia = 48;

total_stack_h = num_discs * (disc_thickness + gap) - gap;

// Derived
housing_od = disc_od + 2*wall + 14;
housing_id = disc_od + 2.5;   // Clearance for CD/DVD

// ==================== MODULES ====================

module housing() {
    difference() {
        cylinder(d = housing_od, h = total_stack_h + 16, center=true, $fn=128);
        
        cylinder(d = housing_id, h = total_stack_h + 5, center=true, $fn=128);
        
        // 6 tangential nozzles
        for (i = [0 : nozzle_count-1]) {
            rotate([0, 0, i * (360 / nozzle_count)]) {
                rotate([0, 90 - nozzle_angle, 0])
                    translate([0, disc_od/2 + 4, 0])
                        linear_extrude(height = nozzle_h, center=true)
                            polygon(points = [
                                [-nozzle_w/2, -16],
                                [ nozzle_w/2, -16],
                                [ nozzle_w/2 + 5,  24],
                                [-nozzle_w/2 + 5,  24]
                            ]);
            }
        }
        
        // Larger central opening for CD hub + HVAT
        cylinder(d = hv_dia + 8, h = total_stack_h + 22, center=true, $fn=64);
    }
}

// End clamp plates adapted for CD/DVD central hole
module end_clamp_plate(thickness = 7) {
    difference() {
        cylinder(d = disc_od + 26, h = thickness, center=true, $fn=128);
        
        // Larger central hole for CD/DVD hub
        cylinder(d = 16, h = thickness + 1, center=true, $fn=64);
        
        // Bolt pattern (6x)
        for (i = [0 : 5]) {
            rotate([0, 0, i * 60 + 15])
                translate([disc_od/2 - 9, 0, 0])
                    cylinder(d=4.2, h=thickness+2, center=true, $fn=16);
        }
    }
}

// Central hub designed for standard CD/DVD 15mm hole
module cd_dvd_hub() {
    difference() {
        union() {
            cylinder(d = 14.8, h = total_stack_h + 30, center=true, $fn=64);  // Fits inside 15mm hole
            // Flanges
            translate([0,0,-total_stack_h/2 - 6])
                cylinder(d = 22, h = 6, center=true, $fn=64);
            translate([0,0, total_stack_h/2 + 6])
                cylinder(d = 22, h = 6, center=true, $fn=64);
        }
        // Shaft hole (for HVAT shaft)
        cylinder(d = 5.2, h = total_stack_h + 50, center=true, $fn=32);
    }
}

// Simple conical diffuser
module diffuser() {
    translate([0, 0, total_stack_h/2 + 14])
        linear_extrude(height = diffuser_len, scale = diffuser_outlet_dia / hv_dia)
            circle(d = hv_dia + 2, $fn=64);
}

// ==================== USAGE ====================
$fn = 96;

housing();
translate([0,0, total_stack_h/2 + 4]) end_clamp_plate(7);
translate([0,0,-total_stack_h/2 - 4]) end_clamp_plate(7);
cd_dvd_hub();
diffuser();

// Usage notes:
// - Use high-quality blank CD-R or DVD-R for best thickness consistency
// - Clean discs thoroughly with isopropyl alcohol
// - Recommended gap: 1.0 - 1.5mm (thicker discs than HDD platters)
// - The larger diameter gives more flow channels and potentially higher throughput
// - Central hub design accounts for the standard 15mm CD hole
