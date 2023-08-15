### Test test test
# Simulate a single forward pass
X_prior.reset()
X.reset()
Z_prior.reset()
Z.reset()
Y_cond.reset()
Y.reset()

X_prior.send_sp_msg(X)
Z_prior.send_sp_msg(Z)
X.send_sp_msg(Y_cond)
Z.send_sp_msg(Y_cond)
Y_cond.send_sp_msg(Y)

assert np.allclose(X.marginal(), [0.95, 0.05])
assert np.allclose(Z.marginal(), [0.8, 0.2])
assert np.allclose(Y.marginal(), [0.821024, 0.178976])
