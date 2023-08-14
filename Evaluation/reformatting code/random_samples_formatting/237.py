from sklearn.model_selection import train_test_split

X_train_5K, X_test_5K, y_train_5K, y_test_5K = train_test_split(X_5K, y_5K, random_state=29)

X_train_5K.head()