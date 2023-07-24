# Re-run the model with the Bib numbers as a feature and for the 5K and 10K split times to predict 15K time

### set up data for modeling
X_15K = boston_clean[['Bib', 'Age','Official Time Duration', 'F', 'M', 'Temp (F)', '5K Duration', '10K Duration']]
y_15K = boston_clean['15K Duration'].values.reshape(-1, 1)
print(X_15K.shape, y_15K.shape)

# split the data into test and train subsets

from sklearn.model_selection import train_test_split

X_train_15K, X_test_15K, y_train_15K, y_test_15K = train_test_split(X_15K, y_15K, random_state=29)
# X_train_15K.head()

# Create a linear regression model and fit it to the training data

from sklearn.linear_model import LinearRegression
model_15K = LinearRegression()
model_15K.fit(X_train_15K, y_train_15K)

# Make predictions

predictions_15K = model_15K.predict(X_test_15K)

# Plot the residuals

plt.scatter(model_15K.predict(X_train_15K), model_15K.predict(X_train_15K) - y_train_15K, c="blue", label="Training Data")
plt.scatter(model_15K.predict(X_test_15K), model_15K.predict(X_test_15K) - y_test_15K, c="orange", label="Testing Data")
plt.legend()
plt.hlines(y=0, xmin=y_test_15K.min(), xmax=y_test_15K.max())
plt.title("Residual Plot 15K")
plt.savefig('model_15k.png')
plt.show()
