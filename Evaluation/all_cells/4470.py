from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier

rf = RandomForestClassifier()
sgd = SGDClassifier()

rf.fit(X_train, y_train)
sgd.fit(X_train, y_train)