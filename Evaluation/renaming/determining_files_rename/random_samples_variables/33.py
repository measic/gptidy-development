my_testword = 'CHOCOLATE'
model, variable_def = train_a_word(my_testword, 3, features_ground)
show_model_stats(my_testword, model)
print('logL = {}'.format(variable_def))