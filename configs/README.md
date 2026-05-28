# Example Configuration Folders

This directory contains ready-to-use example parameter sets for different experimental goals.

Each subfolder contains:
- A modified version of the main OpenSCAD file with the key parameters changed
- A short README explaining the intent and expected behavior

## Available Configurations

- `aggressive_cavitation/` — Maximize bubble collapse intensity
- `gentle_high_throughput/` — Move lots of fluid with milder conditions
- `maximum_uniformity/` — Best possible flow conditioning quality
- `rapid_prototyping_cd_dvd/` — Fast iteration using cheap CD/DVD discs

## How to Use

1. Copy the `.scad` file from the desired config folder into your working `scad/` directory (or use it as a reference while editing the main file).
2. Adjust the cavitation nozzle orifice size in your usage as recommended in the config README.
3. Print using the calibration pieces first to validate your printer can hit the required tolerances for that config.
4. Compare results against the baseline default configuration.

These are starting points — feel free to mix and match ideas from different configs.
