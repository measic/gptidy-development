def function_def(x_train, t_train, x_valid, t_valid):
    epochs = 10
    lrs = [0.01, 0.001, 0.0001]
    Vs = [[], [], []]
    logp_train = [[], [], []]
    logp_valid = [[], [], []]
    for i, lr in enumerate(lrs):
        W, b, V, a = init_params(28 * 28, 10, 20)
        logp_t = eval_mean_logp(x_train, t_train, W, b, V, a)
        logp_v = eval_mean_logp(x_valid, t_valid, W, b, V, a)
        logp_train[i].append(logp_t)
        logp_valid[i].append(logp_v)
        Vs[i].append(V)
        print(f'lr: {lr}')
        for epoch in range(1, epochs + 1):
            print(f'epoch: {epoch}', end='\r')
            logp_t, W, b, V, a = mlp_sgd_iter(x_train, t_train, W, b, V, a, lr)
            logp_v = eval_mean_logp(x_valid, t_valid, W, b, V, a)
            Vs[i].append(V)
            logp_train[i].append(logp_t)
            logp_valid[i].append(logp_v)
    return (logp_train, logp_valid, Vs)
logp_train, logp_valid, Vs = function_def(x_train, t_train, x_valid, t_valid)