# This part was used for hyper-parameter search as well
EPOCHS = 80
BATCH_SIZE = 128
RELOAD_MODEL = False
HYPER_PARAM_SEARCH_ITERATIONS = 1 #5

timestr = time.strftime("%Y%m%d-%H%M%S"); print(timestr);

for i in range(HYPER_PARAM_SEARCH_ITERATIONS):

    #LEARNING_RATE = 10 ** np.random.uniform(low = -5, high = -2, size = 1)[0]
    #BETA = 10 ** np.random.uniform(low = -7, high = -3, size = 1)[0]
    
    LEARNING_RATE = 10 ** (-3) #10 ** np.random.uniform(low = -5, high = -3, size = 1)[0]
    BETA = 10**(-6) #10 ** np.random.uniform(low = -6, high = -3, size = 1)[0]
    
    for LEARN_DECAY in [True]: #False, True]
    
        # Remove the previous weights and bias
        tf.reset_default_graph()
        # Rebuild graph
        tf_train_dataset, tf_train_labels, tf_train_labels_cls, tf_beta, tf_keep_prob, tf_learning_rate, weights, biases,conv1, conv2, conv3, flat, fc1, fc2, logits, train_prediction, regularizers,  cross_entropy, loss, optimizer, labels_pred_cls, correct_prediction, accuracy_operation, accuracy_operation, summary_op  = define_graph()

        print('------------------------------------------------')
        print('beta:',BETA, ' / ', 'learning rate:', LEARNING_RATE, ' / ', 'learn decay:', LEARN_DECAY)
        print('------------------------------------------------')

        name_ext = get_name_ext(timestr=timestr, beta=BETA, learning_rate = LEARNING_RATE, learn_decay = LEARN_DECAY)

        train_acc_list_, valid_acc_list_ = train_model(beta = BETA
                                                       , lr = LEARNING_RATE
                                                       , name_ext = name_ext
                                                       , learn_decay = LEARN_DECAY)
                
        # saving for hyperparemeter search:
        #combined_train_acc_list = combine_acc_lists(beta = BETA, lr = LEARNING_RATE, ld = LEARN_DECAY, acc_list_temp = train_acc_list_, acc_list = combined_train_acc_list)
        #combined_valid_acc_list = combine_acc_lists(beta = BETA, lr = LEARNING_RATE, ld = LEARN_DECAY, acc_list_temp = valid_acc_list_, acc_list = combined_valid_acc_list)
        
        #pickle.dump( combined_train_acc_list, open( "accuracies/train_acc_list.p", "wb" ) )
        #pickle.dump( combined_valid_acc_list, open( "accuracies/valid_acc_list.p", "wb" ) )