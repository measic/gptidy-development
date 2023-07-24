x3 = 26.9
y3 = 55.7
z3 = 'Third record.'
zz3 = ['an', 'example','list']
data3 = np.array([13,15,17,25.7,34.6,88])
datalist = []
data_enc = list(np.array(data,dtype=float))
data2_enc = list(np.array(data2,dtype=float))
data3_enc = list(data3)
datalist.append({'x':x, 'y':y, 'z':z, 'data':data_enc})
datalist.append({'x':x2, 'y':y2, 'z':z2, 'data':data2_enc})
datalist.append({'x':x3, 'y':y3, 'z':z3, 'zz':zz3, 'data':data3_enc})
print(datalist)