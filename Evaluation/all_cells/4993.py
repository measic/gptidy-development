### Test test test
# message from X_prior to X
X_prior.reset()
X.reset()

X_prior.send_sp_msg(X)
assert np.allclose(list(X.in_msgs.values()), [0.95, 0.05])

# message from Z_prior to Z
Z_prior.reset()
Z.reset()

Z_prior.send_sp_msg(Z)
assert np.allclose(list(Z.in_msgs.values()), [0.8, 0.2])

# message from Y_cond to Y
Y_cond.reset()
Y.reset()

Y_cond.receive_msg(X, X_prior.f) # simulating that Y_cond received all necessary messages from X
Y_cond.receive_msg(Z, Z_prior.f) # simulating that Y_cond received all necessary messages from Z
Y_cond.send_sp_msg(Y)
assert np.allclose(list(Y.in_msgs.values()), [0.821024, 0.178976])
