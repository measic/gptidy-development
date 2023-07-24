import numpy as np

A = np.array([[1, 0, 0],
              [4, 0, 0],
              [2, 3, 5]])

print(np.linalg.det(A))
print(np.linalg.matrix_rank(A)) 