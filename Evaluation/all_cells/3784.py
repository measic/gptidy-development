x = np.array([0,1,2,3,4,5,6,7,8,9])
print(f'x dimmension: {x.ndim}')

visulize_array(x, 'x')
visulize_array(x[4:6], 'x[4:6]')
visulize_array(x[4:], 'x[4:]')
visulize_array(x[:4], 'x[:4]')
visulize_array(x[:], 'x[:]')
visulize_array(x[:-1], 'x[:-1]')
x[4:6] = [11,12]