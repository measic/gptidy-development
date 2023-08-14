import pyprind
pbar = pyprind.ProgBar(45)
classes = np.array([0, 1])
for _ in range(45):
    variable_def, y_train = get_minibatch(doc_stream, size=1000)
    if not variable_def:
        break
    variable_def = vect.transform(variable_def)
    clf.partial_fit(variable_def, y_train, classes=classes)
    pbar.update()