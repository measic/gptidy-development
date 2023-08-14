## check if both give the same result
x = spsolve(A, b)
x_ = np.linalg.solve(A_, b)
np.allclose(x, x_)