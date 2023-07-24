# Plot the residuals of each model

plt.scatter(boston_residuals_df['boston_models'], boston_mse, c="red", label="MSE")

# plt.scatter(model_Final.predict(X_test_Final), model_Final.predict(X_test_Final) - y_test_Final, c="orange", label="Testing Data")
# plt.legend()
# plt.hlines(y=0, xmin=y_test_Final.min(), xmax=y_test_Final.max())
plt.title("Mean Square Error for each model")
plt.savefig('MSE.png')
plt.show()
