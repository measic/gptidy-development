### Test, test, test
X_prior.reset()
X.reset()
Y_cond.reset()

X_prior.send_sp_msg(X)
X.set_observed(0)
X.send_sp_msg(Y_cond)
assert np.allclose(list(Y_cond.in_msgs.values()), [9.5e-01, 5.0e-12])
