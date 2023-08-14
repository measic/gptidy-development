# import libraries needed
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score

# define help functions
def shuffle_split_data(X, y):
    """ 
    Shuffles and splits data into 75% training and 25% testing subsets,
    then returns the training and testing subsets.
    :param X: numpy array. Features
    :param y: numpy array. Labels
    """
    # Shuffle and split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25,
                                                        random_state=0)
    # Return the training and testing data subsets
    return X_train, y_train, X_test, y_test

l_score = []
for s_col in data.columns:
    # TODO: Make a copy of the DataFrame, using the 'drop' function to drop the
    # given feature
    new_data = data.copy()
    y = new_data[s_col]
    X = new_data.drop([s_col], axis=1)

    # TODO: Split the data into training and testing sets using the given feature
    # as the target
    X_train ,y_train, X_test, y_test = shuffle_split_data(X, y)

    # TODO: Create a decision tree regressor and fit it to the training set
    regressor = DecisionTreeRegressor(random_state=0)
    regressor.fit(X_train, y_train)

    # TODO: Report the score of the prediction using the testing set
    score = r2_score(regressor.predict(X_test), y_test)
    l_score.append(score)
    
df_r2 = pd.DataFrame(l_score, index = data.columns, columns=["Score"])
df_r2.index.names = ["PREDICTED"]
df_r2