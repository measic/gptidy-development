min_acc = best_acc['Acc_valid'].min()
max_acc = best_acc['Acc_valid'].max()

# Plot best accuracy v.s. beta
min_beta = np.log10(best_acc['Beta']).min() 
max_beta = np.log10(best_acc['Beta']).max() 

fig = plt.figure(1)
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.plot(np.log10(best_acc["Beta"]), best_acc["Acc_valid"], 'ro')
#axes = plt.gca()
ax1.set_xlim( [min_beta,max_beta])
ax1.set_ylim([min_acc, max_acc])
ax1.set_xlabel('Log Beta')

# Plot best accuracy v.s. learning_rate
min_lr = np.log10(best_acc['Learning_Rate']).min() 
max_lr = np.log10(best_acc['Learning_Rate']).max() 

#ig, ax = plt.subplots(1,1); 
ax2.plot(np.log10(best_acc["Learning_Rate"]), best_acc["Acc_valid"], 'ro')
ax2.set_xlim( [min_lr,max_lr])
ax2.set_ylim([min_acc, max_acc])
ax2.set_xlabel('Log Learning Rate')

ax1.set_ylabel('Log Accuracy Validation set')

plt.show()