"""
First working orbit
Set: 2026-11-12    Your request: "ok lets find a set of parameters that work"

Result:
Variable mass: r ≈ 12.9 – 16.7, slow wobble (~1 radial cycle per 22 rad of φ).
L1 > L0 and E1 > E0 so r_star ≈ 15 is stable; c=2 keeps m(r) real.
(No Schwarzschild curve yet.)

Paste the three lines below into the params cell (ba21fa11) of galaxy-rotation-orbits.ipynb
(or galaxy_rotation_orbits_sim.py). Equation: your d²r/dφ² form with m(r) = sqrt(c + rs E0²/r - L0²/r²).
"""
# import numpy as np

# params = dict(rs=.1, L0=19.2, E0=10.0, L1=20., E1=11.91, c=2)   # L0,E0: m(r);  L1,E1: geodesic / phidot
# r0, rdot0 = 13.0, .02          # initial r and dr/dtau
# phi0, phi_max = 0.0, 8*np.pi
