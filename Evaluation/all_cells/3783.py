x = np.array([0,1,2,3,4,5,6,7,8,9])
visulize_array(x, 'array')
sliced_array_1 = x[-4:10]
sliced_array_2 = x[0:-4]
sliced_array_3 = x[-2:1:-2] # [10-2:1:-2] = [8:1:-2]
visulize_array(sliced_array_1, 'sliced_array_1')
visulize_array(sliced_array_2, 'sliced_array_2')
visulize_array(sliced_array_3, 'sliced_array_3')