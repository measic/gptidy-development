from my_model_selectors import SelectorDIC
training = asl.build_training(features_ground)
sequences = training.get_all_sequences()
variable_def = training.get_all_Xlengths()
for word in words_to_train:
    start = timeit.default_timer()
    model = SelectorDIC(sequences, variable_def, word, min_n_components=2, max_n_components=15, random_state=14).select()
    end = timeit.default_timer() - start
    if model is not None:
        print('Training complete for {} with {} states with time {} seconds'.format(word, model.n_components, end))
    else:
        print('Training failed for {}'.format(word))