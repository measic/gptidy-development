train_acc_list_ = 'train_acc_list_.p'
valid_acc_list_ = 'valid_acc_list_.p'

with open(train_acc_list_, mode='rb') as f:
    train_acc_list_ = pickle.load(f)
with open(valid_acc_list_, mode='rb') as f:
    valid_acc_list_ = pickle.load(f)

plt.plot(train_acc_list_)
plt.plot(valid_acc_list_)
plt.title('accuracy for training and validation set by epoch')