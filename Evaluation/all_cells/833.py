## solving the system with A as a standard matrix
A_ = A.toarray()
%timeit -r1 -n1  np.linalg.solve(A_, b)