## Example of Pasting. Notice the results. 
## If it is possible to do pasting, it would else, it would start repeating
## Pasting is possible is max_samples * n_estimators <= X
X_train1 = np.array([[1, 1],[1, 0], [0, 1], [0,0], [0,0], [0,0]])
y_train1 = np.array([0, 1, 1, 0, 0, 0])
bag_clf1 = BaggingClassifier( 
    DecisionTreeClassifier(), 
    n_estimators=10, 
    max_samples=0.2, 
    bootstrap=True, 
    n_jobs=-1,
    random_state=42
)

bag_clf1.fit(X_train1, y_train1)
#bag_clf1.estimators_samples_