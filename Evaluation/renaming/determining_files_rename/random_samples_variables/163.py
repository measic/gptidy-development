y, x = np.indices((600, 800))
variable_def[(x - 450) ** 2 + (y - 350) ** 2 < 50 ** 2] = (1, 0, 0)
plt.imshow(variable_def, interpolation='bilinear')