"""Pygame animation of the two orbits from galaxy-rotation-orbits.ipynb.

Blue: variable mass geodesic, the notebook's d^2r/dphi^2 expression (with
m -> m(r) and N = 1 - r_s/r). Red: standard Schwarzschild orbit with the same
rs, L1, r0, rdot0 (m = 1), as in the notebook. Both integrated with RK45
directly in phi.

Controls:
    SPACE       pause / resume
    UP / DOWN   speed up / slow down
    + / -       zoom in / out
    R           restart
    ESC / Q     quit
"""


import numpy as np
import sympy as sp
import pygame
from scipy.integrate import RK45


# Parameters and initial conditions (same as the notebook)
# ---------------------------------------------------------------------------
params = dict(rs=10, L0=19.2, E0=10.0, L1=21.428459297547853, E1=10.009041703577916, c=2)   # L0,E0: m(r);  L1,E1: geodesic / phidot
r0, rdot0 = 150.0, .0          # initial r and dr/dtau
phi0, phi_max = 0.0, 10*np.pi
# ---------------------------------------------------------------------------
# Symbolic equation of motion (same as the notebook, cell 11)
# ---------------------------------------------------------------------------
r, rs = sp.symbols('r r_s', positive=True)
E0, L0, E1, L1 = sp.symbols('E_0 L_0 E_1 L_1', positive=True)
c = sp.Symbol('c')
rp, rpp = sp.symbols('rp rpp', real=True)       # dr/dphi, d²r/dphi²

N = 1 - rs/r

# m(r)
m_sol = sp.sqrt(c + rs*E0**2/r - L0**2/r**2)

# d²r/dphi² (same as the notebook), with m -> m_sol and N = 1 - rs/r
rpp_expr = (m_sol*rs/(2*N*r**2) * rp**2
            + m_sol*N*((1 - L0**2/L1**2)*r - rs*(E1**2 - E0**2)*r**2/(2*L1**2)))
sp.pprint(sp.Eq(rpp, rpp_expr))

rpp_func = sp.lambdify((r, rp, rs, L0, E0, L1, E1, c), rpp_expr, 'numpy')
m_func   = sp.lambdify((r, rs, L0, E0, c), m_sol, 'numpy')
# ---------------------------------------------------------------------------

# m(r) is only real where m^2 = c + rs E0^2/r - L0^2/r^2 > 0
m2_0 = params['c'] + params['rs']*params['E0']**2/r0 - params['L0']**2/r0**2
if m2_0 <= 0:
    raise SystemExit(f'm(r0)^2 = {m2_0:.4g} <= 0, so m(r0) is imaginary: choose r0, c, E0, L0 '
                     f'with c*r0^2 + rs*E0^2*r0 > L0^2')

# initial dr/dtau -> dr/dphi:  dr/dphi = -rdot * m r^2 / L1
rp0 = -rdot0 * m_func(r0, params['rs'], params['L0'], params['E0'], params['c']) * r0**2 / params['L1']


def system(phi, y):
    return [y[1], rpp_func(y[0], y[1], params['rs'], params['L0'], params['E0'],
                           params['L1'], params['E1'], params['c'])]


# Standard Schwarzschild orbit with the same rs, L1, r0, rdot0 (m = 1), as in the notebook.
# Binet form u'' + u = rs/(2 L^2) + (3/2) rs u^2 with u = 1/r, rewritten for r(phi):
#   d²r/dphi² = 2 (dr/dphi)^2 / r + r - rs r^2 / (2 L1^2) - 3 rs / 2
rp0_s = -rdot0 * r0**2 / params['L1']          # dr/dphi = -rdot r^2 / L1  (m = 1)


def system_s(phi, y):
    r_, rp_ = y
    return [rp_, 2*rp_**2/r_ + r_ - params['rs']*r_**2/(2*params['L1']**2) - 1.5*params['rs']]


def new_solver(f, y0):
    return RK45(f, phi0, y0, t_bound=phi_max, max_step=0.05, rtol=1e-9, atol=1e-12)


# ---------------------------------------------------------------------------
# Pygame setup
# ---------------------------------------------------------------------------
width, height = 800, 800
center_x = width // 2
center_y = height // 2

BG = (10, 10, 20)
GRID = (40, 40, 60)
BLUE = (80, 160, 255)        # variable mass geodesic
RED = (255, 70, 70)           # Schwarzschild
BLUE_TRAIL = (50, 100, 170)
RED_TRAIL = (170, 50, 50)
HORIZON = (200, 60, 60)
TEXT = (220, 220, 220)

MONITOR = 1  # which display to open on (0 = primary); falls back to 0 if not connected

pygame.init()
monitor = MONITOR if MONITOR < pygame.display.get_num_displays() else 0
screen = pygame.display.set_mode((width, height), display=monitor)
pygame.display.set_caption('r(phi) orbits: variable mass (blue) vs Schwarzschild (red)')
clock = pygame.time.Clock()
font = pygame.font.SysFont('menlo', 16)

# pixels per unit of r; auto-fit so the largest r reached so far fills the window
fit_radius = 0.9 * min(center_x, center_y)
base_scale = fit_radius / abs(r0)
zoom = 1.0  # manual zoom on top of the auto-fit


def to_screen(r_val, phi_val):
    s = base_scale * zoom
    return (center_x + r_val * np.cos(phi_val) * s,
            center_y - r_val * np.sin(phi_val) * s)


