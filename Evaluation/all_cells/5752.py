best_acc_matrix = best_acc[["Beta","Learning_Rate","Acc_valid"]]

best_acc_matrix["log_beta"] = np.log10(best_acc_matrix["Beta"])
best_acc_matrix["log_learning_rate"] = np.log10(best_acc["Learning_Rate"])

cm = plt.cm.get_cmap('hot')
plt.scatter(x=np.log10(best_acc["Beta"]), y=np.log10(best_acc["Learning_Rate"]), 
            c=-best_acc["Acc_valid"],s=100*best_acc["Acc_valid"],
            cmap=cm)
plt.xlim( [-8,0])
plt.ylim( [-8,0])
plt.xlabel('Log Beta')
plt.ylabel('Log Learning Rate')

row_iterator = best_acc_matrix.iterrows()
_, last = next(row_iterator)  
for i, row in row_iterator:
    plt.annotate(round(100*row["Acc_valid"],1), (row["log_beta"]+0.08,row["log_learning_rate"]+0.08),
                fontsize=8)

plt.title("Validation accuracy after 9 epochs \nfor different regularization parameter and learning rates")
plt.show()
