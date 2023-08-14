N_test = 100
sigma = 0.2
beta = 1.0 / pow(sigma, 2)
x_test = np.linspace(-1, 1, N_test)
y_test = true_mean_function(x_test)

thetas = np.array([(1., 4., 0., 0.),
                   (9., 4., 0., 0.),
                   (1., 64., 0., 0.),
                   (1., 0.25, 0., 0.),
                   (1., 4., 10., 0.),
                   (1., 4., 0., 5.)])
n_train = 2
x_train = np.random.uniform(-1, 1, n_train)
y_train = true_mean_function(x_train)
t_train = add_noise(y_train, sigma)

for idx, theta in enumerate(thetas):
    mean_test, covar_test, _ = gp_predictive_distribution(x_train, t_train, x_test, theta, beta, C=None)
    lp, _, _ = gp_log_likelihood(x_train, t_train, theta, beta, C=None, invC=None)
    plt.subplot(2, 3, idx + 1).title.set_text(f"theta: {theta}, lp = {lp:.2f}")
    gp_plot(x_test, y_test, mean_test, covar_test, x_train, t_train, theta, beta)

plt.suptitle(f"{n_train} data points")
plt.show()