variable_def[...] = 0
X = (x - 400) / 30
Y = -(y - 300) / 30
heart = X ** 2 + (Y - 2 * (X ** 2 + np.abs(X) - 6) / (3 * (X ** 2 + np.abs(X) + 2))) ** 2 < 36
variable_def[heart] = (1, 0, 0)
plt.imshow(variable_def, interpolation='bilinear')