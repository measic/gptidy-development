import numpy as np


def nCr(n, r):
    return np.math.factorial(n) // (np.math.factorial(r) * np.math.factorial(n - r))