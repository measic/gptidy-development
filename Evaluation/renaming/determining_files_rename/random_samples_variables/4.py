X = Variable(name='X', num_states=2)
X_prior = Factor(name='p(X)', f=np.array([0.95, 0.05]), neighbours=[X])
Z = Variable(name='Z', num_states=2)
variable_def = Factor(name='p(Z)', f=np.array([0.8, 0.2]), neighbours=[Z])
Y = Variable(name='Y', num_states=2)
f_Y_cond = [[[0.9999, 0.3], [0.1, 0.01]], [[0.0001, 0.7], [0.9, 0.99]]]
Y_cond = Factor(name='p(Y |X, Z)', f=np.array(f_Y_cond), neighbours=[Y, X, Z])