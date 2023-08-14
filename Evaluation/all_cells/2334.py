fpr, tpr, _ = roc_curve(y_test, prediction[:,1])
plt.plot(fpr, tpr);