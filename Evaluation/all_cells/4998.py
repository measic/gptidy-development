### Test test test
Y_cond.reset()
Y.reset()

# First message from X to Y_cond
X_prior.reset()
X.reset()
X_prior.send_sp_msg(X) # simulating that X received all necessary messages
X.send_sp_msg(Y_cond) 
assert np.allclose(list(Y_cond.in_msgs.values()), [0.95, 0.05])

# Second message from Z to Y_cond
Z_prior.reset()
Z.reset()
Z_prior.send_sp_msg(Z) # simulating that Z received all necessary messages
Z.send_sp_msg(Y_cond)
assert np.allclose(list(Y_cond.in_msgs.values()), [[0.95, 0.05], [0.8, 0.2]])
