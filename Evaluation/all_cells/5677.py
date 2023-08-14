from sklearn.preprocessing import MultiLabelBinarizer

mlb = MultiLabelBinarizer()
mlb.fit_transform(data['tags'])
print("number of categories in dataset ",len(mlb.classes_))

#data[0:10]
#print(mlb.classes_)