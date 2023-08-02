img[...] = 0
X = (x - 400) / 30
Y = -(y - 300) / 30
R = np.sqrt(X ** 2 + Y ** 2)
variable_def = np.arctan2(Y, X)
img[R < 5] = (1, 0, 0)
img[(variable_def > 0) & (variable_def < 3.14 / 4)] = (0, 0, 1)
plt.imshow(img, interpolation='bilinear')