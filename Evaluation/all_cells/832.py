A = lil_matrix((1000, 1000))

A.setdiag(np.random.rand(1000))
A[0, :100] = np.random.rand(100)
A[1, 100:200] = A[0, :100]