from locale import normalize
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import math 
import numpy as np

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

G = 2/(2*np.pi) 
limit = np.sqrt(2)*2*np.pi/G 

# Make data.
X = np.arange(-limit, limit, 0.5)
Y = np.arange(-limit, limit, 0.5)
X, Y = np.meshgrid(X, Y)
Z = 1 + 0.2*( np.cos(G*X) + np.cos((np.sqrt(3)/2)*G*Y + (G/2)*X) + np.cos((np.sqrt(3)/2)*G*Y - (G/2)*X) ) 

bottom = math.floor((np.min(Z))*10)/10
top = math.ceil((np.max(Z))*10)/10

ax.set_axis_off()
# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.magma,
                       linewidth=0, antialiased=False)


# Customize the z axis.
ax.set_zlim(bottom, top)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
# ax.zaxis.set_major_formatter('{x:.02f}')


Y_Vec = np.arange(-limit, limit, 4)
X_Vec = np.zeros_like(Y_Vec)
X_Vec, Y_Vec = np.meshgrid(X_Vec, Y_Vec)
Z_Vec = 1 + 0.2*( np.cos(G*X_Vec) + np.cos((np.sqrt(3)/2)*G*Y_Vec + (G/2)*X_Vec) + np.cos((np.sqrt(3)/2)*G*Y_Vec - (G/2)*X_Vec) ) 

ups = np.ones_like(X_Vec)
ax.quiver(X_Vec, Y_Vec, Z_Vec, X_Vec, X_Vec, ups, length=0.1, normalize=True,
        arrow_length_ratio = 0.05, color='blue', linewidth = 2)

plt.xlabel('x')

# Add a color bar which maps values to colors.
# fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()