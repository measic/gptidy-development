#artifacts have a pointer (filename), internal name, and (optional) parent
X_train = ex.artifact('x_train.npz', 'X_train', do_split)
X_test = ex.artifact('x_test.npz', 'X_test', do_split)
y_train = ex.artifact('y_train.json', 'y_train', do_split)
y_test = ex.artifact('y_test.json', 'y_test', do_split)