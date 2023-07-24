# Re-run the model with the Bib numbers as a feature and for the 5K, 10K 15K 20K 25K and half split times to predict 30K time

### set up data for modeling
X_30K = boston_clean[['Bib', 'Age','Official Time Duration', 'F', 'M', 'Temp (F)', '5K Duration', '10K Duration', '15K Duration', '20K Duration','Half Duration', '25K Duration']]
y_30K = boston_clean['30K Duration'].values.reshape(-1, 1)
print(X_30K.shape, y_30K.shape)

# split the data into test and train subsets

from sklearn.model_selection import train_test_split

X_train_30K, X_test_30K, y_train_30K, y_test_30K = train_test_split(X_30K, y_30K, random_state=29)
# X_train_30K.head()

# Create a linear regression model and fit it to the training data

from sklearn.linear_model import LinearRegression
model_30K = LinearRegression()
model_30K.fit(X_train_30K, y_train_30K)

# Make predictions

predictions_30K = model_30K.predict(X_test_30K)

# Plot the residuals

plt.scatter(model_30K.predict(X_train_30K), model_30K.predict(X_train_30K) - y_train_30K, c="blue", label="Training Data")
plt.scatter(model_30K.predict(X_test_30K), model_30K.predict(X_test_30K) - y_test_30K, c="orange", label="Testing Data")
plt.legend()
plt.hlines(y=0, xmin=y_test_30K.min(), xmax=y_test_30K.max())
plt.title("Residual Plot 30K")
plt.savefig('model_30k.png')
plt.show()
