### Test test test
nodes = [X_prior, X, Z_prior, Z, Y_cond, Y]
for n in nodes:
    n.reset()
    
X_prior.pending.add(X)
Z_prior.pending.add(Z)
Y.pending.add(Y_cond)

sum_product(nodes)
assert np.allclose(Y.marginal(), [0.821024, 0.178976])
