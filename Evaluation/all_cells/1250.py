array = []
for i in x_ax:
    for j in y_ax:
        result = qda([i, j])
        if abs(result - 0) < 0.01:
            array.append([i,j])
#             print(result)

array = np.array(array)
a1 = array[:,0]
a2 = array[:,1]
