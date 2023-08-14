variable_def, x = np.indices((600, 800))
img[(x - 450) ** 2 + (variable_def - 350) ** 2 < 50 ** 2] = (1, 0, 0)
plt.imshow(img, interpolation='bilinear')