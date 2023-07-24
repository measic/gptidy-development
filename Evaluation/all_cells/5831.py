## plot the input data and the new set of axes
ax = plt.gca()
plot_gmm(initial_guess, X, label=labels, ax=ax)

p = -6.0*v2
v2l = 10.0*v2 

ax.quiver(p[0],p[1],v2l[0],v2l[1], units = 'xy',scale=1)
ax.text(v2l[0] + p[0], v2l[1] + p[1], 'y')
ax.grid()