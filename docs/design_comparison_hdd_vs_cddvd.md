# Design Comparison: HDD Platter vs CD/DVD Version

This document compares the two physical implementations of the Precision Flow Conditioner.

## Summary Table

| Aspect                    | HDD Platter Version                  | CD/DVD Version                          | Winner / Notes |
|---------------------------|--------------------------------------|-----------------------------------------|---------------|
| **Disc Diameter**         | 95 mm                               | 120 mm                                 | CD/DVD (more flow area) |
| **Disc Thickness**        | ~0.9 mm                             | ~1.2 mm                                | HDD (tighter gaps possible) |
| **Surface Quality**       | Excellent (mirror polish)           | Good (polycarbonate, varies by brand)  | **HDD clear winner** |
| **Cost / Availability**   | Medium (scrap Enterprise drives)    | Very low (blank or used CDs/DVDs)      | **CD/DVD** |
| **Consistency**           | High (matched platters)             | Medium (brand variation)               | HDD |
| **Central Hole**          | Small + custom                      | Standard 15 mm                         | CD/DVD easier |
| **Max Stack Height**      | Excellent                           | Good                                   | HDD |
| **Best For**              | Highest performance / research      | Prototyping, low budget, education     | Depends on goal |
| **Ease of Sourcing**      | Medium                              | Extremely easy                         | CD/DVD |
| **Repeatability**         | Higher                              | Good (with good blank media)           | HDD |

## Detailed Comparison

### 1. Flow Characteristics
- **HDD Version**: Superior due to mirror-polished surfaces. Creates the cleanest boundary layers and lowest turbulence.
- **CD/DVD Version**: Slightly higher surface roughness. Still very usable, especially with high-quality blank media. May produce marginally more turbulence at high flow rates.

**Recommendation**: Use HDD platters when you need the absolute best data quality. Use CD/DVD for development, teaching, or when budget/sourcing is the constraint.

### 2. Mechanical Construction
- HDD platters are thinner → can fit more channels in the same height.
- CD/DVD discs are thicker and have a large central hole → requires a different hub design (already provided in `cd_dvd_version/`).

### 3. Cost & Accessibility
This is the strongest argument for the CD/DVD version:
- Blank CD-Rs or DVD-Rs can be bought for pennies each.
- Many people already have stacks of old CDs/DVDs.
- No need to hunt for specific Enterprise hard drives.

### 4. Experimental Use Cases

**Choose HDD Platters when**:
- You are doing serious LENR/cavitation research and need maximum repeatability.
- You already have access to matched platters.
- You want the highest possible performance.

**Choose CD/DVD when**:
- You are prototyping or teaching.
- Budget is very limited.
- You want to quickly build multiple units.
- You are testing the overall concept before investing in premium platters.

## Hybrid Recommendation

Many experimenters may want to do this:

1. Build the **CD/DVD version first** for learning, tuning, and initial experiments.
2. Once the experimental protocol is solid, build the **HDD platter version** for high-quality data collection.

The OpenSCAD code is parametric enough that switching between the two is relatively straightforward.

## File Locations

- HDD version: `scad/` (main files)
- CD/DVD version: `scad/cd_dvd_version/`
- Comparison notes are also embedded in the individual CD/DVD SCAD files.

---

**Bottom line**: The HDD version is higher performance. The CD/DVD version is dramatically more accessible. Both are valid and useful.
