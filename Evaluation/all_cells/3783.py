from pprint import pprint

x = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(f'x dimmension: {matrix.ndim}')

# integer and slice indexing
row_1_1d = x[0, :]
row_2_1d = x[1, :] 
row_3_1d = x[2, :]

# slice indexing
row_1_2d = x[0:1, :]
row_2_2d = x[1:2, :] 
row_3_2d = x[2:3, :]

# integer and slice indexing
col_1_1d = x[:, 0]
col_2_1d = x[:, 1]
col_3_1d = x[:, 2]

# slice indexing
col_1_2d = x[:, 0:1]
col_2_2d = x[:, 1:2]
col_3_2d = x[:, 2:3]

visulize_array(x, 'matrix')
print('Integer and slice indexing')
visulize_array(row_2_1d, 'row_2_1d, x[1, :]')
print('Slice indexing')
visulize_array(row_2_2d, 'row_2_2d, x[1:2, :]')
print('Integer and slice indexing')
visulize_array(col_3_1d, 'col_3_1d, x[:, 2]')
print('Slice indexing')
visulize_array(col_3_2d, 'col_3_2d, col_3_2d = x[:, 2:3]')

print('Integer and slice indexing')
print(f'row_1_1d: {row_1_1d}, shape: {row_1_1d.shape}, dim: {row_1_1d.ndim}')
print(f'row_2_1d: {row_2_1d}, shape: {row_2_1d.shape}, dim: {row_2_1d.ndim}')
print(f'row_3_1d: {row_3_1d}, shape: {row_3_1d.shape}, dim: {row_3_1d.ndim}')

print('\nSlice indexing')
print(f'row_1_2d: {row_1_2d}, shape: {row_1_2d.shape}, dim: {row_1_2d.ndim}')
print(f'row_2_2d: {row_2_2d}, shape: {row_2_2d.shape}, dim: {row_2_2d.ndim}')
print(f'row_3_2d: {row_3_2d}, shape: {row_3_2d.shape}, dim: {row_3_2d.ndim}')

print('\nInteger and slice indexing')
print(f'col_1_1d: {col_1_1d}, shape: {col_1_1d.shape}, dim: {col_1_1d.ndim}')
print(f'col_2_1d: {col_2_1d}, shape: {col_2_1d.shape}, dim: {col_2_1d.ndim}')
print(f'col_3_1d: {col_3_1d}, shape: {col_3_1d.shape}, dim: {col_3_1d.ndim}')

print('\nSlice indexing')
print(f'col_1_r2:\n {col_1_2d}, shape: {col_1_2d.shape}, dim: {col_1_2d.ndim}')
print(f'col_2_r2:\n {col_2_2d}, shape: {col_2_2d.shape}, dim: {col_2_2d.ndim}')
print(f'col_3_r2:\n {col_3_2d}, shape: {col_3_2d.shape}, dim: {col_3_2d.ndim}')