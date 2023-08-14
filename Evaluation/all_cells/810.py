a, b, c, d = 5, 0.4, 0, 0.3

A = np.array([[1, b], [1, -d]])
y = np.array([[a], [c]])

np.linalg.solve(A, y)