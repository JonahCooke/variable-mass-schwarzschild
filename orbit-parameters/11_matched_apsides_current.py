"""
Matched orbits: same closest/farthest points (CURRENT)
Set: 2026-11-13    Your request: "lets pick one where the orbits are closer"

Result:
Both orbits: r ≈ 46.0 – 150, e ≈ 0.53, ≈ +116.5° per orbit; apsides at almost the same angles
(closest 238° vs 241°, farthest 477° vs 476°), but the paths between differ (r'² term).
This is what is in galaxy-rotation-orbits.ipynb and galaxy_rotation_orbits_sim.py now (sim script set 2026-11-14).

Paste the three lines below into the params cell (ba21fa11) of galaxy-rotation-orbits.ipynb
(or galaxy_rotation_orbits_sim.py). Equation: your d²r/dφ² form with m(r) = sqrt(c + rs E0²/r - L0²/r²).
"""
# import numpy as np

# params = dict(rs=10, L0=19.2, E0=10.0, L1=21.428459297547853, E1=10.009041703577916, c=2)   # L0,E0: m(r);  L1,E1: geodesic / phidot
# r0, rdot0 = 150.0, .0          # initial r and dr/dtau
# phi0, phi_max = 0.0, 6*np.pi
