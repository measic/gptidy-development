### Test test test
X_prior.reset()
X.reset()
assert X_prior.pending == set()

X_prior.pending.add(X)
assert str(list(X_prior.pending)[0]) == X.name

X_prior.send_sp_msg(X)
assert X_prior.pending == set()
