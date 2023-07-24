ts = t.reshape(-1,1)

# calculate equation for decision boundary
# w.T *x + b = 0
w = np.sum(a * ts * X, axis=0)

Ns = np.sum(cond)
atK = (a * ts * computeK(X))
sum_atK = np.sum(atK[cond], axis=0)
b = 1/Ns * np.sum((t - sum_atK)[cond])

# translate into x2 = slope * x1 + intercept
slope = -w[0] / w[1]
intercept = -b / w[1]
incept_m = [ -(b+1) / w[1], -(b-1) / w[1] ]

# plot decision boundary with marign
xs = np.array([min(X[:,0]), max(X[:,0])])
plt.plot(xs, slope*xs + intercept, color='black')
plt.plot(xs, slope*xs + incept_m[0], color='grey', linestyle='--')
plt.plot(xs, slope*xs + incept_m[1], color='grey', linestyle='--')
plt.fill_between(xs, slope*xs + incept_m[0], slope*xs + incept_m[1], color=(1.0,0.0,0.0,0.3))

# plot data points with support vectors
plt.scatter(X[(t==-1),0], X[(t==-1),1], color='blue')
plt.scatter(X[(t==1),0], X[(t==1),1], color='green')
plt.scatter(X[cond,0], X[cond,1], color='red', marker='x', s=100)
plt.ylim(min(X[:,1]) - 0.5, max(X[:,1] + 0.5))
plt.title("Decision Boundery")
plt.show()
