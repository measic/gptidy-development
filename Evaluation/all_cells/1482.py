from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
# Create the grid of X, Y coordinates that defines the plotting area and coarseness of the plotting grid.
x = np.arange(-6, 6.25, 0.25) #x in [-6,6] with 0.25 step size.
y = np.arange(-5, 5.25, 0.25) #y in [-5,5] with 0.25 step size.
print(x)
#use the 1D x and y vectors to produce two 2D arrays. x is repeated to fill each row of X; y is repeated to fill each column of Y.
#  The 2D X is the grid of x coordinates; the 2D Y is the grid of y coordinates.
X, Y = np.meshgrid(x, y) 

# Create the function you want to plot in the region defined by X,Y
R = np.sqrt(X**2 + Y**2) #radial distance from origin
# The 2D Z is the grid of z (function) values, in this case a 2D cosine wave.
Z = np.cos(R)

# Plot the surface. Different color palettes from the color map (cmap).
surf = ax.plot_surface(X, Y, Z, cmap=cm.winter, linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-1.01, 1.01) #range of z axis
ax.zaxis.set_major_locator(LinearLocator(5)) #set number of z axis labels
ax.zaxis.set_major_formatter(FormatStrFormatter('%.1f')) #string format for z labels

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.savefig('Figure-3Dsurface.png')
plt.show()
