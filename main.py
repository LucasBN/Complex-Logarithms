from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np, math, cmath

def complex_log_arg(z):
    return float(np.sin(cmath.polar(np.log(z))[1]))

def complex_log_mod(z):
    return float(np.sin(cmath.polar(np.log(z))[0]))

def complex_log_real(z):
    return float((np.log(z).real))

def complex_log_imag(z):
    return float((np.log(z).imag))

fig = plt.figure()

xs = np.arange(-3, 3, 0.125)
ys = np.arange(-3, 3, 0.125)

xs, ys = np.meshgrid(xs, ys)
zs = xs*0

xn, yn = xs.shape
for xi in range(xn):
    for yi in range(yn):
        try:
            z = complex(xs[xi,yi], ys[xi,yi])
            zs[xi,yi] = complex_log_real(z)
        except (ZeroDivisionError):
            pass

ax = plt.axes(projection='3d')
ax.plot_surface(xs, ys, zs, rstride=2, cstride=2, cmap='rainbow', edgecolor='none')

plt.show()
