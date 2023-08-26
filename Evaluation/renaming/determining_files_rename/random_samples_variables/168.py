img[...] = 0
variable_def = (x - 400) / 30
Y = -(y - 300) / 30
heart = variable_def ** 2 + (Y - 2 * (variable_def ** 2 + np.abs(variable_def) - 6) / (3 * (variable_def ** 2 + np.abs(variable_def) + 2))) ** 2 < 36
img[heart] = (1, 0, 0)
plt.imshow(img, interpolation='bilinear')