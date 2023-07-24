# data. Each is a 1D vector with 100 elements.
x = np.linspace(0.0, 4*np.pi,100)
y = np.linspace(0.0, 2*np.pi,100)
m=100
n=1
# print(x)
#repeat x by m times in n columns. Here tile inputs 1D vector 'x' to generate a 2D matrix and repeats that row 100 times in 1 column.
# This tiling is done only to create an image from a row vector but we do need a 2D matrix for imshow()
# therefore result is a 100x100 matrix
X = np.tile(x,(m,n))
# print(X)
Y = np.tile(y,(m,n))
# generate the image 'c' from two 2D matrices (X and Y). The values are 1D (one channel) and converted to colors by a 1D color scale. (Not RGB)
c = np.sin(X) + np.cos(Y)
# extent is needed in order to get correct x,y values for the axes (instead of the matrix indices).
plt.imshow(c, extent=(np.amin(x), np.amax(x), np.amin(y), np.amax(y)), aspect = 'auto')
# colorbar is the color legend.
plt.colorbar()
plt.savefig('image.png')
