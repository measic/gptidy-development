# Re-run the model with the Bib numbers as a feature and for the 5K, 10K and 15K split times to predict 20K time

### set up data for modeling
X_20K = boston_clean[['Bib', 'Age','Official Time Duration', 'F', 'M', 'Temp (F)', '5K Duration', '10K Duration', '15K Duration']]
y_20K = boston_clean['20K Duration'].values.reshape(-1, 1)
print(X_20K.shape, y_20K.shape)

# split the data into test and train subsets

from sklearn.model_selection import train_test_split

X_train_20K, X_test_20K, y_train_20K, y_test_20K = train_test_split(X_20K, y_20K, random_state=29)
# X_train_20K.head()

# Create a linear regression model and fit it to the training data

from sklearn.linear_model import LinearRegression
model_20K = LinearRegression()
model_20K.fit(X_train_20K, y_train_20K)

# Make predictions

predictions_20K = model_20K.predict(X_test_20K)

# Plot the residuals

plt.scatter(model_20K.predict(X_train_20K), model_20K.predict(X_train_20K) - y_train_20K, c="blue", label="Training Data")
plt.scatter(model_20K.predict(X_test_20K), model_20K.predict(X_test_20K) - y_test_20K, c="orange", label="Testing Data")
plt.legend()
plt.hlines(y=0, xmin=y_test_20K.min(), xmax=y_test_20K.max())
plt.title("Residual Plot 20K")
plt.savefig('model_20k.png')
plt.show()
