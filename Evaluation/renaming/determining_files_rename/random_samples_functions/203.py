from plots import *

def function_def():
    """Constructing the polynomial basis function expansion of the data,
       and then running least squares regression."""
    degrees = [1, 3, 7, 12]
    num_row = 2
    num_col = 2
    f, axs = plt.subplots(num_row, num_col)
    for ind, degree in enumerate(degrees):
        raise NotImplementedError
        raise NotImplementedError
        print('Processing {i}th experiment, degree={d}, rmse={loss}'.format(i=ind + 1, d=degree, loss=rmse))
        plot_fitted_curve(y, x, weights, degree, axs[ind // num_col][ind % num_col])
    plt.tight_layout()
    plt.savefig('visualize_polynomial_regression')
    plt.show()