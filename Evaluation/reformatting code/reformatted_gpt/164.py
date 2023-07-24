# Find the best regularization strength
# Generate logistic regression
def logit_reg(X_train, X_dev, y_train, y_dev, predict_anim):
    logit_reg = LogisticRegression(penalty="l2", multi_class='multinomial', solver='newton-cg')
    print(X_train.shape)
    print(type(pd.Series(y_train)))
    y_train = y_train.values.ravel()
    y_dev = y_dev.values.ravel()

    # Test C within [0.001, 10]
    param_domain = [0.001, 0.01, 0.1, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 5.0, 10.0]
    param_dict = dict(C=param_domain)
    print(param_dict)

    # Initialize GridSearchCV to identify the optimal parameter values
    gridsearch = GridSearchCV(logit_reg, param_dict)
    gridsearch.fit(X_train, y_train)

    # Generate model at the best C value
    C = gridsearch.best_params_["C"]
    print("Train data: Logistic Regression score at C=%.3f: %f" % (C, gridsearch.best_score_))
    print('\n' * 1)
    logit_reg = LogisticRegression(C=C, penalty="l2")
    logit_reg.fit(X_train, y_train)

    # Predict on the X_dev set
    logit_reg_dev = logit_reg.predict(X_dev)

    # Generate classification report
    print("Classification Report:")
    print(" ")
    print(classification_report(y_dev, logit_reg_dev, target_names=logit_reg.classes_))
    print("Dev data: Logistic Regression score at C=%.3f: %f" % (C, metrics.f1_score(y_dev, logit_reg_dev, average="weighted")))
    print("Weights:")
    # Get the variables with the highest weights for each outcome
    print(logit_reg.classes_)
    weights = []
    for i in range(len(logit_reg.classes_)):
        top_vars = np.argsort(logit_reg.coef_[i])[-6:-1]
        print(logit_reg.classes_[i])
        for j in top_vars:
            print(predict_anim[j], round(logit_reg.coef_[i][j], 3))
        print
    print('\n' * 2)

    # Generate logistic regression and add the squared weight values to an array, at each C
    logit_reg_coeff = []
    for c in param_domain:
        logit_reg = LogisticRegression(C=c, penalty="l2")
        logit_reg.fit(X_train, y_train)
        squared_weights = []
        squared_weights.append(c)
        for i in range(0, 4):
            squared_weights.append(np.sum(np.power(logit_reg.coef_[i], 2)))
        logit_reg_coeff.append(squared_weights)

    coeff = np.asarray(logit_reg_coeff, dtype="object")


print('Logistic Regression: Dogs Only')
logit_reg(X_dog_train, X_dog_dev, y_dog_train, y_dog_dev, predictors_dog)
print('Logistic Regression: Cats Only')
logit_reg(X_cat_train, X_cat_dev, y_cat_train, y_cat_dev, predictors_cat)