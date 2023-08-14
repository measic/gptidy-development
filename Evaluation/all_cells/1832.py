#Full pipelines, using the best regularization strengths for the dog and cat models, respectively
pipeline_dog = Pipeline([('Preprocess', FeatureUnion([('Discrete', discrete_pipe_dog), ('Continuous', continuous_pipe_dog)])),
                      ('Predict', LogisticRegression(multi_class='multinomial', C=0.25, solver='newton-cg'))])
pipeline_cat = Pipeline([('Preprocess', FeatureUnion([('Discrete', discrete_pipe_cat), ('Continuous', continuous_pipe_cat)])),
                      ('Predict', LogisticRegression(multi_class='multinomial', C=0.10, solver='newton-cg'))])

#Fit the multinomial logistic regression for dogs and cats, respectively
test_dog_lr = pipeline_dog.fit(X_dog_train, y_dog_train)
test_cat_lr = pipeline_cat.fit(X_cat_train, y_cat_train)

print "Dogs: Multinomial Logistic Regression Train Accuracy :: ", metrics.accuracy_score(y_dog_train, test_dog_lr.predict(X_dog_train))
print "Dogs: Multinomial Logistic Regression Dev Accuracy :: ", metrics.accuracy_score(y_dog_dev, test_dog_lr.predict(X_dog_dev))
print
print "Cats: Multinomial Logistic Regression Train Accuracy :: ", metrics.accuracy_score(y_cat_train, test_cat_lr.predict(X_cat_train))
print "Cats: Multinomial Logistic Regression Dev Accuracy :: ", metrics.accuracy_score(y_cat_dev, test_cat_lr.predict(X_cat_dev))