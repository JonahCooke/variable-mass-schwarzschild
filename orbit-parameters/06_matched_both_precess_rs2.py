"""
Both orbits precess, same size (rs = 2)
Set: 2026-11-13    Your request: "chose parameters where they both precess and are roughly the same size"

Result:
Variable mass: r ≈ 26.6 – 52, ≈ +51° per orbit.
Schwarzschild:  r ≈ 28.3 – 52, ≈ +34° per orbit.
E0 tunes precession (3 → +173°, 8 → −36°); keep E1² = E0² + 0.75 for the same size.
m(r) ≈ 0.98 – 1.37 vs M = 1, so M >> m(r) is not met.

Paste the three lines below into the params cell (ba21fa11) of galaxy-rotation-orbits.ipynb
(or galaxy_rotation_orbits_sim.py). Equation: your d²r/dφ² form with m(r) = sqrt(c + rs E0²/r - L0²/r²).
"""
# import numpy as np

# params = dict(rs=2.0, L0=np.sqrt(10), E0=5.0, L1=np.sqrt(40), E1=np.sqrt(25.75), c=1e-6)   # L0,E0: m(r);  L1,E1: geodesic / phidot
# r0, rdot0 = 52.0, 0.0          # initial r and dr/dtau
# phi0, phi_max = 0.0, 20*np.pi
