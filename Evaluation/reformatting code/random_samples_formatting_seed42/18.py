### Test test test
# Simulate a single forward pass
X_prior.reset()
X.reset()
Z_prior.reset()
Z.reset()
Y_cond.reset()
Y.reset()

X_prior.send_ms_msg(X)
Z_prior.send_ms_msg(Z)
X.send_ms_msg(Y_cond)
Z.send_ms_msg(Y_cond)
Y_cond.send_ms_msg(Y)

assert np.allclose(X.unnormalized_log_marginal(), [-0.05129329, -2.99573227])
assert np.allclose(Z.unnormalized_log_marginal(), [-0.22314355, -1.60943791])
assert np.allclose(Y.unnormalized_log_marginal(), [-0.27453685, -2.01740615])
