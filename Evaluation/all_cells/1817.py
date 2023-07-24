#Turn categorical variables into binaries, eliminating unconverted columns
data2_dog = pd.concat([data[target], data[continuous['dog']], pd.get_dummies(data[discrete['dog']])], axis=1)
data2_cat = pd.concat([data[target], data[continuous['cat']], pd.get_dummies(data[discrete['cat']])], axis=1)
print data2_dog.shape
print data2_cat.shape