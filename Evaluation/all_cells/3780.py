
x = np.array([0,1,2,3,4,5,6,7,8,9])
visulize_array(x, 'array')
start_index = 1
stop_index = 10
step = 2
sliced_array = x[start_index:stop_index:step]
visulize_array(sliced_array, 'sliced_array')