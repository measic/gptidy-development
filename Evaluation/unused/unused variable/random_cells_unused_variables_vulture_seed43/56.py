# Re-run the model with the Bib numbers as a feature and for the 5K split times to predict 10K time

### set up data for modeling
X_10K = boston_clean[['Bib', 'Age','Official Time Duration', 'F', 'M', 'Temp (F)', '5K Duration']]
y_10K = boston_clean['10K Duration'].values.reshape(-1, 1)
print(X_10K.shape, y_10K.shape)

# split the data into test and train subsets

from sklearn.model_selection import train_test_split

X_train_10K, X_test_10K, y_train_10K, y_test_10K = train_test_split(X_10K, y_10K, random_state=29)
# X_train_5K.head()

# Create a linear regression model and fit it to the training data

from sklearn.linear_model import LinearRegression
model_10K = LinearRegression()
model_10K.fit(X_train_10K, y_train_10K)

# Make predictions

predictions_10K = model_10K.predict(X_test_10K)

# Plot the residuals

plt.scatter(model_10K.predict(X_train_10K), model_10K.predict(X_train_10K) - y_train_10K, c="blue", label="Training Data")
plt.scatter(model_10K.predict(X_test_10K), model_10K.predict(X_test_10K) - y_test_10K, c="orange", label="Testing Data")
plt.legend()
plt.hlines(y=0, xmin=y_test_10K.min(), xmax=y_test_10K.max())
plt.title("Residual Plot 10K")
plt.savefig('model_10k.png')
plt.show()