def draw_grid():
    s = base_scale * zoom
    # rings at a 1-2-5 step in r so they stay ~40 px apart at any scale
    raw = 40 / s
    mag = 10 ** np.floor(np.log10(raw))
    step = next(k * mag for k in (1, 2, 5, 10) if k * mag >= raw)
    max_r = np.hypot(center_x, center_y) / s
    for ring in np.arange(step, max_r + step, step):
        pygame.draw.circle(screen, GRID, (center_x, center_y), int(ring * s), 1)
    for k in range(8):
        a = k * np.pi / 4
        pygame.draw.line(screen, GRID, (center_x, center_y),
                         (center_x + 2 * width * np.cos(a), center_y - 2 * width * np.sin(a)), 1)
    pygame.draw.circle(screen, HORIZON, (center_x, center_y), max(2, int(params['rs'] * s)))


class Orbit:
    def __init__(self, name, f, y0, body, trail):
        self.name, self.f, self.y0, self.body, self.trail = name, f, y0, body, trail
        self.reset()

    def reset(self):
        self.solver = new_solver(self.f, self.y0)
        self.phis, self.ys = [self.solver.t], [self.solver.y.copy()]
        self.fail_msg = ''
        self.broken = False   # True once this orbit can't continue; the other one keeps going

    @property
    def done(self):
        return self.broken or self.solver.status != 'running'

    def _break(self, msg):
        self.broken, self.fail_msg = True, msg

    def advance(self, phi_target):
        """Step the integrator past phi_target; return (phi, r, dr/dphi) to draw.

        Any failure (solver failure, exception, NaN/inf, r <= 0) stops only this
        orbit, which stays frozen at its last good point.
        """
        sv = self.solver
        while not self.broken and sv.status == 'running' and sv.t < phi_target:
            try:
                msg = sv.step()
            except Exception as e:
                self._break(f'{type(e).__name__}: {e}')
                break
            if sv.status == 'failed':
                self._break(msg or 'step failed')
                break
            if not np.all(np.isfinite(sv.y)):
                self._break(f'non-finite state at phi = {sv.t:.4f}')
                break
            if sv.y[0] <= 0:
                self._break(f'r <= 0 at phi = {sv.t:.4f}')
                break
            self.phis.append(sv.t)
            self.ys.append(sv.y.copy())
        # interpolate inside the last RK45 step (only while the orbit is healthy)
        if (not self.broken and sv.step_size is not None and sv.t_old is not None
                and sv.t_old <= phi_target <= sv.t):
            try:
                r_now, rp_now = sv.dense_output()(phi_target)
                if np.isfinite(r_now) and np.isfinite(rp_now):
                    return phi_target, r_now, rp_now
            except Exception:
                pass
        r_now, rp_now = self.ys[-1]
        return min(phi_target, self.phis[-1]), r_now, rp_now

    def status_line(self, phi_now):
        if self.broken:
            return f'{self.name}: stopped ({self.fail_msg})'
        if self.solver.status == 'finished' and phi_now >= phi_max:
            return f'{self.name}: finished'
        return None


orbits = [
    Orbit('variable mass', system, [r0, rp0], BLUE, BLUE_TRAIL),
    Orbit('Schwarzschild', system_s, [r0, rp0_s], RED, RED_TRAIL),
]


def reset():
    global base_scale, r_max
    for o in orbits:
        o.reset()
    r_max = abs(r0)
    base_scale = fit_radius / r_max
    return phi0


phi_now = reset()
speed = 1.0  # radians of phi per second
paused = False
running = True

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_ESCAPE, pygame.K_q):
                running = False
            elif event.key == pygame.K_SPACE:
                paused = not paused
            elif event.key == pygame.K_UP:
                speed *= 1.5
            elif event.key == pygame.K_DOWN:
                speed /= 1.5
            elif event.key in (pygame.K_EQUALS, pygame.K_PLUS, pygame.K_KP_PLUS):
                zoom *= 1.25
            elif event.key in (pygame.K_MINUS, pygame.K_KP_MINUS):
                zoom /= 1.25
            elif event.key == pygame.K_r:
                phi_now = reset()

    if not paused:
        phi_now = min(phi_now + speed * dt, phi_max)

    # Advance both integrators to the displayed phi (each stops on its own if it fails)
    states = [o.advance(phi_now) for o in orbits]

    # Auto-scale so the largest r reached so far fits the window
    for _, r_now, _ in states:
        if np.isfinite(r_now):
            r_max = max(r_max, abs(r_now))
    base_scale = fit_radius / max(r_max, 1e-12)

    # Draw
    screen.fill(BG)
    draw_grid()

    for o, (phi_o, r_now, _) in zip(orbits, states):
        trail = [to_screen(y[0], t) for t, y in zip(o.phis, o.ys) if t <= phi_o]
        trail.append(to_screen(r_now, phi_o))
        if len(trail) > 1:
            pygame.draw.aalines(screen, o.trail, False, trail)
    for o, (phi_o, r_now, _) in zip(orbits, states):
        px, py = to_screen(r_now, phi_o)
        pygame.draw.circle(screen, o.body, (int(px), int(py)), 6)

    hud = [(f'phi       = {phi_now:7.3f} / {phi_max:.3f}', TEXT)]
    for o, (_, r_now, rp_now) in zip(orbits, states):
        hud.append((f'{o.name:<14} r = {r_now:10.4f}   dr/dphi = {rp_now:10.4f}', o.body))
    hud.append((f'speed {speed:.2f}x   zoom {zoom:.2f}x' + ('   [paused]' if paused else ''), TEXT))
    hud.append(('  '.join(f'{k}={v}' for k, v in params.items()), TEXT))
    for o in orbits:
        msg = o.status_line(phi_now)
        if msg:
            hud.append((msg, o.body))
    if all(o.done for o in orbits) and (phi_now >= phi_max or all(o.broken for o in orbits)):
        hud.append(('press R to restart', TEXT))
    for i, (line, col) in enumerate(hud):
        screen.blit(font.render(line, True, col), (10, 10 + 20 * i))

    pygame.display.flip()

pygame.quit()
