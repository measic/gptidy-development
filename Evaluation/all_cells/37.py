plt.scatter(X.numpy(), y.numpy()); # Original datapoints
plt.plot(X_best_fit, preds_best_fit.numpy(), color='k',
         linewidth=6, label='$R^2$ score: %.2f' %r2_score) # Our predictions
plt.xlabel('Input', fontsize=15);
plt.ylabel('Target', fontsize=15);
plt.title('Toy regression problem', fontsize=15);
plt.legend(fontsize=15);