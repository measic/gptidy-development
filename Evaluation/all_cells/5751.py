training_acc_file = 'accuracies/train_acc_list.p'
valid_acc_file = 'accuracies/valid_acc_list.p'

with open(training_acc_file, mode='rb') as f:
    combined_train_acc_list = pickle.load(f)
with open(valid_acc_file, mode='rb') as f:
    combined_valid_acc_list = pickle.load(f)
    
all_acc = np.row_stack([combined_train_acc_list, combined_valid_acc_list[0]])