matrix_1 = np.array([[1,2,3],[4,5,6], [7,8,9]])
matrix_2 = np.array([[1,2,3],[1,2,3], [1,2,3]])
matrix_3 = np.dot(matrix_1,matrix_2)
matrix_4 = np.dot(matrix_2,matrix_1)
matrices_1 = [matrix_1, matrix_2, matrix_3]
names_1 = ['matrix_1', 'matrix_2', 'matrix_3']
matrices_2 = [matrix_2, matrix_1, matrix_4]
names_2 = ['matrix_2', 'matrix_1', 'matrix_4']

visulize_multiplication(matrices_1, names_1)
visulize_multiplication(matrices_2, names_2)