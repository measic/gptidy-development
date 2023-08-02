from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score

def function_def(X, y):
    """ 
    Shuffles and splits data into 75% training and 25% testing subsets,
    then returns the training and testing subsets.
    :param X: numpy array. Features
    :param y: numpy array. Labels
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
    return (X_train, y_train, X_test, y_test)
l_score = []
for s_col in data.columns:
    new_data = data.copy()
    y = new_data[s_col]
    X = new_data.drop([s_col], axis=1)
    X_train, y_train, X_test, y_test = function_def(X, y)
    regressor = DecisionTreeRegressor(random_state=0)
    regressor.fit(X_train, y_train)
    score = r2_score(regressor.predict(X_test), y_test)
    l_score.append(score)
df_r2 = pd.DataFrame(l_score, index=data.columns, columns=['Score'])
df_r2.index.names = ['PREDICTED']
df_r2