# One-hot encode the 'features_raw' data using pandas.get_dummies()
features = pd.get_dummies(features_raw)

# Encode the 'income_raw' data to numerical values. Here, "0" is less or equal 50k, "1" is more.
income = pd.get_dummies(income_raw)['>50K']

# Print the number of features after one-hot encoding
encoded = list(features.columns)
print "{} total features after one-hot encoding.".format(len(encoded))

#Uncomment the following line to see the encoded feature names
#print encoded
print len(list(features_raw.columns))