for model_name, model in [('shake_lstm', model_lstm), ('shake_gru', model_gru)]:
    print("MODEL: ", model_name)
    
    full_test(model, hypothesis_capswords, 'Capitalized Words',
              train_len=95, test_len=5, ex_name='{}_capswords'.format(model_name))
    full_test(model, hypothesis_nouns, 'Nouns',
              train_len=95, test_len=5, ex_name='{}_nouns'.format(model_name))
    full_test(model, hypothesis_verbs, 'Verbs',
              train_len=95, test_len=5, ex_name='{}_verbs'.format(model_name))