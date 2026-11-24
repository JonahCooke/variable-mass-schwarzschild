"""
Comet-like orbit (very elliptic, closed)
Set: 2026-11-12    Your request: "make the orbits very elliptic like a comet"

Result:
Variable mass: r ≈ 1000 – 14,900, ratio ~15 (e ≈ 0.87). Egg shape with a dimple at closest approach.
c was tuned so the orbit CLOSES: zero precession by construction.
(No Schwarzschild curve yet.)

Paste the three lines below into the params cell (ba21fa11) of galaxy-rotation-orbits.ipynb
(or galaxy_rotation_orbits_sim.py). Equation: your d²r/dφ² form with m(r) = sqrt(c + rs E0²/r - L0²/r²).
"""
# import numpy as np

# params = dict(rs=.1, L0=19.2, E0=10.0, L1=38.4, E1=10.109987141435937, c=9.935104)   # L0,E0: m(r);  L1,E1: geodesic / phidot
# r0, rdot0 = 1000.0, 0.0          # initial r and dr/dtau
# phi0, phi_max = 0.0, 6*np.pi
