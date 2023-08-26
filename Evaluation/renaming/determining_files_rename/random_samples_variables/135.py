from numpy import ma
U = paf_avg[:, :, 16] * -1
variable_def = paf_avg[:, :, 17]
X, Y = np.meshgrid(np.arange(U.shape[1]), np.arange(U.shape[0]))
M = np.zeros(U.shape, dtype='bool')
M[U ** 2 + variable_def ** 2 < 0.3 * 0.3] = True
U = ma.masked_array(U, mask=M)
variable_def = ma.masked_array(variable_def, mask=M)
plt.figure()
plt.imshow(oriImg[:, :, [2, 1, 0]], alpha=0.5)
s = 5
Q = plt.quiver(X[::s, ::s], Y[::s, ::s], U[::s, ::s], variable_def[::s, ::s], scale=50, headaxislength=4, alpha=0.5, width=0.001, color='r')
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(10, 10)