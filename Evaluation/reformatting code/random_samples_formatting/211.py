Sw_inv = np.linalg.inv(Sw)
I = np.matmul(Sw,Sw_inv)

print('Sw:')
Sw

print('Inverted Sw:')
Sw_inv

print('Identity matrix')
I