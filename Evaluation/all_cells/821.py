A = np.array([[1, 2, 4],
              [4, 5, 6],
              [7, 8, 9]])
Q = np.diag( np.diag(A) )
print(Q)