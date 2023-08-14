def sgd_iter(x_train, t_train, W, b):
    indices = np.arange(len(x_train))
    np.random.shuffle(indices)
    lr = 0.0001
    logp = np.zeros(len(x_train))
    for i in indices:
        x = x_train[i:i + 1]
        t = t_train[i]
        logp[i], grad_w, grad_b = logreg_gradient(x, t, W, b)
        W = W + lr * grad_w
        b = b + lr * grad_b
    variable_def = logp.mean()
    return (variable_def, W, b)