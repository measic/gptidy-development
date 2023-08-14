from my_model_selectors import SelectorDIC
variable_def = asl.build_training(features_ground)
sequences = variable_def.get_all_sequences()
Xlengths = variable_def.get_all_Xlengths()
for word in words_to_train:
    start = timeit.default_timer()
    model = SelectorDIC(sequences, Xlengths, word, min_n_components=2, max_n_components=15, random_state=14).select()
    end = timeit.default_timer() - start
    if model is not None:
        print('Training complete for {} with {} states with time {} seconds'.format(word, model.n_components, end))
    else:
        print('Training failed for {}'.format(word))