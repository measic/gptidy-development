unique, counts = np.unique(y_train, return_counts=True)
unique_test, counts_test = np.unique(y_test, return_counts=True)

#print(dict(zip(unique, counts)))
plt.hist(y_train, color = 'b', label = 'train', normed = True, bins=range(n_classes+1))
plt.title('New distribution of the number of images per class \n for train set')
plt.xlabel('Class')
plt.ylabel('Percentage of images')
plt.show()
