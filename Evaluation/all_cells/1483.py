from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


def randrange(n, vmin, vmax):
    '''
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    '''
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
#this method requires Axes3D.The first argument determines arrangement if there are multiple subplots.

ax = fig.add_subplot(1, 1, 1, projection='3d') 
# Use this instead to put red markers in separate subplot on left.
# ax = fig.add_subplot(1, 2, 1, projection='3d') 

#number of points to plot for each marker type (100 red and 100 green)
n = 1000

# Set the random x coordinates to be in [-50,50], y in [0, 100].
xlow = -50
xhigh = 50
ylow = 0
yhigh = 100

#set red circle marker and zlow and zhigh.
c, m, zlow, zhigh = ('r', 'o', -50, -25)
#set the x,y coordinates randomly
xs = randrange(n, xlow, xhigh)
ys = randrange(n, ylow, yhigh)
# random values for z coordinate
#zs = randrange(n, zlow, zhigh)
# some function we wish to plot for red circles f(x,y)
zs = np.sqrt(100.0*(np.sqrt(np.absolute(xs * ys))))
# plot the 3D scatter plot of these points.
ax.scatter(xs, ys, zs, c=c, marker=m)

#use this line only if creating separate subplots, and will put green markers in right subplot.
# ax = fig.add_subplot(1, 2, 2, projection='3d') 

#set green X marker and zlow and zhigh.
c, m, zlow, zhigh = ('g', 'x', -30, -5)
xs = randrange(n, xlow, xhigh)
ys = randrange(n, ylow, yhigh)
# random values for z coordinate
#zs = randrange(n, zlow, zhigh)
# some function we wish to plot for green markers f(x,y)
zs = np.sqrt(xs**2 + ys**2)
#zs = 5*np.cos(np.sqrt(xs**2 + ys**2))
ax.scatter(xs, ys, zs, c=c, marker=m)

plt.tight_layout()

plt.savefig('Figure-3Dscatter.png')
plt.show()