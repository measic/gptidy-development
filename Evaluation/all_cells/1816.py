#Split the data into cat and dog data sets
data2_dog = pd.concat([data[target], data[continuous['dog']], pd.get_dummies(data[discrete['dog']])], axis=1)
data2_cat = pd.concat([data[target], data[continuous['cat']], pd.get_dummies(data[discrete['cat']])], axis=1)

discrete_dog = ['AnimalType_Cat', 'AnimalType_Dog', 'Female_Female', 'Female_Male', 'Female_Unknown',
           'Intact_Intact', 'Intact_Spayed/Neutered', 'Intact_Unknown', 'MixedBreed_Known Breed Combo',
           'MixedBreed_Mixed Breed', 'MixedBreed_Nonmixed', 'Named_Named', 'Named_Unnamed', 'TopBreed', 'PitBull']

discrete_cat = ['AnimalType_Cat', 'AnimalType_Dog', 'Female_Female', 'Female_Male', 'Female_Unknown',
           'Intact_Intact', 'Intact_Spayed/Neutered', 'Intact_Unknown', 'MixedBreed_Known Breed Combo',
           'MixedBreed_Mixed Breed', 'MixedBreed_Nonmixed', 'Named_Named', 'Named_Unnamed', 'BlackCat']

predictors_dog = continuous['dog'] + discrete_dog
predictors_cat = continuous['cat'] + discrete_cat

# Train/test split
X_dog = data2_dog[data2_dog['AnimalType_Dog'] == 1][predictors_dog]
y_dog = data2_dog[data2_dog['AnimalType_Dog'] == 1][[target]]
X_dog_train, X_dog_dev, y_dog_train, y_dog_dev = train_test_split(X_dog, y_dog, random_state=2)

X_cat = data2_cat[data2_cat['AnimalType_Cat'] == 1][predictors_cat]
y_cat = data2_cat[data2_cat['AnimalType_Cat'] == 1][[target]]
X_cat_train, X_cat_dev, y_cat_train, y_cat_dev = train_test_split(X_cat, y_cat, random_state=2)

#Normalize 
ss_dog = StandardScaler()
ss_dog.fit(X_dog_train[continuous['dog']])   # Compute mean and std of training data
X_dog_train[continuous['dog']] = ss_dog.transform(X_dog_train[continuous['dog']])  # Use that mean and std to normalize columns of training data
X_dog_dev[continuous['dog']] = ss_dog.transform(X_dog_dev[continuous['dog']]) 
print X_dog.shape

ss_cat = StandardScaler()
ss_cat.fit(X_cat_train[continuous['cat']])   # Compute mean and std of training data
X_cat_train[continuous['cat']] = ss_cat.transform(X_cat_train[continuous['cat']])  # Use that mean and std to normalize columns of training data
X_cat_dev[continuous['cat']] = ss_cat.transform(X_cat_dev[continuous['cat']]) 
print X_cat.shape