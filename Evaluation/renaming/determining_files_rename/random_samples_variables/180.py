from sklearn.ensemble import AdaBoostClassifier
variable_def = AdaBoostClassifier(random_state=42)
model = variable_def.fit(X_train, y_train)
importances = model.feature_importances_
vs.feature_plot(importances, X_train, y_train)