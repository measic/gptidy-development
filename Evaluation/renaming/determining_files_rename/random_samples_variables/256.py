variable_def = '../test_dataset/IMG/*'
img_list = glob.glob(variable_def)
idx = np.random.randint(0, len(img_list) - 1)
image = mpimg.imread(img_list[idx])
plt.imshow(image)