"""
Higher eccentricity
Set: 2026-11-13    Your request: "i want something with a higher eccentricity  /  yes"

Result:
Only r0 changed from 08.
Variable mass: r ≈ 21.1 – 150, e ≈ 0.75, ≈ +29° per orbit.
Schwarzschild:  r ≈ 52.8 – 150, e ≈ 0.48, ≈ +100° per orbit.
Other r0 checked: 130 (your value) blue e≈0.62 +45°, red e≈0.39 +98°;
180 blue e≈0.83 −9°; 220 blue e≈0.87 −48°.

Paste the three lines below into the params cell (ba21fa11) of galaxy-rotation-orbits.ipynb
(or galaxy_rotation_orbits_sim.py). Equation: your d²r/dφ² form with m(r) = sqrt(c + rs E0²/r - L0²/r²).
"""
# import numpy as np

# params = dict(rs=10, L0=19.2, E0=10.0, L1=22.188007849009164, E1=10.015446531771273, c=2)   # L0,E0: m(r);  L1,E1: geodesic / phidot
# r0, rdot0 = 150.0, 0.0          # initial r and dr/dtau
# phi0, phi_max = 0.0, 6*np.pi
