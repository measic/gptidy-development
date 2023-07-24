C = np.array([C])
print(C)
#transpose to get a column vector from the original row vector.
print('transpose\n',C.transpose())
# Note that you can do this even if C was a row vector instead of a 2D matrix. 
print('A more compact way to transpose where T is an alias to the transpose function')
# The .T is an accessor to the transpose function.
print(C.T)
C = np.array([6,8])
#matrix multiplication. In this case it is same as dot product.
print(np.matmul(C,C.T))