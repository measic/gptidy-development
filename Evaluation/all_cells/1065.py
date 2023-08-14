x, y = util.get_sample_classification_data()
x_new = np.linspace(-15, 15, 100)
util.scatter_raw_data_classification(x, y, y_label = "Class")