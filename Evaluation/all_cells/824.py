A = np.array([[1, 2, 4],
              [4, 5, 6],
              [7, 8, 9]])
b = np.array([1, 2, 3]) 

## initial guess
x0 = np.array([-0.33, 0.66, 0]) 

print( gauss_seidel(A, b, x0) )