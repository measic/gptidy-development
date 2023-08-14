matrix_1 = np.array([[1,2,3],[4,5,6]])
print(matrix_1.shape)
matrix_2 = np.array([[1,2,3],[1,2,3], [1,2,3]])
matrix_3 = np.dot(matrix_1,matrix_2)
matrices_1 = [matrix_1, matrix_2, matrix_3]
names_1 = ['matrix_1', 'matrix_2', 'matrix_3']

visulize_multiplication(matrices_1, names_1)