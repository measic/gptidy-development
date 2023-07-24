A = np.array([[1.001, 0], [0, 0.5]])
B = np.array([[1.], [1.]])

# for controllability
cont = np.hstack([B, A@B, A@A@B])
assert np.linalg.matrix_rank(cont)==cont.shape[0]