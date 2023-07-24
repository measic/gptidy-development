matrix_1 = np.array([[4,2,1,3,5]])
matrix_2 = np.array([[4],[2], [1], [3], [5]])
matrix_3 = np.dot(matrix_1,matrix_2)
matrices_1 = [matrix_1, matrix_2, matrix_3]
names_1 = ['matrix_1', 'matrix_2', 'matrix_3']

visulize_multiplication(matrices_1, names_1)