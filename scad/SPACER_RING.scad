/*
 * Precise spacer rings for HDD platter stack
 * 1.0 mm default (24 required for 25 platters @ 1 mm gap)
 * Lightening holes for material savings + easier printing
 * Parametric — change thickness or OD for your build
 *
 * =============================================================================
 * 3D PRINTING NOTES (Highest precision requirement)
 * =============================================================================
 * THIS IS ONE OF THE MOST CRITICAL PARTS FOR PERFORMANCE.
 * Gap consistency directly affects flow quality.
 *
 * Material: PETG preferred. Must be dimensionally stable.
 *
 * Settings for Precision:
 *   - Layer height: 0.12 - 0.15 mm (critical for thickness accuracy)
 *   - First layer height: 0.2 mm max
 *   - Perimeters: 4
 *   - Infill: 100% or very high (these are thin)
 *   - **Print all 24+ at once** on the same plate for consistency
 *   - Use same filament spool for the entire batch
 *
 * Tolerance Target: ±0.03 to ±0.05 mm thickness
 * - Measure a sample with digital calipers after printing
 * - If consistently thick: adjust flow rate down 2-4%
 * - If elephant's foot present: increase first layer height or use compensation
 *
 * Print 26-28 pieces. You will want spares.
 * =============================================================================
 */

module platter_spacer(od=95, thickness=1.0, id=30) {
    difference() {
        // CRITICAL DIMENSION: Thickness must be consistent across all spacers
        // Target tolerance: ±0.05mm (ideally ±0.03mm)
        // This directly controls gap size between platters.
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
