"""
Near-circular, close to the body (~8 rs)
Set: 2026-11-13    Your request: "a more circular orbit that goes semiclose to the body"

Result:
Both set to circle at r = 80, started 10% out.
Variable mass: r ≈ 71.9 – 88, ≈ +34° per orbit.
Schwarzschild:  r ≈ 73.2 – 88, ≈ +96° per orbit.

Paste the three lines below into the params cell (ba21fa11) of galaxy-rotation-orbits.ipynb
(or galaxy_rotation_orbits_sim.py). Equation: your d²r/dφ² form with m(r) = sqrt(c + rs E0²/r - L0²/r²).
"""
# import numpy as np

# params = dict(rs=10, L0=19.2, E0=10.0, L1=22.188007849009164, E1=10.015446531771273, c=2)   # L0,E0: m(r);  L1,E1: geodesic / phidot
# r0, rdot0 = 88.0, 0.0          # initial r and dr/dtau
# phi0, phi_max = 0.0, 6*np.pi
