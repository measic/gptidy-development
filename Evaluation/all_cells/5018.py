### Test test test: partiallY observed
nodes = [X_prior, X, Z_prior, Z, Y_cond, Y]
for n in nodes:
    n.reset()
    
X_prior.pending.add(X)
Z_prior.pending.add(Z)
Y.pending.add(Y_cond)

Z.set_observed(1)

max_sum(nodes)

assert np.allclose(Y.unnormalized_log_marginal(), [-2.86470401, -2.01740615])
