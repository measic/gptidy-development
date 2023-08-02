img[...] = 0
X = (x - 400) / 30
variable_def = -(y - 300) / 30
heart = X ** 2 + (variable_def - 2 * (X ** 2 + np.abs(X) - 6) / (3 * (X ** 2 + np.abs(X) + 2))) ** 2 < 36
img[heart] = (1, 0, 0)
plt.imshow(img, interpolation='bilinear')