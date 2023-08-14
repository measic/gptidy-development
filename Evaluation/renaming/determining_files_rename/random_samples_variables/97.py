import pickle
training_file = '../traffic-signs-data/train.p'
validation_file = '../traffic-signs-data/valid.p'
testing_file = '../traffic-signs-data/test.p'
with open(training_file, mode='rb') as f:
    train = pickle.load(f)
with open(validation_file, mode='rb') as f:
    valid = pickle.load(f)
with open(testing_file, mode='rb') as f:
    test = pickle.load(f)
variable_def, y_train = (train['features'], train['labels'])
X_valid, y_valid = (valid['features'], valid['labels'])
X_test, y_test = (test['features'], test['labels'])