# remove class
n_classes = 9
classes_to_keep = np.asarray([x for x in range(1, n_classes)])

names_keep = np.asarray(names)
names_keep = names_keep.tolist()
print("classes to keep: " + str(names_keep))