img[...] = 0
variable_def = (x - 400) / 30
Y = -(y - 300) / 30
R = np.sqrt(variable_def ** 2 + Y ** 2)
t = np.arctan2(Y, variable_def)
img[R < 5] = (1, 0, 0)
img[(t > 0) & (t < 3.14 / 4)] = (0, 0, 1)
plt.imshow(img, interpolation='bilinear')