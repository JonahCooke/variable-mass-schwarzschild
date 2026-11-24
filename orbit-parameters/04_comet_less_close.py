"""
Comet-like orbit, larger perihelion (closed)
Set: 2026-11-12    Your request: "Lets maybe not go that close"

Result:
Variable mass: r ≈ 3000 – 14,500, ratio ~5. Rounder egg.
c tuned so the orbit closes: zero precession by construction (c=2 instead gives ≈ +68°/orbit).
(No Schwarzschild curve yet.)

Paste the three lines below into the params cell (ba21fa11) of galaxy-rotation-orbits.ipynb
(or galaxy_rotation_orbits_sim.py). Equation: your d²r/dφ² form with m(r) = sqrt(c + rs E0²/r - L0²/r²).
"""
# import numpy as np

# params = dict(rs=.1, L0=19.2, E0=10.0, L1=38.4, E1=10.109987141435937, c=3.968064)   # L0,E0: m(r);  L1,E1: geodesic / phidot
# r0, rdot0 = 3000.0, 0.0          # initial r and dr/dtau
# phi0, phi_max = 0.0, 6*np.pi
