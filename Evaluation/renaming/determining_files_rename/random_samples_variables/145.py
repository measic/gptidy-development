variable_def = X[:, -1::-1][-1::-1, :]
plt.imshow(variable_def, interpolation='nearest', cmap=plt.cm.gray)