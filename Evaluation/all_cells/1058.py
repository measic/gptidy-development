reload(util)
reload(test)
sigma_n = 0.1
sigma_f = 1
l = 1
theta = [sigma_f, l, sigma_n]
util.solve_and_visualize(regression_GP, kernel, x, y, theta)