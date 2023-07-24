Bx = np.zeros((10,10))
x = (3,5)
Bx[x[1]-1:x[1]+2,x[0]-1:x[0]+2] = B
plt.plot(3,5,'or')
plt.imshow(Bx,interpolation='nearest',cmap=plt.cm.gray);