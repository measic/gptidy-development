## PCA See no need to use labels
pca = sklearnPCA(n_components=1)

Y = pca.fit_transform(X)

Y.shape

vpca = pca.components_[0]

print('Comparing eigenvectors')
v2
vpca

print('dot product')
vpca.dot(v2.T)

print('Show me dont tell me')
ax = plt.gca()
plot_gmm(initial_guess, X, label=labels, ax=ax)


ax.quiver(0,0,3*v2[0],3*v2[1], units = 'xy',scale=1)
ax.quiver(0,0,3*vpca[0],3*vpca[1], units = 'xy',scale=1)
ax.text(3.1*v2[0], 3.1*v2[1], 'v2')
ax.text(3.1*vpca[0], 3.1*vpca[1], 'vpca')
ax.grid()