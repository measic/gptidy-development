#create row vector then reshape to be a column vector
C = np.array([4,3,8])
C = C.reshape(-1,1) #-1 indicates number of rows is inferred from specified number of columns (1)
print('C')
print(C)