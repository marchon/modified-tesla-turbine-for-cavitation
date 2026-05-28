#!/usr/bin/env python3
"""
Simple physics models for the HDD Platter Precision Flow Conditioner.

- Reynolds number in the inter-platter gaps
- Rough estimate of tangential + radial velocities in the spiral
- Cavitation number at the exit nozzle (for different orifice sizes)

These are order-of-magnitude engineering estimates only.
For serious work, run proper CFD (OpenFOAM) on the generated STLs.

References:
- Classic Tesla turbine boundary layer analysis
- Cavitation number definition (σ)
"""

import math
from dataclasses import dataclass

@dataclass
class PlatterStack:
    num_platters: int = 25
    platter_od_mm: float = 95.0
    gap_mm: float = 1.0
    platter_thick_mm: float = 0.9

    @property
    def active_height_mm(self) -> float:
        return self.num_platters * (self.platter_thick_mm + self.gap_mm) - self.gap_mm

    @property
    def num_gaps(self) -> int:
        return self.num_platters - 1


def reynolds_in_gap(velocity_m_s: float, gap_mm: float = 1.0,
                    fluid: str = "air") -> float:
    """Reynolds number based on gap height as characteristic length."""
    if fluid == "air":
        rho = 1.225   # kg/m3
        mu  = 1.81e-5 # Pa.s
    elif fluid == "water":
        rho = 998.0
        mu  = 0.001
    else:
        raise ValueError("fluid must be 'air' or 'water'")

    gap_m = gap_mm / 1000.0
    return (rho * velocity_m_s * gap_m) / mu


def approximate_exit_velocity(total_flow_lpm: float, stack: PlatterStack,
                              nozzle_count: int = 6, nozzle_angle_deg: float = 10.0) -> float:
    """
    Very rough estimate of average velocity at the nozzle exits.
    Assumes most mass flow is still nearly tangential at nozzle exit.
    """
    # Total gap flow area (very approximate)
    gap_area_m2 = (stack.num_gaps * (stack.platter_od_mm / 1000.0) * (stack.gap_mm / 1000.0))
    flow_m3_s = total_flow_lpm / 60000.0
    # Effective tangential component (cosine of angle from tangent)
    v_tangential = flow_m3_s / (gap_area_m2 * math.cos(math.radians(nozzle_angle_deg)))
    return v_tangential


def cavitation_number(p_static_pa: float, p_vapor_pa: float,
                      velocity_m_s: float, fluid: str = "water") -> float:
    """
    Classic cavitation number σ = (P_static - P_vapor) / (0.5 * ρ * v²)
    Typical inception values for sharp orifices ~1.5–3.0 depending on geometry.
    """
    if fluid == "water":
        rho = 998.0
    else:
        rho = 1.225  # air — not usually used for cavitation calc

    dynamic = 0.5 * rho * velocity_m_s ** 2
    if dynamic < 1e-6:
        return float('inf')
    return (p_static_pa - p_vapor_pa) / dynamic


def main():
    stack = PlatterStack()
    print("HDD Platter Flow Conditioner — Quick Estimates")
    print(f"  {stack.num_platters} platters, {stack.gap_mm} mm gaps → {stack.num_gaps} channels")
    print(f"  Active stack height: {stack.active_height_mm:.1f} mm\n")

    # Example: 15 L/min air through the 6-nozzle stack at 10°
    flow = 15.0  # L/min
    v_exit = approximate_exit_velocity(flow, stack, nozzle_count=6, nozzle_angle_deg=10)
    Re = reynolds_in_gap(v_exit, gap_mm=stack.gap_mm, fluid="air")
    print(f"Air @ {flow} L/min:")
    print(f"  Approx. nozzle exit velocity: {v_exit:.1f} m/s")
    print(f"  Re (gap) ≈ {Re:.0f}  (laminar–transitional for air in 1 mm gap)")

    # Water example at the cavitation nozzle (8 mm orifice, 4 L/min)
    v_jet = 1.8  # m/s example after Venturi acceleration
    sigma = cavitation_number(p_static_pa=101325, p_vapor_pa=2330,
                              velocity_m_s=v_jet, fluid="water")
    print(f"\nWater jet example (v≈{v_jet} m/s):")
    print(f"  Cavitation number σ ≈ {sigma:.2f}")
    print("  (σ < ~2–3 often indicates cavitation is likely with sharp geometry)")


if __name__ == "__main__":
    main()
