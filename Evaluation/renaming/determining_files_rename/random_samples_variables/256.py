path = '../test_dataset/IMG/*'
img_list = glob.glob(path)
idx = np.random.randint(0, len(img_list) - 1)
variable_def = mpimg.imread(img_list[idx])
plt.imshow(variable_def)