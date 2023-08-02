from sklearn.metrics import fbeta_score, accuracy_score
beta = 0.5

def train_predict(learner, sample_size, X_train, y_train, X_test, y_test):
    """
    inputs:
       - learner: the learning algorithm to be trained and predicted on
       - sample_size: the size of samples (number) to be drawn from training set
       - X_train: features training set
       - y_train: income training set
       - X_test: features testing set
       - y_test: income testing set
    """
    variable_def = {}
    start = time()
    learner = learner.fit(X_train[:sample_size], y_train[:sample_size])
    end = time()
    variable_def['train_time'] = end - start
    start = time()
    predictions_test = learner.predict(X_test)
    predictions_train = learner.predict(X_train[:300])
    end = time()
    variable_def['pred_time'] = end - start
    variable_def['acc_train'] = accuracy_score(y_train[:300], predictions_train)
    variable_def['acc_test'] = accuracy_score(y_test, predictions_test)
    variable_def['f_train'] = fbeta_score(y_train[:300], predictions_train, beta)
    variable_def['f_test'] = fbeta_score(y_test, predictions_test, beta)
    print('{} trained on {} samples.'.format(learner.__class__.__name__, sample_size))
    return variable_def