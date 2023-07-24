def get_name_ext(timestr, beta, learning_rate, learn_decay, separator = '_'):
    return timestr + separator + str(beta) + separator + str(learning_rate) + separator + str(learn_decay)

def combine_acc_lists(beta, lr, ld, acc_list_temp, acc_list):
    length_acc_list_temp = len(acc_list_temp)
    beta_list = [beta] * length_acc_list_temp
    lr_list = [lr] * length_acc_list_temp
    ld_list = [ld] * length_acc_list_temp
    t = np.vstack((np.asarray(acc_list_temp),beta_list,lr_list,ld_list))
    
    if(acc_list is None):
        acc_list = t
    else:
        acc_list = np.concatenate((acc_list, t), axis = 1)
    
    return acc_list