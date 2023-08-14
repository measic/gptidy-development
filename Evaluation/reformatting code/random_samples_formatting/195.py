### Test, test, test
# Simulate a single forward pass
X_prior.reset()
X.reset()
Z_prior.reset()
Z.reset()
Y_cond.reset()
Y.reset()

X.set_observed(0)
Z.set_observed(0)

X_prior.send_sp_msg(X)
Z_prior.send_sp_msg(Z)
X.send_sp_msg(Y_cond)
Z.send_sp_msg(Y_cond)
Y_cond.send_sp_msg(Y)

assert np.allclose(Y.marginal(), [9.99900000e-01, 1.00000022e-04])
