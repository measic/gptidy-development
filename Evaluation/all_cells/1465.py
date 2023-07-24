with open('datalist.txt', 'r') as readfile:
    read_datalist = json.load(readfile)

#some examples of how to use the JSON data that was read from file.
print('read_datalist')
print(read_datalist)
print('zz variable of third record')
print(read_datalist[2]['zz'])
print('numpy array from first record')
print(np.array(read_datalist[0]['data']))
print('standard deviation from array of 2nd record')
print(np.std(read_datalist[1]['data']))
