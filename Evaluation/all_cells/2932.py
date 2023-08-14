grads = [np.array(iteration['grad']) for iteration in itervars]
for grad in grads:
    print('variance:\n', np.var(grad, 0))
    print('covariance:\n', np.cov(grad.T), '\n')