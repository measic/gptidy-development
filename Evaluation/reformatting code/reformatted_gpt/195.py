import numpy as np

A = np.array([[2, 0, -1, 2],
              [4, 2, -1, 4],
              [2, -2, -2, 3],
              [-2, 2, 7, -3]])

# Compute the determinant of a matrix
print(np.linalg.det(A))