variable_def[...] = 0
X = (x - 400) / 30
Y = -(y - 300) / 30
R = np.sqrt(X ** 2 + Y ** 2)
t = np.arctan2(Y, X)
variable_def[R < 5] = (1, 0, 0)
variable_def[(t > 0) & (t < 3.14 / 4)] = (0, 0, 1)
plt.imshow(variable_def, interpolation='bilinear')