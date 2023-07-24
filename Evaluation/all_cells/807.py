A = np.array([[1, 1],
              [2, 1]])
b = np.array([3, 4])

## solve system Ax = b using the inverse
print( np.linalg.inv(A) @ b )