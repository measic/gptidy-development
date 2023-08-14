from sklearn.ensemble import AdaBoostClassifier
ada_clf = AdaBoostClassifier(random_state=42)
variable_def = ada_clf.fit(X_train, y_train)
importances = variable_def.feature_importances_
vs.feature_plot(importances, X_train, y_train)