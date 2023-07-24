from sklearn.model_selection import KFold

training = asl.build_training(features_ground)  # Experiment here with different feature sets
word = 'VEGETABLE'  # Experiment here with different words
word_sequences = training.get_word_sequences(word)
split_method = KFold()
for cv_train_idx, cv_test_idx in split_method.split(word_sequences):
    print("Train fold indices: {} Test fold indices: {}".format(cv_train_idx, cv_test_idx))  # view indices of the folds