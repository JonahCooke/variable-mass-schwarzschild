Variable mass Lagrangian:
$$\mathcal{L}=m(r) \sqrt{\left(1-\frac{r_s}{r}\right)\left(t^{\prime}\right)^2-\left(1-\frac{r_s}{r}\right)^{-1}\left(r^{\prime}\right)^2-r^2\left(\phi^{\prime}\right)^2}$$
Geodesics:
$$\begin{aligned} & \frac{\partial m}{\partial r}\left(1-\frac{r_s}{r}-\dot{r}^2\right)=m(r)\left(\ddot{r}+\frac{r_s}{2\left(r-r_s\right) r} \dot{r}^2+\left(r-r_s\right) \dot{\phi}^2-\frac{\left(1-\frac{r_s}{r}\right) r_s}{2 r^2} \dot{t}^2\right) \\ & \frac{\partial m}{\partial r}\left(1-\frac{r_s}{r}-\dot{r}^2\right)=m(r)\left(\ddot{r}+\frac{r_s}{2\left(r-r_s\right) r} \dot{r}^2\right)+\frac{\left(1-\frac{r_s}{r}\right)}{m(r)}\left(\frac{L^2}{r^3}-\frac{r_s E^2}{2 r^2}\right)\end{aligned}$$
Conjugate momentum:
$$P_\phi = L=-m(r)r^2\dot{\phi}\rightarrow\dot{\phi} =  \frac{-L}{m(r)r^2}$$

Circular orbit mass solution:

$$\begin{gathered}N(r)=\left(1-\frac{r_s}{r}\right),\quad\beta(r)=\left(\frac{L^2}{r^3}-\frac{r_s E^2}{r^2}\right)\\ \frac{\partial m}{\partial r}=\frac{1}{m(r)}\left(\frac{L^2}{r^3}-\frac{r_s E^2}{r^2}\right) =\frac{\beta(r)}{m(r)}\\ m(r)=\sqrt{c+\frac{r_s E^2}{r}-\frac{L_0^2}{r^2}}\end{gathered}$$

Radial equation:

$$0=\ddot{r}+\dot{r}^2\left(\frac{r_s}{2N(r) r^2}\right)+\frac{r^3 \dot{r}^2}{L_0^2-r_sr E_0^2 }+\frac{r^3-r^2 r_s}{L_0^2-r_sr E_0^2}\left(\frac{L_1^2-L_0^2}{r^3}-\frac{r_s\left(E_1^2-E_0^2\right)}{r^2}\right)$$

## Orbit equation in $\phi$
 $E_0, L_0$ set $m(r)$; $E_1, L_1$ appear in the geodesic and in $\dot\phi = -L_1/(m r^2)$.

$$\frac{\partial^2 r}{\partial \phi^2}=\frac{m(r)\, r_s}{2 N(r) r^2}\left(\frac{\partial r}{\partial \phi}\right)^2+m(r) N(r)\left(\left(1-\frac{L_0^2}{L_1^2}\right) r-\frac{r_s\left(E_1^2-E_0^2\right) r^2}{2 L_1^2}\right),\quad m(r)=\sqrt{c+\frac{r_sE_0^2}{r}-\frac{L_0^2}{r^2}},\quad N(r)=1-\frac{r_s}{r}$$

Initial condition conversion: $\dfrac{\partial r}{\partial \phi} = -\dot r\,\dfrac{m(r)\,r^2}{L_1}$

## SymPy versions

Setup (run once before using the expressions below):

```python
from sympy import *
r, r_s, E, L, L_0, c = symbols('r r_s E L L_0 c')
E_0, E_1, L_1 = symbols('E_0 E_1 L_1')
tp, rp, phip = symbols('tp rp phip')                      # t', r', φ'
tdot, rdot, rddot, phidot = symbols('tdot rdot rddot phidot')  # ṫ, ṙ, r̈, φ̇
drdphi, d2rdphi2 = symbols('drdphi d2rdphi2')             # dr/dφ, d²r/dφ²
m = Function('m')
```

| Quantity                                 | SymPy |
| ---------------------------------------- | ----- |
| Lagrangian $\mathcal{L}$                 | `m(r)*sqrt((1 - r_s/r)*tp**2 - (1 - r_s/r)**-1*rp**2 - r**2*phip**2)` |
| Geodesic (1)                             | `Eq(Derivative(m(r), r)*(1 - r_s/r - rdot**2), m(r)*(rddot + r_s/(2*(r - r_s)*r)*rdot**2 + (r - r_s)*phidot**2 - (1 - r_s/r)*r_s/(2*r**2)*tdot**2))` |
| Geodesic (2)                             | `Eq(Derivative(m(r), r)*(1 - r_s/r - rdot**2), m(r)*(rddot + r_s/(2*(r - r_s)*r)*rdot**2) + (1 - r_s/r)/m(r)*(L**2/r**3 - r_s*E**2/(2*r**2)))` |
| Conjugate momentum $P_\phi$              | `Eq(L, -m(r)*r**2*phidot)` |
| $\dot\phi$                               | `Eq(phidot, -L/(m(r)*r**2))` |
| $N(r)$                                   | `1 - r_s/r` |
| $\beta(r)$                               | `L**2/r**3 - r_s*E**2/r**2` |
| $\partial m/\partial r$ (circular orbit) | `Eq(Derivative(m(r), r), (L**2/r**3 - r_s*E**2/r**2)/m(r))` |
| $m(r)$ (circular orbit solution)         | `Eq(m(r), sqrt(c + r_s*E**2/r - L_0**2/r**2))` |
| Radial equation                          | `Eq(0, rddot + rdot**2*(r_s/(2*(1 - r_s/r)*r**2)) + r**3*rdot**2/(L_0**2 - r_s*r*E_0**2) + (r**3 - r**2*r_s)/(L_0**2 - r_s*r*E_0**2)*((L_1**2 - L_0**2)/r**3 - r_s*(E_1**2 - E_0**2)/r**2))` |
| $m(r)$ (orbit equation, $E_0, L_0$)      | `Eq(m(r), sqrt(c + r_s*E_0**2/r - L_0**2/r**2))` |
| Orbit equation $\partial^2 r/\partial\phi^2$ | `Eq(d2rdphi2, m(r)*r_s/(2*(1 - r_s/r)*r**2)*drdphi**2 + m(r)*(1 - r_s/r)*((1 - L_0**2/L_1**2)*r - r_s*(E_1**2 - E_0**2)*r**2/(2*L_1**2)))` |
| Initial condition $\partial r/\partial\phi$ | `Eq(drdphi, -rdot*m(r)*r**2/L_1)` |
