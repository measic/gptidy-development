# Selecting certian numerical features
X_select = X_Num_Cov[space]
# Dropping the missing values from the feature space
X_select = X_select.dropna()
# Creating the output space
Y = X_select['reviews_per_month']
X_select = X_select.drop(['reviews_per_month'], axis=1)
print(X_select.info())
X_select.head()