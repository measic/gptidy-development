def sgd_iter(x_train, t_train, W, b):
    indices = np.arange(len(x_train))
    np.random.shuffle(indices)
    lr = 0.0001
    logp = np.zeros(len(x_train))
    for i in indices:
        variable_def = x_train[i:i + 1]
        t = t_train[i]
        logp[i], grad_w, grad_b = logreg_gradient(variable_def, t, W, b)
        W = W + lr * grad_w
        b = b + lr * grad_b
    logp_train = logp.mean()
    return (logp_train, W, b)