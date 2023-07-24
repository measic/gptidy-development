# Re-run the model with the Bib numbers as a feature and for the 5K, 10K 15K 20K and Half split times to predict 25K time

### set up data for modeling
X_25K = boston_clean[['Bib', 'Age','Official Time Duration', 'F', 'M', 'Temp (F)', '5K Duration', '10K Duration', '15K Duration', '20K Duration', 'Half Duration']]
y_25K = boston_clean['25K Duration'].values.reshape(-1, 1)
print(X_25K.shape, y_25K.shape)

# split the data into test and train subsets

from sklearn.model_selection import train_test_split

X_train_25K, X_test_25K, y_train_25K, y_test_25K = train_test_split(X_25K, y_25K, random_state=29)
# X_train_25K.head()

# Create a linear regression model and fit it to the training data

from sklearn.linear_model import LinearRegression
model_25K = LinearRegression()
model_25K.fit(X_train_25K, y_train_25K)

# Make predictions

predictions_25K = model_25K.predict(X_test_25K)

# Plot the residuals

plt.scatter(model_25K.predict(X_train_25K), model_25K.predict(X_train_25K) - y_train_25K, c="blue", label="Training Data")
plt.scatter(model_25K.predict(X_test_25K), model_25K.predict(X_test_25K) - y_test_25K, c="orange", label="Testing Data")
plt.legend()
plt.hlines(y=0, xmin=y_test_25K.min(), xmax=y_test_25K.max())
plt.title("Residual Plot 25K")
plt.savefig('model_25k.png')
plt.show()
