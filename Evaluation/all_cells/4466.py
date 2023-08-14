import numpy as np
from xgboost import XGBClassifier
from sklearn.datasets import fetch_mldata
mnist = fetch_mldata('MNIST original')

X, y = mnist["data"], mnist["target"]
shuffle_index = np.random.permutation(70000)
X, y = X[shuffle_index], y[shuffle_index]
X_train60, X_test, y_train60, y_test = X[:60000], X[60000:], y[:60000], y[60000:]
X_train, y_train = X_train60[:5000], y_train60[:5000]