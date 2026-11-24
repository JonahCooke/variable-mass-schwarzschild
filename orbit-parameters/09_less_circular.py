"""
A bit less circular
Set: 2026-11-13    Your request: "go a bit less circular"

Result:
Only r0 changed from 08.
Variable mass: r ≈ 59.5 – 100 (ratio 1.68), ≈ +37° per orbit.
Schwarzschild:  r ≈ 66.2 – 100 (ratio 1.51), ≈ +96° per orbit.
(r0 = 110 gives blue 49–110, red 62–110.)

Paste the three lines below into the params cell (ba21fa11) of galaxy-rotation-orbits.ipynb
(or galaxy_rotation_orbits_sim.py). Equation: your d²r/dφ² form with m(r) = sqrt(c + rs E0²/r - L0²/r²).
"""
# import numpy as np

# params = dict(rs=10, L0=19.2, E0=10.0, L1=22.188007849009164, E1=10.015446531771273, c=2)   # L0,E0: m(r);  L1,E1: geodesic / phidot
# r0, rdot0 = 100.0, 0.0          # initial r and dr/dtau
# phi0, phi_max = 0.0, 6*np.pi
