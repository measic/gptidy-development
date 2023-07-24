params_list = []
for key, value in best_model.params.iteritems():
    params_list.append(str(key)+" = "+str(value['actual']))
params_list