### Test test test: unobserved
nodes = [X_prior, X, Z_prior, Z, Y_cond, Y]
for n in nodes:
    n.reset()
    
X_prior.pending.add(X)
Z_prior.pending.add(Z)
Y.pending.add(Y_cond)

max_sum(nodes)

assert np.allclose(Y.unnormalized_log_marginal(), [-0.27453685, -2.01740615] )
