# Re-run the model with the Bib numbers as a feature and for the 5K, 10K 15K 20K 25K half and 30K split times to predict 35K time

### set up data for modeling
X_35K = boston_clean[['Bib', 'Age','Official Time Duration', 'F', 'M', 'Temp (F)', '5K Duration', '10K Duration', '15K Duration', '20K Duration', 'Half Duration','25K Duration',  '30K Duration']]
y_35K = boston_clean['35K Duration'].values.reshape(-1, 1)
print(X_30K.shape, y_30K.shape)

# split the data into test and train subsets

from sklearn.model_selection import train_test_split

X_train_35K, X_test_35K, y_train_35K, y_test_35K = train_test_split(X_35K, y_35K, random_state=29)
# X_train_30K.head()

# Create a linear regression model and fit it to the training data

from sklearn.linear_model import LinearRegression
model_35K = LinearRegression()
model_35K.fit(X_train_35K, y_train_35K)

# Make predictions

predictions_35K = model_35K.predict(X_test_35K)

# Plot the residuals

plt.scatter(model_35K.predict(X_train_35K), model_35K.predict(X_train_35K) - y_train_35K, c="blue", label="Training Data")
plt.scatter(model_35K.predict(X_test_35K), model_35K.predict(X_test_35K) - y_test_35K, c="orange", label="Testing Data")
plt.legend()
plt.hlines(y=0, xmin=y_test_35K.min(), xmax=y_test_35K.max())
plt.title("Residual Plot 35K")
plt.savefig('model_35k.png')
plt.show()
