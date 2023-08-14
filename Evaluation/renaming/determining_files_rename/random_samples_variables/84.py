def sgd_iter(x_train, t_train, W, b):
    variable_def = np.arange(len(x_train))
    np.random.shuffle(variable_def)
    lr = 0.0001
    logp = np.zeros(len(x_train))
    for i in variable_def:
        x = x_train[i:i + 1]
        t = t_train[i]
        logp[i], grad_w, grad_b = logreg_gradient(x, t, W, b)
        W = W + lr * grad_w
        b = b + lr * grad_b
    logp_train = logp.mean()
    return (logp_train, W, b)