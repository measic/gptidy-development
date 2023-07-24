# TODO: Make a copy of the DataFrame, using the 'drop' function to drop the given feature
new_data = data.copy()
column_to_study = 'Grocery'
X_all = new_data.drop(column_to_study, axis=1)
y_all = data[column_to_study]

# TODO: Split the data into training and testing sets using the given feature as the target
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_all, y_all, test_size=0.25, random_state=10)

# TODO: Create a decision tree regressor and fit it to the training set
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state=10)
regressor = regressor.fit(X_train, y_train)

# TODO: Report the score of the prediction using the testing set
score = regressor.score(X_test, y_test)
print(score)