def function_def(loglike_model, prior_transform_model, datafile, priorRange):
    data_file = io.get_data_file_path(datafile)
    data_x, data_xerr, data_y, data_yerr = io.load_data(data_file)
    n = len(priorRange)

    def new_loglike_model(theta):
        return loglike_model(theta, (data_x, data_xerr, data_y, data_yerr))

    def new_prior_transform_model(theta):
        return prior_transform_model(theta, priorRange)
    result = nestle.sample(new_loglike_model, new_prior_transform_model, n)
    print('log evidence')
    print(result.logz)
    print('numerical (sampling) error on logz')
    print(result.logzerr)
    print('array of sample parameters')
    print(result.samples)
    print('array of weights associated with each sample')
    print(result.weights)
    import matplotlib.pyplot as plt
    import corner
    p_fit, cov_fit = nestle.mean_and_cov(result.samples, result.weights)
    plt.figure()
    plt.errorbar(data_x, data_y, yerr=data_yerr, fmt='*')
    plt.xlabel('r (kpc)')
    plt.ylabel('V (km/s)')
    plt.title('Results of using the model to fit the DM rotational velocity distribution')
    xplot = [5 + 5 * i for i in range(40)]
    yplot = [model.model_NFW(xplot[i], p_fit) for i in range(40)]
    plt.plot(xplot, yplot)
    plt.show()
    fig = corner.corner(result.samples, weights=result.weights, labels=['a', 'rho0'], range=[0.99999, 0.99999], bins=30)
    plt.show()
    return result