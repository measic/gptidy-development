variable_def = 'CHOCOLATE'
model, logL = train_a_word(variable_def, 3, features_ground)
show_model_stats(variable_def, model)
print('logL = {}'.format(logL))