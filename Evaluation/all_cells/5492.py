X, t = create_X_and_t(X1, X2)
a = compute_multipliers(X, t)

cond = (a > 1e-6).reshape(-1)

plt.scatter(X[(t==-1),0], X[(t==-1),1], color='blue')
plt.scatter(X[(t==1),0], X[(t==1),1], color='green')
plt.scatter(X[cond,0], X[cond,1], color='red', marker='x', s=100)
plt.title("Support vectors")
plt.show()
