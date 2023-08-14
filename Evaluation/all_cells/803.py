X = np.array([[0, 0],
              [1, 2]])

print(np.linalg.det(X))
print(np.linalg.matrix_rank(X)) 
print(np.linalg.matrix_rank(X.T))