X_prior.reset()
X.reset()
Z_prior.reset()
Z.reset()
Y_cond.reset()
Y.reset()

# Forward pass
X_prior.send_sp_msg(X)
Z_prior.send_sp_msg(Z)
X.send_sp_msg(Y_cond)
Z.send_sp_msg(Y_cond)
Y_cond.send_sp_msg(Y)
assert np.allclose(list(Y.in_msgs.values()), [0.821024, 0.178976])

# Backward pass
Y.send_sp_msg(Y_cond)
Y_cond.send_sp_msg(X)
Y_cond.send_sp_msg(Z)
X.send_sp_msg(X_prior)
Z.send_sp_msg(Z_prior)
assert np.allclose(list(X.in_msgs.values()), [[0.95, 0.05],[1., 1.]])
assert np.allclose(list(Z.in_msgs.values()), [[0.8, 0.2],[1., 1.]])
