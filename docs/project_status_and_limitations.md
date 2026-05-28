# Project Status & Limitations

**READ THIS PAGE BEFORE USING, BUILDING, OR CITING ANYTHING FROM THIS PROJECT.**

This is not a finished scientific instrument.  
This is not a validated testbed.  
The performance models are not predictions.

If you are looking for proven hardware with reliable data, **this is not it yet**. 

If you proceed anyway, you do so with full knowledge that almost everything performance-related here is speculative.

## Current Maturity Level

**Maturity Matrix** (as of May 2026):

| Area                              | Maturity Level       | Can You Trust It? | Notes |
|-----------------------------------|----------------------|-------------------|-------|
| Physical CAD & BOM                | Good                 | Yes (for building) | Designs are buildable on paper |
| 3D Printing Documentation         | Good                 | Mostly            | Practical guidance exists |
| Assembly Instructions             | Good                 | Mostly            | Jigs and procedures are detailed |
| Engineering Drawings & Visuals    | High                 | For visualization | Pretty pictures, many are generated |
| Performance Graphs & Models       | **Very Low**         | **No**            | Simplified speculation only |
| Experimental Validation           | **None**             | **No**            | Author has not built or tested anything |
| Scientific Usefulness as Testbed  | **Unknown**          | **No**            | Unproven. This is the entire open question |
| Reputation as "Consistent Testbed"| **Does Not Exist**   | **Do not claim**  | No data exists to support this yet |

**Bottom line**: You can build something that looks like the drawings. Whether it actually delivers better, more consistent cavitation conditions than simpler methods is currently unknown.

## Critical Disclaimers (Read These Carefully)

### 1. Performance Graphs and Models — These Are Speculation
**All** performance curves, "what-if" scenarios, bubble size estimates, swirl reduction plots, hybrid synergy diagrams, pressure drop estimates, etc. are:

- Crude, back-of-the-envelope analytical guesses.
- **Not** CFD.
- **Not** based on any physical experiments by the author.
- **Not** validated against real data.

They were created to explore ideas and generate hypotheses. They should **not** be treated as reliable indicators of what will actually happen when you build the device.

**Do not cite these graphs in papers. Do not present them as evidence. Doing so would be misleading.**

The author makes no claim that these models accurately predict real-world behavior. They are educational toys, not scientific tools.

### 2. No Experimental Data From the Author
**The author has not built or tested this device.**

As of now, there are zero physical prototypes built by George Lambert, zero measurements, and zero data.

Everything written about how the device "will" or "is expected to" perform is either:
- Theoretical reasoning, or
- Output from very simple models that the author himself does not trust as accurate.

If you see anyone (including the author in the future) claiming specific performance numbers from this project without showing real build data, treat those claims with extreme skepticism.

### 3. This Is an Open Design Exploration
This project should be viewed as:

- An open hardware starting point for precision flow conditioning in cavitation experiments.
- A well-documented set of tools and parametric designs.
- An invitation for the community (especially the MFMP and broader cavitation research community) to build, test, improve, and validate.

It is **not** a finished, validated scientific instrument.

## What This Project Actually Provides

- Complete, parametric, open-source CAD (OpenSCAD) for two variants (HDD platters and CD/DVD discs).
- Extensive documentation on design rationale, assembly, and 3D printing.
- Useful tooling for generating engineering drawings, DXF fabrication files, flow visualizations, and calibration aids.
- A framework for systematic experimentation (calibration pieces, example configurations, etc.).

## What This Project Does NOT Provide (And May Never Provide)

- Any validated performance data
- CFD validation of the designs
- Experimental protocols that have been shown to work
- Peer-reviewed findings
- Independently replicated results
- A "consistent testbed" that has actually been proven consistent

**There is currently no evidence that this device works better than simpler injection methods.** Any such claim is currently speculation.

## Recommendation for Users and Replicators (Blunt Version)

If you build this device:

- Do **not** assume it will perform better than a simple orifice or bubbler. It might. It might not. Nobody knows yet.
- Do **not** cite the graphs in this project as justification for your results.
- Do **not** present this design as a "proven consistent testbed." It is not proven.
- Document everything honestly, including failures and null results.
- If your results look exciting, be extremely cautious about causation vs correlation until you have rigorous controls and independent replication.

Publishing exciting results based on unvalidated hardware from this project would be premature and potentially damaging to the credibility of the field.

## How to Cite This Project (Do It Honestly)

When referring to this work, use language similar to one of the following:

**Recommended (accurate):**
> "The Precision Flow Conditioner is an open hardware design exploration by George Lambert (2026). The physical designs are available for replication, but as of publication, no experimental validation or performance data from the author exists. All performance estimates in the documentation are simplified conceptual models only."

**Avoid** (misleading):
- Claiming this provides a "consistent testbed"
- Citing the performance graphs as evidence
- Presenting the device as proven superior to simpler injection methods

Misrepresenting the current state of this project in papers or presentations would be scientifically irresponsible.

## Project Philosophy

This project was created in the spirit of open, low-cost, high-documentation experimental work championed by Bob Greenyer and the MFMP community. The goal is to lower the barrier to high-quality, repeatable cavitation experiments — not to make premature claims.

Transparency about limitations is part of that philosophy.

---

**Last updated**: May 2026

If you have built this device or have feedback on these limitations, please open an issue or contact the author. Real-world data from builders will be the most valuable contribution to this project.