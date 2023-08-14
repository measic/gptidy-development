from numpy import ma
variable_def = paf_avg[:, :, 16] * -1
V = paf_avg[:, :, 17]
X, Y = np.meshgrid(np.arange(variable_def.shape[1]), np.arange(variable_def.shape[0]))
M = np.zeros(variable_def.shape, dtype='bool')
M[variable_def ** 2 + V ** 2 < 0.3 * 0.3] = True
variable_def = ma.masked_array(variable_def, mask=M)
V = ma.masked_array(V, mask=M)
plt.figure()
plt.imshow(oriImg[:, :, [2, 1, 0]], alpha=0.5)
s = 5
Q = plt.quiver(X[::s, ::s], Y[::s, ::s], variable_def[::s, ::s], V[::s, ::s], scale=50, headaxislength=4, alpha=0.5, width=0.001, color='r')
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(10, 10)