n = 5
A = np.array([i**j for i in range(1,n+1) for j in range(0, n)] )
A.shape = (n, n)
print(A)