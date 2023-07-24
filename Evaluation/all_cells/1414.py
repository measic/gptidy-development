#create a matrix of random numbers with 3 rows and 5 columns
#random is submodule of numpy. Here the function gives 15 element vector with values in [0,1]
rows = 3
cols = 5
R = np.random.rand(rows*cols)
print('row vector')
print(R)
#reshape from row vector to 3x5 matrix.Here the 'rows' variable could be replaced by -1 and numpy will calculate it.
R = np.reshape(R, (rows,cols))
print('3x5 matrix')
print(R)
#reshape will error if you input the wrong number of elements to form the matrix you tell it to make.
#R = np.reshape(R, (3,6))
