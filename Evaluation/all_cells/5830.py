# tranform each class
Y1 = np.matmul(X1,v2)
Y2 = np.matmul(X2,v2)

## show me dont tell me
ax = plt.gca()
ax.hist(Y1,color='blue', alpha=0.5, label='1')
ax.hist(Y2,color='yellow', alpha=0.5, label='2')
plt.legend(loc='upper right')
plt.xlabel('y')

Y = np.matmul(X,v2)