"""
Precessing rosette, M >> sqrt(c)
Set: 2026-11-12    Your request: "no I said it backwards M>>m  /  write it over my edits"

Result:
Variable mass: r ≈ 3000 – 15,500, ≈ +20° per orbit. M = 1, sqrt(c) = 1e-3.
Schwarzschild (added after, same params): r ≈ 975 – 3000, ≈ +0.74° per orbit (looks static).
Note: m(r) along the orbit is 1.1 – 2.6, so M >> m(r) is NOT actually met.

Paste the three lines below into the params cell (ba21fa11) of galaxy-rotation-orbits.ipynb
(or galaxy_rotation_orbits_sim.py). Equation: your d²r/dφ² form with m(r) = sqrt(c + rs E0²/r - L0²/r²).
"""
# import numpy as np

# params = dict(rs=2.0, L0=19.2, E0=100.0, L1=38.4, E1=100.0005529585, c=1e-6)   # L0,E0: m(r);  L1,E1: geodesic / phidot
# r0, rdot0 = 3000.0, 0.0          # initial r and dr/dtau
# phi0, phi_max = 0.0, 20*np.pi
