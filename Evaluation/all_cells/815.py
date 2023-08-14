import scipy.linalg

%timeit -r1 -n1 scipy.linalg.inv(A) @ b