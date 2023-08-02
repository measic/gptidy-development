img[...] = 0
X = (x - 400) / 30
variable_def = -(y - 300) / 30
R = np.sqrt(X ** 2 + variable_def ** 2)
t = np.arctan2(variable_def, X)
img[R < 5] = (1, 0, 0)
img[(t > 0) & (t < 3.14 / 4)] = (0, 0, 1)
plt.imshow(img, interpolation='bilinear')