"""
Distant orbit (~1e5 rs)
Set: 2026-11-12    Your request: "an orbit that is very distant from the body being orbited"

Result:
Variable mass: r ≈ 9000 – 10,900. r_star = 1e4 (E1 = sqrt(E0² + 2(L1²-L0²)/(rs r_star))).
Same shape as 01, just scaled up.
(No Schwarzschild curve yet.)

Paste the three lines below into the params cell (ba21fa11) of galaxy-rotation-orbits.ipynb
(or galaxy_rotation_orbits_sim.py). Equation: your d²r/dφ² form with m(r) = sqrt(c + rs E0²/r - L0²/r²).
"""
# import numpy as np

# params = dict(rs=.1, L0=19.2, E0=10.0, L1=20., E1=10.003135508429345, c=2)   # L0,E0: m(r);  L1,E1: geodesic / phidot
# r0, rdot0 = 9000.0, 0.0          # initial r and dr/dtau
# phi0, phi_max = 0.0, 8*np.pi
