from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import make_scorer



# TODO: Make a copy of the DataFrame, using the 'drop' function to drop the given feature
new_data = data.drop("Fresh", axis=1)
# TODO: Split the data into training and testing sets(0.25) using the given feature as the target
# Set a random state.
X_train, X_test, y_train, y_test = train_test_split(data, new_data, test_size = 0.25, random_state = 34)



# TODO: Create a decision tree regressor and fit it to the training set
regressor = DecisionTreeRegressor()
regressor_fit = regressor.fit(X_train, y_train)

# TODO: Report the score of the prediction using the testing set
score = regressor.score(X_test, y_test)
print(score)