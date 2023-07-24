# Find the best accuracy for the parameters:
idx = acc.groupby(['Group'])['Acc_valid'].transform(max) == acc['Acc_valid']
best_acc = acc[idx]