from matplotlib.pyplot import *
from numpy import linspace, cos, sin, sqrt, tan, pi, sinh, cosh, tanh
from mpl_toolkits.mplot3d import Axes3D

r = 50
 
t = linspace(-85.0, 85.0, 300)
#x = 5.*cos(2*t)*sqrt(t)
x = r * cos(t) / cosh(0.035 * (t))
#y = 5.*sin(2*t)*sqrt(t)
y = r * sin(t) / cosh(0.035 * (t))
#z = t*5.
z = r * tanh(0.035 * (t))
 
fig = figure(figsize=(4,4))
ax = fig.add_subplot(111,projection='3d')
ax.view_init(30,60)
 
ax.plot(x,y,z)
 
ax.set_xlabel(r'x')
ax.set_ylabel(r'y')
ax.set_zlabel(r'z')

fig.savefig("Test.svg",bbox_inches="tight",\
        pad_inches=.15)

#plt.show()

