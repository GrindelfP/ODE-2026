from sympy import *
import numpy as np
import matplotlib.pyplot as plt

t = symbols('t')
x = Function('x')

# Уравнение: x'' + 0.5 x' + 10 = 0, x(0) = 50, x'(0) = 20
s = dsolve(x(t).diff(t, 2) + Rational(1, 2)*x(t).diff(t) + 10, x(t),
           ics={x(0): 50, x(t).diff(t).subs(t, 0): 20})
xt = s.rhs          # высота x(t)
vt = xt.diff(t)     # скорость v(t)
print("x(t) =", xt)
print("v(t) =", vt)

# а) верхняя точка: v = 0
t1 = nsolve(vt, t, 1)
print("а) t =", t1, " x_max =", xt.subs(t, t1))

# б) падение на землю: x = 0
T = nsolve(xt, t, 6)
print("б) t =", T, " v =", vt.subs(t, T))

# в) предельная скорость
print("в) v(inf) =", limit(vt, t, oo))

# г) графики
fx = lambdify(t, xt, 'numpy')
fv = lambdify(t, vt, 'numpy')
tt = np.linspace(0, float(T), 300)
plt.plot(tt, fx(tt), label='x(t), м')
plt.plot(tt, fv(tt), label='v(t), м/с')
plt.xlabel('t, с')
plt.legend()
plt.grid()
plt.show()
