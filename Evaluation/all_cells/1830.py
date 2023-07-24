#Reset train/test split with pred
data_dog = data[data['AnimalType'] == 'Dog']
data_cat = data[data['AnimalType'] == 'Cat']
X_dog = data_dog[pred['dog']]
X_cat = data_cat[pred['cat']]
y_dog = data_dog[[target]]
y_cat = data_cat[[target]]
X_dog_train, X_dog_dev, y_dog_train, y_dog_dev = train_test_split(X_dog, y_dog, random_state=2)
X_cat_train, X_cat_dev, y_cat_train, y_cat_dev = train_test_split(X_cat, y_cat, random_state=2)
