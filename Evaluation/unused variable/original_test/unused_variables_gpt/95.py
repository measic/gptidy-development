plt.scatter(boston_residuals_df['boston_models'], boston_r2, c="blue", label="R2")
plt.title("R2 for each model")
plt.savefig('R2.png')
plt.show()