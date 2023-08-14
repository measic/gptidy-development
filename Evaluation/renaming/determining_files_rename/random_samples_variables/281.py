def test_sgd(x_train, t_train, x_valid, t_valid, w, b):
    Lts = []
    Lvs = []
    epsilon = 0.01
    while (len(Lts) < 2 or abs(Lts[-1] - Lts[-2]) > epsilon) and len(Lts) < 25:
        variable_def, w, b = sgd_iter(x_train, t_train, w, b)
        logp = []
        for x, t in zip(x_valid, t_valid):
            _, _, logp_valid = logprob(x, w, b)
            logp.append(logp_valid[t])
        L_valid = np.array(logp).mean()
        Lts.append(variable_def)
        Lvs.append(L_valid)
    x = np.arange(len(Lts))
    plt.plot(x, Lts, label='L_train')
    plt.plot(x, Lvs, label='L_validation')
    plt.legend()
    plt.show()
    return (w, b)
np.random.seed(1243)
w = np.zeros((28 * 28, 10))
b = np.zeros(10)
w, b = test_sgd(x_train, t_train, x_valid, t_valid, w, b)