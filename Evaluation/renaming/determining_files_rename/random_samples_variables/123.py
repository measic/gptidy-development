my_testword = 'CHOCOLATE'
variable_def, logL = train_a_word(my_testword, 3, features_ground)
show_model_stats(my_testword, variable_def)
print('logL = {}'.format(logL))