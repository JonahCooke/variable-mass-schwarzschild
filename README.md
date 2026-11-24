# Variable-mass vs. Schwarzschild orbits

This simulation compares two orbits around the same central body:

- **Variable-mass geodesic** (blue): the test particle's mass changes with radius as
  m(r) = sqrt(c + r_s E0²/r − L0²/r²)
- **Standard Schwarzschild orbit** (red): m = 1, using the same r_s, L1, r0 and ṙ0

Both orbits are integrated directly in φ with SciPy's `RK45`, using the orbit equation for d²r/dφ².

This repo holds the latest version (2026-11-23) of the simulation, split out from a larger dark-matter-alternative research project.

## Contents

| Path | What it is |
|---|---|
| `simulation/galaxy-rotation-orbits.ipynb` | Main notebook: equations, parameters cell, matplotlib plots |
| `simulation/galaxy-rotation-orbits-combined.ipynb` | Combined notebook: the main notebook plus the pygame sim in one file |
| `simulation/galaxy_rotation_orbits_sim.py` | Pygame animation of the two orbits |
| `orbit-parameters/` | 11 saved parameter sets (01–11); set 11 is the current one. See its README |
| `docs/Function Reference.md` | Equation reference: Lagrangian, geodesics, m(r), orbit equation, plus SymPy versions |
| `figures/` | Variable-mass vs. Schwarzschild plots: free fall, precessing orbit, rosette orbit |

## Running it

```bash
pip install numpy sympy scipy matplotlib pygame
python simulation/galaxy_rotation_orbits_sim.py
```

Animation controls: SPACE pauses or resumes, UP/DOWN changes speed, +/- zooms, R restarts, ESC or Q quits.

To try a different orbit, copy the three `params` / `r0` / `phi0` lines from a file in `orbit-parameters/` into the notebook's params cell, or into the matching lines of the sim script.

## Notes

- The parameter set behind each figure isn't recorded.
