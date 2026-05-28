/*
 * BEARING_HOUSERS.scad
 * Upper and lower bearing housers for the central HVAT rotor (608ZZ bearings)
 * Press-fit tolerance (+0.1 mm interference on bore).
 * Flanged for screwing to top/bottom end plates.
 *
 * =============================================================================
 * 3D PRINTING NOTES (Highest tolerance sensitivity in the project)
 * =============================================================================
 * Material: PETG or ASA. Must hold precise bore for bearings.
 *
 * Critical Settings for Bearing Bore:
 *   - Layer height: 0.15 mm or lower around the bore
 *   - Perimeters: 6+
 *   - Infill: 50%+ near bore
 *   - **Print the bore vertically** if possible (best roundness)
 *   - Do NOT use elephant foot compensation on first layer for this part
 *
 * Tolerance Strategy:
 *   - Target bore: 8.15 - 8.25 mm for standard 608ZZ (8.00 mm OD)
 *   - Test print a small calibration ring first!
 *   - If too tight: lightly sand or ream
 *   - If too loose: print with +0.05-0.08 mm smaller bore and test
 *
 * Recommended: Print upper and lower housers together on same plate
 *              for consistent material behavior.
 * =============================================================================
 *
 * From the May 2026 Grok design conversation.
 */

module bearing_houser(od=24, id=8.2, h=8, flange_d=32) {
    difference() {
        union() {
            // Main cylinder (press fit for bearing)
            cylinder(d=od, h=h, center=true, $fn=64);
            // Mounting flange
            cylinder(d=flange_d, h=3, center=true, $fn=64);
        }
        // Bearing bore (slight interference for press fit)
        cylinder(d=id, h=h+2, center=true, $fn=48);
    }
}

// Upper and lower (lower can be thicker for stability)
translate([0, 0, 0])   bearing_houser(h=8, flange_d=32);   // upper
translate([50, 0, 0]) bearing_houser(h=10, flange_d=32);  // lower (thicker)

// Mounting: screw flanges to top and bottom end plates.
// Add thin PTFE thrust washer between HVAT top and upper bearing if needed.
