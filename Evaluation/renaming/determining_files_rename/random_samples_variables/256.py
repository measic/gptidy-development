path = '../test_dataset/IMG/*'
variable_def = glob.glob(path)
idx = np.random.randint(0, len(variable_def) - 1)
image = mpimg.imread(variable_def[idx])
plt.imshow(image)